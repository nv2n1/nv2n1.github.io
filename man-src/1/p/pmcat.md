---
title: "pmcat(1)"
name: "pmcat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmcat/"
---

<h2 class="name">NAME</h2>
 

 pmcat - page through a module file 

<h2>DESCRIPTION</h2>

 Given a module name, figure out the path name and send that to the user's pager. 

 <pre>
    $ pmcat CGI
</pre> 

 This works also on alternate installed versions of Perl: 

 <pre>
    $ oldperl -S pmcat strict
    $ filsperl -S pmcat Threads
</pre> 

 This command is mostly here for people too lazy to type 

 <pre>
    $ more `pmpath CGI`
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmpath/">pmpath</a></i>(1)

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


