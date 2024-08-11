// $(document).ready(function() {
//     // 1
//     try{
//         if($('[id="id_category"]')[0].value && !$('[id="id_filter_category"]')[0].value){
//             change($('[id="id_category"]')[0].value);
//         }
//     } catch {}
//     try{
//         if($('[id="id_category"]')[0].value && $('[id="id_filter_category"]')[0].value){
//             edit($('[id="id_category"]')[0].value,$('[id="id_filter_category"]')[0].value)
//         }
//     } catch {}

//     // 2
//     try{
//         if($('[id="id_filter_category"]')[0].value && !$('[id="id_filters"]')[0].value){
//             change2($('[id="id_filter_category"]')[0].value)
//         }
//     } catch{}
//     try{
//         if($('[id="id_filter_category"]')[0].value && $('[id="id_filters"]')[0].value){
//             edit2($('[id="id_filter_category"]')[0].value,$('[id="id_filters"]')[0].value)
//         }
//     } catch{}

//     // 3
//     try{
//         if($('[id="id_status"]')[0].value){
//             change3();
//         }
//     } catch{}

// });

// document.addEventListener('change', function(event){
//     let id = event.srcElement.id;
//     let value = event.target.value;
//     if(id === 'id_category' && value){
//         change(value);
//     }
//     if(id === 'id_filter_category' && value){
//         change2(value);
//     }
//     if(id === 'id_status' && value) {
//         change3();
//     }
//     console.log("id", id, "value", value)
// });

// function change(value){
//     var url = '/api/filter_category/?category=' + value
//     $.ajax({
//         url: url,
//         success: function (data) {
//             var html = $.map(data, function(data){
//                 return '<option value="' + data.id + '">' + data.title + '</option>'
//             }).join('');
//             html = '<option value selected>---------</option>' + html
//             $("#id_filter_category").html(html);
//         }
//     });

//     var url = '/api/period/?category=' + value
//     $.ajax({
//         url: url,
//         success: function (data) {
//             var html = $.map(data, function(data){
//                 return '<option value="' + data.id + '">' + data.title + '</option>'
//             }).join('');
//             html = '<option value selected>---------</option>' + html
//             $("#id_period_filter").html(html);
//         }
//     });
// }

// function change2(value){
//     var url = '/api/filters/?filter_category=' + value
//     $.ajax({
//         url: url,
//         success: function (data) {
//             var html = $.map(data, function(data){
//                 return '<option value="' + data.id + '">' + data.title + '</option>'
//             }).join('');
//             html = '<option value selected>---------</option>' + html
//             $("#id_filters").html(html);
//         }
//     });
// }

// function change3() {
//     let selected = $("#id_status")[0].value;
//     if (selected === "Gl" || selected === "AU" || selected === "Fl" || selected === "VR") {
//         if (selected === "Gl") {
//             $(".field-locations")[0].style.display = "none";
//             $(".field-link")[0].style.display = "none";
//             $(".field-gallery_files")[0].style.display = "block";
//             $(".field-audio_files")[0].style.display = "none";
//             $(".field-file_files")[0].style.display = "none";
//             $(".field-vr_files")[0].style.display = "none";
//             $(".field-video")[0].style.display = "none";
//         } else if (selected === "AU") {
//             $(".field-locations")[0].style.display = "none";
//             $(".field-link")[0].style.display = "none";
//             $(".field-gallery_files")[0].style.display = "none";
//             $(".field-audio_files")[0].style.display = "block";
//             $(".field-file_files")[0].style.display = "none";
//             $(".field-vr_files")[0].style.display = "none";
//             $(".field-video")[0].style.display = "none";
//         } else if (selected === "Fl") {
//             $(".field-locations")[0].style.display = "none";
//             $(".field-link")[0].style.display = "none";
//             $(".field-gallery_files")[0].style.display = "none";
//             $(".field-audio_files")[0].style.display = "none";
//             $(".field-file_files")[0].style.display = "block";
//             $(".field-vr_files")[0].style.display = "none";
//             $(".field-video")[0].style.display = "none";
//         } else if (selected === "VR") {
//             $(".field-locations")[0].style.display = "none";
//             $(".field-link")[0].style.display = "none";
//             $(".field-gallery_files")[0].style.display = "none";
//             $(".field-audio_files")[0].style.display = "none";
//             $(".field-file_files")[0].style.display = "none";
//             $(".field-vr_files")[0].style.display = "block";
//             $(".field-video")[0].style.display = "none";
//         }
//     } else if (selected === "VD") {
//         $(".field-locations")[0].style.display = "none";
//         $(".field-link")[0].style.display = "block";
//         $(".field-gallery_files")[0].style.display = "none";
//         $(".field-audio_files")[0].style.display = "none";
//         $(".field-file_files")[0].style.display = "none";
//         $(".field-vr_files")[0].style.display = "none";
//         $(".field-video")[0].style.display = "block";
    
