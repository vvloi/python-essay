# Testing Guide - Recipe Book Application

## 🧪 Complete Testing Instructions

### Prerequisites
✅ Python 3.8+ installed
✅ pip installed
✅ Terminal with PowerShell

---

## 📝 Step-by-Step Testing

### 1️⃣ Setup Environment (First Time Only)

```powershell
# Navigate to project directory
cd e:\sources\python-essay

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt

# Initialize database with Alembic
alembic upgrade head
```

✅ **Expected Output:**
```
INFO  [alembic.runtime.migration] Running upgrade  -> 001, Initial migration - Create recipe book tables
```

---

### 2️⃣ Start the Application

```powershell
# Make sure you're in the project directory and venv is activated
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

✅ **Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

### 3️⃣ Verify Server is Running

Open browser and test these URLs:

1. **Frontend UI**: http://localhost:8000
   - Should see Recipe Book interface

2. **API Documentation**: http://localhost:8000/docs
   - Should see Swagger UI with all endpoints

3. **Health Check**: http://localhost:8000/api/health
   - Should see: `{"status":"healthy","architecture":"3-layer"}`

---

### 4️⃣ Load Sample Data (Optional but Recommended)

Open a **NEW PowerShell window** (keep server running in first window):

```powershell
# Navigate to project directory
cd e:\sources\python-essay

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run sample data script
python sample_data.py
```

✅ **Expected Output:**
```
============================================================
Recipe Book - Sample Data Generator
============================================================

✓ Server is running

Creating sample recipes...
✓ Created: Phở Bò (ID: 1)
✓ Created: Bún Chả Hà Nội (ID: 2)
✓ Created: Bánh Mì Thịt (ID: 3)
✓ Created: Cơm Tấm Sườn (ID: 4)

