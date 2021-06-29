var registerButton = document.getElementById("RegisterButton")
registerButton.style.display = "None"
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

function generateUUID() {
    var d = new Date().getTime();
    var d2 = (performance && performance.now && (performance.now()*1000)) || 0;
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16;
        if(d > 0){
            r = (d + r)%16 | 0;
            d = Math.floor(d/16);
        } else {
            r = (d2 + r)%16 | 0;
            d2 = Math.floor(d2/16);
        }
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
}

uploadButton.addEventListener("click" , function() {

    id = generateUUID();
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader()
    
    if(file){
        reader.readAsDataURL(file);
        var path = "/Club/" + String(id);
        var ref = storage.ref(path);
        ref.put(file).then((snapshot) => {
            console.log('Uploaded img');
            storageRef.child(path).getDownloadURL().then((url) => {
                document.getElementById("imgUrl").value = url
            });
            alert("Image Upload Successful")
            registerButton.style.display = ""
        });
    }

});