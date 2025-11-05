// Frontend 3-Layer Architecture
// Presentation Layer - UI Components & Event Handlers

import { stateManager } from '../business-layer/StateManager.js';
import { RecipeService } from '../business-layer/RecipeService.js';
import { PantryService } from '../business-layer/PantryService.js';
import { ShoppingListService } from '../business-layer/ShoppingListService.js';

class UIController {
    constructor() {
        this.currentView = 'recipes';
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.subscribeToState();
        this.loadInitialData();
    }

    setupEventListeners() {
        // Navigation
        document.getElementById('nav-recipes').addEventListener('click', () => this.switchView('recipes'));
        document.getElementById('nav-pantry').addEventListener('click', () => this.switchView('pantry'));
        document.getElementById('nav-shopping').addEventListener('click', () => this.switchView('shopping'));

        // Recipe events
        document.getElementById('search-input').addEventListener('input', (e) => this.handleSearch(e.target.value));
        document.getElementById('add-recipe-btn').addEventListener('click', () => this.showRecipeModal());
        document.getElementById('recipe-form').addEventListener('submit', (e) => this.handleRecipeSubmit(e));
        document.getElementById('add-ingredient-btn').addEventListener('click', () => this.addIngredientField());
        document.getElementById('add-step-btn').addEventListener('click', () => this.addStepField());

        // Pantry events
        document.getElementById('add-pantry-btn').addEventListener('click', () => this.showPantryModal());
        document.getElementById('pantry-form').addEventListener('submit', (e) => this.handlePantrySubmit(e));

        // Shopping list events
        document.getElementById('generate-shopping-btn').addEventListener('click', () => this.generateShoppingList());
        document.getElementById('export-shopping-btn').addEventListener('click', () => this.exportShoppingList());

        // Modal close
        document.querySelectorAll('.modal .close').forEach(btn => {
            btn.addEventListener('click', () => this.closeModals());
        });
    }

    subscribeToState() {
        stateManager.subscribe((state) => {
            this.renderRecipes(state.recipes);
            this.renderPantryItems(state.pantryItems);
            this.renderShoppingList(state.shoppingList);
            this.updateSelectedCount(state.selectedRecipeIds.size);
        });
    }

