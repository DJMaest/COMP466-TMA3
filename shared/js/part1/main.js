
$("#timezone").html(`<b>Your Timezone:</b> ${new Date().toLocaleTimeString('en-us',{timeZoneName:'short'}).split(' ')[2]}`)