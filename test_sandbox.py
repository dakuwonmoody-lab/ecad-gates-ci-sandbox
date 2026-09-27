"""Toy test suite for the Gate-12 sandbox: mirrors the real pytest job at
reduced scale (matrix integrity only)."""
import json


def _rows():
    return json.load(open("sandbox-matrix.json"))


def test_matrix_loads_and_ids_unique():
    rows = _rows()
    ids = [r["id"] for r in rows]
    assert ids and len(ids) == len(set(ids))


def test_all_rows_have_next_step():
    rows = _rows()
    assert all(r["next"] for r in rows)
