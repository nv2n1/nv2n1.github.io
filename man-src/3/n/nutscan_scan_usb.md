---
title: "nutscan_scan_usb(3)"
name: "nutscan_scan_usb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_scan_usb/"
description: "nutscan_scan_usb – Scan NUT compatible USB devices."
---

<p>nutscan_scan_usb &#8211; Scan NUT compatible USB devices.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_scan_usb();</pre>
<h2>Description</h2>
<p>The <code>nutscan_scan_usb()</code> function try to detect NUT compatible USB devices. </p>
<p> You MUST call <code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3) before using this function.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_scan_usb()</code> function returns a pointer to a nutscan_device_t structure containing all found devices or NULL if an error occurs or no device is found.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_eaton_serial/">nutscan_scan_eaton_serial</a></code>(3) </p>
