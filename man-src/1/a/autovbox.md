---
title: "autovbox(1)"
name: "autovbox"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autovbox/"
description: "autovbox – ISDN voice box (sound converter)"
---

<h2>NAME</h2>
<p> autovbox &#8211; ISDN voice box (sound converter)</p>
<h2>SYNOPSIS</h2>
<p> autovbox [-2 | -3 | -4 | -h | -v] [-n name] [-p phone] [-l location]</p>
<h2>DESCRIPTION</h2>
<p> Convert .au files (Sun audio format) on standard input into vbox files (vbox audio header) on standard output. autovbox is a link to <a href="/docs/linux/man/1-vboxcnvt/">vboxcnvt</a>(1).</p>
<h2>OPTIONS</h2>
<p> Autovbox reads from stdin and writes to stdout.</p>
<dl>
<dt><code>-2, &#8211;adpcm-2</code></dt>
<dd> Convert to ADPCM 2 format.</dd>
<dt><code>-3, &#8211;adpcm-3</code></dt>
<dd> Convert to ADPCM 3 format.</dd>
<dt><code>-4, &#8211;adpcm-4</code></dt>
<dd> Convert to ADPCM 4 format.</dd>
<dt><code>-u, &#8211;ulaw</code></dt>
<dd> Convert to ulaw format (default).</dd>
<dt><code>-n NAME, &#8211;name NAME</code></dt>
<dd> Name to write into the header.</dd>
<dt><code>-p, &#8211;phone PHONE</code></dt>
<dd> Telephone number to write into the header.</dd>
<dt><code>-l LOCATION, &#8211;location LOCATION</code></dt>
<dd> City to write into the header.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show version of program.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rmdtovbox/">rmdtovbox</a></i>(1), <i><a href="/docs/linux/man/1-vboxtoau/">vboxtoau</a></i>(1), <i><a href="/docs/linux/man/1-vboxmode/">vboxmode</a></i>(1), <i><a href="/docs/linux/man/1-vboxcnvt/">vboxcnvt</a></i>(1), <i><a href="/docs/linux/man/5-vbox/">vbox</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.<br />
 Now maintained by Paul Slootman &lt;paul [at] debian.org&gt;. </p>
