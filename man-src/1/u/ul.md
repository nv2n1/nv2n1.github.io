---
title: "ul(1)"
name: "ul"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ul/"
description: "ul – do underlining"
---

<h2 class="name">NAME</h2>
<p> ul &#8211; do underlining </p>
<h2>SYNOPSIS</h2>
<p> <code>ul</code> [options] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>ul</code> reads the named files (or standard input if none are given) and translates occurrences of underscores to the sequence which indicates underlining for the terminal in use, as specified by the environment variable <code>TERM</code>. The <i>terminfo</i> database is read to determine the appropriate sequences for underlining. If the terminal is incapable of underlining but is capable of a standout mode, then that is used instead. If the terminal can overstrike, or handles underlining automatically, <code>ul</code> degenerates to <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1). If the terminal cannot underline, underlining is ignored.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>&#8211;indicated</code></p>
<dl>
<dt>
<dd> Underlining is indicated by a separate line containing appropriate dashes `-&#8216;; this is useful when you want to look at the underlining which is present in an <code>nroff</code> output stream on a crt-terminal.</dl>
<p> <code>-t</code>, <code>-T</code>, <code>&#8211;terminal</code> <i>terminal</i></p>
<dl>
<dt>
<dd> Override the environment variable <code>TERM</code> with the specified <i>terminal</i> type.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variable is used: </p>
<p> <code>TERM</code></p>
<dl>
<dt>
<dd> The <code>TERM</code> variable is used to relate a tty device with its device capability description (see <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5)). <code>TERM</code> is set at login time, either by the default terminal type specified in <i>/etc/ttys</i> or as set during the login process by the user in their <i>login</i> file (see <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3)).</dl>
<h2>HISTORY</h2>
<p> The <code>ul</code> command appeared in 3.0BSD.</p>
<h2>BUGS</h2>
<p> <code>nroff</code> usually outputs a series of backspaces and underlines intermixed with the text to indicate underlining. No attempt is made to optimize the backward motion.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-colcrt/">colcrt</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>ul</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
