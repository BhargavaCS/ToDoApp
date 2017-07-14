$(document).ready(function(){
        var id;
       var helperpath=$('meta[name=staticpath]').attr("content");
       var model_desc="<div id='myModal_update' class='modal fade' role='dialog'><div class='modal-dialog'><!-- Modal content--> <div class='modal-content'><div class='modal-header'><button type='button' class='close' data-dismiss='modal'>&times;</button><h4 class='modal-title'>To Do Item</h4></div><div class='modal-body'><input type='text' placeholder='Enter Item Description Here' id='list_user'><br><br><input type='date' placeholder='Enter Completion Date Here' id='list_user_date'><br><br><input type='text' placeholder='Enter Completed Or Not Here' id='list_user_completed'><br><br></div><div class='modal-footer'><button type='button' class='btn btn-default' data-dismiss='modal'>Create/Update</button></div></div></div></div>"
       var model_date="<div id='myModal' class='modal fade' role='dialog'><div class='modal-dialog'><!-- Modal content--> <div class='modal-content'><div class='modal-header'><button type='button' class='close' data-dismiss='modal'>&times;</button><h4 class='modal-title'>Create List</h4></div><div class='modal-body'><input type='text' placeholder='Enter List Name Here' id='list_user'></div><div class='modal-footer'><button type='button' class='btn btn-default' data-dismiss='modal'>Create</button></div></div></div></div>"
       var model_completed="<div id='myModal' class='modal fade' role='dialog'><div class='modal-dialog'><!-- Modal content--> <div class='modal-content'><div class='modal-header'><button type='button' class='close' data-dismiss='modal'>&times;</button><h4 class='modal-title'>Create List</h4></div><div class='modal-body'><input type='text' placeholder='Enter List Name Here' id='list_user'></div><div class='modal-footer'><button type='button' class='btn btn-default' data-dismiss='modal'>Create</button></div></div></div></div>"



       function generate_lists_items(id)
       {
                //alert("Gen");
                window.close();
                $.get("/todoapp/rest/lists/"+id+"/items/",function(data,status){
                    //
                    //$('.table').append(JSON.stringify(data));
                    str="<html><body style='background-image:url'"+"('http://www.zarofil.com/i/2017/06/plain-light-green-wallpapers-high-quality-resolution.jpg')"+"'><h1 align=center>All ToDo Items <br><br>"
                    str+="<div class='btn btn-warning itemscreate'>Create</div><br></br></h1>"
                    str+="<table class='table table-hover'>"
                     r=0;
                    str+="<thead class='thead-inverse'  ><tr ><th style='text-align:center;'>SNo.</th><th style='text-align:center;'>Item</th><th style='text-align:center;'>Completed</th><th style='text-align:center;'>Due Date</th><th style='text-align:center;'>Action</th></tr></thead>"
                    $.each(data, function() {
                           console.log(JSON.stringify(data));
                        str += "<tr  class='btn-default' id='" + data[r].id + "'><td></td>";
                         r+=1;
                          $.each(this, function(k, v) {

                            temp_id="myclick_"+k+"_"+data[r-1].id;
                            temp_class="myclick_"+k;
                            console.log(temp_class);
                            console.log(temp_id);
                            if(k!="id" &&  k!="parent"){ str+="<td style='text-align:center;' class='"+k+"'>"+JSON.stringify(this)+"</td>"
                            }
                          });
                    str+="<td><i class='fa fa-edit btn btn-outline-warning itemsupdate' aria-hidden='true'></i><span style='margin-left:10px;'><i class='fa fa-trash btn btn-outline-danger itemsdelete' aria-hidden='true'></i></span></td>"
                        str+="</tr>"
                    });
                    str+="</table>"
                    str+="<a href=''>Back</a>"+model_desc+model_completed+model_date+'</body></html>';
                    console.log(str);
                    $('#temp_body').empty()
                    $('#temp_body').append(str);
            });
       }


     $("body").on('click','.dispitems',function(){
            id=$(this).parent().parent().attr("id");
            generate_lists_items(id);
     });

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


     $("body").on("click",".itemsupdate",function(){
            par=$(this).parent().parent();
            item_id1=$(this).parent().parent().attr("id");
            $("#myModal_update").modal('show');
            $("#myModal_update").on("hide.bs.modal",function(){
            desc=$('#list_user').val();
            completed=$('#list_user_date').val();
            due_by=$('#list_user_completed').val();
            $.ajax({
                url:"/todoapp/rest/items/"+item_id1+"/",
                data:{
                        "description": desc,
                        "completed": due_by,
                        "due_by": completed,
                        "parent": id},
                type:'PUT',
                beforeSend: function(xhr){
                     xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success:function(response){
                    arr=$(par).find('td');
                    //console.log(arr);
                    $(arr[1]).text(desc);
                    $(arr[3]).text(completed);
                    $(arr[2]).text(due_by);
                    //console.log(arr);
                    //alert("Updating Here");
                }
            });
     });
     });


     $("body").on("click",".itemsdelete",function(){
            par=$(this).parent().parent().parent()
            item_id=$(this).parent().parent().parent().attr("id");
            $.ajax({
                url:"/todoapp/rest/items/"+item_id+"/",
                type:'DELETE',
                beforeSend: function(xhr){
                     xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success:function(response){
                    $(par).empty();
                }
            });
            //generate_lists_items(id);
     });


    $("body").on("click","#myheading",function(){
            //alert("Here");
            $("#myModal").modal('show');
            $("#myModal").on("hide.bs.modal",function(){
                ans=$('#list_user').val();
                $.ajax({
                url:"/todoapp/rest/lists/",
                data:{"name":ans},
                type:'POST',
                beforeSend: function(xhr){
                     xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success:function(response){
                   location.reload();
                   //$('#temp_body').empty();
                }
            });
            });
    });

    $("body").on("click",".update",function(){
        check=$(this).parent().parent().attr("id");
        $("#myModal").modal('show');
        $("#myModal").on("hide.bs.modal",function(){
        ans=$('#list_user').val();
        $.ajax({
                url:"/todoapp/rest/lists/"+check+"/",
                type:'PUT',
                data:{"name":ans},
                beforeSend: function(xhr){
                     xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success:function(response){
                   arr=$('#'+check).find("td");
                   $(arr[1]).children(".text").text(ans);
                   console.log(arr);
                }
            });
    });
    });


    $("body").on("click",".delete",function(){
        check=$(this).parent().parent().parent().attr("id");
        $.ajax({
                url:"/todoapp/rest/lists/"+check+"/",
                type:'DELETE',
                beforeSend: function(xhr){
                     xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success:function(response){
                   $('#'+check).empty();
                }
            });
    });


    $("body").on("click",".itemscreate",function(){
            par=$(this).parent().parent();
            var desc=""
            var completed=""
            var due_by=""
            item_id1=$(this).parent().parent().attr("id");
            $("#myModal_update").modal('show');
            $("#myModal_update").on("hide.bs.modal",function(){
            desc=$('#list_user').val();
            completed=$('#list_user_date').val();
            due_by=$('#list_user_completed').val();
            $.ajax({
                url:"/todoapp/rest/lists/"+id+"/items/",
                data:{
                        "description": desc,
                        "completed": due_by,
                        "due_by": completed,
                      },
                type:'POST',
                beforeSend: function(xhr){
                     xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success:function(response){
                    generate_lists_items(id);
                    alert("To Do Item Added Successfully into the ToDoList");
                }
            });

   });
});



     $("body").on("click",".myclick_description",function(){
            var curr=$(this).attr("class");
            var mid=$(this).attr("id");
            $("#myModal").modal('show');
            $("#myModal").on("hide.bs.modal",function(){
            ans=$('#list_user').val();
            //#alert('#'+mid);
            $("#"+mid).attr("value",ans);
            $("input").change(function ()
            {
                alert("hi");
              flagChanges();
            });
     });



 });

 });
