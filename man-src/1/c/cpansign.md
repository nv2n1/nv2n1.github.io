---
title: "cpansign(1)"
name: "cpansign"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpansign/"
---

<h2 class="name">NAME</h2>
 

 cpansign - CPAN signature management utility 

<h2>SYNOPSIS</h2>

 <pre>
    % cpansign              # verify an existing SIGNATURE, or
                            # make a new one if none exists 
    % cpansign file.par     # verify or sign a PAR file
    % cpansign sign         # make signature; overwrites existing one
    % cpansign -s           # same thing
    % cpansign verify       # verify a signature
    % cpansign -v           # same thing
    % cpansign -v --skip    # ignore files in MANIFEST.SKIP
    % cpansign help         # display this documentation
    % cpansign -h           # same thing
</pre>

<h2>DESCRIPTION</h2>

 This utility lets you create and verify <font SIZE="-1">SIGNATURE</font> files.

<h2>SEE ALSO</h2>

 Module::Signature

<h2>AUTHORS</h2>

 Audrey Tang &lt;autrijus [at] autrijus.org&gt;

<h2>COPYRIGHT</h2>

 Copyright 2002, 2003, 2006 by Audrey Tang. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 See &lt;<a rel="nofollow" HREF="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; 

<h2>Index</h2>


