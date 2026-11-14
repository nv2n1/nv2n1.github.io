---
title: "aoe-flush(8)"
name: "aoe-flush"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-flush/"
description: "aoe-flush – flush the down devices out of the aoe driver"
---

<p>aoe-flush &#8211; flush the down devices out of the aoe driver</p>
<h2>Synopsis</h2>
<pre><code>aoe-flush [-a]</code>
<code>aoe-flush dev1 [dev2 ...]</code></pre>
<h2>Description</h2>
<p>The <i>aoe-flush</i> command tells the aoe driver to remove devices from the system and forget about them. Normally the aoe driver will remember all devices it has seen until the module is unloaded. By default, <i>aoe-flush</i> will only flush downed devices. With the <code>-a</code> flag all devices are candidates for removal. </p>
<p> <i>aoe-flush</i> will not remove devices that are in use. This includes devices in the closewait state or those in the process of being installed. </p>
<p> By specifying a series of specific aoe devices, e.g., <code>e7.0 e3.2</code>, it is possible to ask the aoe driver to forget these devices. This feature may be convenient after a temporary AoE target is no longer being used.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>The <code>-a</code> option tells the aoe driver to forget all unused devices.</dl>
<h2>Example</h2>
<pre>nai# aoe-stat | grep e12.0
 e12.0 0.000GB eth1 down 
nai# aoe-flush
nai# aoe-stat | grep e12.0</pre>
<h2>Bugs</h2>
<p>Flushed devices may reappear when they are discovered by the periodic discovery beacon. <i>aoe-discover</i> may be used to force this behaviour.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8).</p>
<h2>Author</h2>
<p>Sam Hopkins (sah [at] coraid.com)</p>
