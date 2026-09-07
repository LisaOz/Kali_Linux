common_ports = {

    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTS"
}

def display_header():
    print("=" * 60)
    print ("MULTY-PORT SECURITY ANALYSIS TOOL")
    print ("=" * 60)


def analyse_port(port):
    return common_ports.get(port, "Unknown")


def security_assessment(port):
    if port == 23:
        return "HIGH RISK - telnet transmits data without encryption"

    elif port == 21:
        return "MEDIUM RISK - FTP mat transmit credential without encryption"

    elif port == 80:
        return "REVIEW SECURITY - HTTP is unencrypted"
        
    elif port == 443:
        return "GOOD - HTTPS suppports encrypted communication"
    
    elif port == 22:
        return "REMOTE ADMINISTRATION - Secure configuration required"
    
    else:
        return "STANDARD SERVICE - Review configuration"
        
 
high_risk_count = 0
medium_risk_count =  0
review_required = 0

display_header()


for port in common_ports:
    service = analyse_port(port)
    assessment = security_assessment(port)

    print(f"\nPort: {port}")
    print(f"Service: {service}")
    print(f"Assessment: {assessment}")

    if port == 23:
        high_risk_count += 1
    elif port == 21:
        medium_risk_count += 1
    elif port == 80:
        review_required += 1

print("\n" + "=" * 60)
print("SECURITY SUMMARY")
print("=" * 60)

print(f"High-risk services detected: {high_risk_count}")
print(f"Medium-risl services detected: {medium_risk_count}")
print(f"Services requiring review: {review_required}")




