---
title: "pmload(1)"
name: "pmload"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmload/"
---

<h2 class="name">NAME</h2>
 

 pmload - show what files a given module loads at compile time 

<h2>DESCRIPTION</h2>

 Given an argument of a module name, show all the files that are loaded directly or indirectly when the module is used at compile-time.

<h2>EXAMPLES</h2>

 <pre>
    $ pmload IO::Handle
    /usr/local/devperl/lib/5.00554/Exporter.pm
    /usr/local/devperl/lib/5.00554/Carp.pm
    /usr/local/devperl/lib/5.00554/strict.pm
    /usr/local/devperl/lib/5.00554/vars.pm
    /usr/local/devperl/lib/5.00554/i686-linux/DynaLoader.pm
    /usr/local/devperl/lib/5.00554/i686-linux/IO/Handle.pm
    /usr/local/devperl/lib/5.00554/Symbol.pm
    /usr/local/devperl/lib/5.00554/i686-linux/IO/File.pm
    /usr/local/devperl/lib/5.00554/SelectSaver.pm
    /usr/local/devperl/lib/5.00554/i686-linux/Fcntl.pm
    /usr/local/devperl/lib/5.00554/AutoLoader.pm
    /usr/local/devperl/lib/5.00554/i686-linux/IO.pm
    /usr/local/devperl/lib/5.00554/i686-linux/IO/Seekable.pm
    $ cat `pmload IO::Socket` | wc -l
       4015
    $ oldperl -S pmload Tk
    /usr/lib/perl5/site_perl/Tk/Pretty.pm
    /usr/lib/perl5/Symbol.pm
    /usr/lib/perl5/site_perl/Tk/Frame.pm
    /usr/lib/perl5/site_perl/Tk/Toplevel.pm
    /usr/lib/perl5/strict.pm
    /usr/lib/perl5/Exporter.pm
    /usr/lib/perl5/vars.pm
    /usr/lib/perl5/site_perl/auto/Tk/Wm/autosplit.ix
    /usr/lib/perl5/site_perl/auto/Tk/Widget/autosplit.ix
    /usr/lib/perl5/site_perl/Tk.pm
    /usr/lib/perl5/i386-linux/5.00404/DynaLoader.pm
    /usr/lib/perl5/site_perl/auto/Tk/Frame/autosplit.ix
    /usr/lib/perl5/site_perl/auto/Tk/Toplevel/autosplit.ix
    /usr/lib/perl5/Carp.pm
    /usr/lib/perl5/site_perl/auto/Tk/autosplit.ix
    /usr/lib/perl5/site_perl/Tk/CmdLine.pm
    /usr/lib/perl5/site_perl/Tk/MainWindow.pm
    /usr/lib/perl5/site_perl/Tk/Submethods.pm
    /usr/lib/perl5/site_perl/Tk/Configure.pm
    /usr/lib/perl5/AutoLoader.pm
    /usr/lib/perl5/site_perl/Tk/Derived.pm
    /usr/lib/perl5/site_perl/Tk/Image.pm
    /usr/lib/perl5/site_perl/Tk/Wm.pm
    /usr/lib/perl5/site_perl/Tk/Widget.pm
</pre>

<h2>NOTE</h2>

 If the programmers used a delayed <tt>&quot;require&quot;</tt>, those files won't show up. Furthermore, this doesn't show all possible files that get opened, just those that those up in <tt>%INC</tt>. Most systems have a way to trace system calls. You can use this to find the real answer. First, get a baseline with no modules loaded. 

 <pre><code>
$ strace perl - e 1 2 &gt; &amp;1 | perl - nle '/^open\("(.*?)".* = [^-]/ &amp;&amp; print $1' / etc / ld.so.cache / lib / libnsl.so .1 / lib / libdb.so .2 / lib / libdl.so .2 / lib / libm.so .6 / lib / libc.so .6 / lib / libcrypt.so .1 / dev / null $ strace perl - e 1 2 &gt; &amp;1 | grep - c '^open.*= [^-]' 8
</code></pre> 

 Now add module loads and see what you get: 

 <pre><code>
$ strace perl - MIO::Socket - e 1 2 &gt; &amp;1 | grep - c '^open.*= [^-]' 24 $ strace perl - MTk - e 1 2 &gt; &amp;1 | grep - c '^open.*= [^-]' 35
</code></pre>

<h2>SEE ALSO</h2>

 Devel::Loaded, <i><a HREF="/docs/linux/man/1-plxload/">plxload</a></i>(1).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


