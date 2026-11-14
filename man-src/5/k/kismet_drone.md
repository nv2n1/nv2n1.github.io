---
title: "kismet_drone(5)"
name: "kismet_drone"
section: "5"
letter: "k"
url: "/docs/linux/man/5-kismet_drone/"
description: "kismet_drone.conf – Wireless sniffing and monitoring drone configuration file"
---

<p><code>kismet_drone.conf </code>&#8211; Wireless sniffing and monitoring drone configuration file</p>
<h2>Description</h2>
<p>kismet_drone uses a minimalized configuration file, similar in options to the main kismet server configuration file. By default, the drone config is in /usr/local/etc/kismet.conf. A default configuration is included with Kismet but it is likely you will need to modify it to suit your hardware and preferences.</p>
<h2>Configuration File Format</h2>
<p>All entries are of the format directive = value</p>
<h2>Configuration Values</h2>
<p>&quot;include&quot; (string) Include another config file. </p>
<p> &quot;servername&quot; (string) Name of this Kismet drone server. This is purely for information in multiple server systems. </p>
<p> &quot;suiduser&quot; (string) User to switch privileges to after binding to the capture. </p>
<p> &quot;tcpport&quot; (int) Port to serve streamed packet data </p>
<p> &quot;allowedhosts&quot; (string) Comma-separated list of IPs or network/mask pairs. Masks can be expressed as dotted quads (/255.255.255.0) or as numbers (/24) </p>
<p> &quot;maxclient&quot; (int) Maximum number of simultaneously connected clients </p>
<p> &quot;source&quot; (string) Comma-separated packet source (cardtype,interface,name). Multiple source lines can be defined, refer to the enablesources config line for more details. </p>
<p> &quot;enablesources&quot; (string) Comma-separated list of source names (defined previously in the source lines) to enable. This is only needed if you wish to selectively enable multiple sources. For example:</p>
<dl>
<dd>enablesources=prism </p>
<p> enablesources=prism,cisco</dl>
<h2>Card Types And Multiple Capture Sources</h2>
<p>kismet_drone supports the same sources and options as the core Kismet server. For details on supported capture types and how to define multiple capture sources, see <a href="/docs/linux/man/5-kismet-conf/">kismet.conf</a>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kismet_drone/">kismet_drone</a></code>(1), <code><a href="/docs/linux/man/5-kismet-conf/">kismet.conf</a></code>(5), <code><a href="/docs/linux/man/5-kismet_ui-conf/">kismet_ui.conf</a></code>(5), <code><a href="/docs/linux/man/1-gpsmap/">gpsmap</a></code>(1), <code><a href="/docs/linux/man/1-kismet/">kismet</a></code>(1) </p>
