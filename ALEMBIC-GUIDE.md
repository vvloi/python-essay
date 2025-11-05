# Alembic Migration Guide (Giống Liquibase)

## 📚 Alembic là gì?

Alembic là công cụ database migration cho Python, tương tự như **Liquibase** trong Java.

### So sánh Liquibase vs Alembic:

| Liquibase | Alembic | Mô tả |
|-----------|---------|-------|
| `<changeSet>` | Migration file | Tập hợp thay đổi |
| `<createTable>` | `op.create_table()` | Tạo bảng |
| `<insert>` | `op.execute("INSERT...")` | Thêm dữ liệu |
| `<dropTable>` | `op.drop_table()` | Xóa bảng |
| `<addColumn>` | `op.add_column()` | Thêm cột |
| `liquibase update` | `alembic upgrade head` | Chạy migrations |
| `liquibase rollback` | `alembic downgrade -1` | Rollback |

---

## 📁 Cấu trúc Migrations

```
alembic/
├── versions/
│   ├── 001_initial_migration.py    # Giống <changeSet id="1">
│   └── 002_seed_sample_data.py     # Giống <changeSet id="2">
├── env.py                           # Cấu hình môi trường
└── script.py.mako                   # Template cho migration mới
```

---

## 🚀 Các lệnh cơ bản

### 1. Chạy tất cả migrations (Giống `liquibase update`)
```powershell
alembic upgrade head
```

**Kết quả:**
- ✅ Tạo tables (migration 001)
- ✅ Insert sample data (migration 002)

### 2. Xem lịch sử migrations (Giống `liquibase history`)
```powershell
alembic history
```

**Output:**
```
001 -> 002 (head), Seed sample data
<base> -> 001, Initial migration - Create recipe book tables
```

### 3. Xem migration hiện tại (Giống `liquibase status`)
```powershell
alembic current
```

### 4. Rollback migration (Giống `liquibase rollback`)
```powershell
# Rollback 1 migration
alembic downgrade -1

# Rollback về version cụ thể
alembic downgrade 001

# Rollback tất cả
alembic downgrade base
```

### 5. Tạo migration mới (Giống tạo changeSet mới)
```powershell
# Tạo migration trống
alembic revision -m "add user table"

# Tạo migration tự động (detect changes từ models)
alembic revision --autogenerate -m "add user table"
```

---

## 📝 Ví dụ Migration File

### Migration 001: Create Tables (Giống Liquibase createTable)

```python
# alembic/versions/001_initial_migration.py

def upgrade():
    # Giống <createTable tableName="recipes">
    op.create_table(
        'recipes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recipes_id'), 'recipes', ['id'])

def downgrade():
    # Giống <rollback>
    op.drop_index(op.f('ix_recipes_id'), table_name='recipes')
    op.drop_table('recipes')
```

### Migration 002: Insert Data (Giống Liquibase insert)

```python
# alembic/versions/002_seed_sample_data.py

def upgrade():
    # Giống <insert tableName="recipes">
    op.execute("""
        INSERT INTO recipes (id, name, cuisine, servings)
        VALUES (1, 'Phở Bò', 'Vietnamese', 4)
    """)

def downgrade():
    # Giống <delete tableName="recipes">
    op.execute("DELETE FROM recipes WHERE id = 1")
```

---

## 🔄 Workflow hoàn chỉnh

### Lần đầu setup database:

```powershell
# 1. Xem các migrations có sẵn
alembic history

# 2. Chạy tất cả migrations
alembic upgrade head

# 3. Kiểm tra database đã được tạo
# File: recipe_book.db sẽ xuất hiện
```

### Khi thêm feature mới (ví dụ: thêm rating cho recipe):

