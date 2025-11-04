"""
Sample Data Script - Recipe Book
Run this script to populate database with sample recipes and pantry items
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"


def create_sample_recipes():
    """Create sample Vietnamese recipes"""
    
    recipes = [
        {
            "name": "Phở Bò",
            "description": "Traditional Vietnamese beef noodle soup with rich broth and tender beef slices",
            "cuisine": "Vietnamese",
            "servings": 4,
            "prep_time_minutes": 30,
            "cook_time_minutes": 120,
            "ingredients": [
                {"name": "Beef bones", "quantity": 1, "unit": "kg"},
                {"name": "Beef brisket", "quantity": 500, "unit": "g"},
                {"name": "Rice noodles", "quantity": 400, "unit": "g"},
                {"name": "Onion", "quantity": 2, "unit": "pieces"},
                {"name": "Ginger", "quantity": 50, "unit": "g"},
                {"name": "Star anise", "quantity": 3, "unit": "pieces"},
                {"name": "Cinnamon stick", "quantity": 1, "unit": "piece"},
                {"name": "Fish sauce", "quantity": 3, "unit": "tbsp"},
                {"name": "Rock sugar", "quantity": 2, "unit": "tbsp"}
            ],
            "steps": [
                {"step_number": 1, "instruction": "Blanch beef bones in boiling water for 5 minutes, then rinse"},
                {"step_number": 2, "instruction": "Char onion and ginger over open flame until fragrant"},
                {"step_number": 3, "instruction": "Simmer bones with water, star anise, and cinnamon for 2 hours"},
                {"step_number": 4, "instruction": "Add beef brisket and cook for 30 minutes"},
                {"step_number": 5, "instruction": "Season broth with fish sauce and rock sugar"},
                {"step_number": 6, "instruction": "Cook rice noodles separately according to package"},
                {"step_number": 7, "instruction": "Assemble: noodles, beef slices, hot broth, and garnish"}
            ]
        },
        {
            "name": "Bún Chả Hà Nội",
            "description": "Grilled pork with rice vermicelli and dipping sauce, a Hanoi specialty",
            "cuisine": "Vietnamese",
            "servings": 2,
            "prep_time_minutes": 20,
            "cook_time_minutes": 15,
            "ingredients": [
                {"name": "Pork shoulder", "quantity": 300, "unit": "g"},
                {"name": "Pork belly", "quantity": 200, "unit": "g"},
                {"name": "Rice vermicelli", "quantity": 200, "unit": "g"},
                {"name": "Fish sauce", "quantity": 4, "unit": "tbsp"},
                {"name": "Sugar", "quantity": 3, "unit": "tbsp"},
                {"name": "Garlic", "quantity": 4, "unit": "cloves"},
                {"name": "Lime juice", "quantity": 2, "unit": "tbsp"},
                {"name": "Carrot", "quantity": 1, "unit": "piece"},
                {"name": "Green papaya", "quantity": 100, "unit": "g"}
            ],
            "steps": [
                {"step_number": 1, "instruction": "Marinate pork with fish sauce, sugar, and minced garlic for 30 minutes"},
                {"step_number": 2, "instruction": "Grill pork over charcoal until caramelized and cooked through"},
                {"step_number": 3, "instruction": "Prepare dipping sauce: mix fish sauce, sugar, lime juice, and water"},
                {"step_number": 4, "instruction": "Add julienned carrot and papaya to the sauce"},
                {"step_number": 5, "instruction": "Cook rice vermicelli according to package"},
                {"step_number": 6, "instruction": "Serve grilled pork with vermicelli and dipping sauce"}
            ]
        },
        {
            "name": "Bánh Mì Thịt",
            "description": "Vietnamese sandwich with various fillings and fresh vegetables",
            "cuisine": "Vietnamese",
            "servings": 4,
            "prep_time_minutes": 15,
            "cook_time_minutes": 10,
            "ingredients": [
                {"name": "Baguette", "quantity": 4, "unit": "pieces"},
                {"name": "Pork pâté", "quantity": 200, "unit": "g"},
                {"name": "Grilled pork", "quantity": 300, "unit": "g"},
                {"name": "Cucumber", "quantity": 1, "unit": "piece"},
                {"name": "Carrot", "quantity": 2, "unit": "pieces"},
                {"name": "Daikon radish", "quantity": 1, "unit": "piece"},
                {"name": "Cilantro", "quantity": 1, "unit": "bunch"},
                {"name": "Mayonnaise", "quantity": 4, "unit": "tbsp"},
                {"name": "Soy sauce", "quantity": 2, "unit": "tbsp"}
            ],
            "steps": [
                {"step_number": 1, "instruction": "Pickle carrot and daikon with vinegar and sugar"},
                {"step_number": 2, "instruction": "Toast baguettes until crispy outside, soft inside"},
                {"step_number": 3, "instruction": "Spread mayonnaise and pâté on bread"},
                {"step_number": 4, "instruction": "Layer grilled pork slices"},
                {"step_number": 5, "instruction": "Add cucumber slices and pickled vegetables"},
                {"step_number": 6, "instruction": "Top with fresh cilantro and drizzle soy sauce"}
            ]
        },
        {
            "name": "Cơm Tấm Sườn",
            "description": "Broken rice with grilled pork chop, a Southern Vietnamese classic",
            "cuisine": "Vietnamese",
            "servings": 2,
            "prep_time_minutes": 25,
            "cook_time_minutes": 15,
            "ingredients": [
                {"name": "Broken rice", "quantity": 300, "unit": "g"},
                {"name": "Pork chop", "quantity": 400, "unit": "g"},
                {"name": "Fish sauce", "quantity": 3, "unit": "tbsp"},
                {"name": "Lemongrass", "quantity": 2, "unit": "stalks"},
                {"name": "Garlic", "quantity": 3, "unit": "cloves"},
                {"name": "Sugar", "quantity": 2, "unit": "tbsp"},
                {"name": "Egg", "quantity": 2, "unit": "pieces"},
                {"name": "Green onion", "quantity": 2, "unit": "stalks"}
            ],
            "steps": [
                {"step_number": 1, "instruction": "Marinate pork chops with lemongrass, garlic, fish sauce, and sugar"},
                {"step_number": 2, "instruction": "Let pork marinate for at least 2 hours or overnight"},
                {"step_number": 3, "instruction": "Grill pork chops until charred and cooked through"},
                {"step_number": 4, "instruction": "Cook broken rice in rice cooker"},
                {"step_number": 5, "instruction": "Fry eggs sunny-side up"},
                {"step_number": 6, "instruction": "Serve rice with grilled pork, fried egg, and fish sauce"}
            ]
        }
    ]
    
    print("Creating sample recipes...")
    created_recipes = []
    
    for recipe in recipes:
        try:
            response = requests.post(f"{BASE_URL}/recipes", json=recipe)
            if response.status_code == 201:
                created = response.json()
                created_recipes.append(created)
                print(f"✓ Created: {created['name']} (ID: {created['id']})")
            else:
                print(f"✗ Failed to create: {recipe['name']} - {response.text}")
        except Exception as e:
            print(f"✗ Error creating {recipe['name']}: {str(e)}")
    
    return created_recipes


def create_sample_pantry():
    """Create sample pantry items"""
    
    pantry_items = [
        {"name": "Fish sauce", "quantity": 500, "unit": "ml"},
        {"name": "Sugar", "quantity": 1, "unit": "kg"},
        {"name": "Rice", "quantity": 5, "unit": "kg"},
        {"name": "Garlic", "quantity": 200, "unit": "g"},
        {"name": "Onion", "quantity": 5, "unit": "pieces"},
        {"name": "Soy sauce", "quantity": 300, "unit": "ml"},
        {"name": "Salt", "quantity": 500, "unit": "g"},
        {"name": "Black pepper", "quantity": 100, "unit": "g"},
        {"name": "Vegetable oil", "quantity": 1, "unit": "L"},
        {"name": "Eggs", "quantity": 12, "unit": "pieces"}
    ]
    
    print("\nCreating sample pantry items...")
    
    for item in pantry_items:
        try:
            response = requests.post(f"{BASE_URL}/pantry", json=item)
            if response.status_code == 201:
                created = response.json()
                print(f"✓ Added to pantry: {created['name']} - {created['quantity']} {created['unit']}")
            else:
                print(f"✗ Failed to add: {item['name']} - {response.text}")
        except Exception as e:
            print(f"✗ Error adding {item['name']}: {str(e)}")


def main():
    print("=" * 60)
    print("Recipe Book - Sample Data Generator")
    print("=" * 60)
    print("\nMake sure the server is running at http://localhost:8000\n")
    
    try:
        # Test connection
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code != 200:
            print("✗ Server is not responding. Please start the server first.")
            return
        
        print("✓ Server is running\n")
        
        # Create sample data
        recipes = create_sample_recipes()
        create_sample_pantry()
        
        print("\n" + "=" * 60)
        print(f"✓ Successfully created {len(recipes)} recipes")
        print("✓ Successfully populated pantry")
        print("=" * 60)
        print("\nYou can now:")
        print("1. Open http://localhost:8000 to view recipes")
        print("2. Select recipes and generate shopping list")
        print("3. View pantry items")
        print("\nEnjoy testing the Recipe Book app! 🍜")
        
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to server. Please start the server first:")
        print("  uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000")
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
