---

title: "perlmodinstall(1)"
name: "perlmodinstall"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmodinstall/"
---

perlmodinstall - Installing CPAN Modules 

<h2>DESCRIPTION</h2>

 You can think of a module as the fundamental unit of reusable Perl code; see perlmod for details. Whenever anyone creates a chunk of Perl code that they think will be useful to the world, they register as a Perl developer at &lt;<a rel="nofollow" HREF="http://www.cpan.org/modules/04pause.html">http://www.cpan.org/modules/04pause.html</a>&gt; so that they can then upload their code to the CPAN. The CPAN is the Comprehensive Perl Archive Network and can be accessed at &lt;<a rel="nofollow" HREF="http://www.cpan.org/">http://www.cpan.org/</a>&gt; , and searched at &lt;<a rel="nofollow" HREF="http://search.cpan.org/">http://search.cpan.org/</a>&gt; . 

 This documentation is for people who want to download CPAN modules and install them on their own computer.

<h3>PREAMBLE</h3>

 First, are you sure that the module isn't already on your system? Try <tt>&quot;perl -MFoo -e 1&quot;</tt>. (Replace ``Foo'' with the name of the module; for instance, <tt>&quot;perl -MCGI::Carp -e 1&quot;</tt>.) 

 If you don't see an error message, you have the module. (If you do see an error message, it's still possible you have the module, but that it's not in your path, which you can display with <tt>&quot;perl -e &quot;print qq(@INC)&quot;&quot;</tt>.) For the remainder of this document, we'll assume that you really honestly truly lack an installed module, but have found it on the CPAN. 

 So now you have a file ending in .tar.gz (or, less often, .zip). You know there's a tasty module inside. There are four steps you must now take:
<dl>
<dt><b>DECOMPRESS</b> the file
</dt><dd>
</dd><dt><b>UNPACK</b> the file into a directory
</dt><dd>
</dd><dt><b>BUILD</b> the module (sometimes unnecessary)
</dt><dd>
</dd><dt><b>INSTALL</b> the module.
</dt><dd></dd></dl>
 

 Here's how to perform each step for each operating system. This is &lt;not&gt; a substitute for reading the README and INSTALL files that might have come with your module! 

 Also note that these instructions are tailored for installing the module into your system's repository of Perl modules, but you can install modules into any directory you wish. For instance, where I say <tt>&quot;perl Makefile.PL&quot;</tt>, you can substitute <tt>&quot;perl Makefile.PL PREFIX=/my/perl_directory&quot;</tt> to install the modules into <i>/my/perl_directory</i>. Then you can use the modules from your Perl programs with <tt>&quot;use lib &quot;/my/perl_directory/lib/site_perl&quot;;&quot;</tt> or sometimes just <tt>&quot;use &quot;/my/perl_directory&quot;;&quot;</tt>. If you're on a system that requires superuser/root access to install modules into the directories you see when you type <tt>&quot;perl -e &quot;print qq(@INC)&quot;&quot;</tt>, you'll want to install them into a local directory (such as your home directory) and use this approach.
<dl>
<dt>&bull;
</dt><dd> <b>If you're on a Unix or Unix-like system,</b> 
 You can use Andreas Koenig's CPAN module ( &lt;<a rel="nofollow" HREF="http://www.cpan.org/modules/by-module/CPAN">http://www.cpan.org/modules/by-module/CPAN</a>&gt; ) to automate the following steps, from DECOMPRESS through INSTALL. 
 A. DECOMPRESS 
 Decompress the file with <tt>&quot;gzip -d yourmodule.tar.gz&quot;</tt> 
 You can get gzip from &lt;<a HREF="ftp://prep.ai.mit.edu/pub/gnu/">ftp://prep.ai.mit.edu/pub/gnu/</a>&gt; 
 Or, you can combine this step with the next to save disk space: 
 <pre>
     gzip -dc yourmodule.tar.gz | tar -xof -
</pre> 
 B. UNPACK 
 Unpack the result with <tt>&quot;tar -xof yourmodule.tar&quot;</tt> 
 C. BUILD 
 Go into the newly-created directory and type: 
 <pre>
      perl Makefile.PL
      make test
</pre> 
 or 
 <pre>
      perl Makefile.PL PREFIX=/my/perl_directory
