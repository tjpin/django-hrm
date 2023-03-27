var chatInput = $("#msg");
var sendChatBtn = $("#send-msg");
var chatBody = $("#chat-body");

let time = new Date().toTimeString().substring(0, 8);
let wsScheme = 'ws://'

if(location.protocol === 'https://'){ // location.protocol === 'http://' | 
    wsScheme = 'wss://'
}

function sendMessage(message){
    if(message.trim() === "") {return false}
    let mm = "";
    let msg_element = `
        <span id="chat-message-card" class="w-fit h-fit flex gap-2 items-start">
            <img src="{% static 'images/face.jpeg' %}" alt="" class="w-11 h-11 rounded-full object-cover">
            <span class="chat-card flex flex-col items-end gap-2 border shadow px-2 py-2 w-fit">
                <p class="text-mainText text-sm flex flex-wrap">${message}</p>
                <h4 class="text-xs py-1 px-2 rounded bg-hg w-fit">${time}</h4>
            </span>
        </span>
    `
    chatBody.append($(msg_element))
    chatBody.animate({
        scrollTop: $(document).height()
    }, 100);
    chatInput.val(null);
}



var endpoint = wsScheme + location.host + location.pathname
var socket = new WebSocket(endpoint)

socket.onopen = async (event) => {
    console.log('Open: ', event);
    $("#msg-input").on('submit', function(e){
        e.preventDefault();
        let mssg = chatInput.val().trim();
        let data = {'message': mssg}
        var json = JSON.stringify(data)
        socket.send(json)
        sendMessage(chatInput.val().trim());
        $(this)[0].reset();
    })
}

socket.onmessage = async (event) => {
    console.log('Message: ', event)
}

socket.onerror = async (event) => {
    console.log('Error Occured: ', event)
}

