---
title: "modpods(1)"
name: "modpods"
section: "1"
letter: "m"
url: "/docs/linux/man/1-modpods/"
---

<h2 class="name">NAME</h2>
 

 modpods - print out paths for the standard modules 

<h2>DESCRIPTION</h2>

 This program outputs the paths to all installed modules on your systems. This includes both the standard modules (which the <i>stdpods</i> command produces) and the site-specific ones (which the <i>sitepods</i> command produces). 

 This is just a front-end for calling <i>pminst -l</i>, supplied to make it more obvious what it does.

<h2>EXAMPLE</h2>

 This finds all the modules whose documentation mentions destructors, and cats it out at you. 

 <pre>
    $ podgrep -i destructor `modpods`
    =head1 /usr/local/devperl/lib/5.00554/i686-linux/DB_File.pm chunk 371
    Having read L&lt;perltie&gt; you will probably have already guessed that the
    error is caused by the extra copy of the tied object stored in C&lt;$X&gt;.
    If you haven't, then the problem boils down to the fact that the
    B&lt;DB_File&gt; destructor, DESTROY, will not be called until I&lt;all&gt;
    references to the tied object are destroyed. Both the tied variable,
    C&lt;%x&gt;, and C&lt;$X&gt; above hold a reference to the object. The call to
    untie() will destroy the first, but C&lt;$X&gt; still holds a valid
    reference, so the destructor will not get called and the database file
    F&lt;tst.fil&gt; will remain open. The fact that Berkeley DB then reports the
    attempt to open a database that is alreday open via the catch-all
    &quot;Invalid argument&quot; doesn't help.
    =head1 /usr/local/devperl/lib/5.00554/Tie/Array.pm chunk 40
    Normal object destructor method.
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-podgrep/">podgrep</a></i>(1), <i><a HREF="/docs/linux/man/1-modpods/">modpods</a></i>(1), <i><a HREF="/docs/linux/man/1-pods/">pods</a></i>(1), <i><a HREF="/docs/linux/man/1-sitepods/">sitepods</a></i>(1), <i><a HREF="/docs/linux/man/1-podpath/">podpath</a></i>(1), and <i><a HREF="/docs/linux/man/1-stdpod/">stdpod</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


