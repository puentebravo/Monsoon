import {Application, Request, Response } from "express"

module.exports = (app: Application) => {
    app.get("/api/getWeather", (req: Request, res: Response) => {
        console.log("Route hit.")
    })
}