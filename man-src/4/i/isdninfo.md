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
<dt><code>idmap</code></p>
<dd>is the tag of the first line. In this line for every virtual channel, the Id-string of the corresponding lowlevel driver is shown. If no driver is loaded, a &#8211; (hyphen) is shown.</p>
<dt><code>chmap</code></p>
<dd>is the tag of line 2. In this line for every virtual channel, the channel number of the corresponding lowlevel driver is shown. If no driver is loaded, -1 is shown.</p>
<dt><code>drmap</code></p>
<dd>is the tag of line 3. In this line for every virtual channel, the index number of the corresponding lowlevel driver is shown. If no driver is loaded, -1 is shown.</p>
<dt><code>usage</code></p>
<dd>is the tag of line 4. In this line for every virtual channel, the current usage is shown. The following usage constants are defined:</p>
<dl>
<dd>
<dl>
<dt><code>ISDN_USAGE_NONE</code> (0)</p>
<dd>Unused channel</p>
<dt><code>ISDN_USAGE_RAW</code> (1)</p>
<dd>Channel used by raw device (currently unsupported)</p>
<dt><code>ISDN_USAGE_MODEM</code> (2)</p>
<dd>Channel used by some ttyI</p>
<dt><code>ISDN_USAGE_NET</code> (3)</p>
<dd>Channel used by an ISDN net-interface</p>
<dt><code>ISDN_USAGE_VOICE</code> (4)</p>
<dd>Channel used by some ttyI in voice mode.</p>
<dt><code>ISDN_USAGE_EXCLUSIVE</code> (64)</p>
<dd>Channel exclusively preserved for a net-interface. This value is logically or&#8217;ed with one of the other codes.</p>
<dt><code>ISDN_USAGE_OUTGOING</code> (128)</p>
<dd>Channel is used outgoing. This value is logically or&#8217;ed with one of the other codes. It is set, when dialling is started and reset, when either dialling failed or after hangup. Therefore, it is <code>not</code> always an indicator for an established connection. To get a reliable indicator for an established connection, the driver flags (see below) have to be inspected also.</dl>
</dl>
<dt><code>flags</code></p>
<dd>is the tag of line 5. In this line for every driver slot, it&#8217;s B-Channel status is shown. If no driver is registered in a slot, a ? is shown. For every established B-Channel of the driver, a bit is set in the shown value. The driver&#8217;s first channel is mapped to bit 0, the second channel to bit 1 and so on.</p>
<dt><code>phone</code></p>
<dd>is the tag of line 6. In this line for every virtual channel, the remote phone number is shown if the channel is active. A ??? is shown, if the channel is inactive. </p>
</dl>
<h2>Blocking Behaviour</h2>
<p>After opening the device, at most 6 lines can be read by a user process. After that, the user process is blocked. Whenever a status change happens, the process is allowed to read 6 more lines, starting with line one.</p>
<h2>Ioctl Functions</h2>
<p>Currently, there are two ioctl calls supported:</p>
<dl>
<dt><code>IIOCGETDVR</code></p>
<dd>Get Revision information.</p>
<dl>
<dd>Returns an unsigned long value <i>v</i>, representing various user level interface revisions, where</p>
<dl>
<dt><code>(</code><i>v</i><code> &amp; 0xff)</code></p>
<dd>is the revision of the modem-register info, available via ioctl on <i>/dev/isdnctrl</i>.</p>
<dt><code>((</code><i>v</i><code> &gt;&gt; 8) &amp; 0xff)</code></p>
<dd>is the revision of the net-interface config data, available via ioctl on <i>/dev/isdnctrl</i>. and</p>
<dt><code>((</code><i>v</i><code> &gt;&gt; 16) &amp; 0xff)</code></p>
<dd>is the revision of the data delivered via <i>/dev/isdninfo</i> itself.</dl>
</dl>
<dt><code>IIOCGETCPS</code></p>
<dd>Get transfer statistics.</p>
<dl>
<dd>Returns the number of bytes transferred so far for all virtual channels. The third parameter should be a pointer to an array of unsigned long of size ISDN_MAX_CHANNELS * 2. This array is filled with the byte counter values upon return.</dl>
</dl>
<h2>Other Constants</h2>
<p>There are some more useful constants defined in <i>/usr/include/linux/isdn.h</i>:</p>
<dl>
<dt><code>ISDN_TTY_MAJOR</code></p>
<dd>The major device number of <i>/dev/ttyI</i>.</p>
<dt><code>ISDN_TTYAUX_MAJOR</code></p>
<dd>The major device number of <i>/dev/cui</i>.</p>
<dt><code>ISDN_MAJOR</code></p>
<dd>The major device number of <i>/dev/isdnctrl</i>, <i>/dev/isdninfo</i>, <i>/dev/ippp</i> and <i>/dev/isdn</i></p>
<dt><code>ISDN_MAX_DRIVERS</code></p>
<dd>The number of driver slots.</p>
<dt><code>ISDN_MAX_CHANNELS</code></p>
<dd>The number of virtual channels.</p>
<dt><code>ISDN_MINOR_CTRL</code></p>
<dd>The minor device number of <i>/dev/isdnctrl0</i>.</p>
<dt><code>ISDN_MINOR_CTRLMAX</code></p>
<dd>The minor device number of <i>/dev/isdnctrl63</i>.</p>
<dt><code>ISDN_MINOR_PPP</code></p>
<dd>The minor device number of <i>/dev/ippp0</i>.</p>
<dt><code>ISDN_MINOR_PPPMAX</code></p>
<dd>The minor device number of <i>/dev/ippp64</i>.</p>
<dt><code>ISDN_MINOR_STATUS</code></p>
<dd>The minor device number of <i>/dev/isdninfo</i>.</dl>
<p> Other constants, necessary for ioctl&#8217;s on <i>/dev/isdnctrl</i> are listed in <code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4).</p>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4), <code><a href="/docs/linux/man/4-icnctrl/">icnctrl</a></code>(4). </p>
