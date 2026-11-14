---
title: "chicken-bug(1)"
name: "chicken-bug"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chicken-bug/"
description: "chicken-bug – generates a bug report from user input"
---

<h2 class="name">NAME</h2>
<p> chicken-bug &#8211; generates a bug report from user input</p>
<h2>SYNOPSIS</h2>
<p> <code>chicken-bug</code> [ <i>filename</i> | <i>OPTION &#8230;</i> ] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Show usage information. </p>
<dt><code>-to-stdout</code></p>
<dd> Write bug report to standard output instead of writing it to a file. </p>
<dt><code>&#8211;</code></p>
<dd> Read user input from standard input, even if files are given on the command line. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>chicken-bug</i> generates a bug report file that collects user-input, optional files and system information obtained from the installed CHICKEN executables and libraries. Non-option arguments given on the command line are inserted into the bug report. If no option is given, or if <code>&#8211;</code> has been passed on the command line, then a description of the problem is read from standard input, until EOF (CTRL-D) or a line consisting only of &quot;.&quot; (period) is read. </p>
<p> The bug report will be written to a file in the current directory, which should be sent to CHICKEN maintainers as it contains various useful bits of information that make it easier to classify the problem described. </p>
<p> Bug reports should be as detailed as possible. It is also very helpful to include code that reproduces the problem. The more detailed the input and the more thorough the description is, the easier you make it for the CHICKEN developers to help you. </p>
<h2>BUGS</h2>
<p> Submit bug reports by e-mail to <i>chicken-janitors [at] nongnu.org</i> </p>
<h2>AUTHOR</h2>
<p> The CHICKEN Team. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chicken/">chicken</a>(1)</code> </p>
<h2>Index</h2>
