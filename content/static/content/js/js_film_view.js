let cinema_id = new Map()
let hall_id = new Map()
let film_id = new Map()
let date = new Map()
let fd2 = new Map()
let fd3 = new Map()
let imax = new Map()

cinema_id.set('cinema_id', false)

film_id.set('film_id', false)
date.set('date', false)
hall_id.set('hall_id', false)
fd2.set('f2d', true)
fd3.set('f3d', true)
imax.set('imax', true)



//first select
function start(){
    $("#session_listok").empty()
}

//get cinema filter data
$('#cinema').on('change', function() {
    localStorage.removeItem('cinema_id')
    if ($(this).val() !== 'all') {
        cinema_id.set('cinema_id', $(this).val())
        $('#cinema_show .cinema_name').remove()
        $('#start_cinema').css('display', 'none')
        $('#cinema_show').css('display', 'block')
        cinema_names = document.getElementById($(this).val()).textContent
        cinema = '<p class="cinema_name" style="font-size: 150%; margin-bottom: 25px">'+cinema_names+'</p>'
          console.log(cinema)
        $("#cinema_show").append(cinema)
    } else {
        cinema_id.set('cinema_id', false)
        $('#cinema_show').css('display', 'none')
        $('#start_cinema').css('display', 'block')
    }
    get_data_cinema()
})

//get date filter data
$('.date').on('click', function() {
    console.log($(this).val())
    date.set('date', $(this).val())
    get_data()
})

//get type2d filter data
$('#f2d').on('click', function() {
        fd2.set('f2d', true)
        fd3.set('f3d', false)
        imax.set('imax', false)
        $('#f2d').css('background', '#343a40')
        $('#f2d').css('color', 'white')
        $('#f3d').css('background', 'none')
        $('#f3d').css('color', 'black')
        $('#imax').css('background', 'none')
        $('#imax').css('color', 'black')
        $('#all').css('background', 'none')
        $('#all').css('color', 'black')
    get_data()
})

//get type3d filter data
$('#f3d').on('click', function() {
        fd2.set('f2d', false)
        fd3.set('f3d', true)
        imax.set('imax', false)
        $('#f3d').css('background', '#343a40')
        $('#f3d').css('color', 'white')
        $('#f2d').css('background', 'none')
        $('#f2d').css('color', 'black')
        $('#imax').css('background', 'none')
        $('#imax').css('color', 'black')
        $('#all').css('background', 'none')
        $('#all').css('color', 'black')
    get_data()
})

//get type-imax filter data
$('#imax').on('click', function() {
    fd2.set('f2d', false)
        fd3.set('f3d', false)
        imax.set('imax', true)
        $('#imax').css('background', '#343a40')
        $('#imax').css('color', 'white')
        $('#f3d').css('background', 'none')
        $('#f3d').css('color', 'black')
        $('#f2d').css('background', 'none')
        $('#f2d').css('color', 'black')
        $('#all').css('background', 'none')
        $('#all').css('color', 'black')
    get_data()
})
$('#all').on('click', function() {
        fd2.set('f2d', true)
        fd3.set('f3d', true)
        imax.set('imax', true)
        $('#all').css('background', '#343a40')
        $('#all').css('color', 'white')
        $('#f3d').css('background', 'none')
        $('#f3d').css('color', 'black')
        $('#f2d').css('background', 'none')
        $('#f2d').css('color', 'black')
        $('#imax').css('background', 'none')
        $('#imax').css('color', 'black')
    get_data()
})

