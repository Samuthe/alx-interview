#!/usr/bin/node
// stringify movie characters

const request = require('request');
const arg = process.argv[2];

async function resUrl (dataUrl) {
  return new Promise(function (resolve, reject) {
    request(dataUrl, function (err, res, body) {
      resolve(JSON.parse(body).name);
      if (err) throw err;
    });
  });
}

async function chars () {
  return new Promise(function (resolve, reject) {
    request(`https://swapi-api.alx-tools.com/api/films/${arg}`, function (err, res, bod) {
      resolve(JSON.parse(bod).characters);
      if (err) throw err;
    });
  });
}

async function names () {
  const mychars = await chars();
  for (let i = 0; i < mychars.length; i++) {
    console.log(await resUrl(mychars[i]));
  }
}

names();
