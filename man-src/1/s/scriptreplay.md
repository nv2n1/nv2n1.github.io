---
title: "scriptreplay(1)"
name: "scriptreplay"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scriptreplay/"
description: "scriptreplay – play back typescripts, using timing information"
---

<h2 class="name">NAME</h2>
<p> scriptreplay &#8211; play back typescripts, using timing information </p>
<h2>SYNOPSIS</h2>
<p> <code>scriptreplay</code> [options] [<code>-t</code>] <i>timingfile</i> [<i>typescript</i> [<i>divisor</i>]]</p>
<h2>DESCRIPTION</h2>
<p> This program replays a typescript, using timing information to ensure that output happens in the same rhythm as it originally appeared when the script was recorded. </p>
<p> The replay simply displays the information again; the programs that were run when the typescript was being recorded are <code>not run again</code>. Since the same information is simply being displayed, <code>scriptreplay</code> is only guaranteed to work properly if run on the same type of terminal the typescript was recorded on. Otherwise, any escape characters in the typescript may be interpreted differently by the terminal to which <code>scriptreplay</code> is sending its output. </p>
<p> The timing information is what <code><a href="/docs/linux/man/1-script/">script</a></code>(1) outputs to file specified by <code>&#8211;log-timing</code>. </p>
<p> By default, the typescript to display is assumed to be named <i>typescript</i>, but other filenames may be specified, as the second parameter or with option <code>&#8211;log-out</code>. </p>
<p> If the third parameter or <code>&#8211;divisor</code> is specified, it is used as a speed-up multiplier. For example, a speed-up of 2 makes <code>scriptreplay</code> go twice as fast, and a speed-up of 0.1 makes it go ten times slower than the original session.</p>
<h2>OPTIONS</h2>
<p> <code>-I</code>, <code>&#8211;log-in</code> <i>file</i></p>
<dl>
<dt>
<dd> File containing <code>script</code>&#8216;s terminal input.</dl>
<p> <code>-O</code>, <code>&#8211;log-out</code> <i>file</i></p>
<dl>
<dt>
<dd> File containing <code>script</code>&#8216;s terminal output.</dl>
<p> <code>-B</code>, <code>&#8211;log-io</code> <i>file</i></p>
<dl>
<dt>
<dd> File containing <code>script</code>&#8216;s terminal output and input.</dl>
<p> <code>-t</code>, <code>&#8211;timing</code> <i>file</i></p>
<dl>
<dt>
<dd> File containing <code>script</code>&#8216;s timing output. This option overrides old-style arguments.</dl>
<p> <code>-T</code>, <code>&#8211;log-timing</code> <i>file</i></p>
<dl>
<dt>
<dd> This is an alias for <code>-t</code>, maintained for compatibility with <code><a href="/docs/linux/man/1-script/">script</a></code>(1) command-line options.</dl>
<p> <code>-s</code>, <code>&#8211;typescript</code> <i>file</i></p>
<dl>
<dt>
<dd> File containing <code>script</code>&#8216;s terminal output. Deprecated alias to <code>&#8211;log-out</code>. This option overrides old-style arguments.</dl>
<p> <code>-c</code>, <code>&#8211;cr-mode</code> <i>mode</i></p>
<dl>
<dt>
<dd> Specifies how to use the CR (0x0D, carriage return) character from log files. The default mode is <i>auto</i>, in this case CR is replaced with line break for stdin log, because otherwise <code>scriptreplay</code> would overwrite the same line. The other modes are <i>never</i> and <i>always</i>.</dl>
<p> <code>-d</code>, <code>&#8211;divisor</code> <i>number</i></p>
<dl>
<dt>
<dd> Speed up the replay displaying this <i>number</i> of times. The argument is a floating-point number. It&#8217;s called divisor because it divides the timings by this factor. This option overrides old-style arguments.</dl>
<p> <code>-m</code>, <code>&#8211;maxdelay</code> <i>number</i></p>
<dl>
<dt>
<dd> Set the maximum delay between updates to <i>number</i> of seconds. The argument is a floating-point number. This can be used to avoid long pauses in the typescript replay.</dl>
<p> <code>&#8211;summary</code></p>
<dl>
<dt>
<dd> Display details about the session recorded in the specified timing file and exit. The session has to be recorded using <i>advanced</i> format (see <code><a href="/docs/linux/man/1-script/">script</a></code>(1)) option <code>&#8211;logging-format</code> for more details).</dl>
<p> <code>-x</code>, <code>&#8211;stream</code> <i>type</i></p>
<dl>
<dt>
<dd> Forces <code>scriptreplay</code> to print only the specified stream. The supported stream types are <i>in</i>, <i>out</i>, <i>signal</i>, or <i>info</i>. This option is recommended for multi-stream logs (e.g., <code>&#8211;log-io</code>) in order to print only specified data.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
% script-- log - timing file.tm-- log - out script.out Script started, file is script.out % ls&lt;etc, etc&gt; % exit Script done, file is script.out % scriptreplay-- log - timing file.tm-- log - out script.out
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> The original <code>scriptreplay</code> program was written by The program was re-written in C by and</p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2008 James Youngman </p>
<p> Copyright © 2008-2019 Karel Zak </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<p> Released under the GNU General Public License version 2 or later.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-script/">script</a></code>(1), <code><a href="/docs/linux/man/1-scriptlive/">scriptlive</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>scriptreplay</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
