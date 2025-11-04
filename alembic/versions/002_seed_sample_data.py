"""Seed sample data - Vietnamese recipes

Revision ID: 002
Revises: 001
Create Date: 2025-11-04

This is similar to Liquibase <insert> tags
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert sample data - similar to Liquibase <insert>"""
    
    # Insert sample recipes
    op.execute("""
        INSERT INTO recipes (id, name, description, cuisine, servings, prep_time_minutes, cook_time_minutes)
        VALUES 
            (1, 'Phở Bò', 'Traditional Vietnamese beef noodle soup with rich broth', 'Vietnamese', 4, 30, 120),
            (2, 'Bún Chả Hà Nội', 'Grilled pork with rice vermicelli and dipping sauce', 'Vietnamese', 2, 20, 15),
            (3, 'Bánh Mì Thịt', 'Vietnamese sandwich with various fillings', 'Vietnamese', 4, 15, 10);
    """)
    
    # Insert ingredients for Phở Bò (recipe_id = 1)
    op.execute("""
        INSERT INTO ingredients (recipe_id, name, quantity, unit)
        VALUES 
            (1, 'Beef bones', 1.0, 'kg'),
            (1, 'Beef brisket', 500.0, 'g'),
            (1, 'Rice noodles', 400.0, 'g'),
            (1, 'Onion', 2.0, 'pieces'),
            (1, 'Ginger', 50.0, 'g'),
            (1, 'Star anise', 3.0, 'pieces'),
            (1, 'Fish sauce', 3.0, 'tbsp');
    """)
    
    # Insert steps for Phở Bò
    op.execute("""
        INSERT INTO steps (recipe_id, step_number, instruction)
        VALUES 
            (1, 1, 'Blanch beef bones in boiling water for 5 minutes, then rinse'),
            (1, 2, 'Char onion and ginger over open flame until fragrant'),
            (1, 3, 'Simmer bones with water, star anise for 2 hours'),
            (1, 4, 'Add beef brisket and cook for 30 minutes'),
            (1, 5, 'Season broth with fish sauce'),
            (1, 6, 'Cook rice noodles separately'),
            (1, 7, 'Assemble: noodles, beef slices, hot broth');
    """)
    
    # Insert ingredients for Bún Chả (recipe_id = 2)
    op.execute("""
        INSERT INTO ingredients (recipe_id, name, quantity, unit)
        VALUES 
            (2, 'Pork shoulder', 300.0, 'g'),
            (2, 'Pork belly', 200.0, 'g'),
            (2, 'Rice vermicelli', 200.0, 'g'),
            (2, 'Fish sauce', 4.0, 'tbsp'),
            (2, 'Sugar', 3.0, 'tbsp'),
            (2, 'Garlic', 4.0, 'cloves');
    """)
    
    # Insert steps for Bún Chả
    op.execute("""
        INSERT INTO steps (recipe_id, step_number, instruction)
        VALUES 
            (2, 1, 'Marinate pork with fish sauce, sugar, and garlic'),
            (2, 2, 'Grill pork over charcoal until caramelized'),
            (2, 3, 'Prepare dipping sauce with fish sauce and lime'),
            (2, 4, 'Cook rice vermicelli'),
            (2, 5, 'Serve grilled pork with vermicelli and sauce');
    """)
    
    # Insert ingredients for Bánh Mì (recipe_id = 3)
    op.execute("""
        INSERT INTO ingredients (recipe_id, name, quantity, unit)
        VALUES 
            (3, 'Baguette', 4.0, 'pieces'),
            (3, 'Pork pâté', 200.0, 'g'),
            (3, 'Grilled pork', 300.0, 'g'),
            (3, 'Cucumber', 1.0, 'piece'),
            (3, 'Carrot', 2.0, 'pieces'),
            (3, 'Cilantro', 1.0, 'bunch');
    """)
    
    # Insert steps for Bánh Mì
    op.execute("""
        INSERT INTO steps (recipe_id, step_number, instruction)
        VALUES 
            (3, 1, 'Pickle carrot with vinegar and sugar'),
            (3, 2, 'Toast baguettes until crispy'),
            (3, 3, 'Spread pâté on bread'),
            (3, 4, 'Layer grilled pork slices'),
            (3, 5, 'Add cucumber and pickled vegetables'),
            (3, 6, 'Top with fresh cilantro');
    """)
    
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
    
    # Delete in reverse order due to foreign keys
    op.execute("DELETE FROM steps WHERE recipe_id IN (1, 2, 3)")
    op.execute("DELETE FROM ingredients WHERE recipe_id IN (1, 2, 3)")
    op.execute("DELETE FROM recipes WHERE id IN (1, 2, 3)")
    op.execute("DELETE FROM pantry WHERE name IN ('Fish sauce', 'Sugar', 'Rice', 'Garlic', 'Onion', 'Salt', 'Vegetable oil')")
