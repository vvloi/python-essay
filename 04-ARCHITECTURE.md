# Recipe Book - Architecture Diagram

## 🏗️ 3-Layer Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP Requests
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              FRONTEND (React + TypeScript)                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  PRESENTATION LAYER (React Components - TSX)           │   │
│  │  • RecipeList.tsx                                      │   │
│  │  • Pantry.tsx                                          │   │
│  │  • ShoppingList.tsx                                    │   │
│  │  • React Hooks (useState, useEffect)                   │   │
│  │  • User Interaction & View Rendering                   │   │
│  └────────────────┬────────────────────────────────────────┘   │
│                   │                                             │
│  ┌────────────────▼────────────────────────────────────────┐   │
│  │  BUSINESS LAYER (StateManager.ts)                      │   │
│  │  • StateManager (Observer Pattern)                     │   │
│  │  • State Management with TypeScript types             │   │
│  │  • Business Logic & Data Processing                   │   │
│  └────────────────┬────────────────────────────────────────┘   │
│                   │                                             │
│  ┌────────────────▼────────────────────────────────────────┐   │
│  │  DATA LAYER (API Clients - TS)                        │   │
│  │  • ApiClient.ts                                        │   │
│  │  • RecipeAPI.ts                                        │   │
│  │  • PantryAPI.ts                                        │   │
│  │  • ShoppingListAPI.ts                                  │   │
│  │  • HTTP Communication (fetch)                          │   │
│  └────────────────┬────────────────────────────────────────┘   │
└───────────────────┼─────────────────────────────────────────────┘
                    │
                    │ REST API (JSON)
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND (Python/FastAPI)                      │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  PRESENTATION LAYER (routes.py)                        │   │
│  │  • FastAPI Router                                      │   │
│  │  • HTTP Request/Response                               │   │
│  │  • /api/recipes endpoints                              │   │
│  │  • /api/pantry endpoints                               │   │
│  │  • /api/shopping-list endpoint                         │   │
│  │  • Input Validation (Pydantic)                         │   │
│  └────────────────┬────────────────────────────────────────┘   │
│                   │                                             │
│  ┌────────────────▼────────────────────────────────────────┐   │
│  │  BUSINESS LAYER (services.py)                          │   │
│  │  • RecipeService                                       │   │
│  │  •   - CRUD operations                                 │   │
│  │  •   - Scale recipe logic                              │   │
│  │  • PantryService                                       │   │
│  │  •   - Inventory management                            │   │
│  │  • ShoppingListService                                 │   │
│  │  •   - Shopping list generation                        │   │
│  │  •   - Pantry subtraction logic                        │   │
│  │  • Business Rules & Orchestration                      │   │
│  └────────────────┬────────────────────────────────────────┘   │
│                   │                                             │
│  ┌────────────────▼────────────────────────────────────────┐   │
│  │  DATA LAYER (repositories.py)                          │   │
│  │  • RecipeRepository                                    │   │
│  │  • IngredientRepository                                │   │
│  │  • StepRepository                                      │   │
│  │  • PantryRepository                                    │   │
│  │  • Database CRUD Operations                            │   │
│  │  • SQLAlchemy ORM Queries                              │   │
│  └────────────────┬────────────────────────────────────────┘   │
└───────────────────┼─────────────────────────────────────────────┘
                    │
                    │ SQLAlchemy ORM
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                     DATABASE (SQLite)                            │
├─────────────────────────────────────────────────────────────────┤
│  • recipes (id, name, description, cuisine, servings, times)    │
│  • ingredients (id, recipe_id, name, quantity, unit)            │
│  • steps (id, recipe_id, step_number, instruction)              │
│  • pantry (id, name, quantity, unit)                            │
│  • alembic_version (migration tracking)                         │
└─────────────────────────────────────────────────────────────────┘
                    ▲
                    │
                    │ Alembic Migrations
                    │
┌───────────────────┴─────────────────────────────────────────────┐
│                    ALEMBIC (Migration Tool)                      │
├─────────────────────────────────────────────────────────────────┤
│  • Version Control for Database Schema                          │
│  • Migration Scripts (versions/*.py)                            │
│  • Upgrade/Downgrade Commands                                   │
│  • Similar to Liquibase for Java                                │
└─────────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow Example: Creating a Recipe

```
1. USER INTERACTION
   └─> User fills form and clicks "Save Recipe"
   
2. FRONTEND PRESENTATION LAYER (React Component)
   └─> RecipeList.tsx handleSubmit() collects form data
       • React state (useState) manages form
       • TypeScript types validate data
   
3. FRONTEND BUSINESS LAYER (StateManager.ts)
   └─> StateManager.setState(newRecipe)
       • Updates centralized state
       • Notifies all subscribers
   
4. FRONTEND DATA LAYER (RecipeAPI.ts)
   └─> RecipeAPI.create(data)
       • POST /api/recipes
       • Sends JSON payload with type safety
   
5. BACKEND PRESENTATION LAYER (routes.py)
   └─> @router.post("/recipes")
       • Receives HTTP request
       • Validates with Pydantic schema
   
6. BACKEND BUSINESS LAYER (services.py)
   └─> RecipeService.create_recipe(db, recipe_data)
       • Applies business logic
       • Creates Recipe object
       • Adds ingredients & steps
   
7. BACKEND DATA LAYER (repositories.py)
   └─> RecipeRepository.create(db, recipe)
       • Executes SQL INSERT
       • Returns created object
   
8. DATABASE
   └─> SQLite stores data
       • recipes table
       • ingredients table
       • steps table
   
9. RESPONSE FLOW (reverse path)
   └─> Repository → Service → Route → API → Service → UI
       • Returns created recipe
       • Updates state
       • Re-renders UI
```

## 🎯 Key Design Principles

### Separation of Concerns
- Each layer has a single responsibility
- No layer skips another layer
- Clear interfaces between layers

### Dependency Direction
```
Presentation → Business → Data → Database
```

### Benefits
✅ Easy to test (mock each layer)
✅ Easy to maintain (change one layer without affecting others)
✅ Easy to scale (add features to appropriate layer)
✅ Code reusability (services can be used by multiple routes)
✅ Clear architecture (easy for new developers to understand)

## 📦 File Structure Mapping

```
Backend:
├── presentation_layer/
│   └── routes.py           ➡️  HTTP endpoints
├── business_layer/
│   └── services.py         ➡️  Business logic
└── data_layer/
    └── repositories.py     ➡️  Database access

Frontend (React + TypeScript):
├── src/components/
│   └── *.tsx               ➡️  React components (UI)
├── src/business/
│   └── StateManager.ts     ➡️  State management
└── src/data/
    └── *API.ts             ➡️  HTTP API clients
```

## 🔐 Security Flow

```
Input Validation:
  Frontend Form → Pydantic Schema → Business Logic → Database

SQL Injection Prevention:
  SQLAlchemy ORM → Parameterized Queries → Safe SQL

XSS Prevention:
  escapeHtml() → Safe DOM Manipulation
```

## 🚀 Deployment Architecture (Production)

```
┌─────────────────────┐
│   Nginx (Reverse    │
│   Proxy + Static)   │
└──────────┬──────────┘
           │
    ┌──────▼──────┐
    │   Gunicorn  │
    │   Workers   │
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │  Uvicorn    │
    │  Workers    │
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │  FastAPI    │
    │  Application│
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │ PostgreSQL  │
    │ Database    │
    └─────────────┘
```

---

**Clean Architecture = Maintainable Code** 🏗️
