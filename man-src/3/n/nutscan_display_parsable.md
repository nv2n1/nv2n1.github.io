---
title: "nutscan_display_parsable(3)"
name: "nutscan_display_parsable"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_display_parsable/"
description: "nutscan_display_parsable – Display the specified `nutscan_device_t` structure on stdout."
---

<p>nutscan_display_parsable &#8211; Display the specified `nutscan_device_t` structure on stdout.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;
void nutscan_display_parsable(nutscan_device_t *device);</code></pre>
<h2>Description</h2>
<p>The <code>nutscan_display_parsable()</code> function displays all NUT devices in <i>device</i> to stdout. It displays them in a way that can be easily parsed which is: </p>
<p> &lt;driver type&gt;:driver=&quot;&lt;driver name&gt;&quot;,port=&quot;&lt;port type&gt;&quot;[,&lt;optional parameter 1&gt;=&quot;&lt;optional data 1&gt;&quot;,&lt;optional parameter 2&gt;=&quot;&lt;optional data 2&gt;&quot;,&#8230;] </p>
<p> &lt;driver type&gt; may be one of USB, SNMP, XML, NUT, IPMI or AVAHI. &lt;driver name&gt; is the name of the driver&#8217;s binary corresponding to this device. &lt;port type&gt; and &lt;optional parameter X&gt; depend on &lt;driver name&gt;, see the corresponding driver&#8217;s man page.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_cidr_to_ip/">nutscan_cidr_to_ip</a></code>(3) </p>
