import {db} from './Firebase.js';
import * as fs from 'fs';
import {addDoc,collection} from "firebase/firestore";



const filedir = './vocabulario.txt';
fs.readFile(filedir, (error, data) => {
    data.toString("utf-8").split("\n").forEach( async line => {
        // Add a new document in collection 
        await addDoc(collection(db, "Papiamento-data"), {
            papiamento: line,
            isNotPapiamento: 0,
            isPapiamento: 0,
            english:[],
        });

    });
});

// await addDoc(collection(db, "Papiamento-data"), {
//     papiamento: "saki ta un palabra",
//     isNotPapiamento: 0,
//     isPapiamento: 0,
//     english:[],
// });
console.log("all data has been uploaded, good luck and good job!")
