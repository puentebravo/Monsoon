import { PrismaClient } from "@prisma/client"
import {Application, Request, Response } from "express"

const prisma = new PrismaClient()

module.exports = (app: Application) => {
    app.get("/api/getSavedWeather", async (req: Request, res: Response) => {
       
        const weatherData = await prisma.savedSearches.findMany();

        res.json(weatherData)
    })

    app.post("/api/saveSearch", async (req: Request, res: Response) => {
        const savedSearch = await prisma.savedSearches.create({
            data: {
                city: req.body.city,
                dateTime: req.body.dateTime,
                feel: req.body.feel,
                high: req.body.high,
                humidity: req.body.humidity,
                lat: req.body.lat,
                long: req.body.long,
                low: req.body.low,
                sunrise: req.body.sunrise,
                temp: req.body.temp
            }
        })

        res.json(savedSearch)
    })


}