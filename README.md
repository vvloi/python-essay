# Recipe Book Web Application

## 📚 Overview
A full-stack Recipe Book application built with **Python (FastAPI)** for backend and **React + TypeScript + TailwindCSS** for frontend, implementing **3-Layer Architecture** pattern for both sides.

## 📖 Documentation Sitemap

Read the documentation in this order:

1. **[README.md](./README.md)** ⬅️ You are here
   - Project overview and architecture
   - Technology stack
   - Features and database schema

2. **[01-QUICKSTART.md](./01-QUICKSTART.md)** 🚀
   - Quick installation guide
   - Setup instructions for both backend and frontend
   - First-time setup commands

3. **[02-RUN-GUIDE.md](./02-RUN-GUIDE.md)** ▶️
   - How to run the application
   - Backend server commands
   - Frontend dev server commands
   - Production build steps

4. **[03-ARCHITECTURE.md](./03-ARCHITECTURE.md)** 🏗️
   - Detailed architecture explanation
   - Layer responsibilities
   - Design patterns and best practices

5. **[04-3-LAYER-EXPLAINED.md](./04-3-LAYER-EXPLAINED.md)** 📚
   - Deep dive into 3-Layer Architecture
   - Layer separation principles
   - Code examples for each layer

6. **[05-ALEMBIC-GUIDE.md](./05-ALEMBIC-GUIDE.md)** 🔄
   - Database migration guide
   - Alembic commands and workflow
   - Creating and applying migrations

7. **[06-MIGRATION-SUMMARY.md](./06-MIGRATION-SUMMARY.md)** 📝
   - Summary of all migrations
   - Migration history and changes
   - Database version tracking

8. **[07-PROJECT-SUMMARY.md](./07-PROJECT-SUMMARY.md)** 📊
   - Project development summary
   - Implementation timeline
   - Key decisions and learnings

9. **[08-TESTING.md](./08-TESTING.md)** ✅
   - Testing guide and strategy
   - Unit tests and integration tests
   - How to run tests

## 🏗️ Architecture

### Backend (3-Layer Architecture)
```
backend/
├── data_layer/          # Data Access Layer
│   └── repositories.py  # Database operations (CRUD)
├── business_layer/      # Business Logic Layer
│   └── services.py      # Business rules & data processing
├── presentation_layer/  # Presentation Layer
│   └── routes.py        # API endpoints (REST controllers)
├── database.py          # Database configuration
├── models.py            # SQLAlchemy ORM models
├── schemas.py           # Pydantic data validation schemas
└── main.py              # Application entry point
```

**Layers:**
1. **Data Layer (Repositories)**: Direct database access, raw CRUD operations
2. **Business Layer (Services)**: Business logic, data transformation, orchestration
3. **Presentation Layer (Routes/Controllers)**: HTTP request/response handling, API endpoints

### Frontend (3-Layer Architecture)
```
frontend/
├── src/
│   ├── data/               # Data Access Layer
│   │   ├── ApiClient.ts    # HTTP client
│   │   ├── RecipeAPI.ts    # Recipe endpoints
│   │   ├── PantryAPI.ts    # Pantry endpoints
│   │   └── ShoppingListAPI.ts
│   ├── business/           # Business Logic Layer
│   │   └── StateManager.ts # State management
│   ├── components/         # Presentation Layer
│   │   ├── RecipeList.tsx  # Recipe component
│   │   ├── Pantry.tsx      # Pantry component
│   │   └── ShoppingList.tsx
│   ├── App.tsx             # Main app component
│   ├── main.tsx            # App entry point
│   ├── index.scss          # Tailwind + custom styles
│   └── types.ts            # TypeScript types
├── package.json            # Node dependencies
├── tsconfig.json           # TypeScript config
├── vite.config.js          # Vite bundler config
└── tailwind.config.cjs     # Tailwind config
```

**Layers:**
1. **Data Layer (API)**: HTTP communication with backend using TypeScript
2. **Business Layer (Services)**: State management, data processing, business rules
3. **Presentation Layer (Components)**: React components with TSX, user interaction

### Database Migration (Alembic)
```
alembic/
├── versions/
│   └── 001_initial_migration.py  # Initial schema
├── env.py                         # Alembic environment config
└── script.py.mako                 # Migration template
```

