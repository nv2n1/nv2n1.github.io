---
title: "nutscan(3)"
name: "nutscan"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan/"
description: "nutscan – Network UPS Tools (NUT) device discovery library"
---

<p>nutscan &#8211; Network UPS Tools (NUT) device discovery library</p>
<h2>Description</h2>
<p>The Network UPS Tools (NUT) <code>nutscan</code> library provides the same discovery related features that are also offered by <code><a href="/docs/linux/man/8-nut-scanner/">nut-scanner</a></code>(8). </p>
<p> It enables the discovery of supported NUT devices (USB, SNMP, Eaton XML/HTTP and IPMI) and NUT servers (using Avahi, or the classic connection method).</p>
<h2>Discovery Functions</h2>
<p>First, include the required header file: </p>
<dl>
<dd>
<pre>#include &lt;nut-scan.h&gt;</pre>
</dl>
<p> Then, to discover new devices, use the appropriate function: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3) for supported USB devices,</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3) for supported SNMP agents,</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3) for Eaton Network Management Card,</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3) for NUT servers (upsd), using the classic method,</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3) for NUT servers (upsd), using the mDNS (Avahi) method,</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3) for supported IPMI PSU.</dl>
<p> All of these functions return a list of devices found, using the nutscan_device_t structure. This structure is described in <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3). </p>
<p> Helper functions are also provided to output data using standard formats: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3) for parsable output,</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3) for ups.conf style.</dl>
<h2>Error Handling</h2>
<p>There is currently no specific mechanism for error handling.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nut-scanner/">nut-scanner</a></code>(8), <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_cidr_to_ip/">nutscan_cidr_to_ip</a></code>(3), <a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a> </p>
