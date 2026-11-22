---
title: "nstat(8)"
name: "nstat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nstat/"
description: "nstat, rtacct – network statistics tools."
---

<p>nstat, rtacct &#8211; network statistics tools.</p>
<h2>Synopsis</h2>
<p>Usage: nstat [ -h?vVzrnasd:t:jp ] [ PATTERN [ PATTERN ] ]<br/>
 Usage: rtacct [ -h?vVzrnasd:t: ] [ ListOfRealms ] </p>
<h2>Description</h2>
<p><code>nstat</code> and <code>rtacct</code> are simple tools to monitor kernel snmp counters and network interface statistics. <code>nstat</code> can filter kernel snmp counters by name with one or several specified wildcards. Wildcards are case-insensitive and can include special symbols <code>?</code> and <code>*</code> </p>
<h2>Options</h2>
<p><code>-h, &#8211;help</code> Print help</p>
<dl>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print version</dd>
<dt><code>-z, &#8211;zeros</code></dt>
<dd>Dump zero counters too. By default they are not shown.</dd>
<dt><code>-r, &#8211;reset</code></dt>
<dd>Reset history.</dd>
<dt><code>-n, &#8211;nooutput</code></dt>
<dd>Do not display anything, only update history.</dd>
<dt><code>-a, &#8211;ignore</code></dt>
<dd>Dump absolute values of counters. The default is to calculate increments since the previous use.</dd>
<dt><code>-s, &#8211;noupdate</code></dt>
<dd>Do not update history, so that the next time you will see counters including values accumulated to the moment of this measurement too.</dd>
<dt><code>-j, &#8211;json</code></dt>
<dd>Display results in JSON format.</dd>
<dt><code>-p, &#8211;pretty</code></dt>
<dd>When combined with <code>&#8211;json</code>, pretty print the output.</dd>
<dt><code>-d, &#8211;scan &lt;INTERVAL&gt;</code></dt>
<dd>Run in daemon mode collecting statistics. &lt;INTERVAL&gt; is interval between measurements in seconds.</dd>
<dt><code>-t, &#8211;interval &lt;INTERVAL&gt;</code></dt>
<dd>Time interval to average rates. Default value is 60 seconds. </dd>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-lnstat/">lnstat</a>(8) </p>
