from scenarios import get_scenario


def test_get_scenario_default() -> None:
    scenario = get_scenario("unknown")
    assert scenario["id"] == "soci_energy_grid"
