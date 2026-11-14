---
title: "a5booklet(1)"
name: "a5booklet"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a5booklet/"
description: "a5booklet – copy two A5 pages from a .dvi file to one A4 page in another."
---

<h2 class="name">NAME</h2>
<p> a5booklet &#8211; copy two A5 pages from a .dvi file to one A4 page in another. </p>
<h2>SYNOPSIS</h2>
<p> <code>a5booklet</code> <i>file</i><code>[.dvi]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>A5booklet</code> is a little script that allows you to typeset two A5 pages next to eachother on a single A4 page (landscape), combining pages from the original file in such a way that after double sided printing and some reshuffeling of the pages you get a nice a5 booklet that is ready for a staple in the middle. </p>
<p> The script calls a very clever program <code>dvidvi</code>, written by Tomas Rokicki (the author of <code>dvips</code>), that does the real work. </p>
<p> The output is written to two files, <i>file</i><code>-1.dvi</code> and <i>file</i><code>-2.dvi</code> </p>
<p> <code>dvips -ta4 -tlandscape </code> <i>file</i><code>-1</code> </p>
<p> then put the stack upside doen in the printer, and print the second file using </p>
<p> <code>dvips -ta4 -tlandscape </code> <i>file</i><code>-2</code> </p>
<p> Make sure that the bottom of the A5-pages is on the correct side of the paper when you put the stack back for printing the back side. After the two print jobs, you must re-shuffle the paper stack before you can staple it. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-dvidvi/">dvidvi</a></code>(1). </p>
<h2>BUGS</h2>
<p> The script has A4 papersize hardwired into it. Admittedly, a European-centered way of thinking. </p>
<p> Page number 1 is always the first page in the original .dvi file, not the page numbered 1 by TeX&#8217;s numbering scheme. </p>
<h2>AUTHOR</h2>
<p> <code>A5booklet</code> is written by David A. van Leeuwen (david [at] ElseWare.cistron.nl), but is is not original in any way. The main two lines that do the work are inspired from the man page of <code>dvidvi</code>. <code>A5booklet</code> is available under the conditions of the Gnu Public Licence. </p>
<h2>Index</h2>
