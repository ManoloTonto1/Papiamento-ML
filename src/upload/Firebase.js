// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { getFirestore } from "firebase/firestore"

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCZ_U92dgrXqejfoyvtFU5igFpxujp5T6k",
  authDomain: "react-test-1-1f83c.firebaseapp.com",
  projectId: "react-test-1-1f83c",
  storageBucket: "react-test-1-1f83c.appspot.com",
  messagingSenderId: "149387264897",
  appId: "1:149387264897:web:ca7281b3c49c23ad411e80",
  measurementId: "G-2PKX2N8FBP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
//const analytics = getAnalytics(app);
//const auth = getAuth(app);
//const user = auth.currentUser;
const db = getFirestore();

// onAuthStateChanged(auth, user =>{
//   if(user !== null){
//     console.log("user logged in");
//   }
//   else{
//     console.log("No user signed in");
//   }
// })



export { app, db };