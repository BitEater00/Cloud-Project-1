var registerButton = document.getElementById("UpdateButton")
var uploadButton = document.getElementById("uploadImg")
var firebaseConfig = {
    'apiKey': "AIzaSyBEBdlgDtMjwb0SfE-s1AwJGVuOxVFBjaw",
    'authDomain': "cloudproject-bcd7008.firebaseapp.com",
    'databaseURL': "https://cloudproject-bcd7008-default-rtdb.firebaseio.com",
    'projectId': "cloudproject-bcd7008",
    'storageBucket': "cloudproject-bcd7008.appspot.com",
    'messagingSenderId': "1011436028629",
    'appId': "1:1011436028629:web:bc858dfc883bd3cabb985c",
    'measurementId': "G-EJYZXZDTQV"
};
firebase.initializeApp(firebaseConfig);
var storage = firebase.storage();
var storageRef = firebase.storage().ref();

uploadButton.addEventListener("click" , function() {

    pattern = ".{36}[?]"
    str = document.getElementById("imgUrl").value
    imgId =  str.match(pattern).toString()
    imgId = imgId.substring(0, imgId.length-1)
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader()
    
    if(file){
        reader.readAsDataURL(file);
        var path = "/Club/" + String(imgId);
        var ref = storage.ref(path);
        ref.put(file).then((snapshot) => {
            console.log('Uploaded img');
            alert("Image Upload Successful.")
        });
    }

});