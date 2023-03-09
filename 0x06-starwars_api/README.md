# 0x06 Starwars API

This script retrieves the character names from a Star Wars movie based on the movie ID using the Star Wars API.

## Prerequisites

- Node.js (version 10.14.x or above)* 
- request

* For a detailed guid on how to setup node.js click [here](https://www.pluralsight.com/guides/getting-started-with-nodejs).

## Installation

1. Clone the repository:
```
git clone [https://github.com/<username>/starwars-api.git](https://github.com/Amha-Endrayes/alx-interview/0x06-starwars_api)
```
  
2. Navigate to the project directory:
```
cd 0x06-starwars_api
```
3. Install the dependencies:
```
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Usage

To retrieve the character names from a Star Wars movie, run the script with the movie ID as an argument:
```
node 0-starwars_characters.js <movie_id>
```

For example, to retrieve the character names from "Return of the Jedi", which has a movie ID of 3, run the following command:
```
$root@ubuntu: node 0-starwars_characters.js 1

Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna

$root@ubuntu:
```
