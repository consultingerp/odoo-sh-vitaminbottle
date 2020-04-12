$(document).ready(function() {
    document.getElementsByName("delivery_type").forEach(function(item) {
        item.addEventListener("change", function() {
            if($('input[name=delivery_type]:checked').val() == $('#ppp_id').attr('delivery_id')) {
                if ($('#ppp_data').length) {
                    $('#ppp_data').show();
                } else {
                    $('#payment_method').hide();
                    $('input[name=delivery_type]:checked').parent().append('<div id="ppp_data"> \
                        <strong>Átvételi pont:</strong> <span id="ppp_name"></span><br/> \
                        <strong>Átvételi pont címe:</strong> <span id="ppp_address"></span><br/> \
                        <iframe width="100%" height="650px" src="https://online.sprinter.hu/terkep/#/"></iframe> \
                        </div>');
                }
            } else {
                if ($('#ppp_data').length) {
                    $('#ppp_data').hide();
                }
                $('#payment_method').show();
            }
        });
    });                  
});


function receiveMessage(event){
    data = JSON.parse(event.data);

    if(typeof data != 'undefined' && typeof data.shopCode != 'undefined') {
        $.ajax({
            url: '/shop/set_pickup_location?locationid='+data.shopCode+'&address='+data.address+'&name='+data.shopName,
            success: function(result) {
                $('#ppp_name').html(data.shopName);
                $('#ppp_address').html(data.address);
                $('#payment_method').show();
            }
        });
    }
}

window.addEventListener("message", receiveMessage, false);