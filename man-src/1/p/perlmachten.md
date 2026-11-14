---
title: "perlmachten(1)"
name: "perlmachten"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmachten/"
---

<h2 class="name">NAME</h2>
 

 README.machten - Perl version 5 on Power MachTen systems 

<h2>DESCRIPTION</h2>

 This document describes how to build Perl 5 on Power MachTen systems, and discusses a few wrinkles in the implementation.

<h2>Perl version 5.8.x and greater not supported</h2>

 <b>Power MachTen is not supported by versions of Perl later than 5.6.x.</b> If you wish to build a version from the 5.6 track, please obtain a source distribution from the archive at &lt;<a rel="nofollow" HREF="http://cpan.org/src/5.0/">http://cpan.org/src/5.0/</a>&gt; and follow the instructions in its <font SIZE="-1">README</font>.machten file. 

 MachTen is no longer supported by its developers, Tenon Intersystems. A <font SIZE="-1">UNIX</font> environment hosted on Mac <font SIZE="-1">OS</font> Classic, MachTen has been superseded by Mac <font SIZE="-1">OS</font> X and by <font SIZE="-1">BSD</font> and Linux implementations for Macintosh hardware. The final version of Power MachTen, 4.1.4, lacks many features found in modern implementations of <font SIZE="-1">UNIX</font>, and has a number of bugs. These shortcomings prevent recent versions of Perl from being able to use extensions on MachTen, and cause numerous test suite failures in the perl core. 

 In September 2003, a discussion on the MachTen mailing list determined that there was no interest in making a later version of Perl build successfully on MachTen. Consequently, support for building Perl under MachTen has been suppressed in Perl distributions published after February 2004. The hints file, <i>hints/machten.sh</i>, remains a part of the distributions for reference purposes.

<h2>Compiling Perl 5.6.x on MachTen</h2>

 To compile perl 5.6.x under MachTen 4.1.4 (and probably earlier versions): 

 <pre>
  ./Configure -de
  make
  make test
  make install
</pre> 

 This builds and installs a statically-linked perl; MachTen's dynamic linking facilities are not adequate to support Perl's use of dynamically linked libraries. (See <i>hints/machten.sh</i> for more information.) 

 You should have at least 32 megabytes of free memory on your system before running the <tt>&quot;make&quot;</tt> command. 

 For much more information on building perl --- for example, on how to change the default installation directory --- see <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.

<h2>Failures during make test on MachTen</h2>

<dl>
<dt>op/lexassign.t
<dd> This test may fail when first run after building perl. It does not fail subsequently. The cause is unknown.
<dt>pragma/warnings.t
<dd> Test 257 fails due to a failure to warn about attempts to read from a filehandle which is a duplicate of stdout when stdout is attached to a pipe. The output of the test contains a block comment which discusses a different failure, not applicable to MachTen. 

 The root of the problem is that Machten does not assign a file type to either end of a pipe (see stat), resulting, among other things in Perl's <tt>&quot;-p&quot;</tt> test failing on file descriptors belonging to pipes. As a result, perl becomes confused, and the test for reading from a write-only file fails. I am reluctant to patch perl to get around this, as it's clearly an <font SIZE="-1">OS</font> bug (about which Tenon has been informed), and limited in its effect on practical Perl programs.</dl>

<h2>Building external modules on MachTen</h2>

 To add an external module to perl, build in the normal way, which is documented in ExtUtils::MakeMaker, or which can be driven automatically by the <font SIZE="-1">CPAN</font> module (see <font SIZE="-1">CPAN</font>), which is part of the standard distribution. If you want to install a module which contains <font SIZE="-1">XS</font> code (C or C<font SIZE="-2">++</font> source which compiles to object code for linking with perl), you will have to replace your perl binary with a new version containing the new statically-linked object module. The build process tells you how to do this. 

 There is a gotcha, however, which users usually encounter immediately they respond to <font SIZE="-1">CPAN</font>'s invitation to <tt>&quot;install Bundle::CPAN&quot;</tt>. When installing a <i>bundle</i> --- a group of modules which together achieve some particular purpose, the installation process for later modules in the bundle tends to assume that earlier modules have been fully installed and are available for use. This is not true on a statically-linked system for earlier modules which contain <font SIZE="-1">XS</font> code. As a result the installation of the bundle fails. The work-around is not to install the bundle as a one-shot operation, but instead to see what modules it contains, and install these one-at-a-time by hand in the order given.

<h2>AUTHOR</h2>

 Dominic Dunlop &lt;domo [at] computer.org&gt;

<h2>DATE</h2>

 Version 1.1.0 2004-02-13 

<h2>Index</h2>


