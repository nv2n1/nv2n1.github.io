---
title: "perl5132delta(1)"
name: "perl5132delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5132delta/"
description: "perl5132delta – what is new for perl v5.13.2"
---

<h2 class="name">NAME</h2>
<p> perl5132delta &#8211; what is new for perl v5.13.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.2 release and the 5.13.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.10, first read perl5120delta, which describes differences between 5.10 and 5.12.</p>
<h2>Incompatible Changes</h2>
<h3>localised tied scalars are tied again.</h3>
<p> The change in behaviour in 5.13.1 of localising tied scalar values has been reverted to the existing 5.12.0 and earlier behaviour (the change for arrays and hashes remains).</p>
<h3>Naming fixes in Policy_sh.SH may invalidate Policy.sh</h3>
<p> Several long-standing typos and naming confusions in Policy_sh.SH have been fixed, standardizing on the variable names used in config.sh. </p>
<p> This will change the behavior of Policy.sh if you happen to have been accidentally relying on the Policy.sh incorrect behavior. We&#8217;d appreciate feedback from anyone using Policy.sh to be sure nothing is broken by this change (c1bd23).</p>
<h3>Stashes are now always defined</h3>
<p> <tt>&quot;defined %Foo::&quot;</tt> now always returns true, even when no symbols have yet been defined in that package. </p>
<p> This is a side effect of removing a special case kludge in the tokeniser, added for 5.10.0, to hide side effects of changes to the internal storage of hashes that to drastically reduce their memory usage overhead. </p>
<p> Calling defined on a stash has been deprecated since 5.6.0, warned on lexicals since 5.6.0, and has warned for stashes (and other package variables) since 5.12.0. <tt>&quot;defined %hash&quot;</tt> has always exposed an implementation detail &#8211; emptying a hash by deleting all entries from it does not make <tt>&quot;defined %hash&quot;</tt> false, hence <tt>&quot;defined %hash&quot;</tt> is not valid code to determine whether an arbitrary hash is empty. Instead, use the behaviour that an empty <tt>%hash</tt> always returns false in a scalar context.</p>
<h2>Core Enhancements</h2>
<h3>Non-destructive substitution</h3>
<p> The substitution operator now supports a <tt>&quot;/r&quot;</tt> option that copies the input variable, carries out the substitution on the copy and returns the result. The original remains unmodified. </p>
<pre>
  my $old = 'cat';
  my $new = $old =~ s/cat/dog/r;
  # $old is 'cat' and $new is 'dog'
