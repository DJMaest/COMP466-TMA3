
$(function () {
    // Enables popover
    var toast = new bootstrap.Toast(document.getElementById("processToast"));

    toast.show();
    updateBadgeCount();
    $("[data-toggle=popover]").popover({
        html: true,
        offset: '130px,0px',
        trigger: "manual",
        template:  `<div style="padding:5px;" class="popover" role="tooltip">
                        <div class="arrow"></div>
                        <div class="popover-body"></div>
                        <a href="/part4/bag/" style="width:100%" class="btn btn-primary btn-sm">Open Bag</a>
                        <br>
                    </div>`
    });

    $("#bagBtn").on("click", ()=>{
        
        location.href="/part4/bag"
    });

});

$('body').on('click', function (e) {
    //did not click a popover toggle or popover
    if ($(e.target).data('toggle') !== 'popover'
        && $(e.target).parents('.popover.in').length === 0) { 
        $('[data-toggle="popover"]').popover('hide');
    }
});

function updateBadgeCount(){
    if (Cookies.get("bagItems")) {
        var items = JSON.parse(Cookies.get('bagItems')); // this would be an array of JSONs
        $("#badgeCount").html(items.length);

    }
}