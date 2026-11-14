---
title: "pmdesc(1)"
name: "pmdesc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdesc/"
---

<h2 class="name">NAME</h2>
 

 pmdesc - print out version and whatis description of perl modules 

<h2>DESCRIPTION</h2>

 Given one or more module names, show the version number (if known) and the `whatis' line, that is, the <font SIZE="-1">NAME</font> section's description, typically used for generation whatis databases.

<h2>EXAMPLES</h2>

 <pre><code>
    $ pmdesc IO::Socket
    IO::Socket (1.25) - Object interface to socket communications
    $ oldperl pmdesc IO::Socket
    IO::Socket (1.1603) - Object interface to socket communications
    $ pmdesc `pminst -s | perl -lane 'print $F[1] if $F[0] =~ /site/'`
    XML::Parser::Expat (2.19) - Lowlevel access to James Clark's expat XML parser
    XML::Parser (2.19) - A perl module for parsing XML documents
</code></pre>

<h2>RESTRICTIONS</h2>

 This only works on modules. It should also work on filenames, but then it's a bit tricky finding out the package to call the <font SIZE="-1">VERSION</font> method on.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmdesc/">pmdesc</a></i>(1) <i><a HREF="/docs/linux/man/1-pminst/">pminst</a></i>(1) <i><a HREF="/docs/linux/man/1-pmpath/">pmpath</a></i>(1) <i><a HREF="/docs/linux/man/1-pmvers/">pmvers</a></i>(1)

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


