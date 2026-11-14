---
title: "pmls(1)"
name: "pmls"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmls/"
---

<h2 class="name">NAME</h2>
 

 pmls - long list the module path 

<h2>DESCRIPTION</h2>

 This is mostly here for people too lazy to type 

 <pre>
    $ ls -l `pmpath CGI`
</pre>

<h2>EXAMPLES</h2>

 <pre><code>
$ pmls CGI - r-- r-- r-- 1 root root 190901 Dec 6 03 : 19 / usr / local / devperl / lib / 5.00554 / CGI.pm $ oldperl - S pmls CGI - r-- r-- r-- 1 root root 186637 Sep 10 00 : 18 / usr / lib / perl5 / CGI.pm
</code></pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmpath/">pmpath</a></i>(1)

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


