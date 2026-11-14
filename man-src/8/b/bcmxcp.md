---
title: "bcmxcp(8)"
name: "bcmxcp"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcmxcp/"
description: "bcmxcp – Driver for UPSes supporting the serial BCM/XCP protocol"
---

<p>bcmxcp &#8211; Driver for UPSes supporting the serial BCM/XCP protocol</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the bcmxcp driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver should recognize all serial BCM/XCP-compatible UPSes. It has been developed and tested on Powerware PW5115 and PW9120 hardware. If your UPS has a USB connection, you may also consult the <code><a href="/docs/linux/man/8-bcmxcp_usb/">bcmxcp_usb</a></code>(8) driver documentation.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5). </p>
<p> <code>shutdown_delay=</code><i>delay</i></p>
<dl>
<dd>The number of seconds that the UPS should wait between receiving the shutdown command (upsdrvctl shutdown) and actually shutting off.</dl>
<p> <code>baud_rate=</code><i>rate</i></p>
<dl>
<dd>Communication speed for the UPS. If this is set to 9600, it tries to connect to the UPS at 9600bps. If it fails to communicate, it will go into baud-hunting. It starts at 1200 and goes up to 19200. If it succeeds, it tell you the speed it connected with. If not included in the config, it defaults to baud-hunting.</dl>
<h2>Default Values For The Extra Arguments</h2>
<dl>
<dd>&bull; </p>
<p> <code>shutdown_delay =</code> <i>120</i></dl>
<dl>
<dd>&bull; </p>
<p> <code>baud_rate =</code> <i>none</i></dl>
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
<p> <code>outlet.n.shutdown.return</code></p>
<dl>
<dd>Turn off the load on outlet <i>n</i> and return when power is back. (<i>n</i> is the outlet number reported by the upsc command)</dl>
<h2>Todo List</h2>
<p>Report UPS statistics information</p>
<dl>
<dd>BCM/XCP supports reporting of UPS statistics data.</dl>
<p> Change settings</p>
<dl>
<dd>Access the config register to change settings.</dl>
<h2>Bugs</h2>
<p>None known.</p>
<h2>Author</h2>
<p>Tore Ørpetveit &lt;tore [at] orpetveit.net&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>The USB BCM/XCP driver:</h3>
<p><code><a href="/docs/linux/man/8-bcmxcp_usb/">bcmxcp_usb</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
