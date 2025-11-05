# Frontend (React + TypeScript + TailwindCSS + SCSS)

Modern frontend built with **Vite + React 18 + TypeScript + TailwindCSS + SCSS** following **3-layer architecture**.

## 🏗️ Tech Stack

- **React 18**: Component-based UI framework
- **TypeScript 5**: Type-safe JavaScript with strong typing
- **Vite 5**: Fast build tool and dev server with HMR
- **TailwindCSS 3**: Utility-first CSS framework
- **SCSS**: CSS preprocessor for enhanced styling
- **PostCSS**: CSS transformation tool

## 📁 Project Structure (3-Layer Architecture)

```
src/
├── data/                      # Data Access Layer
│   ├── ApiClient.ts          # HTTP client wrapper
│   ├── RecipeAPI.ts          # Recipe endpoints
│   ├── PantryAPI.ts          # Pantry endpoints
│   └── ShoppingListAPI.ts    # Shopping list endpoints
├── business/                  # Business Logic Layer
│   └── StateManager.ts       # Centralized state management
├── components/                # Presentation Layer
│   ├── RecipeList.tsx        # Recipe list component
│   ├── Pantry.tsx            # Pantry component
│   └── ShoppingList.tsx      # Shopping list component
├── App.tsx                    # Main app component
├── main.tsx                   # App entry point
├── index.scss                 # Tailwind + custom SCSS
└── types.ts                   # TypeScript type definitions
```

## 🚀 Quick Start

### 1. Install dependencies
```bash
npm install
```

### 2. Run development server
```bash
npm run dev
```
- Dev server runs at: **http://localhost:5173**
- Hot Module Replacement (HMR) enabled
- TypeScript type checking in IDE

### 3. Build for production
```bash
npm run build
```
- Output: `frontend/dist/`
- Backend will automatically serve this folder at **http://localhost:8000**

### 4. Preview production build locally
```bash
npm run preview
```

## 🛠️ Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server with HMR |
| `npm run build` | Build for production (output: `dist/`) |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint (if configured) |

## 🎨 Styling with Tailwind + SCSS

### Tailwind Configuration
- Config file: `tailwind.config.cjs`
- PostCSS config: `postcss.config.cjs`
- Entry point: `src/index.scss`

### Using Tailwind classes
```tsx
<div className="bg-blue-500 text-white p-4 rounded-lg">
  Hello Tailwind!
</div>
```

### Custom SCSS
Add custom styles in `src/index.scss`:
```scss
@tailwind base;
@tailwind components;
@tailwind utilities;

// Your custom SCSS here
.my-custom-class {
  @apply bg-gradient-to-r from-blue-500 to-purple-600;
}
```

## 📝 TypeScript Configuration

TypeScript is configured in `tsconfig.json`:
- Strict mode enabled
- React JSX transform
- Path aliases supported
- Type checking for all `.ts` and `.tsx` files

### Type Safety Example
```typescript
// src/types.ts
export interface Recipe {
  id: number
  title: string
  servings: number
  ingredients: Ingredient[]
  steps: Step[]
}

// Usage in component
const recipe: Recipe = await RecipeAPI.getById(1)
```

## 🔌 API Integration

All API calls are in the **data layer** (`src/data/`):

```typescript
// Example: Fetch recipes
import { RecipeAPI } from './data/RecipeAPI'

const recipes = await RecipeAPI.getAll()
```

The backend API base URL is `/api` (proxied by Vite in dev mode).

## 🏗️ 3-Layer Architecture

### Data Layer (`src/data/`)
- **Purpose**: HTTP communication with backend
- **Files**: `ApiClient.ts`, `RecipeAPI.ts`, `PantryAPI.ts`, `ShoppingListAPI.ts`
- **Responsibility**: Pure API calls, no business logic

### Business Layer (`src/business/`)
- **Purpose**: State management and business logic
- **Files**: `StateManager.ts`
- **Responsibility**: Manage application state, notify components of changes

### Presentation Layer (`src/components/`)
- **Purpose**: UI components and user interaction
- **Files**: `*.tsx` React components
- **Responsibility**: Render UI, handle user events, display data

## 🔧 Development Tips

### Hot Module Replacement (HMR)
Vite provides instant HMR. Changes to `.tsx`, `.ts`, `.scss` files are reflected immediately without full page reload.

### TypeScript Errors
TypeScript errors appear in:
- VS Code (with TypeScript extension)
- Terminal (during `npm run dev` or `npm run build`)

### Debugging
Use React DevTools browser extension for component inspection.

## 📦 Production Build

The production build is optimized:
- ✅ Code splitting
- ✅ Tree shaking (removes unused code)
- ✅ Minification
- ✅ CSS optimization via PostCSS
- ✅ Asset hashing for cache busting

Output files in `dist/`:
```
dist/
├── index.html
├── assets/
│   ├── index-[hash].js
│   ├── index-[hash].css
│   └── [other assets]
```

## 🌐 Backend Integration

The FastAPI backend (`backend/main.py`) serves the frontend:
- If `frontend/dist` exists → serves static files from there
- Otherwise → serves `frontend/` (for legacy or dev fallback)

After building (`npm run build`), visit **http://localhost:8000** to see the app.

## 🚀 Deployment

### Option 1: Backend serves frontend (recommended)
1. Build frontend: `npm run build`
2. Deploy backend with `frontend/dist/` included
3. Backend serves everything at one URL

### Option 2: Separate frontend hosting (CDN/Netlify/Vercel)
1. Update API base URL in `src/data/ApiClient.ts`:
   ```typescript
   const API_BASE_URL = 'https://your-backend.com/api'
   ```
2. Build: `npm run build`
3. Deploy `dist/` to CDN/static hosting

## 📚 Learn More

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [SCSS Guide](https://sass-lang.com/guide)

---

**Built with 3-Layer Architecture** 🏗️  
Clean separation: Data → Business → Presentation
