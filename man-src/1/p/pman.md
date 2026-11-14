---
title: "pman(1)"
name: "pman"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pman/"
---

<h2 class="name">NAME</h2>
 

 pman - show a module's man page 

<h2>DESCRIPTION</h2>

 Send a module's pod through pod2text and your pager. 

 This is mostly here for people too lazy to type 

 <pre>
    $ pod2text `pmpath CGI` | $PAGER
</pre>

<h2>EXAMPLES</h2>

 <pre>
    $ pman CGI
    $ pman Curses
</pre> 

 Or running under different versions of Perl: 

 <pre>
    $ oldperl -S pman CGI
    $ filsperl -S pman Threads
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pod2text/">pod2text</a></i>(1), <i><a HREF="/docs/linux/man/1-perlpod/">perlpod</a></i>(1), <i><a HREF="/docs/linux/man/1-pod2man/">pod2man</a></i>(1), <i><a HREF="/docs/linux/man/1-pod2html/">pod2html</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


