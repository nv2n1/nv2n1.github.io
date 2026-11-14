---
title: "clipfilter(1)"
name: "clipfilter"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clipfilter/"
---

<h2 class="name">NAME</h2>
 

 clipfilter - Run various conversions for your clipboard data. 

<h2>USAGE</h2>

 <pre>
    # (copy some stuff)
    $ clipfilter -html
    # (paste, with html entities substituted in)
    
    # or URI-escaping:
    $ clipfilter -uri
    # or pipe through an arbitrary program, like `tac`, the backwards cat:
    $ clipfilter tac
    # Note: currently, this just dumps everything to open2() and reads
    # everything back. It could possibly create a deadlock, but I haven't
    # found the case that causes this, yet.
</pre>

<h2>MOTIVATION</h2>

 A very frequent user pattern is to copy something, edit it in some rote way, and then paste it back. Writing your own filter scripts will make it even more useful.

<h2>BUGS</h2>

 Current weirdness when piping this to some programs, like 'wc' and 'tail'. I will work on this.

<h2>AUTHOR</h2>

 Ryan King &lt;rking [at] panoptic.com&gt;

<h2>COPYRIGHT</h2>

 Copyright (c) 2010. Ryan King. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 See &lt;<a rel="nofollow" HREF="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; 

<h2>Index</h2>


