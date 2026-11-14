---
title: "nutscan_scan_eaton_serial(3)"
name: "nutscan_scan_eaton_serial"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_scan_eaton_serial/"
description: "nutscan_scan_eaton_serial – Scan serial ports for Eaton devices (XCP, SHUT and Q1)."
---

<p>nutscan_scan_eaton_serial &#8211; Scan serial ports for Eaton devices (XCP, SHUT and Q1).</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_scan_eaton_serial(const char* ports_list);</pre>
<h2>Description</h2>
<p>The <code>nutscan_scan_eaton_serial()</code> function tries to detect NUT devices which are compatible with Eaton&#8217;s serial device protocols (SHUT, XCP and Q1 (aka blazer)). <i>ports_list</i> is a NULL terminated array of pointers to strings containing serial device name (/dev/ttyS0, COM1, /dev/ttya&#8230;) </p>
<p> You MUST call <code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3) before using this function.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_scan_eaton_serial()</code> function returns a pointer to a nutscan_device_t structure containing all found devices or NULL if an error occurs or no device is found.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_get_serial_ports_list/">nutscan_get_serial_ports_list</a></code>(3) </p>
