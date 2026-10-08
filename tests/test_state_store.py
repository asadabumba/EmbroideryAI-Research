from embroideryai.state_store import StateSetting, order_state_settings


def test_orders_by_position_then_id() -> None:
    settings = [
        StateSetting(20, 1, 9, 0),
        StateSetting(10, 2, 8, 1),
        StateSetting(10, 1, 7, 2),
    ]
    assert [(x.needle_position, x.state_id) for x in order_state_settings(settings)] == [
        (10, 1),
        (10, 2),
        (20, 1),
    ]


def test_equivalent_keys_are_newest_first_and_value_is_not_a_key() -> None:
    settings = [
        StateSetting(10, 3, 0x10, 4),
        StateSetting(10, 3, 0xFE, 9),
        StateSetting(10, 3, 0x01, 7),
    ]
    assert [x.sequence for x in order_state_settings(settings)] == [9, 7, 4]
