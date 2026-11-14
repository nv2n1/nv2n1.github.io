---
title: "podtoc(1)"
name: "podtoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podtoc/"
---

<h2 class="name">NAME</h2>
 

 podtoc - show outline of pods 

<h2>DESCRIPTION</h2>

 This program shows the structure of one or more pod documents.

<h2>EXAMPLES</h2>

 <pre>
    $ podtoc `pmpath CGI`
     NAME
     SYNOPSIS
     ABSTRACT
     DESCRIPTION
         PROGRAMMING STYLE
         CALLING CGI.PM ROUTINES
         *  1. Use another name for the argument, if one is available.  For
            example, -value is an alias for -values.
         *  2. Change the capitalization, e.g. -Values
    (etc)
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pod2man/">pod2man</a></i>(1), <i><a HREF="/docs/linux/man/1-perlpod/">perlpod</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


