function moveLogin(){
    location.href = "{% url 'Member:login' %}";
}

function moveJoin(){
    location.href = "{% url 'Member:join' %}";
}

function moveLogout(){
    location.href = "{% url 'Member:logout' %}";
}

function moveMy(){
    location.href = "{% url 'Member:info_detail' %}";
}

