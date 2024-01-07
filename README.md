# VigilantEye-Master

VigilantEye is a Python web scanning toolkit built with Flask, featuring a master and worker architecture. It enables users to perform various scans using both built-in modules and custom modules added to the `MODULES` folder.

## Worker
[https://github.com/stephanevdb/VigilantEye-Worker](https://github.com/stephanevdb/VigilantEye-Worker)

## Getting Started

### Prerequisites

- Python (3.11 or higher)
- Communication between master and worker on ports `8666` and `8667`

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the master:

```bash
python app.py
```

The web graphical user interface (Web GUI) is accessible on port `8666` of the master.

Start a worker node after running the master.

## Modules

Expand the functionality of VigilantEye by using the built-in modules or creating custom ones. Modules are self-contained scripts that perform specific tasks during scans.

### Ping

The "Ping" module checks the responsiveness of a target by sending ICMP packets and measuring the round-trip time.

### Traceroute

The "Traceroute" module traces the path that packets take from the source to the destination, providing insights into network routing.

### [Your Custom Module]

Create custom modules by adding a `.py` file to the `MODULES` folder and a matching `.txt` file specifying the required Python modules.

## License

[GPL License](LICENSE).
