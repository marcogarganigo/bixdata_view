function load_fields(el, tableid, recordid, master_tableid, master_recordid) {
    console.info('base.js-load_fields')
    console.info(base_url)
    $.ajax({
        type: "POST",
        url: "/get_record_fields/",
        data: {
            'http_response': 'true',
            'tableid': tableid,
            'recordid': recordid,
            'master_tableid': master_tableid,
            'master_recordid': master_recordid,
            'contextfunction': 'edit',
        },
        success: function (response) {
            $(el).closest('.block_record_card').find('.tab-pane-fields').html(response)
        },
        error: function (response) {
            $(el).closest('.block_record_card').find('.tab-pane-fields').html(response)
        }
    });
}

function save_record(el, setting) {
    console.info('FUN:base.js-save_record')
    var record_fields_container = $(el).closest('.record_fields_container')
    var tableid = $(record_fields_container).data('tableid')
    var contextfunction = $(record_fields_container).data('contextfunction')
    var recordid = $(record_fields_container).data('recordid')
    var master_tableid = $(record_fields_container).data('master_tableid')
    var master_recordid = $(record_fields_container).data('master_recordid')
    let necessaryFields = $(record_fields_container).find('.necessary');
    let hasNecessaryFields = false;

    $(necessaryFields).each(function (field) {
        if ($(this).val() === null || $(this).val() === "" || $(this).val() === "None") {
            hasNecessaryFields = true;
        }
    });

    if (hasNecessaryFields === true) {
        swal({
            title: "Attenzione",
            text: "Compilare tutti i campi obbligatori",
            icon: "error",
            button: "Ok",
            dangerMode: true,
        });

    } else {
          swal({
            title: "Salvataggio in corso!",
            text: " ",
            icon: "info",
            timer: 1200,
            buttons: false,
        })
        console.info("DEBUG")
        //const tipoContrattoselectedValues = $('#field-tipocontratto').val(); // Ottieni i valori selezionati
        //console.log('Valori selezionati:', tipoContrattoselectedValues);
        serialized_form = serializeForm($(el).closest('#universal-container-timesheet').find('.fields_container').find("select,textarea,input"));



            //console.info(serialized_form)
            //console.log(serialized_form)
            serialized_json = convertFormToJSON(serialized_form);

            //console.info(serialized_json)
            var post_data = [];
            post_data.push({name: 'tableid', value: tableid});
            post_data.push({name: 'recordid', value: recordid});
            post_data.push({name: 'fields', value: serialized_json});
            post_data.push({name: 'contextfunction', value: contextfunction});
            // Initialize FormData object from the form element
            var formData = new FormData($(el).closest('#universal-container-timesheet').find("#form_fields_container")[0]);

            // Append static data
            formData.append('tableid', tableid);
            formData.append('recordid', recordid);
            formData.append('contextfunction', contextfunction);
            //formData.append('tipocontratto', tipoContrattoselectedValues);
            
            // Check if there are any textarea-editor elements
            if ($(el).closest('#universal-container-timesheet').find('.textarea-editor').length > 0) {

                // Iterate over each textarea-editor element
                $(el).closest('#universal-container-timesheet').find('.textarea-editor').each(function () {
                    // Get the HTML content from the second .ProseMirror element
                    var valuea = $(this).find('.ProseMirror:eq(1)').html();

                    // Ensure valuea is a valid string
                    if (valuea !== null && valuea !== undefined) {
                        valuea = valuea.toString();

                        // Get the name of the field
                        var fieldname = $(this).attr('data-name');

                        // Append the field name and value to FormData
                        formData.append(fieldname, valuea);
                        console.log(fieldname)
                    }
                });
            }

            //console.info(formData)

        

        closeNewRecordModal(el)
        $(el).closest('.modal').modal("hide");
        $.ajax({
            type: "POST",
            url: "/save_record_fields/", 
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                saved_recordid = response

                if (master_tableid == 'None') {
                    if(contextfunction=='insert'){
                        refresh();
                    }
                } else {
                    load_linked(tableid + '-' + master_recordid, tableid, master_recordid, master_tableid)
                    load_badge(master_tableid, master_recordid)
                }


                setTimeout(function () {


                    $('#fields_container_' + tableid + '_' + recordid).load('/loading/');

                    if ((master_tableid == 'None') && tableid != 'deal') {
                        if (window.innerWidth > min_width) {
                            if (setting == 'modal') {
                                //open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
                            } else {
                                //$('#fields_container_' + tableid + '_' + recordid).load('/loading/');
                                open_record(window.content, tableid, saved_recordid, contextfunction, 'card')
                            }
                        }
                    }
                    if (window.innerWidth < min_width) {
                        //open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
                    }


                    if (tableid == 'deal') {
                        open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
                    }


                    swal({
                        title: "Salvato!",
                        text: "Il record è stato salvato",
                        icon: "success",
                        timer: 800,
                        buttons: false,
                    })

                });

            },
            error: function () {
                notify_error()
            }
        });
    }


}


