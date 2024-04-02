class DataMixin:
    title_page = None
    extra_context = {}
    paginate_by = 2

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
