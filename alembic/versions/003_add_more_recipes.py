"""Add more delicious recipes with real data

Revision ID: 003
Revises: 002
Create Date: 2025-11-05

Adding Vietnamese, Italian, Japanese, Thai, and Mexican recipes
"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None

RECIPE_NAMES = [
    'Cơm Tấm Sườn Nướng',
    'Gỏi Cuốn',
    'Bún Bò Huế',
    'Spaghetti Carbonara',
    'Margherita Pizza',
    'Tiramisu',
    'Sushi Roll',
    'Ramen',
    'Pad Thai',
    'Tom Yum Soup',
    'Tacos al Pastor',
    'Guacamole',
]


def upgrade() -> None:
    """Insert delicious recipes with real cooking data"""
    import sqlalchemy as sa

    conn = op.get_bind()

    recipes = [
        # Vietnamese Recipes
        {
            'name': 'Cơm Tấm Sườn Nướng',
            'description': 'Broken rice with grilled pork chop, Vietnamese style',
            'cuisine': 'Vietnamese',
            'servings': 2,
            'prep_time_minutes': 20,
            'cook_time_minutes': 25,
            'ingredients': [
                ('Broken rice', 300.0, 'g'),
                ('Pork chops', 400.0, 'g'),
                ('Lemongrass', 2.0, 'stalks'),
                ('Fish sauce', 3.0, 'tbsp'),
                ('Sugar', 2.0, 'tbsp'),
                ('Garlic', 4.0, 'cloves'),
                ('Shallots', 3.0, 'pieces'),
                ('Egg', 2.0, 'pieces'),
            ],
            'steps': [
                'Marinate pork chops with lemongrass, garlic, fish sauce, sugar for 1 hour',
                'Grill pork chops over medium-high heat for 12-15 minutes, turning once',
                'Cook broken rice as regular rice',
                'Fry eggs sunny side up',
                'Prepare dipping sauce with fish sauce, sugar, lime juice, chili',
                'Serve rice with grilled pork chop, fried egg, and cucumber slices',
                'Drizzle with fish sauce dressing',
            ]
        },
        {
            'name': 'Gỏi Cuốn',
            'description': 'Fresh spring rolls with shrimp and pork',
            'cuisine': 'Vietnamese',
            'servings': 4,
            'prep_time_minutes': 30,
            'cook_time_minutes': 15,
            'ingredients': [
                ('Rice paper', 12.0, 'sheets'),
                ('Shrimp', 300.0, 'g'),
                ('Pork belly', 200.0, 'g'),
                ('Rice vermicelli', 100.0, 'g'),
                ('Lettuce', 1.0, 'head'),
                ('Mint leaves', 1.0, 'bunch'),
                ('Basil', 1.0, 'bunch'),
                ('Peanut butter', 3.0, 'tbsp'),
                ('Hoisin sauce', 2.0, 'tbsp'),
            ],
            'steps': [
                'Boil shrimp until pink and peel',
                'Boil pork belly and slice thinly',
                'Cook rice vermicelli according to package',
                'Prepare dipping sauce: mix peanut butter, hoisin sauce, water',
                'Soften rice paper in warm water',
                'Place lettuce, vermicelli, shrimp, pork, herbs on rice paper',
                'Roll tightly like a burrito',
                'Serve with peanut dipping sauce',
            ]
        },
        {
            'name': 'Bún Bò Huế',
            'description': 'Spicy beef noodle soup from Hue city',
            'cuisine': 'Vietnamese',
            'servings': 4,
            'prep_time_minutes': 30,
            'cook_time_minutes': 90,
            'ingredients': [
                ('Beef shank', 500.0, 'g'),
                ('Pork hock', 300.0, 'g'),
                ('Rice vermicelli', 400.0, 'g'),
                ('Lemongrass', 3.0, 'stalks'),
                ('Shrimp paste', 2.0, 'tbsp'),
                ('Chili oil', 3.0, 'tbsp'),
                ('Fish sauce', 4.0, 'tbsp'),
                ('Onion', 2.0, 'pieces'),
                ('Banana flower', 1.0, 'piece'),
            ],
            'steps': [
                'Boil beef shank and pork hock with lemongrass for 60 minutes',
                'Remove meat and slice into pieces',
                'Add shrimp paste and chili oil to broth',
                'Season with fish sauce and sugar',
                'Cook rice vermicelli separately',
                'Slice banana flower thinly',
                'Assemble bowl with vermicelli, meat, and hot broth',
                'Top with banana flower, herbs, lime, and extra chili oil',
            ]
        },

        # Italian Recipes
        {
            'name': 'Spaghetti Carbonara',
            'description': 'Classic Italian pasta with eggs, cheese, and pancetta',
            'cuisine': 'Italian',
            'servings': 4,
            'prep_time_minutes': 10,
            'cook_time_minutes': 15,
            'ingredients': [
                ('Spaghetti', 400.0, 'g'),
                ('Pancetta', 200.0, 'g'),
                ('Egg yolks', 4.0, 'pieces'),
                ('Parmesan cheese', 100.0, 'g'),
                ('Black pepper', 1.0, 'tsp'),
                ('Salt', 1.0, 'tsp'),
            ],
            'steps': [
                'Boil salted water and cook spaghetti al dente',
                'Cut pancetta into small cubes and fry until crispy',
                'Beat egg yolks with grated parmesan cheese',
                'Reserve 1 cup pasta water before draining',
                'Mix hot pasta with pancetta off heat',
                'Add egg mixture and toss quickly, adding pasta water for creaminess',
                'Season with black pepper generously',
                'Serve immediately with extra parmesan',
            ]
        },
        {
            'name': 'Margherita Pizza',
            'description': 'Classic Neapolitan pizza with tomato, mozzarella, and basil',
            'cuisine': 'Italian',
            'servings': 2,
            'prep_time_minutes': 90,
            'cook_time_minutes': 12,
            'ingredients': [
                ('Pizza dough', 300.0, 'g'),
                ('Tomato sauce', 150.0, 'ml'),
                ('Mozzarella cheese', 200.0, 'g'),
                ('Fresh basil', 10.0, 'leaves'),
                ('Olive oil', 2.0, 'tbsp'),
                ('Salt', 0.5, 'tsp'),
            ],
            'steps': [
                'Let pizza dough rest at room temperature for 1 hour',
                'Preheat oven to maximum temperature (250°C or higher)',
                'Roll dough into 12-inch circle',
                'Spread tomato sauce evenly, leaving border for crust',
                'Tear mozzarella and distribute on sauce',
                'Drizzle with olive oil and sprinkle salt',
                'Bake for 10-12 minutes until crust is golden',
                'Add fresh basil leaves after baking',
            ]
        },
        {
            'name': 'Tiramisu',
            'description': 'Italian coffee-flavored dessert with mascarpone',
            'cuisine': 'Italian',
            'servings': 8,
            'prep_time_minutes': 30,
            'cook_time_minutes': 0,
            'ingredients': [
                ('Ladyfinger biscuits', 300.0, 'g'),
                ('Mascarpone cheese', 500.0, 'g'),
                ('Egg yolks', 4.0, 'pieces'),
                ('Sugar', 100.0, 'g'),
                ('Espresso coffee', 300.0, 'ml'),
                ('Cocoa powder', 3.0, 'tbsp'),
                ('Marsala wine', 50.0, 'ml'),
            ],
            'steps': [
                'Brew strong espresso and let cool completely',
                'Beat egg yolks with sugar until pale and thick',
                'Fold in mascarpone cheese gently',
                'Mix espresso with marsala wine',
                'Quickly dip ladyfingers in coffee mixture',
                'Layer dipped biscuits in dish',
                'Spread mascarpone cream over biscuits',
                'Repeat layers and dust top with cocoa powder',
                'Refrigerate for at least 4 hours before serving',
            ]
        },

        # Japanese Recipes
        {
            'name': 'Sushi Roll',
            'description': 'Classic Japanese rolled sushi with fresh fish',
            'cuisine': 'Japanese',
            'servings': 4,
            'prep_time_minutes': 40,
            'cook_time_minutes': 20,
            'ingredients': [
                ('Sushi rice', 400.0, 'g'),
                ('Nori sheets', 4.0, 'sheets'),
                ('Fresh salmon', 200.0, 'g'),
                ('Cucumber', 1.0, 'piece'),
                ('Avocado', 1.0, 'piece'),
                ('Rice vinegar', 3.0, 'tbsp'),
                ('Sugar', 2.0, 'tbsp'),
                ('Soy sauce', 4.0, 'tbsp'),
                ('Wasabi', 1.0, 'tbsp'),
            ],
            'steps': [
                'Cook sushi rice and let cool slightly',
                'Mix rice vinegar, sugar, salt and fold into rice',
                'Cut salmon, cucumber, avocado into thin strips',
                'Place nori sheet on bamboo mat',
                'Spread thin layer of rice on nori, leaving 1 inch at top',
                'Place fish and vegetables in center',
                'Roll tightly using bamboo mat',
                'Cut roll into 6-8 pieces with sharp wet knife',
                'Serve with soy sauce, wasabi, and pickled ginger',
            ]
        },
        {
            'name': 'Ramen',
            'description': 'Japanese noodle soup with rich broth and toppings',
            'cuisine': 'Japanese',
            'servings': 2,
            'prep_time_minutes': 20,
            'cook_time_minutes': 30,
            'ingredients': [
                ('Ramen noodles', 300.0, 'g'),
                ('Pork belly', 300.0, 'g'),
                ('Chicken broth', 1000.0, 'ml'),
                ('Soy sauce', 4.0, 'tbsp'),
                ('Miso paste', 2.0, 'tbsp'),
                ('Egg', 2.0, 'pieces'),
                ('Green onions', 2.0, 'stalks'),
                ('Nori', 2.0, 'sheets'),
                ('Sesame oil', 1.0, 'tbsp'),
            ],
            'steps': [
                'Simmer pork belly in water for 25 minutes, then slice',
                'Boil eggs for 7 minutes for soft-boiled, peel and halve',
                'Heat chicken broth and whisk in miso paste',
                'Add soy sauce and sesame oil to broth',
                'Cook ramen noodles according to package',
                'Divide noodles between bowls',
                'Pour hot broth over noodles',
                'Top with pork slices, egg halves, nori, and green onions',
            ]
        },

        # Thai Recipes
        {
            'name': 'Pad Thai',
            'description': 'Thai stir-fried rice noodles with shrimp',
            'cuisine': 'Thai',
            'servings': 2,
            'prep_time_minutes': 15,
            'cook_time_minutes': 10,
            'ingredients': [
                ('Rice noodles', 200.0, 'g'),
                ('Shrimp', 200.0, 'g'),
                ('Egg', 2.0, 'pieces'),
                ('Bean sprouts', 100.0, 'g'),
                ('Peanuts', 50.0, 'g'),
                ('Tamarind paste', 2.0, 'tbsp'),
                ('Fish sauce', 3.0, 'tbsp'),
                ('Sugar', 2.0, 'tbsp'),
                ('Garlic', 3.0, 'cloves'),
                ('Lime', 1.0, 'piece'),
            ],
            'steps': [
                'Soak rice noodles in warm water for 20 minutes',
                'Mix tamarind paste, fish sauce, and sugar for sauce',
                'Heat wok with oil, scramble eggs and set aside',
                'Stir-fry garlic and shrimp until pink',
                'Add drained noodles and sauce, toss well',
                'Add eggs back, stir in bean sprouts',
                'Cook for 2 minutes until noodles are tender',
                'Serve with crushed peanuts, lime wedges, and chili flakes',
            ]
        },
        {
            'name': 'Tom Yum Soup',
            'description': 'Spicy and sour Thai soup with shrimp',
            'cuisine': 'Thai',
            'servings': 4,
            'prep_time_minutes': 15,
            'cook_time_minutes': 20,
            'ingredients': [
                ('Shrimp', 400.0, 'g'),
                ('Mushrooms', 200.0, 'g'),
                ('Lemongrass', 2.0, 'stalks'),
                ('Galangal', 30.0, 'g'),
                ('Kaffir lime leaves', 4.0, 'leaves'),
                ('Thai chilies', 3.0, 'pieces'),
                ('Fish sauce', 3.0, 'tbsp'),
                ('Lime juice', 3.0, 'tbsp'),
                ('Tomatoes', 2.0, 'pieces'),
                ('Cilantro', 1.0, 'bunch'),
            ],
            'steps': [
                'Bring water to boil, add lemongrass, galangal, kaffir lime leaves',
                'Simmer for 10 minutes to infuse flavors',
                'Add mushrooms and tomatoes, cook for 5 minutes',
                'Add shrimp and cook until pink (3-4 minutes)',
                'Remove from heat',
                'Add fish sauce, lime juice, and chilies',
                'Taste and adjust sourness and spiciness',
                'Garnish with cilantro and serve hot',
            ]
        },

        # Mexican Recipes
        {
            'name': 'Tacos al Pastor',
            'description': 'Mexican tacos with marinated pork and pineapple',
            'cuisine': 'Mexican',
            'servings': 4,
            'prep_time_minutes': 30,
            'cook_time_minutes': 20,
            'ingredients': [
                ('Pork shoulder', 600.0, 'g'),
                ('Corn tortillas', 12.0, 'pieces'),
                ('Pineapple', 200.0, 'g'),
                ('Onion', 1.0, 'piece'),
                ('Cilantro', 1.0, 'bunch'),
                ('Dried chilies', 3.0, 'pieces'),
                ('Garlic', 4.0, 'cloves'),
                ('Cumin', 1.0, 'tsp'),
                ('Lime', 2.0, 'pieces'),
            ],
            'steps': [
                'Rehydrate dried chilies in hot water',
                'Blend chilies with garlic, cumin, vinegar for marinade',
                'Slice pork thinly and marinate for 2 hours',
                'Grill or pan-fry pork slices until caramelized',
                'Grill pineapple chunks until slightly charred',
                'Warm corn tortillas on griddle',
                'Dice onion and cilantro finely',
                'Assemble tacos: tortilla, pork, pineapple, onion, cilantro',
                'Squeeze lime juice over tacos before eating',
            ]
        },
        {
            'name': 'Guacamole',
            'description': 'Fresh Mexican avocado dip',
            'cuisine': 'Mexican',
            'servings': 4,
            'prep_time_minutes': 10,
            'cook_time_minutes': 0,
            'ingredients': [
                ('Avocados', 3.0, 'pieces'),
                ('Tomato', 1.0, 'piece'),
                ('Onion', 0.5, 'piece'),
                ('Cilantro', 0.5, 'bunch'),
                ('Lime juice', 2.0, 'tbsp'),
                ('Jalapeño', 1.0, 'piece'),
                ('Salt', 0.5, 'tsp'),
                ('Garlic', 1.0, 'clove'),
            ],
            'steps': [
                'Cut avocados in half, remove pit and scoop flesh',
                'Mash avocados with fork, leaving some chunks',
                'Dice tomato, onion, jalapeño very small',
                'Mince garlic and chop cilantro',
                'Mix all ingredients together',
                'Add lime juice and salt to taste',
                'Adjust spiciness with more jalapeño if desired',
                'Serve immediately with tortilla chips or tacos',
            ]
        },
    ]

    # Insert all recipes
    for recipe_data in recipes:
        result = conn.execute(
            sa.text("""
                INSERT INTO recipes (name, description, cuisine, servings, prep_time_minutes, cook_time_minutes)
                VALUES (:name, :description, :cuisine, :servings, :prep_time_minutes, :cook_time_minutes)
                RETURNING id
            """),
            {
                'name': recipe_data['name'],
                'description': recipe_data['description'],
                'cuisine': recipe_data['cuisine'],
                'servings': recipe_data['servings'],
                'prep_time_minutes': recipe_data['prep_time_minutes'],
                'cook_time_minutes': recipe_data['cook_time_minutes'],
            }
        )
        recipe_id = result.scalar()

        # Insert ingredients
        for name, quantity, unit in recipe_data['ingredients']:
            conn.execute(
                sa.text("""
                    INSERT INTO ingredients (recipe_id, name, quantity, unit)
                    VALUES (:recipe_id, :name, :quantity, :unit)
                """),
                {'recipe_id': recipe_id, 'name': name, 'quantity': quantity, 'unit': unit}
            )

        # Insert steps
        for step_number, instruction in enumerate(recipe_data['steps'], start=1):
            conn.execute(
                sa.text("""
                    INSERT INTO steps (recipe_id, step_number, instruction)
                    VALUES (:recipe_id, :step_number, :instruction)
                """),
                {'recipe_id': recipe_id, 'step_number': step_number, 'instruction': instruction}
            )

    # Add more pantry items
    op.execute("""
        INSERT INTO pantry (name, quantity, unit)
        VALUES
            ('Soy sauce', 300.0, 'ml'),
            ('Lime', 10.0, 'pieces'),
            ('Eggs', 12.0, 'pieces'),
            ('Butter', 250.0, 'g'),
            ('Olive oil', 500.0, 'ml'),
            ('Black pepper', 50.0, 'g'),
            ('Chili flakes', 30.0, 'g'),
            ('Ginger', 100.0, 'g');
    """)


def downgrade() -> None:
    """Remove the delicious recipes"""
    recipe_list = ', '.join(f"'{name}'" for name in RECIPE_NAMES)
    
    # Delete in reverse order due to foreign keys
    op.execute(f"DELETE FROM steps WHERE recipe_id IN (SELECT id FROM recipes WHERE name IN ({recipe_list}))")
    op.execute(f"DELETE FROM ingredients WHERE recipe_id IN (SELECT id FROM recipes WHERE name IN ({recipe_list}))")
    op.execute(f"DELETE FROM recipes WHERE name IN ({recipe_list})")
    
    # Remove added pantry items
    pantry_items = ['Soy sauce', 'Lime', 'Eggs', 'Butter', 'Olive oil', 'Black pepper', 'Chili flakes', 'Ginger']
    pantry_list = ', '.join(f"'{item}'" for item in pantry_items)
    op.execute(f"DELETE FROM pantry WHERE name IN ({pantry_list})")
