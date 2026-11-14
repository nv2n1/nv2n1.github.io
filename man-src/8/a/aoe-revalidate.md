---
title: "aoe-revalidate(8)"
name: "aoe-revalidate"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-revalidate/"
description: "aoe-revalidate – revalidate the disk size of an aoe device"
---

<p>aoe-revalidate &#8211; revalidate the disk size of an aoe device</p>
<h2>Synopsis</h2>
<pre><code>aoe-revalidate e{major}.{minor}</code></pre>
<h2>Description</h2>
<p>The <i>aoe-revalidate</i> command tells the aoe driver to revalidate the disk size of an open aoe device. Normally the aoe driver will only acknowledge changes in an aoe device&#8217;s disk size when the aoe device is not open. </p>
<p> It should be noted that if an aoe device&#8217;s disk size shrinks in revalidation any users may become hopelessly confused when their resumed I/O starts to fail.</p>
<h2>Example</h2>
<pre>nai# aoe-stat | grep e1.9
 e1.9 82.348GB eth0 up 
nai# &lt; /dev/etherd/e1.9 sleep 600 &amp;
[1] 13006
nai# aoe-revalidate e1.9
nai# aoe-stat | grep e1.9
 e1.9 164.696GB eth0 up </pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8).</p>
<h2>Author</h2>
<p>Sam Hopkins (sah [at] coraid.com)</p>
