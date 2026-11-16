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
<dt>The following options are available:</dt>
<dd>
</dd><dt><code>-V | &#8211;version</code></dt>
<dd>Show spmd version.</dd>
<dt><code>-f | &#8211;config-file [FILE]</code></dt>
<dd>Specify racoon2 configuration file name <code>FILE</code>.</dd>
<dt><code>-d | &#8211;debug</code></dt>
<dd>Increase debug level.</dd>
<dt><code>-D | &#8211;DEBUG [1-3]</code></dt>
<dd>Specify debug level directly (recommend &#8216;5&#8217;).</dd>
<dt><code>-F | &#8211;foreground</code></dt>
<dd>Run foreground.</dd>
<dt><code>-k | &#8211;kill</code></dt>
<dd>Kill running spmd.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd>Show help message.</dd></dl>
<h2>Files</h2>
<p><i>racoon2.conf</i> <i>/var/run/spmd.pid</i></p>
<h2>Authors</h2>
<p>WIDE Project, racoon2 project &lt;<a rel="nofollow" href="http://www.racoon2.wide.ad.jp/">http://www.racoon2.wide.ad.jp/</a>&gt;</p>
<h2>See Also</h2>
<p>spmdctl(8) iked(8) kinkd(8) racoon2.conf(5) racoon2(7) </p>
