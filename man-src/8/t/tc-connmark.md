---
title: "tc-connmark(8)"
name: "tc-connmark"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-connmark/"
description: "connmark – netfilter connmark retriever action"
---

<p>connmark &#8211; netfilter connmark retriever action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action connmark </code>[<code> zone</code> <i>u16_zone_index</i> ] [ <i>CONTROL</i> ] [ <code>index</code><i> u32_index </i> ] </p>
<pre><code>CONTROL := { reclassify | pipe | drop | continue | ok }</code></pre>
<h2>Description</h2>
<p>The connmark action is used to restore the connection&#8217;s mark value into the packet&#8217;s fwmark.</p>
<h2>Options</h2>
<dl>
<dt><code>zone</code><i> u16_zone_index</i></dt>
<dd>Specify the conntrack zone when doing conntrack lookups for packets. <i>u16_zone_index</i> is a 16bit unsigned decimal value.</dd>
<dt><i>CONTROL</i></dt>
<dd>How to continue after executing this action.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>reclassify</code></dt>
<dd>Restarts classification by jumping back to the first filter attached to this action&#8217;s parent.</dd>
<dt><code>pipe</code></dt>
<dd>Continue with the next action, this is the default.</dd>
<dt><code>drop</code></dt>
<dd><code>shot</code> Packet will be dropped without running further actions.</dd>
<dt><code>continue</code></dt>
<dd>Continue classification with next filter in line.</dd>
<dt><code>pass</code></dt>
<dd>Return to calling qdisc for packet processing. This ends the classification process.</dd></dl>
</dl>
<dt><code>index</code><i> u32_index </i></dt>
<dd>Specify an index for this action in order to being able to identify it in later commands. <i>u32_index</i> is a 32bit unsigned decimal value.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
