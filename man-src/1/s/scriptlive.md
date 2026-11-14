---
title: "scriptlive(1)"
name: "scriptlive"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scriptlive/"
description: "scriptlive – re-run session typescripts, using timing information"
---

<h2 class="name">NAME</h2>
<p> scriptlive &#8211; re-run session typescripts, using timing information </p>
<h2>SYNOPSIS</h2>
<p> <code>scriptlive</code> [options] [<code>-t</code>] <i>timingfile</i> [<code>-I</code>|<code>-B</code>] <i>typescript</i></p>
<h2>DESCRIPTION</h2>
<p> This program re-runs a typescript, using stdin typescript and timing information to ensure that input happens in the same rhythm as it originally appeared when the script was recorded. </p>
<p> The <code>session is executed</code> in a newly created pseudoterminal with the user&#8217;s $SHELL (or defaults to <i>/bin/bash</i>). </p>
<p> <code>Be careful!</code> Do not forget that the typescript may contains arbitrary commands. It is recommended to use <code>&quot;scriptreplay &#8211;stream in &#8211;log-in typescript&quot;</code> (or with <code>&#8211;log-io</code> instead of <code>&#8211;log-in</code>) to verify the typescript before it is executed by <code>scriptlive</code>. </p>
<p> The timing information is what script1 outputs to file specified by <code>&#8211;log-timing</code>. The typescript has to contain stdin information and it is what script1 outputs to file specified by <code>&#8211;log-in</code> or <code>&#8211;log-io</code>.</p>
<h2>OPTIONS</h2>
<p> <code>-I</code>, <code>&#8211;log-in</code> <i>file</i></p>
<dl>
<dt>
<dd> File containing <code>script</code>&#8216;s terminal input.</dl>
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
<dd> Aliased to <code>-t</code>, maintained for compatibility with <code><a href="/docs/linux/man/1-script/">script</a></code>(1) command-line options.</dl>
<p> <code>-d</code>, <code>&#8211;divisor</code> <i>number</i></p>
<dl>
<dt>
<dd> Speed up the replay displaying this <i>number</i> of times. The argument is a floating-point number. It&#8217;s called divisor because it divides the timings by this factor. This option overrides old-style arguments.</dl>
<p> <code>-m</code>, <code>&#8211;maxdelay</code> <i>number</i></p>
<dl>
<dt>
<dd> Set the maximum delay between updates to <i>number</i> of seconds. The argument is a floating-point number. This can be used to avoid long pauses in the typescript replay.</dl>
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
% script-- log - timing file.tm-- log - in script.in Script started, file is script.out % date&lt;etc, etc&gt; % exit Script done, file is script.out % scriptlive-- log - timing file.tm-- log - in script.in
</code></pre>
</dl>
<h2>AUTHORS</h2>
<h2>COPYRIGHT</h2>
<p> Copyright © 2019 Karel Zak </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<p> Released under the GNU General Public License version 2 or later.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-script/">script</a></code>(1), <code><a href="/docs/linux/man/1-scriptreplay/">scriptreplay</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>scriptlive</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
