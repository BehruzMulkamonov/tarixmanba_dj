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
        if (selected === "Gl") {
            $(".field-locations")[0].style.display = "none";
            $(".field-link")[0].style.display = "none";
            $(".field-gallery_files")[0].style.display = "block";
            $(".field-audio_files")[0].style.display = "none";
            $(".field-file_files")[0].style.display = "none";
            $(".field-vr_files")[0].style.display = "none";
            $(".field-video")[0].style.display = "none";
        } else if (selected === "AU") {
            $(".field-locations")[0].style.display = "none";
            $(".field-link")[0].style.display = "none";
            $(".field-gallery_files")[0].style.display = "none";
            $(".field-audio_files")[0].style.display = "block";
            $(".field-file_files")[0].style.display = "none";
            $(".field-vr_files")[0].style.display = "none";
            $(".field-video")[0].style.display = "none";
        } else if (selected === "Fl") {
            $(".field-locations")[0].style.display = "none";
            $(".field-link")[0].style.display = "none";
            $(".field-gallery_files")[0].style.display = "none";
            $(".field-audio_files")[0].style.display = "none";
            $(".field-file_files")[0].style.display = "block";
            $(".field-vr_files")[0].style.display = "none";
            $(".field-video")[0].style.display = "none";
        } else if (selected === "VR") {
            $(".field-locations")[0].style.display = "none";
            $(".field-link")[0].style.display = "none";
            $(".field-gallery_files")[0].style.display = "none";
            $(".field-audio_files")[0].style.display = "none";
            $(".field-file_files")[0].style.display = "none";
            $(".field-vr_files")[0].style.display = "block";
            $(".field-video")[0].style.display = "none";
        }
    } else if (selected === "VD") {
        $(".field-locations")[0].style.display = "none";
        $(".field-link")[0].style.display = "block";
        $(".field-gallery_files")[0].style.display = "none";
        $(".field-audio_files")[0].style.display = "none";
        $(".field-file_files")[0].style.display = "none";
        $(".field-vr_files")[0].style.display = "none";
        $(".field-video")[0].style.display = "block";
    
    } else {
        $(".field-locations")[0].style.display = "block";
        $(".field-link")[0].style.display = "none";
        $(".field-gallery_files")[0].style.display = "none";
        $(".field-audio_files")[0].style.display = "none";
        $(".field-file_files")[0].style.display = "none";
        $(".field-vr_files")[0].style.display = "none";
        $(".field-video")[0].style.display = "none";
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