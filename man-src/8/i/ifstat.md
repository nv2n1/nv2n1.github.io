---
title: "ifstat(8)"
name: "ifstat"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifstat/"
description: "ifstat – handy utility to read network interface statistics"
---

<p>ifstat &#8211; handy utility to read network interface statistics</p>
<h2>Synopsis</h2>
<p><code>ifstat</code> [ <i>OPTIONS</i> ] [ <i>INTERFACE_LIST</i> ] </p>
<pre><code>INTERFACE_LIST := INTERFACE_LIST | interface</code></pre>
<h2>Description</h2>
<p><code>ifstat</code> neatly prints out network interface statistics. The utility keeps records of the previous data displayed in history files and by default only shows difference between the last and the current call. Location of the history files defaults to /tmp/.ifstat.u$UID but may be overridden with the IFSTAT_HISTORY environment variable. Similarly, the default location for xstat (extended stats) is /tmp/.&lt;xstat name&gt;_ifstat.u$UID.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show version of program.</p>
<dt><code>-a, &#8211;ignore</code></p>
<dd>Ignore the history file.</p>
<dt><code>-d, &#8211;scan=SECS</code></p>
<dd>Sample statistics every SECS second.</p>
<dt><code>-e, &#8211;errors</code></p>
<dd>Show errors.</p>
<dt><code>-n, &#8211;nooutput</code></p>
<dd>Don&#8217;t display any output. Update the history file only.</p>
<dt><code>-r, &#8211;reset</code></p>
<dd>Reset history.</p>
<dt><code>-s, &#8211;noupdate</code></p>
<dd>Don&#8217;t update the history file.</p>
<dt><code>-t, &#8211;interval=SECS</code></p>
<dd>Report average over the last SECS seconds.</p>
<dt><code>-z, &#8211;zeros</code></p>
<dd>Show entries with zero activity.</p>
<dt><code>-x, &#8211;extended=TYPE</code></p>
<dd>Show extended stats of TYPE. Supported types are: </p>
<p> <code>cpu_hits</code> &#8211; Counts only packets that went via the CPU. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>IFSTAT_HISTORY</code></p>
<dd>If set, it&#8217;s value is interpreted as alternate history file path.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Author</h2>
<p>ifstat was written by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;. </p>
<p> This manual page was written by Petr Sabata &lt;contyk [at] redhat.com&gt;.</p>
