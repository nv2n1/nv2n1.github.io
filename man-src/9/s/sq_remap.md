---
title: "sq_remap(9)"
name: "sq_remap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sq_remap/"
description: "sq_remap – Map a physical address through the Store Queues"
---

<p>sq_remap &#8211; Map a physical address through the Store Queues</p>
<h2>Synopsis</h2>
<pre><code>unsigned long sq_remap(unsigned long phys, unsigned int size, const char *name, pgprot_t prot);</code></pre>
<h2>Arguments</h2>
<p><i>phys</i></p>
<dl>
<dd>
<dd>Physical address of mapping.</dl>
<p> <i>size</i></p>
<dl>
<dd>Length of mapping.</dl>
<p> <i>name</i></p>
<dl>
<dd>User invoking mapping.</dl>
<p> <i>prot</i></p>
<dl>
<dd>Protection bits.</dl>
<h2>Description</h2>
<p>Remaps the physical address <i>phys</i> through the next available store queue address of <i>size</i> length. <i>name</i> is logged at boot time as well as through the sysfs interface.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
