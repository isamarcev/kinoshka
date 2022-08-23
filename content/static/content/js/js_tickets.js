
let place = ''

$(function () {
    // $('.reserve').unbind('click')
    $('.unselected').on('click', function () {
        $(this).toggleClass('unselected selected')
        var all_selected = document.getElementsByClassName("selected")
        let total_price = parseInt(document.getElementById('price').textContent) * all_selected.length
        document.getElementById('tickets_count').textContent = all_selected.length
        document.getElementById('total_price').textContent = total_price
    })
})

function buy_place() {
    let all_selected = ($('.selected'));
    for (let i of all_selected) {
        x = ((i.getAttribute('row')+ ':' + (i.getAttribute('place') + ',')))
        place += x
        }
    console.log(place);
    }

    function get_data_tickets() {
                    $.ajax({
                        url: '',
                        type: 'get',
                        data: {
                    'session': session,
                },
                success: (data) => {
                    $(function () {
                        var all_place = document.getElementsByTagName('rect');
                        var b = "bought"
                        var r = "reserved"
                        for (let elem of all_place) {
                            var row = parseInt(elem.getAttribute('row'));
                            var place = parseInt(elem.getAttribute('place'));
                            if (data[row][place][b]||data[row][place][r] ) {
                                $(elem).addClass('reserve').removeClass('selected').removeClass('unselected').unbind('click')
                            }
                        }
                    })
                    error: (error) => {
                    console.log(error);

                    }
            }})

        }
