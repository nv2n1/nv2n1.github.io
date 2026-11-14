---
title: "clipaccumulate(1)"
name: "clipaccumulate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clipaccumulate/"
---

<h2 class="name">NAME</h2>
 

 clipaccumulate - Make a bunch of little clipboards into one big one. 

<h2>USAGE</h2>

 The first thing it says (which goes to <font SIZE="-1">STDERR,</font> so you can redirect into a file if you want), is how to exit, which is by copying the magic ``end'' string into the clipboard. Crufty? Yep. You can still do Ctrl+C if you don't like this (or if the string scrolls off the top of the screen). 

 The next thing it does is wait for the clipboard to change, at which point it will print out the new data and go back to waiting for the clipboard to change. 

 Then you copy the exit string, and it will fill the clipboard with all the little pieces it saw along the way. 

 (Right now, it just joins everything with spaces in between - is this bugging anyone?)

<h2>MOTIVATION</h2>

 Hard to explain. I run into cases where I wanted to make a bunch of small notes that included all these different bits of info. Instead of jotting them down on a scrap of paper, I made this. 

 Let me know how it can be made better.

<h2>AUTHOR</h2>

 Ryan King &lt;rking [at] panoptic.com&gt;

<h2>COPYRIGHT</h2>

 Copyright (c) 2010. Ryan King. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 See &lt;<a rel="nofollow" HREF="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; 

<h2>Index</h2>


