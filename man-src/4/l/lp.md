---
title: "lp(4)"
name: "lp"
section: "4"
letter: "l"
url: "/docs/linux/man/4-lp/"
description: "lp – line printer devices"
---

<p>lp &#8211; line printer devices</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/lp.h&gt;</code></pre>
<h2>Configuration</h2>
<p><code>lp</code>[0-2] are character devices for the parallel line printers; they have major number 6 and minor number 0-2. The minor numbers correspond to the printer port base addresses 0x03bc, 0x0378, and 0x0278. Usually they have mode 220 and are owned by user <i>root</i> and group <i>lp</i>. You can use printer ports either with polling or with interrupts. Interrupts are recommended when high traffic is expected, for example, for laser printers. For typical dot matrix printers, polling will usually be enough. The default is polling.</p>
<h2>Description</h2>
<p>The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls are supported:</p>
<dl>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPTIME, int </code><i>arg</i><code>)</code></p>
<dd>Sets the amount of time that the driver sleeps before rechecking the printer when the printer&#8217;s buffer appears to be filled to <i>arg</i>. If you have a fast printer, decrease this number; if you have a slow printer, then increase it. This is in hundredths of a second, the default 2 being 0.02 seconds. It influences only the polling driver.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPCHAR, int </code><i>arg</i><code>)</code></p>
<dd>Sets the maximum number of busy-wait iterations which the polling driver does while waiting for the printer to get ready for receiving a character to <i>arg</i>. If printing is too slow, increase this number; if the system gets too slow, decrease this number. The default is 1000. It influences only the polling driver.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPABORT, int </code><i>arg</i><code>)</code></p>
<dd>If <i>arg</i> is 0, the printer driver will retry on errors, otherwise it will abort. The default is 0.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPABORTOPEN, int </code><i>arg</i><code>)</code></p>
<dd>If <i>arg</i> is 0, <code><a href="/docs/linux/man/2-open/">open</a></code>(2) will be aborted on error, otherwise error will be ignored. The default is to ignore it.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPCAREFUL, int </code><i>arg</i><code>)</code></p>
<dd>If <i>arg</i> is 0, then the out-of-paper, offline, and error signals are required to be false on all writes, otherwise they are ignored. The default is to ignore them.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPWAIT, int </code><i>arg</i><code>)</code></p>
<dd>Sets the number of busy waiting iterations to wait before strobing the printer to accept a just-written character, and the number of iterations to wait before turning the strobe off again, to <i>arg</i>. The specification says this time should be 0.5 microseconds, but experience has shown the delay caused by the code is already enough. For that reason, the default value is 0. This is used for both the polling and the interrupt driver.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPSETIRQ, int </code><i>arg</i><code>)</code></p>
<dd>This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requires superuser privileges. It takes an <i>int</i> containing the new IRQ as argument. As a side effect, the printer will be reset. When <i>arg</i> is 0, the polling driver will be used, which is also default.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPGETIRQ, int *</code><i>arg</i><code>)</code></p>
<dd>Stores the currently used IRQ in <i>arg</i>.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPGETSTATUS, int *</code><i>arg</i><code>)</code></p>
<dd>Stores the value of the status port in <i>arg</i>. The bits have the following meaning: </p>
<table>
<tr VALIGN=top>
<td>LP_PBUSY</td>
<td>inverted busy input, active high
</td>
</tr>
<tr VALIGN=top>
<td>LP_PACK</td>
<td>unchanged acknowledge input, active low
</td>
</tr>
<tr VALIGN=top>
<td>LP_POUTPA</td>
<td>unchanged out-of-paper input, active high
</td>
</tr>
<tr VALIGN=top>
<td>LP_PSELECD</td>
<td>unchanged selected input, active high
</td>
</tr>
<tr VALIGN=top>
<td>LP_PERRORP</td>
<td>unchanged error input, active low
</td>
</tr>
</table>
<dd>Refer to your printer manual for the meaning of the signals. Note that undocumented bits may also be set, depending on your printer.</p>
<dt><code>int ioctl(int </code><i>fd</i><code>, LPRESET)</code></p>
<dd>Resets the printer. No argument is used.</dl>
<h2>Files</h2>
<p><i>/dev/lp*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/8-lpcntl/">lpcntl</a></code>(8), <code><a href="/docs/linux/man/8-tunelp/">tunelp</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
