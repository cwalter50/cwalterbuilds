
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#thebutton").onclick = count
    document.getElementById("bdaystats").style.display = "none"; // hide stats
});


// Date Picker
$( 
    function() {
        $( "#datepicker" ).datepicker().datepicker("setDate", new Date());
    } 
  );

// var x = setInterval(function() {
// console.log("hello");
// }, 1000);
var nextBDay = new Date();

function count() {
    let dateString = document.querySelector("#datepicker").value;

    let bdate = new Date(dateString); // Birthday including year
    let year = bdate.getFullYear();
    let bmonth = bdate.getMonth(); // from 0-11
    let bDayOfMonth = bdate.getDate(); // from 1 to 31
    
    // Steps to get days until your next birthday.
    // 1. get now, get next birthday. Compare them to figure out when next BDay is

    let now = new Date();
    let m = bmonth - now.getMonth()

    nextBDay = new Date();
    nextBDay.setHours(0);
    nextBDay.setMinutes(0);
    nextBDay.setSeconds(0);
    nextBDay.setMilliseconds(0);

    if (m > 0 || (m === 0 && bDayOfMonth - now.getDate() > 0)) {
        // Your birthday will happen in this calendar year
        nextBDay.setDate(bDayOfMonth);
        nextBDay.setMonth(bmonth);
        
    }
    else if (m === 0 && bDayOfMonth - now.getDate() === 0) {
        // Today is your birthday
        
    }
    else {
        // Your birthday already happened this calendar year and your next birthday will be next year.
        nextBDay.setDate(bDayOfMonth);
        nextBDay.setMonth(bmonth);
        nextBDay.setFullYear(now.getFullYear() + 1);
        
    }

    // let result = `Next Birthday: ${nextBDay.toDateString()} BirthYear: ${year}`;

    // document.querySelector("#results").innerHTML = result;
    let totalHours = getTotalHours(bdate);
    let totalDays = getTotalDays(bdate);
    let totalWeeks = getTotalWeeks(bdate);
    let totalMonths = getTotalMonths(bdate);
    let sleeps = getNumberOfSleeps();
    let age = getAge(bdate);

    document.getElementById("bdaystats").style.display = "block"; // show stats
    document.querySelector("#nextbday").innerHTML = "Next Birthday: " + nextBDay.toDateString();
    document.querySelector("#age").innerHTML = "Age: " + age;
    document.querySelector("#sleeps").innerHTML = "# of Sleeps 😴 until next Birthday: " + sleeps;
    document.querySelector("#totalhours").innerHTML = "Total Hours Living: " + totalHours;
    document.querySelector("#totaldays").innerHTML = "Total Days Living: " + totalDays;
    document.querySelector("#totalweeks").innerHTML = "Total Weeks Living: " + totalWeeks;
    document.querySelector("#totalmonths").innerHTML = "Total Months Living: " + totalMonths;

    // document.querySelector("#bdaystats").innerHTML = "Total Days: " + totalDays + " # of Sleeps: " + sleeps;
    // document.getElementById("bdaystats").style.display = "none"; // hide stats
    // document.getElementById("bdaystats").style.display = "block"; // show stats
    setCountdown();
    
}

function getAge(bDate)
{
    let now = new Date();
    let age = now.getFullYear() - bDate.getFullYear();

    let m = now.getMonth() - bDate.getMonth();
    if (m < 0 || (m === 0 && now.getDate() - bDate.getDate() < 0))
    {
        age = age - 1;
    }

    return `${age}`;


}

function getTotalHours(birthday) {

    let now = new Date().getTime();
    let distance = now - birthday.getTime();
    let hours = Math.floor(distance / (1000 * 60 * 60));

    return `${hours}`;

}

function getTotalDays(birthday) {

    let now = new Date().getTime();
    let distance = now - birthday.getTime();
    let days = Math.floor(distance / (1000 * 60 * 60 * 24));

    return `${days}`;

}

function getTotalWeeks(birthday) {
    let now = new Date().getTime();
    let distance = now - birthday.getTime();

    let weeks = Math.floor(distance / (1000 * 60 * 60 * 24 * 7));
    return `${weeks}`;
}

function getTotalMonths(birthday) {
    let now = new Date();
    let months = (now.getFullYear() - birthday.getFullYear()) * 12;
    let extra = now.getMonth() - birthday.getMonth();
    months += extra;

    return `${months}`;
}

function getNumberOfSleeps() {
    let countDownDate = nextBDay.getTime();

    // Get today's date and time
    let now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.ceil(distance / (1000 * 60 * 60 * 24));
    
    return `${days}`;
}


function setCountdown(){
    var x = setInterval(function(){
        let countDownDate = nextBDay.getTime();

        // Get today's date and time
        let now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        // Display the result in the element with id="demo"
        // document.getElementById("demo").innerHTML = days + "d " + hours + "h "
        // + minutes + "m " + seconds + "s ";
        document.getElementById("countdown").innerHTML = "Birthday Countdown: " + days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("countdown").innerHTML = "🎈🎉🎉 Today is your Birthday 🎂 Happy Birthday 🎉🎉🎈";
        }
    }, 1000);
}

// Simple hello Alert
function hello() {
    // alert("Hello, World!")
    let header = document.querySelector('h1');
    if (header.innerHTML === 'Hello!') {
        header.innerHTML = 'Goodbye!';
    }
    else {
        header.innerHTML = 'Hello!';
    }     
}


