---
title: "pwhich(1)"
name: "pwhich"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwhich/"
---

<h2 class="name">NAME</h2>
 

 pwhich - Perl-only `which' 

<h2>SYNOPSIS</h2>

 <pre>
  $ pwhich perl
  $ pwhich -a perl          # print all matches
  $ pwhich perl perldoc ... # look for multiple programs
  $ pwhich -a perl perldoc ...
</pre>

<h2>DESCRIPTION</h2>

 `pwhich' is a command-line utility program for finding paths to other programs based on the user's <tt>&quot;PATH&quot;</tt>. It is similar to the usualy Unix tool `which', and tries to emulate its functionality, but is written purely in Perl (uses the module <tt>&quot;File::Which&quot;</tt>), so is portable.

<h3>Calling syntax</h3>

 <pre><code>
$ pwhich[-a][-v] programname[programname...]
</code></pre>

<h3>Options</h3>

<dl>
<dt>-a
<dd> The option <i>-a</i> will make <tt>&quot;pwhich&quot;</tt> print all matches found in the <tt>&quot;PATH&quot;</tt> variable instead of just the first one. Each match is printed on a separate line.
<dt>-v
<dd> Prints version (of <tt>&quot;File::Which&quot;</tt>) and copyright notice and exits.</dl>

<h2>SUPPORT</h2>

 Bugs should be reported via the <font SIZE="-1">CPAN</font> bug tracker at 

 &lt;<a rel="nofollow" HREF="http://rt.cpan.org/NoAuth/ReportBug.html?Queue=File-Which">http://rt.cpan.org/NoAuth/ReportBug.html?Queue=File-Which</a>&gt; 

 For other issues, contact the maintainer.

<h2>AUTHOR</h2>

 Adam Kennedy &lt;adamk [at] cpan.org&gt; 

 Per Einar Ellefsen &lt;pereinar [at] cpan.org&gt; 

 Originated in <i>modperl-2.0/lib/Apache/Build.pm</i>. Changed for use in DocSet (for the mod_perl site) and Win32-awareness by me, with slight modifications by Stas Bekman, then extracted to create <tt>&quot;File::Which&quot;</tt>. 

 Version 0.04 had some significant platform-related changes, taken from the Perl Power Tools <tt>`which'</tt> implementation by Abigail with enhancements from Peter Prymmer. See &lt;<a rel="nofollow" HREF="http://www.perl.com/language/ppt/src/which/index.html">http://www.perl.com/language/ppt/src/which/index.html</a>&gt; for more information.

<h2>COPYRIGHT</h2>

 Copyright 2002 Per Einar Ellefsen. 

 Some parts copyright 2009 Adam Kennedy. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 perl, File::Which, <i><a HREF="/docs/linux/man/1-which/">which</a></i>(1) 

<h2>Index</h2>


