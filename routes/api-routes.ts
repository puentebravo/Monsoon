import { PrismaClient } from "@prisma/client"
import {Application, Request, Response } from "express"

const prisma = new PrismaClient()

module.exports = (app: Application) => {
    app.get("/api/getWeather", async (req: Request, res: Response) => {
       
        const weatherData = await prisma.savedSearches.findMany();

        res.json(weatherData)
    })
}