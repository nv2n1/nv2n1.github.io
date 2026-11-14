---
title: "perlbeos(1)"
name: "perlbeos"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlbeos/"
---

<h2 class="name">NAME</h2>
 

 perlbeos - Perl version 5.8+ on BeOS 

<h2>DESCRIPTION</h2>

 This file contains instructions how to build Perl under BeOS and lists known problems.

<h2>BUILD AND INSTALL</h2>

<h3>Requirements</h3>

 I have built and tested Perl 5.8.6 and 5.9.1 under BeOS R5 x86 net server. I can't say anything with regard to <font SIZE="-1">PPC</font>. Since Perl 5.8.0 had been released for BeOS <font SIZE="-1">BONE</font>, I suspect, there is a good chance, that it still compiles on a <font SIZE="-1">BONE</font> system. The only change I've made, that affects <font SIZE="-1">BONE</font> systems is the recognition of whether it is a <font SIZE="-1">BONE</font> system or not in <i>hints/beos.sh</i>. Now network socket support should remain enabled on <font SIZE="-1">BONE</font> systems. This might as well break the build, though. 

 As more recent versions of autoconf require <i>flock()</i> support, I wrote a <i>flock()</i> emulation (flock_server) and released it on BeBits: 

 <pre>
        <a rel="nofollow" HREF="http://www.bebits.com/app/4030">http://www.bebits.com/app/4030</a>
</pre> 

 If you want to build a Perl with <i>flock()</i> support, you have to install this package first.

<h3>Configure</h3>

 With <i>flock()</i> support: 

 <pre>
        CFLAGS=-I/path/to/flock/server/headers ./configure.gnu \
                --prefix=/boot/home/config
</pre> 

 Replace <tt>&quot;/path/to/flock/server/headers&quot;</tt> with the path to the directory containing the <tt>&quot;flock.h&quot;</tt> header. 

 Without <i>flock()</i> support: 

 <pre>
        ./configure.gnu --prefix=/boot/home/config
</pre>

<h3>Build</h3>

 With <i>flock()</i> support: 

 <pre>
        make LDLOADLIBS=&quot;-lnet -lflock&quot;
</pre> 

 Without <i>flock()</i> support: 

 <pre>
        make LDLOADLIBS=&quot;-lnet&quot;
</pre> 

 <tt>&quot;-lnet&quot;</tt> is needed on net server systems only and if the compiler doesn't add it automatically (Be's R5 gcc does, Oliver Tappe's gcc 2.95.3 does not).

<h3>Install</h3>

 Install all perl files: 

 <pre>
        make install
</pre> 

 Create a symlink for libperl: 

 <pre>
        cd ~/config/lib; ln -s perl5/5.8.6/BePC-beos/CORE/libperl.so .
</pre> 

 Replace <tt>5.8.6</tt> with your respective version of Perl.

<h2>KNOWN PROBLEMS</h2>

<dl>
<dt>&bull;
<dd> Network socket support is disabled for BeOS R5 net server. I didn't dare yet to try enabling it and see what problems occur.
<dt>&bull;
<dd> The <font SIZE="-1">LFS</font> (large file support) tests (<i>t/op/lfs</i> and <i>xt/Fcntl/t/syslfs</i>) are disabled as seeking beyond 2 <font SIZE="-1">GB</font> is broken according to jhi [at] iki.fi who was the last one checking the BeOS port and updating this file before me. Haven't checked this myself.
<dt>&bull;
<dd> The <i>t/io/fflush</i> test fails at #6. As far as I can tell, this is caused by a bug in the BeOS pipes implementation that occurs when starting other child processes. In the particular test case a <tt>&quot;system(&quot;perl -e 0&quot;)&quot;</tt> flushes the stdout pipe of another child process.
<dt>&bull;
<dd> The <i>ext/POSIX/t/waitpid</i> test fails at #1. After all child processes are gone BeOS' waitpid(-1,...) returns 0 instead of -1 (as it should). No idea how to fix this.</dl>

<h2>CONTACT</h2>

 For BeOS specifics problems feel free to mail to: Ingo Weinhold &lt;bonefish [at] cs.tu-berlin.de&gt; 

 Last update: 2004-12-16 

<h2>Index</h2>