Creating sample pantry items...
✓ Added to pantry: Fish sauce - 500.0 ml
✓ Added to pantry: Sugar - 1.0 kg
...
```

---

## 🎯 Manual Testing Scenarios

### Test 1: Create a New Recipe

1. Open http://localhost:8000
2. Click **"➕ Add Recipe"** button
3. Fill in the form:
   ```
   Recipe Name: Gỏi Cuốn
   Description: Fresh spring rolls with shrimp and vegetables
   Cuisine: Vietnamese
   Servings: 4
   Prep Time: 20 minutes
   Cook Time: 5 minutes
   ```
4. Click **"➕ Add"** in Ingredients section, add:
   ```
   - Rice paper, 12, sheets
   - Shrimp, 200, g
   - Rice vermicelli, 100, g
   - Lettuce, 1, head
   ```
5. Click **"➕ Add"** in Steps section, add:
   ```
   Step 1: Cook shrimp and vermicelli
   Step 2: Soak rice paper in warm water
   Step 3: Roll with vegetables and shrimp
   ```
6. Click **"Save Recipe"**

✅ **Expected Result:**
- Success message appears
- New recipe card appears in the list

---

### Test 2: Search Recipes

1. In the search box, type: `phở`
2. Wait 1 second

✅ **Expected Result:**
- Only recipes with "phở" in name appear
- Other recipes are filtered out

---

### Test 3: Scale Recipe

1. Find a recipe card (e.g., "Phở Bò")
2. Click **"Scale"** button
3. Enter scale factor: `2` (to double)
4. Click OK

✅ **Expected Result:**
- Alert shows scaled ingredients
- All quantities are doubled

---

### Test 4: Add Pantry Item

1. Click **"Pantry"** tab in navigation
2. Click **"➕ Add Item"** button
3. Fill in:
   ```
   Item Name: Chicken breast
   Quantity: 500
   Unit: g
   ```
4. Click **"Save Item"**

✅ **Expected Result:**
- Success message
- New item appears in pantry list

---

### Test 5: Generate Shopping List

1. Go back to **"Recipes"** tab
2. Check the checkbox on 2-3 recipe cards
3. Notice the badge showing selected count
4. Click **"Shopping List"** tab
5. Click **"Generate List"** button

✅ **Expected Result:**
- Shopping list appears showing all ingredients
- Items in pantry are subtracted from the list
- Only missing ingredients are shown

---

### Test 6: Export Shopping List

1. After generating shopping list (Test 5)
2. Click **"📥 Export"** button

✅ **Expected Result:**
- A text file downloads: `shopping-list-YYYY-MM-DD.txt`
- File contains formatted shopping list

---

### Test 7: Update Recipe

1. Find any recipe card
2. Click **"Edit"** button
3. Change any field (e.g., servings from 4 to 6)
4. Click **"Save Recipe"**

✅ **Expected Result:**
- Success message
- Recipe card updates with new information

---

### Test 8: Delete Recipe

1. Find any recipe card
2. Click **"Delete"** button
3. Confirm deletion in the popup

✅ **Expected Result:**
- Recipe card disappears from the list
- Success message appears

---

## 🔍 API Testing (Using Swagger UI)

1. Open http://localhost:8000/docs
2. Try these endpoints:

### Get All Recipes
- Click `GET /api/recipes`
- Click "Try it out"
- Click "Execute"
- Should see JSON array of recipes

### Create Recipe via API
- Click `POST /api/recipes`
- Click "Try it out"
- Paste this JSON:
```json
{
  "name": "Chè Ba Màu",
  "description": "Three-color dessert",
  "cuisine": "Vietnamese",
  "servings": 2,
  "prep_time_minutes": 15,
  "cook_time_minutes": 0,
  "ingredients": [
    {"name": "Red beans", "quantity": 100, "unit": "g"},
    {"name": "Mung beans", "quantity": 100, "unit": "g"},
    {"name": "Coconut milk", "quantity": 200, "unit": "ml"}
  ],
  "steps": [
    {"step_number": 1, "instruction": "Cook beans separately"},
    {"step_number": 2, "instruction": "Layer in glass with ice"},
    {"step_number": 3, "instruction": "Pour coconut milk on top"}
  ]
}
```
- Click "Execute"
- Should return 201 status with created recipe

---

## 🐛 Troubleshooting

### Issue: "Port 8000 is already in use"
**Solution:**
```powershell
# Use a different port
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8001
```

### Issue: "No module named 'backend'"
**Solution:**
- Make sure you're in the project root directory
- Make sure virtual environment is activated

### Issue: "Database is locked"
**Solution:**
```powershell
# Stop the server (Ctrl+C)
# Delete the database file
Remove-Item recipe_book.db
# Re-run migrations
alembic upgrade head
# Restart server
```

### Issue: Cannot activate venv (PowerShell execution policy)
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📊 Test Results Checklist

Use this checklist to verify all features work:

- [ ] Server starts successfully
- [ ] Frontend loads without errors
- [ ] Sample data loads successfully
- [ ] Can create new recipe
- [ ] Can view recipe details
- [ ] Can edit existing recipe
- [ ] Can delete recipe
- [ ] Can search recipes
- [ ] Can scale recipe
- [ ] Can add pantry item
- [ ] Can edit pantry item
- [ ] Can delete pantry item
- [ ] Can generate shopping list
- [ ] Shopping list subtracts pantry items
- [ ] Can export shopping list
- [ ] API docs are accessible
- [ ] Health check returns OK

---

## 🎓 Understanding the Architecture While Testing

### When you create a recipe, this happens:

```
Frontend Layer Flow:
1. UI Controller (presentation) captures form data
2. Recipe Service (business) validates and updates state
3. API Client (data) sends HTTP POST request

Backend Layer Flow:
4. Routes (presentation) receives request
5. Service (business) processes business logic
6. Repository (data) executes SQL INSERT
7. Database stores the data

Response Flow (reverse):
8. Database → Repository → Service → Routes
9. HTTP Response → API Client → Service → UI Controller
10. UI updates with new recipe
```

This demonstrates the **3-Layer Architecture** in action!

---

## 📈 Performance Testing

### Test Database Performance
```powershell
# Create 100 recipes
for ($i=1; $i -le 100; $i++) {
    python -c "import requests; requests.post('http://localhost:8000/api/recipes', json={'name': 'Test Recipe $i', 'servings': 4, 'ingredients': [], 'steps': []})"
}

# Search should still be fast
# Open frontend and search
```

---

## 🎉 Congratulations!

If all tests pass, your Recipe Book application is working perfectly with:
- ✅ 3-Layer Architecture (Backend & Frontend)
- ✅ Alembic database migrations
- ✅ Full CRUD operations
- ✅ Search functionality
- ✅ Shopping list generation
- ✅ Data export

**Happy Cooking! 🍜**
