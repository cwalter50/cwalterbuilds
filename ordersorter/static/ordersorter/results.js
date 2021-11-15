document.addEventListener('DOMContentLoaded', function() {
    // this is used to test if the javascript is connected to the .html correctly.
    // document.querySelector('#test').innerHTML = "Bella"

    // By default, load the inbox
    console.log("reloadedDOM");
    var results = '{{ results|escapejs }}';
    console.log(results);
});


