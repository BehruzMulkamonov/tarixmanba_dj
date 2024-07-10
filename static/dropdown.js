$(document).ready(function() {
    // 1
    try{
        if($('[id="id_category"]')[0].value && !$('[id="id_filter_category"]')[0].value){
            change($('[id="id_category"]')[0].value);
        }
    } catch {}
    try{
        if($('[id="id_category"]')[0].value && $('[id="id_filter_category"]')[0].value){
            edit($('[id="id_category"]')[0].value,$('[id="id_filter_category"]')[0].value)
        }
    } catch {}

    // 2
    try{
        if($('[id="id_filter_category"]')[0].value && !$('[id="id_filters"]')[0].value){
            change2($('[id="id_filter_category"]')[0].value)
        }
    } catch{}
    try{
        if($('[id="id_filter_category"]')[0].value && $('[id="id_filters"]')[0].value){
            edit2($('[id="id_filter_category"]')[0].value,$('[id="id_filters"]')[0].value)
        }
    } catch{}

    // 3
    try{
        if($('[id="id_status"]')[0].value){
            change3();
        }
    } catch{}

});

document.addEventListener('change', function(event){
    let id = event.srcElement.id;
    let value = event.target.value;
    if(id === 'id_category' && value){
        change(value);
    }
    if(id === 'id_filter_category' && value){
        change2(value);
    }
    if(id === 'id_status' && value) {
        change3();
    }
    console.log("id", id, "value", value)
});

function change(value){
    var url = '/api/filter_category/?category=' + value
    $.ajax({
        url: url,
        success: function (data) {
            var html = $.map(data, function(data){
                return '<option value="' + data.id + '">' + data.title + '</option>'
            }).join('');
            html = '<option value selected>---------</option>' + html
            $("#id_filter_category").html(html);
        }
    });

    var url = '/api/period/?category=' + value
    $.ajax({
        url: url,
        success: function (data) {
            var html = $.map(data, function(data){
                return '<option value="' + data.id + '">' + data.title + '</option>'
            }).join('');
            html = '<option value selected>---------</option>' + html
            $("#id_period_filter").html(html);
        }
    });
}

function change2(value){
    var url = '/api/filters/?filter_category=' + value
    $.ajax({
        url: url,
        success: function (data) {
            var html = $.map(data, function(data){
                return '<option value="' + data.id + '">' + data.title + '</option>'
            }).join('');
            html = '<option value selected>---------</option>' + html
            $("#id_filters").html(html);
        }
    });
}

function change3() {
    let selected = $("#id_status")[0].value;
    if (selected === "Gl" || selected === "AU" || selected === "Fl" || selected === "VR") {
        $(".field-locations")[0].style.display = "none";
        $(".field-link")[0].style.display = "none";
        $(".field-files")[0].style.display = "block";
        $(".field-video")[0].style.display = "none";

        // let location_elements = $("#id_locations")[0].options;
        // for (var i=0; i < location_elements.length; i++) {
        //     location_elements[i].selected = false;
        // }

        // $("#id_link")[0].value = "";
    } else if (selected === "VD") {
        $(".field-locations")[0].style.display = "none";
        $(".field-link")[0].style.display = "block";
        $(".field-files")[0].style.display = "none";
        $(".field-video")[0].style.display = "block";

        // let location_elements = $("#id_locations")[0].options;
        // for (var i=0; i < location_elements.length; i++) {
        //     location_elements[i].selected = false;
        // }

        // let file_elements = $("#id_files")[0].options;
        // for (var i=0; i < file_elements.length; i++) {
        //     file_elements[i].selected = false;
        // }
    } else {
        $(".field-locations")[0].style.display = "block";
        $(".field-link")[0].style.display = "none";
        $(".field-files")[0].style.display = "none";
        $(".field-video")[0].style.display = "none";

        // let file_elements = $("#id_files")[0].options;
        // for (var i=0; i < file_elements.length; i++) {
        //     file_elements[i].selected = false;
        // }

        // $("#id_link")[0].value = "";
    }
}

function edit(value, sub_value){
    var url = '/api/filter_category/?category=' + value

    $.ajax({
        url: url,
        success: function (data) {
            var html = $.map(data, function(data){
                return '<option value="' + data.id + '">' + data.title + '</option>'
            }).join('');
            html = '<option value selected>---------</option>' + html
            $("#id_filter_category").html(html);
            // $("#id_category").val(sub_value);
        }
    });
}

function edit2(value, sub_value){
    var url = '/api/filter_category/?category=' + value

    $.ajax({
        url: url,
        success: function (data) {
            var html = $.map(data, function(data){
                return '<option value="' + data.id + '">' + data.title + '</option>'
            }).join('');
            html = '<option value selected>---------</option>' + html
            $("#id_filters").html(html);
            // $("#id_category").val(sub_value);
        }
    });
}
