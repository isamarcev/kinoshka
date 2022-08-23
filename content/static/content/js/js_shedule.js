
let cinema_id = new Map()
let hall_id = new Map()
let film_id = new Map()
let date = new Map()
let fd2 = new Map()
let fd3 = new Map()
let imax = new Map()

cinema_id.set('cinema_id', localStorage.cinema)

var all_cinemas = document.getElementsByClassName("select-cinema")
$(function (){
    for (i = 0; i < all_cinemas.length; i++) {
        if ($(document.getElementById(all_cinemas[i].id)).val() === localStorage.cinema){
            $(document.getElementById(all_cinemas[i].id)).prop('selected', true)
        }
    }
})

film_id.set('film_id', localStorage.film)

var all_films = document.getElementsByClassName("select-film")
$(function (){
    for (i = 0; i < all_films.length; i++) {
        if ($(document.getElementById(all_films[i].id)).val() === localStorage.film_id){
            $(document.getElementById(all_films[i].id)).prop('selected', true)
        }
    }
})

hall_id.set('hall_id', false)
fd2.set('f2d', true)
fd3.set('f3d', true)
imax.set('imax', true)



//first select
function start(){
    $('#table1').css('display', 'block')
    $("#table1 tbody tr").remove()
}

//get cinema filter data
$('#cinema').on('change', function() {
    localStorage.removeItem('cinema_id')
    if ($(this).val() !== 'all') {
        cinema_id.set('cinema_id', $(this).val())
        hall_id.set('hall_id', false)
    } else {
        cinema_id.set('cinema_id', false)
        hall_id.set('hall_id', false)
    }
    // console.log('aaaaaa')
    $('.hall').remove()
    console.log('aaaaaa')
    get_data_cinema()
})

//get hall filter data
$('#select-halls').on('change', function() {
    if ($(this).val() !== 'all') {
        hall_id.set('hall_id', $(this).val())
    } else {
        hall_id.set('hall_id', false)
    }
    get_data()
})

//get film filter data
$('#film').on('change', function() {
    localStorage.removeItem('film_name')
    if ($(this).val() !== 'all') {
        film_id.set('film_id', $(this).val())
    } else {
        film_id.set('film_id', false)
    }
    get_data()
})

//get date filter data
$('#date').on('change', function() {
    date.set('date', $(this).val())
    get_data()
})


//get type2d filter data
$('#2d').on('change', function() {
    fd2.set('f2d', $(this).is(':checked'))
    get_data()
})

//get type3d filter data
$('#3d').on('change', function() {
    fd3.set('f3d', $(this).is(':checked'))
    get_data()
})

//get type-imax filter data
$('#imax').on('change', function() {
    imax.set('imax', $(this).is(':checked'))
    get_data()
})





//
// const select = document.querySelectorAll('select');
//
// select.forEach(selectItem => {
//     selectItem.addEventListener('click', filter(selectItem.value, selectItem.name)
// })
// function changeOn(value) {
//     let rows = document.getElementsByTagName('tr');
//         for (let row of rows) {
//             row.style.display = 'table-row';
//         }
// }
//
//  function filter(name, value) {
//     changeOn(value);
//     let allObjects = document.getElementsByClassName(value);
//     for (let elem of allObjects) {
//         console.log(elem.innerHTML);
//         console.log(elem.innerHTML == name)
//         if (elem.innerHTML != name && elem.closest('tr').style.display == 'table-row') {
//             console.log('CHEKIN');
//             father = elem.closest('tr');
//             father.style.display = 'none';
//             console.log('CHEKOUT IF');
//
//         }
//         else if (elem.innerHTML == name && elem.closest('tr').style.display == 'none') {
//             console.log('CHEKINELSE');
//
//             father = elem.closest('tr');
//             father.style.display = 'table-row';
//             console.log('CHEKOUT else');
//
//         }
//
//     }
// }
//
// function filterCinema(name, value) {
//     alert(value)
//     if (value == 'cinema_all') {
//         console.log(value == 'cinema_all')
//         let allCinema = document.getElementsByClassName('cinema');
//         for (let elem of allCinema) {
//         elem.closest('tr').style.display = 'table-row';
//         }
//         document.getElementById('film').click();
//         document.getElementById('hall').click();
//     }
//     else {
//         let allCinema = document.getElementsByClassName(value);
//         for (let elem of allCinema) {
//             if (elem.innerHTML != name) {
//                 elem.closest('tr').style.display = 'none';
//             }
//             else if (elem.innerHTML == name) {
//                 elem.closest('tr').style.display = 'table-row';
//
//             }
//         }
//         document.getElementById('film').click();
//         document.getElementById('hall').click();
//     }
//
//
// }
//
// function filterCinem(name, value) {
//     let allCinema = document.getElementsByClassName(value);
//     if (value == 'cinema_all') {
//         for (let elem of allCinema) {
//             elem.closest('tr').style.display = 'table-row'
//         }
//     }
//     else {
//         for (let elem of allCinema) {
//                 if (elem.innerHTML != name && elem.closest('tr').style.display == 'none') {
//                     console.log('Nothing');
//                 }
//                 else {
//                     elem.closest('tr').style.display = 'table-row';
//                 }
//         }
//     }
// }
//
// function filterFilm(name, value) {
//     document.getElementById('cinema').click();
//     let allFinema = document.getElementsByClassName(value);
//     for (let elem of allFinema) {
//         console.log(elem, elem.innerHTML == name, name)
//         if (elem.innerHTML != name && elem.closest('tr').style.display == 'table-row') {
//             elem.closest('tr').style.display = 'none';
//             alert('hello')
//         }
//     }
//     document.getElementById('hall').click();
// }
//
//
// function filterFil(name, value) {
//     let allCinema = document.getElementsByClassName(value);
//     alert(name)
//     // if (value == 'film_all') {
//     document.getElementById('cinema').click();
//     for (let elem of allCinema) {
//         if (elem.innerHTML != name && elem.closest('tr').style.display == 'table-row') {
//             elem.closest('tr').style.display = 'none';
//         }
//     }
//
//     document.getElementById('hall').click();
// }
//
// function filterHall(name, value) {
//     let allCinema = document.getElementsByClassName(value);
//     document.getElementById('cinema').click();
//     document.getElementById('film').click();
//     if (value == 'hall_all') {
//         for (let elem of allCinema) {
//             if (elem.innerHTML != name && elem.closest('tr').style.display == 'table-row') {
//                 elem.closest('tr').style.display = 'none';
//             }
//         }
//     }
// }
//
// function filterHal(name, value) {
//     let allCinema = document.getElementsByClassName(value);
//     alert(name)
//     // if (value == 'hall_all') {
//     //     document.getElementById('cinema').click();
//     //     document.getElementById('film').click();
//     for (let elem of allCinema) {
//             if (elem.innerHTML != name && elem.closest('tr').style.display == 'table-row') {
//                 elem.closest('tr').style.display = 'none';
//             } else if (elem.innerHTML == name && elem.closest('tr').style.display == 'none') {
//                 console.log('Nothing')
//             }
//     }
// }
//



// for (let elem of y) {
//     if (elem.innerHTML == 'Kl4W66P4Af Bctjinm5Tl') {
//         console.log(elem.closest('tr'));
//         x = elem.closest('tr');
//         x.style.display = 'none';
//     };
// }