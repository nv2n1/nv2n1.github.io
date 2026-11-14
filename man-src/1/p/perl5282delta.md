---
title: "perl5282delta(1)"
name: "perl5282delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5282delta/"
---

<h2 class="name">NAME</h2>
 

 perl5282delta - what is new for perl v5.28.2 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.28.1 release and the 5.28.2 release. 

 If you are upgrading from an earlier release such as 5.28.0, first read perl5281delta, which describes differences between 5.28.0 and 5.28.1.

<h2>Incompatible Changes</h2>

<h3>Any set of digits in the Common script are legal in a script run of another script</h3>

 There are several sets of digits in the Common script. <tt>&quot;[0-9]&quot;</tt> is the most familiar. But there are also <tt>&quot;[\x{FF10}-\x{FF19}]&quot;</tt> (<font SIZE="-1">FULLWIDTH DIGIT ZERO</font> - <font SIZE="-1">FULLWIDTH DIGIT NINE</font>), and several sets for use in mathematical notation, such as the <font SIZE="-1">MATHEMATICAL</font> DOUBLE-STRUCK DIGITs. Any of these sets should be able to appear in script runs of, say, Greek. But the previous design overlooked all but the <font SIZE="-1">ASCII</font> digits <tt>&quot;[0-9]&quot;</tt>, so the design was flawed. This has been fixed, so is both a bug fix and an incompatibility. 

 All digits in a run still have to come from the same set of ten digits. 

 [perl #133547] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133547">https://rt.perl.org/Ticket/Display.html?id=133547</a>&gt;

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> Module::CoreList has been upgraded from version 5.20181129_28 to 5.20190419.
<dt>&bull;
<dd> PerlIO::scalar has been upgraded from version 0.29 to 0.30.
<dt>&bull;
<dd> Storable has been upgraded from version 3.08 to 3.08_01.</dl>

<h2>Platform Support</h2>

<h3>Platform-Specific Notes</h3>

<dl>
<dt>Windows
<dd> The Windows Server 2003 <font SIZE="-1">SP1</font> Platform <font SIZE="-1">SDK</font> build, with its early x64 compiler and tools, was accidentally broken in Perl 5.27.9. This has now been fixed.
<dt>Mac <font SIZE="-1">OS X</font>
<dd> Perl's build and testing process on Mac <font SIZE="-1">OS X</font> for <tt>&quot;-Duseshrplib&quot;</tt> builds is now compatible with Mac <font SIZE="-1">OS X</font> System Integrity Protection (<font SIZE="-1">SIP</font>). 

 <font SIZE="-1">SIP</font> prevents binaries in <i>/bin</i> (and a few other places) being passed the <tt>&quot;DYLD_LIBRARY_PATH&quot;</tt> environment variable. For our purposes this prevents <tt>&quot;DYLD_LIBRARY_PATH&quot;</tt> from being passed to the shell, which prevents that variable being passed to the testing or build process, so running <tt>&quot;perl&quot;</tt> couldn't find <i>libperl.dylib</i>. 

 To work around that, the initial build of the <i>perl</i> executable expects to find <i>libperl.dylib</i> in the build directory, and the library path is then adjusted during installation to point to the installed library. 

 [perl #126706] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=126706">https://rt.perl.org/Ticket/Display.html?id=126706</a>&gt;</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> If an in-place edit is still in progress during global destruction and the process exit code (as stored in <tt>$?</tt>) is zero, perl will now treat the in-place edit as successful, replacing the input file with any output produced. 

 This allows code like: 

 <pre>
  perl -i -ne 'print &quot;Foo&quot;; last'
</pre> 

 to replace the input file, while code like: 

 <pre>
  perl -i -ne 'print &quot;Foo&quot;; die'
</pre> 

 will not. Partly resolves [perl #133659]. 

 [perl #133659] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133659">https://rt.perl.org/Ticket/Display.html?id=133659</a>&gt;
<dt>&bull;
<dd> A regression in Perl 5.28 caused the following code to fail 

 <pre>
 close(STDIN); open(CHILD, &quot;|wc -l&quot;)'
</pre> 

 because the child's stdin would be closed on exec. This has now been fixed.
<dt>&bull;
<dd> <tt>&quot;pack &quot;u&quot;, &quot;invalid uuencoding&quot;&quot;</tt> now properly <font SIZE="-1">NUL</font> terminates the zero-length <font SIZE="-1">SV</font> produced. 

 [perl #132655] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=132655">https://rt.perl.org/Ticket/Display.html?id=132655</a>&gt;
<dt>&bull;
<dd> Failing to compile a format now aborts compilation. Like other errors in sub-parses this could leave the parser in a strange state, possibly crashing perl if compilation continued. 

 [perl #132158] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=132158">https://rt.perl.org/Ticket/Display.html?id=132158</a>&gt;
<dt>&bull;
<dd> See ``Any set of digits in the Common script are legal in a script run of another script''.</dl>

<h2>Acknowledgements</h2>

 Perl 5.28.2 represents approximately 4 months of development since Perl 5.28.1 and contains approximately 2,500 lines of changes across 75 files from 13 authors. 

 Excluding auto-generated files, documentation and release tools, there were approximately 1,200 lines of changes to 29 .pm, .t, .c and .h files. 

 Perl continues to flourish into its fourth decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.28.2: 

 Aaron Crane, Abigail, Andy Dougherty, David Mitchell, Karen Etheridge, Karl Williamson, Leon Timmermans, Nicolas R., Sawyer X, Steve Hay, Tina Müller, Tony Cook, Zak B. Elep. 

 The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. 

 Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl's core. We're grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. 

 For a more complete list of all of Perl's historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the perl bug database at &lt;<a rel="nofollow" HREF="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION''</font> in perlsec for details of how to report the issue.

<h2>Give Thanks</h2>

 If you wish to thank the Perl 5 Porters for the work we had done in Perl 5, you can do so by running the <tt>&quot;perlthanks&quot;</tt> program: 

 <pre>
    perlthanks
</pre> 

 This will send an email to the Perl 5 Porters list with your show of thanks.

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>


