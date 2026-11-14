---
title: "use-devel-checklib(1)"
name: "use-devel-checklib"
section: "1"
letter: "u"
url: "/docs/linux/man/1-use-devel-checklib/"
---

<h2 class="name">NAME</h2>
 

 use-devel-checklib - a script to package Devel::CheckLib with your code. 

<h2>DESCRIPTION</h2>

 This script, when run in the directory in which your shiny new module lives, will bundle Devel::CheckLib in the <tt>&quot;inc&quot;</tt> directory, and update your Makefile.PL (or Build.PL) appropriately. If neither exists, it will create a Makefile.PL.

<h2>SYNOPSIS</h2>

 <pre>
    use-devel-checklib list of libraries
</pre>

<h2>WARNINGS, BUGS and FEEDBACK</h2>

 This script has not been thoroughly tested. You should check by hand that it has done what you expected after running it. 

 If you use Module::Build::Compat to write a Makefile.PL, then you will need to re-run this script whenever you have generated a new Makefile.PL. 

 I welcome feedback about my code, including constructive criticism. Bug reports should be made using &lt;<a rel="nofollow" HREF="http://rt.cpan.org/">http://rt.cpan.org/</a>&gt; or by email.

<h2>SEE ALSO</h2>

 Devel::CheckLib

<h2>AUTHOR</h2>

 David Cantrell &lt;<i>david [at] cantrell.org.uk</i>&gt;

<h2>COPYRIGHT and LICENCE</h2>

 Copyright 2007 David Cantrell 

 This software is free-as-in-speech software, and may be used, distributed, and modified under the same conditions as perl itself.

<h2>CONSPIRACY</h2>

 This module is also free-as-in-mason software. 

<h2>Index</h2>


