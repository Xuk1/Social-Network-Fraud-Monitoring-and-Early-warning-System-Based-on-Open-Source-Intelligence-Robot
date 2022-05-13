$(function () {
    $(".views").click(function (){
        window.location.href = "manage-profile.html"
    })

    $(".edit").click(function () {
        window.location.href = "authentication-reset-password.html"
    })

    $(".delete").click(function () {
        let tr = this.parentNode.parentNode.parentNode;
        let flag = confirm("是否删除？");
        if(flag){
            tr.remove();
        }
    })
})