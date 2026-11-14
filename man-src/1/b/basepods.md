---
title: "basepods(1)"
name: "basepods"
section: "1"
letter: "b"
url: "/docs/linux/man/1-basepods/"
---

<h2 class="name">NAME</h2>
 

 basepods - print out pod paths for the standard perl manpages 

<h2>DESCRIPTION</h2>

 This program uses your configuration's <tt>&quot;installprivlib&quot;</tt> directory to look up the full paths to those pod pages. Any files in that directory whose names end in <tt>&quot;.pod&quot;</tt> will be printed to the standard output, one per line. This is normally used in backticks to produce a list of filenames for other commands.

<h2>EXAMPLES</h2>

 <pre>
    $ podgrep typeglob `basepods`
    $ basepods | grep delt
    /usr/local/devperl/lib/5.00554/pod/perl5004delta.pod
    /usr/local/devperl/lib/5.00554/pod/perl5005delta.pod
    /usr/local/devperl/lib/5.00554/pod/perldelta.pod
</pre> 

 You can also run this using alternate perl binaries, like so: 

 <pre>
    $ oldperl -S basepods | grep delt
    /usr/lib/perl5/pod/perldelta.pod
    $ podgrep -i thread `filsperl basepods | grep delt`
    ....
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-faqpods/">faqpods</a></i>(1), <i><a HREF="/docs/linux/man/1-modpods/">modpods</a></i>(1), <i><a HREF="/docs/linux/man/1-pods/">pods</a></i>(1), <i><a HREF="/docs/linux/man/1-sitepod/">sitepod</a></i>(1), <i><a HREF="/docs/linux/man/1-podpath/">podpath</a></i>(1), and <i><a HREF="/docs/linux/man/1-stdpod/">stdpod</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


