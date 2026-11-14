---
title: "perlsymbian(1)"
name: "perlsymbian"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsymbian/"
description: "perlsymbian – Perl version 5 on Symbian OS"
---

<h2 class="name">NAME</h2>
<p> perlsymbian &#8211; Perl version 5 on Symbian OS </p>
<h2>DESCRIPTION</h2>
<p> This document describes various features of the Symbian operating system that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font><code> this port (as of 0.4.1) does not compile into a Symbian </code><font SIZE="-1"><code>OS GUI</code></font><code> application, but instead it results in a Symbian </code><font SIZE="-1"><code>DLL.</code></font> The <font SIZE="-1">DLL</font> includes a C<font SIZE="-2">++</font> class called CPerlBase, which one can then (derive from and) use to embed Perl into applications, see <i>symbian/README</i>. </p>
<p> The base port of Perl to Symbian only implements the basic POSIX-like functionality; it does not implement any further Symbian or Series 60, Series 80, or <font SIZE="-1">UIQ</font> bindings for Perl. </p>
<p> It is also possible to generate Symbian executables for &#8220;miniperl&#8221; and &#8220;perl&#8221;, but since there is no standard command line interface for Symbian (nor full keyboards in the devices), these are useful mainly as demonstrations.</p>
<h3>Compiling Perl on Symbian</h3>
<p> (0) You need to have the appropriate Symbian <font SIZE="-1">SDK</font> installed. </p>
<p> These instructions have been tested under various Nokia Series 60 Symbian SDKs (1.2 to 2.6, 2.8 should also work, 1.2 compiles but does not work), Series 80 2.0, and Nokia 7710 (Series 90) <font SIZE="-1">SDK.</font> You can get the SDKs from Forum Nokia (&lt;<a rel="nofollow" href="http://www.forum.nokia.com/">http://www.forum.nokia.com/</a>&gt;). A very rough port (&#8220;it compiles&#8221;) to <font SIZE="-1">UIQ 2.1</font> has also been made. </p>
<p> A prerequisite for any of the SDKs is to install ActivePerl from ActiveState, &lt;<a rel="nofollow" href="http://www.activestate.com/Products/ActivePerl/">http://www.activestate.com/Products/ActivePerl/</a>&gt; </p>
<p> Having the <font SIZE="-1">SDK</font> installed also means that you need to have either the Metrowerks CodeWarrior installed (2.8 and 3.0 were used in testing) or the Microsoft Visual C<font SIZE="-2">++</font> 6.0 installed (<font SIZE="-1">SP3</font> minimum, <font SIZE="-1">SP5</font> recommended). </p>
<p> Note that for example the Series 60 2.0 <font SIZE="-1">VC SDK</font> installation talks about ActivePerl build 518, which does no more (as of mid-2005) exist at the ActiveState website. The ActivePerl 5.8.4 build 810 was used successfully for compiling Perl on Symbian. The 5.6.x ActivePerls do not work. </p>
<p> Other SDKs or compilers like Visual.NET, command-line-only Visual.NET, Borland, GnuPoc, or sdk2unix have not been tried. </p>
<p> These instructions almost certainly won&#8217;t work with older Symbian releases or other SDKs. Patches to get this port running in other releases, SDKs, compilers, platforms, or devices are naturally welcome. </p>
<p> (1) Get a Perl source code distribution (for example the file perl-5.9.2.tar.gz is fine) from &lt;<a rel="nofollow" href="http://www.cpan.org/src/">http://www.cpan.org/src/</a>&gt; and unpack it in your the C:/Symbian directory of your Windows system. </p>
<p> (2) Change to the perl source directory. </p>
<pre>
    cd c:\Symbian\perl-5.x.x
</pre>
<p> (3) Run the following script using the perl coming with the <font SIZE="-1">SDK</font> </p>
<pre>
    perl symbian
