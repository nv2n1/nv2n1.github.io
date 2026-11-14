---
title: "pmexp(1)"
name: "pmexp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmexp/"
---

<h2 class="name">NAME</h2>
 

 pmexp - show a module's exports 

<h2>DESCRIPTION</h2>

 Given a module name, this program identifies which symbols are automatically exported (in that package's <tt>@EXPORT</tt>), those which are optionally exported (in that package's <tt>@EXPORT_OK</tt>), and also lists out the import groups (in that package's <tt>%EXPORT_TAGS</tt> hash).

<h2>EXAMPLES</h2>

 <pre>
    $ pmexp Text::ParseWords
    Text::ParseWords automatically exports shellwords, quotewords, nested_quotewords, and parse_line
    Text::ParseWords optionally exports old_shellwords
    $ pmexp Text::Wrap
    Text::Wrap automatically exports wrap and fill
    Text::Wrap optionally exports $columns, $break, and $huge
    $ pmexp Fcntl
    Fcntl automatically exports FD_CLOEXEC, F_DUPFD, F_EXLCK, F_GETFD, F_GETFL, F_GETLK, F_GETLK64, F_GETOWN, F_POSIX, F_RDLCK, F_SETFD, F_SETFL, F_SETLK, F_SETLK64, F_SETLKW, F_SETLKW64, F_SETOWN, F_SHLCK, F_UNLCK, F_WRLCK, O_ACCMODE, O_APPEND, O_ASYNC, O_BINARY, O_CREAT, O_DEFER, O_DSYNC, O_EXCL, O_EXLOCK, O_LARGEFILE, O_NDELAY, O_NOCTTY, O_NONBLOCK, O_RDONLY, O_RDWR, O_RSYNC, O_SHLOCK, O_SYNC, O_TEXT, O_TRUNC, and O_WRONLY
    Fcntl optionally exports FAPPEND, FASYNC, FCREAT, FDEFER, FEXCL, FNDELAY, FNONBLOCK, FSYNC, FTRUNC, LOCK_EX, LOCK_NB, LOCK_SH, and LOCK_UN
    Fcntl export tag `Fcompat' includes FAPPEND, FASYNC, FCREAT, FDEFER, FEXCL, FNDELAY, FNONBLOCK, FSYNC, and FTRUNC
    Fcntl export tag `flock' includes LOCK_SH, LOCK_EX, LOCK_NB, and LOCK_UN
</pre>

<h2>BUGS</h2>

 The output formatting should be nicer, perhaps using <tt>&quot;format&quot;</tt> and <tt>&quot;write&quot;</tt>.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-pmeth/">pmeth</a></i>(1), <i><a HREF="/docs/linux/man/1-perlmod/">perlmod</a></i>(1), <i><a HREF="/docs/linux/man/3-exporter/">Exporter</a></i>(3).

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


