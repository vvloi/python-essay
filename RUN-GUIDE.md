# 🚀 Hướng dẫn chạy ứng dụng (Backend + Frontend)

## 📋 Prerequisites (Yêu cầu)

- Python 3.8+
- Node.js 16+ và npm
- Git

---

## 🔧 Backend (FastAPI + Python)

### 1. Activate Virtual Environment
```powershell
# Tại thư mục gốc project (E:\sources\python-essay)
.\venv\Scripts\Activate.ps1
```

### 2. Khởi động Backend Server
```powershell
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Kết quả:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [xxxx]
INFO:     Application startup complete.
```

**URLs quan trọng:**
- 🌐 Backend API: http://localhost:8000
- 📚 API Docs (Swagger): http://localhost:8000/docs
- 💚 Health Check: http://localhost:8000/api/health

**Dừng server:** Nhấn `Ctrl+C` trong terminal

---

## ⚛️ Frontend (React + TypeScript + Vite)

### Option 1: Development Mode (HMR - Hot Module Replacement)

**Khuyên dùng khi đang dev** - có live reload tự động

```powershell
# Mở terminal mới
cd E:\sources\python-essay\frontend
npm run dev
```

**Kết quả:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**Frontend Dev Server:** http://localhost:5173

**Lưu ý:**
- Frontend dev server chạy riêng (port 5173)
- Vite tự động proxy API calls đến backend (port 8000)
- Khi sửa code `.tsx`, `.ts`, `.scss` → tự động reload

**Dừng server:** Nhấn `Ctrl+C` trong terminal

---

### Option 2: Production Build (Backend serve Frontend)

**Khuyên dùng khi test production hoặc demo**

```powershell
# Tại thư mục frontend
cd E:\sources\python-essay\frontend
npm run build
```

**Kết quả:**
```
vite v5.x.x building for production...
✓ xxx modules transformed.
dist/index.html                  x.xx kB
dist/assets/index-[hash].js      xx.xx kB
✓ built in xxxs
```

**Sau khi build xong:**
- Folder `frontend/dist` được tạo ra
- Backend tự động serve static files từ `frontend/dist`
- Truy cập app tại: http://localhost:8000 (cùng port với backend)

**Rebuild:** Chạy lại `npm run build` nếu sửa code frontend

---

## 🎯 Workflow đầy đủ (Recommended)

### Lần đầu setup:
```powershell
# 1. Clone/pull code
git checkout feat/frontend-ts-scss

# 2. Setup backend
cd E:\sources\python-essay
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head

# 3. Setup frontend
cd frontend
npm install
```

### Mỗi lần dev (2 terminal):

**Terminal 1 - Backend:**
```powershell
cd E:\sources\python-essay
.\venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```powershell
cd E:\sources\python-essay\frontend
npm run dev
```

**Truy cập:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 🐛 Troubleshooting

### Backend không chạy được:

**Lỗi:** `uvicorn: The term 'uvicorn' is not recognized`
```powershell
# Fix: Activate venv trước
.\venv\Scripts\Activate.ps1
```

**Lỗi:** `No module named 'backend'`
```powershell
# Fix: Chắc chắn đang ở thư mục gốc (E:\sources\python-essay)
cd E:\sources\python-essay
```

**Lỗi:** `Port 8000 already in use`
```powershell
# Fix: Dùng port khác
uvicorn backend.main:app --reload --port 8001
```

### Frontend không chạy được:

**Lỗi:** `npm: command not found` hoặc `node: command not found`
```powershell
# Fix: Cài Node.js từ https://nodejs.org/
```

**Lỗi:** TypeScript errors trong terminal
```powershell
# Fix: Chạy lại npm install
cd frontend
npm install
```

**Lỗi:** `EADDRINUSE: address already in use :::5173`
```powershell
# Fix: Dừng process cũ hoặc dùng port khác
# Vite sẽ tự động chọn port khác (5174, 5175, ...)
```

### API calls không hoạt động:

**Khi dùng dev mode (port 5173):**
- Vite tự động proxy `/api` → `http://localhost:8000/api`
- Kiểm tra backend có đang chạy không

**Khi dùng production build:**
- Đảm bảo đã chạy `npm run build`
- Backend serve từ `frontend/dist`
- Truy cập http://localhost:8000 (không phải 5173)

---

## 📝 Tóm tắt lệnh nhanh

### Backend:
```powershell
.\venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Dev:
```powershell
cd frontend
npm run dev
```

### Frontend Production:
```powershell
cd frontend
npm run build
# Sau đó visit http://localhost:8000
```

---

## 🔗 URLs tham khảo

| Service | Dev Mode | Production Mode |
|---------|----------|-----------------|
| Frontend | http://localhost:5173 | http://localhost:8000 |
| Backend API | http://localhost:8000 | http://localhost:8000 |
| API Docs | http://localhost:8000/docs | http://localhost:8000/docs |
| Health Check | http://localhost:8000/api/health | http://localhost:8000/api/health |

---

**Chúc bạn code vui vẻ! 🚀**
