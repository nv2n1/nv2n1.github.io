---
title: "blazer(8)"
name: "blazer"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blazer/"
description: "blazer_ser, blazer_usb – Driver for Megatec/Q1 protocol serial/USB based UPS equipment"
---

<p>blazer_ser, blazer_usb &#8211; Driver for Megatec/Q1 protocol serial/USB based UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the blazer driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The blazer driver is known to work with various UPSes from Blazer, Energy Sistem, Fenton Technologies, Mustek and many others. The NUT compatibility table lists all the known supported models. Keep in mind, however, that other models not listed there may also be supported, but haven&#8217;t been tested. </p>
<p> All devices with a serial interface (use the <code>blazer_ser</code> driver) and many with a USB interface (use the <code>blazer_usb</code> driver) are supported.</p>
<h2>Extra Arguments</h2>
<p>You may need to override or provide defaults for some values, depending on the make and model of your UPS. The following are the ones that most likely will need changing (see <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)): </p>
<dl>
<dt>default.battery.voltage.high = <i>value</i></p>
<dd>Maximum battery voltage that is reached after about 12 to 24 hours charging. If you want the driver to report a guesstimated <code>battery.charge</code>, you need to specify this (see <code>BATTERY CHARGE</code>). </p>
<dt>default.battery.voltage.low = <i>value</i></p>
<dd>Minimum battery voltage just before the UPS automatically shuts down. If you want the driver to report a guesstimated <code>battery.charge</code>, you need to specify this (see <code>BATTERY CHARGE</code>). </p>
<dt>default.battery.voltage.nominal = <i>value</i></p>
<dd>
<dt>override.battery.voltage.nominal = <i>value</i></p>
<dd>Some devices show a wrong nominal battery voltage (or none at all), so you may need to override or set a default value. </p>
<dt>override.battery.packs = <i>value</i></p>
<dd>Some devices report a part of the total battery voltage. For instance, if <code>battery.voltage.nominal</code> is 24 V, but it reports a <code>battery.voltage</code> of around 2 V, the number of <code>battery.packs</code> to correct this reading would be 12. The driver will attempt to detect this automatically, but if this fails somehow, you may want to override this value. </p>
<dt>ondelay = <i>value</i></p>
<dd>Time to wait before switching on the UPS (minutes). Note that a value below 3 minutes, may cause earlier firmware versions to not switch on automatically, so it defaults to 3 minutes. </p>
<dt>offdelay = <i>value</i></p>
<dd>Time to wait before shutting down the UPS (seconds). This value is truncated to units of 6 seconds (less than 60 seconds) or 60 seconds (more than 60 seconds). Defaults to 30 seconds. </p>
<dt>norating</p>
<dd>Some UPSes will lock up if you attempt to read rating information from them. Setting this flag will make the driver skip this step. </p>
<dt>novendor</p>
<dd>Some UPSes will lock up if you attempt to read vendor information from them. Setting this flag will make the driver skip this step. </p>
<dt>runtimecal = <i>value,value,value,value</i></p>
<dd>Parameter used in the (optional) runtime estimation. This takes two runtimes at different loads. Typically, this uses the runtime at full load and the runtime at half load. For instance, if your UPS has a rated runtime of 240 seconds at full load and 720 seconds at half load, you would enter </p>
<p>&nbsp;<wbr><code>runtimecal&nbsp;<wbr>=&nbsp;<wbr>270,100,720,50</code> </p>
<p> The first load should always be higher than the second. If you have values available for loads other than 100 and 50 % respectively, you can use those too, but keep them spaced apart as far as reasonably possible. Just don&#8217;t get too close to no load (prediction of runtime depends more on idle load for the battery then). </p>
<dt>chargetime = <i>value</i></p>
<dd>The time needed to fully recharge the battery after being fully discharged. If not specified, the driver defaults to 43200 seconds (12 hours). Only used if <code>runtimecal</code> is also specified. </p>
<dt>idleload= <i>value</i></p>
<dd>Minimum battery load used by the driver to estimate the runtime. If not specified, the driver defaults to 10 %. Only used if <code>runtimecal</code> is also specified. </p>
</dl>
<h2>Serial Interface Only</h2>
<dl>
<dt>cablepower = <i>string</i></p>
<dd>By default the driver will set DTR and clear RTS (<i>normal</i>). If you find that your UPS isn&#8217;t detected or the communication with the UPS is unreliable, you may try if clear DTR and set RTS (<i>reverse</i>), set DTR and RTS (<i>both</i>) or clear DTR and RTS (<i>none</i>) improves this situation. </p>
</dl>
<h2>Usb Interface Only</h2>
<dl>
<dt>vendorid = <i>regex</i></p>
<dd>
<dt>productid = <i>regex</i></p>
<dd>
<dt>vendor = <i>regex</i></p>
<dd>
<dt>product = <i>regex</i></p>
<dd>
<dt>serial = <i>regex</i></p>
<dd>Select a specific UPS, in case there is more than one connected via USB. Each option specifies an extended regular expression (see <code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code>) that must match the UPS&#8217;s entire vendor/product/serial string (minus any surrounding whitespace), or the whole 4-digit hexadecimal code for vendorid and productid. Try <code>-DD</code> for finding out the strings to match. </p>
<p> Examples: </p>
<p>&nbsp;<wbr><code>-x vendor=&quot;Foo.Corporation.*&quot;</code> </p>
<p>&nbsp;<wbr><code>-x vendorid=051d</code>&nbsp;<wbr>(APC) </p>
<p>&nbsp;<wbr><code>-x product=&quot;.*(Smart|Back)-?UPS.*&quot;</code> </p>
<dt>bus = <i>regex</i></p>
<dd>Select a UPS on a specific USB bus or group of busses. The argument is a regular expression that must match the bus name where the UPS is connected (e.g. bus=&quot;002&quot;, bus=&quot;00[2-3]&quot;). </p>
<dt>subdriver = <i>string</i></p>
<dd>Select a serial-over-USB subdriver to use. You have a choice between <i>phoenix</i> <i>ippon</i>, <i>cypress</i> and <i>krauler</i>. When using this option, it is mandatory to also specify the vendorid and productid. Note that since nut-2.4.2 the <i>ippon</i> subdriver is used where previously the <i>phoenix</i> was selected. If this doesn&#8217;t work for you, add the following to the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) entry for your UPS: </p>
<pre> vendorid = 06da
 productid = 0003
 subdriver = phoenix</pre>
