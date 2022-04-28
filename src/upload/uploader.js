//import {db} from './Firebase';
const fs = require('fs');

const filedir = './sample.txt';
fs.readFile(filedir,(error, data)=>{
    console.log(data.toString("utf-8"));
})

