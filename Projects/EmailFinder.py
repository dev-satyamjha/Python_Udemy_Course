import re

popular_domains = {
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "live.com",
    "protonmail.com"
}

def extract_emails(
        text: str,
        domain_filter: str = "all",
        unique_only: bool = True,
        case_sensitive: bool = True
    ) -> list[str]:

    email_pattern: str = (
        r'\b[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@'
        r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?'
        r'(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*'
        r'\.[A-Za-z]{2,}\b'
    )

    emails: list[str] = re.findall(email_pattern, text)

    if not case_sensitive:
        emails = [email.lower() for email in emails]

    filtered: list[str] = []

    for email in emails:
        domain = email.split("@")[-1].lower()

        if domain_filter == "only_popular":
            if domain in popular_domains:
                filtered.append(email)

        elif domain_filter == "exclude_popular":
            if domain not in popular_domains:
                filtered.append(email)

        else:  # default: "all"
            filtered.append(email)

    if unique_only:
        filtered = list(dict.fromkeys(filtered))

    return filtered


def list_emails(path: str, domain_filter: str = "all") -> None:
    with open(path, 'r') as f:
        text: str = f.read()
        emails = extract_emails(text, domain_filter=domain_filter)

        if emails:
            for email in emails:
                print(email)
        else:
            print("No emails were found..!!")


def main():
    print("--All emails--")
    list_emails('file.txt', domain_filter="all")
    list_emails('website_example.txt', domain_filter="all")
    print()

    print("--Popular emails--")
    list_emails('file.txt', domain_filter="only_popular")
    list_emails('website_example.txt', domain_filter="only_popular")
    print()

    print("--Non-Popular emails--")
    list_emails('file.txt', domain_filter="exclude_popular")
    list_emails('website_example.txt', domain_filter="exclude_popular")


if __name__ == '__main__':
    main()
