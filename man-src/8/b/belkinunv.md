---
title: "belkinunv(8)"
name: "belkinunv"
section: "8"
letter: "b"
url: "/docs/linux/man/8-belkinunv/"
description: "belkinunv – Driver for Belkin \"Universal UPS\" and compatible"
---

<p>belkinunv &#8211; Driver for Belkin &quot;Universal UPS&quot; and compatible</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the belkin driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The belkinunv driver is known to work with the Belkin Universal UPS models F6C800-UNV and F6C120-UNV, and is expected to work with other Belkin Universal UPS models. The driver only supports serial communication, not USB. </p>
<p> The Trust UPS and older Belkin units are not supported by this driver, and neither are the Belkin Home Office models (F6H500-SER and so forth). However, some Belkin models, such as the Regulator Pro, are supported by the <code><a href="/docs/linux/man/8-belkin/">belkin</a></code>(8) driver, and the Home Office models are supported using the <code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8) driver with upstype=7.</p>
<h2>Soft Shutdown Workaround</h2>
<p>One problem with the Belkin Universal UPS is that it cannot enter a soft shutdown (shut down the load until AC power returns) unless the batteries are completely depleted. Thus, one cannot just shut off the UPS after operating system shutdown; it will not come back on when the power comes back on. Therefore, the belkinunv driver should never be used with the <code>-k</code> option. Instead, the <code>-x wait</code> option is provided as a workaround. </p>
<p> When called with the <code>-x wait</code> option, <code>belkinunv</code> behaves as a standalone program (i.e., it does not fork into the background). It performs one simple task: it connects to the UPS, waits for AC power to return, and then exits with status 0. </p>
<p> This is meant to be used in a shutdown script as follows: during a shutdown, after all filesystems have been remounted read-only, and just before the system would normally be halted: check /etc/killpower (or similar) to see if this shutdown was caused by <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8), and if yes, call <code>belkinunv -x wait</code>. If AC power comes back on, <code>belkinunv</code> exits, and things should be arranged so that the system reboots in this case. If AC power does not come back on, the UPS will eventually run out of batteries, kill the computer&#8217;s power supply, and go into soft shutdown mode, which means everything will reboot properly when the power returns. In either case, a deadlock is avoided. </p>
<p> In addition, if an optional integer argument is given to the <code>-x wait</code> option, this causes <code>belkinunv</code> to wait not only for AC power to be present, but also for the battery charge to reach the given level. I use this as part of my startup scripts, to ensure that the batteries are sufficiently charged before the computer continues booting. This should be put very early in the startup script, before any filesystems are mounted read/write, and before any filesystem checks are performed. </p>
<p> Several other <code>-x</code> options are provided to fine-tune this behavior. See the options below for detailed descriptions. See the examples below for examples of how to use <code>belkinunv</code> in shutdown and startup scripts.</p>
<h2>Options</h2>
<p>See also <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8) for generic options. Never use the <code>-k</code> option with this driver; it does not work properly. </p>
<p> <code>-x wait</code>[=<i>level</i>]</p>
<dl>
<dd>When this option is used, <code>belkinunv</code> does not fork into the background, but behaves as a standalone program. It connects to the UPS and waits until AC power is present. If <i>level</i> is specified, it also waits until the battery charge reaches at least the given level in percent. Then, and only then, <code>belkinunv</code> exits. In addition, while <code>belkinunv</code> runs in this mode, it displays a status line with information on the UPS status and battery level. This is intended for use in the computer&#8217;s shutdown and startup scripts, as described under Soft Shutdown Workaround above.</dl>
<p> <code>-x nohang</code></p>
<dl>
<dd>This option only has an effect when used in conjunction with the <code>-x wait</code> option. It causes <code>belkinunv</code> to exit if a connection with the UPS cannot be established or is lost, instead of retrying forever, which is the default behavior. The <code>-x nohang</code> option should be used in a startup script, to ensure the computer remains bootable even if the UPS has been disconnected during the power failure (for instance, you attached your computer to a generator, carried it to a neighbor&#8217;s house, or whatever).</dl>
<p> <code>-x flash</code></p>
<dl>
<dd>This option only has an effect when used in conjunction with the <code>-x wait</code> option. It causes the UPS load to be shut off for a short time (&quot;flashed&quot;) just after the AC power has returned and the requested battery level (if any) has been attained. This is useful if slaves are attached to this UPS; the flash will cause all of them to reboot. Note that, due to the design of the Belkin UPS hardware, the load shutdown lasts ca. 1&#8212;2 minutes; a shorter flash cannot be performed reliably. Also, the computers will reboot at the scheduled time, on battery power if necessary, even if AC power fails again in the meantime. This should not be a problem, as your startup scripts can catch this situation.</dl>
<p> <code>-x silent</code></p>
<dl>
<dd>This option only has an effect when used in conjunction with the <code>-x wait</code> option. It suppresses the status line which <code>belkinunv</code> would normally print.</dl>
<p> <code>-x dumbterm</code></p>
<dl>
<dd>This option only has an effect when used in conjunction with the <code>-x wait</code> option. It changes the way in which <code>belkinunv</code> prints its status line. Normally, terminal control sequences are used to overwrite the same line with new status information, each time the status is updated. This may not work on all terminals. If the <code>-x dumbterm</code> option is given, each status update is written on a new line.</dl>
<h2>Variables</h2>
<p><code>battery.charge</code>, <code>battery.runtime</code></p>
<dl>
<dd>not supported by all hardware.</dl>
<p> <code>battery.voltage</code>, <code>battery.voltage.nominal</code>, <code>input.frequency</code>, <code>input.frequency.nominal</code></p>
<dl>
<dd>e.g. 60 for 60Hz</dl>
<p> <code>input.sensitivity</code></p>
<dl>
<dd>writable: normal/medium/low</dl>
<p> <code>input.transfer.high</code></p>
<dl>
<dd>writable: high transfer voltage point in V</dl>
<p> <code>input.transfer.low</code></p>
<dl>
<dd>writable: low transfer voltage point in V</dl>
<p> <code>input.voltage</code>, <code>input.voltage.maximum</code>, <code>input.voltage.minimum</code>, <code>input.voltage.nominal</code>, <code>output.frequency</code>, <code>output.voltage</code>, <code>ups.beeper.status</code></p>
<dl>
<dd>writable. Values: enabled/disabled/muted. This variable controls the state of the panel beeper. Enabled means sound when the alarm is present, disabled means never sound, and muted means the sound is temporarily disabled until the alarm would normally stop sounding. In the muted state, the beeper is automatically turned back on at the next event (AC failure, battery test, etc). Also, the beeper can&#8217;t be turned off during a critical event (low battery). Note that not all UPS models support the &quot;disabled&quot; state.</dl>
<p> <code>ups.firmware</code>, <code>ups.load</code>, <code>ups.model</code>, <code>ups.power.nominal</code></p>
<dl>
<dd>e.g. 800 for an 800VA system</dl>
<p> <code>ups.status</code></p>
<dl>
<dd>a list of flags; see the status flags below.</dl>
<p> <code>ups.temperature</code></p>
<dl>
<dd>not supported by all hardware.</dl>
<p> <code>ups.test.result</code>, <code>ups.delay.restart</code></p>
<dl>
<dd>time to restart (read only)</dl>
<p> <code>ups.delay.shutdown</code></p>
<dl>
<dd>time to shutdown (read only). This is always a multiple of 60 seconds.</dl>
<p> <code>ups.type</code></p>
<dl>
<dd>ONLINE/OFFLINE/LINEINT. This describes the basic layout of this UPS (for GUI clients which want to draw an animated picture of power flow). An offline UPS has a direct connection from AC input to AC output, and also a connection from AC input to the battery, and from the battery to AC output. An online UPS lacks the direct connection from AC input to AC output, whereas a line interactive UPS lacks the connection from AC input to the battery.</dl>
<h2>Commands</h2>
<p><code>beeper.enable, beeper.disable, beeper.mute</code></p>
<dl>
<dd>Enable, disable or mute the panel beeper. Note that if the beeper is muted, it is automatically turned back on at the next event (AC failure, battery test, etc). Also, the beeper can&#8217;t be turned muted during a critical event (low battery).</dl>
<p> <code>reset.input.minmax</code></p>
<dl>
<dd>Reset the variables <code>input.voltage.minimum</code> and <code>input.voltage.maximum</code>.</dl>
<p> <code>shutdown.reboot</code></p>
<dl>
<dd>Shut down load immediately for about 1&#8212;2 minutes.</dl>
<p> <code>shutdown.reboot.graceful</code></p>
<dl>
<dd>After 40 second delay, shut down load for about 1&#8212;2 minutes.</dl>
<p> <code>shutdown.stayoff</code></p>
<dl>
<dd>Shut down load immediately and stay off. The only way it can be turned back on is by manually pressing the front panel button.</dl>
<p> <code>test.battery.start, test.battery.stop</code></p>
<dl>
<dd>Start/stop 10 second battery test.</dl>
<p> <code>test.failure.start, test.failure.stop</code></p>
<dl>
<dd>Start/stop &quot;deep&quot; battery test.</dl>
<h2>Status Flags</h2>
<p><code>OB</code></p>
<dl>
<dd>load is on battery, including during tests</dl>
<p> <code>OFF</code></p>
<dl>
<dd>load is off</dl>
<p> <code>OL</code></p>
<dl>
<dd>load is online</dl>
<p> <code>ACFAIL</code></p>
<dl>
<dd>AC failure. Note that this refers to the AC input, and thus it is not the same as &quot;OB&quot;. An AC failure can occur at any time, for instance, during a battery test, or when the UPS load is off.</dl>
<p> <code>OVER</code></p>
<dl>
<dd>overload</dl>
<p> <code>OVERHEAT</code></p>
<dl>
<dd>overheat</dl>
<p> <code>COMMFAULT</code></p>
<dl>
<dd>UPS fault</dl>
<p> <code>LB</code></p>
<dl>
<dd>low battery</dl>
<p> <code>CHRG</code></p>
<dl>
<dd>charging</dl>
<p> <code>DEPLETED</code></p>
<dl>
<dd>the battery is depleted. When the UPS raises this flag, it simultaneously switches off the load.</dl>
<p> <code>RB</code></p>
<dl>
<dd>replace battery</dl>
<h2>Examples</h2>
<p>Here is an example for how <code>belkinunv</code> should be used in a computer&#8217;s shutdown script. These commands should go in the very last part of the shutdown script, after all file systems have been mounted read-only, and just before the computer halts. Note that <code>belkinunv</code> must be installed in a directory which is still readable at that point. </p>
<dl>
<dd>
<pre># NEAR END OF SHUTDOWN SCRIPT:
# if shutdown was caused by UPS, perform Belkin UPS workaround.
if [ -f /etc/killpower ] ; then
 echo &quot;Waiting for AC power, or for UPS batteries to run out...&quot;
 /usr/bin/belkinunv -x wait /dev/ttyS1</pre>
</dl>
<dl>
<dd>
<pre> # we get here if the power came back on. Reboot.
 echo &quot;Power is back. Rebooting...&quot;
 reboot
fi</pre>
</dl>
<p> And here is an example of how to use <code>belkinunv</code> in the startup script. These commands should go near the beginning of the startup script, before any file systems are mounted read/write, and before any file system integrity checks are done. </p>
<dl>
<dd>
<pre># NEAR BEGINNING OF STARTUP SCRIPT:
# if we are recovering from a power failure, wait for the UPS to
# charge to a comfortable level before writing anything to disk
if [ -f /etc/killpower ] ; then
 echo &quot;Waiting for UPS battery charge to reach 60%...&quot;
 /usr/bin/belkinunv -x wait=60 -x nohang /dev/ttyS1
fi</pre>
</dl>
<h2>Exit Status</h2>
<p>When used normally, <code>belkinunv</code> forks into the background and its diagnostics are the same as for all NUT drivers, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<p> When used with the <code>-x wait</code> option, the exit status is normally <code>0</code>. If the <code>-x nohang</code> option has also been specified, an exit status of <code>1</code> indicates that communication with the UPS was lost. If the <code>-x flash</code> option has been specified, an exit status of <code>2</code> indicates that the timed shutdown has failed.</p>
<h2>Extra Arguments</h2>
<p>This driver does not support any extra settings in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<dl>
<dd>&bull; The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></dl>
<dl>
<dd>&bull; The documentation for the protocol used by this UPS: belkin-universal-ups.html</dl>
<h2>Author</h2>
<p>Peter Selinger &lt;selinger [at] users.sourceforge.net&gt;</p>
