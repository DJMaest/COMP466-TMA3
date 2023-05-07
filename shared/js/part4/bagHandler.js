$(function () {
    if (Cookies.get("bagItems")) {
        var items = JSON.parse(Cookies.get('bagItems')); // this would be an array of JSONs
        items.forEach(item =>{
            $("#remove-"+item.id).on("click",()=>{
                console.log(item.id);
                var new_items = items.filter((i)=> i.id != item.id);
                Cookies.set('bagItems', JSON.stringify(new_items), { expires: 60 * 60 * 24 });
                location.reload();
            });

        })
        $("#placeOrder").on("click",()=>{
                
            location.href = "/part4/order";
        });
    }

});