</pre> 
 to install it locally. (Remember that if you do this, you'll have to put <tt>&quot;use lib &quot;/my/perl_directory&quot;;&quot;</tt> near the top of the program that is to use this module. 
 D. INSTALL 
 While still in that directory, type: 
 <pre>
      make install
</pre> 
 Make sure you have the appropriate permissions to install the module in your Perl 5 library directory. Often, you'll need to be root. 
 That's all you need to do on Unix systems with dynamic linking. Most Unix systems have dynamic linking. If yours doesn't, or if for another reason you have a statically-linked perl, <b>and</b> the module requires compilation, you'll need to build a new Perl binary that includes the module. Again, you'll probably need to be root.
</dd><dt>&bull;
</dt><dd> <b>If you're running ActivePerl (Win95/98/2K/NT/XP, Linux, Solaris),</b> 
 First, type <tt>&quot;ppm&quot;</tt> from a shell and see whether ActiveState's PPM repository has your module. If so, you can install it with <tt>&quot;ppm&quot;</tt> and you won't have to bother with any of the other steps here. You might be able to use the CPAN instructions from the ``Unix or Linux'' section above as well; give it a try. Otherwise, you'll have to follow the steps below. 
 <pre>
   A. DECOMPRESS
</pre> 
 You can use the shareware Winzip ( &lt;<a rel="nofollow" HREF="http://www.winzip.com">http://www.winzip.com</a>&gt; ) to decompress and unpack modules. 
 <pre>
   B. UNPACK
</pre> 
 If you used WinZip, this was already done for you. 
 <pre>
   C. BUILD
</pre> 
 You'll need the <tt>&quot;nmake&quot;</tt> utility, available at &lt;<a rel="nofollow" HREF="http://download.microsoft.com/download/vc15/Patch/1.52/W95/EN-US/nmake15.exe">http://download.microsoft.com/download/vc15/Patch/1.52/W95/EN-US/nmake15.exe</a>&gt; or dmake, available on CPAN. &lt;<a rel="nofollow" HREF="http://search.cpan.org/dist/dmake/">http://search.cpan.org/dist/dmake/</a>&gt; 
 Does the module require compilation (i.e. does it have files that end in .xs, .c, .h, .y, .cc, .cxx, or .C)? If it does, life is now officially tough for you, because you have to compile the module yourself (no easy feat on Windows). You'll need a compiler such as Visual C++. Alternatively, you can download a pre-built PPM package from ActiveState. &lt;<a rel="nofollow" HREF="http://aspn.activestate.com/ASPN/Downloads/ActivePerl/PPM/">http://aspn.activestate.com/ASPN/Downloads/ActivePerl/PPM/</a>&gt; 
 Go into the newly-created directory and type: 
 <pre>
      perl Makefile.PL
      nmake test
   D. INSTALL
</pre> 
 While still in that directory, type: 
 <pre>
      nmake install
</pre>
</dd><dt>&bull;
</dt><dd> <b>If you're on the </b><b>DJGPP</b><b> port of </b><b>DOS,</b> 
 <pre>
   A. DECOMPRESS
</pre> 
 djtarx ( &lt;<a HREF="ftp://ftp.delorie.com/pub/djgpp/current/v2/">ftp://ftp.delorie.com/pub/djgpp/current/v2/</a>&gt; ) will both uncompress and unpack. 
 <pre>
   B. UNPACK
</pre> 
 See above. 
 <pre>
   C. BUILD
</pre> 
 Go into the newly-created directory and type: 
 <pre>
      perl Makefile.PL
      make test
</pre> 
 You will need the packages mentioned in <i></i><i>README</i><i>.dos</i> in the Perl distribution. 
 <pre>
   D. INSTALL
</pre> 
 While still in that directory, type: 
 <pre>
     make install
</pre> 
 You will need the packages mentioned in <i></i><i>README</i><i>.dos</i> in the Perl distribution.
</dd><dt>&bull;
</dt><dd> <b>If you're on </b><b>OS/2,</b> 
 Get the EMX development suite and gzip/tar, from either Hobbes ( &lt;<a rel="nofollow" HREF="http://hobbes.nmsu.edu">http://hobbes.nmsu.edu</a>&gt; ) or Leo ( &lt;<a rel="nofollow" HREF="http://www.leo.org">http://www.leo.org</a>&gt; ), and then follow the instructions for Unix.
</dd><dt>&bull;
</dt><dd> <b>If you're on </b><b>VMS,</b> 
 When downloading from CPAN, save your file with a <tt>&quot;.tgz&quot;</tt> extension instead of <tt>&quot;.tar.gz&quot;</tt>. All other periods in the filename should be replaced with underscores. For example, <tt>&quot;Your-Module-1.33.tar.gz&quot;</tt> should be downloaded as <tt>&quot;Your-Module-1_33.tgz&quot;</tt>. 
 A. DECOMPRESS 
 Type 
 <pre>
    gzip -d Your-Module.tgz
</pre> 
 or, for zipped modules, type 
 <pre>
    unzip Your-Module.zip
</pre> 
 Executables for gzip, zip, and VMStar: 
 <pre>
    <a rel="nofollow" HREF="http://www.hp.com/go/openvms/freeware/">http://www.hp.com/go/openvms/freeware/</a>
</pre> 
 and their source code: 
 <pre>
    <a rel="nofollow" HREF="http://www.fsf.org/order/ftp.html">http://www.fsf.org/order/ftp.html</a>
</pre> 
 Note that GNU's gzip/gunzip is not the same as Info-ZIP's zip/unzip package. The former is a simple compression tool; the latter permits creation of multi-file archives. 
 B. UNPACK 
 If you're using VMStar: 
 <pre>
     VMStar xf Your-Module.tar
</pre> 
 Or, if you're fond of VMS command syntax: 
 <pre>
     tar/extract/verbose Your_Module.tar
</pre> 
 C. BUILD 
 Make sure you have MMS (from Digital) or the freeware MMK ( available from MadGoat at &lt;<a rel="nofollow" HREF="http://www.madgoat.com">http://www.madgoat.com</a>&gt; ). Then type this to create the DESCRIP.MMS for the module: 
 <pre>
    perl Makefile.PL
</pre> 
 Now you're ready to build: 
 <pre>
    mms test
</pre> 
 Substitute <tt>&quot;mmk&quot;</tt> for <tt>&quot;mms&quot;</tt> above if you're using MMK. 
 D. INSTALL 
 Type 
 <pre>
    mms install
</pre> 
 Substitute <tt>&quot;mmk&quot;</tt> for <tt>&quot;mms&quot;</tt> above if you're using MMK.
</dd><dt>&bull;
</dt><dd> <b>If you're on </b><b>MVS</b>, 
 Introduce the <i>.tar.gz</i> file into an HFS as binary; don't translate from ASCII to EBCDIC. 
 A. DECOMPRESS 
 Decompress the file with <tt>&quot;gzip -d yourmodule.tar.gz&quot;</tt> 
 You can get gzip from &lt;<a rel="nofollow" HREF="http://www.s390.ibm.com/products/oe/bpxqp1.html">http://www.s390.ibm.com/products/oe/bpxqp1.html</a>&gt; 
 B. UNPACK 
 Unpack the result with 
 <pre>
     pax -o to=IBM-1047,from=ISO8859-1 -r &lt; yourmodule.tar
</pre> 
 The BUILD and INSTALL steps are identical to those for Unix. Some modules generate Makefiles that work better with GNU make, which is available from &lt;<a rel="nofollow" HREF="http://www.mks.com/s390/gnu/">http://www.mks.com/s390/gnu/</a>&gt;</dd></dl>

<h2>PORTABILITY</h2>

 Note that not all modules will work with on all platforms. See perlport for more information on portability issues. Read the documentation to see if the module will work on your system. There are basically three categories of modules that will not work ``out of the box'' with all platforms (with some possibility of overlap):
<dl>
<dt>&bull;
</dt><dd> <b>Those that should, but don't.</b> These need to be fixed; consider contacting the author and possibly writing a patch.
</dd><dt>&bull;
</dt><dd> <b>Those that need to be compiled, where the target platform doesn't have compilers readily available.</b> (These modules contain <i>.xs</i> or <i>.c</i> files, usually.) You might be able to find existing binaries on the CPAN or elsewhere, or you might want to try getting compilers and building it yourself, and then release the binary for other poor souls to use.
</dd><dt>&bull;
</dt><dd> <b>Those that are targeted at a specific platform.</b> (Such as the Win32:: modules.) If the module is targeted specifically at a platform other than yours, you're out of luck, most likely.</dd></dl>
 

 Check the CPAN Testers if a module should work with your platform but it doesn't behave as you'd expect, or you aren't sure whether or not a module will work under your platform. If the module you want isn't listed there, you can test it yourself and let CPAN Testers know, you can join CPAN Testers, or you can request it be tested. 

 <pre>
    <a rel="nofollow" HREF="http://testers.cpan.org/">http://testers.cpan.org/</a>
</pre>

<h2>HEY</h2>

 If you have any suggested changes for this page, let me know. Please don't send me mail asking for help on how to install your modules. There are too many modules, and too few Orwants, for me to be able to answer or even acknowledge all your questions. Contact the module author instead, ask someone familiar with Perl on your operating system, or if all else fails, file a ticket at &lt;<a rel="nofollow" HREF="http://rt.cpan.org/">http://rt.cpan.org/</a>&gt;.

<h2>AUTHOR</h2>

 Jon Orwant 

 orwant [at] medita.mit.edu 

 with invaluable help from Chris Nandor, and valuable help from Brandon Allbery, Charles Bailey, Graham Barr, Dominic Dunlop, Jarkko Hietaniemi, Ben Holzman, Tom Horsley, Nick Ing-Simmons, Tuomas J. Lukka, Laszlo Molnar, Alan Olsen, Peter Prymmer, Gurusamy Sarathy, Christoph Spalinger, Dan Sugalski, Larry Virden, and Ilya Zakharevich. 

 First version July 22, 1998; last revised November 21, 2001.

<h2>COPYRIGHT</h2>

 Copyright (C) 1998, 2002, 2003 Jon Orwant. All Rights Reserved. 

 This document may be distributed under the same terms as Perl itself. 



<dt><a HREF="#lbAE">PORTABILITY</a>
</dt><dd>
</dd><dt><a HREF="#lbAF">HEY</a>
</dt><dd>
</dd><dt><a HREF="#lbAG">AUTHOR</a>
</dt><dd>
</dd><dt><a HREF="#lbAH">COPYRIGHT</a>
</dt><dd></dd></dl>
