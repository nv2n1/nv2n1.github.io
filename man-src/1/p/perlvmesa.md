---
title: "perlvmesa(1)"
name: "perlvmesa"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlvmesa/"
---

<h2 class="name">NAME</h2>
 

 perlvmesa - building and installing Perl for VM/ESA. 

<h2>SYNOPSIS</h2>

 This document will help you Configure, build, test and install Perl on <font SIZE="-1">VM/ESA</font>.

<h2>DESCRIPTION</h2>

 This is a fully ported perl for <font SIZE="-1">VM/ESA</font> 2.3.0. It may work on other versions, but that's the one we've tested it on. 

 If you've downloaded the binary distribution, it needs to be installed below /usr/local. Source code distributions have an automated ``make install'' step that means you do not need to extract the source code below /usr/local (though that is where it will be installed by default). You may need to worry about the networking configuration files discussed in the last bullet below.

<h3>Unpacking Perl Distribution on <font SIZE="-1">VM/ESA</font></h3>

 To extract an <font SIZE="-1">ASCII</font> tar archive on <font SIZE="-1">VM/ESA</font>, try this: 

 <pre>
   pax -o to=IBM-1047,from=ISO8859-1 -r &lt; latest.tar
</pre>

<h3>Setup Perl and utilities on <font SIZE="-1">VM/ESA</font></h3>

 <font SIZE="-1">GNU</font> make for <font SIZE="-1">VM/ESA</font>, which may be required for the build of perl, is available from: 

 &lt;<a rel="nofollow" HREF="http://vm.marist.edu/~neale/vmoe.html">http://vm.marist.edu/~neale/vmoe.html</a>&gt;

<h3>Configure Perl on <font SIZE="-1">VM/ESA</font></h3>

 Once you've unpacked the distribution, run Configure (see <font SIZE="-1">INSTALL</font> for full discussion of the Configure options), and then run make, then ``make test'' then ``make install'' (this last step may require UID=0 privileges). 

 There is a ``hints'' file for vmesa that specifies the correct values for most things. Some things to watch out for are:
<dl>
<dt>&bull;
<dd> this port does support dynamic loading but it's not had much testing
<dt>&bull;
<dd> Don't turn on the compiler optimization flag ``-O''. There's a bug in the compiler (<font SIZE="-1">APAR</font> <font SIZE="-1">PQ18812</font>) that generates some bad code the optimizer is on.
<dt>&bull;
<dd> As <font SIZE="-1">VM/ESA</font> doesn't fully support the <i>fork()</i> <font SIZE="-1">API</font> programs relying on this call will not work. I've replaced <i>fork()</i>/<i>exec()</i> with <i>spawn()</i> and the standalone <i>exec()</i> with <i>spawn()</i>. This has a side effect when opening unnamed pipes in a shell script: there is no child process generated under.
<dt>&bull;
<dd> At the moment the hints file for <font SIZE="-1">VM/ESA</font> basically bypasses all of the automatic configuration process. This is because Configure relies on: 1. The header files living in the Byte File System (you could put the there if you want); 2. The C preprocessor including the #include statements in the preprocessor output (.i) file.</dl>

<h3>Testing Anomalies of Perl on <font SIZE="-1">VM/ESA</font></h3>

 The ``make test'' step runs a Perl Verification Procedure, usually before installation. As the 5.6.1 kit was being assembled the following ``failures'' were known to appear on some machines during ``make test'' (mostly due to <font SIZE="-1">ASCII</font> vs. <font SIZE="-1">EBCDIC</font> conflicts), your results may differ: 

 [the list of failures being compiled]

<h3>Usage Hints for Perl on <font SIZE="-1">VM/ESA</font></h3>

 When using perl on <font SIZE="-1">VM/ESA</font> please keep in mind that the <font SIZE="-1">EBCDIC</font> and <font SIZE="-1">ASCII</font> character sets are different. Perl builtin functions that may behave differently under <font SIZE="-1">EBCDIC</font> are mentioned in the perlport.pod document. 

 OpenEdition (<font SIZE="-1">UNIX</font> System Services) does not (yet) support the #! means of script invocation. See: 

 <pre>
    head `whence perldoc`
</pre> 

 for an example of how to use the ``eval exec'' trick to ask the shell to have perl run your scripts for you.

<h2>AUTHORS</h2>

 Neale Ferguson.

<h2>SEE ALSO</h2>

 <font SIZE="-1">INSTALL</font>, perlport, perlebcdic.

<h3>Mailing list for Perl on <font SIZE="-1">VM/ESA</font></h3>

 If you are interested in the <font SIZE="-1">VM/ESA</font>, z/OS (formerly known as <font SIZE="-1">OS/390</font>) and POSIX-BC (<font SIZE="-1">BS2000</font>) ports of Perl then see the perl-mvs mailing list. To subscribe, send an empty message to perl-mvs-subscribe [at] perl.org. 

 See also: 

 <a rel="nofollow" HREF="http://lists.perl.org/list/perl-mvs.html">http://lists.perl.org/list/perl-mvs.html</a> &lt;<a HREF="http://lists.perl.org/list/perl-mvs.html">http://lists.perl.org/list/perl-mvs.html</a>&gt; 

 There are web archives of the mailing list at:
<dl>
<dt>&bull;
<dd> <a rel="nofollow" HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a> &lt;<a HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a>&gt;
<dt>&bull;
<dd> <a rel="nofollow" HREF="http://archive.develooper.com/perl-mvs@perl.org/">http://archive.develooper.com/perl-mvs@perl.org/</a> &lt;<a HREF="http://archive.develooper.com/perl-mvs@perl.org/">http://archive.develooper.com/perl-mvs@perl.org/</a>&gt; 

</dl>

<h2>Index</h2>



<dt><a HREF="#lbAJ">AUTHORS</a>
<dd>
<dt><a HREF="#lbAK">SEE ALSO</a>
<dd>

</dl>
