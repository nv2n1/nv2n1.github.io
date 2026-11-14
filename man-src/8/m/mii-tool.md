---
title: "mii-tool(8)"
name: "mii-tool"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mii-tool/"
description: "mii-tool – view, manipulate media-independent interface status"
---

<p>mii-tool &#8211; view, manipulate media-independent interface status</p>
<h2>Synopsis</h2>
<p><code>mii-tool</code> [<code>-v</code>, <code>&#8211;verbose</code>] [<code>-V</code>, <code>&#8211;version</code>] [<code>-R</code>, <code>&#8211;reset</code>] [<code>-r</code>, <code>&#8211;restart</code>] [<code>-w</code>, <code>&#8211;watch</code>] [<code>-l</code>, <code>&#8211;log</code>] [<code>-A</code>, <code>&#8211;advertise=</code><i>media,&#8230;</i>] [<code>-F</code>, <code>&#8211;force=</code><i>media</i>] [<code>-p</code>, <code>&#8211;phy=</code><i>addr</i>] interface &#8230; </p>
<h2>Description</h2>
<p>This utility checks or sets the status of a network interface&#8217;s Media Independent Interface (MII) unit. Most fast ethernet adapters use an MII to autonegotiate link speed and duplex setting. </p>
<p> Most intelligent network devices use an autonegotiation protocol to communicate what media technologies they support, and then select the fastest mutually supported media technology. The <code>-A</code> or <code>&#8211;advertise</code> options can be used to tell the MII to only advertise a subset of its capabilities. Some passive devices, such as single-speed hubs, are unable to autonegotiate. To handle such devices, the MII protocol also allows for establishing a link by simply detecting either a 10baseT or 100baseT link beat. The <code>-F</code> or <code>&#8211;force</code> options can be used to force the MII to operate in one mode, instead of autonegotiating. The <code>-A</code> and <code>-F</code> options are mutually exclusive. </p>
<p> The default short output reports the negotiated link speed and link status for each interface.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more detailed MII status information. If used twice, also display raw MII register contents.<br />
 <code>Alert:</code> If used three times, will force reading all MII registers, including non standard ones. It&#8217;s not guaranteed any valid answer from PHY while PHY communication can even hang. With driver e1000e will fail while reading register 0x07.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display program version information.</p>
<dt><code>-R</code>, <code>&#8211;reset</code></p>
<dd>Reset the MII to its default configuration.</p>
<dt><code>-r</code>, <code>&#8211;restart</code></p>
<dd>Restart autonegotiation.</p>
<dt><code>-w</code>, <code>&#8211;watch</code></p>
<dd>Watch interface(s) and report changes in link status. The MII interfaces are polled at one second intervals.</p>
<dt><code>-l</code>, <code>&#8211;log</code></p>
<dd>Used with <code>-w</code>, records link status changes in the system log instead of printing on standard output.</p>
<dt><code>-F</code><i> media</i>, <code>&#8211;force=</code><i>media</i></p>
<dd>Disable autonegotiation, and force the MII to either <code>100baseTx-FD</code>, <code>100baseTx-HD</code>, <code>10baseT-FD</code>, or <code>10baseT-HD</code> operation.</p>
<dt><code>-A</code><i> media,&#8230;</i>, <code>&#8211;advertise=</code><i>media,&#8230;</i></p>
<dd>Enable and restart autonegotiation, and advertise only the specified media technologies. Multiple technologies should be separated by commas. Valid media are <code>100baseT4</code>, <code>100baseTx-FD</code>, <code>100baseTx-HD</code>, <code>10baseT-FD</code>, and <code>10baseT-HD</code>.</p>
<dt><code>-p</code><i> addr</i>, <code>&#8211;phy=</code><i>addr</i></p>
<dd>Override the MII address provided by kernel with value <code>addr</code>. </p>
</dl>
<h2>Diagnostics</h2>
<dl>
<dt>SIOCGMIIPHY on &#8216;eth?&#8217; failed: Invalid argument</p>
<dd>If the interface is not running (up), kernel will refuse to report its link state.</p>
<dt>SIOCGMIIPHY on &#8216;eth?&#8217; failed: Operation not permitted</p>
<dd>Most kernels restrict access to root.</p>
<dt>SIOCGMIIPHY on &#8216;eth?&#8217; failed: No such device</p>
<dd>This error is shown, if the kernel does not know about the named device.</p>
<dt>SIOCGMIIPHY on &#8216;eth?&#8217; failed: Operation not supported</p>
<dd>The interface in question does not support MII queries. Most likely, it does not have MII transceivers, at all. </p>
</dl>
<h2>Authors</h2>
<p>David Hinds &#8211; dhinds [at] pcmcia.sourceforge.org<br />
 Donald Becker &#8211; becker [at] scyld.com<br />
 Bernd Eckenfels &#8211; net-tools [at] lina.inka.de</p>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://net-tools.sourceforge.net">http://net-tools.sourceforge.net</a> &#8211; Homepage of the net-tools project </p>
