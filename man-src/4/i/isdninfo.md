---
title: "isdninfo(4)"
name: "isdninfo"
section: "4"
letter: "i"
url: "/docs/linux/man/4-isdninfo/"
description: "isdninfo – ISDN status device"
---

<p>isdninfo &#8211; ISDN status device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/isdn.h&gt;</code></pre>
<h2>Description</h2>
<p><i>/dev/isdninfo</i> is a character device with major number <code>45</code> and minor number <code>255</code>. It delivers status information from the Linux <font SIZE="-1">ISDN</font> subsystem to user level.</p>
<h2>Data Format</h2>
<p>When reading from this device, the current status of the Linux <font SIZE="-1">ISDN</font> subsystem is delivered in <code>6</code> lines of text. Each line starts with a tag string followed by a colon and whitespace. After that the status values are appended separated by whitespace.</p>
<dl>
<dt><code>idmap</code></dt>
<dd>is the tag of the first line. In this line for every virtual channel, the Id-string of the corresponding lowlevel driver is shown. If no driver is loaded, a &#8211; (hyphen) is shown.</dd>
<dt><code>chmap</code></dt>
<dd>is the tag of line 2. In this line for every virtual channel, the channel number of the corresponding lowlevel driver is shown. If no driver is loaded, -1 is shown.</dd>
<dt><code>drmap</code></dt>
<dd>is the tag of line 3. In this line for every virtual channel, the index number of the corresponding lowlevel driver is shown. If no driver is loaded, -1 is shown.</dd>
<dt><code>usage</code></dt>
<dd>is the tag of line 4. In this line for every virtual channel, the current usage is shown. The following usage constants are defined:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ISDN_USAGE_NONE</code> (0)</dt>
<dd>Unused channel</dd>
<dt><code>ISDN_USAGE_RAW</code> (1)</dt>
<dd>Channel used by raw device (currently unsupported)</dd>
<dt><code>ISDN_USAGE_MODEM</code> (2)</dt>
<dd>Channel used by some ttyI</dd>
<dt><code>ISDN_USAGE_NET</code> (3)</dt>
<dd>Channel used by an ISDN net-interface</dd>
<dt><code>ISDN_USAGE_VOICE</code> (4)</dt>
<dd>Channel used by some ttyI in voice mode.</dd>
<dt><code>ISDN_USAGE_EXCLUSIVE</code> (64)</dt>
<dd>Channel exclusively preserved for a net-interface. This value is logically or&#8217;ed with one of the other codes.</dd>
<dt><code>ISDN_USAGE_OUTGOING</code> (128)</dt>
<dd>Channel is used outgoing. This value is logically or&#8217;ed with one of the other codes. It is set, when dialling is started and reset, when either dialling failed or after hangup. Therefore, it is <code>not</code> always an indicator for an established connection. To get a reliable indicator for an established connection, the driver flags (see below) have to be inspected also.</dd></dl>
</dl>
<dt><code>flags</code></dt>
<dd>is the tag of line 5. In this line for every driver slot, it&#8217;s B-Channel status is shown. If no driver is registered in a slot, a ? is shown. For every established B-Channel of the driver, a bit is set in the shown value. The driver&#8217;s first channel is mapped to bit 0, the second channel to bit 1 and so on.</dd>
<dt><code>phone</code></dt>
<dd>is the tag of line 6. In this line for every virtual channel, the remote phone number is shown if the channel is active. A ??? is shown, if the channel is inactive. </dd>
</dl>
<h2>Blocking Behaviour</h2>
<p>After opening the device, at most 6 lines can be read by a user process. After that, the user process is blocked. Whenever a status change happens, the process is allowed to read 6 more lines, starting with line one.</p>
<h2>Ioctl Functions</h2>
<p>Currently, there are two ioctl calls supported:</p>
<dl>
<dt><code>IIOCGETDVR</code></dt>
<dd>Get Revision information.</dd>
<dl>
<dd>Returns an unsigned long value <i>v</i>, representing various user level interface revisions, where</dd>
<dl>
<dt><code>(</code><i>v</i><code> &amp; 0xff)</code></dt>
<dd>is the revision of the modem-register info, available via ioctl on <i>/dev/isdnctrl</i>.</dd>
<dt><code>((</code><i>v</i><code> &gt;&gt; 8) &amp; 0xff)</code></dt>
<dd>is the revision of the net-interface config data, available via ioctl on <i>/dev/isdnctrl</i>. and</dd>
<dt><code>((</code><i>v</i><code> &gt;&gt; 16) &amp; 0xff)</code></dt>
<dd>is the revision of the data delivered via <i>/dev/isdninfo</i> itself.</dd></dl>
</dl>
<dt><code>IIOCGETCPS</code></dt>
<dd>Get transfer statistics.</dd>
<dl>
<dd>Returns the number of bytes transferred so far for all virtual channels. The third parameter should be a pointer to an array of unsigned long of size ISDN_MAX_CHANNELS * 2. This array is filled with the byte counter values upon return.</dd></dl>
</dl>
<h2>Other Constants</h2>
<p>There are some more useful constants defined in <i>/usr/include/linux/isdn.h</i>:</p>
<dl>
<dt><code>ISDN_TTY_MAJOR</code></dt>
<dd>The major device number of <i>/dev/ttyI</i>.</dd>
<dt><code>ISDN_TTYAUX_MAJOR</code></dt>
<dd>The major device number of <i>/dev/cui</i>.</dd>
<dt><code>ISDN_MAJOR</code></dt>
<dd>The major device number of <i>/dev/isdnctrl</i>, <i>/dev/isdninfo</i>, <i>/dev/ippp</i> and <i>/dev/isdn</i></dd>
<dt><code>ISDN_MAX_DRIVERS</code></dt>
<dd>The number of driver slots.</dd>
<dt><code>ISDN_MAX_CHANNELS</code></dt>
<dd>The number of virtual channels.</dd>
<dt><code>ISDN_MINOR_CTRL</code></dt>
<dd>The minor device number of <i>/dev/isdnctrl0</i>.</dd>
<dt><code>ISDN_MINOR_CTRLMAX</code></dt>
<dd>The minor device number of <i>/dev/isdnctrl63</i>.</dd>
<dt><code>ISDN_MINOR_PPP</code></dt>
<dd>The minor device number of <i>/dev/ippp0</i>.</dd>
<dt><code>ISDN_MINOR_PPPMAX</code></dt>
<dd>The minor device number of <i>/dev/ippp64</i>.</dd>
<dt><code>ISDN_MINOR_STATUS</code></dt>
<dd>The minor device number of <i>/dev/isdninfo</i>.</dd></dl>
<p> Other constants, necessary for ioctl&#8217;s on <i>/dev/isdnctrl</i> are listed in <code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4).</p>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4), <code>icnctrl</code>(4). </p>
