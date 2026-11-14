---
title: "podgrep(1)"
name: "podgrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podgrep/"
description: "podgrep – grep in pod sections only"
---

<h2 class="name">NAME</h2>
<p> podgrep &#8211; grep in pod sections only </p>
<h2>SYNOPSIS</h2>
<p> podgrep [<code>-i</code>] [<code>-p</code>] [<code>-f</code>] [<code>-h</code>] <i>pattern</i> [ <i>files</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> This program searches each paragraph in a pod document and prints each paragraph that matches the supplied pattern. This pod may be mixed with program code, such as in a module. </p>
<p> Options are:</p>
<dl>
<dt>-i</p>
<dd> means case insensitive match</p>
<dt>-p</p>
<dd> means page output though the user&#8217;s pager. The pager will be primed with an argument to search for the string. This highlights the result.</p>
<dt>-f</p>
<dd> means format output though the <i>pod2text</i> program.</p>
<dt>-h</p>
<dd> means check for matches in pod <tt>&quot;=head&quot;</tt> and <tt>&quot;=item&quot;</tt> headers alone, and to keep printing podagraphs until the next header is found.</dl>
<h2>EXAMPLES</h2>
<pre>
    $ podgrep mail `pmpath CGI`
    (prints out podagraphs from the CGI.pm manpage that mention mail)
    $ podgrep -i destructor `sitepods`
    (prints out podagraphs that mention destructors in the 
     site-installed pods)
    $ podgrep -i 'type.?glob' `stdpods`
    (prints out podagraphs that mention typeglob in the
     standard pods)
    $ podgrep -hpfi &quot;lock&quot; `faqpods`
    (prints out all podagraphs with &quot;lock&quot; in the headers
    case-insensitively, then formats these with pod2text, then
    shows them in the pager with matches high-lighted)
    $ podgrep -fh seek `podpath perlfunc`
    (prints out and formats podagraphs from the standard perlfunc manpage
    whose headers or items contain &quot;seek&quot;.)
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-faqpods/">faqpods</a></i>(1), <i><a href="/docs/linux/man/1-pfcat/">pfcat</a></i>(1), <i><a href="/docs/linux/man/1-pmpath/">pmpath</a></i>(1), <i><a href="/docs/linux/man/1-pod2text/">pod2text</a></i>(1), <i><a href="/docs/linux/man/1-podpath/">podpath</a></i>(1), <i><a href="/docs/linux/man/1-sitepods/">sitepods</a></i>(1), <i><a href="/docs/linux/man/1-stdpods/">stdpods</a></i>(1), and <i><a href="/docs/linux/man/1-tcgrep/">tcgrep</a></i>(1).</p>
<h2>NOTE</h2>
<p> For a pager, the author likes these environment settings (in the login startup, of course): </p>
<pre><code>
$ENV{PAGER} = "less";
$ENV{LESS} = "MQeicsnf";
</code></pre>
<h2>AUTHORS and COPYRIGHTS</h2>
<p> Copyright (C) 1999 Tom Christiansen. </p>
<p> Copyright (C) 2006-2014 Mark Leighton Fisher.</p>
<h2>LICENSE</h2>
<p> This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl &#8220;Artistic License&#8221;. (This is the Perl 5 licensing scheme.) </p>
<p> Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl &#8220;Artistic License&#8221;. </p>
<h2>Index</h2>
