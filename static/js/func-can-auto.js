/**
 * Created by eloy on 09/05/17.
 */
$(document).ready(function () {
    var $clone = $(this).find('tr.hide').clone(true).removeClass('hide table-line');
    $clone.addClass('nro_precio');
    $(this).find('table#precios').append($clone);
    var i = document.getElementsByClassName('nro_precio').length;
    if (i > 1) {
        var n = document.getElementById('precios').rows.length - 1;
        document.getElementById('precios').rows[n].cells[0].textContent = i;
    }
    var objDiv = document.getElementById('cuerpo_tabla');
    objDiv.scrollTop = objDiv.scrollHeight;
    $(":input:last").focus();
});

$(document).on('click', '.table-remove', function () {
    $(this).parents('tr').detach();
    var n = document.getElementById('precios').rows.length;
    var j = 1;
    for (var i = 1; i < n; ++i){
        if (document.getElementById('precios').rows[i].getAttribute('class') == 'hide'){
            j -= 1;
        }
        document.getElementById('precios').rows[i].cells[0].textContent = j;
        j += 1;
    }
    var csrftoken = getCookie('csrftoken');
    var id = $(this).parents('tr')[0].id;
    if (id){
        $.ajax({
            type: "POST",
            url: "/autoponderado/borrar/",
            data: { id: id, csrfmiddlewaretoken: csrftoken },
            success: function(response){
                location.reload();
            }
        });
    }
});

$(document).on('change', '.pesos', function(){
    var csrftoken = getCookie('csrftoken');
    var precio = $(this)[0].value;
    precio = precio.replace(',', '.');
    var id = $(this).parent().parent().parent()[0].id;
    if (id) {
        $.ajax({
            type: "POST",
            url: "/autoponderado/actualizar/",
            data: {id: id, precio: precio, csrfmiddlewaretoken: csrftoken},
            success: function (response) {
                location.reload();
            }
        });
    } else {
        var fecha = document.getElementById('fecha').value.split('-');
        var anio = fecha[0];
        var mes = fecha[1];
        var articulo = document.getElementById('articulo').value;
        $.ajax({
            type: "POST",
            url: "/autoponderado/guardar/",
            data: {precio: precio, mes: mes, anio: anio, articulo: articulo, csrfmiddlewaretoken: csrftoken},
            success: function (response) {
                location.reload();
            }
        });
    }
});