```powershell
# 1. Sửa models.py - thêm column rating
# class Recipe(Base):
#     rating = Column(Float, default=0.0)

# 2. Tạo migration tự động
alembic revision --autogenerate -m "add rating to recipes"

# 3. Xem file migration được tạo
# alembic/versions/003_add_rating_to_recipes.py

# 4. Chạy migration
alembic upgrade head

# 5. Nếu có lỗi, rollback
alembic downgrade -1
```

---

## 📊 Các thao tác nâng cao

### Add Column (Giống Liquibase addColumn)
```python
def upgrade():
    op.add_column('recipes', sa.Column('rating', sa.Float(), nullable=True))

def downgrade():
    op.drop_column('recipes', 'rating')
```

### Modify Column (Giống Liquibase modifyColumn)
```python
def upgrade():
    op.alter_column('recipes', 'name',
                    existing_type=sa.String(200),
                    type_=sa.String(300))

def downgrade():
    op.alter_column('recipes', 'name',
                    existing_type=sa.String(300),
                    type_=sa.String(200))
```

### Add Foreign Key (Giống Liquibase addForeignKeyConstraint)
```python
def upgrade():
    op.create_foreign_key(
        'fk_ingredients_recipe',
        'ingredients', 'recipes',
        ['recipe_id'], ['id']
    )

def downgrade():
    op.drop_constraint('fk_ingredients_recipe', 'ingredients')
```

### Create Index (Giống Liquibase createIndex)
```python
def upgrade():
    op.create_index('ix_recipes_name', 'recipes', ['name'])

def downgrade():
    op.drop_index('ix_recipes_name', 'recipes')
```

---

## 🎯 Migration trong project này

### Migration 001: Initial Schema
- Tạo 4 tables: recipes, ingredients, steps, pantry
- Tạo foreign keys
- Tạo indexes

### Migration 002: Sample Data
- Insert 3 recipes mẫu (Phở, Bún Chả, Bánh Mì)
- Insert ingredients cho mỗi recipe
- Insert steps cho mỗi recipe
- Insert pantry items mẫu

---

## 🔍 Debug Migrations

### Xem SQL sẽ được chạy (không thực thi)
```powershell
alembic upgrade head --sql
```

### Kiểm tra migrations chưa chạy
```powershell
alembic current
alembic history
```

### Đánh dấu migration đã chạy (không chạy SQL)
```powershell
alembic stamp head
```

---

## 🚨 Lưu ý quan trọng

### ✅ Nên làm:
- Luôn test migration trước khi deploy
- Backup database trước khi chạy migration
- Viết cả upgrade() và downgrade()
- Commit migration files vào git

### ❌ Không nên:
- Sửa migration đã chạy trên production
- Xóa migration files cũ
- Skip migrations (phải chạy theo thứ tự)
- Chạy upgrade/downgrade nhiều lần liên tục

---

## 📚 So sánh chi tiết với Liquibase

### Liquibase XML:
```xml
<changeSet id="1" author="user">
    <createTable tableName="recipes">
        <column name="id" type="int" autoIncrement="true">
            <constraints primaryKey="true"/>
        </column>
        <column name="name" type="varchar(200)">
            <constraints nullable="false"/>
        </column>
    </createTable>
</changeSet>

<changeSet id="2" author="user">
    <insert tableName="recipes">
        <column name="name" value="Phở Bò"/>
        <column name="servings" value="4"/>
    </insert>
</changeSet>
```

### Alembic Python:
```python
# Migration 001
def upgrade():
    op.create_table(
        'recipes',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(200), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

# Migration 002
def upgrade():
    op.execute("""
        INSERT INTO recipes (name, servings)
        VALUES ('Phở Bò', 4)
    """)
```

---

## 🎓 Kết luận

- **Alembic = Liquibase của Python**
- Quản lý database schema như code
- Version control cho database
- Dễ rollback khi có lỗi
- Tự động generate migrations từ models
- Làm việc tốt với SQLAlchemy ORM

**Chạy ngay:**
```powershell
alembic upgrade head
```

Và database của bạn sẽ được setup hoàn chỉnh! 🎉
