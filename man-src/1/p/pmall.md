---
title: "pmall(1)"
name: "pmall"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmall/"
---

<h2 class="name">NAME</h2>
 

 pmall - show all installed versions and descs 

<h2>SYNOPSIS</h2>

 <pre><code>
pmall[-d][-w][-a][-s]
</code></pre> 

 pmall - show all installed versions and descs

<h2>DESCRIPTION</h2>

 This program runs through all your installed modules and tells you what they're for and what version number they are at. 

 The following options are honored:
<dl>
<dt>-v
<dd> give debug info
<dt>-w
<dd> warn about missing descriptions on modules
<dt>-a
<dd> include relative paths
<dt>-s
<dd> sort output within each directory</dl>

<h2>HISTORICAL NOTE</h2>

 This program used to be called <i>pmdesc</i> and is included in <i>The Perl Cookbook</i> under that name. However, that name has been usurped by a simpler program. 

 For example, to find the versions of what is in your site-specific directory, the simpler <i>pmdesc</i> might be preferred: 

 <pre><code>
    $ pmdesc `pminst -s | perl -lane 'print $F[1] if $F[0] =~ /site/'`
    XML::Parser::Expat (2.19) - Lowlevel access to James Clark's expat XML parser
    XML::Parser (2.19) - A perl module for parsing XML documents
</code></pre>

<h2>KNOWN BUGS</h2>

 This program takes a long time to run. 

 Some modules don't work right (<font SIZE="-1">CPAN</font>.pm, ExtUtils) because of noisy things they do at compile time or poor formatting of the pod.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmdesc/">pmdesc</a></i>(1) <i><a HREF="/docs/linux/man/1-pmvers/">pmvers</a></i>(1)

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


