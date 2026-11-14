---
title: "progress(1)"
name: "progress"
section: "1"
letter: "p"
url: "/docs/linux/man/1-progress/"
description: "progress – Coreutils Progress Viewer"
---

<h2 class="name">NAME</h2>
<p> progress &#8211; Coreutils Progress Viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>progress</code> [ <code>-qdwmM</code> ] [ <code>-W</code> <i>secs</i> ] [ <code>-c</code> <i>command</i> ] [ <code>-p</code> <i>pid</i> ]<br />
 <code>progress -v</code> | <code>&#8211;version</code><br />
 <code>progress -h</code> | <code>&#8211;help</code> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>progress</code> command. </p>
<p> This tool can be described as a Tiny, Dirty, Linux-Only C command that looks for coreutils basic commands (cp, mv, dd, tar, gzip/gunzip, cat, etc.) currently running on your system and displays the percentage of copied data. </p>
<p> It can now also estimate throughput (using flag <code>-w</code> ). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q (&#8211;quiet)</code></p>
<dd> hides all messages</p>
<dt><code>-d (&#8211;debug)</code></p>
<dd> shows all warning/error messages</p>
<dt><code>-w (&#8211;wait)</code></p>
<dd> estimate I/O throughput and estimated remaining time (slower display)</p>
<dt><code>-W (&#8211;wait-delay secs)</code></p>
<dd> wait &#8216;secs&#8217; seconds for I/O estimation (implies <code>-w</code> )</p>
<dt><code>-m (&#8211;monitor)</code></p>
<dd> loop while monitored processes are still running</p>
<dt><code>-M (&#8211;monitor-continuously)</code></p>
<dd> like monitor but never stop (similar to <code>watch progress</code> )</p>
<dt><code>-c (&#8211;command cmd)</code></p>
<dd> monitor only this command name (ex: firefox). This option can be used multiple times on the command line.</p>
<dt><code>-p (&#8211;pid id)</code></p>
<dd> monitor only this numeric process ID (ex: `pidof firefox`). This option can be used multiple times on the command line.</p>
<dt><code>-i (&#8211;ignore-file file)</code></p>
<dd> do not report a process for &#8216;file&#8217;. If the file does not exist yet, you must give a full and clean absolute path. This option can be used multiple times on the command line.</p>
<dt><code>-o (&#8211;open-mode {r|w})</code></p>
<dd> report only files opened for read or write by the process. This option is useful when you want to monitor only output files (or input ones) of a process.</p>
<dt><code>-v (&#8211;version)</code></p>
<dd> show program version and exit</p>
<dt><code>-h (&#8211;help)</code></p>
<dd> display help message and exit </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> It&#8217;s possible to give permanent options using PROGRESS_ARGS environment variable. See example below. Command line arguments take precedence over environment. </p>
<h2>EXAMPLES</h2>
<p> Continuously monitor all current and upcoming instances of coreutils commands</p>
<dl>
<dt>
<dd>
<p> <code>watch progress -q</code> </p>
</dl>
<p> See how your download is progressing</p>
<dl>
<dt>
<dd>
<p> <code>watch progress -wc firefox</code> </p>
</dl>
<p> Look at your Web server activity</p>
<dl>
<dt>
<dd>
<p> <code>progress -c httpd</code> </p>
</dl>
<p> Launch and monitor any heavy command using $!</p>
<dl>
<dt>
<dd>
<p> <code>cp bigfile newfile &amp; progress -mp $!</code> </p>
</dl>
<p> Use environment variable to set permanent (multiple) arguments</p>
<dl>
<dt>
<dd>
<p> <code>export PROGRESS_ARGS=&#8217;-M &#8211;ignore-file ~/.xsession-errors&#8217;</code> </p>
</dl>
<h2>BUGS</h2>
<p> Please report bugs at: <a rel="nofollow" href="http://github.com/Xfennec/progress/issues">http://github.com/Xfennec/progress/issues</a> </p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://github.com/Xfennec/progress">http://github.com/Xfennec/progress</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Zimmermann &lt;bugs [at] vdm-design.de&gt;, for the openSUSE project (and may be used by others). </p>
<h2>Index</h2>
