#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the movie API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the API endpoint
request(url, function (error, response, body) {
  // If there's an error, print it to the console
  if (error) {
    console.error(error);
  } else {
    // Extract the character URLs from the response body
    const characterUrls = JSON.parse(body).characters;

    // Define a function to print the names of the characters
    const printCharacterNames = (urls) => {
      // If there are no more character URLs to process, return
      if (urls.length === 0) {
        return;
      }

      // Get the next character URL from the array
      const characterUrl = urls.shift();

      // Make a request to the character API endpoint
      request(characterUrl, function (err, res, html) {
        // If there's an error, print it to the console
        if (err) {
          console.error(err);
        } else {
          // Extract the character name from the response body
          const characterName = JSON.parse(html).name;
          // Print the character name to the console
          console.log(characterName);
          // Recursively call the printCharacterNames function with the remaining URLs
          printCharacterNames(urls);
        }
      });
    };

    // Call the printCharacterNames function with the character URLs
    printCharacterNames(characterUrls);
  }
});
