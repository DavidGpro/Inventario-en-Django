
$(document).ready(function () {

    //$("#id_Alergenos").addClass('flex-row');
    //$("#id_Alergenos").addClass('flex-row');

    url = window.location.href
    url_split = url.split("/")
    found = url_split.find(v => v == 'mostrar_producto')
    found2 = url_split.find(v => v == 'crear_producto')
    found3 = url_split.find(v => v == 'editar_producto')
    found3 = url_split.find(v => v == 'editar_producto')
    category = url_split[4].split("=")[0]
    category_id = url_split[4].split("=")[1]

    if (found == 'mostrar_producto') {
        $("#fieldset").children().attr("disabled", "disabled");
        $("#pop_up").css('visibility', 'visible');
        $(".form-visible").css('visibility', 'visible');
    } else if (found2 == 'crear_producto') {
        $("#fieldset").removeAttr("disabled")
        $("#pop_up").css('visibility', 'visible');
        $(".save").css('visibility', 'visible');
        $(".form-visible").css('visibility', 'visible');
    } else if (found3 == 'editar_producto') {
        $("#fieldset").removeAttr("disabled")
        $("#pop_up").css('visibility', 'visible');
        $(".save").css('visibility', 'visible');
        $(".form-visible").css('visibility', 'visible');
    } else if (category == '?category') {
        $('.icon-box').removeClass("selected")
        $("div").find(`[data-info='${category_id}']`).addClass('selected')
    } else if (category == '?stock') {
        $('.box').removeClass("selected")
        $("div").find(`[data-info='${category_id}']`).addClass('selected')
    } else {
        $("#pop_up").css('visibility', 'hidden');
    }

    $(".gear-box").click(function () {
        let data = $(this).attr("data-info")
        if (data == 'quit') {
            if ($(".circle-quit").css('visibility') == 'visible') {
                $(".circle-quit").css('visibility', 'hidden');
            } else {
                $(".quit").css('display', 'block');
                $(".edit").css('display', 'none');
                $('.toggle-icon').addClass("fa-minus")
                $('.toggle-icon').removeClass("fa-pencil")
                $('.toggle-icon').addClass("red")
                $(".circle-quit").css('visibility', 'visible');
            }
        } else if (data == 'edit') {
            if ($(".circle-quit").css('visibility') == 'visible') {
                $(".circle-quit").css('visibility', 'hidden');
            } else {
                $(".quit").css('display', 'none');
                $(".edit").css('display', 'block');
                $('.toggle-icon').removeClass("fa-minus")
                $('.toggle-icon').addClass("fa-pencil")
                $('.toggle-icon').removeClass("red")
                $(".circle-quit").css('visibility', 'visible');
            }
        }
    });

    $(".box").click(function () {
        let data = $(this).css('background-color')
        if (data == 'rgb(255, 255, 255)') {
            $(".box").removeClass("selected")
            $(this).addClass("selected")
        }
    });

    $(".icon-box").click(function () {
        let data = $(this).css('background-color')
        if (data == 'rgb(255, 255, 255)') {
            $(".icon-box").removeClass("selected")
            $(this).addClass("selected")
        }
        if ($(this).attr("data-info") == 'all') {
            $(".fa-globe").css('color', '#fff');
        } else {
            $(".fa-globe").css('color', '#000000');
        }
    });

    $('#list1 input:checkbox').click(function () {
        let value = $(this).is(":checked")
        let text = $(this).attr('data-info')
        if (value == true) {
            [...document.querySelectorAll('#table-tam tbody tr')].forEach((row, i) => {
                const input = document.createElement("input")
                input.setAttribute('type', 'text')
                const cell = document.createElement(i ? "td" : "th")
                cell.appendChild(input)
                row.appendChild(cell)
            });
            [...document.querySelectorAll('#table-tam thead tr')].forEach((row, i) => {
                const cell = document.createElement(i ? "td" : "th")
                cell.append(text)
                row.appendChild(cell)
            });
        } else {
            // [...document.querySelectorAll('#table-tam tbody tr')].forEach((row, i) => {
                // const input = document.createElement("input")
                // input.setAttribute('type', 'text')
                // const cell = document.createElement(i ? "td" : "th")
                // cell.appendChild(input)
                // row.appendChild(cell)
            //     console.log(row)
            // });
            // [...document.querySelectorAll('#table-tam thead tr')].forEach((row, i) => {
                // const cell = document.createElement(i ? "td" : "th")
                // cell.append(text)
                // row.appendChild(cell)
            //     console.log(row)
            // });
            var table = document.getElementById('table-tam'),
                rows = table.rows;

            for (var i = 0; i < rows[0].cells.length; i++) {
                var str = rows[0].cells[i].innerHTML;
                if (str.search("<span></span>") != -1) {
                    for (var j = 0; j < rows.length; j++) {
                        rows[j].deleteCell(i);
                    }
                }
            }
        }
    })
    $('#add_tam').click(function () {
        [...document.querySelectorAll('#table-tam tbody tr')].forEach((row, i) => {
            const input = document.createElement("input")
            input.setAttribute('type', 'text')
            const cell = document.createElement(i ? "td" : "th")
            cell.appendChild(input)
            row.appendChild(cell)
        });
        [...document.querySelectorAll('#table-tam thead tr')].forEach((row, i) => {
            const cell = document.createElement(i ? "td" : "th")
            cell.append('S')
            row.appendChild(cell)
        });
    })

    $('#table-tam select').change(function () {
        var name = $('#table-tam select option').filter(':selected').text()
        var number = $('#table-tam select option').filter(':selected').val()
        if (number || null){
            var tbodyRef = document.getElementById('table-tam').getElementsByTagName('tbody')[0];
            var newRow = tbodyRef.insertRow();
            var newCell = newRow.insertCell();
            var newText = document.createTextNode(name);
            newCell.appendChild(newText);
        }
    })
})

