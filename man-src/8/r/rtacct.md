---
title: "rtacct(8)"
name: "rtacct"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtacct/"
description: "nstat, rtacct – network statistics tools."
---

<p>nstat, rtacct &#8211; network statistics tools.</p>
<h2>Synopsis</h2>
<p>Usage: nstat [ -h?vVzrnasd:t:jp ] [ PATTERN [ PATTERN ] ]<br />
 Usage: rtacct [ -h?vVzrnasd:t: ] [ ListOfRealms ] </p>
<h2>Description</h2>
<p><code>nstat</code> and <code>rtacct</code> are simple tools to monitor kernel snmp counters and network interface statistics. <code>nstat</code> can filter kernel snmp counters by name with one or several specified wildcards. Wildcards are case-insensitive and can include special symbols <code>?</code> and <code>*</code> </p>
<h2>Options</h2>
<p><code>-h, &#8211;help</code> Print help</p>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Print version</p>
<dt><code>-z, &#8211;zeros</code></p>
<dd>Dump zero counters too. By default they are not shown.</p>
<dt><code>-r, &#8211;reset</code></p>
<dd>Reset history.</p>
<dt><code>-n, &#8211;nooutput</code></p>
<dd>Do not display anything, only update history.</p>
<dt><code>-a, &#8211;ignore</code></p>
<dd>Dump absolute values of counters. The default is to calculate increments since the previous use.</p>
<dt><code>-s, &#8211;noupdate</code></p>
<dd>Do not update history, so that the next time you will see counters including values accumulated to the moment of this measurement too.</p>
<dt><code>-j, &#8211;json</code></p>
<dd>Display results in JSON format.</p>
<dt><code>-p, &#8211;pretty</code></p>
<dd>When combined with <code>&#8211;json</code>, pretty print the output.</p>
<dt><code>-d, &#8211;scan &lt;INTERVAL&gt;</code></p>
<dd>Run in daemon mode collecting statistics. &lt;INTERVAL&gt; is interval between measurements in seconds.</p>
<dt><code>-t, &#8211;interval &lt;INTERVAL&gt;</code></p>
<dd>Time interval to average rates. Default value is 60 seconds. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-lnstat/">lnstat</a>(8) </p>
