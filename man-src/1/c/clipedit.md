---
title: "clipedit(1)"
name: "clipedit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clipedit/"
---

<h2 class="name">NAME</h2>
 

 clipedit - Edit clipboard contents in one swoop. 

<h2>MOTIVATION</h2>

 Eliminating the ``Open editor, edit stuff, copy back to the clipboard'' shuffle.

<h2>NOTE</h2>

 If for some reason the clipboard contents changes during the edit session, you will be prompted to choose between 1) the original Clipboard contents, 2) the new Clipboard contents, and 3) the result of your edits (which is the default if you just hit ``Enter'').

<h2>CONFIGURATION</h2>

 If you don't want the script to use <tt>&quot;vim&quot;</tt> to edit, set either the environment variable <tt>$VISUAL</tt> or <tt>$EDITOR</tt>.

<h2>AUTHOR</h2>

 Ryan King &lt;rking [at] panoptic.com&gt;

<h2>COPYRIGHT</h2>

 Copyright (c) 2010. Ryan King. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 See &lt;<a rel="nofollow" HREF="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; 

<h2>Index</h2>


