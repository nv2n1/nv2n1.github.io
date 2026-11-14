---
title: "clone(8)"
name: "clone"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clone/"
description: "clone – UPS driver clone"
---

<p>clone &#8211; UPS driver clone</p>
<h2>Note</h2>
<p>This man page only documents the specific features of the clone driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Description</h2>
<p>This driver, which sits on top of another driver socket, allows users to group clients to a particular outlet of a device and deal with this output as if it was a normal UPS.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following settings: </p>
<p> <code>load.off</code>=<i>command</i></p>
<dl>
<dd>Recommended. Set the command on the &quot;real&quot; UPS driver that will be used to switch off the outlet. You need both <code>load.off</code> and <code>load.on</code> in order to power cycle the outlet. Otherwise, shutting down the clients powered by an outlet is a one way street (see IMPORTANT).</dl>
<p> <code>load.on</code>=<i>command</i></p>
<dl>
<dd>Recommended. Set the command on the &quot;real&quot; UPS driver that will be used to switch on the outlet. You need both <code>load.off</code> and <code>load.on</code> in order to power cycle the outlet. Otherwise, shutting down the clients powered by an outlet is a one way street (see IMPORTANT).</dl>
<p> <code>load.status</code>=<i>value</i></p>
<dl>
<dd>Recommended. Set the variable on the &quot;real&quot; UPS driver that will be used to indicate the outlet status (i.e. on/off). If not specified, the clone driver will attempt to keep track of the outlet status, but this is less reliable.</dl>
<p> <code>offdelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer (in seconds) before the outlet is turned off after the shutdown condition (OB LB) for this outlet is met or a command to shutdown was issued. Defaults to 120 seconds.</dl>
<p> <code>ondelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer (in seconds) for the outlet to switch on in case the power returns after the oulet has been switched off. Defaults to 30 seconds.</dl>
<p> <code>mincharge</code>=<i>value</i></p>
<dl>
<dd>Set the remaining battery level when the clone UPS switches to LB (percent).</dl>
<p> <code>minruntime</code>=<i>value</i></p>
<dl>
<dd>Set the remaining battery runtime when the clone UPS switches to LB (seconds).</dl>
<h2>Implementation</h2>
<p>The port specification in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) reference the driver socket that the &quot;real&quot; UPS driver is using. For example: </p>
<dl>
<dd>
<pre>[realups]
 driver = usbhid-ups
 port = auto</pre>
</dl>
<dl>
<dd>
<pre>[clone-outlet-1]
 driver = clone
 port = usbhid-ups-realups
 load.on = outlet.1.load.on
 load.off = outlet.1.load.off
 load.status = outlet.1.status
 [...]</pre>
</dl>
<h2>Important</h2>
<p>Unlike a real UPS, you should <code>not</code> configure a upsmon master for this driver. When a upsmon master sees the OB LB flags and tells the upsd server it is OK to initiate the shutdown sequence, the server will latch the FSD status and it will not be possible to restart the systems connected without restarting the upsd server. </p>
<p> This will be a problem if the power returns after the clone UPS initiated the shutdown sequence on it&#8217;s outlet, but returns before the real UPS begins shutting down. The solution is in the clone driver, that will insert the FSD flag if needed without the help of a upsmon master.</p>
<h2>Caveats</h2>
<p>The clone UPS will follow the status on the real UPS driver. You can only make the clone UPS shutdown earlier than the real UPS driver, not later. If the real UPS driver initiates a shutdown, the clone UPS driver will immediately follow. </p>
<p> Be aware that the commands to shutdown/restart an outlet on the real UPS drivers are not affected, so if you tell the real UPS driver to shutdown the outlet of the clone UPS driver, your clients will lose power without warning.</p>
<h2>Author</h2>
<p>Arjen de Korte &lt;adkorte-guest [at] alioth.debian.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-upscmd/">upscmd</a></code>(1), <code><a href="/docs/linux/man/1-upsrw/">upsrw</a></code>(1), <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet Resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
