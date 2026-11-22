---

title: "perlvmesa(1)"
name: "perlvmesa"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlvmesa/"
---

perlvmesa - building and installing Perl for VM/ESA. 

<h2>SYNOPSIS</h2>

 This document will help you Configure, build, test and install Perl on VM/ESA.

<h2>DESCRIPTION</h2>

 This is a fully ported perl for VM/ESA 2.3.0. It may work on other versions, but that's the one we've tested it on. 

 If you've downloaded the binary distribution, it needs to be installed below /usr/local. Source code distributions have an automated ``make install'' step that means you do not need to extract the source code below /usr/local (though that is where it will be installed by default). You may need to worry about the networking configuration files discussed in the last bullet below.

<h3>Unpacking Perl Distribution on VM/ESA</h3>

 To extract an ASCII tar archive on VM/ESA, try this: 

 <pre>
   pax -o to=IBM-1047,from=ISO8859-1 -r &lt; latest.tar
</pre>

<h3>Setup Perl and utilities on VM/ESA</h3>

 GNU make for VM/ESA, which may be required for the build of perl, is available from: 

 &lt;<a rel="nofollow" HREF="http://vm.marist.edu/~neale/vmoe.html">http://vm.marist.edu/~neale/vmoe.html</a>&gt;

<h3>Configure Perl on VM/ESA</h3>

 Once you've unpacked the distribution, run Configure (see INSTALL for full discussion of the Configure options), and then run make, then ``make test'' then ``make install'' (this last step may require UID=0 privileges). 

 There is a ``hints'' file for vmesa that specifies the correct values for most things. Some things to watch out for are:
<dl>
<dt>&bull;
</dt><dd> this port does support dynamic loading but it's not had much testing
</dd><dt>&bull;
</dt><dd> Don't turn on the compiler optimization flag ``-O''. There's a bug in the compiler (APAR PQ18812) that generates some bad code the optimizer is on.
</dd><dt>&bull;
</dt><dd> As VM/ESA doesn't fully support the <i>fork()</i> API programs relying on this call will not work. I've replaced <i>fork()</i>/<i>exec()</i> with <i>spawn()</i> and the standalone <i>exec()</i> with <i>spawn()</i>. This has a side effect when opening unnamed pipes in a shell script: there is no child process generated under.
</dd><dt>&bull;
</dt><dd> At the moment the hints file for VM/ESA basically bypasses all of the automatic configuration process. This is because Configure relies on: 1. The header files living in the Byte File System (you could put the there if you want); 2. The C preprocessor including the #include statements in the preprocessor output (.i) file.</dd></dl>

<h3>Testing Anomalies of Perl on VM/ESA</h3>

 The ``make test'' step runs a Perl Verification Procedure, usually before installation. As the 5.6.1 kit was being assembled the following ``failures'' were known to appear on some machines during ``make test'' (mostly due to ASCII vs. EBCDIC conflicts), your results may differ: 

 [the list of failures being compiled]

<h3>Usage Hints for Perl on VM/ESA</h3>

 When using perl on VM/ESA please keep in mind that the EBCDIC and ASCII character sets are different. Perl builtin functions that may behave differently under EBCDIC are mentioned in the perlport.pod document. 

 OpenEdition (UNIX System Services) does not (yet) support the #! means of script invocation. See: 

 <pre>
    head `whence perldoc`
</pre> 

 for an example of how to use the ``eval exec'' trick to ask the shell to have perl run your scripts for you.

<h2>AUTHORS</h2>

 Neale Ferguson.

<h2>SEE ALSO</h2>

 INSTALL, perlport, perlebcdic.

<h3>Mailing list for Perl on VM/ESA</h3>

 If you are interested in the VM/ESA, z/OS (formerly known as OS/390) and POSIX-BC (BS2000) ports of Perl then see the perl-mvs mailing list. To subscribe, send an empty message to perl-mvs-subscribe [at] perl.org. 

 See also: 

 <a rel="nofollow" HREF="http://lists.perl.org/list/perl-mvs.html">http://lists.perl.org/list/perl-mvs.html</a> &lt;<a HREF="http://lists.perl.org/list/perl-mvs.html">http://lists.perl.org/list/perl-mvs.html</a>&gt; 

 There are web archives of the mailing list at:
<dl>
<dt>&bull;
</dt><dd> <a rel="nofollow" HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a> &lt;<a HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a>&gt;
</dd><dt>&bull;
</dt><dd> <a rel="nofollow" HREF="http://archive.develooper.com/perl-mvs@perl.org/">http://archive.develooper.com/perl-mvs@perl.org/</a> &lt;<a HREF="http://archive.develooper.com/perl-mvs@perl.org/">http://archive.develooper.com/perl-mvs@perl.org/</a>&gt; 
</dd></dl>



<dt><a HREF="#lbAJ">AUTHORS</a>
</dt><dd>
</dd><dt><a HREF="#lbAK">SEE ALSO</a>
</dt><dd>

</dd></dl>
