//index
const min_width = 1280;
 const fhd_width = 1920;



        if (screen.width <= min_width) {
            $("html").attr("data-sidenav-size", "condensed");
            $(".tabs-title").attr("display", "none");
            $(".tabs-icon").attr("display", "visible");
            $(".card-body").attr("display", "none");
        }





        $("#bixdata2").ready(function () {
            getDashboard();

            $("#toggle-menu").click(function () {
                //$("#content-container").load('http://127.0.0.1:8000/loading/');
                var current_sidenav_size = $("html").attr("data-sidenav-size");
                if (current_sidenav_size == 'default') {
                    $("html").attr("data-sidenav-size", "condensed");
                } else {
                    $("html").attr("data-sidenav-size", "default");
                }

            });




        });

        function getContentRecords(tableid) {
            var serialized_data = [];
            $("#content-container").load('http://127.0.0.1:8000/loading/');
            serialized_data.push({ name: 'tableid', value: tableid });
            serialized_data.push({ name: 'searchTerm', value: '' });
            $.ajax({
                type: "POST",
                crossDomain: true,
                url: "{% url 'content_records' %}",
                data: serialized_data,
                success: function (response) {
                    $("#content_container").html(response);
                    $('[data-toggle="tooltip"]').tooltip();
                },
                error: function () {
                    $("#content_container").html(response);
                }
            });
        }

        function getRenderChartsView() {
            var serialized_data = [];

            $.ajax({
                type: "POST",
                crossDomain: true,
                url: "{% url 'charts_view' %}",
                data: serialized_data,
                success: function (response) {
                    $("#content-container").load('http://127.0.0.1:8000/loading/');
                    $("#content_container").html(response);
                    $('[data-toggle="tooltip"]').tooltip();
                },
                error: function () {
                    $("#content-container").load('http://127.0.0.1:8000/loading/');
                    $("#content_container") .html(response);
                }
            });
        }

        function getDashboard()
        {
            var serialized_data = [];
            $("#content-container").load('http://127.0.0.1:8000/loading/');
            $.ajax({
                type: "POST",
                crossDomain: true,
                url: "{% url 'dashboard' %}",
                data: serialized_data,
                success: function (response) {
                    $("#content_container").html(response);
                    $('[data-toggle="tooltip"]').tooltip();
                },
                error: function () {
                    $("#content_container").html(response);
                }
            });
        }

        //records

   $("#tables").ready(function() {




        $('[data-bs-toggle="popover"]').popover();


        $('button[data-bs-toggle="tab"]').each(function(i){
            if($(this).attr("id")=='gantt-tab')
            {
                $(this)[0].addEventListener('shown.bs.tab', function (event) {
                    searchGantt()
                })
            }
            if($(this).attr("id")=='kanban-tab')
            {
                $(this)[0].addEventListener('shown.bs.tab', function (event) {
                    searchKanban()

                })
            }
            if($(this).attr("id")=='calendar-tab')
            {
                $(this)[0].addEventListener('shown.bs.tab', function (event) {
                    searchCalendar()
                })
            }
            if($(this).attr("id")=='chart-tab')
            {
                $(this)[0].addEventListener('shown.bs.tab', function (event) {
                    searchChart()
                })
            }
        })

        if (screen.width <= min_width) {
                $("#block-record-card-container").css('display', 'none');
                $("#block-records-search-container").css('width', '100%');
            }



    })





    $(function() {
        $('#calendar-tab a:last').tab('show');
    });


    function searchGantt(){
        var serialized_data = [];
        serialized_data.push({
            name: 'table',
            value: ''
        });
        serialized_data.push({
            name: 'searchTerm',
            value: $("#searchTerm").val()
        });

        $.ajax({
            type: "POST",
            url: "{% url 'block_records_gantt' %}",
            data: serialized_data,
            success: function(response) {
                $("#gantt-tab-pane").html(response);
            },
            error: function() {
                $("#gantt-tab-pane").html(response);
            }
        });
    }

    function searchKanban(){
        var serialized_data = [];
        $.ajax({
            type: "POST",
            url: "{% url 'block_records_kanban' %}",
            data: serialized_data,
            success: function(response) {
                console.info(response)
                $("#kanban-tab-pane").html(response);
            },
            error: function() {
                $("#kanban-tab-pane").html(response);
            }
        });
    }

    function searchCalendar() {
        var serialized_data = [];
        serialized_data.push(
            {name: 'tableid',value: '{{tableid}}'}
        );
        $.ajax({
            type: "POST",
            url: "{% url 'block_records_calendar' %}",
            data: serialized_data,
            success: function(response) {
                $("#calendar-tab-pane").html(response);
            },
            error: function() {
                $("#calendar-tab-pane").html(response);
            }
        });
    }

    function searchChart() {
        var serialized_data = [];
        serialized_data.push({
            name: 'table',
            value: ''
        });
        serialized_data.push({
            name: 'searchTerm',
            value: $("#searchTerm").val()
        });

        $.ajax({
            type: "POST",
            url: "{% url 'block_records_chart' %}",
            data: serialized_data,
            success: function(response) {
                $("#chart-tab-pane").html(response);
            },
            error: function() {
                $("#chart-tab-pane").html(response);
            }
        });
    }


    function search() {
        var serialized_data = [];
        serialized_data.push({
            name: 'table',
            value: ''
        });
        serialized_data.push({
            name: 'searchTerm',
            value: $("#searchTerm").val()
        });

        $.ajax({
            type: "POST",
            url: "{% url 'block_records_table' %}",
            data: serialized_data,
            success: function(response) {
                $("#records-table-container").load('http://127.0.0.1:8000/loading/');
                $("#records_table_container").html(response);
            },
            error: function() {
                $("#records_table_container").load('http://127.0.0.1:8000/loading/');
                $("#records_table_container").html(response);
            }
        });
    }

    $("#searchTerm").ready(function() {
        $("input").keypress(function() {
            var keycode = (event.keyCode ? event.keyCode : event.which);
            if (keycode == '13') {
                var serialized_data = [];
                serialized_data.push({
                    name: 'table',
                    value: '{{tableid}}'
                });
                serialized_data.push({
                    name: 'searchTerm',
                    value: $("#searchTerm").val()
                });
                serialized_data.push({
                    name: 'viewid',
                    value: null
                });
                $.ajax({
                    type: "POST",
                    url: "{% url 'block_records_table' %}",
                    data: serialized_data,
                    success: function(response) {
                        $("#records_table_container").html(response);
                    },
                    error: function() {
                        $("#records_table_container").html(response);
                    }
                });
            }
        });
    });



    function checkWidth(response) {
        if (screen.width > min_width) {
            $("#bixdata_recordcard_container").html(response);
        } else {
            $("#fullwidth_modal").html(response);
            $("#fullwidth_modal_newrecord").html(response);
        }
    }

    function newRecord() {
        var tableid='{{tableid}}'
        $('#newRecordModal').modal('show');
        var serialized_data = [];
        serialized_data.push({name: 'tableid',value: tableid});
        serialized_data.push({name: 'function',value: 'insert'});
        serialized_data.push({name: 'http_response',value: true});
        $.ajax({
            type: "POST",
            url: "{% url 'get_record_fields' %}",
            data: serialized_data,
            success: function(response) {
                $("#fullwidth_modal_newrecord").html(response);

            },
            error: function() {
                $("#bixdata_recordcard_container").html(response);
            }
        });


    }

    function reloadFunc()
    {
        getContentRecords('{{ tableid }}')
        var serialized_data = [];
        serialized_data.push({
            name: 'table',
            value: ''
        });
        $.ajax({
            type: "POST",
            url: "{% url 'block_reload' %}",
            data: serialized_data,
            success: function(response) {
            },
            error: function() {
            }
        })
    }



    function open_record(tableid,recordid) {
        var serialized_data = [];
        serialized_data.push({name: 'tableid',value: tableid});
        serialized_data.push({name: 'recordid',value: recordid});
        if (screen.width <= min_width) {
            $('#recordModal').modal('show');
            $("#fullwidth_modal").load('http://127.0.0.1:8000/loading/');
        }
        //$("#block-record-card-container").html('caricamento');
        $("#block-record-card-container").load('http://127.0.0.1:8000/loading/');
        $.ajax({
            type: "POST",
            url: "{% url 'block_record_card' %}",
            data: serialized_data,
            success: function(response) {
                if ($('block_records_table').attr(type))
                if (screen.width > min_width) {
                    $("#block-record-card-container").html(response);
                } else {
                    $("#fullwidth_modal").html(response);
                }
            },
            error: function() {
                $("#bixdata_recordcard_container").html(response);
            }
        });

    }
