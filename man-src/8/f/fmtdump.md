---
title: "fmtdump(8)"
name: "fmtdump"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fmtdump/"
description: "fmtdump – decode nmh format files"
---

<p>fmtdump &#8211; decode nmh format files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/libexec/nmh/fmtdump</code> [<code>-form</code> <i>formatfile</i>] [<code>-format</code> <i>string</i>] [<code>-version</code>] [<code>-help</code>]</dt></dl>
<h2>Description</h2>
<p><code>Fmtdump</code></p>
<dd>is a program that parses an <code>nmh</code> format file and produces a pseudo-language listing of the how <code>nmh</code> interprets the file. This is useful when debugging a complicated format file. </dd>
<p> The <code>-format</code> <i>string</i> and <code>-form</code> <i>formatfile</i> switches may be used to specify a format string or format file to read. The string is simply a format string and the file is simply a format file. See <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for the details.</p>
<h2>Files</h2>
<dl>
<dt>$HOME/.mh_profile</dt>
<dd>The user&#8217;s profile.</dd>
<dt>/etc/nmh/scan.default</dt>
<dd>The default format file.</dd></dl>
<h2>Profile Components</h2>
<dl>
<dt>Path:</dt>
<dd>To determine the user&#8217;s nmh directory.</dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5), <i>mh-sequences</i>(8)</p>
<h2>Context</h2>
<p>None</p>
