const express = require("express");
const app = express();
const version = "v0.0";

app.get("/health", (req, res) => {
  res.send({ success: true, message: "App is working" });
});

app.get("/", (req, res) => {
    res.send(version + ' Hello World!');
});

app.get("/kill", (req,res) => {
    // this route is designed to hang the application
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on PORT ${PORT}`);
});
