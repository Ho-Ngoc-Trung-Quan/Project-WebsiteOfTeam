const express = require('express');
const path = require('path');
const app = express();
const fs = require('fs');

app.use(express.static(path.join(__dirname)))

app.get('/', (req, res) => {
    fs.readFile('./default.html', 'utf8', (err, html) => {
        if (err){
            res.status(500).send("Sorry, out of order");
        }
        res.send(html);
    })
})

app.listen(process.env.PORT || 3000, () =>{
    console.log('Server is running');
})