---
title: "logsave(8)"
name: "logsave"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logsave/"
description: "logsave – save the output of a command in a logfile"
---

<p>logsave &#8211; save the output of a command in a logfile</p>
<h2>Synopsis</h2>
<p><code>logsave</code> [ <code>-asv</code> ] <i>logfile cmd_prog [ &#8230; ]</i></p>
<h2>Description</h2>
<p>The <code>logsave</code> program will execute <i>cmd_prog</i> with the specified argument(s), and save a copy of its output to <i>logfile</i>. If the containing directory for <i>logfile</i> does not exist, <code>logsave</code> will accumulate the output in memory until it can be written out. A copy of the output will also be written to standard output. </p>
<p> If <i>cmd_prog</i> is a single hyphen (&#8216;-&#8216;), then instead of executing a program, <code>logsave</code> will take its input from standard input and save it in <i>logfile</i> </p>
<p> <code>logsave</code> is useful for saving the output of initial boot scripts until the /var partition is mounted, so the output can be written to /var/log.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>This option will cause the output to be appended to <i>logfile</i>, instead of replacing its current contents.</p>
<dt><code>-s</code></p>
<dd>This option will cause <code>logsave</code> to skip writing to the log file text which is bracketed with a control-A (ASCII 001 or Start of Header) and control-B (ASCII 002 or Start of Text). This allows progress bar information to be visible to the user on the console, while not being written to the log file.</p>
<dt><code>-v</code></p>
<dd>This option will make <code>logsave</code> to be more verbose in its output to the user.</dl>
<h2>Author</h2>
<p>Theodore Ts&#8217;o (tytso [at] mit.edu)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8) </p>
