import {db} from './Firebase.js';
import * as fs from 'fs';
import {setDoc,collection, doc} from "firebase/firestore";



const filedir = './vocabulario.txt';
fs.readFile(filedir, (error, data) => {
    data.toString("utf-8").split("\n").forEach( async (line,index) => {
        // Add a new document in collection 
       
        await setDoc(doc(db, "Papiamento-data",line), {
            id: index,
            papiamento: line,
            isNotPapiamento: 0,
            isPapiamento: 0,
            english:[],
        });
        
        console.log(index);

    });
});

// await setDoc(doc(db, "Papiamento-data",""), {
//     papiamento: "bo mama ta gordo",
//     isNotPapiamento: 0,
//     isPapiamento: 0,
//     english:[],
// });
console.log("all data has been uploaded, good luck and good job!")
