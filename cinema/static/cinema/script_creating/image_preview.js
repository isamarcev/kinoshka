function showPreview() {
    logo_preview.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-logo').click(function () {
    $('#logo').val("");
    $('#logo_preview').attr("src", "/static/cinema/dist/img/preview_upload.png")
})

function showPreviewBanner() {
    banner_preview.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-banner').click(function () {
    $('#banner').val("");
    $('#banner_preview').attr("src", "/static/cinema/dist/img/preview_upload.png")
})