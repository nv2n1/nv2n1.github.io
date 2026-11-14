---
title: "pminst(1)"
name: "pminst"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pminst/"
description: "pminst – find modules whose names match this pattern"
---

<h2 class="name">NAME</h2>
<p> pminst &#8211; find modules whose names match this pattern </p>
<h2>SYNOPSIS</h2>
<p> pminst [<code>-s</code>] [<code>-l</code>] [<i>pattern</i>]</p>
<h2>DESCRIPTION</h2>
<p> Without arguments, show the names of all installed modules. Given a pattern, show all module names that match it. The <code>-l</code> flag will show the full pathname. The <code>-s</code> flag will separate the base directory from <tt>@INC</tt> from the module portion itself.</p>
<h2>EXAMPLES</h2>
<pre>
    $ pminst
    (lists all installed modules)
    $ pminst Carp
    CGI::Carp
    Carp
    $ pminst ^IO::
    IO::Socket::INET
    IO::Socket::UNIX
    IO::Select
    IO::Socket
    IO::Poll
    IO::Handle
    IO::Pipe
    IO::Seekable
    IO::Dir
    IO::File
    $ pminst '(?i)io'
    IO::Socket::INET
    IO::Socket::UNIX
    IO::Select
    IO::Socket
    IO::Poll
    IO::Handle
    IO::Pipe
    IO::Seekable
    IO::Dir
    IO::File
    IO
    Pod::Functions
  The -s flag provides output with the directory separated
  by a space:
    $ pminst -s | sort +1
    (lists all modules, sorted by name, but with where they 
     came from)
    $ oldperl -S pminst -s IO
    /usr/lib/perl5/i386-linux/5.00404 IO::File
    /usr/lib/perl5/i386-linux/5.00404 IO::Handle
    /usr/lib/perl5/i386-linux/5.00404 IO::Pipe
    /usr/lib/perl5/i386-linux/5.00404 IO::Seekable
    /usr/lib/perl5/i386-linux/5.00404 IO::Select
    /usr/lib/perl5/i386-linux/5.00404 IO::Socket
    /usr/lib/perl5/i386-linux/5.00404 IO
    /usr/lib/perl5/site_perl LWP::IO
    /usr/lib/perl5/site_perl LWP::TkIO
    /usr/lib/perl5/site_perl Tk::HTML::IO
    /usr/lib/perl5/site_perl Tk::IO
    /usr/lib/perl5/site_perl IO::Stringy
    /usr/lib/perl5/site_perl IO::Wrap
    /usr/lib/perl5/site_perl IO::ScalarArray
    /usr/lib/perl5/site_perl IO::Scalar
    /usr/lib/perl5/site_perl IO::Lines
    /usr/lib/perl5/site_perl IO::WrapTie
    /usr/lib/perl5/site_perl IO::AtomicFile
  The -l flag gives full paths:
    $ filsperl -S pminst -l Thread
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/Thread/Queue.pm
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/Thread/Semaphore.pm
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/Thread/Signal.pm
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/Thread/Specific.pm
    /usr/local/filsperl/lib/5.00554/i686-linux-thread/Thread.pm
</pre>
<h2>AUTHORS and COPYRIGHTS</h2>
<p> Copyright (C) 1999 Tom Christiansen. </p>
<p> Copyright (C) 2006-2014 Mark Leighton Fisher.</p>
<h2>LICENSE</h2>
<p> This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl &#8220;Artistic License&#8221;. (This is the Perl 5 licensing scheme.) </p>
<p> Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl &#8220;Artistic License&#8221;. </p>
<h2>Index</h2>
