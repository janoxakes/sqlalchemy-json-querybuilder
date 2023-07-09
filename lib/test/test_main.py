from lib.sqlalchemy_json_querybuilder.querybuilder.search import Search
from src.examples import models

from sqlalchemy.orm import Session

def test_dummy_true():
    assert True

def test_dummy():
    try:
        Search(session=Session(), model_module=models, model_classes=[models.Image, models.Tag], filter_by=[], order_by=(), page=1, per_page=10, all=False,
                    window_size=None).query()
        return
    except Exception as exc:
        raise Exception from exc
