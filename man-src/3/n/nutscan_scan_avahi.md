---
title: "nutscan_scan_avahi(3)"
name: "nutscan_scan_avahi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_scan_avahi/"
description: "nutscan_scan_avahi – Scan network for NUT services via mDNS"
---

<p>nutscan_scan_avahi &#8211; Scan network for NUT services via mDNS</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_scan_avahi(long usec_timeout);</pre>
<h2>Description</h2>
<p>The <code>nutscan_scan_avahi()</code> function tries to detect the NUT service via mDNS, and its associated devices. It uses the Avahi library to do so. </p>
<p> You MUST call <code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3) before using this function. </p>
<p> This function waits up to <i>usec_timeout</i> microseconds before considering an IP address to be unresponsive.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_scan_avahi()</code> function returns a pointer to a nutscan_device_t structure containing all found devices. It returns NULL if an error occurs, or if no device is found.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_cidr_to_ip/">nutscan_cidr_to_ip</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_eaton_serial/">nutscan_scan_eaton_serial</a></code>(3), <a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a> </p>
