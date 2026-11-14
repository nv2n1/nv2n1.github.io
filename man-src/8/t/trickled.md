---
title: "trickled(8)"
name: "trickled"
section: "8"
letter: "t"
url: "/docs/linux/man/8-trickled/"
description: "trickled – userspace bandwidth manager daemon"
---

<p><code>trickled</code> &#8211; userspace bandwidth manager daemon</p>
<h2>Synopsis</h2>
<p><code>trickled</code> [-<code>h</code> ] [-<code>v</code> ] [-<code>V</code> ] [-<code>f</code> ] [-<code>s</code> ] [-<code>d </code><i>rate</i> ] [-<code>u </code><i>rate</i> ] [-<code>t </code><i>seconds</i> ] [-<code>l </code><i>length</i> ] [-<code>p </code><i>priority</i> ] [-<code>c </code><i>file</i> ] [-<code>n </code><i>path</i> ] [-<code>N </code><i>seconds</i> ] [-<code>w </code><i>size</i> ]</p>
<h2>Description</h2>
<p><code>trickled</code> is a userspace bandwidth manager daemon. <code>trickled</code> manages several <a href="/docs/linux/man/1-trickle/">trickle</a>(1) sessions at a time, shaping across multiple sessions. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-v</code></p>
<dd>Increases the verbosity level (can be specified multiple times).</p>
<dt><code>-V</code></p>
<dd>Prints version.</p>
<dt><code>-f</code></p>
<dd>Runs <code>trickled</code> in the foreground.</p>
<dt><code>-s</code></p>
<dd>Uses syslog for all output (instead of stderr).</p>
<dt><code>-d </code><i>rate</i></p>
<dd>Limit the download bandwidth consumption to <i>rate</i> KB/s.</p>
<dt><code>-u </code><i>rate</i></p>
<dd>Limit the upload bandwidth consumption to <i>rate</i> KB/s.</p>
<dt><code>-t </code><i>seconds</i></p>
<dd>Set smoothing time to <i>seconds </i> s. The smoothing time determines with what intervals <code>trickled</code> will try to let the application transcieve data. Smaller values will result in a more continuous (smooth) session, while larger values may produce bursts in the sending and receiving data. Smaller values (0.1 &#8211; 1 s) are ideal for interactive applications while slightly larger values (1 &#8211; 10 s) are better for applications that need bulk transfer. This parameter is customizable on a per-application basis via trickled.conf5. The default value is 5 s.</p>
<dt><code>-l </code><i>length</i></p>
<dd>Set smoothing length to <i>length </i> KB. The smoothing length is a fallback of the smoothing time. If <code>trickled</code> cannot meet the requested smoothing time, it will instead fall back on sending <i>length</i> KB of data. The default value is 10 KB.</p>
<dt><code>-p </code><i>priority</i></p>
<dd>Set default priority to <i>priority</i></p>
<dt><code>-c </code><i>file</i></p>
<dd>Use the configuration file <i>file</i> This file must be of the format documented in trickled.conf5.</p>
<dt><code>-n </code><i>path</i></p>
<dd>Set socket name to <i>path</i> By default, <code>trickled</code> uses <i>/tmp/.trickled.sock</i></p>
<dt><code>-N </code><i>seconds</i></p>
<dd>Notifies user of total bandwidth consumption every <i>seconds</i> s.</p>
<dt><code>-w </code><i>size</i></p>
<dd>Set peak detection window size to <i>size</i> KB. This determines how aggressive <code>trickled</code> is at eliminating bandwidth consumption peaks. Lower values will be more aggressive, but may also result in over shaping. The default value (512 KB) is usually sufficient.</dl>
</dl>
<h2>Examples</h2>
<p><code>trickled -u 10 -d 20</code> </p>
<p> Limit aggregate <a href="/docs/linux/man/1-trickle/">trickle</a>(1) upload bandwidth consumption to 10 KB/s and download consumption to 20 KB/s.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-trickle/">trickle</a>(1), trickled.conf5, <a href="/docs/linux/man/3-syslog/">syslog</a>(3), <a href="/docs/linux/man/4-netintro/">netintro</a>(4)</p>
<h2>Authors</h2>
<p><code>trickled</code> has been developed by Marius Aamodt Eriksen Aq marius [at] monkey.org .</p>
