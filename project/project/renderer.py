from rest_framework.renderers import JSONRenderer

class JSONResponseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {'Data': data}
        return super().render(response_data, accepted_media_type, renderer_context)
