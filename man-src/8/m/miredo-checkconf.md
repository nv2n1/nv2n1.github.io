---
title: "miredo-checkconf(8)"
name: "miredo-checkconf"
section: "8"
letter: "m"
url: "/docs/linux/man/8-miredo-checkconf/"
description: "miredo-checkconf – Miredo configuration file syntax checking tool"
---

<p>miredo-checkconf &#8211; Miredo configuration file syntax checking tool</p>
<h2>Synopsis</h2>
<p><code>miredo-checkconf</code> [<code>config_file</code>] </p>
<h2>Descripton</h2>
<p><code>miredo-checkconf</code> checks the syntax of a configuration file for Miredo. miredo-checkconf exits with an error code if the syntax was found to be incorrect, contained unused directives or if the file could not be opened.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display some help and exit. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd>Display program version and exit. </p>
<dt><code>config_file</code></p>
<dd>This optional argument specifies the path to the configuration file to be checked. If not given, the default /etc/miredo/miredo.conf will be assumed. </p>
</dl>
<h2>Bugs</h2>
<p>miredo-checkconf cannot check the syntax of a configuration file for miredo-server. </p>
<h2>Files</h2>
<dl>
<dt><i>/etc/miredo/miredo.conf</i></p>
<dd>The default configuration file. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-miredo-conf/">miredo.conf</a>(5), <a href="/docs/linux/man/8-miredo/">miredo</a>(8) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/miredo/">http://www.remlab.net/miredo/</a></p>
