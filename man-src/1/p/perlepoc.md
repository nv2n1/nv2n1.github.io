---
title: "perlepoc(1)"
name: "perlepoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlepoc/"
---

<h2 class="name">NAME</h2>
 

 perlepoc - Perl for EPOC 

<h2>SYNOPSIS</h2>

 Perl 5 <font SIZE="-1">README</font> file for the <font SIZE="-1">EPOC</font> Release 5 operating system.

<h2>INTRODUCTION</h2>

 <font SIZE="-1">EPOC</font> is an <font SIZE="-1">OS</font> for palmtops and mobile phones. For more information look at: &lt;<a rel="nofollow" HREF="http://www.symbian.com/">http://www.symbian.com/</a>&gt; 

 This is a port of perl to the epocemx <font SIZE="-1">SDK</font> by Eberhard Mattes, which itself uses the <font SIZE="-1">SDK</font> by symbian. Essentially epocemx it is a <font SIZE="-1">POSIX</font> look alike environment for the <font SIZE="-1">EPOC</font> <font SIZE="-1">OS</font>. For more information look at: &lt;<a rel="nofollow" HREF="http://epocemx.sourceforge.net/">http://epocemx.sourceforge.net/</a>&gt; 

 perl and epocemx runs on Epoc Release 5 machines: Psion 5mx, 5mx Pro, Psion Revo, Psion Netbook and on the Ericsson M128. It may run on Epoc Release 3 Hardware (Series 5 classic), too. For more information about this hardware please refer to &lt;<a rel="nofollow" HREF="http://www.psion.com/">http://www.psion.com/</a>&gt; 

 Vendors which like to have support for their devices are free to send me a sample.

<h2>INSTALLING PERL ON EPOC</h2>

 You can download a ready-to-install version from &lt;<a rel="nofollow" HREF="http://www.oflebbe.de/perl/perl5.html">http://www.oflebbe.de/perl/perl5.html</a>&gt; 

 You will need at least ~6MB free space in order to install and run perl. 

 Please install the emxusr.sis package from &lt;<a rel="nofollow" HREF="http://epocemx.sourceforge.net/">http://epocemx.sourceforge.net/</a>&gt; first. 

 Install perl.sis on the <font SIZE="-1">EPOC</font> machine. If you do not know how to do that, consult your PsiWin documentation. 

 Perl itself and its standard library is using 4 <font SIZE="-1">MB</font> disk space. Unicode support and some other modules are left out. (For details, please look into epoc/createpkg.pl). If you like to use these modules, you are free to copy them from a current perl release.

<h2>STARTING PERL ON EPOC</h2>

 Please use the epocemx shell to start perl. perl integrates with the conventions of epocemx.

<h3>Features of Perl on Epoc</h3>

 The built-in function EPOC::getcwd returns the current directory.

<h3>Restrictions of Perl on Epoc</h3>

 Features are left out, because of restrictions of the <font SIZE="-1">POSIX</font> support in <font SIZE="-1">EPOC:</font>
<dl>
<dt>&bull;
<dd> socket <font SIZE="-1">IO</font> is only implemented poorly. You can only use sysread and syswrite on them. The commands read, write, print, &lt;&gt; do not work for sockets. This may change iff epocemx supports sockets.
<dt>&bull;
<dd> kill, alarm and signals. Do not try to use them. This may be impossible to implement on <font SIZE="-1">EPOC</font>.
<dt>&bull;
<dd> select is missing.
<dt>&bull;
<dd> binmode does not exist. (No <font SIZE="-1">CR</font> <font SIZE="-1">LF</font> to <font SIZE="-1">LF</font> translation for text files)
<dt>&bull;
<dd> <font SIZE="-1">EPOC</font> does not handle the notion of current drive and current directory very well (i.e. not at all, but it tries hard to emulate one). See <font SIZE="-1">PATH</font>.
<dt>&bull;
<dd> Heap is limited to 4MB.
<dt>&bull;
<dd> Dynamic loading is not implemented.</dl>

<h3>Compiling Perl 5 on the <font SIZE="-1">EPOC</font> cross compiling environment</h3>

 Sorry, this is far too short.
<dl>
<dt>&bull;
<dd> You will need the epocemx <font SIZE="-1">SDK</font> from Eberhard Mattes.
<dt>&bull;
<dd> Get the Perl sources from your nearest <font SIZE="-1">CPAN</font> site.
<dt>&bull;
<dd> Unpack the sources.
<dt>&bull;
<dd> Build a native perl from this sources... Make sure to save the miniperl executable as miniperl.native. 

 Start again from scratch 

 <pre>
      cp epoc/* .
      ./Configure -S
      make 
      cp miniperl.native miniperl
      touch miniperl.exe
      make
      perl createpkg.pl 
      emxsis perl.pkg perl.sis
</pre></dl>

<h2>SUPPORT STATUS OF PERL ON EPOC</h2>

 I'm offering this port ``as is''. You can ask me questions, but I can't guarantee I'll be able to answer them. Since the port to epocemx is quite new, please check the web for updates first. 

 Very special thanks to Eberhard Mattes for epocemx.

<h2>AUTHOR</h2>

 Olaf Flebbe &lt;olaf [at] oflebbe.de&gt; &lt;<a rel="nofollow" HREF="http://www.oflebbe.de/perl/perl5.html">http://www.oflebbe.de/perl/perl5.html</a>&gt;

<h2>LAST UPDATE</h2>

 2003-01-18 

<h2>Index</h2>



<dt><a HREF="#lbAJ">SUPPORT STATUS OF PERL ON EPOC</a>
<dd>
<dt><a HREF="#lbAK">AUTHOR</a>
<dd>
<dt><a HREF="#lbAL">LAST UPDATE</a>
<dd></dl>
