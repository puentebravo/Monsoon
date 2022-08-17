// import { PrismaClient } from "@prisma/client";
import {Application, Request, Response } from "express"

const express = require("express");
const path = require("path");
const PORT: string | number = process.env.PORT || 3001;
const app: Application = express();


app.use(express.urlencoded({ extended: true }));
app.use(express.json());


if (process.env.NODE_ENV === "production") {
  app.use(express.static("./client/public"));
}

require("./routes/api-routes.js")(app)

app.get("*", function (req: Request, res: Response) {
  res.sendFile(path.join(__dirname, "./client/build/index.html"));
});

app.listen(PORT, () => {
  console.log(`Server now listening on ${PORT}. Check localhost:`, PORT);
});