//     } else {
//         $(".field-locations")[0].style.display = "block";
//         $(".field-link")[0].style.display = "none";
//         $(".field-gallery_files")[0].style.display = "none";
//         $(".field-audio_files")[0].style.display = "none";
//         $(".field-file_files")[0].style.display = "none";
//         $(".field-vr_files")[0].style.display = "none";
//         $(".field-video")[0].style.display = "none";
//     }
// }

// function edit(value, sub_value){
//     var url = '/api/filter_category/?category=' + value

//     $.ajax({
//         url: url,
//         success: function (data) {
//             var html = $.map(data, function(data){
//                 return '<option value="' + data.id + '">' + data.title + '</option>'
//             }).join('');
//             html = '<option value selected>---------</option>' + html
//             $("#id_filter_category").html(html);
//             // $("#id_category").val(sub_value);
//         }
//     });
// }

// function edit2(value, sub_value){
//     var url = '/api/filter_category/?category=' + value

//     $.ajax({
//         url: url,
//         success: function (data) {
//             var html = $.map(data, function(data){
//                 return '<option value="' + data.id + '">' + data.title + '</option>'
//             }).join('');
//             html = '<option value selected>---------</option>' + html
//             $("#id_filters").html(html);
//             // $("#id_category").val(sub_value);
//         }
//     });
// }

// chat gpt

// Global saqlash obyekt
let savedFilters = {};

$(document).ready(function() {
    // Eski tanlangan `filters`larni yuklash
    loadSavedFilters();

    // Event listener qo'shamiz
    document.addEventListener('change', function(event) {
        let id = event.srcElement.id;
        let value = event.target.value;
        
        if(id === 'id_category' && value) {
            change(value);
        }
        if(id === 'id_filter_category' && value) {
            change2(value);
        }
        if(id === 'id_filters') {
            saveSelectedFilters();
        }
    });
});

function change(value) {
    // `filter_category` va `filters` opsiyalarini tozalash
    $("#id_filter_category").html('<option value selected>---------</option>');
    $("#id_filters").html('<option value selected>---------</option>');

    var url = '/api/filter_category/?category=' + value;
    $.ajax({
        url: url,
        success: function(data) {
            var html = $.map(data, function(item) {
                return '<option value="' + item.id + '">' + item.title + '</option>';
            }).join('');
            html = '<option value selected>---------</option>' + html;
            $("#id_filter_category").html(html);

            // Oldindan saqlangan `filters`ni yuklash
            let filterCategory = $("#id_filter_category").val();
            if (savedFilters[filterCategory]) {
                $('#id_filters').val(savedFilters[filterCategory]);
            }
        }
    });
}

