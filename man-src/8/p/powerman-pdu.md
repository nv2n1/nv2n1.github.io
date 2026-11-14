---
title: "powerman-pdu(8)"
name: "powerman-pdu"
section: "8"
letter: "p"
url: "/docs/linux/man/8-powerman-pdu/"
description: "powerman-pdu – Driver for Powerman PDU"
---

<p>powerman-pdu &#8211; Driver for Powerman PDU</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the powerman-pdu driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports a wide range of PDUs through the Powerman project. </p>
<p> This includes various models from APC, Baytech, Cyclades, but also support IPMI and various blade management modules from HP, IBM and Sun.</p>
<h2>Extra Arguments</h2>
<p>This driver doesn&#8217;t support any optional setting.</p>
<h2>Variables</h2>
<p>This driver doesn&#8217;t (yet) support any changeable variable.</p>
<h2>Commands</h2>
<p>The following commands are available for each outlet, with X for the outlet number:</p>
<dl>
<dt><code>outlet.X.load.on</code></p>
<dd>power on the outlet.</p>
<dt><code>outlet.X.load.off</code></p>
<dd>power off the outlet.</p>
<dt><code>outlet.X.load.cycle</code></p>
<dd>cycle the outlet (power off then power on, possibly with a delay). </p>
</dl>
<h2>Implementation</h2>
<p>The hostname of the Powerman server is specified using the &quot;port&quot; value in <code>ups.conf</code>, i.e.: </p>
<pre> [pdu]
 driver = powerman-pdu
 port = host.example.com:port</pre>
<p>The port used to reach powermand is optional if the default port is used.</p>
<h2>Known Issues</h2>
<p>ups.status is still exposed, with the value &quot;WAIT&quot;. Some other values from the ups collection are also exposed.</p>
<h2>Author</h2>
<p>Arnaud Quette &lt;arnaud.quette [at] gmail.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> The PowerMan home page: <a rel="nofollow" href="http://powerman.sourceforge.net/">http://powerman.sourceforge.net/</a> </p>
