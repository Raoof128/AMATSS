"""Static MITRE ATT&CK TTP catalog for simulation."""

from mitre_integration.types import TTP

DEFAULT_TTPS: dict[str, list[TTP]] = {
    "recon": [
        {"id": "T1590", "name": "Gather Victim Network Information", "tactic": "Reconnaissance"},
        {"id": "T1595", "name": "Active Scanning", "tactic": "Reconnaissance"},
    ],
    "social": [
        {"id": "T1566", "name": "Phishing", "tactic": "Initial Access"},
        {"id": "T1204", "name": "User Execution", "tactic": "Execution"},
    ],
    "exploit": [
        {"id": "T1190", "name": "Exploit Public-Facing Application", "tactic": "Initial Access"},
        {"id": "T1210", "name": "Exploitation of Remote Services", "tactic": "Lateral Movement"},
    ],
    "lateral": [
        {"id": "T1021", "name": "Remote Services", "tactic": "Lateral Movement"},
        {"id": "T1053", "name": "Scheduled Task/Job", "tactic": "Persistence"},
    ],
    "detection": [
        {"id": "T1082", "name": "System Information Discovery", "tactic": "Discovery"},
    ],
    "response": [
        {"id": "T1070", "name": "Indicator Removal", "tactic": "Defense Evasion"},
    ],
    "intel": [
        {"id": "T1587", "name": "Develop Capabilities", "tactic": "Resource Development"},
    ],
}
