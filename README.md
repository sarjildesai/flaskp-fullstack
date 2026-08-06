# Express Frontend + Flask Backend (Dockerized)

A simple contact form served by a **Node.js/Express** frontend, submitted via
`fetch()` to a **Flask** backend, both containerized and connected through
Docker Compose.

## Folder structure

```
flaskp-fullstack/
├── backend/
│   ├── app.py            # Flask API (/ and /process)
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── server.js         # Express server
│   ├── views/index.ejs   # The form
│   ├── public/style.css
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yaml
└── .gitignore
```

## How it works

1. Express (`frontend/server.js`) renders `index.ejs`, which contains a form
   with **name**, **email**, and **message** fields (same pattern as the
   single-field form in Flask Assignment 2, extended slightly).
2. On submit, client-side JS sends a `POST` request as JSON to the Flask
   backend's `/process` endpoint (`http://localhost:5000/process`).
3. Flask validates the payload and returns a JSON response, which is
   displayed back on the page — no page reload.

This was tested locally (frontend on port 3000, backend on port 5000) and
confirmed working end-to-end: the form renders, submits, and displays the
backend's response.

## Running locally without Docker (for dev/testing)

```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py            # http://localhost:5000

# Frontend (separate terminal)
cd frontend
npm install
node server.js            # http://localhost:3000
```

## Running with Docker Compose

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend:  http://localhost:5000

Stop with `docker-compose down`.

## Building and pushing images to Docker Hub

Replace `<dockerhub-username>` with your Docker Hub username.

```bash
# Backend image
docker build -t <dockerhub-username>/flaskp-backend:latest ./backend
docker push <dockerhub-username>/flaskp-backend:latest

# Frontend image
docker build -t <dockerhub-username>/flaskp-frontend:latest ./frontend
docker push <dockerhub-username>/flaskp-frontend:latest
```

Log in first if needed: `docker login`

## Pushing the code to GitHub

```bash
git init
git add .
git commit -m "Express frontend + Flask backend with Docker Compose"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

`.gitignore` already excludes `node_modules/`, Python `venv`/`__pycache__`,
and `.vscode/` so none of that gets committed.

## Screenshots to capture for submission

Take screenshots of:
1. `docker-compose up --build` running successfully in your terminal.
2. `docker ps` showing both containers running.
3. The form in the browser at `http://localhost:3000`.
4. The success message after submitting the form.
5. `docker push` output for both images.
6. Your Docker Hub repository page showing both images.

(Two real screenshots of the working form — `shot_form_filled.png` and
`shot_form_success.png` — are included in this submission as a reference
for what steps 3–4 should look like.)