**Alembic** is the Liquibase equivalent for Python/SQLAlchemy:
- Version-controlled database schema
- Automatic migration generation
- Rollback capability
- Database-agnostic DDL

## 🗄️ Database Schema (CSDL)

### Tables
- **recipes**: Recipe information (name, description, cuisine, servings, times)
- **ingredients**: Recipe ingredients (name, quantity, unit)
- **steps**: Cooking steps (step_number, instruction)
- **pantry**: Pantry inventory (name, quantity, unit)

### Relationships
- `recipes` ← one-to-many → `ingredients`
- `recipes` ← one-to-many → `steps`

## ✨ Features (Chức năng)

### 📖 Recipe Management
- ✅ Create, Read, Update, Delete recipes
- ✅ Add multiple ingredients and steps
- ✅ Search recipes by name (FTS5-like search)
- ✅ Scale recipes (adjust ingredient quantities)
- ✅ Recipe details with servings, prep/cook time

### 🏪 Pantry Management
- ✅ Track available ingredients
- ✅ Add/update/delete pantry items
- ✅ Automatic quantity aggregation

### 🛒 Shopping List
- ✅ Select multiple recipes
- ✅ Generate shopping list
- ✅ Subtract pantry items from needed ingredients
- ✅ Export shopping list to text file

### 🔍 Search
- ✅ Real-time recipe search
- ✅ Search by recipe name (SQL LIKE-based, similar to FTS5)

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+
- Node.js 16+ (for frontend)
- npm or yarn (Node package manager)

### Backend Setup

1. **Create and activate virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Install Python dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Initialize database with Alembic**
   ```powershell
   alembic upgrade head
   ```

4. **Run the backend server**
   ```powershell
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```powershell
   cd frontend
   ```

2. **Install Node dependencies**
   ```powershell
   npm install
   ```

3. **Run development server** (for development)
   ```powershell
   npm run dev
   ```

4. **Build for production** (backend will serve this)
   ```powershell
   npm run build
   ```

### Access the Application
- **Frontend Dev**: http://localhost:5173 (Vite dev server)
- **Frontend Prod**: http://localhost:8000 (served by backend after `npm run build`)
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## 📁 Project Structure

```
python-essay/
├── backend/                          # Backend application
│   ├── data_layer/                   # Data Access Layer
│   │   ├── __init__.py
│   │   └── repositories.py           # Repository pattern (CRUD)
│   ├── business_layer/               # Business Logic Layer
│   │   ├── __init__.py
│   │   └── services.py               # Services (business rules)
│   ├── presentation_layer/           # Presentation Layer
│   │   ├── __init__.py
│   │   └── routes.py                 # API routes (controllers)
│   ├── __init__.py
│   ├── database.py                   # Database configuration
│   ├── models.py                     # SQLAlchemy models
│   ├── schemas.py                    # Pydantic schemas
│   └── main.py                       # FastAPI app entry point
├── frontend/                         # Frontend application
│   ├── js/
│   │   ├── data-layer/               # Data Access Layer
│   │   │   └── api.js                # API communication
│   │   ├── business-layer/           # Business Logic Layer
│   │   │   └── services.js           # State & business logic
│   │   └── presentation-layer/       # Presentation Layer
│   │       └── ui-controller.js      # UI control & events
│   ├── css/
│   │   └── styles.css                # Styling
│   └── index.html                    # Main HTML
├── alembic/                          # Database migrations
│   ├── versions/
│   │   └── 001_initial_migration.py  # Initial schema
│   ├── env.py                        # Alembic environment
│   └── script.py.mako                # Migration template
├── alembic.ini                       # Alembic configuration
├── requirements.txt                  # Python dependencies
├── .env                              # Environment variables
└── README.md                         # This file
```

## 🔧 API Endpoints

### Recipes
- `GET /api/recipes` - Get all recipes
- `GET /api/recipes/{id}` - Get recipe by ID
- `GET /api/recipes/search?q={query}` - Search recipes
- `POST /api/recipes` - Create recipe
- `PUT /api/recipes/{id}` - Update recipe
- `DELETE /api/recipes/{id}` - Delete recipe
- `GET /api/recipes/{id}/scale?factor={factor}` - Scale recipe

### Pantry
- `GET /api/pantry` - Get all pantry items
- `GET /api/pantry/{id}` - Get pantry item by ID
- `POST /api/pantry` - Add pantry item
- `PUT /api/pantry/{id}` - Update pantry item
- `DELETE /api/pantry/{id}` - Delete pantry item

### Shopping List
- `POST /api/shopping-list` - Generate shopping list (body: array of recipe IDs)

### Health
- `GET /api/health` - Health check

## 🧪 Testing the Application

### Create a Recipe
1. Click "Add Recipe" button
2. Fill in recipe details:
   - Name: "Phở Bò"
   - Cuisine: "Vietnamese"
   - Servings: 4
   - Prep time: 30 minutes
   - Cook time: 60 minutes
3. Add ingredients:
   - Beef: 500g
   - Rice noodles: 400g
   - Broth: 2L
4. Add steps:
   1. Prepare broth
   2. Cook beef
   3. Prepare noodles
5. Click "Save Recipe"

### Generate Shopping List
1. Select multiple recipes (checkbox)
2. Navigate to "Shopping List" tab
3. Click "Generate List"
4. Click "Export" to download as text file

## 🛠️ Database Management with Alembic

### Create New Migration
```powershell
alembic revision -m "description of changes"
```

### Run Migrations (Upgrade)
```powershell
alembic upgrade head
```

### Rollback Migration (Downgrade)
```powershell
alembic downgrade -1
```

### View Migration History
```powershell
alembic history
```

### Check Current Version
```powershell
alembic current
```

## 🎯 Design Principles Applied

### Backend Principles
1. **Separation of Concerns**: Each layer has distinct responsibility
2. **Dependency Injection**: Database session injected via FastAPI Depends
3. **Repository Pattern**: Abstracted data access in repository layer
4. **Service Layer**: Business logic isolated from HTTP concerns
5. **Schema Validation**: Pydantic for request/response validation
6. **Type Hints**: Full type annotations for better IDE support

### Frontend Principles
1. **Component-Based Architecture**: React components for reusability
2. **Type Safety**: TypeScript for compile-time error detection
3. **State Management**: Centralized state with observer pattern
4. **API Abstraction**: HTTP logic separated from business logic
5. **Utility-First CSS**: TailwindCSS for rapid UI development
6. **Modularity**: Clear 3-layer separation in React app

### Code Quality
- ✅ Minimal if-else nesting (strategy pattern, early returns)
- ✅ Clear function names
- ✅ Single responsibility per function
- ✅ DRY (Don't Repeat Yourself)
- ✅ Explicit error handling

## 📝 Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=sqlite:///./recipe_book.db
HOST=0.0.0.0
PORT=8000
```

