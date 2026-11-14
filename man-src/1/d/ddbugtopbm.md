---
title: "ddbugtopbm(1)"
name: "ddbugtopbm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddbugtopbm/"
description: "ddbugtopbm – convert Diddle or DiddleBug sketches to PBM files"
---

<h2 class="name">NAME</h2>
<p> ddbugtopbm &#8211; convert Diddle or DiddleBug sketches to PBM files </p>
<h2>SYNOPSIS</h2>
<p> <code>ddbugtopbm</code> </p>
<h2>EXAMPLES</h2>
<pre>
<code>ddbugtopbm &lt;/path/to/palm/backup/dir/DiddleBugDB.pdb</code>
<code>ddbugtopbm &lt;/path/to/palm/backup/dir/DiddleDB.pdb</code>
<code>ddbugtopbm &lt;/path/to/palm/backup/dir/DiddleIDB.pdb</code>
</pre>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ddbugtopbm</code> converts all sketches present in a database used by the PalmOS programs <code>Diddle</code> or <code>DiddleBug</code> into appropriately-named PBM files. The backup copy of DiddleBug&#8217;s database you should use as this program&#8217;s input is usually called <code>DiddleBugDB.pdb</code>. Or if you use the original Diddle, it has two separate DBs &#8211; <code>DiddleDB.pdb</code>, containing unnamed `scratch&#8217; sketches, and <code>DiddleIDB.pdb</code>, containing the saved (and named) sketches which are listed by its `index&#8217; option. You can feed this program any of these three on standard input. </p>
<h2>USING THE PROGRAM</h2>
<p> I recommend you <i>not</i> run <code>ddbugtopbm</code> from your Palm backup directory, i.e. don&#8217;t run it from the directory the DB will normally be in. Instead, run it from some other directory (perhaps you could make a directory purely to hold the PBM files, just to keep things simple) and use an absolute or relative path to the DB. </p>
<p> The filenames used for the output PBMs are based on the names given to each sketch; if you have an unnamed sketch, it&#8217;s given a name along the lines of <code>sketch-0123.pbm</code>. </p>
<p> While the named sketches will overwrite any existing PBM file with the same name, the unnamed ones won&#8217;t &#8211; they&#8217;ll just try using another filename. (I think this is probably the right approach, as you can&#8217;t really tell the unnamed sketches apart.) </p>
<h2>LIMITATIONS</h2>
<p> The DiddleBug DB reader is only known to work with DBs from DiddleBug version 2.50. But it should probably work on later versions, and I think it&#8217;ll work on DBs from version 2.15 as well. </p>
<p> It might fall over if fed an empty database, and doesn&#8217;t do much (if any) checking of the input. </p>
<h2>AUTHOR</h2>
<p> Russell Marks (<i>rus [at] svgalib.org</i>). </p>
<p> Mitch Blevins&#8217;s decompression code is directly from DiddleBug itself, which like ddbugtopbm is distributed under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-palmtopnm/">palmtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<p> Jens-Chr. Heyer&#8217;s `didcon&#8217; script does something similar. </p>
<h2>HISTORY</h2>
<p> <code>ddbugtopbm</code> was new in Netpbm 10.18 (August 2003). It was written and independently distributed in August 2002. </p>
<h2>Index</h2>
