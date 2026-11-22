---

title: "perlepoc(1)"
name: "perlepoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlepoc/"
---

perlepoc - Perl for EPOC 

<h2>SYNOPSIS</h2>

 Perl 5 README file for the EPOC Release 5 operating system.

<h2>INTRODUCTION</h2>

 EPOC is an OS for palmtops and mobile phones. For more information look at: &lt;<a rel="nofollow" HREF="http://www.symbian.com/">http://www.symbian.com/</a>&gt; 

 This is a port of perl to the epocemx SDK by Eberhard Mattes, which itself uses the SDK by symbian. Essentially epocemx it is a POSIX look alike environment for the EPOC OS. For more information look at: &lt;<a rel="nofollow" HREF="http://epocemx.sourceforge.net/">http://epocemx.sourceforge.net/</a>&gt; 

 perl and epocemx runs on Epoc Release 5 machines: Psion 5mx, 5mx Pro, Psion Revo, Psion Netbook and on the Ericsson M128. It may run on Epoc Release 3 Hardware (Series 5 classic), too. For more information about this hardware please refer to &lt;<a rel="nofollow" HREF="http://www.psion.com/">http://www.psion.com/</a>&gt; 

 Vendors which like to have support for their devices are free to send me a sample.

<h2>INSTALLING PERL ON EPOC</h2>

 You can download a ready-to-install version from &lt;<a rel="nofollow" HREF="http://www.oflebbe.de/perl/perl5.html">http://www.oflebbe.de/perl/perl5.html</a>&gt; 

 You will need at least ~6MB free space in order to install and run perl. 

 Please install the emxusr.sis package from &lt;<a rel="nofollow" HREF="http://epocemx.sourceforge.net/">http://epocemx.sourceforge.net/</a>&gt; first. 

 Install perl.sis on the EPOC machine. If you do not know how to do that, consult your PsiWin documentation. 

 Perl itself and its standard library is using 4 MB disk space. Unicode support and some other modules are left out. (For details, please look into epoc/createpkg.pl). If you like to use these modules, you are free to copy them from a current perl release.

<h2>STARTING PERL ON EPOC</h2>

 Please use the epocemx shell to start perl. perl integrates with the conventions of epocemx.

<h3>Features of Perl on Epoc</h3>

 The built-in function EPOC::getcwd returns the current directory.

<h3>Restrictions of Perl on Epoc</h3>

 Features are left out, because of restrictions of the POSIX support in EPOC:
<dl>
<dt>&bull;
</dt><dd> socket IO is only implemented poorly. You can only use sysread and syswrite on them. The commands read, write, print, &lt;&gt; do not work for sockets. This may change iff epocemx supports sockets.
</dd><dt>&bull;
</dt><dd> kill, alarm and signals. Do not try to use them. This may be impossible to implement on EPOC.
</dd><dt>&bull;
</dt><dd> select is missing.
</dd><dt>&bull;
</dt><dd> binmode does not exist. (No CR LF to LF translation for text files)
</dd><dt>&bull;
</dt><dd> EPOC does not handle the notion of current drive and current directory very well (i.e. not at all, but it tries hard to emulate one). See PATH.
</dd><dt>&bull;
</dt><dd> Heap is limited to 4MB.
</dd><dt>&bull;
</dt><dd> Dynamic loading is not implemented.</dd></dl>

<h3>Compiling Perl 5 on the EPOC cross compiling environment</h3>

 Sorry, this is far too short.
<dl>
<dt>&bull;
</dt><dd> You will need the epocemx SDK from Eberhard Mattes.
</dd><dt>&bull;
</dt><dd> Get the Perl sources from your nearest CPAN site.
</dd><dt>&bull;
</dt><dd> Unpack the sources.
</dd><dt>&bull;
</dt><dd> Build a native perl from this sources... Make sure to save the miniperl executable as miniperl.native. 
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
</pre></dd></dl>

<h2>SUPPORT STATUS OF PERL ON EPOC</h2>

 I'm offering this port ``as is''. You can ask me questions, but I can't guarantee I'll be able to answer them. Since the port to epocemx is quite new, please check the web for updates first. 

 Very special thanks to Eberhard Mattes for epocemx.

<h2>AUTHOR</h2>

 Olaf Flebbe &lt;olaf [at] oflebbe.de&gt; &lt;<a rel="nofollow" HREF="http://www.oflebbe.de/perl/perl5.html">http://www.oflebbe.de/perl/perl5.html</a>&gt;

<h2>LAST UPDATE</h2>

 2003-01-18 



<dt><a HREF="#lbAJ">SUPPORT STATUS OF PERL ON EPOC</a>
</dt><dd>
</dd><dt><a HREF="#lbAK">AUTHOR</a>
</dt><dd>
</dd><dt><a HREF="#lbAL">LAST UPDATE</a>
</dt><dd></dd></dl>
