const express = require("express");
const { Client } = require("pg");
const swaggerUi = require("swagger-ui-express");
const swaggerDocument = require("./swagger.json");
const admin = require("./infrastructure/routes/admin");

const app = express();

var client;
if (process.env.NODE_ENV !== 'stage') {
    client = new Client({
      connectionString: process.env.DATABASE_URL,
      query_timeout: 1000,
      statement_timeout: 1000,
      ssl: false
    }); 
} else {
    client = new Client({
      connectionString: process.env.DATABASE_URL,
      query_timeout: 1000,
      statement_timeout: 1000,
      ssl: {
        rejectUnauthorized: false
      }
    });
}

client.connect();

app.use("/admin", admin);
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.get("/ping", (req, res) => res.send("Pong!"));
app.get("/status", (req, res) => client.query("SELECT NOW()", (err) => res.send({ service: "UP", db: err ? "DOWN" : "UP" })));

app.listen(process.env.PORT, () => {
  console.log(`App running on port ${process.env.PORT}`);
});