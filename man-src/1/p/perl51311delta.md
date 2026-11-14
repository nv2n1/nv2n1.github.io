---
title: "perl51311delta(1)"
name: "perl51311delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl51311delta/"
---

<h2 class="name">NAME</h2>
 

 perl51311delta - what is new for perl v5.13.11 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.13.10 release and the 5.13.11 release. 

 If you are upgrading from an earlier release such as 5.13.9, first read perl5139delta, which describes differences between 5.13.9 and 5.13.10.

<h2>Security</h2>

<h3>User-defined regular expression properties</h3>

 Perl no longer allows a tainted regular expression to invoke a user-defined property via <tt>&quot;\p{...}&quot;</tt> syntax. It simply dies instead [perl #82616].

<h2>Incompatible Changes</h2>

<h3>local($_) will strip all magic from $_</h3>

 <i>local()</i> on scalar variables will give them a new value, but keep all their magic intact. This has proven to be problematic for the default scalar variable <tt>$_</tt>, where perlsub recommends that any subroutine that assigns to <tt>$_</tt> should localize it first. This would throw an exception if <tt>$_</tt> is aliased to a read-only variable, and could have various unintentional side-effects in general. 

 Therefore, as an exception to the general rule, local($_) will not only assign a new value to <tt>$_</tt>, but also remove all existing magic from it as well.

<h3>Passing references to <i>warn()</i></h3>

 An earlier Perl 5.13.x release changed <tt>&quot;warn($ref)&quot;</tt> to leave the reference unchanged, allowing <tt>$SIG{__WARN__}</tt> handlers to access the original reference. But this stopped warnings that were references from having the file and line number appended even when there was no <tt>$SIG{__WARN__}</tt> handler in place. 

 Now <tt>&quot;warn&quot;</tt> checks for the presence of such a handler and, if there is none, proceeds to stringify the reference and append the file and line number. This allows simple uses of <tt>&quot;warn&quot;</tt> for debugging to continue to work as they did before.

<h3><i>fork()</i> emulation will not wait for signalled children</h3>

 On Windows parent processes would not terminate until all forked childred had terminated first. However, <tt>&quot;kill('KILL', ...)&quot;</tt> is inherently unstable on pseudo-processes, and <tt>&quot;kill('TERM', ...)&quot;</tt> might not get delivered if the child if blocked in a system call. 

 To avoid the deadlock and still provide a safe mechanism to terminate the hosting process, Perl will now no longer wait for children that have been sent a <font SIZE="-1">SIGTERM</font> signal. It is up to the parent process to <i>waitpid()</i> for these children if child clean-up processing must be allowed to finish. However, it is also the responsibility of the parent then to avoid the deadlock by making sure the child process can't be blocked on I/O either. 

 See perlfork for more information about the <i>fork()</i> emulation on Windows.

<h3>Perl source code is read in text mode on Windows</h3>

 Perl scripts used to be read in binary mode on Windows for the benefit of the ByteLoader module (which is no longer part of core Perl). This had the side effect of breaking various operations on the <font SIZE="-1">DATA</font> filehandle, including <i>seek()</i>/<i>tell()</i>, and even simply reading from <font SIZE="-1">DATA</font> after file handles have been flushed by a call to <i>system()</i>, backticks, <i>fork()</i> etc. 

 The default build options for Windows have been changed to read Perl source code on Windows in text mode now. Hopefully ByteLoader will be updated on <font SIZE="-1">CPAN</font> to automatically handle this situation.

<h2>Performance Enhancements</h2>

<dl>
<dt>&bull;
<dd> An earlier optimisation to speed up <tt>&quot;my @array = ...&quot;</tt> and <tt>&quot;my %hash = ...&quot;</tt> assignments caused a bug and was disabled in Perl 5.12.0. 

 Now we have found another way to speed up these assignments [perl #82110].</dl>

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> <tt>&quot;attributes&quot;</tt> has been upgraded from version 0.13 to 0.14.
<dt>&bull;
<dd> <tt>&quot;base&quot;</tt> has been upgraded from version 2.15 to 2.16.
<dt>&bull;
<dd> <tt>&quot;CPAN&quot;</tt> has been upgraded from version 1.94_65 to 1.9600.
<dt>&bull;
<dd> <tt>&quot;CPANPLUS&quot;</tt> has been upgraded from version 0.9101 to 0.9103
<dt>&bull;
<dd> <tt>&quot;CPANPLUS::Dist::Build&quot;</tt> has been upgraded from version 0.52 to 0.54
<dt>&bull;
<dd> <tt>&quot;Cwd&quot;</tt> has been downgraded from version 3.37 to 3.36. 

 An optimisation that recent core changes have rendered unnecessary has been reverted.
<dt>&bull;
<dd> <tt>&quot;Devel::DProf&quot;</tt> has been upgraded from version 20110225.01 to 20110228.00.
<dt>&bull;
<dd> <tt>&quot;Digest::SHA&quot;</tt> has been upgraded from version 5.50 to 5.61 

 New <font SIZE="-1">SHA-512/224</font> and <font SIZE="-1">SHA-512/256</font> transforms ref. <font SIZE="-1">NIST</font> Draft <font SIZE="-1">FIPS</font> 180-4 (February 2011)
<dt>&bull;
<dd> <tt>&quot;ExtUtils::Command&quot;</tt> has been upgraded from version 1.16 to 1.17.
<dt>&bull;
<dd> <tt>&quot;File::Copy&quot;</tt> has been downgraded from version 2.22 to 2.21. 

 An optimisation that recent core changes have rendered unnecessary has been reverted.
<dt>&bull;
<dd> <tt>&quot;File::Glob&quot;</tt> has been upgraded from version 1.11 to 1.12.
<dt>&bull;
<dd> <tt>&quot;GDBM_File&quot;</tt> has been upgraded from version 1.13 to 1.14.
<dt>&bull;
<dd> <tt>&quot;Hash::Util&quot;</tt> has been upgraded from version 0.10 to 0.11.
<dt>&bull;
<dd> <tt>&quot;Hash::Util::FieldHash&quot;</tt> has been upgraded from version 1.08 to 1.09.
<dt>&bull;
<dd> <tt>&quot;HTTP::Tiny&quot;</tt> has been upgraded from version 0.010 to 0.011.
<dt>&bull;
<dd> <tt>&quot;I18N::Langinfo&quot;</tt> has been upgraded from version 0.07 to 0.08.
<dt>&bull;
<dd> <tt>&quot;IO&quot;</tt> has been upgraded from version 1.25_03 to 1.25_04.
<dt>&bull;
<dd> <tt>&quot;JSON::PP&quot;</tt> has been upgraded from version 2.27103 to 2.27105
<dt>&bull;
<dd> <tt>&quot;Locale::Codes&quot;</tt> has been upgraded from version 3.15 to 3.16
<dt>&bull;
<dd> <tt>&quot;Math::BigInt&quot;</tt> has been upgraded from version 1.992 to 1.994
<dt>&bull;
<dd> <tt>&quot;Math::BigInt::FastCalc&quot;</tt> has been upgraded from version 0.24_02 to 0.28
<dt>&bull;
<dd> <tt>&quot;Module::Build&quot;</tt> has been upgraded from version 0.37_05 to 0.3800
<dt>&bull;
<dd> <tt>&quot;Module::CoreList&quot;</tt> has been upgraded from version 2.45 to 2.46.
<dt>&bull;
<dd> <tt>&quot;mro&quot;</tt> has been upgraded from version 1.06 to 1.07.
<dt>&bull;
<dd> <tt>&quot;NDBM_File&quot;</tt> has been upgraded from version 1.11 to 1.12.
<dt>&bull;
<dd> <tt>&quot;parent&quot;</tt> has been upgraded from version 0.224 to 0.225
<dt>&bull;
<dd> <tt>&quot;Pod::Simple&quot;</tt> has been upgraded from version 3.15 to 3.16
<dt>&bull;
<dd> <tt>&quot;Storable&quot;</tt> has been upgraded from version 2.26 to 2.27.
<dt>&bull;
<dd> <tt>&quot;Sys::Hostname&quot;</tt> has been upgraded from version 1.15 to 1.16.
<dt>&bull;
<dd> <tt>&quot;Test::Harness&quot;</tt> has been upgraded from version 3.22 to 3.23
<dt>&bull;
<dd> <tt>&quot;Test::Simple&quot;</tt> has been upgraded from version 0.97_01 to 0.98
<dt>&bull;
<dd> <tt>&quot;Tie::Hash::NamedCapture&quot;</tt> has been upgraded from version 0.07 to 0.08. 

 Some of the Perl code has been converted to <font SIZE="-1">XS</font> for efficency's sake.
<dt>&bull;
<dd> <tt>&quot;Tie::RefHash&quot;</tt> has been upgraded from version 1.38 to 1.39.
<dt>&bull;
<dd> <tt>&quot;Unicode::Collate&quot;</tt> has been upgraded from version 0.72 to 0.73 

 <font SIZE="-1">DUCET</font> has been updated for Unicode 6.0.0 as Collate/allkeys.txt and the default UCA_Version is 22.
<dt>&bull;
<dd> <tt>&quot;Unicode::UCD&quot;</tt> has been upgraded from version 0.31 to 0.32. This includes a number of bug fixes:
<dl>
<dt>
<dd>
<dl>
<dt><i>charinfo()</i>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> It is now updated to Unicode Version 6 with Corrigendum #8, except, as with Perl 5.14, the code point at U+1F514 has no name.
<dt>&bull;
<dd> The Hangul syllable code points have the correct names, and their decompositions are always output without requiring Lingua::KO::Hangul::Util to be installed.
<dt>&bull;
<dd> The <font SIZE="-1">CJK</font> (Chinese-Japanese-Korean) code points U+2A700 - U+2B734 and U+2B740 - 2B81D are now properly handled.
<dt>&bull;
<dd> The numeric values are now output for those <font SIZE="-1">CJK</font> code points that have them.
<dt>&bull;
<dd> The names that are output for code points with multiple aliases are now the corrected ones.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt><i>charscript()</i>
<dd> This now correctly returns ``Unknown'' instead of <tt>&quot;undef&quot;</tt> for the script of a code point that hasn't been assigned another one.
<dt><i>charblock()</i>
<dd> This now correctly returns ``No_Block'' instead of <tt>&quot;undef&quot;</tt> for the block of a code point that hasn't been assigned to another one.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>&bull;
<dd> <tt>&quot;XS::Typemap&quot;</tt> has been upgraded from version 0.04 to 0.05.</dl>

<h2>Documentation</h2>

<h3>Changes to Existing Documentation</h3>

 <i>perlfunc</i>
<dl>
<dt>&bull;
<dd> Clarified the order in which to check <tt>$@</tt> and <tt>$!</tt> after <tt>&quot;do FILE&quot;</tt>. (<font SIZE="-1">RT</font> #80626)</dl>

<h2>Diagnostics</h2>

 The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.

<h3>New Diagnostics</h3>

<dl>
<dt>&bull;
<dd> Regexp modifier ``/%c'' may not appear twice 

 (F syntax) The regular expression pattern had one of the mutually exclusive modifiers repeated. Remove all but one of the occurrences.
<dt>&bull;
<dd> Regexp modifiers ``/%c'' and ``/%c'' are mutually exclusive 

 (F syntax) The regular expression pattern had more than one of the mutually exclusive modifiers. Retain only the modifier that is supposed to be there.
<dt>&bull;
<dd> Insecure user-defined property <tt>%s</tt> 

 (F) Perl detected tainted data when trying to compile a regular expression that contains a call to a user-defined character property function, i.e. <tt>&quot;\p{IsFoo}&quot;</tt> or <tt>&quot;\p{InFoo}&quot;</tt>. See ``User-Defined Character Properties'' in perlunicode and perlsec.</dl>

<h2>Testing</h2>

 Many of the tests have been refactored to use testing libraries more consistently. In some cases test files were created or deleted:
<dl>
<dt>&bull;
<dd> The tests for <tt>&quot;split /\s/&quot;</tt> and Unicode have been moved from <i>t/op/split.t</i> to the new <i>t/op/split_unicode.t</i>.
<dt>&bull;
<dd> <i>t/re/re.t</i> has been moved to <i>ext/re/t/re_funcs_u.t</i>.
<dt>&bull;
<dd> The tests for [perl #72922] have been moved from <i>t/re/qr.t</i> to the new <i>t/re/qr-72922.t</i>.
<dt>&bull;
<dd> <i>t/re/reg_unsafe.t</i> has been deleted and its only test moved to <i>t/re/pat_advanced.t</i>.</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> A fix for a bug in <tt>&quot;length(undef)&quot;</tt> in 5.13.4 introduced a regression that meant <tt>&quot;print length undef&quot;</tt> did not warn when warnings were enabled. It now correctly warns [perl #85508].
<dt>&bull;
<dd> The <tt>&quot;(?|...)&quot;</tt> regular expression construct no longer crashes if the final branch has more sets of capturing parentheses than any other branch. This was fixed in Perl 5.10.1 for the case of a single branch, but that fix did not take multiple branches into account [perl #84746].
<dt>&bull;
<dd> Accessing an element of a package array with a hard-coded number (as opposed to an arbitrary expression) would crash if the array did not exist. Usually the array would be autovivified during compilation, but typeglob manipulation could remove it, as in these two cases which used to crash: 

 <pre><code>
*d = *a;
print $d[0];
undef *d;
print $d[0];
</code></pre>
<dt>&bull;
<dd> <tt>&quot;#line&quot;</tt> directives in string evals were not properly updating the arrays of lines of code (<tt>&quot;@{&quot;_&lt;...&quot;}&quot;</tt>) that the debugger (or any debugging or profiling module) uses. In threaded builds, they were not being updated at all. In non-threaded builds, the line number was ignored, so any change to the existing line number would cause the lines to be misnumbered [perl #79442].
<dt>&bull;
<dd> <tt>$AUTOLOAD</tt> used to remain tainted forever if it ever became tainted. Now it is correctly untainted if an autoloaded method is called and the method name was not tainted.
<dt>&bull;
<dd> A bug has been fixed in the implementation of <tt>&quot;{...}&quot;</tt> quantifiers in regular expressions that prevented the code block in <tt>&quot;/((\w+)(?{ print $2 })){2}/&quot;</tt> from seeing the <tt>$2</tt> sometimes [perl #84294].
<dt>&bull;
<dd> <tt>&quot;sprintf&quot;</tt> now dies when passed a tainted scalar for the format. It did already die for arbitrary expressions, but not for simple scalars [perl #82250].
<dt>&bull;
<dd> <font SIZE="-1">DESTROY</font> methods of objects implementing ties are no longer able to crash by accessing the tied variable through a weak reference [perl #86328].
<dt>&bull;
<dd> On Windows, calling kill(9, <tt>$child</tt>) on a pseudo-process created by the <i>fork()</i> emulation is inherently unstable. It can also be responsible for overriding the parent process exit code with a value of '9' if the parent terminates right after killing the child. This condition will now happen a lot less often than before. 

 See also ``<i>fork()</i> emulation will not wait for signalled children'' for a better way to terminate child processes that avoids deadlocks altogether.
<dt>&bull;
<dd> Ensure that the <tt>&quot;exists &amp;Errno::EFOO&quot;</tt> idiom continues to work as documented. 

 A change post-5.12 caused the documented idiom not to work if Errno was loaded after the <tt>&quot;exists&quot;</tt> code had been compiled, as the compiler implicitly creates typeglobs in the Errno symbol table when it builds the optree for the <tt>&quot;exists code&quot;</tt>.</dl>

<h2>Acknowledgements</h2>

 Perl 5.13.11 represents approximately one month of development since Perl 5.13.10 and contains approximately 80,000 lines of changes across 549 files from 31 authors and committers: 

 Alastair Douglas, Arvan, Boris Ratner, brian d foy, Chris 'BinGOs' Williams, Craig A. Berry, David Golden, David Leadbeater, David Mitchell, Father Chrysostomos, Florian Ragwitz, Jan Dubois, Karl Williamson, Kevin Ryde, Leon Brocard, Leon Timmermans, Michael Stevens, Michael Witten, Moritz Lenz, Nicholas Clark, Paul Johnson, Peter John Acklam, Reini Urban, Robin Barker, Steve Hay, Sullivan Beck, Tony Cook, Vadim Konovalov, Yves Orton, Zefram and var Arnfjo.rd<i>-</i> Bjarmason

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" HREF="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>



<dt><a HREF="#lbAK">Performance Enhancements</a>
<dd>
<dt><a HREF="#lbAL">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAN">Documentation</a>
<dd>


<dt><a HREF="#lbAP">Diagnostics</a>
<dd>


<dt><a HREF="#lbAR">Testing</a>
<dd>
<dt><a HREF="#lbAS">Selected Bug Fixes</a>
<dd>
<dt><a HREF="#lbAT">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAU">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAV">SEE ALSO</a>
<dd></dl>
