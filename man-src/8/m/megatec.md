---
title: "megatec(8)"
name: "megatec"
section: "8"
letter: "m"
url: "/docs/linux/man/8-megatec/"
description: "megatec – Driver for Megatec protocol based UPS equipment"
---

<p>megatec &#8211; Driver for Megatec protocol based UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the megatec driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The megatec driver is known to work with various UPSes from Blazer, Energy Sistem, Fenton Technologies, Mustek and many others. The NUT compatibility table lists all the known supported models. Keep in mind, however, that other models not listed there may also be supported but haven&#8217;t been tested. </p>
<p> On models with both a serial port (RS-232) and an USB port, only the serial port is supported. Connecting a computer which does not have a serial interface to the UPS serial port using a USB-to-serial converter should work, provided the converter is supported by your operating system.</p>
<h2>Extra Arguments</h2>
<p>This driver supports some extra parameters (see <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)): </p>
<dl>
<dt>mfr=<i>string</i></p>
<dd>Optional. Specify the UPS manufacturer name. </p>
<dt>model=<i>string</i></p>
<dd>Optional. Specify the UPS model name. </p>
<dt>serial=<i>string</i></p>
<dd>Optional. Specify the UPS serial number. </p>
<dt>offdelay=<i>int</i></p>
<dd>Optional. After receiving a shutdown command, the UPS will wait this many minutes before turning off the load. Specify this if the UPS must remain online for a short period of time after the computer has powered down. The default is 0 (turn off immediately). </p>
<dt>ondelay=<i>int</i></p>
<dd>Optional. After turning off the load (see <code>offdelay</code>), the UPS will wait at least this many minutes before coming back online. If line power gets restored before this delay expires, the UPS will wait until it does. If line power gets restored after this delay expires, the UPS will power on the load immediately. The default is 2 minutes. </p>
<dt>lowbatt=<i>float</i></p>
<dd>Optional. Low battery level (%). Overrides the hardware default level. Cannot be used if the driver is unable to calculate the charge percentage for your UPS automatically (see <code>KNOWN PROBLEMS</code>) and the <code>battvolts</code> parameter isn&#8217;t specified. </p>
<dt>battvolts=<i>float</i>:<i>float</i></p>
<dd>Optional. The battery voltage interval (see <code>KNOWN PROBLEMS</code>). </p>
<dt>battvoltmult=<i>num</i></p>
<dd>Optional. Multiply the reported battery voltage by this number. Some devices report only a fraction of the total battery voltage. The default is 1. </p>
<dt>dtr=<i>int</i></p>
<dd>Optional. Some UPS models need the DTR serial line set to a specific state, either <i>0</i> or <i>1</i>. See also <code>rts</code>. </p>
<dt>rts=<i>int</i></p>
<dd>Optional. Some UPS models need the RTS serial line set to a specific state, either <i>0</i> or <i>1</i>. See also <code>dtr</code>. </p>
<dt>ignoreoff</p>
<dd>Optional. This option should be used if <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8) shows the UPS status as OFF when it&#8217;s clearly on. This will force the driver to ignore the OFF status altogether. </p>
<dt>sendpace=<i>int</i></p>
<dd>Optional. This option can be used to change the wait interval between each character that is sent to the UPS, between 1 and 1000 milliseconds. Some models may need this if the default interval (100 milliseconds) proves to be too long, or too short. </p>
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
<dt>reset.input.minmax</p>
<dd>Reset minimum and maximum input voltage status. </p>
<dt>reset.watchdog</p>
<dd>Restarts the UPS watchdog timeout. The watchdog is started if it isn&#8217;t running, which means the UPS shuts down one minute after this command is executed for the last time, restarting one minute afterwards. To cancel the watchdog, run the &quot;shutdown.stop&quot; command. </p>
<dt>shutdown.return</p>
<dd>Turn off the load and return when power is back. Uses the timers defined by <code>ondelay</code> and <code>offdelay</code>. </p>
<dt>shutdown.stayoff</p>
<dd>Turn off the load and remain off (see <code>KNOWN PROBLEMS</code>). Uses the timer defined by <code>offdelay</code>. </p>
<dt>shutdown.stop</p>
<dd>Stop a shutdown in progress. </p>
<dt>test.battery.start.deep</p>
<dd>Perform a long battery test (Not available on some hardware.) </p>
<dt>test.battery.start</p>
<dd>Perform a (10 second) battery test. </p>
<dt>test.battery.stop</p>
<dd>Stop a running battery test. (Not available on some hardware.) </p>
</dl>
<h2>Known Problems</h2>
<p>The battery charge (%) value is only a best-effort calculation and may be incorrect, or non-existant, for some UPS models. In any case, you can always resort to finding the voltages at which the battery becomes fully discharged and fully charged, and specify them manually using the &quot;battvolts&quot; option. If you do this, please notify the author of this driver so that information can be added to the NUT hardware compatibility list. Note that if you also specified the &quot;battvoltmult&quot; option, you need to divide the found voltages for fully discharged and fully charged by this number. </p>
<p> Some UPS commands aren&#8217;t supported by all models. In most cases, the driver will send a message to the system log when the user tries to execute an unsupported command. Unfortunately, some models don&#8217;t even provide a way for the driver to check for this, so the unsupported commands will silently fail. </p>
<p> Both the &quot;load.off&quot; and &quot;shutdown.stayoff&quot; instant commands are meant to turn the load off indefinitely. However, some UPS models don&#8217;t allow this. When this is the case, the driver will tell the UPS to turn off the load for 9999 minutes (about 7 days) and a message will be sent to the system log. </p>
<p> Some models report a bogus value for the beeper status (will always be &quot;enabled&quot; or &quot;disabled&quot;). So, the &quot;beeper.toggle&quot; command may appear to have no effect in the status reported by the driver when, in fact, it is working fine. </p>
<p> The temperature value is also known to be bogus in some models.</p>
<h2>Author</h2>
<p>Carlos Rodrigues &lt;carlos.efr at mail.telepac.pt&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
