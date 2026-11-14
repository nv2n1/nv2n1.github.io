---
title: "podpath(1)"
name: "podpath"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podpath/"
---

<h2 class="name">NAME</h2>
 

 podpath - print the path to the Pod 

<h2>DESCRIPTION</h2>

 podpath prints the path to the Pod. podpath calls stdpods underneath if the Pod name includes 'perl'. Otherwise, it searches down <tt>@INC</tt>, printing the '.pod' filename if there is a separate Pod file, otherwise printing the 'pm' filename. This accommodates systems where the Pod lives in a separate file from the module file.

<h2>EXAMPLES</h2>

 <pre>
    $ podpath Cwd
    /usr/local/devperl/lib/5.00554/Cwd.pm
</pre> 

 It works with alternate installations, too: 

 <pre>
    $ devperl -S podpath perlfunc
    /usr/local/devperl/lib/5.00554/pod/perlfunc.pod
    $ oldperl -S podpath IO::Handle
    /usr/lib/perl5/i386-linux/5.00404/IO/Handle.pm
    $ filsperl -S podpath Thread
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/Thread.pm
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-stdpods/">stdpods</a></i>(1), <i><a HREF="/docs/linux/man/1-pmpath/">pmpath</a></i>(1), <i><a HREF="/docs/linux/man/1-perlmodlib/">perlmodlib</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


