---
title: "racoon2-spmd(8)"
name: "racoon2-spmd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-racoon2-spmd/"
description: "spmd – Manages IPsec Security Policy for racoon2"
---

<p><code>spmd</code> &#8211; Manages IPsec Security Policy for racoon2</p>
<h2>Synopsis</h2>
<p><code>spmd</code> [<i>option</i>]</p>
<h2>Description</h2>
<p><code>spmd</code> manages IPsec Security Policy for racoon2 key management daemons(ikev2, kinkd). And behaves as a local DNS proxy server if you set on in racoon2 configuration file.</p>
<dl>
<dt>The following options are available:</p>
<dd>
<dt><code>-V | &#8211;version</code></p>
<dd>Show spmd version.</p>
<dt><code>-f | &#8211;config-file [FILE]</code></p>
<dd>Specify racoon2 configuration file name <code>FILE</code>.</p>
<dt><code>-d | &#8211;debug</code></p>
<dd>Increase debug level.</p>
<dt><code>-D | &#8211;DEBUG [1-3]</code></p>
<dd>Specify debug level directly (recommend &#8216;5&#8217;).</p>
<dt><code>-F | &#8211;foreground</code></p>
<dd>Run foreground.</p>
<dt><code>-k | &#8211;kill</code></p>
<dd>Kill running spmd.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Show help message.</dl>
<h2>Files</h2>
<p><i>racoon2.conf</i> <i>/var/run/spmd.pid</i></p>
<h2>Authors</h2>
<p>WIDE Project, racoon2 project &lt;<a rel="nofollow" href="http://www.racoon2.wide.ad.jp/">http://www.racoon2.wide.ad.jp/</a>&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-spmdctl/">spmdctl</a>(8) <a href="/docs/linux/man/8-iked/">iked</a>(8) <a href="/docs/linux/man/8-kinkd/">kinkd</a>(8) <a href="/docs/linux/man/5-racoon2-conf/">racoon2.conf</a>(5) <a href="/docs/linux/man/7-racoon2/">racoon2</a>(7) </p>
