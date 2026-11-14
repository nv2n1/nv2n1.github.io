---
title: "powerpanel(8)"
name: "powerpanel"
section: "8"
letter: "p"
url: "/docs/linux/man/8-powerpanel/"
description: "powerpanel – Driver for PowerPanel Plus compatible UPS equipment"
---

<p>powerpanel &#8211; Driver for PowerPanel Plus compatible UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the powerpanel driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports CyberPower BC1200, PR2200 and many other similar devices, both for the text and binary protocols. The driver will autodetect which protocol is used.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>protocol=</code>[<i>text,binary</i>]</p>
<dl>
<dd>Override the default autodetection of the protocol.</dl>
<p> <code>manufacturer=</code><i>value</i></p>
<dl>
<dd>If you don&#8217;t like the autodetected value, you can override this by setting it here.</dl>
<p> <code>model=</code><i>value</i></p>
<dl>
<dd>Like manufacturer above.</dl>
<p> <code>serial=</code><i>value</i></p>
<dl>
<dd>Like manufacturer above.</dl>
<p> <code>ondelay=</code><i>value</i></p>
<dl>
<dd>Time to wait before switching on the UPS (1 &#8211; 9999 minutes, 0=indefinite). Only available with the text protocol driver (see Support Status).</dl>
<p> <code>offdelay=</code><i>value</i></p>
<dl>
<dd>Time to wait before shutting down the UPS (6 &#8211; 600 seconds). Values below 60 seconds will be truncated to 6 seconds intervals, values above 60 seconds to 60 seconds intervals. Only available with the text protocol driver (see Support Status).</dl>
<h2>Variables</h2>
<p>Depending on the type of your UPS unit, some of the following variables may be changed with <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8). If the driver can&#8217;t read a variable from the UPS, it will not be made available. </p>
<p> <code>input.transfer.high</code></p>
<dl>
<dd>writable: high transfer voltage point in V</dl>
<p> <code>input.transfer.low</code></p>
<dl>
<dd>writable: low transfer voltage point in V</dl>
<p> <code>battery.charge.low</code></p>
<dl>
<dd>writable: remaining battery charge percentage for low battery warning</dl>
<p> <code>output.voltage.nominal</code></p>
<dl>
<dd>writable: nominal output voltage in V</dl>
<p> <code>ups.start.battery</code></p>
<dl>
<dd>writable: allow cold start from battery</dl>
<h2>Commands</h2>
<p>Depending on the type of your UPS unit, some of the following commands may be available. </p>
<dl>
<dd>&bull; test.battery.start.quick, test.battery.stop</dl>
<dl>
<dd>&bull; beeper.enable, beeper.disable, beeper.toggle</dl>
<dl>
<dd>&bull; shutdown.return, shutdown.reboot, shutdown.stayoff</dl>
<p> On many devices, these commands are unreliable, so before using them you must verify that these work as expected (see Shutdown Issues). </p>
<dl>
<dd>&bull; shutdown.stop</dl>
<h2>Support Status</h2>
<p>Vendor support is absent for this driver, so if you need some features that are currently not available, provide ample documentation on what the driver should sent to the UPS in order to make this work. If more information would be available on the binary protocol, it would probably be possible to make <i>ondelay</i> and <i>offdelay</i> configurable. So far, nobody has taken the time to investigate what we should tell the UPS to make this work, and CyberPower isn&#8217;t willing to share this with us.</p>
<h2>Shutdown Issues</h2>
<p>If the <code>shutdown.return</code> command on your UPS doesn&#8217;t seem to work, chances are that your UPS is an older model. Try a couple of different settings for <i>offdelay</i>. If no value in the range 6..600 works, your UPS likely doesn&#8217;t support this. In order to get the expected behaviour, it requires <code>shutdown.stayoff</code> (when on battery) and <code>shutdown.reboot</code> (when on mains). The driver will automatically fallback to these commands if <code>shutdown.return</code> fails, and tries to detect which one should be used when called with the <i>-k</i> option (or through <code>upsdrvctl shutdown</code>). </p>
<p> This isn&#8217;t bullet-proof, however, and you should be prepared that the power will either not be shutdown or that it doesn&#8217;t return when the power comes back. All models supported by the binary protocol and many supported through the text protocol are affected by this.</p>
<h2>Known Problems</h2>
<p>The CyberPower OP series don&#8217;t offer direct voltage, charge, frequency and temperature readings. Instead, they will return a binary value that needs conversion to the actual value. </p>
<p> The exact conversion needed is unknown at the time of this writing, hence an estimation was made based om readings from actual devices. This may (probably will) be off, possibly a lot. Unless you can tell us the exact mapping between values from the UPS and actual readings, don&#8217;t bother to complain. We&#8217;ve done the best we can based on the limited information available. Remember, a UPS isn&#8217;t a measuring instrument.</p>
<h2>Authors</h2>
<p>Arjen de Korte &lt;arjen [at] de-korte.org&gt;, Doug Reynolds &lt;mav [at] wastegate.net&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
