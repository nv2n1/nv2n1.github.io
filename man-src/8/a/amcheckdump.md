---
title: "amcheckdump(8)"
name: "amcheckdump"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcheckdump/"
description: "amcheckdump – check the results of an Amanda dump"
---

<p>amcheckdump &#8211; check the results of an Amanda dump</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcheckdump</code> [&#8211;timestamp|-t&nbsp;<wbr><i>timestamp</i>] [&#8211;verbose] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i></dl>
<h2>Description</h2>
<p><code>Amcheckdump</code></p>
<dd>verifies Amanda dump images by reading them from storage volume(s) and verifying that the images can be parsed by the appropriate application (if available). For example, a GNUTAR image is passed to GNU Tar for parsing, and any errors (e.g., corrupt or missing data) are noted. </p>
<p> The application runs on the most recent dump or, if <i>&#8211;timestamp</i> is specified, on the most recent dump with that timestamp. Note that the verification is local to the Amanda server; if the dump application is not available, or is configured differently on the server than on the client, then the verification will most likely fail. </p>
<p> If a changer is available, it is used to load the required tapes. Otherwise, the application interactively requests the tapes. </p>
<p> See the &quot;<code>CONFIGURATION OVERRIDE</code>&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) for information on the -o option.</p>
<h2>Example</h2>
<pre># check the most recent dump
amcheckdump MYCONFIG
# check a specific dump from back in '78
amcheckdump MYCONFIG --timestamp 19780615</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amcheck/">amcheck</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Ian Turner</code> &lt;ian [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
