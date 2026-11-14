---
title: "perl5114delta(1)"
name: "perl5114delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5114delta/"
description: "perl5114delta – what is new for perl v5.11.4"
---

<h2 class="name">NAME</h2>
<p> perl5114delta &#8211; what is new for perl v5.11.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.11.3 release and the 5.11.4 release. </p>
<p> If you are upgrading from an earlier release such as 5.11.2, first read perl5113delta, which describes differences between 5.11.2 and 5.11.3.</p>
<h2>Incompatible Changes</h2>
<h3>Version number formats</h3>
<p> Acceptable version number formats have been formalized into &#8220;strict&#8221; and &#8220;lax&#8221; rules. <tt>&quot;package NAME VERSION&quot;</tt> takes a strict version number. <tt>&quot;use NAME VERSION&quot;</tt> takes a lax version number. <tt>&quot;UNIVERSAL::VERSION&quot;</tt> and the version object constructors take lax version numbers. Providing an invalid version will result in a fatal error. </p>
<p> These formats will be documented fully in the version module in a subsequent release of Perl 5.11. To a first approximation, a &#8220;strict&#8221; version number is a positive decimal number (integer or decimal-fraction) without exponentiation or else a dotted-decimal v-string with a leading &#8216;v&#8217; character and at least three components. A &#8220;lax&#8221; version number allows v-strings with fewer than three components or without a leading &#8216;v&#8217;. Under &#8220;lax&#8221; rules, both decimal and dotted-decimal versions may have a trailing &#8220;alpha&#8221; component separated by an underscore character after a fractional or dotted-decimal component. </p>
<p> The version module adds <tt>&quot;version::is_strict&quot;</tt> and <tt>&quot;version::is_lax&quot;</tt> functions to check a scalar against these rules.</p>
<h2>Core Enhancements</h2>
<h3>Unicode properties</h3>
<p> <tt>&quot;\p{XDigit}&quot;</tt> now matches the same characters as <tt>&quot;\p{Hex_Digit}&quot;</tt>. This means that in addition to the characters it currently matches, <tt>&quot;[A-Fa-f0-9]&quot;</tt>, it will also match their fullwidth equivalent forms, for example U+FF10: <font SIZE="-1">FULLWIDTH</font> <font SIZE="-1">DIGIT</font> <font SIZE="-1">ZERO</font>.</p>
<h2>Modules and Pragmata</h2>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;less&quot;</p>
<dd> Upgraded from version 0.02 to 0.03. </p>
<p> This version introduces the <tt>&quot;stash_name&quot;</tt> method to allow subclasses of less to pick where in %^H to store their stash.</p>
<dt>&quot;version&quot;</p>
<dd> Upgraded from version 0.77 to 0.81. </p>
<p> This version adds support for &#8220;Version number formats&#8221; as described earlier in this document and in its own documentation.</p>
<dt>&quot;warnings&quot;</p>
<dd> Upgraded from version 1.08 to 1.09. </p>
<p> This version adds the <tt>&quot;illegalproto&quot;</tt> warning category. See also &#8220;New or Changed Diagnostics&#8221; for this change.</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Archive::Extract&quot;</p>
<dd> Upgraded from version 0.36 to 0.38.</p>
<dt>&quot;B::Deparse&quot;</p>
<dd> Upgraded from version 0.93 to 0.94.</p>
<dt>&quot;Compress::Raw::Bzip2&quot;</p>
<dd> Upgraded from version 2.021 to 2.024.</p>
<dt>&quot;Compress::Raw::Zlib&quot;</p>
<dd> Upgraded from version 2.021 to 2.024.</p>
<dt>&quot;CPAN&quot;</p>
<dd> Upgraded from version 1.94_5301 to 1.94_54.</p>
<dt>&quot;File::Fetch&quot;</p>
<dd> Upgraded from version 0.22 to 0.24.</p>
<dt>&quot;Module::Build&quot;</p>
<dd> Upgraded from version 0.36 to 0.3603.</p>
<dt>&quot;Safe&quot;</p>
<dd> Upgraded from version 2.20 to 2.21. </p>
<p> Anonymous coderefs created in Safe containers no longer get bogus arguments passed to them, fixing <font SIZE="-1">RT</font> #72068.</dl>
<h3>Removed Modules and Pragmata</h3>
<dl>
<dt>&quot;Devel::DProf::V&quot;</p>
<dd> Removed from the Perl core. Prior version was &#8216;undef&#8217;.</dl>
<h2>Changes to Existing Documentation</h2>
<p> A significant fraction of the core documentation has been updated to clarify the behavior of Perl&#8217;s Unicode handling. </p>
<p> Much of the remaining core documentation has been reviewed and edited for clarity, consistent use of language, and to fix the spelling of Tom Christiansen&#8217;s name.</p>
<h3>Configuration improvements</h3>
<p> <font SIZE="-1">USE_ATTRIBUTES_FOR_PERLIO</font> is now reported in the compile-time options listed by the <tt>&quot;-V&quot;</tt> switch.</p>
<h3>Platform Specific Changes</h3>
<dl>
<dt><font SIZE="-1">VMS</font></p>
<dd> The default pipe buffer size on <font SIZE="-1">VMS</font> has been updated to 8192 on 64-bit systems.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Tie::Hash::NamedCapture::* shouldn&#8217;t abort if passed bad input (<font SIZE="-1">RT</font> #71828)</p>
<dt>&bull;</p>
<dd> <tt>@_</tt> and <tt>$_</tt> no longer leak under threads (<font SIZE="-1">RT</font> #34342 and #41138, also #70602, #70974)</dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>New warning category &quot;illegalproto&quot;</p>
<dd> The two warnings : </p>
<pre>
  Illegal character in prototype for %s : %s
  Prototype after '%c' for %s : %s
</pre>
<p> have been moved from the <tt>&quot;syntax&quot;</tt> top-level warnings category into a new first-level category, <tt>&quot;illegalproto&quot;</tt>. These two warnings are currently the only ones emitted during parsing of an invalid/illegal prototype, so one can now do </p>
<pre>
  no warnings 'illegalproto';
</pre>
<p> to suppress only those, but not other syntax-related warnings. Warnings where prototypes are changed, ignored, or not met are still in the <tt>&quot;prototype&quot;</tt> category as before. (Matt S. Trout)</p>
<dt>lvalue attribute ignored after the subroutine has been defined</p>
<dd> This new warning is issued when one attempts to mark a subroutine as lvalue after it has been defined.</dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</p>
<dd> Perl_magic_setmglob now knows about globs, fixing <font SIZE="-1">RT</font> #71254.</dl>
<h2>Known Problems</h2>
<p> Perl 5.11.4 is a development release leading up to Perl 5.12.0. Some notable known problems found in 5.11.4 are listed as dependencies of <font SIZE="-1">RT</font> #69710, the Perl 5 version 12 meta-ticket.</p>
<h2>Deprecations</h2>
<p> The following items are now deprecated.</p>
<dl>
<dt>&quot;UNIVERSAL-&gt;import()&quot;</p>
<dd> The method <tt>&quot;UNIVERSAL-&gt;import()&quot;</tt> is now deprecated. Attempting to pass import arguments to a <tt>&quot;use UNIVERSAL&quot;</tt> statement will result in a deprecation warning. (This is a less noisy version of the full deprecation warning added in 5.11.0.)</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.11.4 represents approximately one month of development since Perl 5.11.3 and contains 17682 lines of changes across 318 files from 40 authors and committers: </p>
<p> Abigail, Andy Dougherty, brian d foy, Chris Williams, Craig A. Berry, David Golden, David Mitchell, Father Chrysostomos, Gerard Goossen, H.Merijn Brand, Jesse Vincent, Jim Cromie, Josh ben Jore, Karl Williamson, kmx, Matt S Trout, Nicholas Clark, Niko Tyni, Paul Marquess, Philip Hazel, Rafael Garcia-Suarez, Rainer Tammer, Reini Urban, Ricardo Signes, Shlomi Fish, Tim Bunce, Todd Rinaldo, Tom Christiansen, Tony Cook, Vincent Pit, and Zefram </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at &lt;<a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a>&gt;. There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analyzed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