For PostgreSQL:
```env
DATABASE_URL=postgresql://user:password@localhost/recipe_book
```

## 🔒 Security Notes

- Input validation via Pydantic schemas
- SQL injection protection via SQLAlchemy ORM
- XSS protection via proper HTML escaping in frontend
- CORS enabled for development (configure for production)

## 📦 Dependencies

### Backend
- **FastAPI**: Modern web framework
- **Uvicorn**: ASGI server
- **SQLAlchemy**: ORM for database operations
- **Alembic**: Database migration tool
- **Pydantic**: Data validation
- **python-dotenv**: Environment variable management

### Frontend
- **React 18+**: Component-based UI framework
- **TypeScript 5+**: Type-safe JavaScript
- **Vite 5+**: Fast build tool and dev server
- **TailwindCSS 3+**: Utility-first CSS framework
- **SCSS**: CSS preprocessor with Tailwind integration

## 🚀 Production Deployment

### Backend
1. Update `.env` with production database URL
2. Set `DEBUG=False` in configuration
3. Use production-grade ASGI server (Gunicorn + Uvicorn workers)
4. Configure proper CORS origins
5. Enable HTTPS
6. Use PostgreSQL or MySQL instead of SQLite

Example production command:
```bash
gunicorn backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend
1. Build the production bundle:
   ```powershell
   cd frontend
   npm run build
   ```
2. The `frontend/dist` folder will be automatically served by the backend
3. For separate frontend hosting (CDN/Netlify/Vercel):
   - Update API base URL in `ApiClient.ts`
   - Deploy `dist` folder to hosting service

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 🤝 Contributing

This is an educational project demonstrating 3-layer architecture. Feel free to fork and modify!

## 📄 License

MIT License - Free to use for educational purposes.

---

**Built with 3-Layer Architecture** 🏗️
- Clean separation of concerns
- Maintainable and testable code
- Scalable design patterns
