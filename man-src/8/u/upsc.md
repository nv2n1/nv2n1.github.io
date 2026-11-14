---
title: "upsc(8)"
name: "upsc"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsc/"
description: "upsc – example lightweight UPS client"
---

<p>upsc &#8211; example lightweight UPS client</p>
<h2>Synopsis</h2>
<p><code>upsc</code> -l | -L [<i>host</i>] </p>
<p> <code>upsc</code> <i>ups</i> [<i>variable</i>] </p>
<p> <code>upsc</code> -c <i>ups</i></p>
<h2>Description</h2>
<p><code>upsc</code> is provided as a quick way to poll the status of a UPS server. It can be used inside shell scripts and other programs that need UPS data but don&#8217;t want to include the full interface.</p>
<h2>Options</h2>
<p><code>-l</code> <i>host</i></p>
<dl>
<dd>List all UPS names configured at <i>host</i>, one name per line. The hostname defaults to &quot;localhost&quot;. You may optionally add a colon and a port number.</dl>
<p> <code>-L</code> <i>host</i></p>
<dl>
<dd>As above, list all UPS names configured at <i>host</i>, including their description provided by the remote <a href="/docs/linux/man/8-upsd/">upsd</a>(8) from <a href="/docs/linux/man/5-ups-conf/">ups.conf</a>(5). The hostname defaults to &quot;localhost&quot;. You may optionally add a colon and a port number to override the default port.</dl>
<p> <code>-c</code> <i>ups</i></p>
<dl>
<dd>Lists each client connected on <i>ups</i>, one name per line.</dl>
<p> <i>ups</i></p>
<dl>
<dd>Display the status of that UPS. The format for this option is <i>upsname[@hostname[:port]]</i>. The default hostname is &quot;localhost&quot;.</dl>
<p> <i>variable</i></p>
<dl>
<dd>Display the value of this variable only. By default, upsc retrieves the list of variables from the server and then displays the value for each. This may be useful in shell scripts to save an additional pipe into grep.</dl>
<h2>Examples</h2>
<p>To list all variables on an UPS named &quot;myups&quot; on a host called &quot;mybox&quot;, with <a href="/docs/linux/man/8-upsd/">upsd</a>(8) running on port 1234: </p>
<dl>
<dd>
<pre>$ upsc myups [at] mybox:1234
battery.charge: 100.0
battery.voltage: 13.9
battery.voltage.nominal: 13.6
. . .</pre>
</dl>
<p> To list the UPSes configured on this system, along with their descriptions: </p>
<dl>
<dd>
<pre>$ upsc -L
apc: Back-UPS 500
ppro2: Patriot Pro II</pre>
</dl>
<p> To retrieve the status for all UPSes connected to mybox, using Bourne-shell syntax: </p>
<dl>
<dd>
<pre>$ for UPS in `upsc -l mybox:1234`; do
 upsc $UPS ups.status
done</pre>
</dl>
<p> To list clients connected on &quot;myups&quot;: </p>
<dl>
<dd>
<pre>$ upsc -c myups
127.0.0.1
::1
192.168.1.2</pre>
</dl>
<h2>Scripted Mode</h2>
<p>If you run this program inside a shell script or similar to get the list of devices and variables, you should only consider using output from stdout, not stderr.</p>
<h2>Diagnostics</h2>
<p>upsc will either print a list of UPS names, a list of all supported variables and their values on the UPS, or an error message. If you receive an error, make sure you have specified a valid UPS on the command line, that <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) is really running on the other host and that no firewalls are blocking you.</p>
<h2>History</h2>
<p>Earlier versions of this program used the <i>upsfetch</i> library and UDP sockets to talk to upsd. This version of upsc uses the new <i>upsclient</i> library, which only talks TCP. This is why <i>upsct</i> no longer exists.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
