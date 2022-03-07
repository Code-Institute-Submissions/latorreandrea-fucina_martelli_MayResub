var str_stripe_public_key = document.getElementById("id_stripe_public_key").innerHTML;
var stripe_public_key = str_stripe_public_key.slice(1, -1);

var str_client_secret = document.getElementById("id_client_secret").innerHTML;
var client_secret = str_client_secret.slice(1, -1);

var stripe = Stripe(stripe_public_key);

var elements = stripe.elements();


var style = {
    base: {
        color: '#000',
        background: 'antiquewhite',
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