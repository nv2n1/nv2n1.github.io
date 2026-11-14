---
title: "nutscan_scan_nut(3)"
name: "nutscan_scan_nut"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_scan_nut/"
description: "nutscan_scan_nut – Scan network for available NUT services."
---

<p>nutscan_scan_nut &#8211; Scan network for available NUT services.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_scan_nut(const char * startIP, const char * stopIP, const char * port, long usec_timeout);</pre>
<h2>Description</h2>
<p>The <code>nutscan_scan_nut()</code> function try to detect available NUT services and their associated devices. It issues a NUT request on every IP ranging from <i>startIP</i> to <i>stopIP</i>. <i>startIP</i> is mandatory, <i>stopIP</i> is optional. Those IP may be either IPv4 or IPv6 addresses or host names. </p>
<p> You MUST call <code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3) before using this function. </p>
<p> A specific <i>port</i> number may be passed, or NULL to use the default NUT port. </p>
<p> This function waits up to <i>usec_timeout</i> microseconds before considering an IP address does not respond to NUT queries.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_scan_nut()</code> function returns a pointer to a nutscan_device_t structure containing all found devices or NULL if an error occurs or no device is found.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_eaton_serial/">nutscan_scan_eaton_serial</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_cidr_to_ip/">nutscan_cidr_to_ip</a></code>(3) </p>
