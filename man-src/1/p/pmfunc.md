---
title: "pmfunc(1)"
name: "pmfunc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmfunc/"
---

<h2 class="name">NAME</h2>
 

 pmfunc - cat out a function from a module 

<h2>DESCRIPTION</h2>

 Given a fully-qualified function, this program opens up the file and attempts to cat out the source for that function.

<h2>EXAMPLES</h2>

 <pre><code>
$ pmfunc Cwd::getcwd
    sub getcwd
{
    abs_path('.');
}
</code></pre>

<h2>RESTRICTIONS</h2>

 Only subroutines that are defined in the normal fashion are seen, since a simple pattern-match is what does the extraction. Those loaded other ways, such as via <font SIZE="-1">AUTOLOAD,</font> typeglob aliasing, or in an <tt>&quot;eval&quot;</tt>, will all necessarily be missed. 

 This is mostly here for people who are too lazy to type 

 <pre>
    sed '/^sub getcwd/,/}/p' `pmpath Cwd`
or
    perl -ne 'print if /^sub\s+getcwd\b/ .. /}/' `pmpath Cwd`
</pre>

<h2>RESTRICTIONS</h2>

<h2>SEE ALSO</h2>

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


