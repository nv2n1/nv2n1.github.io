---
title: "nutscan_add_device_to_device(3)"
name: "nutscan_add_device_to_device"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_add_device_to_device/"
description: "nutscan_add_device_to_device – Concatenate two devices structure."
---

<p>nutscan_add_device_to_device &#8211; Concatenate two devices structure.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_add_device_to_device(nutscan_device_t * first, nutscan_device_t * second);</pre>
<h2>Description</h2>
<p>The nutscan_device_t contains the following variables: </p>
<dl>
<dd>
<pre>nutscan_device_type_t type;
char * driver;
char * port;
nutscan_options_t opt;
struct nutscan_device * prev;
struct nutscan_device * next;</pre>
</dl>
<p> This is a double linked list of device. Each device is described by its type, its driver name, its port and any number of optional data. </p>
<p> The <code>nutscan_add_device_to_device()</code> concatenates <i>first</i> and <i>second</i> devices to a unique device. No new device is created, the two linked list are simply linked to each other. So <i>first</i> and <i>second</i> devices are likely to be modified by this function.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_add_device_to_device()</code> functions returns a pointer to a device containg both passed devices. Note that it&#8217;s not a new device, so it is either <i>first</i> or <i>second</i> which is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3) </p>
