---
title: "oldfind(1)"
name: "oldfind"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oldfind/"
description: "oldfind – search for files in a directory hierarchy"
---

<h2>NAME</h2>
<p> oldfind &#8211; search for files in a directory hierarchy</p>
<h2>SYNOPSIS</h2>
<p> <code>oldfind</code> [-H] [-L] [-P] [-D debugopts] [-Olevel] [path&#8230;] [expression]</p>
<h2>DESCRIPTION</h2>
<p> The <code>oldfind</code> and <code>find</code> programs are functionally identical. The only difference between them is the implementation internals of how the filesystem is searched. The <code>oldfind</code> binary has a recursive implementation while <code>find</code> uses <code><a href="/docs/linux/man/3-fts/">fts</a></code>(3). The fts-based implementation will replace the recursive implementation but for the moment both implementations are installed. </p>
<p> The implementation which is installed as <code>find</code> on this system is the fts-based implementation, since the <code>&#8211;without-fts</code> option was not passed to the <code>configure</code> script when findutils was built.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/3-fts/">fts</a></code>(3), <code>Finding Files</code> (on-line in Info, or printed). </p>
<h2>Index</h2>