function load_linked(linkedtableid, tableid, masterrecordid, mastertableid, order, order_field) {
    if (order == 'None') {
        order = ''
    }
    if (order_field == 'None') {
        order_field = ''
    }

    var masterrecordid = masterrecordid
    var mastertableid = mastertableid
    $("#linked-container-" + linkedtableid).load('/loading/')
    $.ajax({
        url: "/get_records_linked/",
        type: 'POST',
        data: {
            'tableid': tableid,
            'master_tableid': mastertableid,
            'master_recordid': masterrecordid,
            'order': order,
            'order_field': order_field,
        },
        success: function (response) {
            //$(collapse).find('.linked_container').html(response);
            $("#linked-container-" + linkedtableid).html(response)
        },
        error: function (response) {
        }
    });
}


function saveSignature() {

    swal({
        title: "Generazione file in corso",
        text: " ",
        icon: "info",
        buttons: false,
    })

    var url = window.location.href;
    var urlSplit = url.split('/');
    var firstpart = urlSplit[0] + '//' + urlSplit[2];
    var completeURL = firstpart + '/static/pdf/'

    var canvas = document.getElementById("signatureCanvas");

    var signature = canvas.toDataURL()


    var filename = 'timesheet' + new Date().getTime() + '.pdf';

    $.ajax({
        url: "/save_signature/",
        type: "POST",
        data: {
            signature: signature,
            tableid: 'timesheet',
            recordid: $('#signatureModal').data('recordid'),
            completeUrl: completeURL,
            filename: filename,
        },
        xhrFields: {
            responseType: 'blob'
        },
        success: function (response, status, xhr) {

            swal({
                title: "File Generato!",
                text: "Il file è stato generato e scaricato correttamente",
                icon: "success",
                timer: 800,
                buttons: false,
            })

            const contentType = xhr.getResponseHeader('content-type');
            const blob = new Blob([response], {type: contentType});

            const blobUrl = window.URL.createObjectURL(blob);

            const contentDisposition = xhr.getResponseHeader('content-disposition');
            const filename = contentDisposition.split(';')[1].trim().split('=')[1];

            const a = document.createElement('a');
            a.href = blobUrl;
            a.download = filename;
            document.body.appendChild(a);

            a.click();

            window.URL.revokeObjectURL(blobUrl);
            document.body.removeChild(a);
        },

        error: function (response, status, xhr) {

            swal({
                title: "Errore nella generazione del file",
                text: "sengnalalo ad un tecnico del software al più presto",
                icon: "error",
                button: "Ok",
                dangerMode: true,
            });

            const contentType = xhr.getResponseHeader('content-type');
            const blob = new Blob([response], {type: contentType});

            const blobUrl = window.URL.createObjectURL(blob);

            const contentDisposition = xhr.getResponseHeader('content-disposition');
            const filename = contentDisposition.split(';')[1].trim().split('=')[1];

            const a = document.createElement('a');
            a.href = blobUrl;
            a.download = filename;
            document.body.appendChild(a);

            a.click();

            window.URL.revokeObjectURL(blobUrl);
            document.body.removeChild(a);
        },
    })
}

