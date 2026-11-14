---
title: "unbound-checkconf(8)"
name: "unbound-checkconf"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unbound-checkconf/"
description: "unbound-checkconf – Check unbound configuration file for errors."
---

<p>unbound-checkconf &#8211; Check unbound configuration file for errors.</p>
<h2>Synopsis</h2>
<p><code>unbound-checkconf</code> [<code>-h</code>] [<code>-o</code> <i>option</i>] [<i>cfgfile</i>]</p>
<h2>Description</h2>
<p><code>Unbound-checkconf</code> checks the configuration file for the <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8) DNS resolver for syntax and other errors. The config file syntax is described in <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5). </p>
<p> The available options are:</p>
<dl>
<dt><code>-h</code></p>
<dd>Show the version and commandline option help.</p>
<dt><code>-o</code><i> option</i></p>
<dd>If given, after checking the config file the value of this option is printed to stdout. For &quot;&quot; (disabled) options an empty line is printed.</p>
<dt><i>cfgfile</i></p>
<dd>The config file to read with settings for unbound. It is checked. If omitted, the config file at the default location is checked.</dl>
<h2>Exit Code</h2>
<p>The unbound-checkconf program exits with status code 1 on error, 0 for a correct config file.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/unbound/unbound.conf</i></p>
<dd>unbound configuration file.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). </p>
