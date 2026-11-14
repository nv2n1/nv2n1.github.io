---
title: "migspeed(8)"
name: "migspeed"
section: "8"
letter: "m"
url: "/docs/linux/man/8-migspeed/"
description: "migspeed – Test the speed of page migration"
---

<p>migspeed &#8211; Test the speed of page migration</p>
<h2>Synopsis</h2>
<p><code>migspeed</code> -p pages from-nodes to-nodes</p>
<h2>Description</h2>
<p><code>migspeed</code> attempts to move a sample of pages from the indicated node to the target node and measures the time it takes to perform the move. <code>-p pages</code> The default sample is 1000 pages. Override that with another number. </p>
<h2>Notes</h2>
<p>Requires an NUMA policy aware kernel with support for page migration (Linux 2.6.16 and later). </p>
<h2>Copyright</h2>
<p>Copyright 2007 Christoph Lameter, Silicon Graphics, Inc. migratepages is under the GNU General Public License, v.2</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-numactl/">numactl</a>(8)</i> </p>