function createCanvas() {
  // Ottieni il riferimento al canvas e al contesto 2D
var canvas = document.getElementById("signatureCanvas");
var ctx = canvas.getContext("2d");

// Variabili per tracciare la firma
var isDrawing = false;
var lastX = 0;
var lastY = 0;

// Aggiungi eventi per iniziare e finire il disegno
canvas.addEventListener("mousedown", startDrawing);
canvas.addEventListener("mouseup", endDrawing);
canvas.addEventListener("mousemove", draw);
canvas.addEventListener("touchstart", startDrawingTouch);
canvas.addEventListener("touchend", endDrawingTouch);
canvas.addEventListener("touchmove", drawTouch);

// Funzione per iniziare il disegno con il mouse
function startDrawing(e) {
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

// Funzione per finire il disegno con il mouse
function endDrawing() {
    isDrawing = false;
}

// Funzione per disegnare con il mouse
function draw(e) {
    if (!isDrawing) return;
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.strokeStyle = "#000";
    ctx.lineWidth = 5;
    ctx.stroke();
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

// Funzione per iniziare il disegno con il touch


// Funzione per finire il disegno con il touch
function endDrawingTouch() {
    isDrawing = false;
}

// Funzione per disegnare con il touch
// Funzione per iniziare il disegno con il touch
function startDrawingTouch(e) {
    isDrawing = true;
    var touch = e.touches[0];
    var rect = canvas.getBoundingClientRect();
    [lastX, lastY] = [touch.clientX - rect.left, touch.clientY - rect.top];
    e.preventDefault();
}

// Funzione per disegnare con il touch
function drawTouch(e) {
    if (!isDrawing) return;
    var touch = e.touches[0];
    var rect = canvas.getBoundingClientRect();
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(touch.clientX - rect.left, touch.clientY - rect.top);
    ctx.strokeStyle = "#000";
    ctx.lineWidth = 2;
    ctx.stroke();
    [lastX, lastY] = [touch.clientX - rect.left, touch.clientY - rect.top];
    e.preventDefault();
}


// Funzione per salvare la firma come immagine PNG
function saveSignature() {
    var dataURL = canvas.toDataURL("image/png");
    // Puoi usare dataURL per salvare l'immagine o inviarla al server
}

}


function newRecord(tableid, new_linked = '') {
    console.info('fun:newRecord')

    var serialized_data = [];
    serialized_data.push({name: 'tableid', value: tableid});
    serialized_data.push({name: 'contextfunction', value: 'insert'});
    serialized_data.push({name: 'contextreference', value: tableid});
    serialized_data.push({name: 'http_response', value: true});
    $.ajax({
        type: "POST",
        url: "/get_record_fields/",
        data: serialized_data,
        success: function (response) {
            if (new_linked == 'yes') {
                console.info('fun:newRecord - new linekd')
                $('#newLinkedRecordModal').modal('show');
                $("#newLinkdeRecordModalContent").html(response);
            } else {
                console.info('fun:newRecord - new master')
                $('#newRecordModal').modal('show');
                $("#fullwidth_modal_newrecord").html(response);
            }
        },
        error: function () {
            $("#bixdata_recordcard_container").html(response);
        }
    });
}


function newTimesheet(recordid) {
    new_linked = ''
    tableid = 'timesheet'
    var serialized_data = [];
    serialized_data.push({name: 'tableid', value: tableid});
    serialized_data.push({name: 'contextfunction', value: 'insert'});
    serialized_data.push({name: 'contextreference', value: tableid});
    serialized_data.push({name: 'http_response', value: true});
    serialized_data.push({name: 'timetr_recordid', value: recordid});
    $.ajax({
        type: "POST",
        url: "/new_timesheet/",
        data: serialized_data,
        success: function (response) {
            if (new_linked == 'yes') {
                console.info('fun:newRecord - new linekd')
                $('#newLinkedRecordModal').modal('show');
                $("#newLinkdeRecordModalContent").html(response);
            } else {
                console.info('fun:newRecord - new master')
                $('#newRecordModal').modal('show');
                $("#fullwidth_modal_newrecord").html(response);
            }
        },
        error: function () {
            $("#bixdata_recordcard_container").html(response);
        }
    })
}


function closeNewRecordModal(el) {
    $(el).closest(".modal").modal("hide");
}

function notify_error() {
    $.ajax({
        type: "POST",
        url: "/notify_error/",
        success: function (response) {
          swal({
            title: "Si è verificato un errore",
            text: "L'errore è stato segnalato ai nostri tecnici ",
            icon: "error",
            button: "Ok",
            dangerMode: true,
        });
        },
        error: function (response) {

        }
    });
}


