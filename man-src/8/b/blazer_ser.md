---
title: "blazer_ser(8)"
name: "blazer_ser"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blazer_ser/"
description: "blazer_ser – Driver for Megatec/Q1 protocol serial based UPS equipment"
---

<p>blazer_ser &#8211; Driver for Megatec/Q1 protocol serial based UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the blazer driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The blazer driver is known to work with various UPSes from Blazer, Energy Sistem, Fenton Technologies, General Electric, Mustek and many others. The NUT compatibility table lists all the known supported models. Keep in mind, however, that other models not listed there may also be supported, but haven&#8217;t been tested. </p>
<p> All devices with a serial interface (use the <code>blazer_ser</code> driver) and many with a USB interface (use the <code>blazer_usb</code> driver) are supported.</p>
<h2>Extra Arguments</h2>
<p>You may need to override or provide defaults for some values, depending on the make and model of your UPS. The following are the ones that most likely will need changing (see <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)): </p>
<p> <code>default.battery.voltage.high =</code> <i>value</i></p>
<dl>
<dd>Maximum battery voltage that is reached after about 12 to 24 hours charging. If you want the driver to report a guesstimated <code>battery.charge</code>, you need to specify this (see BATTERY CHARGE).</dl>
<p> <code>default.battery.voltage.low =</code> <i>value</i></p>
<dl>
<dd>Minimum battery voltage just before the UPS automatically shuts down. If you want the driver to report a guesstimated <code>battery.charge</code>, you need to specify this (see BATTERY CHARGE).</dl>
<p> <code>default.battery.voltage.nominal =</code> <i>value</i>, <code>override.battery.voltage.nominal =</code> <i>value</i></p>
<dl>
<dd>Some devices show a wrong nominal battery voltage (or none at all), so you may need to override or set a default value.</dl>
<p> <code>override.battery.packs =</code> <i>value</i></p>
<dl>
<dd>Some devices report a part of the total battery voltage. For instance, if <code>battery.voltage.nominal</code> is 24 V, but it reports a <code>battery.voltage</code> of around 2 V, the number of <code>battery.packs</code> to correct this reading would be 12. The driver will attempt to detect this automatically, but if this fails somehow, you may want to override this value.</dl>
<p> <code>ondelay =</code> <i>value</i></p>
<dl>
<dd>Time to wait before switching on the UPS (minutes). Note that a value below 3 minutes, may cause earlier firmware versions to not switch on automatically, so it defaults to 3 minutes. The acceptable range is 0..9999 minutes.</dl>
<p> <code>offdelay =</code> <i>value</i></p>
<dl>
<dd>Time to wait before shutting down the UPS (seconds). This value is truncated to units of 6 seconds (less than 60 seconds) or 60 seconds (more than 60 seconds). Defaults to 30 seconds. The acceptable range is 12..600 seconds.</dl>
<p> <code>norating</code></p>
<dl>
<dd>Some UPSes will lock up if you attempt to read rating information from them. Setting this flag will make the driver skip this step.</dl>
<p> <code>novendor</code></p>
<dl>
<dd>Some UPSes will lock up if you attempt to read vendor information from them. Setting this flag will make the driver skip this step.</dl>
<p> <code>protocol =</code> <i>string</i></p>
<dl>
<dd>Skip autodetection of the protocol to use and only use the one specified. Supported values <i>megatec</i>, <i>megatec/old</i>, <i>mustek</i> and <i>zinto</i>.</dl>
<p> <code>runtimecal =</code> <i>value,value,value,value</i></p>
<dl>
<dd>Parameter used in the (optional) runtime estimation. This takes two runtimes at different loads. Typically, this uses the runtime at full load and the runtime at half load. For instance, if your UPS has a rated runtime of 240 seconds at full load and 720 seconds at half load, you would enter </p>
<dl>
<dd>
<pre>runtimecal = 240,100,720,50</pre>
</dl>
<p> The first load should always be higher than the second. If you have values available for loads other than 100 and 50 % respectively, you can use those too, but keep them spaced apart as far as reasonably possible. Just don&#8217;t get too close to no load (prediction of runtime depends more on idle load for the battery then).</dl>
<p> <code>chargetime =</code> <i>value</i></p>
<dl>
<dd>The time needed to fully recharge the battery after being fully discharged. If not specified, the driver defaults to 43200 seconds (12 hours). Only used if <code>runtimecal</code> is also specified.</dl>
<p> <code>idleload =</code> <i>value</i></p>
<dl>
<dd>Minimum battery load used by the driver to estimate the runtime. If not specified, the driver defaults to 10%. Only used if <code>runtimecal</code> is also specified.</dl>
<h3>Serial Interface Only</h3>
<p><code>cablepower =</code> <i>string</i></p>
<dl>
<dd>By default the driver will set DTR and clear RTS (<i>normal</i>). If you find that your UPS isn&#8217;t detected or the communication with the UPS is unreliable, you may try if clear DTR and set RTS (<i>reverse</i>), set DTR and RTS (<i>both</i>) or clear DTR and RTS (<i>none</i>) improves this situation.</dl>
<h2>Ups Commands</h2>
<p>This driver supports some instant commands (see <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8)): </p>
<p> <code>beeper.toggle</code></p>
<dl>
<dd>Toggle the UPS beeper. (Not available on some hardware.)</dl>
<p> <code>load.on</code></p>
<dl>
<dd>Turn on the load immediately.</dl>
<p> <code>load.off</code></p>
<dl>
<dd>Turn off the load immediately (see KNOWN PROBLEMS).</dl>
<p> <code>shutdown.return</code></p>
<dl>
<dd>Turn off the load and return when power is back. Uses the timers defined by <code>ondelay</code> and <code>offdelay</code>.</dl>
<p> <code>shutdown.stayoff</code></p>
<dl>
<dd>Turn off the load and remain off (see KNOWN PROBLEMS). Uses the timer defined by <code>offdelay</code>.</dl>
<p> <code>shutdown.stop</code></p>
<dl>
<dd>Stop a shutdown in progress.</dl>
<p> <code>test.battery.start.deep</code></p>
<dl>
<dd>Perform a long battery test (Not available on some hardware.)</dl>
<p> <code>test.battery.start.quick</code></p>
<dl>
<dd>Perform a (10 second) battery test.</dl>
<p> <code>test.battery.start</code> <i>value</i></p>
<dl>
<dd>Perform a battery test for the duration of <i>value</i> minutes.</dl>
<p> <code>test.battery.stop</code></p>
<dl>
<dd>Stop a running battery test (not available on some hardware.)</dl>
<h2>Battery Charge</h2>
<p>Due to popular demand, this driver will report a guesstimated <code>battery.charge</code> and optionally <code>battery.runtime</code>, provided you specified a couple of the EXTRA ARGUMENTS listed above. </p>
<p> If you specify both <code>battery.voltage.high</code> and <code>battery.voltage.low</code> in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), but don&#8217;t enter <code>runtimecal</code>, it will guesstimate the state of charge by looking at the battery voltage alone. This is not reliable under load, as this only gives reasonably accurate readings if you disconnect the load, let the battery rest for a couple of minutes and then measure the open cell voltage. This just isn&#8217;t practical if the power went out and the UPS is providing power for your systems. </p>
<dl>
<dd>
<pre> battery.voltage - battery.voltage.low
battery.charge = ------------------------------------------ x 100 %
 battery.voltage.high - battery.voltage.low</pre>
