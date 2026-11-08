---
title: "Querying Maximum Temperature Across Linux Server Sensors"
date: 2018-03-24 11:53:32 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-the-highest-temperature-from-all-sensors-in-a-server-on-linux/
---

Monitoring server temperatures is essential for preventing hardware damage and maintaining system stability. Linux provides several tools to query thermal sensors and identify which components are running hot.

## Using lm-sensors

The most reliable approach is `lm-sensors`, a userspace tool that reads temperature data from kernel drivers:

``` bash
# Install lm-sensors
sudo apt install lm-sensors    # Debian/Ubuntu
sudo dnf install lm-sensors    # Fedora/RHEL

# Initialize and detect sensors
sudo sensors-detect

# List all sensor readings
sensors
```

The `sensors` command displays raw output from all detected thermal zones and their current temperatures.

## Extracting the Highest Temperature

To get just the maximum temperature across all sensors:

``` bash
sensors | grep -oE '[0-9]+\.[0-9]+°C' | sed 's/°C//' | sort -rn | head -1
```

This pipeline extracts temperature values, removes the degree symbol, sorts numerically in descending order, and returns the highest value.

For a more robust approach using `awk`:

``` bash
sensors | awk '/Core|Package|Temp/ {gsub(/[^0-9.]/,"",$NF); print $NF}' | sort -rn | head -1
```

## Using the sysfs Interface

Temperatures are also exposed directly in sysfs without requiring additional tools:

``` bash
# List all thermal zones
ls /sys/class/thermal/

# Read specific zone temperature (in millidegrees Celsius)
cat /sys/class/thermal/thermal_zone0/temp

# Get highest temperature from all zones
for zone in /sys/class/thermal/thermal_zone*/temp; do
  echo "scale=1; $(cat $zone) / 1000" | bc
done | sort -rn | head -1
```

## Checking hwmon Interface

Many modern sensors report through hwmon:

``` bash
# Find all hwmon devices
find /sys/class/hwmon -name "temp*_input" | while read f; do
  echo "$(basename $f): $(cat $f)"
done
```

Divide by 1000 to convert millidegrees to Celsius.

## Real-time Monitoring with acpi

For quick checks without installing extra packages:

``` bash
# View thermal zone information
cat /proc/acpi/thermal_cooling/THM0/temperature

# Or use acpi tool if available
acpi -t
```

## Creating a Monitoring Script

Combine these approaches into a practical script:

``` bash
#!/bin/bash

# Get max temperature from lm-sensors
get_max_temp() {
  if command -v sensors &>/dev/null; then
    sensors | grep -oE '[0-9]+\.[0-9]+°C' | sed 's/°C//' | sort -rn | head -1
  else
    # Fallback to sysfs
    for zone in /sys/class/thermal/thermal_zone*/temp; do
      echo "scale=1; $(cat $zone) / 1000" | bc
    done | sort -rn | head -1
  fi
}

max_temp=$(get_max_temp)
echo "Maximum temperature: ${max_temp}°C"

# Optional: Alert if exceeds threshold
threshold=85
if (( $(echo "$max_temp > $threshold" | bc -l) )); then
  echo "WARNING: Temperature above ${threshold}°C" >&2
  exit 1
fi
```

## Integration with Monitoring Systems

For continuous monitoring in production environments:

- **Prometheus**: Use textfile collectors to expose temperature metrics from a cron job
- **Telegraf**: Built-in `inputs.exec` plugin can run temperature scripts
- **systemd timer**: Replace cron with a systemd timer for better integration

Example Prometheus exporter script:

``` bash
#!/bin/bash
max_temp=$(sensors | grep -oE '[0-9]+\.[0-9]+°C' | sed 's/°C//' | sort -rn | head -1)
echo "node_thermal_max_celsius $max_temp"
```

## Important Considerations

- **Permissions**: Reading sysfs directly may require root; configure sudo rules if scripting
- **Sensor accuracy**: Not all sensors are equally reliable; cross-reference multiple readings
- **Thresholds**: Check your hardware documentation for safe operating temperatures (typically 80-95°C for CPUs)
- **Cooling verification**: High sustained temperatures indicate cooling issues; check for dust, thermal paste degradation, or fan failures

Always validate temperature readings match your system’s actual load and ambient conditions.
