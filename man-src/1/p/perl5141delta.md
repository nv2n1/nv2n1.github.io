---

title: "perl5141delta(1)"
name: "perl5141delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5141delta/"
description: "perl5141delta – what is new for perl v5.14.1"
---

<p> This document describes differences between the 5.14.0 release and the 5.14.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.0, first read perl5140delta, which describes differences between 5.12.0 and 5.14.0.  </p>
<h2>Core Enhancements</h2>
<p> No changes since 5.14.0.  </p>
<h2>Security</h2>
<p> No changes since 5.14.0.  </p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.14.0. If any exist, they are bugs and reports are welcome.  </p>
<h2>Deprecations</h2>
<p> There have been no deprecations since 5.14.0.  </p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> None  </p>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 1.03 to 1.04, to address two regressions in Perl 5.14.0: </p>
<p> Deparsing of the <code>&quot;glob&quot;</code> operator and its diamond (<code>&quot;&lt;&gt;&quot;</code>) form now works again. [perl #90898] </p>
<p> The presence of subroutines named <code>&quot;::::&quot;</code> or <code>&quot;::::::&quot;</code> no longer causes B::Deparse to hang. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded from version 3.15_03 to 3.15_04. </p>
<p> It corrects the search paths on <font SIZE="-1">VMS.</font> [perl #90640] </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<p> None  </p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> None  </p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;given&quot;</code>, <code>&quot;when&quot;</code> and <code>&quot;default&quot;</code> are now listed in perlfunc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documentation for <code>&quot;use&quot;</code> now includes a pointer to <i>if.pm</i>. </p>
 </dd></dl>
<p> <i>perllol</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perllol has been expanded with examples using the new <code>&quot;push $scalar&quot;</code> syntax introduced in Perl 5.14.0. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The explanation of bitwise operators has been expanded to explain how they work on Unicode strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The section on the triple-dot or yada-yada operator has been moved up, as it used to separate two closely related sections about the comma operator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> More examples for <code>&quot;m//g&quot;</code> have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;&lt;&lt;\FOO&quot;</code> here-doc syntax has been documented. </p>
 </dd></dl>
<p> <i>perlrun</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlrun has undergone a significant clean-up. Most notably, the <code>-0x...</code> form of the <code>-0</code> flag has been clarified, and the final section on environment variables has been corrected and expanded. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>POSIX</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The invocation documentation for <code>&quot;WIFEXITED&quot;</code>, <code>&quot;WEXITSTATUS&quot;</code>, <code>&quot;WIFSIGNALED&quot;</code>, <code>&quot;WTERMSIG&quot;</code>, <code>&quot;WIFSTOPPED&quot;</code>, and <code>&quot;WSTOPSIG&quot;</code> was corrected. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> None  </p>
<h3>Changes to Existing Diagnostics</h3>
<p> None  </p>
<h2>Utility Changes</h2>
<p> None  </p>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>regexp.h</i> has been modified for compatibility with <font SIZE="-1">GCC</font>&#8216;s <code>&quot;-Werror&quot;</code> option, as used by some projects that include perl&#8217;s header files. </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Some test failures in <i>dist/Locale-Maketext/t/09_compile.t</i> that could occur depending on the environment have been fixed. [perl #89896] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A watchdog timer for <i>t/re/re.t</i> was lengthened to accommodate <font SIZE="-1">SH-4</font> systems which were unable to complete the tests before the previous timer ran out. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<p> None  </p>
<h3>Discontinued Platforms</h3>
<p> None  </p>
<h3>Platform-Specific Notes</h3>
<p> <i>Solaris</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Documentation listing the Solaris packages required to build Perl on Solaris 9 and Solaris 10 has been corrected. </p>
 </dd></dl>
<p> <i>Mac </i><font SIZE="-1"><i>OS X</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <i>lib/locale.t</i> test script has been updated to work on the upcoming Lion release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mac <font SIZE="-1">OS X</font> specific compilation instructions have been clarified. </p>
 </dd></dl>
<p> <i>Ubuntu Linux</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The ODBM_File installation process has been updated with the new library paths on Ubuntu natty. </p>
 </dd></dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The compiled representation of formats is now stored via the mg_ptr of their PERL_MAGIC_fm. Previously it was stored in the string buffer, beyond <code>SvLEN()</code>, the regular end of the string. <code>SvCOMPILED()</code> and SvCOMPILED_{on,off}() now exist solely for compatibility for <font SIZE="-1">XS</font> code. The first is always 0, the other two now no-ops. </p>
 </dd></dl>
<h2>Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A bug has been fixed that would cause a ``Use of freed value in iteration&#8217;&#8216; error if the next two hash elements that would be iterated over are deleted. [perl #85026] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Passing the same constant subroutine to both <code>&quot;index&quot;</code> and <code>&quot;formline&quot;</code> no longer causes one or the other to fail. [perl #89218] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 5.14.0 introduced some memory leaks in regular expression character classes such as <code>&quot;[\w\s]&quot;</code>, which have now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An edge case in regular expression matching could potentially loop. This happened only under <code>&quot;/i&quot;</code> in bracketed character classes that have characters with multi-character folds, and the target string to match against includes the first portion of the fold, followed by another character that has a multi-character fold that begins with the remaining portion of the fold, plus some more. </p>
<pre><code> &quot;s\N{U+DF}&quot; =~ /[\x{DF}foo]/i
</code></pre>
<p> is one such case. <code>&quot;\xDF&quot;</code> folds to <code>&quot;ss&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several Unicode case-folding bugs have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new (in 5.14.0) regular expression modifier <code>&quot;/a&quot;</code> when repeated like <code>&quot;/aa&quot;</code> forbids the characters outside the <font SIZE="-1">ASCII</font> range that match characters inside that range from matching under <code>&quot;/i&quot;</code>. This did not work under some circumstances, all involving alternation, such as: </p>
<pre><code> &quot;\N{KELVIN SIGN}&quot; =~ /k|foo/iaa;
</code></pre>
<p> succeeded inappropriately. This is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a case where it was possible that a freed buffer may have been read from when parsing a here document. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.14.1 represents approximately four weeks of development since Perl 5.14.0 and contains approximately 3500 lines of changes across 38 files from 17 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.14.1: </p>
<p> Bo Lindbergh, Claudio Ramirez, Craig A. Berry, David Leadbeater, Father Chrysostomos, Jesse Vincent, Jim Cromie, Justin Case, Karl Williamson, Leo Lapworth, Nicholas Clark, Nobuhiro Iwamatsu, smash, Tom Christiansen, Ton Hospel, Vladimir Timofeev, and Zsbán Ambrus.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
