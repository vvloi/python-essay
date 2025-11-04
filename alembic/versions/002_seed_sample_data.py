"""Seed sample data - Vietnamese recipes

Revision ID: 002
Revises: 001
Create Date: 2025-11-04

This is similar to Liquibase <insert> tags
"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

# Pantry items for consistent upgrade/downgrade
PANTRY_ITEMS = ['Fish sauce', 'Sugar', 'Rice', 'Garlic', 'Onion', 'Salt', 'Vegetable oil']


def upgrade() -> None:
    """Insert sample data - similar to Liquibase <insert>"""
    import sqlalchemy as sa

    conn = op.get_bind()

    # Recipe data
    recipes = [
        {
            'name': 'Phở Bò',
            'description': 'Traditional Vietnamese beef noodle soup with rich broth',
            'cuisine': 'Vietnamese',
            'servings': 4,
            'prep_time_minutes': 30,
            'cook_time_minutes': 120,
            'ingredients': [
                ('Beef bones', 1.0, 'kg'),
                ('Beef brisket', 500.0, 'g'),
                ('Rice noodles', 400.0, 'g'),
                ('Onion', 2.0, 'pieces'),
                ('Ginger', 50.0, 'g'),
                ('Star anise', 3.0, 'pieces'),
                ('Fish sauce', 3.0, 'tbsp'),
            ],
            'steps': [
                'Blanch beef bones in boiling water for 5 minutes, then rinse',
                'Char onion and ginger over open flame until fragrant',
                'Simmer bones with water, star anise for 2 hours',
                'Add beef brisket and cook for 30 minutes',
                'Season broth with fish sauce',
                'Cook rice noodles separately',
                'Assemble: noodles, beef slices, hot broth',
            ]
        },
        {
            'name': 'Bún Chả Hà Nội',
            'description': 'Grilled pork with rice vermicelli and dipping sauce',
            'cuisine': 'Vietnamese',
            'servings': 2,
            'prep_time_minutes': 20,
            'cook_time_minutes': 15,
            'ingredients': [
                ('Pork shoulder', 300.0, 'g'),
                ('Pork belly', 200.0, 'g'),
                ('Rice vermicelli', 200.0, 'g'),
                ('Fish sauce', 4.0, 'tbsp'),
                ('Sugar', 3.0, 'tbsp'),
                ('Garlic', 4.0, 'cloves'),
            ],
            'steps': [
                'Marinate pork with fish sauce, sugar, and garlic',
                'Grill pork over charcoal until caramelized',
                'Prepare dipping sauce with fish sauce and lime',
                'Cook rice vermicelli',
                'Serve grilled pork with vermicelli and sauce',
            ]
        },
        {
            'name': 'Bánh Mì Thịt',
            'description': 'Vietnamese sandwich with various fillings',
            'cuisine': 'Vietnamese',
            'servings': 4,
            'prep_time_minutes': 15,
            'cook_time_minutes': 10,
            'ingredients': [
                ('Baguette', 4.0, 'pieces'),
                ('Pork pâté', 200.0, 'g'),
                ('Grilled pork', 300.0, 'g'),
                ('Cucumber', 1.0, 'piece'),
                ('Carrot', 2.0, 'pieces'),
                ('Cilantro', 1.0, 'bunch'),
            ],
            'steps': [
                'Pickle carrot with vinegar and sugar',
                'Toast baguettes until crispy',
                'Spread pâté on bread',
                'Layer grilled pork slices',
                'Add cucumber and pickled vegetables',
                'Top with fresh cilantro',
            ]
        }
    ]

    # Insert recipes and their related data
    for recipe_data in recipes:
        # Insert recipe and get its ID
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

    # Insert sample pantry items
    op.execute("""
        INSERT INTO pantry (name, quantity, unit)
        VALUES
            ('Fish sauce', 500.0, 'ml'),
            ('Sugar', 1.0, 'kg'),
            ('Rice', 5.0, 'kg'),
            ('Garlic', 200.0, 'g'),
            ('Onion', 5.0, 'pieces'),
            ('Salt', 500.0, 'g'),
            ('Vegetable oil', 1.0, 'L');
    """)


def downgrade() -> None:
    """Remove sample data - similar to Liquibase rollback"""

    # Delete recipes by name instead of hardcoded IDs
    recipe_names = ['Phở Bò', 'Bún Chả Hà Nội', 'Bánh Mì Thịt']
    recipe_list = ', '.join(f"'{name}'" for name in recipe_names)

    # Delete in reverse order due to foreign keys
    op.execute(f"DELETE FROM steps WHERE recipe_id IN (SELECT id FROM recipes WHERE name IN ({recipe_list}))")
    op.execute(f"DELETE FROM ingredients WHERE recipe_id IN (SELECT id FROM recipes WHERE name IN ({recipe_list}))")
    op.execute(f"DELETE FROM recipes WHERE name IN ({recipe_list})")

    # Use constant for pantry items
    pantry_list = ', '.join(f"'{item}'" for item in PANTRY_ITEMS)
    op.execute(f"DELETE FROM pantry WHERE name IN ({pantry_list})")
