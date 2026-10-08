import pytest

from embroideryai.machine_rules import ExpansionPair, MachineFamily, expand_source_tag


def test_schiffli_a5_maps_to_pf17_pair() -> None:
    assert expand_source_tag(MachineFamily.SCHIFFLI, 0xA5) == ExpansionPair(0x17, 0x18)


def test_ztc_is_an_adversarial_counterexample() -> None:
    assert expand_source_tag(MachineFamily.ZTC, 0xA5) == ExpansionPair(0x06, 0x07)


def test_a5_is_not_global_and_unknown_rules_fail_closed() -> None:
    with pytest.raises(LookupError):
        expand_source_tag(MachineFamily.SCHIFFLI, 0xA6)
