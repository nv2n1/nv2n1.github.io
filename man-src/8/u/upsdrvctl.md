---
title: "upsdrvctl(8)"
name: "upsdrvctl"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsdrvctl/"
description: "upsdrvctl – UPS driver controller"
---

<p>upsdrvctl &#8211; UPS driver controller</p>
<h2>Synopsis</h2>
<p><code>upsdrvctl</code> -h </p>
<p> <code>upsdrvctl</code> [<i>OPTIONS</i>] {start | stop | shutdown} [<i>ups</i>]</p>
<h2>Description</h2>
<p><code>upsdrvctl</code> provides a uniform interface for controlling your UPS drivers. You should use upsdrvctl instead of direct calls to the drivers whenever possible. </p>
<p> When used properly, upsdrvctl lets you maintain identical startup scripts across multiple systems with different UPS configurations.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display the help text.</dl>
<p> <code>-r</code> <i>directory</i></p>
<dl>
<dd>If starting a driver, this value will direct it to <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) into <i>directory</i>. This can be useful when securing systems.</dl>
<p> This may be set in the ups.conf with &quot;chroot&quot; in the global section. </p>
<p> <code>-t</code></p>
<dl>
<dd>Enable testing mode. This also enables debug mode. Testing mode makes upsdrvctl display the actions it would execute without actually doing them. Use this to test out your configuration without actually doing anything to your UPS drivers. This may be helpful when defining the <i>sdorder</i> directive in your <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</dl>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dd>If starting a driver, this value will direct it to <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2) to the user id associated with <i>username</i>.</dl>
<p> If the driver is started as root without specifying this value, it will use the username that was compiled into the binary. This defaults to &quot;nobody&quot;, and is far from ideal. </p>
<p> This may be set in ups.conf with &quot;user&quot; in the global section. </p>
<p> <code>-D</code></p>
<dl>
<dd>Raise the debug level. Use this multiple times for additional details.</dl>
<h2>Commands</h2>
<p>upsdrvctl supports three commands &#8211; start, stop and shutdown. They take an optional argument which is a UPS name from <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5). Without that argument, they operate on every UPS that is currently configured. </p>
<p> <code>start</code></p>
<dl>
<dd>Start the UPS driver(s). In case of failure, further attempts may be executed by using the <i>maxretry</i> and <i>retrydelay</i> options &#8211; see <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stop the UPS driver(s).</dl>
<p> <code>shutdown</code></p>
<dl>
<dd>Command the UPS driver(s) to run their shutdown sequence. Drivers are stopped according to their sdorder value &#8211; see <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> this will probably power off your computers, so don&#8217;t play around with this option. Only use it when your systems are prepared to lose power. </p>
</dl>
<h2>Environment Variables</h2>
<p><code>NUT_CONFPATH</code> is the path name of the directory that contains upsd.conf and other configuration files. If this variable is not set, <code>upsdrvctl</code> the driver use a built-in default, which is often /usr/local/ups/etc.</p>
<h2>Diagnostics</h2>
<p>upsdrvctl will return a nonzero exit code if it encounters an error while performing the desired operation. This will also happen if a driver takes longer than the <i>maxstartdelay</i> period to enter the background.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
