---
title: "pfcat(1)"
name: "pfcat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pfcat/"
description: "pfcat – grep out function definitions from perlfunc"
---

<h2 class="name">NAME</h2>
<p> pfcat &#8211; grep out function definitions from perlfunc </p>
<h2>DESCRIPTION</h2>
<p> This program uses <i>podgrep</i> program to search your configuration&#8217;s perlfunc for function definitions. It honors a <code>-f</code> flag to format through <i>pod2text</i> and a <code>-p</code> flag to send the output through the pager. (Actually, it just passes these to <i>podgrep</i>.)</p>
<h2>EXAMPLES</h2>
<pre>
    $ pfcat seek
    (find all seek functions (including sysseek))
    $ pfcat -pf sprintf
    (sprintf function is formated and sent to pager)
    $ pfcat -f 'int'
    /usr/local/devperl/lib/5.00554/pod/perlfunc.pod chunk 506
    int EXPR
    int
    Returns the integer portion of EXPR. If EXPR is omitted, uses
    `$_'. You should not use this for rounding, because it truncates
    towards `0', and because machine representations of floating point
    numbers can sometimes produce counterintuitive results. Usually
    `sprintf()' or `printf()', or the `POSIX::floor' or `POSIX::ceil'
    functions, would serve you better.
</pre>
<p> You can also run this using alternate perl binaries, like so: </p>
<pre>
    $ oldperl -S pfcat open
    ....
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-podgrep/">podgrep</a></i>(1)</p>
<h2>AUTHORS and COPYRIGHTS</h2>
<p> Copyright (C) 1999 Tom Christiansen. </p>
<p> Copyright (C) 2006-2014 Mark Leighton Fisher.</p>
<h2>LICENSE</h2>
<p> This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl &#8220;Artistic License&#8221;. (This is the Perl 5 licensing scheme.) </p>
<p> Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl &#8220;Artistic License&#8221;. </p>
<h2>Index</h2>