/*
    function closeCard(vrbl) {
        console.log('chiudendo base')
        $("#linked-table-modal").modal("hide");
        if (screen.width > min_width) {
            $(vrbl).closest("#RecordCard").slideToggle(200, function() {
                $('#bixdata_recordcard_container').html('');
            });
        } else {
            $("#recordModal").modal("hide");

    }
}
*/
    function closeNewRecordModal() {
        $("#newRecordModal").modal("hide");
    }

    function open_kanban() {
        var serialized_data = [];
        $.ajax({
            type: "POST",
            url: controller_url + 'ajax_get_kanban',
            data: serialized_data,
            success: function(response) {
                $("#bixdata_results_container").html(response);
            },
            error: function() {
                $("#bixdata_results_container").html(response);
            }
        });
    }

    //record card

   $("#RecordCard").ready(function() {

        $('[data-bs-toggle="tooltip"]').tooltip();

    });



    function closeModal() {
        $("#recordModal").modal("hide");
    }

    //appena la card carica aprire collegato di default
    $(document).ready(function() {
        document.getElementById("linked-tab").click();
    });




    function caricaRis(el) {
        $(el)
        var serialized_data = [];
        //$("#bixdata_recordcard_container").load('Loading.php');
        /*
         $.ajax({
             type: "POST",
             url: controller_url + 'ajax_get_recordcard',
             data: serialized_data,
             success: function(response) {
                 //$("#bixdata_recordcard_container").html(response);
                 $("#bixdata_recordcard_container").html('test');
             },
             error: function() {
                 $("#bixdata_recordcard_container").html(response);
             }
         });*/
    }

    if (screen.width <= min_width) {
        if ($("html").attr("data-sidenav-size") == "condensed") {
            $(".tabs-title").css("display", "none");
            $(".tabs-icon").css("display", "block");
        }
    } else {
        $(".tabs-title").css("display", "block");
        $(".tabs-icon").css("display", "none");
    }

    function copyFunc() {
        var serialized_data = [];
        $.ajax({
            type: "POST",
            type: "POST",
            url: "{% url 'record_card_copy' %}",
            data: serialized_data,
            success: function(response) {
                //$("#bixdata_recordcard_container").html(response);
                alert('copy')
            },
            error: function() {
                alert('copy')
            }
        });
    }

    function deleteFunc() {
        var serialized_data = [];
        $.ajax({
            type: "POST",
            url: "{% url 'record_card_delete' %}",
            data: serialized_data,
            success: function(response) {
                //$("#bixdata_recordcard_container").html(response);
                alert('delete')
            },
            error: function() {
                alert('delete')
            }
        });
    }

    function permissionsFunc()
    {
        var serialized_data = [];
        $.ajax({
            type: "POST",
            url: "{% url 'record_card_permissions' %}",
            data: serialized_data,
            success: function(response) {
                //$("#bixdata_recordcard_container").html(response);
                alert('permissions')
            },
            error: function() {
                alert('permissions')
            }
        });
    }

    function pinFunc() {
        var serialized_data = [];
        $.ajax({
            type: "POST",
            url: "{% url 'record_card_pin' %}",
            data: serialized_data,
            success: function(response) {
                //$("#bixdata_recordcard_container").html(response);
                alert('pin')
            },
            error: function() {
                alert('pin')
            }
        });
    }

    //record fields

    $(document).ready(function(){
      $("input").attr("disabled", true);
      $("select").attr("disabled", true);
      $("textarea").attr("disabled", true);
      document.getElementById("save-button").style.display = "none";
    });
    $(document).ready(function(){
      $("input").attr("disabled", false);
      $("select").attr("disabled", false);
      $("textarea").attr("disabled", false);
    });

    function save_record() {

    closeNewRecordModal()
    var serialized_array = $('#fields_container').find("select,textarea,input").serializeArray();
    var serialized_json=convertFormToJSON(serialized_array);
    var post_data=[];
    post_data.push({name: 'tableid',value: '{{ tableid }}'});
    post_data.push({name: 'recordid',value: '{{ recordid }}'});
    post_data.push({name: 'fields',value: serialized_json});


    $.ajax({
        type: "POST",
        url: "{% url 'save_record_fields' %}",
        data: post_data,
        success: function(response) {
            document.getElementById("saved-alert").style.display = "block";
            setTimeout(function() {
                $("#saved-alert").fadeOut(1500);
                getContentRecords('{{ tableid }}')
            });

        },
        error: function() {
            alert('ko')
        }
    });

}

