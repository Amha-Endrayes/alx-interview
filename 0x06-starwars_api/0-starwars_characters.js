#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function(error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characterUrls = JSON.parse(body).characters;

    const printCharacterNames = (urls) => {
      if (urls.length === 0) {
        return;
      }

      const characterUrl = urls.shift();
      request(characterUrl, function(err, res, html) {
        if (err) {
          console.error(err);
        } else {
          const characterName = JSON.parse(html).name;
          console.log(characterName);
          printCharacterNames(urls);
        }
      });
    };

    printCharacterNames(characterUrls);
  }
});
