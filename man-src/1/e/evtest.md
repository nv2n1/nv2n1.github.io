---
title: "evtest(1)"
name: "evtest"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evtest/"
description: "evtest – Input device event monitor and query tool"
---

<h2 class="name">NAME</h2>
<p> evtest &#8211; Input device event monitor and query tool </p>
<h2>SYNOPSIS</h2>
<pre>
evtest [--grab] /dev/input/eventX
</pre>
<pre>
evtest --query /dev/input/eventX &lt;type&gt; &lt;value&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> The first invocation type displayed above (&quot;capture mode&quot;) causes evtest to display information about the specified input device, including all the events supported by the device. It then monitors the device and displays all the events layer events generated. </p>
<p> If the &#8211;grab flag is given in capture mode, evtest keeps an EVIOCGRAB on the device. While this grab is active, other processes will not receive events from the kernel devices. The grab is released again when evtest quits. </p>
<p> In the second invocation type (&quot;query mode&quot;), evtest performs a one-shot query of the state of a specific key <code>value</code> of an event <code>type</code>. </p>
<p> <code>type</code> is one of: <code>EV_KEY</code>, <code>EV_SW</code>, <code>EV_SND</code>, <code>EV_LED</code> (or the numerical value) </p>
<p> <code>value</code> can be either a decimal representation (e.g. 44), hex (e.g. 0x2c), or the constant name (e.g. KEY_Z) of the key/switch/sound/LED being queried. </p>
<p> If the state bit is set (key pressed, switch on, &#8230;), evtest exits with code 10. If the state bit is unset (key depressed, switch off, &#8230;), evtest exits with code 0. No other output is generated. </p>
<p> evtest needs to be able to read from the device; in most cases this means it must be run as root. </p>
<p> evtest is commonly used to debug issues with input devices in X.Org. The output of evtest shows the information presented by the kernel; based on this information it can be determined whether a bug may be a kernel or an X.Org issue.</p>
<h2>DIAGNOSTICS</h2>
<p> If evtest does not show any events even though the device is being used, the device may be grabbed by a process (EVIOCGRAB). This is usually the case when debugging a synaptics device from within X. VT switching to a TTY or shutting down the X server terminates this grab and synaptics devices can be debugged. </p>
<p> The following command shows the processes with an open file descriptor on the device: </p>
<dl>
<dt>
<dd>
<pre>
fuser -v /dev/input/eventX
</pre>
</dl>
<h2>EXIT CODE</h2>
<p> evtest returns 1 on error. </p>
<p> When used to query state, evtest returns 0 if the state bit is unset and 10 if the state bit is set.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-inputattach/">inputattach</a>(1)</p>
<h2>AUTHOR</h2>
<p> evtest was written by Vojtech Pavlik &lt;m[blue]<code>vojtech [at] suse.cz</code>m[]<font SIZE="-2">[1]</font>&gt;. </p>
<p> This manual page was written by Stephen Kitt &lt;m[blue]<code>steve [at] sk2.org</code>m[]<font SIZE="-2">[2]</font>&gt;, based on that present in the lineakd package, for the Debian GNU/Linux system (but may be used by others).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> vojtech [at] suse.cz</p>
<dl>
<dt>
<dd> mailto:vojtech [at] suse.cz</dl>
<dt> 2.</p>
<dd> steve [at] sk2.org</p>
<dl>
<dt>
<dd> mailto:steve [at] sk2.org</dl>
</dl>
<h2>Index</h2>
