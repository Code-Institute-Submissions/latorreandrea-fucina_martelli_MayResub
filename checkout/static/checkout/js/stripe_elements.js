var str_stripe_public_key = document.getElementById("id_stripe_public_key").innerHTML;
var stripePublicKey = str_stripe_public_key.slice(1, -1);

var str_client_secret = document.getElementById("id_client_secret").innerHTML;
var clientSecret = str_client_secret.slice(1, -1);

var stripe = Stripe(stripePublicKey);

var elements = stripe.elements();


var style = {
    base: {
        color: '#000',
        fontFamily: '"Rubik", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};

var card = elements.create('card', {
    style: style
});

card.mount('#card-element')

// Handle form submit
var form = document.getElementById('payment');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});