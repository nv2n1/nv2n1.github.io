---
title: "pmpath(1)"
name: "pmpath"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmpath/"
---

<h2 class="name">NAME</h2>
 

 pmpath - show full path to a perl module 

<h2>SYNOPSIS</h2>

 pmpath module ...

<h2>DESCRIPTION</h2>

 For each module name given as an argument, produces its full path on the standard output, one per line.

<h2>EXAMPLES</h2>

 <pre>
    $ pmpath CGI
    /usr/local/devperl/lib/5.00554/CGI.pm
    $ filsperl -S pmpath IO::Socket CGI::Carp
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/IO/Socket.pm
    /usr/local/filsperl/lib/5.00554/CGI/Carp.pm
    $ oldperl -S pmpath CGI CGI::Imagemap
    /usr/lib/perl5/CGI.pm
    /usr/lib/perl5/site_perl/CGI/Imagemap.pm
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmdesc/">pmdesc</a></i>(1), <i><a HREF="/docs/linux/man/1-pmvers/">pmvers</a></i>(1), <i><a HREF="/docs/linux/man/1-pmcat/">pmcat</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


