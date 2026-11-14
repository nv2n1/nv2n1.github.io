---
title: "nutscan_get_serial_ports_list(3)"
name: "nutscan_get_serial_ports_list"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_get_serial_ports_list/"
description: "nutscan_get_serial_ports_list – Get a port list name from a range of port."
---

<p>nutscan_get_serial_ports_list &#8211; Get a port list name from a range of port.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;
char **nutscan_get_serial_ports_list(const char *ports_range);</code></pre>
<h2>Description</h2>
<p>The <code>nutscan_get_serial_ports_list()</code> function returns a null terminated array of string generated from a port range. <i>ports_range</i> may be one of: </p>
<dl>
<dd>&bull; a single character from 0 to 9 or a to z representing a serial communication port depending on the operating system. For instance &quot;0&quot; is converted to /dev/ttyS0 and /dev/ttyUSB0 on Linux; &quot;1&quot; is converted to COM1 on Windows; &quot;c&quot; is converted to /dev/ttyc on solaris&#8230;</dl>
<dl>
<dd>&bull; a range of character in the form &quot;X-Y&quot;. For instance &quot;0-1&quot; will be converted to /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0 and /dev/ttyUSB1 on Linux; &quot;1-3&quot; will be converted to COM1, COM2 and COM3 on Windows; &quot;a-c&quot; will be converted to /dev/ttya, /dev/ttyb and /dev/ttyc on Solaris.</dl>
<dl>
<dd>&bull; a single port name (/dev/ttyS5, COM4&#8230;).</dl>
<dl>
<dd>&bull; a list of port names separated with comas : &quot;/dev/ttyS0,/dev/ttyS2,/dev/ttyS4&quot; or &quot;COM1,COM3&quot;&#8230;</dl>
<p> The returned array can be used in a call to <code>nutscan_scan_eaton_serial</code> to get the serial device on a system.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_get_serial_ports_list()</code> function returns NULL if an error occured (invalid port range) or a pointer to a nll terminated array of string on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_snmp/">nutscan_scan_snmp</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_eaton_serial/">nutscan_scan_eaton_serial</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3) </p>
