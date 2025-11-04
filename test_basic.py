# Simple test suite for Recipe Book
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def test_imports():
    """Test that all modules can be imported"""
    try:
        from backend import database, models, schemas, main
        from backend.data_layer import repositories
        from backend.business_layer import services
        from backend.presentation_layer import routes
        # Verify modules are imported
        assert database and models and schemas and main
        assert repositories and services and routes
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_database_models():
    """Test that database models are properly defined"""
    try:
        from backend.models import Recipe, Ingredient, Step, Pantry

        # Check model attributes
        assert hasattr(Recipe, '__tablename__')
        assert hasattr(Recipe, 'id')
        assert hasattr(Recipe, 'name')

        assert hasattr(Ingredient, '__tablename__')
        assert hasattr(Step, '__tablename__')
        assert hasattr(Pantry, '__tablename__')

        print("✓ Database models are valid")
        return True
    except AssertionError as e:
        print(f"✗ Model validation failed: {e}")
        return False

def test_schemas():
    """Test that Pydantic schemas are valid"""
    try:
        from backend import schemas

        # Test creating schema instances
        schemas.RecipeCreate(
            name="Test Recipe",
            servings=4,
            ingredients=[],
            steps=[]
        )

        schemas.IngredientCreate(
            name="Test Ingredient",
            quantity=100.0,
            unit="g"
        )

        schemas.PantryCreate(
            name="Test Pantry",
            quantity=1.0,
            unit="kg"
        )

        print("✓ Pydantic schemas are valid")
        return True
    except Exception as e:
        print(f"✗ Schema validation failed: {e}")
        return False

def test_alembic_migrations():
    """Test that Alembic migrations are loadable"""
    try:
        import importlib.util

        # Load migration files
        migrations = [
            'alembic/versions/001_initial_migration.py',
            'alembic/versions/002_seed_sample_data.py'
        ]

        for migration_path in migrations:
            spec = importlib.util.spec_from_file_location("migration", migration_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            assert hasattr(module, 'upgrade')
            assert hasattr(module, 'downgrade')

        print("✓ Alembic migrations are valid")
        return True
    except Exception as e:
        print(f"✗ Migration validation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("Running Recipe Book Test Suite")
    print("=" * 60)

    tests = [
        test_imports,
        test_database_models,
        test_schemas,
        test_alembic_migrations,
    ]

    results = []
    for test in tests:
        print(f"\n[Test] {test.__name__}")
        result = test()
        results.append(result)

    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Test Results: {passed}/{total} passed")
    print("=" * 60)

    if passed == total:
        print("\n✅ All tests passed!")
        return 0
    else:
        print(f"\n❌ {total - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
