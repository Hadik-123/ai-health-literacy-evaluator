from evaluator.readability import compute_readability

def test_compute_readability_basic():
    res = compute_readability("This is a simple sentence. This is another.")
    assert "fk_grade" in res and res["sentences"] >= 1
