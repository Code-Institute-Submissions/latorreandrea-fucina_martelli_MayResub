from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    event = None


    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Set up webhook
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions

    event_map = {
        "payment_intent_succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent_failed": handler.handle_payment_intent_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    # call the event handler with the event
    response = event_handler(event)
    return response