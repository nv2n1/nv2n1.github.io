---
title: "evemu-record(1)"
name: "evemu-record"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evemu-record/"
description: "evemu-describe, evemu-record – print information and events from an input device"
---

<h2 class="name">NAME</h2>
<p> evemu-describe, evemu-record &#8211; print information and events from an input device </p>
<h2>SYNOPSIS</h2>
<pre><code>
evemu - describe[/ dev / input / eventX][output file]
</code></pre>
<pre><code>
evemu - record[--autorestart = s][/ dev / input / eventX][output file]
</code></pre>
<h2>DESCRIPTION</h2>
<p> evemu-describe gathers information about the input device and prints it to stdout. This information can be parsed by <a href="/docs/linux/man/1-evemu-device/">evemu-device</a>(1) to create a virtual input device with the same properties. </p>
<p> evemu-record captures events from the input device and prints them to stdout. The events can be parsed by <a href="/docs/linux/man/1-evemu-play/">evemu-play</a>(1) to let a virtual input device created with <a href="/docs/linux/man/1-evemu-device/">evemu-device</a>(1) emit the exact same event sequence. </p>
<p> evemu-describe and evemu-record need to be able to read from the device; in most cases this means they must be run as root. </p>
<p> If an event node is provided, evemu-describe and evemu-record use that event node. Otherwise, the user must interactively choose from a list of detected devices. </p>
<p> If no output file is given, stdout is used.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<pre>
--autorestart=&lt;s&gt;
      Terminate the current recording after &lt;s&gt; seconds of device
      inactivity. This option requires an output, the file is suffixed
      with the date and time of the recording's start.
      The timeout must be greater than 0.
</pre>
</dl>
<h2>DIAGNOSTICS</h2>
<p> If evtest-record does not see any events even though the device is being used, the device may be grabbed by a process (EVIOCGRAB). This is usually the case when debugging a synaptics or wacom device from within X. VT switching to a TTY or shutting down the X server terminates this grab and the devices can be recorded. For most X drivers, disabling the device also removes the grab. </p>
<p> The following command shows the processes with an open file descriptor on the device. </p>
<dl>
<dt>
<dd>
<pre>
fuser -v /dev/input/eventX
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-evemu-device/">evemu-device</a>(1) <a href="/docs/linux/man/1-evemu-play/">evemu-play</a>(1)</p>
<h2>AUTHOR</h2>
<p> evemu was written by Henrik Rydberg &lt;m[blue]<code>rydberg [at] euromail.se</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> rydberg [at] euromail.se</p>
<dl>
<dt>
<dd> mailto:rydberg [at] euromail.se</dl>
</dl>
<h2>Index</h2>
