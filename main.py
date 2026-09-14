import os


from system_audit import (
    collect_system_info,
    check_security_basics
)

from port_check import check_local_ports

from file_integrity import (
    create_baseline,
    verify_baseline
)


def print_header():

    print("\n" + "=" * 60)

    print(
        "        CYBERSECURITY AUTOMATION TOOLKIT"
    )

    print("=" * 60)

    print(
        "Defensive / Educational Local Security Audit\n"
    )


def system_audit():

    info = collect_system_info()

    print("\n--- SYSTEM INFORMATION ---")

    for key, value in info.items():

        print(
            f"{key}: {value}"
        )

    print("\n--- SECURITY BASICS ---")

    for item, status in check_security_basics().items():

        print(
            f"{item}: {status}"
        )


def port_audit():

    print("\n--- LOCALHOST PORT CHECK ---")

    print(
        "Checking only common TCP ports on 127.0.0.1."
    )

    results = check_local_ports()

    for port, status in results.items():

        print(
            f"Port {port}: {status}"
        )


def integrity_menu():

    folder = input(
        "Enter a folder path to protect/verify: "
    ).strip()

    if not os.path.isdir(folder):

        print("Folder not found.")

        return

    choice = input(
        "1 = Create baseline, "
        "2 = Verify baseline: "
    ).strip()

    if choice == "1":

        count = create_baseline(folder)

        print(
            f"Baseline created. "
            f"Files hashed: {count}"
        )

    elif choice == "2":

        result = verify_baseline(folder)

        print("\nIntegrity report:")

        for k, v in result.items():

            print(
                f"{k}: {v}"
            )

    else:

        print("Invalid choice.")


def main():

    while True:

        print_header()

        print("1. System security audit")
        print("2. Localhost port check")
        print("3. File integrity monitor")
        print("4. Exit")

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":

            system_audit()

        elif choice == "2":

            port_audit()

        elif choice == "3":

            integrity_menu()

        elif choice == "4":

            print("Exiting toolkit.")

            break

        else:

            print("Invalid option.")


if __name__ == "__main__":

    main()