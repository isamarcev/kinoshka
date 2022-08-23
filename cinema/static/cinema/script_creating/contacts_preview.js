function preview_logo(index) {
    let url = URL.createObjectURL(event.target.files[0]);
    $('#' + index + '-logo').attr('src', url)
}

function delete_logo(index) {
    $('#id_' + index + '-logo').val("");
    $('#' + index + '-logo').attr('src', "/static/cinema/dist/img/preview_upload.png")
}

