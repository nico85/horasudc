
function filtroPorCarrera(){
    var i;
    var carr = document.getElementById("id_carrera");
    var mat = document.getElementById("id_materia");
    var sede = document.getElementById("id_sede");

    //var val = carr.options[carr.selectedIndex].value;
    //var txt = carr.options[carr.selectedIndex].text;
    //alert('Value: '+ val + ' - Texto: ' + txt);
    //text = carr.value;
    //alert('Carrera elegida: '+ text);

    mat.selectedIndex = '';
    sede.selectedIndex = '';
    for (i = 0; i < mat.options.length; i++) {
        if (mat.options[i].disabled != null && mat.options[i].disabled == true) {
            mat.options[i].disabled = false;
            mat.options[i].hidden = false;
        }
    }

    for (i = 0; i < sede.options.length; i++) {
        if (sede.options[i].disabled != null && sede.options[i].disabled == true) {
            sede.options[i].disabled = false;
            sede.options[i].hidden = false;
        }
    }
    var patron = '';
    if (carr.options[carr.selectedIndex].value == 'DES01') {
        patron = "(DES01)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'ENF01'){
        patron = "(ENF01)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'LAN'){
        patron = "(LAN)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Puerto Madryn') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'LAP'){
        patron = "(LAP)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'LE'){
        patron = "(LE)";
        for (i = 0; i < sede.options.length; i++) {
            if ((sede.options[i].text != 'Rawson')&&(sede.options[i].text != 'Esquel')&&(sede.options[i].text != 'Puerto Madryn')) {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'LRT'){
        patron = "(LRT)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'RED01'){
        patron = "(RED01)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'TDS'){
        patron = "(TDS)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'TEA'){
        patron = "(TEA)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Gaiman') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'TGI'){
        patron = "(TGI)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'TUP') {
        patron = "(TUP)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Trelew') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else if (carr.options[carr.selectedIndex].value == 'TUER'){
        patron = "(TUER)";
        for (i = 0; i < sede.options.length; i++) {
            if (sede.options[i].text != 'Rawson') {
                sede.options[i].disabled = true;
                sede.options[i].hidden = true;
            }
        }
    } else{
        patron = "";
    }

    var re = new RegExp(patron);
    for (i = 0; i < mat.options.length; i++) {
        var result = re.test(String(mat.options[i].text));
        if (!result) {
            mat.options[i].hidden = true;
            mat.options[i].disabled = true;
        }
    }
    /*for (i = 0; i < p.options.length; i++) {
        var result = re.test(String(p.options[i].value));
        if (!result) {
            p.options[i].hidden = true;
            p.options[i].disabled = true;
        }
    }*/


}

function validarFechas(){

}
