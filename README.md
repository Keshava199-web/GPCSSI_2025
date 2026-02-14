# GPCSSI_2025
## IP Intelligence Scanner (CLI-Based)

A scalable command-line IP intelligence and reconnaissance tool built to support OSINT investigations, threat hunting, incident response, and large-scale security assessments.

This tool automates bulk IP enrichment by collecting geolocation data, ISP details, ASN information, and infrastructure metadata, then exporting structured results for operational analysis.

---

### 🚀 Core Capabilities

- Bulk IP scanning (hundreds to thousands in a single execution)
- Automated geolocation intelligence extraction
- ISP, ASN, organization & timezone identification
- Reverse geocoding using OpenStreetMap
- Structured CSV export for reporting & investigation workflows
- Optimized for automation and large dataset processing

---

### 🛠 Tech Stack

- **Python** – Core scripting & automation
- **Requests / HTTP APIs** – IP data enrichment
- **OpenStreetMap (Nominatim API)** – Reverse geocoding
- **CSV / Pandas** – Structured data export & formatting
- **CLI-based architecture** – Lightweight & deployment-ready

---

### 🧠 Architecture Overview

1. Accepts bulk IP input (file or manual entry)
2. Processes IPs sequentially or concurrently
3. Queries external intelligence APIs
4. Normalizes and structures response data
5. Performs reverse geocoding on coordinates
6. Exports enriched results into a clean CSV file

The design prioritizes modularity, scalability, and automation for real-world investigative workflows.

---

### 📊 Performance

- Designed to process 1,000+ IP addresses per execution
- Optimized API handling and structured output processing
- Lightweight CLI design ensures minimal system resource usage
- Suitable for integration into larger SOC or automation pipelines

---

### 🎯 Practical Use Cases

- Threat hunting & IOC enrichment
- Incident response investigations
- External attack surface reconnaissance
- Infrastructure footprint analysis
- OSINT-based intelligence gathering
---

#### Key Features[summary]:
🚀 Bulk IP Scanning: Scan hundreds or thousands of IPs in one go.
🌍 Geolocation Info: Get city, region, country, latitude, longitude, and exact physical address.
🏢 Network Information: Retrieve ISP, ASN, organization name, and timezone.
📤 CSV Export: Saves results in a clean CSV file for reporting or further analysis.
🛰️ Reverse Geocoding: Converts latitude and longitude to human-readable addresses using OpenStreetMap.
