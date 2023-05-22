function load_fields(el, tableid, recordid) {
    $.ajax({
        type: "POST",
        url: "/get_record_fields/",
        data: {
            'http_response': 'true',
            'tableid': tableid,
            'recordid': recordid,
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