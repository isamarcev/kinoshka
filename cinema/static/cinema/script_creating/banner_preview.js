function showPreview() {
    logo_preview.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-logo').click(function () {
    $('#image').val("");
    $('#logo_preview').attr("src", "/static/cinema/dist/img/preview_upload.png")
})