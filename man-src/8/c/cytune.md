---
title: "cytune(8)"
name: "cytune"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cytune/"
description: "cytune – tune driver parameters for Cyclades-Z multiport serial card"
---

<p>cytune &#8211; tune driver parameters for Cyclades-Z multiport serial card</p>
<h2>Synopsis</h2>
<p><code>cytune</code> [<code>-q</code> [<code>-i</code> <i>interval</i>]] [{<code>-s</code>|<code>-S</code>} <i>value</i>] [<code>-g</code>|<code>-G</code>] [{<code>-t</code>|<code>-T</code>} <i>timeout</i>] <i>tty</i>&#8230;</p>
<h2>Description</h2>
<p><code>cytune</code> queries and modifies the interruption threshold for the Cyclades driver. Each serial line on a Cyclades card has a 12-byte FIFO for input (and another 12-byte FIFO for output). The &quot;threshold&quot; specifies how many input characters must be present in the FIFO before an interruption is raised. When a Cyclades tty is opened, this threshold is set to a default value based on baud rate:</p>
<dl>
<dd>&nbsp;<wbr>Baud&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Threshold 50-4800 10<br />
 9600 8<br />
 19200 4<br />
 38400 2<br />
 57600-150000 1</dl>
<p> If the threshold is set too low, the large number of interruptions can load the machine and decrease overall system throughput. If the threshold is set too high, the FIFO buffer can overflow, and characters will be lost. Slower machines, however, may not be able to deal with the interrupt load, and will require that the threshold be adjusted upwards. If the cyclades driver was compiled with <code>ENABLE_MONITORING</code> defined, the cytune command can be used with the <code>-q</code> option to report interrupts over the monitoring interval and characters transferred over the monitoring interval. It will also report the state of the FIFO. The maximum number of characters in the FIFO when an interrupt occurred, the instantaneous count of characters in the FIFO, and how many characters are now in the FIFO are reported. This output might look like this:</p>
<dl>
<dd>/dev/cubC0: 830 ints, 9130 chars; fifo: 11 threshold, 11 max, 11 now </p>
<p>166.259866 interrupts/second, 1828.858521 characters/second</dl>
<p> This output indicates that for this monitoring period, the interrupts were always being handled within one character time, because <code>max</code> never rose above <code>threshold</code>. This is good, and you can probably run this way, provided that a large number of samples come out this way. You will lose characters if you overrun the FIFO, as the Cyclades hardware does not seem to support the RTS RS-232 signal line for hardware flow control from the DCE to the DTE. In query mode <code>cytune</code> will produce a summary report when ended with a SIGINT or when the threshold or timeout is changed. There may be a responsiveness vs. throughput tradeoff. The Cyclades card, at the higher speeds, is capable of putting a very high interrupt load on the system. This will reduce the amount of CPU time available for other tasks on your system. However, the time it takes to respond to a single character may be increased if you increase the threshold. This might be noticed by monitoring <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8) times on a SLIP link controlled by a Cyclades card. If your SLIP link is generally used for interactive work such as <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1), you may want to leave the threshold low, so that characters are responded to as quickly as possible. If your SLIP link is generally used for file transfer, WWW, and the like, setting the FIFO to a high value is likely to reduce the load on your system while not significantly affecting throughput. Alternatively, see the <code>-t</code> or <code>-T</code> options to adjust the time that the cyclades waits before flushing its buffer. Units are 5ms. If you are running a mouse on a Cyclades port, it is likely that you would want to maintain the threshold and timeout at a low value. </p>
<h2>Options</h2>
<dl>
<dt><code>-s</code><i> value</i></p>
<dd>Set the current threshold to <i>value</i> characters. Note that if the <i>tty</i> is not being held open by another process, the threshold will be reset on the next open. Only values between 1 and 12, inclusive, are permitted.</p>
<dt><code>-t</code><i> value</i></p>
<dd>Set the current flush timeout to <i>value</i> units. Note that if the <i>tty</i> is not being held open by another process, the threshold will be reset on the next open. Only values between 0 and 255, inclusive, are permitted. Setting <i>value</i> to zero forces the default, currently 0x20 (160ms), but soon to be 0x02 (10ms). Units are 5 ms.</p>
<dt><code>-g</code></p>
<dd>Get the current threshold and timeout.</p>
<dt><code>-S</code><i> value</i></p>
<dd>Set the default threshold to <i>value</i> characters. When the <i>tty</i> is next opened, this value will be used instead of the default. Only values between 1 and 12, inclusive, are permitted.</p>
<dt><code>-T</code><i> value</i></p>
<dd>Set the default flush timeout to <i>value</i> units. When the <i>tty</i> is next opened, this value will be used instead of the default. If <i>value</i> is zero, then the the value will default to 0x20 (160ms), soon to be 0x02 (10ms).</p>
<dt><code>-G</code></p>
<dd>Get the default threshold and flush timeout values.</p>
<dt><code>-q</code></p>
<dd>Gather statistics about the <i>tty</i>. The results are only valid if the Cyclades driver has been compiled with <code>ENABLE_MONITORING</code> defined. This is probably not the default.</p>
<dt><code>-i</code><i> interval</i></p>
<dd>Statistics will be gathered every <i>interval</i> seconds.</dl>
<h2>Bugs</h2>
<p>If you run two copies of <code>cytune</code> at the same time to report statistics about the same port, the &#8216;ints&#8217;, &#8216;chars&#8217;, and &#8216;max&#8217; value will be reset and not reported correctly. <code>cytune</code> should prevent this, but does not.</p>
<h2>Files</h2>
<p><i>/dev/ttyC[0-8]</i><br />
 <i>/dev/cubC[0-8]</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setserial/">setserial</a></code>(8)</p>
<h2>Availability</h2>
<p>The cytune command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a></p>
