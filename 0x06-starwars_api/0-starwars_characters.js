#!/usr/bin/node
// stringify movie characters

const apiRequest = require('request');
apiRequest.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, req, res) => {
  if (err) console.log(err);

  if (req) {
    const data = JSON.parse(res);

    for (const x of data.xs) {
      apiRequest.get(x, (err1, req1, res1) => {
        if (err1) console.log(err1);
        if (req1) {
          const names = JSON.parse(res1);
          console.log(names.name);
        }
      });
    }
  }
});
