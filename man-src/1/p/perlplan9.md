---
title: "perlplan9(1)"
name: "perlplan9"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlplan9/"
---

<h2 class="name">NAME</h2>
 

 perlplan9 - Plan 9-specific documentation for Perl 

<h2>DESCRIPTION</h2>

 These are a few notes describing features peculiar to Plan 9 Perl. As such, it is not intended to be a replacement for the rest of the Perl 5 documentation (which is both copious and excellent). If you have any questions to which you can't find answers in these man pages, contact Luther Huffman at lutherh [at] stratcom.com and we'll try to answer them.

<h3>Invoking Perl</h3>

 Perl is invoked from the command line as described in perl. Most perl scripts, however, do have a first line such as ``#!/usr/local/bin/perl''. This is known as a shebang (shell-bang) statement and tells the <font SIZE="-1">OS</font> shell where to find the perl interpreter. In Plan 9 Perl this statement should be ``#!/bin/perl'' if you wish to be able to directly invoke the script by its name. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Alternatively, you may invoke perl with the command&nbsp;``Perl'' instead of ``perl''. This will produce Acme-friendly error messages of the form ``filename:18''. 

 Some scripts, usually identified with a *.PL extension, are self-configuring and are able to correctly create their own shebang path from config information located in Plan 9 Perl. These you won't need to be worried about.

<h3>What's in Plan 9 Perl</h3>

 Although Plan 9 Perl currently only provides static loading, it is built with a number of useful extensions. These include Opcode, FileHandle, Fcntl, and <font SIZE="-1">POSIX.</font> Expect to see others (and DynaLoading!) in the future.

<h3>What's not in Plan 9 Perl</h3>

 As mentioned previously, dynamic loading isn't currently available nor is MakeMaker. Both are high-priority items.

<h3>Perl5 Functions not currently supported in Plan 9 Perl</h3>

 Some, such as <tt>&quot;chown&quot;</tt> and <tt>&quot;umask&quot;</tt> aren't provided because the concept does not exist within Plan 9. Others, such as some of the socket-related functions, simply haven't been written yet. Many in the latter category may be supported in the future. 

 The functions not currently implemented include: 

 <pre>
    chown, chroot, dbmclose, dbmopen, getsockopt, 
    setsockopt, recvmsg, sendmsg, getnetbyname, 
    getnetbyaddr, getnetent, getprotoent, getservent, 
    sethostent, setnetent, setprotoent, setservent, 
    endservent, endnetent, endprotoent, umask
</pre> 

 There may be several other functions that have undefined behavior so this list shouldn't be considered complete.

<h3>Signals in Plan 9 Perl</h3>

 For compatibility with perl scripts written for the Unix environment, Plan 9 Perl uses the <font SIZE="-1">POSIX</font> signal emulation provided in Plan 9's <font SIZE="-1">ANSI POSIX</font> Environment (<font SIZE="-1">APE</font>). Signal stacking isn't supported. The signals provided are: 

 <pre>
    SIGHUP, SIGINT, SIGQUIT, SIGILL, SIGABRT,
    SIGFPE, SIGKILL, SIGSEGV, SIGPIPE, SIGPIPE, SIGALRM, 
    SIGTERM, SIGUSR1, SIGUSR2, SIGCHLD, SIGCONT,
    SIGSTOP, SIGTSTP, SIGTTIN, SIGTTOU
</pre>

<h2>COMPILING AND INSTALLING PERL ON PLAN 9</h2>

 <font SIZE="-1">WELCOME</font> to Plan 9 Perl, brave soul! 

 <pre>
   This is a preliminary alpha version of Plan 9 Perl. Still to be
implemented are MakeMaker and DynaLoader. Many perl commands are
missing or currently behave in an inscrutable manner. These gaps will,
with perseverance and a modicum of luck, be remedied in the near
future.To install this software:
</pre> 

 1. Create the source directories and libraries for perl by running the plan9/setup.rc command (i.e., located in the plan9 subdirectory). Note: the setup routine assumes that you haven't dearchived these files into /sys/src/cmd/perl. After running setup.rc you may delete the copy of the source you originally detarred, as source code has now been installed in /sys/src/cmd/perl. If you plan on installing perl binaries for all architectures, run ``setup.rc -a''. 

 2. After making sure that you have adequate privileges to build system software, from /sys/src/cmd/perl/5.00301 (adjust version appropriately) run: 

 <pre>
        mk install
</pre> 

 If you wish to install perl versions for all architectures (68020, mips, sparc and 386) run: 

 <pre>
        mk installall
</pre> 

 3. Wait. The build process will take a *long* time because perl bootstraps itself. A 75MHz Pentium, 16MB <font SIZE="-1">RAM</font> machine takes roughly 30 minutes to build the distribution from scratch.

<h3>Installing Perl Documentation on Plan 9</h3>

 This perl distribution comes with a tremendous amount of documentation. To add these to the built-in manuals that come with Plan 9, from /sys/src/cmd/perl/5.00301 (adjust version appropriately) run: 

 <pre>
        mk man
</pre> 

 To begin your reading, start with: 

 <pre>
        man perl
</pre> 

 This is a good introduction and will direct you towards other man pages that may interest you. 

 (Note: ``mk man'' may produce some extraneous noise. Fear not.)

<h2>BUGS</h2>

 ``As many as there are grains of sand on all the beaches of the world . . .'' - Carl Sagan

<h2>Revision date</h2>

 This document was revised 09-October-1996 for Perl 5.003_7.

<h2>AUTHOR</h2>

 Direct questions, comments, and the unlikely bug report (ahem) direct comments toward: 

 Luther Huffman, lutherh [at] stratcom.com, Strategic Computer Solutions, Inc. 

<h2>Index</h2>


