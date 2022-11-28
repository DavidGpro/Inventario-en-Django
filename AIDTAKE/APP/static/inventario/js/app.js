$(document).ready(function() {
        url = window.location.href
        url_split = url.split("/")
        found = url_split.find(v => v == 'mostrar_articulo')
        found2 = url_split.find(v => v == 'crear_articulo')
        found3 = url_split.find(v => v == 'editar_articulo')
        console.log(found3)
        category = url_split[4].split("=")[0]
        category_id = url_split[4].split("=")[1]

        if (found == 'mostrar_articulo'){
            $("#fieldset").children().attr("disabled", "disabled");
            $("#pop_up").css('visibility', 'visible');
            $(".form-visible").css('visibility', 'visible');
        }else if(found2 == 'crear_articulo'){
            $("#fieldset").removeAttr("disabled")
            $("#pop_up").css('visibility', 'visible');
            $(".save").css('visibility', 'visible');
            $(".form-visible").css('visibility', 'visible');
        }else if(found3 == 'editar_articulo'){
            $("#fieldset").removeAttr("disabled")
            $("#pop_up").css('visibility', 'visible');
            $(".save").css('visibility', 'visible');
            $(".form-visible").css('visibility', 'visible');
        }else if(category == '?category'){
            $('.icon-box').removeClass("selected")
            $("div").find(`[data-info='${category_id}']`).addClass('selected')
        }else if(category == '?stock'){
            $('.box').removeClass("selected")
            $("div").find(`[data-info='${category_id}']`).addClass('selected')
        }else{
            $("#pop_up").css('visibility', 'hidden');
        }

        $( ".gear-box" ).click(function() {
            let data = $(this).attr("data-info")
            if(data == 'quit'){
                if ($(".circle-quit").css('visibility') == 'visible'){
                    $(".circle-quit").css('visibility', 'hidden');
                }else{
                    $(".quit").css('display', 'block');
                    $(".edit").css('display', 'none');
                    $('.toggle-icon').addClass("fa-minus")
                    $('.toggle-icon').removeClass("fa-pencil")
                    $('.toggle-icon').addClass("red")
                    $(".circle-quit").css('visibility', 'visible');
                }
            }else if(data == 'edit'){
                if ($(".circle-quit").css('visibility') == 'visible'){
                    $(".circle-quit").css('visibility', 'hidden');
                }else{
                    $(".quit").css('display', 'none');
                    $(".edit").css('display', 'block');
                    $('.toggle-icon').removeClass("fa-minus")
                    $('.toggle-icon').addClass("fa-pencil")
                    $('.toggle-icon').removeClass("red")
                    $(".circle-quit").css('visibility', 'visible');
                }
            }
        });

        $( ".box" ).click(function() {
            let data = $(this).css('background-color')
            if (data == 'rgb(255, 255, 255)'){
                $(".box").removeClass("selected")
                $(this).addClass("selected")
            }
        });

        $( ".icon-box" ).click(function() {
            let data = $(this).css('background-color')
            if (data == 'rgb(255, 255, 255)'){
                $(".icon-box").removeClass("selected")
                $(this).addClass("selected")
            }
            if ($(this).attr("data-info") == 'all'){
                $(".fa-globe").css('color', '#fff');
            }else{
                $(".fa-globe").css('color', '#000000');
            }
        });
})