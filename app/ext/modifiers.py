from flask_sqlalchemy.query import Query
from app.errors.client.base import NotFoundException


def make_notfound_handling(cls: Query):
    def _first_or_404(self, description=None):
        res = self.first()
        if res is None:
            raise NotFoundException()
        return res

    setattr(cls, 'first_or_404', _first_or_404)
    return cls
