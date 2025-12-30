from mitre_integration.attack_mapping import map_actions_to_ttp


def test_map_actions_to_ttp_recon() -> None:
    ttps = map_actions_to_ttp(["osint sweep", "recon planning"])
    assert any(ttp["id"] == "T1590" for ttp in ttps)
