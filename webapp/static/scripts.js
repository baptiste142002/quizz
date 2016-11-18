var i = 0;

document.getElementById('add-question-response').onclick = function(e){

    // Don't submit the form
    e.preventDefault();

    var modelFieldSet = document.getElementsByClassName('question-response')[0];
    var divClone = modelFieldSet.cloneNode(true);
    divClone.getElementsByTagName('input')[0].value = '';
    divClone.getElementsByTagName('input')[1].value = '';

    document.getElementById('question-list').appendChild(divClone);

};