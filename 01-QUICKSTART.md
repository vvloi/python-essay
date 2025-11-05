# Quick Start Guide - Recipe Book

## 🚀 Chạy ứng dụng ngay (Backend + Frontend)

### Backend Setup (Python)

#### 1. Tạo và kích hoạt Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 2. Cài đặt Python dependencies
```powershell
pip install -r requirements.txt
```

#### 3. Chạy database migration (Giống Liquibase update)
```powershell
# Tạo tables + insert sample data
alembic upgrade head
```

#### 4. Chạy backend server
```powershell
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup (React + TypeScript)

#### 5. Cài đặt Node dependencies
```powershell
cd frontend
npm install
```

#### 6. Chạy frontend dev server (development)
```powershell
npm run dev
# Frontend sẽ chạy tại http://localhost:5173
```

**HOẶC** build production (backend sẽ serve):
```powershell
npm run build
# Backend sẽ tự động serve frontend/dist tại http://localhost:8000
```

## ✅ Truy cập ứng dụng

### Development Mode
- **Frontend Dev (Vite)**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

### Production Mode (sau khi `npm run build`)
- **Frontend + Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📝 Thử nghiệm nhanh

### Tạo Recipe mới
1. Mở http://localhost:8000
2. Click nút "➕ Add Recipe"
3. Nhập thông tin:
   - Name: Phở Bò
   - Cuisine: Vietnamese
   - Servings: 4
   - Click "➕ Add" trong Ingredients section:
     - Beef, 500, g
     - Rice noodles, 400, g
     - Broth, 2, L
   - Click "➕ Add" trong Steps section:
     - Step 1: Prepare broth
     - Step 2: Cook beef
     - Step 3: Prepare noodles
4. Click "Save Recipe"

### Tạo Shopping List
1. Tick checkbox vào các recipe muốn nấu
2. Click tab "Shopping List"
3. Click "Generate List"
4. Click "📥 Export" để download file text

## 🏗️ Kiến trúc 3 Layer

### Backend
```
📁 Data Layer (repositories.py)
   ↓
📁 Business Layer (services.py)
   ↓
📁 Presentation Layer (routes.py)
```

### Frontend (React + TypeScript)
```
📁 Data Layer (src/data/*API.ts)
   ↓
📁 Business Layer (src/business/StateManager.ts)
   ↓
📁 Presentation Layer (src/components/*.tsx - React)
```

## 🗄️ Database Migration (Alembic)

Alembic là tool giống Liquibase cho Python:

### Xem current version
```powershell
alembic current
```

### Xem migration history
```powershell
alembic history
```

### Tạo migration mới (nếu thay đổi models)
```powershell
alembic revision --autogenerate -m "describe changes"
```

### Apply migration
```powershell
alembic upgrade head
```

### Rollback migration
```powershell
alembic downgrade -1
```

## 🔍 API Examples

### Get all recipes
```powershell
curl http://localhost:8000/api/recipes
```

### Search recipes
```powershell
curl http://localhost:8000/api/recipes/search?q=pho
```

### Create recipe
```powershell
curl -X POST http://localhost:8000/api/recipes `
  -H "Content-Type: application/json" `
  -d '{
    "name": "Bún chả",
    "cuisine": "Vietnamese",
    "servings": 2,
    "ingredients": [
      {"name": "Pork", "quantity": 300, "unit": "g"}
    ],
    "steps": [
      {"step_number": 1, "instruction": "Grill pork"}
    ]
  }'
```

## 💡 Tips

### Xem API Documentation
Mở http://localhost:8000/docs để xem interactive API docs (Swagger UI)

### Xem Database
Database được lưu ở file `recipe_book.db` (SQLite)
Dùng tool như DB Browser for SQLite để xem

### Debug
App chạy ở mode `--reload`, tự động restart khi code thay đổi

### Stop Server
Nhấn `Ctrl+C` trong terminal

## 🎯 Các tính năng chính

✅ CRUD cho Recipes (Create, Read, Update, Delete)
✅ CRUD cho Pantry items
✅ Search recipes theo tên
✅ Scale recipes (nhân đôi/chia đôi nguyên liệu)
✅ Generate shopping list từ nhiều recipes
✅ Export shopping list ra file text
✅ Tự động trừ pantry items khỏi shopping list

## 📂 Cấu trúc code đã tối ưu

- ❌ Ít if-else nesting
- ✅ Early returns
- ✅ Strategy pattern thay vì if-else chains
- ✅ Repository pattern cho data access
- ✅ Service layer cho business logic
- ✅ Clear separation of concerns

## 🐛 Troubleshooting

### Lỗi: "No module named 'backend'"
→ Đảm bảo đang ở thư mục gốc của project

### Lỗi: "Port 8000 already in use"
→ Dùng port khác: `uvicorn backend.main:app --port 8001`

### Lỗi: Database locked
→ Đóng các connection đến database, restart server

---

**Chúc bạn code vui vẻ! 🚀**
