---
title: "nfstest-utils(3)"
name: "nfstest-utils"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfstest-utils/"
description: "nfstest.utils – Utilities module"
---

<p>nfstest.utils &#8211; Utilities module</p>
<h2>Description</h2>
<p>Definition for common classes and constants</p>
<h2>Classes</h2>
<h3>class SparseFile(baseobj.BaseObj)</h3>
<pre>SparseFile object
SparseFile() -&gt; New sparse file object
Usage:
 # Create defintion for a sparse file of size 10000 having
 # two holes of size 1000 at offsets 3000 and 6000
 x = SparseFile(&quot;/mnt/t/file1&quot;, 10000, [3000, 6000], 1000)
 # Object attributes defined after creation using the above
 # sample data:
 # endhole: set to True if the file ends with a hole
 # Above example ends with data so,
 # x.endhole = False
 # data_offsets: list of data segment offsets
 # x.data_offsets = [0, 4000, 7000]
 # hole_offsets: list of hole segment offsets including the
 # imlicit hole at the end of the file
 # x.hole_offsets = [3000, 6000, 10000]
 # sparse_data: list of data/hole segments, each item in the list
 # has the following format [offset, size, type]
 # x.sparse_data = [[0, 3000, 1], [3000, 1000, 0], [4000, 2000, 1],
 # [6000, 1000, 0], [7000, 3000, 1]]
<code>Methods defined here:</code>
---------------------
<code>__init__(self, absfile, file_size, hole_list, hole_size)</code>
Create sparse file object definition, the file is not created
just the object. Object attributes are defined which makes it
easy to create the actual file.
<dl><dt><dd><dl><dt><code>absfile:</code>
<dd>Absolute path name of file
<dt><code>file_size:</code>
<dd>Total size of sparse file
<dt><code>hole_list:</code>
<dd>List of hole offsets
<dt><code>hole_size:</code>
<dd>Size for each hole
</dl></dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
