---
title: "grenum(1)"
name: "grenum"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grenum/"
description: "grenum – An advanced refdes renumber utility"
---

<h2 class="name">NAME</h2>
<p> <code>grenum</code> &#8211; An advanced refdes renumber utility</p>
<h2>SYNOPSIS</h2>
<p> <code>grenum</code> [-v|&#8211;version -h|&#8211;help -p|&#8211;pagejump] <i>infile1.sch infile2.sch</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>grenum</code> program will renumber the refdes definitions read from <i>infile.</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt>-p, &#8211;pagejump</p>
<dd> This will switch on the page jump mode. It means that refdes&#8217;s from each <i>inputfile</i> gets renumbered from 100,200&#8230; etc.</p>
<dt>-v, &#8211;version</p>
<dd> prints version information</p>
<dt>-h, &#8211;help</p>
<dd> prints help message </p>
</dl>
<h2>RETURN VALUE</h2>
<p> <code>grenum</code> will return <code>0</code> if all files processed successfully, <code>1</code> if there was no input file specified, <code>2</code> if I/O files can&#8217;t be opened/written, <code>3</code> if there is parse error in input file, <code>4</code> if there is not enough memory to store refdes prefixes.</p>
<h2>BUGS</h2>
<p> If you find one, please report it to: </p>
<h2>AUTHOR</h2>
<p> Levente Kovacs </p>
<p> Levente.Kovacs [at] interware.hu </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gschem/">gschem</a>(1)</code> </p>
<h2>Index</h2>
