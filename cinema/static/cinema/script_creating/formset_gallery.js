$('#add_more').click(function() {
	var form_idx = $('#id_form-TOTAL_FORMS').val();
	$('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});

function is_valid() {
	let $elements = $('option[value="on"]')
	let len = $elements.length
	if (len == 0) {
		$('#submit-btn').prop('disabled', false)
		return true;
	}
	$('#submit-btn').prop('disabled', true)
		return false;
}

function delete_image(index) {
	$('#id_' + index + '-image')[0].value="";
	$('.delete-list').append('<input type="hidden" value="on" name="' + index  + '-DELETE" id="id_' + index + '-DELETE">');
	$('#' + index + '-form').css('display', 'none');
	$('#' + index + '-validation').attr('value', 'off')
	is_valid()
}

function preview_gallery(index) {
	$('#' + index + '-image').attr('src', URL.createObjectURL(event.target.files[0]));
	img = new Image();
	img.src = URL.createObjectURL(event.target.files[0]);
	img.onload = function () {
		if (img.width == 1000 && img.height == 190) {
			$('#' + index + '-validation').css('display', 'none').attr('value', 'off');
			is_valid()
			return true;
		}
		$('#' + index + '-validation').css('display', 'inline-block').attr('value', 'on');
		is_valid()
		return false;
	}
}











// $('#add_more').click(function() {
// 	var form_idx = $('#id_form-TOTAL_FORMS').val();
// 	$('#formset').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
// 	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
// });
//
// function is_valid() {
// 	let $elements = $('option[value="on"]')
// 	let len = $elements.length
// 	if (len == 0) {
// 		$('#submit-btn').prop('disabled', false)
// 		return true;
// 	}
// 	$('#submit-btn').prop('disabled', true)
// 		return false;
// }
//
// function delete_image(index) {
// 	$('#id_' + index )[0].value="";
// 	$('.delete-list').append('<input type="hidden" value="on" name="' + index  + '-DELETE" id="id_' + index + '-DELETE">');
// 	$('#' + index + '-form').css('display', 'none');
// 	$('#' + index + '-validation').attr('value', 'off')
// 	is_valid()
// }
//
// function preview_gallery(index) {
// 	$('#' + index).attr('src', URL.createObjectURL(event.target.files[0]));
// 	img = new Image();
// 	img.src = URL.createObjectURL(event.target.files[0]);
// 	img.onload = function () {
// 		if (img.width == 1000 && img.height == 190) {
// 			$('#' + index + '-validation').css('display', 'none').attr('value', 'off');
// 			is_valid()
// 			return true;
// 		}
// 		$('#' + index + '-validation').css('display', 'inline-block').attr('value', 'on');
// 		is_valid()
// 		return false;
// 	}
// }






