---
title: "dp(8)"
name: "dp"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dp/"
description: "dp – parse dates RFC 822-style"
---

<p>dp &#8211; parse dates RFC 822-style</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/libexec/nmh/dp</code> [<code>-form</code> <i>formatfile</i>] [<code>-format</code> <i>string</i>] [<code>-width</code> <i>columns</i>] [<code>-version</code>] [<code>-help</code>] <i>dates</i> &#8230;</dl>
<h2>Description</h2>
<p><code>Dp</code></p>
<dd>is a program that parses dates according to the ARPA Internet standard. It also understands many non-standard formats, such as those produced by TOPS-20 sites and some UNIX sites using <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3). It is useful for seeing how <code>nmh</code> will interpret a date. </p>
<p> The <code>dp</code> program treats each argument as a single date, and prints the date out in the official RFC 822 format. Hence, it is usually best to enclose each argument in quotes for the shell. </p>
<p> To override the output format used by <code>dp</code>, the <code>-format</code> <i>string</i> or <code>-format</code> <i>file</i> switches are used. This permits individual fields of the address to be extracted with ease. The string is simply a format string and the file is simply a format file. See <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for the details. </p>
<p> Here is the default format string used by <code>dp</code>: </p>
<dl>
<dd>%&lt;(nodate{text})error: %{text}%|%(putstr(pretty{text}))%&gt;</dl>
<p> which says that if an error was detected, print the error, a `:&#8217;, and the date in error. Otherwise, output the RFC 822-proper format of the date.</p>
<h2>Files</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd>The user&#8217;s profile.</dl>
<h2>Profile Components</h2>
<p>None</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ap/">ap</a></i>(8), </p>
<p> <i>Standard for the Format of ARPA Internet Text Messages</i> (RFC 822)</p>
<h2>Defaults</h2>
<dl>
<dt>-format</p>
<dd>As described above.</p>
<dt>-width</p>
<dd>The width of the terminal.</dl>
<h2>Context</h2>
<p>None</p>
