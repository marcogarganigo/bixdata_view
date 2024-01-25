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
            $(el).closest('.block_record_card').find('.tab-pane-fields').append(response)
        },
        error: function (response) {
            $(el).closest('.block_record_card').find('.tab-pane-fields').append(response)
        }
    });
}

function save_record(el) {
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
            dangerMode: true
        });

    } else {

        serialized_form = serializeForm($(el).closest('#universal-container-timesheet').find('.fields_container').find("select,textarea,input"));
        serialized_form['creator'] = '{{ userid}}';
        serialized_json = convertFormToJSON(serialized_form);
        var post_data = [];
        post_data.push({name: 'tableid', value: tableid});
        post_data.push({name: 'recordid', value: recordid});
        post_data.push({name: 'fields', value: serialized_json});
        post_data.push({name: 'contextfunction', value: contextfunction});


        //closeNewRecordModal()
        $(el).closest('.modal').modal("hide");
        $.ajax({
            type: "POST",
            url: "/save_record_fields/",
            data: post_data,
            success: function (response) {
                saved_recordid = response
                if ((master_tableid == 'None')) {
                    refresh();
                } else {
                    load_linked(tableid + '-' + master_recordid, tableid, master_recordid, master_tableid)
                    load_badge(master_tableid, master_recordid)
                }


                setTimeout(function () {


                    //$('#fields_container_' + tableid + '_' + recordid).load('/loading/');


                    if ((master_tableid == 'None') && tableid != 'deal') {
                        if (window.innerWidth > min_width) {
                            if ($('#recordModal').hasClass('show')) {
                                open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
                            } else {
                                open_record(window.content, tableid, saved_recordid, contextfunction, 'card')
                            }
                        }
                    }


                    if (window.innerWidth < min_width) {
                        open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
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
                alert('ko')
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