</dl>
<p> There is a way to get better readings without disconnecting the load but this requires one to keep track on how much (and how fast) current is going in- and out of the battery. If you specified the <code>runtimecal</code>, the driver will attempt to do this. Note however, that this heavily relies on the values you enter and that the UPS must be able to report the load as well. There are quite a couple of devices that report 0 % (or any other fixed value) at all times, in which case this obviously doesn&#8217;t work. </p>
<p> The driver also has no way of determining the degradation of the battery capacity over time, so you&#8217;ll have to deal with this yourself (by adjusting the values in <code>runtimecal</code>). Also note that the driver guesses the initial state of charge based on the battery voltage, so this may be less than 100 %, even when you are certain that they are full. There is just no way to reliably measure this between 0 and 100 % full charge. </p>
<p> This is better than nothing (but not by much). If any of the above calculations is giving you incorrect readings, you are the one that put in the values in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), so don&#8217;t complain with the author. If you need something better, buy a UPS that reports <code>battery.charge</code> and <code>battery.runtime</code> all by itself without the help of a NUT driver.</p>
<h2>Notes For The Previous User Of Megatec Drivers</h2>
<p>The blazer drivers having replaced the megatec ones, some configuration changes may be required by users switching to blazer. </p>
<p> Part of this, the following megatec options, in ups.conf, have to be changed: </p>
<p> <code>battvolts</code></p>
<dl>
<dd>You need to use <i>default.battery.voltage.high</i> and <i>default.battery.voltage.low</i></dl>
<p> <code>dtr and rts</code></p>
<dl>
<dd>You need to use <i>cablepower</i></dl>
<p> <code>ignoreoff</code></p>
<dl>
<dd>This parameter can simply be discarded, since it was a wrong understanding of the specification.</dl>
<h2>Known Problems</h2>
<p>Some UPS commands aren&#8217;t supported by all models. In most cases, the driver will send a message to the system log when the user tries to execute an unsupported command. Unfortunately, some models don&#8217;t even provide a way for the driver to check for this, so the unsupported commands will silently fail. </p>
<p> Both the <code>load.off</code> and <code>shutdown.stayoff</code> instant commands are meant to turn the load off indefinitely. However, some UPS models don&#8217;t allow this. </p>
<p> Some models report a bogus value for the beeper status (will always be <i>enabled</i> or <i>disabled</i>). So, the <code>beeper.toggle</code> command may appear to have no effect in the status reported by the driver when, in fact, it is working fine. </p>
<p> The temperature and load value is known to be bogus in some models.</p>
<h2>Authors</h2>
<p>Arjen de Korte &lt;adkorte-guest at alioth.debian.org&gt;, Alexander Gordeev &lt;lasaine at lvk.cs.msu.su&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-blazer_usb/">blazer_usb</a></code>(8), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)</p>
<h3>Internet Resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> The NUT HCL: <a rel="nofollow" href="http://www.networkupstools.org/stable-hcl.html">http://www.networkupstools.org/stable-hcl.html</a> </p>
