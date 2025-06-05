def main():
    username = input("Enter username to search: ").strip()
    if not username:
        print("No username entered. Exiting.")
        return

    print(f"Checking username '{username}' across {len(sites)} sites...\n")

    found_sites = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_site, site, url, username): site for site, url in sites.items()}

        for future in as_completed(futures):
            site = futures[future]
            try:
                site, url, found = future.result()
                if found is True:
                    print(f"[FOUND] {site}: {url}")
                    found_sites.append((site, url))
                elif found is False:
                    print(f"[NOT FOUND] {site}")
                else:
                    print(f"[ERROR] {site} - Could not check.")
            except Exception as e:
                print(f"[EXCEPTION] {site} - {e}")

    if found_sites:
        # Create HTML content inside main
        html_content = """
        <html>
        <head><title>OSINT Username Search Results</title></head>
        <body>
        """
        html_content += f"<h2>Username: {username}</h2>"
        html_content += "<h3>Found profiles:</h3><ul>"
        for site, url in found_sites:
            html_content += f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">{site}</a></li>'
        html_content += "</ul>"

        # Add Telegram channel promo
        html_content += """
        <hr>
        <p>If you found this tool useful, follow me on Telegram for more OSINT tools, cybersecurity tips, crypto, NFTs, and updates:</p>
        <p><a href="https://t.me/LaFG95s" target="_blank" rel="noopener noreferrer">👉 Join LaFG95s on Telegram</a></p>
        </body></html>
        """

        filename = f"osint_results_{username}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        filepath = os.path.abspath(filename)
        print(f"\nOpening results page: {filepath}")
        webbrowser.open(f"file://{filepath}")
    else:
        print("\nNo profiles found.")
