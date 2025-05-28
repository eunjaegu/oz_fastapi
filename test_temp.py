from temp import add


def test_add() -> None:
    # Given: 재료를 준비 한다.
    a, b = 1, 1

    # When: 테스트 대상이 되는 함수를 호출 한다.
    result = add(a, b)

    # Then: when 절에서 실행한 결과를 검증 한다.
    assert result == 2