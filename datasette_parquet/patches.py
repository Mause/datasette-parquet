from datetime import date

def monkey_patch():
    from datasette.utils import CustomJSONEncoder

    original_default = CustomJSONEncoder.default

    def patched_default(self, obj):
        # We serialize dates as their ISO string.
        # An alternative: we could serialize them with metadata, eg
        # { 'type': 'date', 'value': '2022-12-25' }
        #
        # ...but I think metadata should be a separate thing.
        if isinstance(obj, date):
            return obj.isoformat()

        return original_default(self, obj)

    CustomJSONEncoder.default = patched_default


