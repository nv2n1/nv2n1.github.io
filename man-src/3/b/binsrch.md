---
title: "binsrch(3)"
name: "binsrch"
section: "3"
letter: "b"
url: "/docs/linux/man/3-binsrch/"
description: "bin_search, copyfile, replace_line, insert_line – general purpose functions for performing a binary search"
---

<h2>NAME</h2>
<p> bin_search, copyfile, replace_line, insert_line &#8211; general purpose functions for performing a binary search</p>
<h2>SYNOPSIS</h2>
<p> <code>char *bin_search(char *key, FILE *fp);</code> </p>
<p> <code>void copyfile(FILE *fromfp, FILE *tofp);</code> </p>
<p> <code>char *replace_line(char *new_line, char *key, FILE *fp);</code> </p>
<p> <code>char *insert_line(char *new_line, char *key, FILE *fp);</code></p>
<h2>DESCRIPTION</h2>
<p> The WordNet library contains several general purpose functions for performing a binary search and modifying sorted files. </p>
<p> <code>bin_search()</code> is the primary binary search algorithm to search for <i>key</i> as the first item on a line in the file pointed to by <i>fp</i>. The delimiter between the key and the rest of the fields on the line, if any, must be a space. A pointer to a static variable containing the entire line is returned. <font SIZE="-1"><code>NULL </code></font> is returned if a match is not found. </p>
<p> The remaining functions are not used by WordNet, and are only briefly described. </p>
<p> <code>copyfile()</code> copies the contents of one file to another. </p>
<p> <code>replace_line()</code> replaces a line in a file having searchkey <i>key</i> with the contents of <i>new_line</i>. It returns the original line or <font SIZE="-1"><code>NULL</code></font> in case of error. </p>
<p> <code>insert_line()</code> finds the proper place to insert the contents of <i>new_line</i>, having searchkey <i>key</i> in the sorted file pointed to by <i>fp</i>. It returns <font SIZE="-1"><code>NULL </code></font> if a line with this searchkey is already in the file.</p>
<h2>NOTES</h2>
<p> The maximum length of <i>key</i> is 1024. </p>
<p> The maximum line length in a file is 25K. </p>
<p> If there are no additional fields after the search key, the key must be followed by at least one space before the newline character.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/3-morph/">morph</a></code>(3), <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3), <code><a href="/docs/linux/man/3-wnutil/">wnutil</a></code>(3), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5).</p>
<h2>WARNINGS</h2>
<p> <code>binsearch()</code> returns a pointer to a static character buffer. The returned string should be copied by the caller if the results need to be saved, as a subsequent call will replace the contents of the static buffer. </p>
<h2>Index</h2>
