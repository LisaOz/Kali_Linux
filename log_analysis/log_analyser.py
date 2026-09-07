def display_header():
    print("=" * 60)
    print("SECURITY LOG ANALYSER")
    print("=" * 60)


def analyse_log(filename):
    failed_login_count = 0
    failed_logins_by_ip = {}

    try:
        with open(filename, "r") as log_file:

            for line in log_file:
                if "LOGIN_FAILED" in line:
                    failed_login_count += 1
                    parts = line.split("ip=")

                    if len(parts) == 2:
                        ip_address = parts[1].strip()

                        failed_logins_by_ip[ip_address] = (
                            failed_logins_by_ip.get(ip_address, 0) + 1
                        )

                        print(f"[!] Failed login from {ip_address}")
            return failed_login_count, failed_logins_by_ip

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return None


display_header()

log_filename = "auth.log"

failed_logins, failed_logins_by_ip = analyse_log(log_filename)

if failed_logins is not None:
    print("\n" + "=" * 60)
    print("SECURITY SUMMARY")
    print("=" * 60)
    print(f"Total failed logins: {failed_logins}")
    print("\nFailed logins by IP")
    for ip_address, count in failed_logins_by_ip.items():
        if count >=3:
            print(f"{ip_address}: {count} [!] SUSPICIOUS ACTIVITY")
        else:
            print(f"{ip_address}: {count}")
