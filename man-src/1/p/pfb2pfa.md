---
title: "pfb2pfa(1)"
name: "pfb2pfa"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pfb2pfa/"
---

<h2 class="name">NAME</h2>
 

 pfb2pfa - convert a type1 pfb file (binary MSDOS) into a pfa (ASCII) 

<h2>SYNOPSIS</h2>

 pfb2pfa [-v] pfbfile [pfafile]

<h2>DESCRIPTION</h2>

 Program converts a binary MSDOS representation for a type1 PostScript font into a readable ASCII version. The MSDOS newline (\r) is converted into the UNIX newline (\n). The output is written in a file whose name is the name that is provided on the command line or the basename of the input file plus extension &quot;.pfa&quot;. 

 With the -v option you get some information about what the program is doing.

<h2>AUTHOR</h2>

 <pre>
Piet Tutelaers
Maintained in TeX Live; please send bug reports or other correspondence
to tex-k [at] tug.org (<a rel="nofollow" HREF="http://lists.tug.org/tex-k">http://lists.tug.org/tex-k</a>).
</pre>

<h2>Index</h2>


