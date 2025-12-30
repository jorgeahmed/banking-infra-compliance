import csv
import random
from datetime import datetime

class InfrastructureAuditor:
    def __init__(self, site_name):
        self.site_name = site_name
        self.standards = {
            'Cat6A': {'max_length': 90, 'min_headroom': 3.0}, # dB
            'Cat7A': {'max_length': 100, 'min_headroom': 5.0} # dB
        }

    def simulate_fluke_data(self, records=50):
        """Generates mock cable test results."""
        data = []
        for i in range(1, records + 1):
            cable_id = f"RACK-{random.randint(1,10)}-PORT-{i:02d}"
            cable_type = "Cat7A" if i % 2 == 0 else "Cat6A"
            length = random.uniform(20, 95) # Some will fail
            headroom = random.uniform(1.5, 12.0)
            data.append({
                'id': cable_id,
                'type': cable_type,
                'length': round(length, 1),
                'headroom': round(headroom, 1)
            })
        return data

    def audit_cable(self, record):
        std = self.standards.get(record['type'])
        issues = []
        
        if record['length'] > std['max_length']:
            issues.append(f"Length {record['length']}m > {std['max_length']}m")
        
        if record['headroom'] < std['min_headroom']:
            issues.append(f"Headroom {record['headroom']}dB < {std['min_headroom']}dB")
            
        return "PASS" if not issues else f"FAIL: {', '.join(issues)}"

    def run_audit(self):
        print(f"--- 🏦 BANKING INFRASTRUCTURE AUDIT: {self.site_name} ---")
        data = self.simulate_fluke_data()
        
        passed, failed = 0, 0
        
        for record in data:
            result = self.audit_cable(record)
            status_icon = "✅" if result == "PASS" else "❌"
            if result == "PASS":
                passed += 1
            else:
                failed += 1
                print(f"{status_icon} {record['id']} ({record['type']}) -> {result}")
        
        print("\n" + "="*30)
        print(f"TOTAL NODES: {len(data)}")
        print(f"COMPLIANT:   {passed}")
        print(f"NON-COMPLIANT: {failed}")
        print(f"COMPLIANCE RATE: {(passed/len(data))*100:.1f}%")
        
        if failed > 0:
            print("[ACTION REQUIRED] Generate punch list for cabling vendor (IemsaMX).")

if __name__ == "__main__":
    auditor = InfrastructureAuditor("Santander_Corp_HQ_Lvl4")
    auditor.run_audit()