function change2(value) {
    // `filters` opsiyalarini tozalash
    $("#id_filters").html('<option value selected>---------</option>');

    var url = '/api/filters/?filter_category=' + value;
    $.ajax({
        url: url,
        success: function(data) {
            var html = $.map(data, function(item) {
                return '<option value="' + item.id + '">' + item.title + '</option>';
            }).join('');
            html = '<option value selected>---------</option>' + html;
            $("#id_filters").html(html);

            // Oldindan saqlangan `filters`ni yuklash
            if (savedFilters[value]) {
                $('#id_filters').val(savedFilters[value]);
            }
        }
    });
}

function saveSelectedFilters() {
    let filterCategory = $('#id_filter_category').val();
    let selectedFilters = $('#id_filters').val();
    
    if (filterCategory) {
        savedFilters[filterCategory] = selectedFilters;
    }
}

function loadSavedFilters() {
    let filterCategory = $('#id_filter_category').val();
    if (filterCategory && savedFilters[filterCategory]) {
        $('#id_filters').val(savedFilters[filterCategory]);
    }
}








// let savedFilters = {};

// $(document).ready(function() {
//     // Eski tanlangan `filters`larni yuklash
//     loadSavedFilters();

//     // Event listener qo'shamiz
//     document.addEventListener('change', function(event) {
//         let id = event.srcElement.id;
//         let value = event.target.value;
        
//         if(id === 'id_category' && value) {
//             change(value);
//         }
//         if(id === 'id_filter_category' && value) {
//             change2(value);
//         }
//         if(id === 'id_filters') {
//             saveSelectedFilters();
//         }
//     });

//     // Formani yuborish tugmasi bosilganda
//     $('#save-button').on('click', function(event) {
//         event.preventDefault();
//         saveForm();
//     });
// });

// function saveForm() {
//     // Tanlangan `filter_category` va `filters`larni formaga joylashtirish
//     let filterCategory = $('#id_filter_category').val();
//     let selectedFilters = $('#id_filters').val();

//     $('#hidden_filter_category').val(filterCategory);
//     $('#hidden_filters').val(selectedFilters);

//     // Formani yuborish
//     $('#filters-form').submit();
// }

// function change(value) {
//     // `filter_category` va `filters` opsiyalarini tozalash
//     $("#id_filter_category").html('<option value selected>---------</option>');
//     $("#id_filters").html('<option value selected>---------</option>');

//     var url = '/api/filter_category/?category=' + value;
//     $.ajax({
//         url: url,
//         success: function(data) {
//             var html = $.map(data, function(item) {
//                 return '<option value="' + item.id + '">' + item.title + '</option>';
//             }).join('');
//             html = '<option value selected>---------</option>' + html;
//             $("#id_filter_category").html(html);

//             // Oldindan saqlangan `filters`ni yuklash
//             let filterCategory = $("#id_filter_category").val();
//             if (savedFilters[filterCategory]) {
//                 $('#id_filters').val(savedFilters[filterCategory]);
//             }
//         }
//     });
// }

// function change2(value) {
//     // `filters` opsiyalarini tozalash
//     $("#id_filters").html('<option value selected>---------</option>');

//     var url = '/api/filters/?filter_category=' + value;
//     $.ajax({
//         url: url,
//         success: function(data) {
//             var html = $.map(data, function(item) {
//                 return '<option value="' + item.id + '">' + item.title + '</option>';
//             }).join('');
//             html = '<option value selected>---------</option>' + html;
//             $("#id_filters").html(html);

//             // Oldindan saqlangan `filters`ni yuklash
//             if (savedFilters[value]) {
//                 $('#id_filters').val(savedFilters[value]);
//             }
//         }
//     });
// }

// function saveSelectedFilters() {
//     let filterCategory = $('#id_filter_category').val();
//     let selectedFilters = $('#id_filters').val();
    
//     if (filterCategory) {
//         savedFilters[filterCategory] = selectedFilters;
//     }
// }

// function loadSavedFilters() {
//     let filterCategory = $('#id_filter_category').val();
//     if (filterCategory && savedFilters[filterCategory]) {
//         $('#id_filters').val(savedFilters[filterCategory]);
//     }
// }
