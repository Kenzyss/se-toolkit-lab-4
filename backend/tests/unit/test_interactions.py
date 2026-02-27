"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes


def test_filter_excludes_interaction_with_different_learner_id() -> None:
    # Arrange
    interactions = [
        _make_log(id=1, learner_id=1, item_id=1),  # should match
        _make_log(
            id=2, learner_id=2, item_id=1
        ),  # same item_id, different learner → should match (according to current spec)
        _make_log(id=3, learner_id=3, item_id=5),  # different item → should be excluded
    ]

    # Act
    result = _filter_by_item_id(interactions, item_id=1)

    # Assert
    assert len(result) == 2, (
        "Should return both interactions with item_id=1 regardless of learner_id"
    )
    assert {log.id for log in result} == {1, 2}
<<<<<<< Updated upstream
=======


# 4. Пустой item_id (None) должен возвращать все взаимодействия
def test_filter_by_item_id_none_returns_all() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),
        _make_log(3, 1, 5),
        _make_log(4, 3, 999),
    ]
    result = _filter_by_item_id(interactions, None)
    assert len(result) == 4
    assert result == interactions  # порядок и содержимое сохраняются


# 5. Фильтр по item_id, которого вообще нет → пустой список
def test_filter_by_non_existent_item_id_returns_empty() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),
        _make_log(3, 1, 2),
    ]
    result = _filter_by_item_id(interactions, 777)
    assert len(result) == 0
    assert result == []


# 6. Большое количество записей (boundary: много совпадений)
def test_filter_handles_large_number_of_matching_items() -> None:
    interactions = [
        _make_log(i, learner_id=(i % 5) + 1, item_id=42) for i in range(1, 101)
    ] + [
        _make_log(101, 1, 7),  # другой item
        _make_log(102, 2, 999),
    ]
    result = _filter_by_item_id(interactions, 42)
    assert len(result) == 100
    assert all(log.item_id == 42 for log in result)


# 7. item_id = 0 (граничное значение, часто не ожидается, но должно корректно обрабатываться)
def test_filter_by_zero_item_id() -> None:
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 0),
        _make_log(3, 1, 1),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 2
    assert {log.id for log in result} == {1, 2}


# # 8. Пустой список на входе + item_id задан → всё ещё пустой список
# def test_filter_empty_list_with_item_id_returns_empty() -> None:
#     result = _filter_by_item_id([], item_id=5)
#     assert result == []
>>>>>>> Stashed changes
>>>>>>> Stashed changes
