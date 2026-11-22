---

title: "perl5133delta(1)"
name: "perl5133delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5133delta/"
description: "perl5133delta – what is new for perl v5.13.3"
---

<p> perl5133delta &#8211; what is new for perl v5.13.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.3 release and the 5.13.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.1, first read perl5132delta, which describes differences between 5.13.1 and 5.13.2.</p>
<h2>Core Enhancements</h2>
<h3>\o{&#8230;} for octals</h3>
<p> There is a new escape sequence, <tt>&quot;\o&quot;</tt>, in double-quote-like contexts. It must be followed by braces enclosing an octal number of at least one digit. It interpolates as the character with an ordinal value equal to the octal number. This construct allows large octal ordinals beyond the current max of 0777 to be represented. It also allows you to specify a character in octal which can safely be concatenated with other regex snippets and which won&#8217;t be confused with being a backreference to a regex capture group. See &#8220;Capture groups&#8221; in perlre.</p>
<h3>\N{<i>name</i>} and charnames enhancements</h3>
<p> <tt>&quot;\N{}&quot;</tt> and <tt>&quot;charnames::vianame&quot;</tt> now know about the abbreviated character names listed by Unicode, such as NBSP, SHY, LRO, ZWJ, etc., as well as all the customary abbreviations for the C0 and C1 control characters (such as ACK, BEL, CAN, etc.), as well as a few new variants in common usage of some C1 full names. </p>
<p> In the past, it was ineffective to override one of Perl&#8217;s abbreviations with your own custom alias. Now it works. </p>
<p> You can also create a custom alias directly to the ordinal of a character, known by <tt>&quot;\N{...}&quot;</tt>, <tt>&quot;charnames::vianame()&quot;</tt>, and <tt>&quot;charnames::viacode()&quot;</tt>. Previously, an alias had to be to an official Unicode character name. This made it impossible to create an alias for a code point that had no name, such as the ones reserved for private use. So this change allows you to make more effective use of private use characters. Only if there is no official name will <tt>&quot;charnames::viacode()&quot;</tt> return your custom one. </p>
<p> See charnames for details on all these changes.</p>
<h3>Uppercase X/B allowed in hexadecimal/binary literals</h3>
<p> Literals may now use either upper case <tt>&quot;0X...&quot;</tt> or <tt>&quot;0B...&quot;</tt> prefixes, in addition to the already supported <tt>&quot;0x...&quot;</tt> and <tt>&quot;0b...&quot;</tt> syntax. (RT#76296) (a674e8d, 333f87f) </p>
<p> C, Ruby, Python and PHP already supported this syntax, and it makes Perl more internally consistent. A round-trip with <tt>&quot;eval sprintf &quot;%#X&quot;, 0x10&quot;</tt> now returns <tt>16</tt> in addition to <tt>&quot;eval sprintf &quot;%#x&quot;, 0x10&quot;</tt>, which worked before.</p>
<h2>Incompatible Changes</h2>
<h3>\400 &#8211; \777</h3>
<p> Use of <tt>&quot;\400&quot;</tt> &#8211; <tt>&quot;\777&quot;</tt> in regexes in certain circumstances has given different, anomalous behavior than their use in all other double-quote-like contexts. Since 5.10.1, a deprecated warning message has been raised when this happens. Now, all double-quote-like contexts have the same behavior, namely to be equivalent to <tt>&quot;</tt>\x{100}&quot;</code> &#8211; <code>&quot;\x{1FF}&quot;</code>, with no deprecation warning. Use of these values in the command line option <code>&quot;-0&quot;</code> retains the current meaning to slurp input files whole; previously, this was documented only for <code>&quot;-0777&quot;</code>. It is recommended, however, because of various ambiguities, to use the new <code>&quot;\o{...}&quot;</code> construct to represent characters in octal. (fa1639c..f6993e9).  </p>
<h2>Deprecations</h2>
<h3>Omitting a space between a regular expression and subsequent word</h3>
<p> Omitting a space between a regex pattern or pattern modifiers and the following word is deprecated. Deprecation for regular expression <i>matches</i> was added in Perl 5.13.2. In this release, the deprecation is extended to regular expression <i>substitutions</i>. For example, <code>&quot;s/foo/bar/sand $bar&quot;</code> will still be parsed as <code>&quot;s/foo/bar/s and $bar&quot;</code> but will issue a warning. (aa78b66)  </p>
<h3>Deprecation warning added for deprecated-in-core .pl libs</h3>
<p> This is a mandatory warning, not obeying -X or lexical warning bits. The warning is modelled on that supplied by deprecate.pm for deprecated-in-core .pm libraries. It points to the specific CPAN distribution that contains the .pl libraries. The CPAN version, of course, does not generate the warning. (0111154)  </p>
<h2>Performance Enhancements</h2>
<p> There are several small optimizations to reduce CPU cache misses in various very commonly used modules like <code>&quot;warnings&quot;</code> and <code>&quot;Carp&quot;</code> as well in accessing file-handles for reading.  </p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&quot;autodie&quot;</dt>
<dd> <p> Upgraded from version 2.06_01 to 2.10. </p>
 </dd>
<dt>&quot;charnames&quot;</dt>
<dd> <p> Upgraded from version 1.08 to 1.10. </p>
<p> <code>&quot;viacode()&quot;</code> is now significantly faster. (f3227b7) </p>
 </dd>
<dt>&quot;lib&quot;</dt>
<dd> <p> Upgraded from version 0.62 to 0.63. </p>
 </dd>
<dt>&quot;threads&quot;</dt>
<dd> <p> Upgraded from version 1.77_02 to 1.77_03. </p>
 </dd>
<dt>&quot;threads::shared&quot;</dt>
<dd> <p> Upgraded from version 1.33_01 to 1.33_02. </p>
 </dd>
<dt>&quot;warnings&quot;</dt>
<dd> <p> Upgraded from version 1.09 to 1.10. </p>
<p> Calling <code>&quot;use warnings&quot;</code> without arguments is now significantly more efficient. (8452af9) </p>
 </dd>
<dt>&quot;Archive::Extract&quot;</dt>
<dd> <p> Upgraded from version 0.38 to 0.42. </p>
<p> Updates since 0.38 include: a safe print method that guards Archive::Extract from changes to $\; a fix to the tests when run in core perl; support for TZ files; and a modification for the lzma logic to favour IO::Uncompress::Unlzma (d7f8799) </p>
 </dd>
<dt>&quot;Archive::Tar&quot;</dt>
<dd> <p> Upgraded from version 1.54 to 1.64. </p>
<p> Important changes since 1.54 include: compatibility with busybox implementations of tar; a fix so that <code>&quot;write()&quot;</code> and <code>&quot;create_archive()&quot;</code> close only handles they opened; and a bug was fixed regarding the exit code of extract_archive. (afabe0e) </p>
 </dd>
<dt>&quot;Attribute::Handlers&quot;</dt>
<dd> <p> Upgraded from version 0.87 to 0.88. </p>
 </dd>
<dt>&quot;Compress::Raw::Bzip2&quot;</dt>
<dd> <p> Upgraded from version 2.024 to 2.027. </p>
 </dd>
<dt>&quot;Compress::Raw::Zlib&quot;</dt>
<dd> <p> Upgraded from version 2.024 to 2.027_01. </p>
 </dd>
<dt>&quot;Compress::Zlib&quot;</dt>
<dd> <p> Upgraded from version 2.024 to 2.027. </p>
 </dd>
<dt>&quot;CPANPLUS&quot;</dt>
<dd> <p> Upgraded from version 0.90 to 0.9007. </p>
<p> Fixed the shell test to skip if test is not being run under a terminal; resolved the issue where a prereq on Config would not be recognised as a core module. (d4e225a) </p>
 </dd>
<dt>&quot;Digest::MD5&quot;</dt>
<dd> <p> Upgraded from version 2.39 to 2.40. </p>
 </dd>
<dt>&quot;Digest::SHA&quot;</dt>
<dd> <p> Upgraded from version 5.47 to 5.48. </p>
 </dd>
<dt>&quot;Exporter&quot;</dt>
<dd> <p> Upgraded from version 5.64_02 to 5.64_03. </p>
<p> Exporter no longer overrides <code>$SIG{__WARN__}</code> (RT #74472) (9b86bb5) </p>
 </dd>
<dt>&quot;ExtUtils::CBuilder&quot;</dt>
<dd> <p> Upgraded from version 0.27 to 0.2703. </p>
 </dd>
<dt>&quot;ExtUtils::Manifest&quot;</dt>
<dd> <p> Upgraded from version 1.57 to 1.58. </p>
 </dd>
<dt>&quot;ExtUtils::ParseXS&quot;</dt>
<dd> <p> Upgraded from version 2.2205 to 2.2206. </p>
 </dd>
<dt>&quot;File::Copy&quot;</dt>
<dd> <p> Upgraded from version 2.19 to 2.20. </p>
<p> Skips suid tests on a nosuid partition. These tests were being skipped on OpenBSD, but nosuid partitions can exist on other systems too. Now it just checks if it can create a suid directory, if not the tests are skipped. Perl builds without errors in a nosuid /tmp with this patch. (cae9400) </p>
 </dd>
<dt>&quot;I18N::LangTags&quot;</dt>
<dd> <p> Upgraded from version 0.35 to 0.35_01. </p>
 </dd>
<dt>&quot;IPC::Cmd&quot;</dt>
<dd> <p> Upgraded from version 0.58 to 0.60. </p>
 </dd>
<dt>&quot;IPC::SysV&quot;</dt>
<dd> <p> Upgraded from version 2.01 to 2.03. </p>
 </dd>
<dt>&quot;Locale::Maketext&quot;</dt>
<dd> <p> Upgraded from version 1.14 to 1.15. </p>
<p> Locale::Maketext guts have been merged back into the main module (87d86da) and adds external cache support (ace47d6) </p>
 </dd>
<dt>&quot;Module::Build&quot;</dt>
<dd> <p> Upgraded from version 0.3603 to 0.3607. </p>
 </dd>
<dt>&quot;Module::CoreList&quot;</dt>
<dd> <p> Upgraded from version 2.34 to 2.36. </p>
 </dd>
<dt>&quot;Module::Load&quot;</dt>
<dd> <p> Upgraded from version 0.16 to 0.18. </p>
 </dd>
<dt>&quot;Term::ANSIColor&quot;</dt>
<dd> <p> Upgraded from version 2.02 to 3.00. </p>
 </dd>
<dt>&quot;Test::Harness&quot;</dt>
<dd> <p> Upgraded from version 3.17 to 3.21. </p>
<p> The core update from Test-Harness 3.17 to 3.21 fixed some things, but also introduced a known problem with argument passing to non-Perl tests. </p>
 </dd>
<dt>&quot;Time::HiRes&quot;</dt>
<dd> <p> Upgraded from version 1.9719 to 1.9721. </p>
 </dd>
<dt>&quot;Time::Piece&quot;</dt>
<dd> <p> Upgraded from version 1.15_01 to 1.20_01. </p>
 </dd>
<dt>&quot;Unicode::Collate&quot;</dt>
<dd> <p> Upgraded from version 0.52_01 to 0.53. </p>
<p> Includes Unicode Collation Algorithm 18 (74b94a7) </p>
 </dd>
<dt>&quot;Unicode::Normalize&quot;</dt>
<dd> <p> Upgraded from version 1.03 to 1.06. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> <i>perl5121delta</i> </p>
<p> The Perl 5.12.1 perldelta file was added from the Perl maintenance branch  </p>
<h3>Changes to Existing Documentation</h3>
<p> <i>General changes</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Octal character escapes in documentation now prefer a three-digit octal escape or the new <code>&quot;\o{...}&quot;</code> escape as they have more consistent behavior in different contexts than other forms. (ce7b6f0) (d8b950d) (e1f120a) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documentation now standardizes on the term &#8216;capture group&#8217; over &#8216;buffer&#8217; in regular expression documentation (c27a5cf) </p>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added cautionary note about ``no VERSION&#8216;&#8216; (e0de7c2) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added additional notes regarding srand when forking (d460397) </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Improved documentation of unusual character escapes (4068718, 9644846) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarified how hexadecimal escapes are interpreted, with particular attention to the treatment of invalid characters (9644846) </p>
 </dd></dl>
<p> <i>perlrun</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarified the behavior of the <code>&quot;-0NNN&quot;</code> switch for <code>&quot;-0400&quot;</code> or higher (7ba31cb) </p>
 </dd></dl>
<p> <i>perlpolicy</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added the policy on compatibility and deprecation along with definitions of terms like ``deprecation&#8217;&#8216; (70e4a83) </p>
 </dd></dl>
<p> <i>perlre</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added examples of the perils of not using \g{} when there are more than nine back-references (9d86067) </p>
 </dd></dl>
<p> <i>perltie</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Updated some examples for modern Perl style (67d00dd) </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> <i>perldb</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The remote terminal works after forking and spawns new sessions &#8211; one for each forked process (11653f7) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Uses the less pager path from Config instead of searching for it (bf320d6) </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Adjusted &#8216;make test.valgrind&#8217; to account for cpan/dist/ext separation (e07ce2e) </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>t/harness</i> clears PERL5LIB, PERLLIB, PERL5OPT as t/TEST does (a2d3de1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many common testing routines were refactored into t/lib/common.pl </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several test files have been modernized to use Test::More </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Discontinued Platforms</h3>
<dl>
<dt>MacOS Classic</dt>
<dd> <p> Support for MacOS Classic within ExtUtils::MakeMaker was removed from Perl in December 2004. Vestigial MacOS Classic specific code has now been removed from other core modules as well (8f8c2a4..c457df0) </p>
 </dd></dl>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Win32</dt>
<dd> <p> t/io/openpid.t now uses the <i>alarm()</i> watchdog strategy for more robustness (5732108) </p>
 </dd></dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Under some circumstances, the <code>&quot;CvGV()&quot;</code> field of a CV is now reference counted. To ensure consistent behaviour, direct assignment to it, for example <code>&quot;CvGV(cv) = gv&quot;</code> is now a compile-time error. A new macro, <code>&quot;CvGV_set(cv,gv)&quot;</code> has been introduced to perform this operation safely. Note that modification of this field is not part of of the public API, regardless of this new macro. This change caused some issues in modules that used the private <code>&quot;GvGV()&quot;</code> field. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It is now possible for XS code to hook into Perl&#8217;s lexical scope mechanism at compile time, using the new <code>&quot;Perl_blockhook_register&quot;</code> function. See ``Compile-time scope hooks&#8217;&#8216; in perlguts. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added <code>&quot;Perl_croak_no_modify()&quot;</code> to implement <code>&quot;Perl_croak(&quot;%s&quot;, PL_no_modify)&quot;</code> (6ad8f25) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added prototypes for <code>&quot;tie()&quot;</code> and <code>&quot;untie()&quot;</code> to allow overloading (RT#75902) (1db4d19) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Adds <code>&quot;my_[l]stat_flags()&quot;</code> to replace <code>&quot;my_[l]stat()&quot;</code>. <code>&quot;my_stat()&quot;</code> and <code>&quot;my_lstat()&quot;</code> call get magic on the stack arg, so create <code>&quot;_flags()&quot;</code> variants that allow us to control this. (0d7d409) </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Some work has been done on the internal pointers that link between symbol tables (stashes), typeglobs and subroutines. This has the effect that various edge cases related to deleting stashes or stash entries (e.g. &lt;%FOO:: = ()&gt;), and complex typeglob or code reference aliasing, will no longer crash the interpreter. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed <i>readline()</i> when interrupted by signals so it no longer returns the ``same thing&#8217;&#8216; as before or random memory </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a regression of <i>kill()</i> when a match variable is used for the process ID to kill (RT#75812) (8af710e) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed several subtle bugs in <i>sort()</i> when <code>@_</code> is accessed within a subroutine used for sorting (RT#72334) (8f443ca) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Catch <i>yyparse()</i> exceptions in <code>&quot;(?{...})&quot;</code> (RT#2353) (634d691) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoid UTF-8 cache panics with offsets beyond a string (RT #75898) (3e2d381) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed POSIX::strftime memory leak (RT#73520) (c4bc4aa) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Doesn&#8217;t set strict with <code>&quot;no VERSION&quot;</code> if <code>&quot;VERSION&quot;</code> is greater than 5.12 (da8fb5d) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoids multiple FETCH/stringify on filetest ops (40c852d) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed issue with string <code>&quot;eval&quot;</code> not detecting taint of overloaded/tied arguments (RT #75716) (895b760) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix potential crashes of string <code>&quot;eval&quot;</code> when evaluating a object with overloaded stringification by creating a stringified copy when necessary (3e5c018) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug where overloaded stringification could remove tainting (RT #75716) (a02ec77) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Plugs more memory leaks in vms.c. (9e2bec0) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix pthread include error for Time::Piece (e9f284c) </p>
 </dd></dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Bug fixes involving CvGV reference counting break Sub::Name. A patch has been sent upstream to the maintainer </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>readline()</i> returns an empty string instead of undef when it is interrupted by a signal </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test-Harness was updated from 3.17 to 3.21 for this release. A rewrite in how it handles non-Perl tests (in 3.17_01) broke argument passing to non-Perl tests with prove (RT #59186), and required that non-Perl tests be run as <code>&quot;prove ./test.sh&quot;</code> instead of <code>&quot;prove test.sh&quot;</code> These issues are being solved upstream, but didn&#8217;t make it into this release. They&#8217;re expected to be fixed in time for perl v5.13.4. (RT #59457) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;version&quot;</code> now prevents object methods from being called as class methods (d808b68) </p>
 </dd></dl>
<h2>Errata</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Retroactively added the Acknowledgements list to perl5132delta, which was excluded in the original release (d1e2db0) </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.3 represents approximately one month of development since Perl 5.13.2, and contains 12,184 lines of changes across 575 files from 104 authors and committers. </p>
<p> Thank you to the following for contributing to this release: </p>
<p> Abhijit Menon-Sen, Abigail, Alex Davies, Alex Vandiver, Alexandr Ciornii, Andreas J. Koenig, Andrew Rodland, Andy Dougherty, Aristotle Pagaltzis, Arkturuz, Ben Morrow, Bo Borgerson, Bo Lindbergh, Brad Gilbert, Bram, Brian Phillips, Chas. Owens, Chip Salzenberg, Chris Williams, Craig A. Berry, Curtis Jewell, Dan Dascalescu, Daniel Frederick Crisman, Dave Rolsky, David Caldwell, David E. Wheeler, David Golden, David Leadbeater, David Mitchell, Dennis Kaarsemaker, Eric Brine, Father Chrysostomos, Florian Ragwitz, Frank Wiegand, Gene Sullivan, George Greer, Gerard Goossen, Gisle Aas, Goro Fuji, Graham Barr, H.Merijn Brand, Harmen, Hugo van der Sanden, James E Keenan, James Mastros, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Jim Cromie, John Peacock, Jos Boumans, Josh ben Jore, Karl Williamson, Kevin Ryde, Leon Brocard, Lubomir Rintel, Maik Hentsche, Marcus Holland-Moritz, Matt Johnson, Matt S Trout, Max Maischein, Michael Breen, Michael G Schwern, Moritz Lenz, Nga Tang Chan, Nicholas Clark, Nick Cleaton, Nick Johnston, Niko Tyni, Offer Kaye, Paul Marquess, Philip Hazel, Philippe Bruhat, Rafael Garcia-Suarez, Rainer Tammer, Reini Urban, Ricardo Signes, Richard Soderberg, Robin Barker, Ruslan Zakirov, Salvador Fandino, Salvador Ortiz Garcia, Shlomi Fish, Sinan Unur, Sisyphus, Slaven Rezic, Steffen Mueller, Stepan Kasal, Steve Hay, Steve Peters, Sullivan Beck, Tim Bunce, Todd Rinaldo, Tom Christiansen, Tom Hukins, Tony Cook, Vincent Pit, Yuval Kogman, Yves Orton, Zefram, brian d foy, chromatic, kmx, var Arnfjo.rd <i>-</i> Bjarmason  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on CPAN.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><i>INSTALL</i><i></i> file for how to build Perl. </p>
<p> The <i></i><i>README</i><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
