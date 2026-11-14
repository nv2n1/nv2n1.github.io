---
title: "netxml-ups(8)"
name: "netxml-ups"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netxml-ups/"
description: "netxml-ups – Driver for Eaton / MGE Network Management Card / Proxy (XML/HTTP Protocol) equipment"
---

<p>netxml-ups &#8211; Driver for Eaton / MGE Network Management Card / Proxy (XML/HTTP Protocol) equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the netxml-ups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>netxml-ups support all recent Eaton / MGE models which use a Network Management Card or Proxy (MGE XML/HTTP protocol based). This applies to both Eaton (previously MGE Office Protection Systems) and to MGE UPS SYSTEMS. Supported card and proxy models are: </p>
<dl>
<dd>&bull; NMC Minislot (Ref 66102, firmware EA or newer),</dl>
<dl>
<dd>&bull; SNMP/Web Minislot card (Ref 66244)</dl>
<dl>
<dd>&bull; NMC Transverse (Ref 66074),</dl>
<dl>
<dd>&bull; NMC &amp; Modbus/JBus (Ref 66103),</dl>
<dl>
<dd>&bull; Network Management Proxy,</dl>
<dl>
<dd>&bull; ePDU Monitored (newer version).</dl>
<p> Older models, such as SNMP card (Ref 66062 and Ref 66045), use the SNMP protocol and should use the <code><a href="/docs/linux/man/8-snmp-ups/">snmp-ups</a></code>(8) driver with the &quot;mibs=mge&quot; parameter.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>timeout</code>=<i>value</i></p>
<dl>
<dd>The timeout for connecting to and reading from the UPS. Defaults to 5 seconds. Don&#8217;t change this value unless you know exactly what you&#8217;re doing.</dl>
<p> This value <code>must never</code> be higher than half the MAXAGE value specified in <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5), otherwise you run the risk that <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) declares the driver stale while it is waiting for a connection to timeout. </p>
<p> <code>subscribe</code></p>
<dl>
<dd>Connect to the NMC in subscribed mode. This allows to receive notifications and alarms more quickly, beside from the standard polling requests.</dl>
<p> <code>login</code>=<i>value</i></p>
<dl>
<dd>Set the login value for authenticated mode. This feature also needs the <code>password</code> argument, and allows value settings in the card. This feature is not used yet.</dl>
<p> <code>password</code>=<i>value</i></p>
<dl>
<dd>Set the password value, needed with the login for authenticated mode. This feature is not used yet.</dl>
<p> <code>shutdown_duration</code>=<i>value</i></p>
<dl>
<dd>Set the shutdown duration of the operating system, in seconds. This represents the amount of time needed by the system to operate a clean shutdown. Defaults to 120 seconds.</dl>
<p> <code>shutdown_timer</code>=<i>value</i></p>
<dl>
<dd>Set the shutdown timer, in seconds. After <i>value</i> seconds running on battery, the local system will receive a notification to shutdown. Defaults to &quot;none&quot; (disabled).</dl>
<h2>Implementation</h2>
<p>The hostname of the UPS is specified with the &quot;port&quot; value in <code>ups.conf</code>, i.e.: </p>
<dl>
<dd>
<pre>[mgexml]
 driver = netxml-ups
 port = <a rel="nofollow" href="http://netxml-ups.example.com:80">http://netxml-ups.example.com:80</a></pre>
</dl>
<p> Specifying the method to connect to the UPS (http, https) is mandatory. If the port is equal to the default for the method specified (80 for http, 443 for https) it may be omitted. </p>
<p> In order not to overload older NMCs by polling them too frequently, it is recommended to increase the &quot;pollinterval&quot; (see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)) and <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)) to at least 5 seconds.</p>
<h2>Known Issues</h2>
<p>Don&#8217;t connect to the UPS through a proxy. Although it would be trivial to add support for proxies, this is not recommended and don&#8217;t ask for it. Not only because it will prevent the driver to make a persistent connection to the UPS, but also it adds an additional failure mode. If the proxy goes down (for whatever reason), the driver will no longer be able to reach the UPS.</p>
<h2>Authors</h2>
<p>Arjen de Korte &lt;adkorte-guest [at] alioth.debian.org&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
