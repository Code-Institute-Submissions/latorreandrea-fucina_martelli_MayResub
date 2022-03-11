from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def _init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle generic webhook event
        """
        return HttpResponse(
            content=f'webhook received: {event["tipe"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        handle payment succeded webhook event from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'webhook received: {event["tipe"]}',
            status=200
        )
    
    def handle_payment_intent_failed(self, event):
        """
        handle payment failed webhook event from Stripe
        """
        return HttpResponse(
            content=f'webhook received: {event["tipe"]}',
            status=200
        )
    