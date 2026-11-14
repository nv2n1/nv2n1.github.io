---
title: "nutscan_display_ups_conf(3)"
name: "nutscan_display_ups_conf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_display_ups_conf/"
description: "nutscan_display_ups_conf – Display the specified `nutscan_device_t` structure on stdout."
---

<p>nutscan_display_ups_conf &#8211; Display the specified `nutscan_device_t` structure on stdout.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;
void nutscan_display_ups_conf(nutscan_device_t *device);</code></pre>
<h2>Description</h2>
<p>The <code>nutscan_display_ups_conf()</code> function displays all NUT devices in <i>device</i> to stdout. It displays them in a way that it can be directly copied into the ups.conf file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_cidr_to_ip/">nutscan_cidr_to_ip</a></code>(3) </p>
