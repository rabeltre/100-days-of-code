console.log('May Node be with you')
const express = require('express');
const app  = express();
const bodyParser= require('body-parser');


const MongoClient= require('mongodb').MongoClient

var db

MongoClient.connect('mongodb://rabeltre:rabeltre@ds111648.mlab.com:11648/rabeltre', function(err, database){
  if (err) return console.log(err)
  db = database
  app.listen(3000, function(){
    console.log('listening on 3000')
  })
})


app.use(bodyParser.urlencoded({extended: true}))

app.get('/', function (req, res) {
    // res.send('Hello word')
  res.sendFile(__dirname + '/index.html')
})

app.post('/quotes', function (req, res) {
    db.collection('quotes').insert(req.body, function (err, result) {
        if (err) return console.log(err)

        console.log('saved to database')
        res.redirect('/')
    })
});

app.get('/getQuotes', function (req, res) {
    db.collection('quotes').find().toArray(function (err, result) {
        res.send(result);
    })
})
