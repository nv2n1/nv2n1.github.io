---
title: "ups-conf(5)"
name: "ups-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-ups-conf/"
description: "ups.conf – UPS definitions for Network UPS Tools"
---

<p>ups.conf &#8211; UPS definitions for Network UPS Tools</p>
<h2>Description</h2>
<p>This file is read by the driver controller <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8), the UPS drivers that use the common core (see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), and <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8)). The file begins with global directives, and then each UPS has a section which contains a number of directives that set parameters for that UPS. A UPS section begins with the name of the UPS in brackets, and continues until the next UPS name in brackets or until EOF. The name &quot;default&quot; is used internally in upsd, so you can&#8217;t use it in this file. You must define the <i>driver</i> and <i>port</i> elements for each entry. Anything after that in a section is optional. A simple example might look like this: </p>
<pre><code>[myups]
driver = blazer_ser
port = /dev/ttyS0
desc = &quot;Web server UPS&quot;</code></pre>
<p> A slightly more complicated version includes some extras for the hardware-specific part of the driver: </p>
<pre><code>[bigups]
driver = apcsmart
port = /dev/cua00
cable = 940-0095B
sdtype = 2
desc = &quot;Database server UPS&quot;</code></pre>
<p> In this case, the <code><a href="/docs/linux/man/8-apcsmart/">apcsmart</a></code>(8) driver will receive variables called &quot;cable&quot; and &quot;sdtype&quot; which have special meanings. See the man pages of your driver(s) to learn which variables are supported and what they do.</p>
<h2>Global Directives</h2>
<p><code>chroot</code></p>
<dl>
<dd>Optional. The driver will <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to this directory during initialization. This can be useful when securing systems.</dl>
<p> <code>driverpath</code></p>
<dl>
<dd>Optional. Path name of the directory in which the UPS driver executables reside. If you don&#8217;t specify this, the programs look in a built-in default directory, which is often /usr/local/ups/bin.</dl>
<p> <code>maxstartdelay</code></p>
<dl>
<dd>Optional. Same as the UPS field of the same name, but this is the default for UPSes that don&#8217;t have the field.</dl>
<p> <code>maxretry</code></p>
<dl>
<dd>Optional. Specify the number of attempts to start the driver(s), in case of failure, before giving up. A delay of <i>retrydelay</i> is inserted between each attempt. Caution should be taken when using this option, since it can impact the time taken by your system to start. </p>
<p> The default is 1 attempt.</dl>
<p> <code>retrydelay</code></p>
<dl>
<dd>Optional. Specify the delay between each restart attempt of the driver(s), as specified by <i>maxretry</i>. Caution should be taken when using this option, since it can impact the time taken by your system to start. </p>
<p> The default is 5 seconds.</dl>
<p> <code>pollinterval</code></p>
<dl>
<dd>Optional. The status of the UPS will be refreshed after a maximum delay which is controlled by this setting. This is normally 2 seconds. This may be useful if the driver is creating too much of a load on your system or network.</dl>
<p> <code>user</code></p>
<dl>
<dd>Optional. If started as root, the driver will <a href="/docs/linux/man/2-setuid/">setuid</a>(2) to the user id associated with <i>username</i>.</dl>
<h2>Ups Fields</h2>
<p><code>driver</code></p>
<dl>
<dd>Required. This specifies which program will be monitoring this UPS. You need to specify the one that is compatible with your hardware. See <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8) for more information on drivers in general and pointers to the man pages of specific drivers.</dl>
<p> <code>port</code></p>
<dl>
<dd>Required. This is the serial port where the UPS is connected. On a Linux system, the first serial port usually is <i>/dev/ttyS0</i>. On FreeBSD and similar systems, it probably will be <i>/dev/cuaa0</i>.</dl>
<p> <code>sdorder</code></p>
<dl>
<dd>Optional. When you have multiple UPSes on your system, you usually need to turn them off in a certain order. upsdrvctl shuts down all the 0s, then the 1s, 2s, and so on. To exclude a UPS from the shutdown sequence, set this to -1. </p>
<p> The default value for this parameter is 0.</dl>
<p> <code>desc</code></p>
<dl>
<dd>Optional. This allows you to set a brief description that upsd will provide to clients that ask for a list of connected equipment.</dl>
<p> <code>nolock</code></p>
<dl>
<dd>Optional. When you specify this, the driver skips the port locking routines every time it starts. This may allow other processes to seize the port if you start more than one accidentally. </p>
<p> You should only use this if your system won&#8217;t work without it. </p>
<p> This may be needed on Mac OS X systems.</dl>
<p> <code>ignorelb</code></p>
<dl>
<dd>Optional. When you specify this, the driver ignores a low battery condition flag that is reported by the UPS (some devices will switch off almost immediately after setting this flag, or will report this as soons as the mains fails). Instead it will use either of the following conditions to determine when the battery is low: </p>
<dl>
<dd>
<pre>battery.charge &lt; battery.charge.low
battery.runtime &lt; battery.runtime.low</pre>
</dl>
<p> The idea is to set the battery.charge.low and/or battery.runtime.low levels in <code>ups.conf</code> to a value that gives enough time to cleanly shutdown your system: </p>
<dl>
<dd>
<pre>override.battery.charge.low = 30
override.battery.runtime.low = 180</pre>
</dl>
<p> In order for this to work, your UPS should be able to (reliably) report charge and/or runtime remaining on battery. Use with caution!</dl>
<p> <code>maxstartdelay</code></p>
<dl>
<dd>Optional. This can be set as a global variable above your first UPS definition and it can also be set in a UPS section. This value controls how long upsdrvctl will wait for the driver to finish starting. This keeps your system from getting stuck due to a broken driver or UPS. </p>
<p> The default is 45 seconds.</dl>
<p> <code>default.&lt;variable&gt;</code></p>
<dl>
<dd>Optional. Set a default value for &lt;variable&gt; which is used in case the UPS doesn&#8217;t provide a value, but will be overwritten if a value is available from the UPS: </p>
<dl>
<dd>
<pre>default.input.voltage.nominal = 230</pre>
</dl>
<p> The above will report the nominal input voltage to be 230, unless the UPS tells us differently.</dl>
<p> <code>override.&lt;variable&gt;</code></p>
<dl>
<dd>Optional. Set a value for &lt;value&gt; that overrides any value that may be read from the UPS. Used for overriding values from the UPS that are clearly wrong (some devices report wrong values for battery voltage for instance): </p>
<dl>
<dd>
<pre>override.battery.voltage.nominal = 12</pre>
</dl>
<p> Use with caution! This will only change the appearance of the variable to the outside world, internally in the UPS the original value is used.</dl>
<p> All other fields are passed through to the hardware-specific part of the driver. See those manuals for the list of what is allowed.</p>
<h2>Integration</h2>
<p><code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) uses this file to start and stop the drivers. </p>
<p> The drivers themselves also obtain configuration data from this file. Each driver looks up its section and uses that to configure itself. </p>
<p> <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) learns about which UPSes are installed on this system by reading this file. If this system is called &quot;doghouse&quot; and you have defined a UPS in your <code>ups.conf</code> called &quot;snoopy&quot;, then you can monitor it from <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8) or similar as &quot;snoopy [at] doghouse&quot;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8)</p>
<h3>Internet resources</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