</pre>
<p> This is particularly useful with <tt>&quot;map&quot;</tt>. See perlop for more examples (4f4d75, 000c65).</p>
<h3>package block syntax</h3>
<p> A package declaration can now contain a code block, in which case the declaration is in scope only inside that block. So <tt>&quot;package Foo { ... }&quot;</tt> is precisely equivalent to <tt>&quot;{ package Foo; ... }&quot;</tt>. It also works with a version number in the declaration, as in <tt>&quot;package Foo 1.2 { ... }&quot;</tt>. See perlfunc (434da3..36f77d, 702646).</p>
<h3><font SIZE="-1">CLONE_PARAMS</font> structure added to ease correct thread creation</h3>
<p> Modules that create threads should now create <tt>&quot;CLONE_PARAMS&quot;</tt> structures by calling the new function <tt>&quot;Perl_clone_params_new()&quot;</tt>, and free them with <tt>&quot;Perl_clone_params_del()&quot;</tt>. This will ensure compatibility with any future changes to the internals of the <tt>&quot;CLONE_PARAMS&quot;</tt> structure layout, and that it is correctly allocated and initialised.</p>
<h3>perl -h no longer recommends -w</h3>
<p> perl -h used to mark the -w option as recommended; since this option is far less useful than it used to be due to lexical &#8216;use warnings&#8217; and since perl -h is primary a list and brief explanation of the command line switches, the recommendation has now been removed (60eaec).</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules</h3>
<p> <i>Locale-Codes 3.13</i> </p>
<p> Locale::Country, Locale::Language and Locale::Currency were updated from 3.12 to 3.13 of the Locale-Codes distribution to include locale code changes (e1137b). </p>
<p> <i>Thread-Semaphore 2.11</i> </p>
<p> Added new methods -&gt;<i>down_nb()</i> and -&gt;<i>down_force()</i> at the suggestion of Rick Garlick. </p>
<p> Refactored methods to skip argument validation when no argument is supplied. </p>
<p> (04febe, f06daa) </p>
<p> <i></i><font SIZE="-1"><i>CPAN</i></font><i>.pm 1.94_57</i></p>
<dl>
<dt>&bull;</p>
<dd> release 1.94_57</p>
<dt>&bull;</p>
<dd> bugfix: treat modules correctly that are deprecated in perl 5.12.</p>
<dt>&bull;</p>
<dd> bugfix: <font SIZE="-1">RT</font> #57482 and #57788 revealed that configure_requires implicitly assumed build_requires instead of normal requires. (Reported by Andrew Whatson and Father Chrysostomos respectively)</p>
<dt>&bull;</p>
<dd> testfix: solaris should run the tests without expect because (some?) solaris have a broken expect</p>
<dt>&bull;</p>
<dd> testfix: run tests with cache_metadata off to prevent spill over effects from previous test runs</dl>
<p> (742adb) </p>
<p> <i>Hash::Util warning fix</i> </p>
<p> Hash::Util now enables &#8220;no warnings &#8216;uninitialized&#8221;&#8217; to suppress spurious warnings from undefined hash values (<font SIZE="-1">RT</font> #74280). </p>
<p> <i>B::Deparse now handles &#8216;no </i><font SIZE="-1"><i>VERSION</i></font><i>&#8216;</i> </p>
<p> The &#8216;no 5.13.2&#8217; or similar form is now correctly handled by B::Deparse. </p>
<p> <i>IO::Socket doc additions</i> </p>
<p> getsockopt and setsockopt are now documented. </p>
<p> <i>B::Concise updated for OPpDEREF</i> </p>
<p> B::Concise marks rv2sv, rv2av and rv2hv ops with the new OPpDEREF flag as &#8220;DREFed&#8221;. </p>
<p> <i>File::Copy doc clarification</i> </p>
<p> An extra stanza was added explaining behaviours when the copy destination already exists and is a directory. </p>
<p> <i>Multiple </i><font SIZE="-1"><i>POD</i></font><i> spelling fixes.</i> </p>
<p> Fixes were made to VMS::DCLsym, mro, Search::Dist, B::t::OptreeCheck and <font SIZE="-1">UNIVERSAL</font>.</p>
<h2>Changes to Existing Documentation</h2>
<h3>Replace wrong tr/// table in perlebcdic.pod</h3>
<p> perlebcdic.pod contains a helpful table to use in tr/// to convert between <font SIZE="-1">EBCDIC</font> and Latin1/ASCII. Unfortunately, the table was the inverse of the one it describes, though the code that used the table worked correctly for the specific example given. </p>
<p> The table has been changed to its inverse, and the sample code changed to correspond, as this is easier for the person trying to follow the instructions since deriving the old table is somewhat more complicated. </p>
<p> The table has also been changed to hex from octal, as that is more the norm these days, and the recipes in the pod altered to print out leading zeros to make all the values the same length, as the table that they can generate has them (5f26d5).</p>
<h3>Document tricks for user-defined casing</h3>
<p> perlunicode.pod now contains an explanation of how to override, mangle and otherwise tweak the way perl handles upper, lower and other case conversions on unicode data, and how to provide scoped changes to alter one&#8217;s own code&#8217;s behaviour without stomping on anybody else (71648f).</p>
<h3>Document $# and $* as removed and clarify $#array usage</h3>
<p> $# and $* were both disabled as of perl5 version 10; this release adds documentation to that effect, a description of the results of continuing to try and use them, and a note explaining that $# can also function as a sigil in the $#array form (7f315d2).</p>
<h3><font SIZE="-1">INSTALL</font> explicitly states the requirement for C89</h3>
<p> This was already true but it&#8217;s now Officially Stated For The Record (51eec7).</p>
<h3>No longer advertise Math::TrulyRandom</h3>
<p> This module hasn&#8217;t been updated since 1996 so we can&#8217;t recommend it any more (83918a).</p>
<h3>perlfaq synchronised to upstream</h3>
<p> The <font SIZE="-1">FAQ</font> has been updated to commit 37550b8f812e591bcd0dd869d61677dac5bda92c from the perlfaq repository at git [at] github.com:briandfoy/perlfaq.git</p>
<h2>Performance Enhancements</h2>
<p> Only allocate entries for <tt>@_</tt> on demand &#8211; this not only saves memory per subroutine defined but should hopefully improve <font SIZE="-1">COW</font> behaviour (77bac2).</p>
<h3>Multiple small improvements to threads</h3>
<p> The internal structures of threading now make fewer <font SIZE="-1">API</font> calls and fewer allocations, resulting in noticeably smaller object code. Additionally, many thread context checks have been deferred so that they&#8217;re only done when required (although this is only possible for non-debugging builds).</p>
<h3>Size optimisations to <font SIZE="-1">SV</font> and <font SIZE="-1">HV</font> structures</h3>
<p> xhv_fill has been eliminated from struct xpvhv, saving 1 <font SIZE="-1">IV</font> per hash and on some systems will cause struct xpvhv to become cache aligned. To avoid this memory saving causing a slowdown elsewhere, boolean use of HvFILL now calls HvTOTALKEYS instead (which is equivalent) &#8211; so while the fill data when actually required is now calculated on demand, the cases when this needs to be done should be few and far between (f4431c .. fcd245). </p>
<p> The order of structure elements in <font SIZE="-1">SV</font> bodies has changed. Effectively, the <font SIZE="-1">NV</font> slot has swapped location with <font SIZE="-1">STASH</font> and <font SIZE="-1">MAGIC</font>. As all access to <font SIZE="-1">SV</font> members is via macros, this should be completely transparent. This change allows the space saving for PVHVs documented above, and may reduce the memory allocation needed for PVIVs on some architectures.</p>
<h3>Optimisation of regexp engine string comparison work</h3>
<p> The foldEQ_utf8 <font SIZE="-1">API</font> function for case-insensitive comparison of strings (which is used heavily by the regexp engine) was substantially refactored and optimised &#8211; and its documentation much improved as a free bonus gift (8b3587, e6226b).</p>
<h3>Memory consumption improvements to Exporter</h3>
<p> The <tt>@EXPORT_FAIL</tt> <font SIZE="-1">AV</font> is no longer created unless required, hence neither is the typeglob backing it &#8211; this saves about 200 bytes per Exporter using package that doesn&#8217;t use this functionality.</p>
<h2>Installation and Configuration Improvements</h2>
<h3>Compilation improvements</h3>
<p> Fix <font SIZE="-1">CCINCDIR</font> and <font SIZE="-1">CCLIBDIR</font> for mingw64 cross compiler to correctly be under $(<font SIZE="-1">CCHOME</font>)\mingw\include and \lib rather than immediately below $(<font SIZE="-1">CCHOME</font>). </p>
<p> This means the &#8216;incpath&#8217;, &#8216;libpth&#8217;, &#8216;ldflags&#8217;, &#8216;lddlflags&#8217; and &#8216;ldflags_nolargefiles&#8217; values in Config.pm and Config_heavy.pl are now set correctly (23ae7f).</p>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Timely cleanup of SVs that are cloned into a new thread but then discovered to be orphaned (i.e. their owners are -not- cloned) (e42956)</p>
<dt>&bull;</p>
<dd> Don&#8217;t accidentally clone lexicals in scope within active stack frames in the parent when creating a child thread (<font SIZE="-1">RT</font> #73086) (05d04d).</p>
<dt>&bull;</p>
<dd> Avoid loading feature.pm when &#8216;no 5.13.2;&#8217; or similar is encountered (faee19).</p>
<dt>&bull;</p>
<dd> Trap invalid use of SvIVX on SVt_REGEXP when assertions are on (e77da3)</p>
<dt>&bull;</p>
<dd> Don&#8217;t stamp on <tt>$DB::single</tt>, <tt>$DB::trace</tt> and <tt>$DB::signal</tt> if they already have values when $^P is assigned to (<font SIZE="-1">RT</font> #72422) (4c0f30).</p>
<dt>&bull;</p>
<dd> chop now correctly handles perl&#8217;s extended <font SIZE="-1">UTF-8</font> (<font SIZE="-1">RT</font> #73246) (65ab92)</p>
<dt>&bull;</p>
<dd> Defer signal handling when shared <font SIZE="-1">SV</font> locks are held to avoid deadlocks (<font SIZE="-1">RT</font> #74868) (65c742).</p>
<dt>&bull;</p>
<dd> <i>glob()</i> no longer crashes when <tt>%File::Glob::</tt> is empty and CORE::GLOBAL::glob isn&#8217;t present (4984aa).</p>
<dt>&bull;</p>
<dd> perlbug now always permits the sender address to be changed before sending &#8211; if you were having trouble sending bug reports before now, this should fix it, we hope (e6eb90).</p>
<dt>&bull;</p>
<dd> Overloading now works properly in conjunction with tied variables. What formerly happened was that most ops checked their arguments for overloading <i>before</i> checking for magic, so for example an overloaded object returned by a tied array access would usually be treated as not overloaded (<font SIZE="-1">RT</font> #57012) (6f1401, ed3b9b, 6a5f8c .. 24328f).</p>
<dt>&bull;</p>
<dd> Independently, a bug was fixed that prevented <tt>$tied</tt>-&gt;() from always calling <font SIZE="-1">FETCH</font> correctly (<font SIZE="-1">RT</font> #8438) (7c7501)</dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</p>
<dd> The implementation of <i>sv_dup_inc()</i> has changed from a macro to a function.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;find_rundefsvoffset&quot;</tt> function has been deprecated. It appeared that its design was insufficient to reliably get the lexical <tt>$_</tt> at run-time. </p>
<p> Use the new <tt>&quot;find_rundefsv&quot;</tt> function or the <tt>&quot;UNDERBAR&quot;</tt> macro instead. They directly return the right <font SIZE="-1">SV</font> representing <tt>$_</tt>, whether it&#8217;s lexical or dynamic (789bd8 .. 03d5bc).</p>
<dt>&bull;</p>
<dd> The following new functions or macros have been added to the public <font SIZE="-1">API:</font> <tt>&quot;SvNV_nomg&quot;</tt>, <tt>&quot;sv_2nv_flags&quot;</tt>, <tt>&quot;find_rundefsv&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;UNDERBAR&quot;</tt> macro now calls <tt>&quot;find_rundefsv&quot;</tt>. <tt>&quot;dUNDERBAR&quot;</tt> is now a noop but should still be used to ensure past and future compatibility.</p>
<dt>&bull;</p>
<dd> The ibcmp_* functions have been renamed and are now called foldEQ, foldEQ_locale and foldEQ_utf8 (e6226b).</dl>
<h2>Deprecations</h2>
<p> The following items are now deprecated.</p>
<dl>
<dt>&bull;</p>
<dd> Omitting a space between a regex pattern or pattern modifiers and the following word is deprecated. For example, <tt>&quot;m/foo/sand $bar&quot;</tt> will still be parsed as <tt>&quot;m/foo/s and $bar&quot;</tt> but will issue a warning.</dl>
<h2>Platform Specific Notes</h2>
<h3>Recent OpenBSDs now use perl&#8217;s malloc</h3>
<p> OpenBSD &gt; 3.7 has a new malloc implementation which is mmap based and as such can release memory back to the <font SIZE="-1">OS</font>; however for perl using this malloc causes a substantial slowdown so we now default to using perl&#8217;s malloc instead (<font SIZE="-1">RT</font> #75742) (9b58b5).</p>
<h2>Acknowledgements</h2>
<p> Perl 5.13.2 represents thirty days of development since Perl 5.13.1 (and two days of waiting around while the release manager remembered where he left his brain) and contains 3685 lines of changes across 194 files from 30 authors and committers. </p>
<p> Thank you to the following for contributing to this release: </p>
<p> Abigail, Andreas J. Koenig, Chas. Owens, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, David Caldwell, David Golden, David Mitchell, Father Chrysostomos, George Greer, H.Merijn Brand, Jerry D. Hedden, Karl Williamson, Maik Hentsche, Matt S Trout, Nicholas Clark, Rafael Garcia-Suarez, Ricardo Signes, Salvador Fandino, Salvador Ortiz Garcia, Shlomi Fish, Sinan Unur, Sisyphus, Slaven Rezic, Sullivan Beck, Tony Cook, Vincent Pit, Zefram, brian d foy, var Arnfjo.rd<i>&#8211;</i> Bjarmason </p>
<p> Your humble release manager would like to specifically call out Karl Williamson for making the tests a better place to be, and Shlomi Fish for a passel of tiny incremental docfixes of the sort that don&#8217;t get made often enough.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAO">Changes to Existing Documentation</a></p>
<dd>
<dt><a href="#lbAV">Performance Enhancements</a></p>
<dd>
<dt><a href="#lbBA">Installation and Configuration Improvements</a></p>
<dd>
<dt><a href="#lbBC">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbBD">Changed Internals</a></p>
<dd>
<dt><a href="#lbBE">Deprecations</a></p>
<dd>
<dt><a href="#lbBF">Platform Specific Notes</a></p>
<dd>
<dt><a href="#lbBH">Acknowledgements</a></p>
<dd>
<dt><a href="#lbBI">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBJ">SEE ALSO</a></p>
<dd></dl>
