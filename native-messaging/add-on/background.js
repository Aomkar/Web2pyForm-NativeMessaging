	

		var port = browser.runtime.connectNative("GrabJSON");


var msg_from_native = "";








		function onResponse(response) {
            
            msg_from_native = response;
            console.log("Received from native app : " + msg_from_native);   
            
            
            browser.tabs.query({
			  	currentWindow: true,
			  	active: true
			}).then(sendMessageToTabs).catch(onError);
            
		}


		function onError(error) {
		  console.log(`Error: ${error}`);
		}






        function sendMessageToTabs(tabs) {
            for (let tab of tabs) {
                browser.tabs.sendMessage(
                    tab.id,
                    {greeting: msg_from_native}
                ).then(response => {
                    
                    console.log(response);
                    
                    console.log("Promise  >>> "+response+" <<<  Recieved");
                }).catch(onError);
            }
		}
        





browser.runtime.onMessage.addListener(notify);

function notify(message) {
    
    console.log("Background script : Received content script's message   :  "+message);
    
    //console.log("jsondata is : "+jsondata)
    
    var jsondata = message;
    
    if(message != "INVALID") {
	
		var sending = browser.runtime.sendNativeMessage("GrabJSON", jsondata);
		  sending.then(onResponse, onError);
	
	}
    
}

//-----------------------------------------------------





























