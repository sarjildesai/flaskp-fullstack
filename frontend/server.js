const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));
app.use(express.urlencoded({ extended: true }));

// Backend URL is injected via docker-compose environment variable.
// Falls back to localhost for running the frontend outside Docker.
const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:5000";

app.get("/", (req, res) => {
  res.render("index", { backendUrl: BACKEND_URL });
});

app.listen(PORT, () => {
  console.log(`Frontend server running on http://localhost:${PORT}`);
  console.log(`Talking to Flask backend at ${BACKEND_URL}`);
});
