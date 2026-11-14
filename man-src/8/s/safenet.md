---
title: "safenet(8)"
name: "safenet"
section: "8"
letter: "s"
url: "/docs/linux/man/8-safenet/"
description: "safenet – Driver for SafeNet compatible UPS equipment"
---

<p>safenet &#8211; Driver for SafeNet compatible UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the safenet driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports UPS equipment which can be controlled via SafeNet v1.0 for Windows (serial interface only).</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) file: </p>
<p> <code>manufacturer=</code><i>value</i></p>
<dl>
<dd>Autodetection of this parameter is not possible yet (and it probably never will be). Therefore, this user-defined string accepts any name. The default is <i>unknown</i>.</dl>
<p> <code>modelname=</code><i>value</i></p>
<dl>
<dd>Like manufacturer above. The default is <i>unknown</i>.</dl>
<p> <code>serialnumber=</code><i>value</i></p>
<dl>
<dd>Like manufacturer above. The default is <i>unknown</i>.</dl>
<p> <code>ondelay=</code><i>value</i></p>
<dl>
<dd>Time to wait before switching on the UPS (minutes). Defaults to 1 minute.</dl>
<p> <code>offdelay=</code><i>value</i></p>
<dl>
<dd>Time to wait before shutting down the UPS (seconds). Defaults to 30 seconds.</dl>
<h2>Upscmd</h2>
<p>This driver supports some instant commands (see <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8)): </p>
<p> <code>test.battery.start</code></p>
<dl>
<dd>Start UPS self test</dl>
<p> <code>test.battery.stop</code></p>
<dl>
<dd>Cancel UPS self test</dl>
<p> <code>test.failure.start</code></p>
<dl>
<dd>Start simulated power failure</dl>
<p> <code>test.failure.stop</code></p>
<dl>
<dd>Cancel simulated power failure</dl>
<p> <code>beeper.enable</code></p>
<dl>
<dd>Enable the UPS beeper</dl>
<p> <code>beeper.mute</code></p>
<dl>
<dd>Temporarily mute the UPS beeper</dl>
<p> <code>beeper.toggle</code></p>
<dl>
<dd>Toggle the UPS beeper</dl>
<p> <code>shutdown.return</code></p>
<dl>
<dd>Turn off the load and wait for the power to return. Uses the timer defined by <code>offdelay</code>.</dl>
<p> <code>shutdown.reboot</code></p>
<dl>
<dd>Turn off the load and return. Uses the timers defined by <code>offdelay</code> and <code>ondelay</code>.</dl>
<h2>Known Problems</h2>
<p>If you run the <code>shutdown.return</code> command with mains present, the output may stay on or switch off and not back on again. The <code>shutdown.reboot</code> command will unconditionally switch on the load again (with or without mains present). </p>
<p> If the driver is called with the <i>-k</i> option (or through <code>upsdrvctl shutdown</code>) it tries to detect which command should be used in an attempt to stay off until mains is present again or to cycle the output if the power returned in the mean time. This isn&#8217;t bullet-proof, and you should be prepared that the power will either not be shutdown, or that it doesn&#8217;t return when the power comes back.</p>
<h2>Author</h2>
<p>Arjen de Korte &lt;adkorte-guest at alioth.debian.org&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
