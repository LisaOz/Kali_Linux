def display_header():
    print("=" * 50)
    print("SECURITY TARGET INFORMATION TOOL")
    print("=" * 50)

def collect_target():
    target_name = input("Enter target name: ")
    target_ip = input("Enter target IP address: ")
    target_port = input("Enter target port: ")

    target = {
        "name": target_name,
        "ip_address": target_ip,
        "port": target_port
    }
    return target

def analyse_port(port):
    if port == 21:
        return "FTP"

    if port == 22:
        return "SSH"
    
    if port == 23:
        return "Telnet"
    
    if port == 25:
        return "SMTP"

    if port == 53:
        return "DNS"

    elif port == 90:
        return "HTTP"

    elif port == 443:
        return "HTTPS"

    else:
        return "Unknown"

def security_assessment(port):
    if port == 23:
        print("HIGH RISK - Telnet")
    elif port == 21:
        print("MEDIUM RISK - FTP")
    elif port == 80:
        print("REVIEW SECURITY - HTTP")
    elif port == 443:
        print("ENCRYPTED WEB SERVICE - HTTPS")
    elif port == 22:
        print("REMOTE ADMINISTRATION - SSH")
    else:
        print("UNKNOWN SERVICE")


def display_results(target, service):
    
    print("\nSecurity Target Summary")
    print("-" * 30)
    print(f"Target: {target['name']}")
    print(f"IP Address: {target['ip_address']}")
    print(f"Port: {target['port']}")
    print(f"Detected Service: {service}")
    print("-" * 30)
    print("Target information collected successfully.")

display_header()

target = collect_target()

service = analyse_port(target['port'])

display_results(target, service)

security_assessment(['port'])

