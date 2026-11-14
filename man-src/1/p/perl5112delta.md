---
title: "perl5112delta(1)"
name: "perl5112delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5112delta/"
description: "perl5112delta – what is new for perl v5.11.2"
---

<h2 class="name">NAME</h2>
<p> perl5112delta &#8211; what is new for perl v5.11.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.11.1 release and the 5.11.2 release.</p>
<h2>Core Enhancements</h2>
<h3>qr overloading</h3>
<p> It is now possible to overload the <tt>&quot;qr//&quot;</tt> operator, that is, conversion to regexp, like it was already possible to overload conversion to boolean, string or number of objects. It is invoked when an object appears on the right hand side of the <tt>&quot;=~&quot;</tt> operator, or when it is interpolated into a regexp. See overload.</p>
<h3>Pluggable keywords</h3>
<p> Extension modules can now cleanly hook into the Perl parser to define new kinds of keyword-headed expression and compound statement. The syntax following the keyword is defined entirely by the extension. This allow a completely non-Perl sublanguage to be parsed inline, with the right ops cleanly generated. This feature is currently considered experimental. </p>
<p> See &#8220;PL_keyword_plugin&#8221; in perlapi for the mechanism. The Perl core source distribution also includes a new module XS::APItest::KeywordRPN, which implements reverse Polish notation arithmetic via pluggable keywords. This module is mainly used for test purposes, and is not normally installed, but also serves as an example of how to use the new mechanism.</p>
<h3>APIs for more internals</h3>
<p> The lowest layers of the lexer and parts of the pad system now have C APIs available to <font SIZE="-1">XS</font> extensions. These are necessary to support proper use of pluggable keywords, but have other uses too. The new APIs are experimental, and only cover a small proportion of what would be necessary to take full advantage of the core&#8217;s facilities in these areas. It is intended that the Perl 5.13 development cycle will see the addition of a full range of clean, supported interfaces.</p>
<h3>Overridable function lookup</h3>
<p> Where an extension module hooks the creation of rv2cv ops to modify the subroutine lookup process, this now works correctly for bareword subroutine calls. This means that prototypes on subroutines referenced this way will be processed correctly. (Previously bareword subroutine names were initially looked up, for parsing purposes, by an unhookable mechanism, so extensions could only properly influence subroutine names that appeared with an <tt>&quot;&amp;&quot;</tt> sigil.)</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&quot;legacy&quot;</p>
<dd> Preserves legacy behaviors or enable new non-default behaviors. Currently the only behaviour concerns semantics for the 128 characters on <font SIZE="-1">ASCII</font> systems that have the 8th bit set.</dl>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;diagnostics&quot;</p>
<dd> Supports %.0f formatting internally.</p>
<dt>&quot;overload&quot;</p>
<dd> Allow overloading of &#8216;qr&#8217;.</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;B::Concise&quot;</p>
<dd> Optimize reversing an array in-place, avoid using defined <tt>%hash</tt> in core code and tests.</p>
<dt>&quot;B::Deparse&quot;</p>
<dd> Teach B::Deparse about in-place reverse.</p>
<dt>&quot;Carp&quot;</p>
<dd> Refine Carp <i>caller()</i> fix and add tests.</p>
<dt>&quot;Compress::Zlib&quot;</p>
<dd> Updated to 2.022.</p>
<dt>&quot;CPANPLUS&quot;</p>
<dd> Updated to 0.89_09.</p>
<dt>&quot;Encode&quot;</p>
<dd> Updated to 2.38.</p>
<dt>&quot;ExtUtils::CBuilder&quot;</p>
<dd> Updated to 0.27.</p>
<dt>&quot;Env&quot;</p>
<dd> Add <font SIZE="-1">EXISTS</font> and <font SIZE="-1">DELETE</font> methods to Env.pm.</p>
<dt>&quot;File::Fetch&quot;</p>
<dd> Updated to 0.22.</p>
<dt>&quot;I8N::Langinfo&quot;</p>
<dd> Correctly document export of I18N::Langinfo.</p>
<dt>&quot;I8N::LangTags&quot;</p>
<dd> In I18N::LangTags::Detect, avoid using defined <tt>@array</tt> and defined <tt>%hash</tt>.</p>
<dt>&quot;IO::Compress&quot;</p>
<dd> Updated to 2.022.</p>
<dt>&quot;IPC::Cmd&quot;</p>
<dd> Updated to 0.54.</p>
<dt>&quot;List::Util&quot;</p>
<dd> Updated to 1.22.</p>
<dt>&quot;Locale::Maketext&quot;</p>
<dd> In Locale::Maketext, avoid using defined <tt>@array</tt> and defined <tt>%hash</tt>. Convert the odd Locale::Maketext test out from Test to Test::More.</p>
<dt>&quot;Module::Build&quot;</p>
<dd> Updated to 0.35_08.</p>
<dt>&quot;Module::CoreList&quot;</p>
<dd> Implemented <i>is_deprecated()</i>.</p>
<dt>&quot;Pod::Simple&quot;</p>
<dd> Updated to 3.10.</p>
<dt>&quot;Scalar::Util&quot;</p>
<dd> Updated to 1.22.</p>
<dt>&quot;Switch&quot;</p>
<dd> Updated to 2.16.</dl>
<h2>Utility Changes</h2>
<dl>
<dt><i>a2p</i></p>
<dd> Fixed bugs with the <i>match()</i> operator in list context, remove mention of $[.</dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> Reversing an array to itself (as in <tt>&quot;@a = reverse @a&quot;</tt>) in void context now happens in-place and is several orders of magnitude faster than it used to be. It will also preserve non-existent elements whenever possible, i.e. for non magical arrays or tied arrays with <tt>&quot;EXISTS&quot;</tt> and <tt>&quot;DELETE&quot;</tt> methods.</dl>
<h2>New or Changed Diagnostics</h2>
<p> Several new diagnostics, see perldiag for details.</p>
<dl>
<dt>&quot;Bad plugin affecting keyword &#8216;%s&#8217;&quot;</p>
<dd>
<dt>&quot;gmtime(%.0f) too large&quot;</p>
<dd>
<dt>&quot;Lexing code attempted to stuff non-Latin-1 character into Latin-1 input&quot;</p>
<dd>
<dt>&quot;Lexing code internal error (%s)&quot;</p>
<dd>
<dt>&quot;localtime(%.0f) too large&quot;</p>
<dd>
<dt>&quot;Overloaded dereference did not return a reference&quot;</p>
<dd>
<dt>&quot;Overloaded qr did not return a REGEXP&quot;</p>
<dd>
<dt>&quot;Perl_pmflag() is deprecated, and will be removed from the XS API&quot;</p>
<dd></dl>
<p> One diagnostic has been removed:</p>
<dl>
<dt>&quot;Runaway format&quot;</p>
<dd></dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Perl_pmflag&quot;</tt> has been removed from the public <font SIZE="-1">API</font>. Calling it now generates a deprecation warning, and it will be removed in a future release. Although listed as part of the <font SIZE="-1">API</font>, it was never documented, and only ever used in <i>toke.c</i>, and prior to 5.10, <i>regcomp.c</i>. In core, it has been replaced by a static function.</dl>
<h2>New Tests</h2>
<dl>
<dt><i>t/op/while_readdir.t</i></p>
<dd> Test that a bare readdir in while loop sets <tt>$_</tt>.</dl>
<h2>Known Problems</h2>
<dl>
<dt>Known test failures on <font SIZE="-1">VMS</font></p>
<dd> Perl 5.11.2 fails a small set of core and <font SIZE="-1">CPAN</font> tests as of this release. With luck, that&#8217;ll be sorted out for 5.11.3.</dl>
<h2>Deprecations</h2>
<p> The following items are now deprecated.</p>
<h3>Use of := to mean an empty attribute list is now deprecated.</h3>
<p> An accident of Perl&#8217;s parser meant that these constructions were all equivalent: </p>
<pre>
    my $pi := 4;
    my $pi : = 4;
    my $pi :  = 4;
</pre>
<p> with the <tt>&quot;:&quot;</tt> being treated as the start of an attribute list, which ends before the <tt>&quot;=&quot;</tt>. As whitespace is not significant here, all are parsed as an empty attribute list, hence all the above are equivalent to, and better written as </p>
<pre>
    my $pi = 4;
</pre>
<p> because no attribute processing is done for an empty list. </p>
<p> As is, this meant that <tt>&quot;:=&quot;</tt> cannot be used as a new token, without silently changing the meaning of existing code. Hence that particular form is now deprecated, and will become a syntax error. If it is absolutely necessary to have empty attribute lists (for example, because of a code generator) then avoid the warning by adding a space before the <tt>&quot;=&quot;</tt>.</p>
<h2>Acknowledgements</h2>
<p> Perl 5.11.2 represents approximately 3 weeks development since Perl 5.11.1 and contains 29,992 lines of changes across 458 files from 38 authors and committers: </p>
<p> Abhijit Menon-Sen, Abigail, Ben Morrow, Bo Borgerson, Brad Gilbert, Bram, Chris Williams, Craig A. Berry, Daniel Frederick Crisman, Dave Rolsky, David E. Wheeler, David Golden, Eric Brine, Father Chrysostomos, Frank Wiegand, Gerard Goossen, Gisle Aas, Graham Barr, Harmen, H.Merijn Brand, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Karl Williamson, Kevin Ryde, Leon Brocard, Nicholas Clark, Paul Marquess, Philippe Bruhat, Rafael Garcia-Suarez, Sisyphus, Steffen Mueller, Steve Hay, Steve Peters, Vincent Pit, Yuval Kogman, Yves Orton, and Zefram. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.</p>
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
