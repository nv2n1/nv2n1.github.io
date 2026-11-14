---
title: "nutscan_init(3)"
name: "nutscan_init"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_init/"
description: "nutscan_init – Initialize the nutscan library."
---

<p>nutscan_init &#8211; Initialize the nutscan library. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;nut-scan.h&gt;
</pre>
<pre>
void nutscan_init();
</pre>
<h2>Description</h2>
<p> The <code>nutscan_init()</code> function must be called at least once before using any other function of the nutscan library. </p>
<p> It updates the following global variables which can be used by nutscan library user to know which scan methods are available at run-time. This depends on the libraries installed on the system: </p>
<dl COMPACT>
<dt>
<dd>
<pre>
nutscan_avail_avahi = 1 : AVAHI scan is available
nutscan_avail_ipmi = 1 : IPMI scan is available
nutscan_avail_nut = 1 : Old NUT method is available
nutscan_avail_snmp = 1 : SNMP method is available
nutscan_avail_usb = 1 : USB method is available
nutscan_avail_xml_http = 1 : XML HTTP method is available
</pre>
</dl>
<p> Note that if a method is reported as unavailable by those variables, the call to the corresponding nutscan_scan_* function will always return NULL.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3)</p>
