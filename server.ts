import { PrismaClient } from "@prisma/client";
import {Request, Response } from "express"

const express = require("express");
const path = require("path");
const PORT = process.env.PORT || 3001;
const app = express();
const prisma = new PrismaClient();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
require("./routes/api-routes")(app)

if (process.env.NODE_ENV === "production") {
  app.use(express.static("./client/public"));
}

app.get("*", function (req: Request, res: Response) {
  res.sendFile(path.join(__dirname, "./client/build/index.html"));
});

app.listen(PORT, () => {
  console.log(`Server now listening on ${PORT}. Check localhost:`, PORT);
});
