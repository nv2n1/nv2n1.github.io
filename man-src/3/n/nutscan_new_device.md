---
title: "nutscan_new_device(3)"
name: "nutscan_new_device"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_new_device/"
description: "nutscan_new_device – Create a new nutscan_device_t structure."
---

<p>nutscan_new_device &#8211; Create a new nutscan_device_t structure.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_new_device();</pre>
<h2>Description</h2>
<p>The <code>nutscan_new_device()</code> function allocates a new nutscan_device_type_t structure.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_new_device()</code> function returns the newly allocated nutscan_device_type_t structure</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3) <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3) <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3) <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3) </p>