//record linked

function triggerCollapse(id, label) {
        var collapse = document.getElementById(id);
        if (collapse.classList.contains('show')) {
            collapse.classList.remove('hide');
        } else {
            collapse.classList.add('hide');
        }
        $.ajax({
            url: '/get_linked/',
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': '{{ csrf_token }}',
                'name': label
            },
            success: function (response) {
                console.log(response);
            }, error: function (response) {
                console.log(response);
            }
        });
    }

    //records gantt

   //alert si apre con il doppio click sulla task
        $("#content_records_gantt").ready(function() {


            $(function(){
                var tasks = '{{records_json|safe}}';
                tasks=jQuery.parseJSON(tasks);

                // Get the Gantt task elements
                var gantt = new Gantt('#tasks-gantt',tasks, {
                    //Add click event listener to tasks
                    on_click: function(task) {
                        alert("Task: " + task.name);
                    }
                });
            });
        });

    //records kanban

    function update_status(el) {
        var div_col = $(el).closest('.tasks');

    }

    var tsi_id = [];

    $(".task-list-items").each(function(index) {
        var element_id = $(this).attr("id");
        tsi_id.push(document.getElementById(element_id));
    });
    console.log('Kanban debug:');
    console.log(tsi_id);

    dragula(tsi_id).on('drop', function(el) {
        update_status(el);
    });

    var cards = document.querySelectorAll('.kanban-record');
    cards.forEach(function(card) {
        card.addEventListener('click', function() {
            alert('alert');
        });
    });

    //records table

  function modalShow() {
        $("#recordModal").load('http://127.0.0.1:8000/loading/');
        $("results-row").click(function(){
            if (screen.width <= min_width) {
              $("#recordModal").modal("show");
            }
          });
    }