---
title: "faqpods(1)"
name: "faqpods"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faqpods/"
---

<h2 class="name">NAME</h2>
 

 faqpods - print out pod paths for the standard perl faqs 

<h2>DESCRIPTION</h2>

 This program uses your configuration's <tt>&quot;installprivlib&quot;</tt> directory to look up the full paths to those pod pages. Any files in that directory whose names start in <tt>&quot;perlfaq&quot;</tt> will be printed to the standard output, one per line. This is normally used in backticks to produce a list of filenames for other commands.

<h2>EXAMPLES</h2>

 <pre>
    $ podgrep typeglob `faqpods`
    ....
</pre> 

 You can also run this using alternate perl binaries, like so: 

 <pre>
    $ podgrep -i thread `filsperl faqpods`
    ....
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-basepods/">basepods</a></i>(1), <i><a HREF="/docs/linux/man/1-modpods/">modpods</a></i>(1), <i><a HREF="/docs/linux/man/1-pods/">pods</a></i>(1), <i><a HREF="/docs/linux/man/1-sitepod/">sitepod</a></i>(1), <i><a HREF="/docs/linux/man/1-podpath/">podpath</a></i>(1), and <i><a HREF="/docs/linux/man/1-stdpod/">stdpod</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


