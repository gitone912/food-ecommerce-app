import { initializeApp, getApp, getApps } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

// const apps = getApps();

const firebaseConfig = {
  apiKey: "AIzaSyDMzwYrxLaZsBceNdHkypbZSBLaw9mMx7A",
  authDomain: "kolz108.firebaseapp.com",
  databaseURL: "https://kolz108-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "kolz108",
  storageBucket: "kolz108.firebasestorage.app",
  messagingSenderId: "747784222324",
  appId: "1:747784222324:web:8f09d5536ff888457f4321",
  measurementId: "G-YS0L9V9NMV"
};


// Initialize Firebase
const app = getApps().length > 0 ? getApp() : initializeApp(firebaseConfig);

// database
const firestore = getFirestore(app);
const storage = getStorage(app);

export { app, firestore, storage };
