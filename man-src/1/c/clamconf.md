---
title: "clamconf(1)"
name: "clamconf"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clamconf/"
description: "clamconf – Clam AntiVirus configuration utility"
---

<h2>NAME</h2>
<p> clamconf &#8211; Clam AntiVirus configuration utility</p>
<h2>SYNOPSIS</h2>
<p> clamconf [options]</p>
<h2>DESCRIPTION</h2>
<p> clamconf displays the values of configuration options.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help and exit.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display software version and exit.</dd>
<dt><code>-c DIR, &#8211;config-dir DIR</code></dt>
<dd> Search for configuration files clamd.conf and freshclam.conf in DIR.</dd>
<dt><code>-n, &#8211;non-default</code></dt>
<dd> Only print non-default settings.</dd>
<dt><code>-g CONFIG_NAME, &#8211;generate-config=CONFIG_NAME</code></dt>
<dd> Generate example configuration file.</dd></dl>
<h2>CREDITS</h2>
<p> The idea of this tool is based on Postfix&#8217;s postconf. clamconf was created under pressure from Tomasz Papszun ;-)</p>
<h2>AUTHOR</h2>
<p> Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5), <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5) </p>
