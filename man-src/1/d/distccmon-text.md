---
title: "distccmon-text(1)"
name: "distccmon-text"
section: "1"
letter: "d"
url: "/docs/linux/man/1-distccmon-text/"
description: "distccmon-text – Displays current compilation jobs in text form."
---

<h2>NAME</h2>
<p> distccmon-text &#8211; Displays current compilation jobs in text form.</p>
<h2>SYNTAX</h2>
<p> distccmon-text [DELAY]</p>
<h2>DESCRIPTION</h2>
<p> Displays current compilation jobs in text form. distccmon-text must be run on the client machine, with the same setting for <i>DISTCC_DIR</i> (or home directory) as the user running the distcc client.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>DELAY</code></dt>
<dd> repeatedly updates after <i>delay</i> (fractional) seconds.</dd></dl>
<h2>OUTPUT FORMAT</h2>
<p> The output of distccmon-text contains one line for each job currently being compiled. Each line contains the following columns:</p>
<dl>
<dt><i>PID</i></dt>
<dd> ID of the distcc client process.</dd>
<dt><i>STATE</i></dt>
<dd> Identifies the phase of operation. In order these may be &quot;Startup&quot;, &quot;Blocked&quot;, &quot;Connected&quot;, &quot;Preprocess&quot;, &quot;Conect&quot;, &quot;Send&quot;, &quot;Receive&quot; and &quot;Done&quot;.</dd>
<dt><i>FILE</i></dt>
<dd> The input filename, if known.</dd>
<dt><i>HOST[SLOT]</i></dt>
<dd> The compile hostname. May be followed in square brackets by the slot index for that host.</dd></dl>
<p> When a delay is specified, each block of output is terminated by a blank line.</p>
<h2>EXAMPLES</h2>
<p> To display currently active jobs (updated every second):</p>
<dl>
<dt>
</dt><dd> distccmon-text 1</dd></dl>
<p> To display the status once:</p>
<dl>
<dt>
</dt><dd> distccmon-text</dd></dl>
<h2>AUTHORS</h2>
<p> distcc was written by Martin Pool &lt;mbp [at] sourcefrog.net&gt;, with the co-operation of many scholars including Wayne Davison, Frerich Raabe, Dimitri Papadopoulos and others noted in the NEWS file. Please report bugs to &lt;distcc [at] lists.samba.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-distccd/">distccd</a>(1), <a href="/docs/linux/man/1-ccache/">ccache</a>(1), <a href="/docs/linux/man/1-gcc/">gcc</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1) <a rel="nofollow" href="http://code.google.com/p/distcc/">http://code.google.com/p/distcc/</a> <a rel="nofollow" href="http://ccache.samba.org/">http://ccache.samba.org/</a> </p>
<h2>Index</h2>
