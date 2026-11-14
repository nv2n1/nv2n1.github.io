---
title: "pmvers(1)"
name: "pmvers"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmvers/"
---

<h2 class="name">NAME</h2>
 

 pmvers - print out a module's version 

<h2>DESCRIPTION</h2>

 Given one or more module names, show the version number if present. If more than one argument is given, the name of the module will also be printed. Not all modules define version numbers, however.

<h2>EXAMPLES</h2>

 <pre>
    $ pmvers CGI
    2.46
    $ pmvers IO::Socket Text::Parsewords
    IO::Socket: 1.25
    Text::ParseWords: 3.1
    $ oldperl -S pmvers CGI
    2.42
    $ filsperl -S pmvers CGI
    2.46
    $ pmvers Devel::Loaded
    pmvers: unknown version for module `Devel::Loaded'
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmdesc/">pmdesc</a></i>(1), <i><a HREF="/docs/linux/man/1-pmpath/">pmpath</a></i>(1), <i><a HREF="/docs/linux/man/1-pmcat/">pmcat</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


