$(function () {
    $(".signin").click(function(){
        $.post("assets/login.json",
            //发送给后端的数据
            {
                "email":$(".email").val(),
                "password":$(".password").val()
            },
            //回调函数
            function(data){
                var json=data[0];
                if(json.success == 0){
                    alert("用户名或密码错误");
                }
                else if(json.success== 1){
                    window.location.href="index2.html";
                }
            }
        )
    })
})