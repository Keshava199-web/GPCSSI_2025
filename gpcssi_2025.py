import csv
import requests
import argparse

def fetch_ipinfo_data(ip):
    """ip okka details ni ikkada nunchi thisukkanamu ipinfo.io"""
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                'IP': ip,
                'City (ipinfo)': data.get('city', ''),
                'Region (ipinfo)': data.get('region', ''),
                'Country (ipinfo)': data.get('country', ''),
                'Location (ipinfo)': data.get('loc', ''),
                'Org (ipinfo)': data.get('org', ''),
                'Timezone (ipinfo)': data.get('timezone', ''),
                'Postal (ipinfo)': data.get('postal', ''),
                'Hostname (ipinfo)': data.get('hostname', '')
            }
        else:
            return {'IP': ip, 'Error (ipinfo)': f"HTTP {response.status_code}"}
    except Exception as e:
        return {'IP': ip, 'Error (ipinfo)': str(e)}


def fetch_ipapi_data(ip):
    """idhi IP details ikkada nunchi ip-api.com"""
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                'City (ip-api)': data.get('city', ''),
                'Region (ip-api)': data.get('regionName', ''),
                'Country (ip-api)': data.get('country', ''),
                'Location (ip-api)': f"{data.get('lat', '')},{data.get('lon', '')}",
                'ISP (ip-api)': data.get('isp', ''),
                'Org (ip-api)': data.get('as', ''),
                'Timezone (ip-api)': data.get('timezone', ''),
                'Postal (ip-api)': data.get('zip', '')
            }
        else:
            return {'Error (ip-api)': f"HTTP {response.status_code}"}
    except Exception as e:
        return {'Error (ip-api)': str(e)}


def process_ips(input_csv, output_csv):
    """Read IPs from input CSV, fetch data, and write to output CSV   ee code dwara manam ip's ni read chesi oka input file .csv dhantho cretae chesi mariyu output ni same dhani format lo  save chayyabauthundhi"""
    try:
        with open(input_csv, 'r', encoding='utf-8') as infile, \
                open(output_csv, 'w', newline='', encoding='utf-8') as outfile:

            reader = csv.DictReader(infile)
            fieldnames = ['IP',
                          'City (ipinfo)', 'Region (ipinfo)', 'Country (ipinfo)', 'Location (ipinfo)',
                          'Org (ipinfo)', 'Timezone (ipinfo)', 'Postal (ipinfo)', 'Hostname (ipinfo)',
                          'City (ip-api)', 'Region (ip-api)', 'Country (ip-api)', 'Location (ip-api)',
                          'ISP (ip-api)', 'Org (ip-api)', 'Timezone (ip-api)', 'Postal (ip-api)',
                          'Error (ipinfo)', 'Error (ip-api)']

            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                ip = row.get('ip')
                if not ip:
                    continue

                print(f"[INFO] Processing {ip}...")

                ipinfo_data = fetch_ipinfo_data(ip)
                ipapi_data = fetch_ipapi_data(ip)

                combined = {**ipinfo_data, **ipapi_data}
                writer.writerow(combined)

            print(f"[SUCCESS] Data saved to {output_csv}")

    except FileNotFoundError:
        print(f"[ERROR] Input file {input_csv} not found.")
    except Exception as e:
        print(f"[ERROR] {e}")


def main():
    parser = argparse.ArgumentParser(description="IP Lookup CLI Tool")
    parser.add_argument('--input', '-i', required=True, help='Input CSV file with IPs')
    parser.add_argument('--output', '-o', required=True, help='Output CSV file for results')

    args = parser.parse_args()

    process_ips(args.input, args.output)


if __name__ == "__main__":
    main()
