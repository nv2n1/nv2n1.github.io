---
title: "npcd(8)"
name: "npcd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-npcd/"
description: "npcd – Nagios Performance C Daemon"
---

<p>npcd &#8211; Nagios Performance C Daemon</p>
<h2>Synopsis</h2>
<p><code>npcd</code> [ <code>-d | &#8211;daemon</code> ] ( <code>-f | &#8211;config</code> ) <i>&lt;configfile&gt; </i></p>
<h2>Description</h2>
<p>The <code>npcd</code> is a daemon processing nagios performance data. </p>
<p> For more information you can visit pnp4nagios website:</p>
<dl>
<dd><a rel="nofollow" href="http://docs.pnp4nagios.org/">http://docs.pnp4nagios.org/</a></dl>
<p> and SourceForge project:</p>
<dl>
<dd><a rel="nofollow" href="http://pnp4nagios.sourceforge.net">http://pnp4nagios.sourceforge.net</a></dl>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;daemon</p>
<dd>Run npcd</code> as daemon in the background.</p>
<dt><code>-f, &#8211;config</code> <i>&lt;configfile&gt;</p>
<dd>Path to the </i><code>npcd</code> config file (typically /etc/pnp4nagios/npcd.cfg).</dl>
<h2>Return Value</h2>
<p>On success starting <code>npcd</code> 0 is returned.</p>
<h2>Errors</h2>
<p>On error starting <code>npcd</code> 1 is returned.</p>
<h2>Files</h2>
<pre><i>/etc/pnp4nagios/npcd.cfg</i> default config file</pre>
<h2>Authors</h2>
<p>Joerg Linge &lt;pitchfork [at] pnp4nagios.org&gt;, Hendrik Baecker &lt;andurin [at] process-zero.de&gt;</p>
