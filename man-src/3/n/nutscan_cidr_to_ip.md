---
title: "nutscan_cidr_to_ip(3)"
name: "nutscan_cidr_to_ip"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_cidr_to_ip/"
description: "nutscan_cidr_to_ip – Convert a CIDR IP to a range of IP address."
---

<p>nutscan_cidr_to_ip &#8211; Convert a CIDR IP to a range of IP address.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;
int nutscan_cidr_to_ip(const char *cidr, char **start_ip, char **stop_ip);</code></pre>
<h2>Description</h2>
<p>The <code>nutscan_cidr_to_ip()</code> function converts a range of IP address in the CIDR format given as a string in <i>cidr</i>, to two IPs in strings pointed by <i>start_ip</i> and <i>stop_ip</i> which can be used as input paramters in the scanning functions of the libnutscan API. It is the caller&#8217;s responsability to free <i>start_ip</i> and <i>stop_ip</i> strings.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_cidr_to_ip()</code> function returns 0 if an error occured (invalid <i>cidr</i> address) or 1 if successful.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3) </p>
