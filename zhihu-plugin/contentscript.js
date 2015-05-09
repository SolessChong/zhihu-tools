var script = document.createElement('script');
script.setAttribute("type", "text/javascript");
script.setAttribute("async", true);
script.setAttribute("src", chrome.extension.getURL("require-jquery.js"));  
//Assuming your host supports both http and https
var head = document.head || document.getElementsByTagName( "head" )[0] || document.documentElement;
head.insertBefore(script, head.firstChild);

alert('1');