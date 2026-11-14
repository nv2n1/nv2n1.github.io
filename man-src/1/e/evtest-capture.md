---
title: "evtest-capture(1)"
name: "evtest-capture"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evtest-capture/"
description: "evtest-capture – Input device event capture program"
---

<h2 class="name">NAME</h2>
<p> evtest-capture &#8211; Input device event capture program </p>
<h2>SYNOPSIS</h2>
<pre>
evtest-capture &quot;/dev/input/eventX&quot; [evtest-capture.xml]
</pre>
<h2>DESCRIPTION</h2>
<p> evtest-capture captures the information and events from the input device specified on the command line and writes it to the xml file given. If no filename is given for the output file, evtest-capture.xml is chosen as default. </p>
<p> evtest-capture needs to be able to read from the device; in most cases this means it must be run as root. </p>
<p> Together with with evtest-create-device.xsl, a simple uinput-based software input device can be created that replays the events as if the same input was performed on the physical device. This can be useful to replicate bugs with input devices in upper layers of the stack. </p>
<p> To convert evtest-capture.xml into such a uinput device, run: </p>
<dl>
<dt>
<dd>
<pre>
xsltproc evtest-create-device.xls evtest-capture.xml &gt; mydevice.c
gcc -o mydevice mydevice.c
./mydevice
</pre>
</dl>
<h2>DIAGNOSTICS</h2>
<p> If evtest-capture does not see any events even though the device is being used, the device may be grabbed by a process (EVIOCGRAB). This is usually the case when debugging a synaptics device from within X. VT switching to a TTY or shutting down the X server terminates this grab and synaptics devices can be debugged.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-evtest/">evtest</a>(1)</p>
<h2>AUTHOR</h2>
<p> evtest-capture was written by Peter Hutterer &lt;m[blue]<code>peter.hutterer [at] redhat.com</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> peter.hutterer [at] redhat.com</p>
<dl>
<dt>
<dd> mailto:peter.hutterer [at] redhat.com</dl>
</dl>
<h2>Index</h2>
