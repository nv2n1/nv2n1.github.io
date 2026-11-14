---
title: "adjtime_config(5)"
name: "adjtime_config"
section: "5"
letter: "a"
url: "/docs/linux/man/5-adjtime_config/"
description: "adjtime_config – information about hardware clock setting and drift factor"
---

<p>adjtime_config &#8211; information about hardware clock setting and drift factor</p>
<h2>Synopsis</h2>
<p><i>/etc/adjtime</i></p>
<h2>Description</h2>
<p>The file <i>/etc/adjtime</i> contains descriptive information about the hardware mode clock setting and clock drift factor. The file is read and write by <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8); and read by programs like rtcwake to get RTC time mode. </p>
<p> The file is usually located in <i>/etc</i>, but tools like <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) or <code><a href="/docs/linux/man/8-rtcwake/">rtcwake</a></code>(8) can use alternative location by command line options if write access to <i>/etc</i> is unwanted. The default clock mode is &quot;UTC&quot; if the file is missing. </p>
<p> The Hardware Clock is usually not very accurate. However, much of its inaccuracy is completely predictable &#8211; it gains or loses the same amount of time every day. This is called systematic drift. The util <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) keeps the file <i>/etc/adjtime</i>, that keeps some historical information. For more details see &quot;<code>The Adjust Function</code>&quot; and &quot;<code>The Adjtime File</code>&quot; sections from <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) man page. </p>
<p> The format of the adjtime file is, in ASCII.</p>
<h3>First line</h3>
<p>Three numbers, separated by blanks: </p>
<p> <code>drift factor</code></p>
<dl>
<dd>the systematic drift rate in seconds per day (floating point decimal)</dl>
<p> <code>last adjust time</code></p>
<dl>
<dd>the resulting number of seconds since 1969 UTC of most recent adjustment or calibration (decimal integer)</dl>
<p> <code>adjustment status</code></p>
<dl>
<dd>zero (for compatibility with <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8)) as a floating point decimal</dl>
<h3>Second line</h3>
<p><code>last calibration time</code></p>
<dl>
<dd>The resulting number of seconds since 1969 UTC of most recent calibration. Zero if there has been no calibration yet or it is known that any previous calibration is moot (for example, because the Hardware Clock has been found, since that calibration, not to contain a valid time). This is a decimal integer.</dl>
<h3>Third line</h3>
<p><code>clock mode</code></p>
<dl>
<dd>Supported values are <code>UTC</code> or <code>LOCAL</code>. Tells whether the Hardware Clock is set to Coordinated Universal Time or local time. You can always override this value with options on the <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) command line.</dl>
<h2>Files</h2>
<p><i>/etc/adjtime</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/8-rtcwake/">rtcwake</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p><code>adjtime_config</code> is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
