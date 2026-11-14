---
title: "sitepods(1)"
name: "sitepods"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sitepods/"
---

<h2 class="name">NAME</h2>
 

 sitepods - print out the paths to the modules that this site added 

<h2>DESCRIPTION</h2>

 This program shows the paths to module pods that are in the <i>site_perl</i> directories.

<h2>EXAMPLES</h2>

 <pre>
    $ sitepods
    /usr/local/devperl/lib/site_perl/5.00554/i686-linux/XML/Parser/Expat.pm
    /usr/local/devperl/lib/site_perl/5.00554/i686-linux/XML/Parser.pm
</pre> 

 You can also run this using alternate perl binaries, like so: 

 <pre>
    $ oldperl -S sitepods  
    ....
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-faqpods/">faqpods</a></i>(1), <i><a HREF="/docs/linux/man/1-modpods/">modpods</a></i>(1), <i><a HREF="/docs/linux/man/1-pods/">pods</a></i>(1), <i><a HREF="/docs/linux/man/1-podpath/">podpath</a></i>(1), and <i><a HREF="/docs/linux/man/1-stdpod/">stdpod</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