</dl>
<h2>Ups Commands</h2>
<p>This driver supports some instant commands (see <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8)): </p>
<dl>
<dt>beeper.toggle</p>
<dd>Toggle the UPS beeper. (Not available on some hardware.) </p>
<dt>load.on</p>
<dd>Turn on the load immediately. </p>
<dt>load.off</p>
<dd>Turn off the load immediately (see <code>KNOWN PROBLEMS</code>). </p>
<dt>shutdown.return [<i>value</i>]</p>
<dd>Turn off the load and return when power is back. Uses the timers defined by <code>ondelay</code> and <code>offdelay</code>. </p>
<dt>shutdown.stayoff [<i>value</i>]</p>
<dd>Turn off the load and remain off (see <code>KNOWN PROBLEMS</code>). Uses the timer defined by <code>offdelay</code>. </p>
<dt>shutdown.stop</p>
<dd>Stop a shutdown in progress. </p>
<dt>test.battery.start.deep</p>
<dd>Perform a long battery test (Not available on some hardware.) </p>
<dt>test.battery.start.quick</p>
<dd>Perform a (10 second) battery test. </p>
<dt>test.battery.start <i>value</i></p>
<dd>Perform a battery test for the duration of <i>num</i> seconds (truncated to units of 60 seconds). </p>
<dt>test.battery.stop</p>
<dd>Stop a running battery test (not available on some hardware.) </p>
</dl>
<h2>Battery Charge</h2>
<p>Due to popular demand, this driver will report a guesstimated <code>battery.charge</code> and optionally <code>battery.runtime</code>, provided you specified a couple of the <code>EXTRA PARAMETERS</code> listed above. </p>
<p> If you specify both <code>battery.voltage.high</code> and <code>battery.voltage.low</code> in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), but don&#8217;t enter <code>runtimecal</code>, it will guesstimate the state of charge by looking at the battery voltage alone. This is not reliable under load, as this only gives reasonably accurate readings if you disconnect the load, let the battery rest for a couple of minutes and then measure the open cell voltage. This just isn&#8217;t practical if the power went out and the UPS is providing power for your systems. </p>
<pre> battery.voltage - battery.voltage.low
battery.charge = ------------------------------------------ x 100 %
 battery.voltage.high - battery.voltage.low</pre>
<p>There is a way to get better readings without disconnecting the load but this requires to keep track on how much (and how fast) current is going in- and out of the battery. If you specified the <code>runtimecal</code>, the driver will attempt to do this. Note however, that this heavily relies on the values you enter and that the UPS must be able to report the load as well. There are quite a couple of devices that report 0 % (or any other fixed value) at all times, in which case this obviously doesn&#8217;t work. </p>
<p> The driver also has no way of determining the degradation of the battery capacity over time, so you&#8217;ll have to deal with this yourself (by adjusting the values in <code>runtimecal</code>. Also note that the driver guesses the initial state of charge based on the battery voltage, so this may be less than 100 %, even when you are certain that they are full. There is just no way to reliably measure this between 0 and 100 % full charge. </p>
<p> This is better than nothing (but not by much). If any of the above calculations is giving you incorrect readings, you are the one that put in the values in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), so don&#8217;t complain with the author. If you need something better, buy a UPS that reports <code>battery.charge</code> and <code>battery.runtime</code> all by itself without the help of a NUT driver.</p>
<h2>Known Problems</h2>
<p>Some UPS commands aren&#8217;t supported by all models. In most cases, the driver will send a message to the system log when the user tries to execute an unsupported command. Unfortunately, some models don&#8217;t even provide a way for the driver to check for this, so the unsupported commands will silently fail. </p>
<p> Both the <code>load.off</code> and <code>shutdown.stayoff</code> instant commands are meant to turn the load off indefinitely. However, some UPS models don&#8217;t allow this. </p>
<p> Some models report a bogus value for the beeper status (will always be <i>enabled</i> or <i>disabled</i>). So, the <code>beeper.toggle</code> command may appear to have no effect in the status reported by the driver when, in fact, it is working fine. </p>
<p> The temperature and load value is known to be bogus in some models.</p>
<h2>Authors</h2>
<p>Arjen de Korte &lt;adkorte-guest at alioth.debian.org&gt; Alexander Gordeev &lt;lasaine at lvk.cs.msu.su&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
