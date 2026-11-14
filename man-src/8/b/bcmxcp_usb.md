---
title: "bcmxcp_usb(8)"
name: "bcmxcp_usb"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcmxcp_usb/"
description: "bcmxcp_usb – Experimental driver for UPSes supporting the BCM/XCP protocol over USB"
---

<p>bcmxcp_usb &#8211; Experimental driver for UPSes supporting the BCM/XCP protocol over USB</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the bcmxcp_usb driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). This driver is a variant of the serial driver bcmxcp and uses the same core code.</p>
<h2>Supported Hardware</h2>
<p>This driver should recognize all BCM/XCP-compatible UPSes that are connected via USB. It has been developed and tested on Powerware PW3501 hardware. It also has been tested on PW5110 hardware.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5). </p>
<p> <code>shutdown_delay=</code><i>delay</i></p>
<dl>
<dd>The number of seconds that the UPS should wait between receiving the shutdown command and actually shutting off.</dl>
<h2>Default Values For The Extra Arguments</h2>
<p><code>shutdown_delay =</code><i>120</i></p>
<h2>Instant Commands</h2>
<p>This driver supports the following Instant Commands: </p>
<p> <code>shutdown.return</code></p>
<dl>
<dd>Turn off the load and return when power is back.</dl>
<p> <code>shutdown.stayoff</code></p>
<dl>
<dd>Turn off the load and remain off.</dl>
<p> <code>test.battery.start</code></p>
<dl>
<dd>Start a battery test.</dl>
<h2>Todo List</h2>
<p><code>Report UPS alarm status</code></p>
<dl>
<dd>BCM/XCP supports reporting a wide range of UPS alarm conditions.</dl>
<p> <code>Report UPS statistics informations</code></p>
<dl>
<dd>BCM/XCP supports reporting of UPS statistics data.</dl>
<h2>Experimental Driver</h2>
<p>This driver has been tagged experimental, even if it has been reported to be stable. Thus it is not suitable for production systems and it is not built by default. This is mainly due to the fact that it is a new driver.</p>
<h2>Installation</h2>
<p>This driver is not built by default. You can build it by using &quot;configure &#8211;with-usb=yes&quot;. Note that it will also install other USB drivers. </p>
<p> You also need to install manually the hotplug files (libhidups and libhid.usermap), generally in etc/hotplug/usb/, to address the permission settings problem. Lastly note that the libhidups file must have execution flag set (ie using chmod +x &#8230;).</p>
<h2>Implementation</h2>
<p>bcmxcp_usb only supports 1 UPS at this time. You can put the &quot;auto&quot; value for port in ups.conf, i.e.: </p>
<dl>
<dd>
<pre>[pw3105]
 driver = bcmxcp_usb
 port = auto</pre>
</dl>
<h2>Known Issues And Bugs</h2>
<h3>Got EPERM: Operation not permitted upon driver startup</h3>
<p>You have forgotten to install the hotplug files, as explained in the INSTALLATION section above. Don&#8217;t forget to restart hotplug so that it applies these changes.</p>
<h2>Author</h2>
<p>Tore Ørpetveit &lt;tore [at] orpetveit.net&gt;, Wolfgang Ocker &lt;weo [at] weo1.de&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