    async loadInitialData() {
        this.showLoading();
        try {
            await RecipeService.loadAllRecipes();
            await PantryService.loadAllPantryItems();
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    switchView(view) {
        this.currentView = view;
        document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
        document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
        
        document.getElementById(`${view}-view`).classList.add('active');
        document.getElementById(`nav-${view}`).classList.add('active');
    }

    async handleSearch(query) {
        this.showLoading();
        try {
            await RecipeService.searchRecipes(query);
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    renderRecipes(recipes) {
        const container = document.getElementById('recipes-list');
        const { selectedRecipeIds } = stateManager.getState();
        
        container.innerHTML = recipes.map(recipe => `
            <div class="recipe-card">
                <div class="recipe-header">
                    <input type="checkbox" 
                           class="recipe-select" 
                           data-id="${recipe.id}"
                           ${selectedRecipeIds.has(recipe.id) ? 'checked' : ''}
                           onchange="uiController.toggleRecipeSelection(${recipe.id})">
                    <h3>${this.escapeHtml(recipe.name)}</h3>
                </div>
                ${recipe.cuisine ? `<p class="cuisine">🍴 ${this.escapeHtml(recipe.cuisine)}</p>` : ''}
                ${recipe.description ? `<p class="description">${this.escapeHtml(recipe.description)}</p>` : ''}
                <div class="recipe-meta">
                    <span>👥 ${recipe.servings} servings</span>
                    ${recipe.prep_time_minutes ? `<span>⏱️ ${recipe.prep_time_minutes} min prep</span>` : ''}
                    ${recipe.cook_time_minutes ? `<span>🔥 ${recipe.cook_time_minutes} min cook</span>` : ''}
                </div>
                <div class="recipe-actions">
                    <button onclick="uiController.viewRecipe(${recipe.id})" class="btn-small">View</button>
                    <button onclick="uiController.editRecipe(${recipe.id})" class="btn-small">Edit</button>
                    <button onclick="uiController.scaleRecipe(${recipe.id})" class="btn-small">Scale</button>
                    <button onclick="uiController.deleteRecipe(${recipe.id})" class="btn-small btn-danger">Delete</button>
                </div>
            </div>
        `).join('');
    }

    renderPantryItems(items) {
        const container = document.getElementById('pantry-list');
        
        container.innerHTML = items.map(item => `
            <div class="pantry-item">
                <div class="pantry-info">
                    <h4>${this.escapeHtml(item.name)}</h4>
                    <span>${item.quantity} ${this.escapeHtml(item.unit)}</span>
                </div>
                <div class="pantry-actions">
                    <button onclick="uiController.editPantryItem(${item.id})" class="btn-small">Edit</button>
                    <button onclick="uiController.deletePantryItem(${item.id})" class="btn-small btn-danger">Delete</button>
                </div>
            </div>
        `).join('');
    }

    renderShoppingList(items) {
        const container = document.getElementById('shopping-items');
        
        if (items.length === 0) {
            container.innerHTML = '<p class="empty-message">Generate a shopping list by selecting recipes and clicking "Generate"</p>';
            return;
        }

        container.innerHTML = items.map(item => `
            <div class="shopping-item">
                <span class="item-name">${this.escapeHtml(item.name)}</span>
                <span class="item-quantity">${item.quantity} ${this.escapeHtml(item.unit)}</span>
            </div>
        `).join('');
    }

    showRecipeModal(recipe = null) {
        const modal = document.getElementById('recipe-modal');
        const form = document.getElementById('recipe-form');
        
        form.reset();
        document.getElementById('recipe-id').value = recipe ? recipe.id : '';
        document.getElementById('modal-title').textContent = recipe ? 'Edit Recipe' : 'Add Recipe';
        
        if (recipe) {
            document.getElementById('recipe-name').value = recipe.name;
            document.getElementById('recipe-description').value = recipe.description || '';
            document.getElementById('recipe-cuisine').value = recipe.cuisine || '';
            document.getElementById('recipe-servings').value = recipe.servings;
            document.getElementById('recipe-prep-time').value = recipe.prep_time_minutes || '';
            document.getElementById('recipe-cook-time').value = recipe.cook_time_minutes || '';
            
            // Load ingredients
            document.getElementById('ingredients-container').innerHTML = '';
            recipe.ingredients.forEach(ing => {
                this.addIngredientField(ing);
            });
            
            // Load steps
            document.getElementById('steps-container').innerHTML = '';
            recipe.steps.forEach(step => {
                this.addStepField(step);
            });
        } else {
            document.getElementById('ingredients-container').innerHTML = '';
            document.getElementById('steps-container').innerHTML = '';
            this.addIngredientField();
            this.addStepField();
        }
        
        modal.style.display = 'block';
    }

    addIngredientField(ingredient = null) {
        const container = document.getElementById('ingredients-container');
        const div = document.createElement('div');
        div.className = 'ingredient-row';
        div.innerHTML = `
            <input type="text" placeholder="Ingredient name" value="${ingredient ? this.escapeHtml(ingredient.name) : ''}" required>
            <input type="number" step="0.01" placeholder="Quantity" value="${ingredient ? ingredient.quantity : ''}" required>
            <input type="text" placeholder="Unit" value="${ingredient ? this.escapeHtml(ingredient.unit) : ''}" required>
            <button type="button" onclick="this.parentElement.remove()" class="btn-danger btn-small">Remove</button>
        `;
        container.appendChild(div);
    }

    addStepField(step = null) {
        const container = document.getElementById('steps-container');
        const stepNumber = container.children.length + 1;
        const div = document.createElement('div');
        div.className = 'step-row';
        div.innerHTML = `
            <span class="step-number">${stepNumber}.</span>
            <textarea placeholder="Step instruction" required>${step ? this.escapeHtml(step.instruction) : ''}</textarea>
            <button type="button" onclick="this.parentElement.remove()" class="btn-danger btn-small">Remove</button>
        `;
        container.appendChild(div);
    }

    async handleRecipeSubmit(e) {
        e.preventDefault();
        this.showLoading();
        
        try {
            const formData = new FormData(e.target);
            const recipeId = formData.get('recipe-id');
            
            const ingredients = [];
            document.querySelectorAll('#ingredients-container .ingredient-row').forEach(row => {
                const inputs = row.querySelectorAll('input');
                ingredients.push({
                    name: inputs[0].value,
                    quantity: parseFloat(inputs[1].value),
                    unit: inputs[2].value
                });
            });
            
            const steps = [];
            document.querySelectorAll('#steps-container .step-row').forEach((row, index) => {
                const textarea = row.querySelector('textarea');
                steps.push({
                    step_number: index + 1,
                    instruction: textarea.value
                });
            });
            
            const recipeData = {
                name: formData.get('name'),
                description: formData.get('description') || null,
                cuisine: formData.get('cuisine') || null,
                servings: parseInt(formData.get('servings')),
                prep_time_minutes: formData.get('prep_time_minutes') ? parseInt(formData.get('prep_time_minutes')) : null,
                cook_time_minutes: formData.get('cook_time_minutes') ? parseInt(formData.get('cook_time_minutes')) : null,
                ingredients,
                steps
            };
            
            if (recipeId) {
                await RecipeService.updateRecipe(parseInt(recipeId), recipeData);
                this.showSuccess('Recipe updated successfully!');
            } else {
                await RecipeService.createRecipe(recipeData);
                this.showSuccess('Recipe created successfully!');
            }
            
            this.closeModals();
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    async viewRecipe(id) {
        try {
            const recipe = await RecipeService.getRecipeDetails(id);
            alert(this.formatRecipeForView(recipe));
        } catch (error) {
            this.showError(error.message);
        }
    }

    async editRecipe(id) {
        try {
            const recipe = await RecipeService.getRecipeDetails(id);
            this.showRecipeModal(recipe);
        } catch (error) {
            this.showError(error.message);
        }
    }

    async scaleRecipe(id) {
        const factor = prompt('Enter scale factor (e.g., 2 for double, 0.5 for half):');
        if (!factor) return;
        
        try {
            const scaled = await RecipeService.scaleRecipe(id, parseFloat(factor));
            alert(this.formatScaledRecipe(scaled));
        } catch (error) {
            this.showError(error.message);
        }
    }

    async deleteRecipe(id) {
        if (!confirm('Are you sure you want to delete this recipe?')) return;
        
        this.showLoading();
        try {
            await RecipeService.deleteRecipe(id);
            this.showSuccess('Recipe deleted successfully!');
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    toggleRecipeSelection(id) {
        RecipeService.toggleRecipeSelection(id);
    }

    updateSelectedCount(count) {
        const badge = document.querySelector('.selected-badge');
        if (count > 0) {
            badge.textContent = `${count} selected`;
            badge.style.display = 'inline-block';
        } else {
            badge.style.display = 'none';
        }
    }

    showPantryModal(item = null) {
        const modal = document.getElementById('pantry-modal');
        const form = document.getElementById('pantry-form');
        
        form.reset();
        document.getElementById('pantry-id').value = item ? item.id : '';
        document.getElementById('pantry-modal-title').textContent = item ? 'Edit Pantry Item' : 'Add Pantry Item';
        
        if (item) {
            document.getElementById('pantry-name').value = item.name;
            document.getElementById('pantry-name').readOnly = true;
            document.getElementById('pantry-quantity').value = item.quantity;
            document.getElementById('pantry-unit').value = item.unit;
        } else {
            document.getElementById('pantry-name').readOnly = false;
        }
        
        modal.style.display = 'block';
    }

    async handlePantrySubmit(e) {
        e.preventDefault();
        this.showLoading();
        
        try {
            const formData = new FormData(e.target);
            const pantryId = formData.get('pantry-id');
            
            const itemData = {
                name: formData.get('name'),
                quantity: parseFloat(formData.get('quantity')),
                unit: formData.get('unit')
            };
            
            if (pantryId) {
                delete itemData.name;
                await PantryService.updatePantryItem(parseInt(pantryId), itemData);
                this.showSuccess('Pantry item updated successfully!');
            } else {
                await PantryService.createPantryItem(itemData);
                this.showSuccess('Pantry item added successfully!');
            }
            
            this.closeModals();
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    async editPantryItem(id) {
        try {
            const item = await PantryAPI.getById(id);
            this.showPantryModal(item);
        } catch (error) {
            this.showError(error.message);
        }
    }

    async deletePantryItem(id) {
        if (!confirm('Are you sure you want to delete this pantry item?')) return;
        
        this.showLoading();
        try {
            await PantryService.deletePantryItem(id);
            this.showSuccess('Pantry item deleted successfully!');
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    async generateShoppingList() {
        this.showLoading();
        try {
            await ShoppingListService.generateShoppingList();
            this.showSuccess('Shopping list generated!');
            this.switchView('shopping');
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    exportShoppingList() {
        try {
            ShoppingListService.downloadShoppingList();
            this.showSuccess('Shopping list exported!');
        } catch (error) {
            this.showError(error.message);
        }
    }

    closeModals() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.style.display = 'none';
        });
    }

    formatRecipeForView(recipe) {
        let text = `${recipe.name}\n${'='.repeat(40)}\n\n`;
        if (recipe.description) text += `${recipe.description}\n\n`;
        if (recipe.cuisine) text += `Cuisine: ${recipe.cuisine}\n`;
        text += `Servings: ${recipe.servings}\n`;
        if (recipe.prep_time_minutes) text += `Prep Time: ${recipe.prep_time_minutes} min\n`;
        if (recipe.cook_time_minutes) text += `Cook Time: ${recipe.cook_time_minutes} min\n`;
        
        text += `\nIngredients:\n${'-'.repeat(40)}\n`;
        recipe.ingredients.forEach(ing => {
            text += `• ${ing.quantity} ${ing.unit} ${ing.name}\n`;
        });
        
        text += `\nSteps:\n${'-'.repeat(40)}\n`;
        recipe.steps.forEach(step => {
            text += `${step.step_number}. ${step.instruction}\n`;
        });
        
        return text;
    }

    formatScaledRecipe(scaled) {
        let text = `Scaled Recipe\n${'='.repeat(40)}\n\n`;
        text += `Original Servings: ${scaled.original_servings}\n`;
        text += `Scaled Servings: ${scaled.scaled_servings}\n`;
        text += `Scale Factor: ${scaled.scale_factor}\n\n`;
        text += `Ingredients:\n${'-'.repeat(40)}\n`;
        scaled.ingredients.forEach(ing => {
            text += `• ${ing.quantity} ${ing.unit} ${ing.name}\n`;
        });
        return text;
    }

    showLoading() {
        document.getElementById('loading').style.display = 'flex';
    }

    hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }

    showError(message) {
        alert(`Error: ${message}`);
    }

    showSuccess(message) {
        alert(message);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize UI Controller and expose globally for inline event handlers
let uiController;
document.addEventListener('DOMContentLoaded', () => {
    uiController = new UIController();
    // Make it globally accessible for inline onclick handlers
    window.uiController = uiController;
});
