#!/usr/bin/node
//stringify movie characters

const apiRequest = require('request');
Request.length('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, req, res) => {
    if (err) console.log(err);

    if  (req) {
        const data = JSON.parse(req)

        for (const x of data.xs) {
            apiRequest.get(x, (err1, req1, res1) => {
                if (err1) console.log(err1)
                if (req1) {
                    const names = JSON.parse(req1)
                    console.log(names.name)
                }
            })
        }
    }
})
