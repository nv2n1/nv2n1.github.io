---
title: "e2pall(1)"
name: "e2pall"
section: "1"
letter: "e"
url: "/docs/linux/man/1-e2pall/"
description: "e2pall – convert all EPS files in a LaTeX document to PDF"
---

<h2>NAME</h2>
<p> e2pall &#8211; convert all EPS files in a LaTeX document to PDF </p>
<h2>SYNOPSIS</h2>
<p> <code>e2pall</code> <i>TEXFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>e2pall</code> searches through <i>TEXFILE</i> for \includegraphics commands to find the base names of image files. When it finds one, <code>e2pall</code> runs <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1) to create a PDF file from the EPS file. </p>
<p> <code>e2pall</code> will check to be sure that an existing PDF file is up-to-date with the EPS file, and will not run <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1) if the PDF file is newer than the EPS file. </p>
<h2>BUGS</h2>
<dl>
<dt>
<dd> Seems to be broken</p>
<dt>
<dd> Cannot handle \input{<i>filename</i>} or \includegraphics{<i>filename</i>} split over more than one line</p>
<dt>
<dd> Must be run from same directory as the LaTeX file</p>
<dt>
<dd> Does not look down $TEXINPUTS</p>
<dt>
<dd> Cannot handle documents that use \include commands</p>
<dt>
<dd> Assumes <i>all</i> files included with \includegraphics are EPS files</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> <code>e2pall</code> was written by Jody Klymak &lt;jklymak [at] apl.washington.edu&gt; and published in a posting to the &lt;pdftex [at] tug.org&gt; (mailing list). </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
