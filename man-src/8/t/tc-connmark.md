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
<dt><code>zone</code><i> u16_zone_index</i></p>
<dd>Specify the conntrack zone when doing conntrack lookups for packets. <i>u16_zone_index</i> is a 16bit unsigned decimal value.</p>
<dt><i>CONTROL</i></p>
<dd>How to continue after executing this action.</p>
<dl>
<dd>
<dl>
<dt><code>reclassify</code></p>
<dd>Restarts classification by jumping back to the first filter attached to this action&#8217;s parent.</p>
<dt><code>pipe</code></p>
<dd>Continue with the next action, this is the default.</p>
<dt><code>drop</code></p>
<dd><code>shot</code> Packet will be dropped without running further actions.</p>
<dt><code>continue</code></p>
<dd>Continue classification with next filter in line.</p>
<dt><code>pass</code></p>
<dd>Return to calling qdisc for packet processing. This ends the classification process.</dl>
</dl>
<dt><code>index</code><i> u32_index </i></p>
<dd>Specify an index for this action in order to being able to identify it in later commands. <i>u32_index</i> is a 32bit unsigned decimal value.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
