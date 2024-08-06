#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

function exactOrder(actors, index) {
  if (index === actors.length) {
    return;
  }
  request(actors[index], function (err, res, body) {
    if (err) {
      console.error('Error:', err);
      return;
    }
    console.log(JSON.parse(body).name);
    exactOrder(actors, index + 1);
  });
}

