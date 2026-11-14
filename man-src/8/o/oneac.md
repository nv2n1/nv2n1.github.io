---
title: "oneac(8)"
name: "oneac"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oneac/"
description: "oneac – Driver for Oneac UPS equipment"
---

<p>oneac &#8211; Driver for Oneac UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the oneac driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports various Oneac UPS families: </p>
<dl>
<dd>&bull; EG (late 80s, early 90s, plug-in serial interface card)</dl>
<dl>
<dd>&bull; ON (early and mid-90s, plug-in serial interface card)</dl>
<dl>
<dd>&bull; OZ (mid-90s on, DB-25 std., interface slot)</dl>
<dl>
<dd>&bull; OB (early 2000&#8217;s on, big cabinet, DB-25 std., interface slot)</dl>
<p> If your UPS is equipped with the Basic Interface card, use the <code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8) driver.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) file: </p>
<p> <code>testtime</code>=<i>num</i></p>
<dl>
<dd>Change battery test time from the 2 minute default.</dl>
<p> <code>offdelay</code>=<i>num</i></p>
<dl>
<dd>Change shutdown delay time from 0 second default.</dl>
<h2>Instant Commands</h2>
<p>This driver supports the following Instant Commands. (See <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8))</p>
<h3>All UPS units</h3>
<p><code>shutdown.return</code></p>
<dl>
<dd>Turn off the load possibly after a delay and return when power is back.</dl>
<p> <code>shutdown.stop</code></p>
<dl>
<dd>Stop a shutdown in progress.</dl>
<p> <code>shutdown.reboot</code></p>
<dl>
<dd>Shut down the load briefly while rebooting the UPS.</dl>
<p> <code>test.failure.start</code></p>
<dl>
<dd>Starts a 15 second long simulation of an input power failure.</dl>
<p> <code>test.battery.start.quick</code></p>
<dl>
<dd>Start a &quot;quick&quot; battery test. The default time is 2 minutes. This time can be set in the <code>ups.conf</code> file. See <code>testime</code> above.</dl>
<p> <code>test.battery.stop</code></p>
<dl>
<dd>Stops a battery test that is in progress.</dl>
<h3>All ON UPS units</h3>
<p><code>reset.input.minmax</code></p>
<dl>
<dd>Reset the minimum and maximum input line voltage values seen since the last reset or power on.</dl>
<h3>Newer ON UPS units</h3>
<p><code>test.panel.start</code></p>
<dl>
<dd>Start testing the UPS panel.</dl>
<p> <code>test.battery.start.deep</code></p>
<dl>
<dd>Start a &quot;deep&quot; battery test. This test runs the UPS until the low battery point and then returns to the AC line.</dl>
<p> <code>reset.input.minmax</code></p>
<dl>
<dd>Reset the minimum and maximum input line voltage values seen since the last reset or power on.</dl>
<p> <code>beeper.enable</code></p>
<dl>
<dd>Enable UPS beeper/buzzer.</dl>
<p> <code>beeper.disable</code></p>
<dl>
<dd>Disable UPS beeper/buzzer.</dl>
<p> <code>beeper.mute</code></p>
<dl>
<dd>Mutes the UPS beeper/buzzer for the current alarm condition(s).</dl>
<h2>Writable Variables</h2>
<p>See <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8) to see what variables are writable for the UPS. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If your UPS supports writing battery.runtime.low, the new set value is to be entered in minutes (up to 99) but the reported value is reported in seconds (set value * 60). </p>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If your UPS supports input.transfer.low and input.transfer.high, those values are used to create an allowable output range. The UPS will do what it can to keep the output voltage value within the defined range (for example: tap change or switch to inverter). </p>
</dl>
<h2>Author</h2>
<p>Bill Elliot &lt;bill [at] wreassoc.com&gt;, Eric Lawson &lt;elawson [at] inficad.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
