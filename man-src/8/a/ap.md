---
title: "ap(8)"
name: "ap"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ap/"
description: "ap – parse addresses RFC 822-style"
---

<p>ap &#8211; parse addresses RFC 822-style</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/libexec/nmh/ap</code> [<code>-form</code> <i>formatfile</i>] [<code>-format</code> <i>string</i>] [<code>-width</code> <i>columns</i>] [<code>-version</code>] [<code>-help</code>] <i>addrs</i> &#8230;</dt></dl>
<h2>Description</h2>
<p><code>Ap</code></p>
<dd>is a program that parses addresses according to the ARPA Internet standard. It also understands many non-standard formats. It is useful for seeing how <code>nmh</code> will interpret an address. </dd>
<p> The <code>ap</code> program treats each argument as one or more addresses, and prints those addresses out in the official RFC 822 format. Hence, it is usually best to enclose each argument in quotes for the shell. </p>
<p> To override the output format used by <code>ap</code>, the <code>-format</code> <i>string</i> or <code>-format</code> <i>file</i> switches are used. This permits individual fields of the address to be extracted with ease. The string is simply a format string, and the file is simply a format file. See <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for the details. </p>
<p> In addition to the standard escapes, <code>ap</code> also recognizes the following additional escape: </p>
<dl>
<dd>
<pre><i>Escape Returns Description</i>
error string A diagnostic if the parse failed
</dd></dl></pre>
<p>Here is the default format string used by <code>ap</code>: </p>
<dl>
<dd>%&lt;{error}%{error}: %{text}%|%(putstr(proper{text}))%&gt;</dd></dl>
<p> which says that if an error was detected, print the error, a `:&#8217;, and the address in error. Otherwise, output the RFC 822-proper format of the address.</p>
<h2>Files</h2>
<dl>
<dt>$HOME/.mh_profile</dt>
<dd>The user&#8217;s profile.</dd>
<dt>/etc/nmh/mts.conf</dt>
<dd>The mts configuration file.</dd></dl>
<h2>Profile Components</h2>
<p>None</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-dp/">dp</a></i>(8) </p>
<p> <i>Standard for the Format of ARPA Internet Text Messages</i> (RFC 822)</p>
<h2>Defaults</h2>
<dl>
<dt>-format</dt>
<dd>As described above.</dd>
<dt>-width</dt>
<dd>The width of the terminal.</dd></dl>
<h2>Context</h2>
<p>None</p>
