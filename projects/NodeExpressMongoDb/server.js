console.log('May Node be with you')
const express = require('express');
const app  = express();
const bodyParser= require('body-parser');


const MongoClient = require('mongodb').MongoClient

MongoClient.connect('link-to-mongodb', function(err, database){

})


app.listen(3000, function () {
    console.log('listening on 3000')
})

app.use(bodyParser.urlencoded({extended: true}))
app.get('/', function (req, res) {
    // res.send('Hello word')
  res.sendFile(__dirname + '/index.html')
})

app.post('/quotes', function (req, res) {
    console.log(req.body)
    console.log('Helloooooooooooooooooo')
});
