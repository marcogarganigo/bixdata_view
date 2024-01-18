
    

function save_recordBAK(el) {
    console.info('FUN:index.html-save_record')
    var record_fields_container = $(el).closest('.record_fields_container')
    var tableid = $(record_fields_container).data('tableid')
    console.info(tableid)
    var contextfunction = $(record_fields_container).data('contextfunction')
    var recordid = $(record_fields_container).data('recordid')
    var master_tableid = $(record_fields_container).data('master_tableid')
    console.info('FUN:index.html-save_record: master_tableid='+master_tableid)
    var master_recordid = $(record_fields_container).data('master_recordid')
    console.info('FUN:index.html-save_record: master_recordid='+master_recordid)

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

        //var serialized_array = $(el).closest('.fields_container').find("select,textarea,input").serializeArray();
        //var serialized_json = convertFormToJSON(serialized_array);
        serialized_form = serializeForm($(el).closest('#universal-container-timesheet').find('.fields_container').find("select,textarea,input"));
        //set the value of creator in serialized_form
        serialized_form['creator'] = '{{ userid}}';
        serialized_json = convertFormToJSON(serialized_form);
        var post_data = [];
        post_data.push({name: 'tableid', value: tableid});
        post_data.push({name: 'recordid', value: recordid});
        post_data.push({name: 'fields', value: serialized_json});
        post_data.push({name: 'contextfunction', value: contextfunction});

        closeNewRecordModal()
        $.ajax({
            type: "POST",
            url: "{% url 'save_record_fields' %}",
            data: post_data,
            success: function (response) {
                saved_recordid = response
                if ((contextfunction == 'insert')) {
                    if ((master_tableid == 'None')) {
                        refresh();
                    } else {
                        load_linked(tableid + '-' + master_recordid, tableid, master_recordid, master_tableid)
                        load_badge(master_tableid, master_recordid)
                    }
                }

                setTimeout(function () {


                    $('#fields_container_' + tableid + '_' + recordid).load('/loading/');


                    if ((master_tableid == 'None') && tableid != 'deal') {
                        {% if layout_setting == 'rightcard'%}
                            if (window.innerWidth > min_width) {
                                if ($('#recordModal').hasClass('show')) {
                                    open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
                                } else {
                                    open_record(window.content, tableid, saved_recordid, contextfunction, 'card')
                                }
                            }
                        {% else %}
                            open_record(window.content, tableid, saved_recordid, contextfunction, 'modal')
                        {% endif %}
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
                    //getContentRecords('{{ tableid }}')
                    //$("#linked-container-{{ tableid }}").load('/loading/')

                    //alert('test')
                });

            },
            error: function () {
                alert('ko')
            }
        });
    }
}