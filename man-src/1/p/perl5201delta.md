---
title: "perl5201delta(1)"
name: "perl5201delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5201delta/"
description: "perl5201delta – what is new for perl v5.20.1"
---

<h2 class="name">NAME</h2>
<p> perl5201delta &#8211; what is new for perl v5.20.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.20.0 release and the 5.20.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.18.0, first read perl5200delta, which describes differences between 5.18.0 and 5.20.0.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.20.0. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> An optimization to avoid problems with <font SIZE="-1">COW</font> and deliberately overallocated PVs has been disabled because it interfered with another, more important, optimization, causing a slowdown on some platforms. [perl #121975] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121975">https://rt.perl.org/Ticket/Display.html?id=121975</a>&gt;</p>
<dt>&bull;</p>
<dd> Returning a string from a lexical variable could be slow in some cases. This has now been fixed. [perl #121977] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121977">https://rt.perl.org/Ticket/Display.html?id=121977</a>&gt;</dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Config::Perl::V has been upgraded from version 0.20 to 0.22. </p>
<p> The list of Perl versions covered has been updated and some flaws in the parsing have been fixed.</p>
<dt>&bull;</p>
<dd> Exporter has been upgraded from version 5.70 to 5.71. </p>
<p> Illegal <font SIZE="-1">POD</font> syntax in the documentation has been corrected.</p>
<dt>&bull;</p>
<dd> ExtUtils::CBuilder has been upgraded from version 0.280216 to 0.280217. </p>
<p> Android builds now link to both <code>-lperl</code> and <tt>$Config::Config{perllibs}</tt>.</p>
<dt>&bull;</p>
<dd> File::Copy has been upgraded from version 2.29 to 2.30. </p>
<p> The documentation now notes that <tt>&quot;copy&quot;</tt> will not overwrite read-only files.</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 3.11 to 5.020001. </p>
<p> The list of Perl versions covered has been updated.</p>
<dt>&bull;</p>
<dd> The PathTools module collection has been upgraded from version 3.47 to 3.48. </p>
<p> Fallbacks are now in place when cross-compiling for Android and <tt>$Config::Config{sh}</tt> is not yet defined. [perl #121963] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121963">https://rt.perl.org/Ticket/Display.html?id=121963</a>&gt;</p>
<dt>&bull;</p>
<dd> PerlIO::via has been upgraded from version 0.14 to 0.15. </p>
<p> A minor portability improvement has been made to the <font SIZE="-1">XS</font> implementation.</p>
<dt>&bull;</p>
<dd> Unicode::UCD has been upgraded from version 0.57 to 0.58. </p>
<p> The documentation includes many clarifications and fixes.</p>
<dt>&bull;</p>
<dd> utf8 has been upgraded from version 1.13 to 1.13_01. </p>
<p> The documentation has some minor formatting improvements.</p>
<dt>&bull;</p>
<dd> version has been upgraded from version 0.9908 to 0.9909. </p>
<p> External libraries and Perl may have different ideas of what the locale is. This is problematic when parsing version strings if the locale&#8217;s numeric separator has been changed. Version parsing has been patched to ensure it handles the locales correctly. [perl #121930] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121930">https://rt.perl.org/Ticket/Display.html?id=121930</a>&gt;</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapi</i></p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;av_len&quot;</tt> &#8211; Emphasize that this returns the highest index in the array, not the size of the array. [perl #120386] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120386">https://rt.perl.org/Ticket/Display.html?id=120386</a>&gt;</p>
<dt>&bull;</p>
<dd> Note that <tt>&quot;SvSetSV&quot;</tt> doesn&#8217;t do set magic.</p>
<dt>&bull;</p>
<dd> <tt>&quot;sv_usepvn_flags&quot;</tt> &#8211; Fix documentation to mention the use of <tt>&quot;NewX&quot;</tt> instead of <tt>&quot;malloc&quot;</tt>. [perl #121869] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121869">https://rt.perl.org/Ticket/Display.html?id=121869</a>&gt;</p>
<dt>&bull;</p>
<dd> Clarify where <tt>&quot;NUL&quot;</tt> may be embedded or is required to terminate a string.</dl>
<p> <i>perlfunc</i></p>
<dl>
<dt>&bull;</p>
<dd> Clarify the meaning of <tt>&quot;-B&quot;</tt> and <tt>&quot;-T&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-l&quot;</tt> now notes that it will return false if symlinks aren&#8217;t supported by the file system. [perl #121523] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121523">https://rt.perl.org/Ticket/Display.html?id=121523</a>&gt;</p>
<dt>&bull;</p>
<dd> Note that <tt>&quot;each&quot;</tt>, <tt>&quot;keys&quot;</tt> and <tt>&quot;values&quot;</tt> may produce different orderings for tied hashes compared to other perl hashes. [perl #121404] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121404">https://rt.perl.org/Ticket/Display.html?id=121404</a>&gt;</p>
<dt>&bull;</p>
<dd> Note that <tt>&quot;exec LIST&quot;</tt> and <tt>&quot;system LIST&quot;</tt> may fall back to the shell on Win32. Only <tt>&quot;exec PROGRAM LIST&quot;</tt> and <tt>&quot;system PROGRAM LIST&quot;</tt> indirect object syntax will reliably avoid using the shell. This has also been noted in perlport. [perl #122046] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122046">https://rt.perl.org/Ticket/Display.html?id=122046</a>&gt;</p>
<dt>&bull;</p>
<dd> Clarify the meaning of <tt>&quot;our&quot;</tt>. [perl #122132] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122132">https://rt.perl.org/Ticket/Display.html?id=122132</a>&gt;</dl>
<p> <i>perlguts</i></p>
<dl>
<dt>&bull;</p>
<dd> Explain various ways of modifying an existing <font SIZE="-1">SV</font>&#8216;s buffer. [perl #116925] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=116925">https://rt.perl.org/Ticket/Display.html?id=116925</a>&gt;</dl>
<p> <i>perlpolicy</i></p>
<dl>
<dt>&bull;</p>
<dd> We now have a code of conduct for the <i>p5p</i> mailing list, as documented in &#8220;<font SIZE="-1">STANDARDS OF CONDUCT&#8221;</font> in perlpolicy.</dl>
<p> <i>perlre</i></p>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;/x&quot;</tt> modifier has been clarified to note that comments cannot be continued onto the next line by escaping them.</dl>
<p> <i>perlsyn</i></p>
<dl>
<dt>&bull;</p>
<dd> Mention the use of empty conditionals in <tt>&quot;for&quot;</tt>/<tt>&quot;while&quot;</tt> loops for infinite loops.</dl>
<p> <i>perlxs</i></p>
<dl>
<dt>&bull;</p>
<dd> Added a discussion of locale issues in <font SIZE="-1">XS</font> code.</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> Variable length lookbehind not implemented in regex m/%s/ </p>
<p> Information about Unicode behaviour has been added.</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> Building Perl no longer writes to the source tree when configured with <i>Configure</i>&#8216;s <code>-Dmksymlinks</code> option. [perl #121585] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121585">https://rt.perl.org/Ticket/Display.html?id=121585</a>&gt;</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Android</p>
<dd> Build support has been improved for cross-compiling in general and for Android in particular.</p>
<dt>OpenBSD</p>
<dd> Corrected architectures and version numbers used in configuration hints when building Perl.</p>
<dt>Solaris</p>
<dd> <code>c99</code> options have been cleaned up, hints look for <code>solstudio</code> as well as <code>SUNWspro</code>, and support for native <tt>&quot;setenv&quot;</tt> has been added.</p>
<dt><font SIZE="-1">VMS</font></p>
<dd> An old bug in feature checking, mainly affecting pre-7.3 systems, has been fixed.</p>
<dt>Windows</p>
<dd> <tt>%I64d</tt> is now being used instead of <tt>%lld</tt> for MinGW.</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> Added &#8220;sync_locale&#8221; in perlapi. Changing the program&#8217;s locale should be avoided by <font SIZE="-1">XS</font> code. Nevertheless, certain non-Perl libraries called from <font SIZE="-1">XS,</font> such as <tt>&quot;Gtk&quot;</tt> do so. When this happens, Perl needs to be told that the locale has changed. Use this function to do so, before returning to Perl.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A bug has been fixed where zero-length assertions and code blocks inside of a regex could cause <tt>&quot;pos&quot;</tt> to see an incorrect value. [perl #122460] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122460">https://rt.perl.org/Ticket/Display.html?id=122460</a>&gt;</p>
<dt>&bull;</p>
<dd> Using <tt>&quot;s///e&quot;</tt> on tainted utf8 strings could issue bogus &#8220;Malformed <font SIZE="-1">UTF-8</font> character (unexpected end of string)&#8221; warnings. This has now been fixed. [perl #122148] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122148">https://rt.perl.org/Ticket/Display.html?id=122148</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;system&quot;</tt> and friends should now work properly on more Android builds. </p>
<p> Due to an oversight, the value specified through <code>-Dtargetsh</code> to <i>Configure</i> would end up being ignored by some of the build process. This caused perls cross-compiled for Android to end up with defective versions of <tt>&quot;system&quot;</tt>, <tt>&quot;exec&quot;</tt> and backticks: the commands would end up looking for <i>/bin/sh</i> instead of <i>/system/bin/sh</i>, and so would fail for the vast majority of devices, leaving <tt>$!</tt> as <tt>&quot;ENOENT&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Many issues have been detected by Coverity &lt;<a rel="nofollow" href="http://www.coverity.com/">http://www.coverity.com/</a>&gt; and fixed.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.20.1 represents approximately 4 months of development since Perl 5.20.0 and contains approximately 12,000 lines of changes across 170 files from 36 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 2,600 lines of changes to 110 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.20.1: </p>
<p> Aaron Crane, Abigail, Alberto Simões, Alexandr Ciornii, Alexandre (Midnite) Jousset, Andrew Fresh, Andy Dougherty, Brian Fraser, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Daniel Dragan, David Golden, David Mitchell, H.Merijn Brand, James E Keenan, Jan Dubois, Jarkko Hietaniemi, John Peacock, kafka, Karen Etheridge, Karl Williamson, Lukas Mai, Matthew Horsfall, Michael Bunk, Peter Martini, Rafael Garcia-Suarez, Reini Urban, Ricardo Signes, Shirakata Kentaro, Smylers, Steve Hay, Thomas Sibley, Todd Rinaldo, Tony Cook, Vladimir Marek, Yves Orton. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
