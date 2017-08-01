document.body.style.border = "5px solid blue";

//----------------------------------------


console.clear();



//------------------------------------

//Function to validate json...

function isJSON(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}
//------------------------------------




var jsondata = "";
// Json data (RAO) will come from the page script...



//------------------
// Receiving the RAO from the page script

window.addEventListener("message", (event) => {
    if (event.source == window &&
        event.data &&
        event.data.direction == "from-page-script") {
            
            jsondata = event.data.message;
            jsondata = jsondata.trim();
        
        
        // Validate this json obtained from the page script...
            var isvalid = isJSON(jsondata);
        
        
        
            var msg = "";



            if (isvalid) {
               
                console.log("Valid JSON");
                msg = jsondata;	
                browser.runtime.sendMessage(msg);

            } else {
                
                console.log("INvalid JSON :( ");
                msg = "INVALID";
                browser.runtime.sendMessage(msg);
                
            }    
       
    }
});



//----------------------------------------------

// Getting the response (from native) from the background script... 


var msg_from_native = "";



browser.runtime.onMessage.addListener(request => {

    //---------------------------------------
    msg_from_native = request.greeting;
    //---------------------------------------
    
    console.log("Content script received from background script : "+msg_from_native);
    
    /*
    console.log(message);
    console.log(message["status"]);
    if (message["status"] === "token not present"){
            browser.runtime.sendMessage(jsondata);		
    }
    if (message["status"] === "pin not correct"){
            browser.runtime.sendMessage(jsondata);		
    }
    else if (message["status"] === "success"){
        window.postMessage({
            direction: "from-content-script",
            message: message}, "*");
    }
    */


    window.postMessage({
        direction: "from-content-script",
        message: msg_from_native
    }, "*");

    
    
    
    return Promise.resolve({response: "Ok"});
    
});

























