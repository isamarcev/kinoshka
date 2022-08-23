


function showpreviewfile() {
    loader_file.innerText = (event.target.files[0]).name;
}

document.getElementById('btn_select').setAttribute('disabled', true);


$('#user_select_all').on('click', function () {
    document.getElementById('user_select').checked = false;
    document.getElementById('btn_select').setAttribute('disabled', true);
    ($(this)).checked = true;
    emails_list = []
    $('#users_mail').DataTable().rows().nodes().to$().find('input[type="checkbox"]').each(function(){
        $(this)[0].checked = true;
        emails_list.push($(this).val())
    })
    document.getElementById('emails_count').textContent = emails_list.length
    document.getElementById('send_email').removeAttribute('disabled');

})

$('#user_select').on('click', function () {
    document.getElementById('user_select_all').checked = false;
    document.getElementById('btn_select').removeAttribute('disabled');
    ($(this)).checked = true;
    $('#users_mail').DataTable().rows().nodes().to$().find('input[type="checkbox"]').each(function(){
        $(this)[0].checked = false;
    })
    emails_list = []
    document.getElementById('emails_count').textContent = emails_list.length
})

function choose() {
    emails_list = [];
    $('#users_mail').DataTable().rows().nodes().to$().find('input[type="checkbox"]').each(function(){
        if ($(this)[0].checked) {
        emails_list.push($(this).val())

    }})
    document.getElementById('emails_count').textContent = emails_list.length
}

function cancel_all() {
    $("#deleteModal100-choose_users input[type='checkbox']").each(function (index, elem) {
        elem.checked = false;
    })
}


$('#users').DataTable().rows().nodes().to$().find('input[type="checkbox"]').on('click', function () {
    ($(this)).checked = true;
})

function add_email(index) {
	let all_email;
    all_email = id_all_type.getAttribute('value') + index + ','
    id_all_type.setAttribute('value', all_email)
}


