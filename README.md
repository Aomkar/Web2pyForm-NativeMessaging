# Web2pyForm-NativeMessaging

1. Fill the Leave_Application form /default/index.html
2. After submitting this form, the form data will be stored in the database (in a table named 'Leave_Application') you'll be redirected to      /default/jsonobject.html
   This page will show the json encoding of the filled form.
   It will send this json object, to the native application (on the user's computer) /app/GrabJSON.py
   (Assuming that the form is opened in Mozilla Firefox web browser, web extension is installed on the browser and relevant registry keys       are added. Setting up a Native-Messaging web extension can be determined from the mozilla documentation (MDN - Native Messaging))
3. After performing necessary operations the GrabJSON.py script will then send a message to this page script (/default/jsonobject.html)      open in the browser, which displays it as an alert.
4. This message obtained from the native application, is the stored into the database (in a table named 'Applications'). On successfull      insertion in the database, a confirmation message is displayed.
5. Check the 'Leave_Application' and 'Applications' tables for the updated entries.
