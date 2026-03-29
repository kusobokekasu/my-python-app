from app import add

def test_add():
    assert add(2, 3) == 5
    # 2 + 3は5なので、6と比較すれば必ず失敗します
    # assert add(2, 3) == 6
    print("Test Passed!")
