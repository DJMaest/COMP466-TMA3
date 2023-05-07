
console.log($("#totalPrice").data("value"));

const basePrice = parseInt($("#totalPrice").data("value"));
const premiums = { ram: 0, cpu: 0, ssd: 0, gpu: 0};
var specs= {};
if($("#gpuDefault").html()){
    specs = {
        ram: sanitizeSpecString($("#ramDefault").html()),
        cpu: sanitizeSpecString($("#cpuDefault").html()),
        ssd: sanitizeSpecString($("#ssdDefault").html()),
        gpu:sanitizeSpecString($("#gpuDefault").html()),
        model: $("#model").data("value") 
    };
} else {
    specs = {
        ram: sanitizeSpecString($("#ramDefault").html()),
        cpu: sanitizeSpecString($("#cpuDefault").html()),
        ssd: sanitizeSpecString($("#ssdDefault").html()),
        model: $("#model").data("value") 
    };

}



function updatePrice() {
    const { ram, cpu, ssd, gpu } = premiums;
    const sum = basePrice + ram + cpu + ssd + gpu;
    $("#totalPrice").html(`Total: ${sum}$`);
    $("#totalPrice").data("value", sum);
}

$(document).on('click', '.ram-select', function () {
    var premium = $(this).data('value');
    premiums.ram = premium;
    specs.ram = sanitizeSpecString($(this).html())
    $('.ram-select').removeClass("disabled");
    $(this).addClass("disabled")
    updatePrice();
});

$(document).on('click', '.ssd-select', function () {
    var premium = $(this).data('value');
    premiums.ssd = premium;
    specs.ssd = sanitizeSpecString($(this).html())
    $('.ssd-select').removeClass("disabled");
    $(this).addClass("disabled")
    updatePrice();
});

$(document).on('click', '.cpu-select', function () {
    var premium = $(this).data('value');
    premiums.cpu = premium;
    specs.cpu = sanitizeSpecString($(this).html())
    $('.cpu-select').removeClass("disabled");
    $(this).addClass("disabled")
    updatePrice();
});

$(document).on('click', '.gpu-select', function () {
    var premium = $(this).data('value');
    console.log(premium);
    premiums.gpu = premium;
    specs.gpu = sanitizeSpecString($(this).html())
    $('.gpu-select').removeClass("disabled");
    $(this).addClass("disabled")
    updatePrice();
});

$(document).on('click', '#addToBag', function () {
    var toast = new bootstrap.Toast(document.getElementById('bagToast'))
    toast.show();
    registerCookie();
});

function registerCookie() {
    const { ram, cpu, ssd, gpu } = premiums;
    const sum = basePrice + ram + cpu + ssd + gpu;
    if (Cookies.get("bagItems")) {
        var items = JSON.parse(Cookies.get('bagItems')); // this would be an array of JSONs
        
        items.push({id: items.length.toString(), price: sum,...specs});
        Cookies.set('bagItems', JSON.stringify(items), { expires: 60 * 60 * 24 });


    } else {
        var items = [{id:"0", price: sum, ...specs}];
        Cookies.set('bagItems', JSON.stringify(items), { expires: 60 * 60 * 24 });

    }
    updateBadgeCount();
}

function sanitizeSpecString(str) {
    str = str.replace(/(\r\n|\n|\r)/gm, "");
    str = str.replace(/\+[0-9]{3}\$/gm, "");
    str = str.trim();
    return str.replace(/(\r\n|\n|\r)/gm, "");
}

function updateBadgeCount(){
    if (Cookies.get("bagItems")) {
        var items = JSON.parse(Cookies.get('bagItems')); // this would be an array of JSONs
        $("#badgeCount").html(items.length);

    }
}



