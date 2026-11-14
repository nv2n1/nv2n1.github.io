---
title: "evemu-event(1)"
name: "evemu-event"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evemu-event/"
description: "evemu-device, evemu-play, evemu-event – create a virtual input device and replay an event sequence"
---

<h2 class="name">NAME</h2>
<p> evemu-device, evemu-play, evemu-event &#8211; create a virtual input device and replay an event sequence </p>
<h2>SYNOPSIS</h2>
<pre>
evemu-device [description-file]
</pre>
<pre>
evemu-play /dev/input/eventX &lt; event-sequence
evemu-play event-sequence.txt
</pre>
<pre><code>
evemu - event / dev / input / eventX[--sync]-- type&lt;type&gt; --code&lt;code&gt; --value&lt;value&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> evemu-device creates a virtual input device based on the description-file. This description is usually created by <a href="/docs/linux/man/1-evemu-describe/">evemu-describe</a>(1). evemu-device then creates a new input device with uinput and prints the name and the device file to stdout. </p>
<p> evemu-play replays the event sequence given on stdin through the input device. The event sequence must be in the form created by <a href="/docs/linux/man/1-evemu-record/">evemu-record</a>(1). If the argument is a file containing a recording, evemu-play creates the device and prompts the user for an interactive replay of the events. </p>
<p> evemu-event plays exactly one event with the current time. If <code>&#8211;sync</code> is given, evemu-event generates an <code>EV_SYN</code> event after the event. The event type and code may be specified as the numerical value or the symbolic name from linux/input.h. </p>
<p> evemu-device must be able to write to the uinput device node, and evemu-play must be able to write to the device node specified; in most cases this means it must be run as root.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-evemu-describe/">evemu-describe</a>(1) <a href="/docs/linux/man/1-evemu-record/">evemu-record</a>(1)</p>
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
