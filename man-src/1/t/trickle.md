---
title: "trickle(1)"
name: "trickle"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trickle/"
description: "trickle – a lightweight userspace bandwidth shaper"
---

<h2>NAME</h2>
<p> <code>trickle</code> &#8211; a lightweight userspace bandwidth shaper</p>
<h2>SYNOPSIS</h2>
<p> <code>trickle</code> [-<code>h </code> ] [-<code>v</code> ] [-<code>V</code> ] [-<code>s</code> ] [-<code>d </code><i>rate</i> ] [-<code>u </code><i>rate</i> ] [-<code>w </code><i>length</i> ] [-<code>t </code><i>time</i> ] [-<code>l </code><i>length</i> ] [-<code>n </code><i>path</i> ] <i>command &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>trickle</code> is a userspace bandwidth manager. Currently, <code>trickle</code> supports the shaping of any SOCK_STREAM (see <a href="/docs/linux/man/2-socket/">socket</a>(2)) connection established via the <a href="/docs/linux/man/2-socket/">socket</a>(2) interface. Furthermore, <code>trickle</code> will not work with statically linked executables, nor with <a href="/docs/linux/man/2-setuid/">setuid</a>(2) executables. <code>trickle</code> is highly configurable; download and upload rates can be set separately, or in an aggregate fashion. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-h</code></p>
<dd> Displays help.</p>
<dt><code>-v</code></p>
<dd> Increases the verbosity level (can be specified multiple times).</p>
<dt><code>-V</code></p>
<dd> Prints version.</p>
<dt><code>-s</code></p>
<dd> Runs trickle in standalone mode, independent of <a href="/docs/linux/man/8-trickled/">trickled</a>(8).</p>
<dt><code>-d </code><i>rate</i></p>
<dd> Limit the download bandwidth consumption to <i>rate</i> KB/s.</p>
<dt><code>-u </code><i>rate</i></p>
<dd> Limit the upload bandwidth consumption to <i>rate</i> KB/s.</p>
<dt><code>-w </code><i>length</i></p>
<dd> Set peak detection window size to <i>length</i> KB. This determines how aggressive <code>trickle</code> is at eliminating bandwidth consumption peaks. Lower values will be more aggressive, but may also result in over shaping. The default value (512 KB) is usually sufficient.</p>
<dt><code>-t </code><i>seconds</i></p>
<dd> Set smoothing time to <i>seconds </i> s. The smoothing time determines with what intervals <code>trickle</code> will try to let the application transcieve data. Smaller values will result in a more continuous (smooth) session, while larger values may produce bursts in the sending and receiving data. Smaller values (0.1 &#8211; 1 s) are ideal for interactive applications while slightly larger values (1 &#8211; 10 s) are better for applications that need bulk transfer.</p>
<dt><code>-l </code><i>length</i></p>
<dd> Set smoothing length to <i>length </i> KB. The smoothing length is a fallback of the smoothing time. If <code>trickle</code> cannot meet the requested smoothing time, it will instead fall back on sending <i>length</i> KB of data. The default value is 10 KB.</p>
<dt><code>-n </code><i>path</i></p>
<dd> Use <a href="/docs/linux/man/8-trickled/">trickled</a>(8) socket <i>path </i> to communicate with <a href="/docs/linux/man/8-trickled/">trickled</a>(8). By default, <i>/tmp/.trickled.sock</i> is used.</dl>
</dl>
<h2>EXAMPLES</h2>
<p> <code>trickle -u 10 -d 20 ncftp</code> </p>
<p> Launch <a href="/docs/linux/man/1-ncftp/">ncftp</a>(1) limiting its upload capacity to 10 KB/s, and download capacity at 20 KB/s.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-trickled/">trickled</a>(8), <a href="/docs/linux/man/3-syslog/">syslog</a>(3), <a href="/docs/linux/man/2-socket/">socket</a>(2), <a href="/docs/linux/man/4-netintro/">netintro</a>(4)</p>
<h2>AUTHORS</h2>
<p> <code>trickle</code> has been developed by Marius Aamodt Eriksen Aq marius [at] monkey.org .</p>
<h2>BUGS</h2>
<p> Does not support executables utilizing <a href="/docs/linux/man/2-kqueue/">kqueue</a>(2). Does not support statically linked executables. </p>
<h2>Index</h2>
