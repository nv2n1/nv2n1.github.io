---
title: "nutscan_add_option_to_device(3)"
name: "nutscan_add_option_to_device"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_add_option_to_device/"
description: "nutscan_add_option_to_device – Add option data to the specified device."
---

<p>nutscan_add_option_to_device &#8211; Add option data to the specified device.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;
void nutscan_add_option_to_device(nutscan_device_t *device, char *option_name, char *value);</code></pre>
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
<p> The <code>nutscan_add_option_to_device()</code> adds an optional data in the given devcie. Optional data are made of an <i>option_name</i> and an associated <i>value</i>. Copies of <i>option_name</i> and <i>value</i> are stored in the device, so the caller can safely free both of them.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3) </p>
