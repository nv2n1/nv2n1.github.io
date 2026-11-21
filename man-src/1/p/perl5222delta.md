---
title: "perl5222delta(1)"
name: "perl5222delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5222delta/"
description: "perl5222delta – what is new for perl v5.22.2"
---
<h2 class="name">NAME</h2>
<p> perl5222delta - what is new for perl v5.22.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.22.1 release and the 5.22.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.22.0, first read perl5221delta, which describes differences between 5.22.0 and 5.22.1.  </p>
<h2>Security</h2>
<h3>Fix out of boundary access in Win32 path handling</h3>
<p> This is <font SIZE="-1">CVE-2015-8608.</font> For more information see [perl #126755] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126755">https://rt.perl.org/Ticket/Display.html?id=126755</a>&gt;.  </p>
<h3>Fix loss of taint in canonpath()</h3>
<p> This is <font SIZE="-1">CVE-2015-8607.</font> For more information see [perl #126862] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126862">https://rt.perl.org/Ticket/Display.html?id=126862</a>&gt;.  </p>
<a href="/docs/linux/man/3-mkstemp/"></a><h3>Set proper umask before calling mkstemp (3)</h3>
<p> In 5.22.0 perl started setting umask to <code>0600</code> before calling <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</code> and restoring it afterwards. This wrongfully tells <code><a href="/docs/linux/man/2-open/">open</a>(2)</code> to strip the owner read and write bits from the given mode before applying it, rather than the intended negation of leaving only those bits in place. </p>
<p> Systems that use mode <code>0666</code> in <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</code> (like old versions of glibc) create a file with permissions <code>0066</code>, leaving world read and write permissions regardless of current umask. </p>
<p> This has been fixed by using umask <code>0177</code> instead. </p>
<p> [perl #127322] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127322">https://rt.perl.org/Ticket/Display.html?id=127322</a>&gt;  </p>
<h3>Avoid accessing uninitialized memory in Win32 crypt()</h3>
<p> Validation that will detect both a short salt and invalid characters in the salt has been added. </p>
<p> [perl #126922] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126922">https://rt.perl.org/Ticket/Display.html?id=126922</a>&gt;  </p>
<h3>Remove duplicate environment variables from environ</h3>
<p> Previously, if an environment variable appeared more than once in <code>&quot;environ[]&quot;</code>, <code>%ENV</code> would contain the last entry for that name, while a typical <code>&quot;getenv()&quot;</code> would return the first entry. We now make sure <code>%ENV</code> contains the same as what <code>&quot;getenv()&quot;</code> returns. </p>
<p> Secondly, we now remove duplicates from <code>&quot;environ[]&quot;</code>, so if a setting with that name is set in <code>%ENV</code> we won&#8217;t pass an unsafe value to a child process. </p>
<p> This is <font SIZE="-1">CVE-2016-2381.</font>  </p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with Perl 5.22.1. If any exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs&#8217;&#8216; below.  </p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> File::Spec has been upgraded from version 3.56 to 3.56_01. </p>
<p> <code>&quot;canonpath()&quot;</code> now preserves taint. See &quot;Fix loss of taint in <code>&quot;canonpath()&quot;</code>&quot;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 5.20151213 to 5.20160429. </p>
<p> The version number of Digest::SHA listed for Perl 5.18.4 was wrong and has been corrected. Likewise for the version number of Config in 5.18.3 and 5.18.4. [perl #127624] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127624">https://rt.perl.org/Ticket/Display.html?id=127624</a>&gt; </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perldiag</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The explanation of the warning ``unable to close filehandle <code>%s</code> properly: <code>%s</code>&#8216;&#8216; which can occur when doing an implicit close of a filehandle has been expanded and improved. </p>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;hex()&quot;</code> has been revised to clarify valid inputs. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Dtrace builds now build successfully on systems with a newer dtrace that require an input object file that uses the probes in the <i>.d</i> file. </p>
<p> Previously the probe would fail and cause a build failure. </p>
<p> [perl #122287] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122287">https://rt.perl.org/Ticket/Display.html?id=122287</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> no longer probes for <i>libnm</i> by default. Originally this was the ``New Math&#8217;&#8216; library, but the name has been re-used by the <font SIZE="-1">GNOME</font> NetworkManager. </p>
<p> [perl #127131] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127131">https://rt.perl.org/Ticket/Display.html?id=127131</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> now knows about gcc 5. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compiling perl with <code>-DPERL_MEM_LOG</code> now works again. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Darwin</dt>
<dd> <p> Compiling perl with <code>-Dusecbacktrace</code> on Darwin now works again. </p>
<p> [perl #127764] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127764">https://rt.perl.org/Ticket/Display.html?id=127764</a>&gt; </p>
 </dd>
<dt><font SIZE="-1">OS</font> X/Darwin</dt>
<dd> <p> Builds with both <code>-DDEBUGGING</code> and threading enabled would fail with a ``panic: free from wrong pool&#8217;&#8216; error when built or tested from Terminal on <font SIZE="-1">OS X.</font> This was caused by perl&#8217;s internal management of the environment conflicting with an atfork handler using the libc <code>&quot;setenv()&quot;</code> function to update the environment. </p>
<p> Perl now uses <code>&quot;setenv()&quot;</code>/<code>&quot;unsetenv()&quot;</code> to update the environment on <font SIZE="-1">OS X.</font> </p>
<p> [perl #126240] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126240">https://rt.perl.org/Ticket/Display.html?id=126240</a>&gt; </p>
 </dd>
<dt>ppc64el</dt>
<dd> <p> The floating point format of ppc64el (Debian naming for little-endian PowerPC) is now detected correctly. </p>
 </dd>
<dt>Tru64</dt>
<dd> <p> A test failure in <i>t/porting/extrefs.t</i> has been fixed. </p>
 </dd></dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> An unwarranted assertion in <code>&quot;Perl_newATTRSUB_x()&quot;</code> has been removed. If a stub subroutine definition with a prototype has been seen, then any subsequent stub (or definition) of the same subroutine with an attribute was causing an assertion failure because of a null pointer. </p>
<p> [perl #126845] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126845">https://rt.perl.org/Ticket/Display.html?id=126845</a>&gt; </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Calls to the placeholder <code>&amp;PL_sv_yes</code> used internally when an <code>&quot;import()&quot;</code> or <code>&quot;unimport()&quot;</code> method isn&#8217;t found now correctly handle scalar context. [perl #126042] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126042">https://rt.perl.org/Ticket/Display.html?id=126042</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;pipe()&quot;</code> operator would assert for <code>&quot;DEBUGGING&quot;</code> builds instead of producing the correct error message. The condition asserted on is detected and reported on correctly without the assertions, so the assertions were removed. [perl #126480] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126480">https://rt.perl.org/Ticket/Display.html?id=126480</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In some cases, failing to parse a here-doc would attempt to use freed memory. This was caused by a pointer not being restored correctly. [perl #126443] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126443">https://rt.perl.org/Ticket/Display.html?id=126443</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now reports more context when it sees an array where it expects to see an operator, and avoids an assertion failure. [perl #123737] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123737">https://rt.perl.org/Ticket/Display.html?id=123737</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If a here-doc was found while parsing another operator, the parser had already read end of file, and the here-doc was not terminated, perl could produce an assertion or a segmentation fault. This now reliably complains about the unterminated here-doc. [perl #125540] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125540">https://rt.perl.org/Ticket/Display.html?id=125540</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parsing beyond the end of the buffer when processing a <code>&quot;#line&quot;</code> directive with no filename is now avoided. [perl #127334] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127334">https://rt.perl.org/Ticket/Display.html?id=127334</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.22.0 added support for the C99 hexadecimal floating point notation, but sometimes misparsed hex floats. This has been fixed. [perl #127183] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127183">https://rt.perl.org/Ticket/Display.html?id=127183</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain regex patterns involving a complemented posix class in an inverted bracketed character class, and matching something else optionally would improperly fail to match. An example of one that could fail is <code>&quot;qr/_?[^\Wbar]\x{100}/&quot;</code>. This has been fixed. [perl #127537] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127537">https://rt.perl.org/Ticket/Display.html?id=127537</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an issue with <code>&quot;pack()&quot;</code> where <code>&quot;pack &quot;H&quot;&quot;</code> (and <code>&quot;pack &quot;h&quot;&quot;</code>) could read past the source when given a non-utf8 source and a utf8 target. [perl #126325] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126325">https://rt.perl.org/Ticket/Display.html?id=126325</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed some cases where perl would abort due to a segmentation fault, or a C-level assert. [perl #126193] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126193">https://rt.perl.org/Ticket/Display.html?id=126193</a>&gt; [perl #126257] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126257">https://rt.perl.org/Ticket/Display.html?id=126257</a>&gt; [perl #126258] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126258">https://rt.perl.org/Ticket/Display.html?id=126258</a>&gt; [perl #126405] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126405">https://rt.perl.org/Ticket/Display.html?id=126405</a>&gt; [perl #126602] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126602">https://rt.perl.org/Ticket/Display.html?id=126602</a>&gt; [perl #127773] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127773">https://rt.perl.org/Ticket/Display.html?id=127773</a>&gt; [perl #127786] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127786">https://rt.perl.org/Ticket/Display.html?id=127786</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A memory leak when setting <code>$ENV{foo}</code> on Darwin has been fixed. [perl #126240] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126240">https://rt.perl.org/Ticket/Display.html?id=126240</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now correctly raises an error when trying to compile patterns with unterminated character classes while there are trailing backslashes. [perl #126141] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126141">https://rt.perl.org/Ticket/Display.html?id=126141</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;NOTHING&quot;</code> regops and <code>&quot;EXACTFU_SS&quot;</code> regops in <code>&quot;make_trie()&quot;</code> are now handled properly. [perl #126206] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126206">https://rt.perl.org/Ticket/Display.html?id=126206</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now only tests <code>&quot;semctl()&quot;</code> if we have everything needed to use it. In FreeBSD the <code>&quot;semctl()&quot;</code> entry point may exist, but it can be disabled by policy. [perl #127533] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127533">https://rt.perl.org/Ticket/Display.html?id=127533</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression that allowed undeclared barewords as hash keys to work despite strictures has been fixed. [perl #126981] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126981">https://rt.perl.org/Ticket/Display.html?id=126981</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As an optimization (introduced in Perl 5.20.0), <code>&quot;uc()&quot;</code>, <code>&quot;lc()&quot;</code>, <code>&quot;ucfirst()&quot;</code> and <code>&quot;lcfirst()&quot;</code> sometimes modify their argument in-place rather than returning a modified copy. The criteria for this optimization has been made stricter to avoid these functions accidentally modifying in-place when they should not, which has been happening in some cases, e.g. in List::Util. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Excessive memory usage in the compilation of some regular expressions involving non-ASCII characters has been reduced. A more complete fix is forthcoming in Perl 5.24.0. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.22.2 represents approximately 5 months of development since Perl 5.22.1 and contains approximately 3,000 lines of changes across 110 files from 24 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 1,500 lines of changes to 52 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.22.2: </p>
<p> Aaron Crane, Abigail, Andreas König, Aristotle Pagaltzis, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, David Golden, David Mitchell, H.Merijn Brand, James E Keenan, Jarkko Hietaniemi, Karen Etheridge, Karl Williamson, Matthew Horsfall, Niko Tyni, Ricardo Signes, Sawyer X, Stevan Little, Steve Hay, Todd Rinaldo, Tony Cook, Vladimir Timofeev, Yves Orton. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
