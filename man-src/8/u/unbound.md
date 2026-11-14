---
title: "unbound(8)"
name: "unbound"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unbound/"
description: "unbound – Unbound DNS validating resolver 1.4.20."
---

<p><code>unbound</code> &#8211; Unbound DNS validating resolver 1.4.20.</p>
<h2>Synopsis</h2>
<p><code>unbound</code> [<code>-h</code>] [<code>-d</code>] [<code>-v</code>] [<code>-c</code> <i>cfgfile</i>]</p>
<h2>Description</h2>
<p><code>Unbound </code> is an implementation of a DNS resolver, that does caching and DNSSEC validation. </p>
<p> The available options are:</p>
<dl>
<dt><code>-h</code></p>
<dd>Show the version and commandline option help.</p>
<dt><code>-c</code><i> cfgfile</i></p>
<dd>Set the config file with settings for unbound to read instead of reading the file at the default location, /etc/unbound/unbound.conf. The syntax is described in <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5).</p>
<dt><code>-d</code></p>
<dd>Debug flag, do not fork into the background, but stay attached to the console. This flag will also delay writing to the logfile until the thread-spawn time. So that most config and setup errors appear on stderr.</p>
<dt><code>-v</code></p>
<dd>Increase verbosity. If given multiple times, more information is logged. This is in addition to the verbosity (if any) from the config file.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/8-unbound-checkconf/">unbound-checkconf</a></i>(8).</p>
<h2>Authors</h2>
<p><code>Unbound</code> developers are mentioned in the CREDITS file in the distribution.</p>
