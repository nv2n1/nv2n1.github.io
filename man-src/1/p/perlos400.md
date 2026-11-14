---
title: "perlos400(1)"
name: "perlos400"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlos400/"
---

<h2 class="name">NAME</h2>
 

 perlos400 - Perl version 5 on OS/400 

 This document needs to be updated, but we don't know what it should say. Please email comments to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. 

<h2>DESCRIPTION</h2>

 This document describes various features of <font SIZE="-1">IBM</font>'s <font SIZE="-1">OS/400</font> operating system that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs. 

 By far the easiest way to build Perl for <font SIZE="-1">OS/400</font> is to use the <font SIZE="-1">PASE</font> (Portable Application Solutions Environment), for more information see &lt;<a rel="nofollow" HREF="http://www.iseries.ibm.com/developer/factory/pase/index.html">http://www.iseries.ibm.com/developer/factory/pase/index.html</a>&gt; This environment allows one to use <font SIZE="-1">AIX</font> APIs while programming, and it provides a runtime that allows <font SIZE="-1">AIX</font> binaries to execute directly on the PowerPC iSeries.

<h3>Compiling Perl for <font SIZE="-1">OS/400 PASE</font></h3>

 The recommended way to build Perl for the <font SIZE="-1">OS/400 PASE</font> is to build the Perl 5 source code (release 5.8.1 or later) under <font SIZE="-1">AIX.</font> 

 The trick is to give a special parameter to the Configure shell script when running it on <font SIZE="-1">AIX:</font> 

 <pre>
  sh Configure -DPASE ...
</pre> 

 The default installation directory of Perl under <font SIZE="-1">PASE</font> is /QOpenSys/perl. This can be modified if needed with Configure parameter -Dprefix=/some/dir. 

 Starting from <font SIZE="-1">OS/400 V5R2</font> the <font SIZE="-1">IBM</font> Visual Age compiler is supported on <font SIZE="-1">OS/400 PASE,</font> so it is possible to build Perl natively on <font SIZE="-1">OS/400.</font> The easier way, however, is to compile in <font SIZE="-1">AIX,</font> as just described. 

 If you don't want to install the compiled Perl in <font SIZE="-1">AIX</font> into /QOpenSys (for packaging it before copying it to <font SIZE="-1">PASE</font>), you can use a Configure parameter: -Dinstallprefix=/tmp/QOpenSys/perl. This will cause the ``make install'' to install everything into that directory, while the installed files still think they are (will be) in /QOpenSys/perl. 

 If building natively on <font SIZE="-1">PASE,</font> please do the build under the /QOpenSys directory, since Perl is happier when built on a case sensitive filesystem.

<h3>Installing Perl in <font SIZE="-1">OS/400 PASE</font></h3>

 If you are compiling on <font SIZE="-1">AIX,</font> simply do a ``make install'' on the <font SIZE="-1">AIX</font> box. Once the install finishes, tar up the /QOpenSys/perl directory. Transfer the tarball to the <font SIZE="-1">OS/400</font> using <font SIZE="-1">FTP</font> with the following commands: 

 <pre>
  &gt; binary
  &gt; site namefmt 1
  &gt; put perl.tar /QOpenSys
</pre> 

 Once you have it on, simply bring up a <font SIZE="-1">PASE</font> shell and extract the tarball. 

 If you are compiling in <font SIZE="-1">PASE,</font> then ``make install'' is the only thing you will need to do. 

 The default path for perl binary is /QOpenSys/perl/bin/perl. You'll want to symlink /QOpenSys/usr/bin/perl to this file so you don't have to modify your path.

<h3>Using Perl in <font SIZE="-1">OS/400 PASE</font></h3>

 Perl in <font SIZE="-1">PASE</font> may be used in the same manner as you would use Perl on <font SIZE="-1">AIX.</font> 

 Scripts starting with #!/usr/bin/perl should work if you have /QOpenSys/usr/bin/perl symlinked to your perl binary. This will not work if you've done a setuid/setgid or have environment variable PASE_EXEC_QOPENSYS=``N''. If you have V5R1, you'll need to get the latest PTFs to have this feature. Scripts starting with #!/QOpenSys/perl/bin/perl should always work.

<h3>Known Problems</h3>

 When compiling in <font SIZE="-1">PASE,</font> there is no ``oslevel'' command. Therefore, you may want to create a script called ``oslevel'' that echoes the level of <font SIZE="-1">AIX</font> that your version of <font SIZE="-1">PASE</font> runtime supports. If you're unsure, consult your documentation or use ``4.3.3.0''. 

 If you have test cases that fail, check for the existence of spool files. The test case may be trying to use a syscall that is not implemented in <font SIZE="-1">PASE.</font> To avoid the <font SIZE="-1">SIGILL,</font> try setting the <font SIZE="-1">PASE_SYSCALL_NOSIGILL</font> environment variable or have a handler for the <font SIZE="-1">SIGILL.</font> If you can compile programs for <font SIZE="-1">PASE,</font> run the config script and edit config.sh when it gives you the option. If you want to remove <b>fchdir()</b>, which isn't implement in V5R1, simply change the line that says: 

 d_fchdir='define' 

 to 

 d_fchdir='undef' 

 and then compile Perl. The places where <b>fchdir()</b> is used have alternatives for systems that do not have <b>fchdir()</b> available.

<h3>Perl on <font SIZE="-1">ILE</font></h3>

 There exists a port of Perl to the <font SIZE="-1">ILE</font> environment. This port, however, is based quite an old release of Perl, Perl 5.00502 (August 1998). (As of July 2002 the latest release of Perl is 5.8.0, and even 5.6.1 has been out since April 2001.) If you need to run Perl on <font SIZE="-1">ILE,</font> though, you may need this older port: &lt;<a rel="nofollow" HREF="http://www.cpan.org/ports/#os400">http://www.cpan.org/ports/#os400</a>&gt; Note that any Perl release later than 5.00502 has not been ported to <font SIZE="-1">ILE.</font> 

 If you need to use Perl in the <font SIZE="-1">ILE</font> environment, you may want to consider using <b>Qp2RunPase()</b> to call the <font SIZE="-1">PASE</font> version of Perl.

<h2>AUTHORS</h2>

 Jarkko Hietaniemi &lt;jhi [at] iki.fi&gt; Bryan Logan &lt;bryanlog [at] us.ibm.com&gt; David Larson &lt;larson1 [at] us.ibm.com&gt; 

<h2>Index</h2>



<dt><a HREF="#lbAI">AUTHORS</a>
<dd></dl>
