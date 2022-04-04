function moveContent1(){
    location.href = "{% url 'Board:list' %}";
}
function moveContent2(){
    location.href = "{% url 'Board:list' %}";
}
function moveContent3(){
    location.href = "{% url 'Board:list' %}";
}

function moveBoard1(){
    location.href = "{% url 'Board:detail' 1 %}";
}

function moveReview1(){
    location.href = "{% url 'Contents:detail' 1 %}";
}


