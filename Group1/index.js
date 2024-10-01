const express = require('express');
const app = express();
const {readFile, readFileAsync} = require('fs');

app.get('/', (req, res) => {
    readFile('default.html', 'utf8', (err, data) => {
        if (err){
            res.status(500).send("Sorry, out of order");
        }
        res.send(data)
    })
})

app.listen(process.env.PORT || 3000, () =>{
    console.log("Server is running");
})