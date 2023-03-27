var navlists = document.querySelectorAll("#navlist");
var navDropdowns = document.querySelectorAll("#nav-dropdown");

var menuButton = document.querySelector(".menubar");
var loader = document.getElementById("loader");

var addmodal = document.querySelectorAll("#addmodal");
var addmodalopen = $("*#addmodal-open");
var addmodalClose = $("*#addmodal-close");


$(window).on('load', function(){
    $("#loader").fadeOut(1000);
    $("#body-content").fadeIn(1000);
})

navlists.forEach((li, i) => {
    li.addEventListener('mouseover', () => {
        navDropdowns[i].classList.add("navlist-active");
    })
    li.addEventListener('mouseleave', () => {
        navDropdowns[i].classList.remove("navlist-active");
    })
});

// ************ Open Add Modal
addmodalopen.click(function(){
    $("#addmodal").fadeIn(500);
})
addmodalClose.click(function(){
    $("#dynamic-modal").empty();
    $("#addmodal").fadeOut(500);
})

var isOpen = false;
$(document).ready(function() {
    $(".menubar").click(function(){
        if(!isOpen){
            isOpen = true;
            menuButton.innerHTML = `<i class="fa-solid fa-xmark text-lg text-red-500"></i>`
            $("#navbar-ul").show();
        } else {
            $("#navbar-ul").hide();
            menuButton.innerHTML = `<i class="fa-solid fa-bars text-lg text-mainCyan"></i>`
            isOpen = false;
        }
    });

    // --------------- settings menu--------------------------------------------------
    // -------------------------------------------------------------------------------
    document.getElementById("new-logo").addEventListener('change', (e) => {
        url = URL.createObjectURL(e.target.files[0]);
        document.getElementById("company-logo").src = url;
    });
    
    $("#open-settings").click(function(){
        $(".settings-menu").show(duration=200);
    })
    $("#close-settings").click(function(){
        $(".settings-menu").hide(duration=200);
    })


    // ------------------------------------------------------------------------------
    // ------------------------------------------------------------------------------

    var isChatmodalOpen = false;
    var cbtn = document.getElementById("chart-button");

    $("#chart-button").click(function(){
        if(!isChatmodalOpen){
            isChatmodalOpen = true;
            this.innerHTML = `<i class="fa-solid fa-xmark text-red-500 text-2xl"></i>`
            $("#chat-modal").show();
        } else {
            $("#chat-modal").hide();
            this.innerHTML = `<i class="fa-solid fa-comment text-mainCyan text-2xl"></i>`   
            isChatmodalOpen = false;     
        }
    })
    
    $("#depts-ul li").click(function() {
        setTimeout(() => $("#department-list").fadeIn(300), 200);
        
    })


    // ///////////// Calendar ///////////////////
    // var currentDate = document.getElementById("current-date");
    // var days = document.getElementById("days");
    // var calendarActions = document.querySelectorAll(".date-ction");
    // console.log(calendarActions)

    // var date = new Date();
    // var currentYear = date.getFullYear();
    // var curentMonth = date.getMonth();

    // const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
    //           'August', 'September', 'Octomber', 'November', 'December']

    // const showCalendar = () => {
    //     var lastDate = new Date(currentYear, curentMonth+1, 0).getDate();
    //     var li = "";

    //     for(let i=1; i<= lastDate; i++){
    //         li += `<span class="day">${i}</span>`;
    //     }

    //     currentDate.innerHTML = `${lastDate} ${months[curentMonth]} ${currentYear}`
    //     days.innerHTML = li;
    // }

    // showCalendar();

    // calendarActions.forEach((icon) => {
    //     icon.addEventListener('click', () => {
    //         curentMonth = icon.id === 'prev' ? curentMonth -1 : curentMonth +1;
    //         if( curentMonth < 1){
    //             currentYear -= 1;
    //         } 
    //         if (curentMonth > 12){
    //             currentYear += 1
    //         }
    //         showCalendar();
    //     })
    // })
})


