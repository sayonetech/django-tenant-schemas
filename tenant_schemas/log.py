import logging

from django.db import connections, router


class TenantContextFilter(logging.Filter):
    """
    Add the current ``schema_name`` and ``domain_url`` to log records.

    Thanks to @regolith for the snippet on #248
    """
    def filter(self, record):
        db = router.db_for_read(None)
        connection = connections[db]
        record.schema_name = connection.tenant.schema_name
        record.domain_url = getattr(connection.tenant, 'domain_url', '')
        return True
