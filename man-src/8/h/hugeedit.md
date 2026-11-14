---
title: "hugeedit(8)"
name: "hugeedit"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hugeedit/"
description: "hugeedit – Set default policy for backing text and data with hugepages"
---

<p>hugeedit &#8211; Set default policy for backing text and data with hugepages</p>
<h2>Synopsis</h2>
<p><code>hugeedit binary</code><br />
 <code>hugeedit [options] binary</code></p>
<h2>Description</h2>
<p><code>hugectl</code> runs processes with a specific policy for backing memory regions with hugepages. Ordinarily when processes are relinked with <code>libhugetlbfs</code> using the recommended linking method, either <code>hugectl</code> is required on each execution or environment variables must be set for each execution. <code>hugeedit</code> can be used to set bits in the ELF header that determine if the text or data segments are backed by default without further intervention. If no arguments are specified, <code>hugeedit</code> will display what the current defaults for each segment in a binary are. The available options are</p>
<dl>
<dt><code>&#8211;text</code></p>
<dd>Back the text segments of the binary by default.</p>
<dt><code>&#8211;data</code></p>
<dd>Back the data segments of the binary by default</p>
<dt><code>&#8211;disable</code></p>
<dd>Back all segments using small pages by default </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1),</i> <i><a href="/docs/linux/man/7-libhugetlbfs/">libhugetlbfs</a>(7),</i> <i><a href="/docs/linux/man/8-hugectl/">hugectl</a>(8)</i></p>
<h2>Authors</h2>
<p>libhugetlbfs was written by various people on the libhugetlbfs-devel mailing list.</p>
