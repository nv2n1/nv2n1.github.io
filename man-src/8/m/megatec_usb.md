---
title: "megatec_usb(8)"
name: "megatec_usb"
section: "8"
letter: "m"
url: "/docs/linux/man/8-megatec_usb/"
description: "megatec_usb – Driver for Megatec protocol based USB UPS equipment"
---

<p>megatec_usb &#8211; Driver for Megatec protocol based USB UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the megatec_usb driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<p> <code>Note.</code> This driver is experimental at the moment. It is currently being worked on and may change over time. However, it is stable in execution and does what is needed.</p>
<h2>Supported Hardware</h2>
<p>The megatec_usb driver is known to work with various UPSes from Krauler, Agiler, and Upsonic (Ablerex interface). Others that use the Megatec protocol may work, but haven&#8217;t been tested. </p>
<p> This driver supports the USB versions of UPSs, if you have only serial interface then use the straight <code><a href="/docs/linux/man/8-megatec/">megatec</a></code>(8) driver. </p>
<p> If you find that this driver does not work, and you are sure that your hardware speaks megatec protocol, then you can easily extend this driver. However, you will need to do some analysis of the commands that are sent to the UPS. Please see the forums for discussions on this and how to extend this driver.</p>
<h2>Extensions To Megatec</h2>
<p>This driver extends the standard <code><a href="/docs/linux/man/8-megatec/">megatec</a></code>(8) driver to work with certain UPSes that have a USB interface. These devices do not obey the normal rules for HID USB devices and therefore the <code><a href="/docs/linux/man/8-newhidups/">newhidups</a></code>(8) driver will not work for them. </p>
<p> This driver takes the standard serial interface and passes this over USB to the UPS. This means that most, but not all, commands available for the serial driver will work. For Krauler, Agiler, and Upsonic (with Ablerex interface) UPSes it appears to give very similar results to the serial interface. The driver supports monitoring most of the usual UPS variables, and also supports automatic shutdown.</p>
<h2>Extra Arguments</h2>
<dl>
<dt>mfr=<i>string</i></p>
<dd>Optional. Specify the UPS manufacturer name. </p>
<dt>model=<i>string</i></p>
<dd>Optional. Specify the UPS model name. </p>
<dt>serial=<i>string</i></p>
<dd>Optional. Specify the UPS serial number. </p>
<dt>lowbatt=<i>float</i></p>
<dd>Optional. Low battery level (%). Overrides the hardware default level. </p>
<dt>ondelay=<i>int</i></p>
<dd>Optional. Delay before the UPS is turned back on (minutes). </p>
<dt>offdelay=<i>int</i></p>
<dd>Optional. Delay before the UPS is turned off (minutes). </p>
<dt>battvolts=<i>float</i>:<i>float</i></p>
<dd>Optional. The battery voltage interval &lt;empty:full&gt; (volts). </p>
<dt>vendor=<i>regex</i></p>
<dd>
<dt>product=<i>regex</i></p>
<dd>
<dt>vendorid=<i>regex</i></p>
<dd>
<dt>productid=<i>regex</i></p>
<dd>Select a specific UPS, in case there is more than one connected via USB. Each option specifies an extended regular expression (see <code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code>) that must match the UPS&#8217;s entire vendor/product/serial string (minus any surrounding whitespace), or the whole 4-digit hexadecimal code for vendorid and productid. Try <code>-DD</code> for finding out the strings to match. </p>
<p> Examples: </p>
<p>&nbsp;<wbr><code>-x vendor=&quot;Foo.Corporation.*&quot;</code> </p>
<p>&nbsp;<wbr><code>-x vendorid=05b8</code>&nbsp;<wbr>(Agiler) </p>
<p>&nbsp;<wbr><code>-x product=&quot;.*(Smart|Back)-?UPS.*&quot;</code> </p>
<dt>bus=<i>regex</i></p>
<dd>Select a UPS on a specific USB bus or group of busses. The argument is a regular expression that must match the bus name where the UPS is connected (e.g. bus=&quot;002&quot;, bus=&quot;00[2-3]&quot;). </p>
<dt>subdriver=<i>string</i></p>
<dd>Select a serial-over-USB subdriver to use. You have a choice between &quot;agiler&quot; and &quot;krauler&quot; subdrivers currently. </p>
</dl>
<h2>Ups Commands</h2>
<p>This driver supports some extra commands (see <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8)): </p>
<dl>
<dt>beeper.toggle</p>
<dd>Toggle the UPS beeper. (Not available on some hardware.) </p>
<dt>load.on</p>
<dd>Turn on the load immediately. </p>
<dt>load.off</p>
<dd>Turn off the load immediately. (Not yet supported) </p>
<dt>reset.input.minmax</p>
<dd>Reset minimum and maximum input voltage status. (Not yet supported) </p>
<dt>reset.watchdog</p>
<dd>Restarts the UPS watchdog timeout. The watchdog is started if it isn&#8217;t running, which means the UPS shuts down one minute after this command is executed for the last time, restarting one minute afterwards. To cancel the watchdog, run the &quot;shutdown.stop&quot; command. </p>
<dt>shutdown.return</p>
<dd>Turn off the load and return when power is back. (Not yet supported) </p>
<dt>shutdown.stayoff</p>
<dd>Turn off the load and remain off. (Not yet supported) </p>
<dt>shutdown.stop</p>
<dd>Stop a shutdown in progress. </p>
<dt>test.battery.start.deep</p>
<dd>Perform a long battery test (Not available on some hardware.) </p>
<dt>test.battery.start</p>
<dd>Perform a (10 second) battery test. </p>
<dt>test.battery.stop</p>
<dd>Stop a running battery test. (Not available on some hardware.) </p>
</dl>
<h2>User Variables</h2>
<p>The behavior of the driver can be controlled by some user definable variables (see <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)): </p>
<dl>
<dt>ups.delay.shutdown</p>
<dd>Interval to wait after shutdown with delay command (seconds) </p>
<dt>ups.delay.start</p>
<dd>Interval to wait before (re)starting the load (seconds) </p>
</dl>
<h2>Known Problems</h2>
<p>The battery charge (%) value is only a best-effort calculation and may be incorrect, or non-existant, for some UPS models. In any case, you can always resort to finding the voltages at which the battery becomes fully discharged and fully charged, and specify them manually using the &quot;battvolts&quot; option. If you do this, please notify the author of this driver. </p>
<p> Some UPS commands aren&#8217;t supported by all models. In most cases, the driver will send a message to the system log when the user tries to execute an unsupported command. Unfortunately, some models don&#8217;t even provide a way for the driver to check for this, so the unsupported commands will silently fail. </p>
<p> Some models report a bogus value for the beeper status (will always be &quot;enabled&quot; or &quot;disabled&quot;). So, the &quot;beeper.toggle&quot; command may appear to have no effect in the status reported by the driver when, in fact, it is working fine. </p>
<p> The temperature value is also known to be bogus in some models.</p>
<h2>Authors</h2>
<p>Carlos Rodrigues &lt;carlos.efr at mail.telepac.pt&gt;<br />
 Andrey Lelikov &lt;nut-driver at lelik.org&gt;<br />
 Alexander Gordeev &lt;lasaine at lvk.cs.msu.su&gt;<br />
 Jon Gough &lt;jon.gough at eclipsesystems.com.au&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-megatec/">megatec</a></code>(8), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
