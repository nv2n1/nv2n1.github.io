---
title: "perl5134delta(1)"
name: "perl5134delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5134delta/"
description: "perl5134delta – what is new for perl v5.13.4"
---

<h2 class="name">NAME</h2>
<p> perl5134delta &#8211; what is new for perl v5.13.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.4 release and the 5.13.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.2, first read perl5133delta, which describes differences between 5.13.2 and 5.13.3.</p>
<h2>Core Enhancements</h2>
<h3>srand() now returns the seed</h3>
<p> This allows programs that need to have repeatable results to not have to come up with their own seed generating mechanism. Instead, they can use <tt>&quot;srand()&quot;</tt> and somehow stash the return for future use. Typical is a test program which has too many combinations to test comprehensively in the time available to it each run. It can test a random subset each time, and should there be a failure, log the seed used for that run so that it can later be used to reproduce the exact results.</p>
<h3>\N{<i>name</i>} and charnames enhancements</h3>
<p> <tt>&quot;\N{}&quot;</tt>, <tt>&quot;charnames::vianame&quot;</tt>, <tt>&quot;charnames::viacode&quot;</tt> now know about every character in Unicode. Previously, they didn&#8217;t know about the Hangul syllables nor a number of <font SIZE="-1">CJK</font> (Chinese/Japanese/Korean) characters.</p>
<h2>Incompatible Changes</h2>
<h3>Declare <font SIZE="-1">API</font> incompatibility between blead releases</h3>
<p> Only stable releases (5.10.x, 5.12.x, 5.14.x, &#8230;) guarantee binary compatibility with each other, while blead releases (5.13.x, 5.15.x, &#8230;) often break this compatibility. However, prior to perl 5.13.4, all blead releases had the same <tt>&quot;PERL_API_REVISION&quot;</tt>, <tt>&quot;PERL_API_VERSION&quot;</tt>, and <tt>&quot;PERL_API_SUBVERSION&quot;</tt>, effectively declaring them as binary compatible, which they weren&#8217;t. From now on, blead releases will have a <tt>&quot;PERL_API_SUBVERSION&quot;</tt> equal to their <tt>&quot;PERL_SUBVERSION&quot;</tt>, explicitly marking them as incompatible with each other. </p>
<p> Maintenance releases of stable perl versions will continue to make no intentionally incompatible <font SIZE="-1">API</font> changes.</p>
<h3>Check <font SIZE="-1">API</font> compatibility when loading <font SIZE="-1">XS</font> modules</h3>
<p> When perl&#8217;s <font SIZE="-1">API</font> changes in incompatible ways (which usually happens between every major release), <font SIZE="-1">XS</font> modules compiled for previous versions of perl will not work anymore. They will need to be recompiled against the new perl. </p>
<p> In order to ensure that modules are recompiled, and to prevent users from accidentally loading modules compiled for old perls into newer ones, the <tt>&quot;XS_APIVERSION_BOOTCHECK&quot;</tt> macro has been added. That macro, which is called when loading every newly compiled extension, compares the <font SIZE="-1">API</font> version of the running perl with the version a module has been compiled for and raises an exception if they don&#8217;t match.</p>
<h3>Binary Incompatible with all previous Perls</h3>
<p> Some bit fields have been reordered; therefore, this release will not be binary compatible with any previous Perl release.</p>
<h3>Change in the parsing of certain prototypes</h3>
<p> Functions declared with the following prototypes now behave correctly as unary functions:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;*&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;\sigil&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;\[...]&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;;$&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;;*&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;;\sigil&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;;\[...]&quot;</tt></dl>
<p> Due to this bug fix, functions using the <tt>&quot;(*)&quot;</tt>, <tt>&quot;(;$)&quot;</tt> and <tt>&quot;(;*)&quot;</tt> prototypes are parsed with higher precedence than before. So in the following example: </p>
<pre><code>
sub foo($);
foo $a &lt; $b;
</code></pre>
<p> the second line is now parsed correctly as <tt>&quot;foo($a) &lt; $b&quot;</tt>, rather than <tt>&quot;foo($a &lt; $b)&quot;</tt>. This happens when one of these operators is used in an unparenthesised argument: </p>
<pre><code>
  &lt; &gt; &lt;= &gt;= lt gt le ge
  == != &lt;=&gt; eq ne cmp ~~
  &amp;
  | ^
  &amp;&amp;
  || //
  .. ...
  ?:
  = += -= *= etc.
</code></pre>
<h2>Deprecations</h2>
<h3>List assignment to $[</h3>
<p> After assignment to <tt>$[</tt> has been deprecated and started to give warnings in perl version 5.12.0, this version of perl also starts to emit a warning when assigning to <tt>$[</tt> in list context. This fixes an oversight in 5.12.0.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> Make string appending 100 times faster </p>
<p> When doing a lot of string appending, perl could end up allocating a lot more memory than needed in a very inefficient way, if perl was configured to use the system&#8217;s <tt>&quot;malloc&quot;</tt> implementation instead of its own. </p>
<p> <tt>&quot;sv_grow&quot;</tt>, which is what&#8217;s being used to allocate more memory if necessary when appending to a string, has now been taught how to round up the memory it requests to a certain geometric progression, making it much faster on certain platforms and configurations. On Win32, it&#8217;s now about 100 times faster.</p>
<dt>&bull;</p>
<dd> For weak references, the common case of just a single weak reference per referent has been optimised to reduce the storage required. In this case it saves the equivalent of one small perl array per referent.</p>
<dt>&bull;</p>
<dd> <tt>&quot;XPV&quot;</tt>, <tt>&quot;XPVIV&quot;</tt>, and <tt>&quot;XPVNV&quot;</tt> now only allocate the parts of the <tt>&quot;SV&quot;</tt> body they actually use, saving some space.</dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> This release does not introduce any new modules or pragmata.</p>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&quot;Archive::Tar&quot;</p>
<dd> Upgraded from version 1.64 to 1.68. </p>
<p> Among other things, the new version adds a new option to <tt>&quot;ptar&quot;</tt> to allow safe creation of tarballs without world-writable files on Windows, allowing those archives to be uploaded to <font SIZE="-1">CPAN</font>.</p>
<dt>&quot;B::Lint&quot;</p>
<dd> Upgraded from version 1.11 to 1.12.</p>
<dt>&quot;Carp&quot;</p>
<dd> Upgraded from version 1.16 to 1.18. </p>
<p> Carp now detects incomplete <i>caller()</i> overrides and avoids using bogus <tt>@DB::args</tt>. To provide backtraces, Carp relies on particular behaviour of the caller built-in. Carp now detects if other code has overridden this with an incomplete implementation, and modifies its backtrace accordingly. Previously incomplete overrides would cause incorrect values in backtraces (best case), or obscure fatal errors (worst case) </p>
<p> This fixes certain cases of <tt>&quot;Bizarre copy of ARRAY&quot;</tt> caused by modules overriding <tt>&quot;caller()&quot;</tt> incorrectly.</p>
<dt>&quot;Compress::Raw::Bzip2&quot;</p>
<dd> Upgraded from version 2.027 to 2.030.</p>
<dt>&quot;Compress::Raw::Zlib&quot;</p>
<dd> Upgraded from version 2.027 to 2.030.</p>
<dt>&quot;File::Spec&quot;</p>
<dd> Upgraded from version 3.31 to 3.31_01. </p>
<p> Various issues in File::Spec::VMS have been fixed.</p>
<dt>&quot;I18N::Langinfo&quot;</p>
<dd> Upgraded from version 0.03 to 0.04. </p>
<p> <tt>&quot;langinfo()&quot;</tt> now defaults to using <tt>$_</tt> if there is no argument given, just like the documentation always claimed it did.</p>
<dt>&quot;IO::Compress&quot;</p>
<dd> Upgraded from version 2.027 to 2.030.</p>
<dt>&quot;Module::CoreList&quot;</p>
<dd> Upgraded from version 2.36 to 2.37. </p>
<p> Besides listing the updated core modules of this release, it also stops listing the <tt>&quot;Filespec&quot;</tt> module. That module never existed in core. The scripts generating <tt>&quot;Module::CoreList&quot;</tt> confused it with <tt>&quot;VMS::Filespec&quot;</tt>, which actually is a core module, since the time of perl 5.8.7.</p>
<dt>&quot;Test::Harness&quot;</p>
<dd> Upgraded from version 3.21 to 3.22.</p>
<dt>&quot;Test::Simple&quot;</p>
<dd> Upgraded from version 0.94 to 0.96. </p>
<p> Among many other things, subtests without a <tt>&quot;plan&quot;</tt> or <tt>&quot;no_plan&quot;</tt> now have an implicit <tt>&quot;done_testing()&quot;</tt> added to them.</p>
<dt>&quot;Unicode::Collate&quot;</p>
<dd> Upgraded from version 0.53 to 0.56. </p>
<p> Among other things, it is now using <font SIZE="-1">UCA</font> Revision 20 (based on Unicode 5.2.0) and supports a couple of new locales.</p>
<dt>&quot;feature&quot;</p>
<dd> Upgraded from version 1.17 to 1.18.</dl>
<h3>Removed Modules and Pragmata</h3>
<p> This release does not remove any modules or pragmata.</p>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perldiag</i></p>
<dl>
<dt>&bull;</p>
<dd> The following existing diagnostics are now documented:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Ambiguous use of <tt>%c</tt> resolved as operator <tt>%c</tt></p>
<dt>&bull;</p>
<dd> Ambiguous use of <tt>%c</tt>{%s} resolved to <tt>%c</tt>%s</p>
<dt>&bull;</p>
<dd> Ambiguous use of <tt>%c</tt>{%s%s} resolved to <tt>%c</tt>%s%s</p>
<dt>&bull;</p>
<dd> Ambiguous use of -%s resolved as -&amp;%s()</p>
<dt>&bull;</p>
<dd> Invalid strict version format (%s)</p>
<dt>&bull;</p>
<dd> Invalid version format (%s)</p>
<dt>&bull;</p>
<dd> Invalid version object</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>perlport</i></p>
<dl>
<dt>&bull;</p>
<dd> Documented a limitation of <i>alarm()</i> on Win32.</dl>
<p> <i>perlre</i></p>
<dl>
<dt>&bull;</p>
<dd> Minor fix to a multiple scalar match example.</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> Compatibility with <tt>&quot;C++&quot;</tt> compilers has been improved.</p>
<dt>&bull;</p>
<dd> On compilers that support it, <tt>&quot;-Wwrite-strings&quot;</tt> is now added to cflags by default.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> <i>t/op/print.t</i> has been added to test implicit printing of <tt>$_</tt>.</p>
<dt>&bull;</p>
<dd> <i>t/io/errnosig.t</i> has been added to test for restoration of of <tt>$!</tt> when leaving signal handlers.</p>
<dt>&bull;</p>
<dd> <i>t/op/tie_fetch_count.t</i> has been added to see if <tt>&quot;FETCH&quot;</tt> is only called once on tied variables.</p>
<dt>&bull;</p>
<dd> <i>lib/Tie/ExtraHash.t</i> has been added to make sure the, previously untested, Tie::ExtraHash keeps working.</p>
<dt>&bull;</p>
<dd> <i>t/re/overload.t</i> has been added to test against string corruption in pattern matches on overloaded objects. This is a <font SIZE="-1">TODO</font> test.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Win32</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Fixed a possible hang in <i>t/op/readline.t</i>.</p>
<dt>&bull;</p>
<dd> Fixed build process for <font SIZE="-1">SDK2003SP1</font> compilers.</p>
<dt>&bull;</p>
<dd> When using old 32-bit compilers, the define <tt>&quot;_USE_32BIT_TIME_T&quot;</tt> will now be set in <tt>$Config{ccflags}</tt>. This improves portability when compiling <font SIZE="-1">XS</font> extensions using new compilers, but for a perl compiled with old 32-bit compilers.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>Removed &quot;PERL_POLLUTE&quot;</p>
<dd> The option to define <tt>&quot;PERL_POLLUTE&quot;</tt> to expose older 5.005 symbols for backwards compatibility has been removed. It&#8217;s use was always discouraged, and MakeMaker contains a more specific escape hatch: </p>
<pre>
    perl Makefile.PL POLLUTE=1
</pre>
<p> This can be used for modules that have not been upgraded to 5.6 naming conventions (and really should be completely obsolete by now).</p>
<dt>Added &quot;PERL_STATIC_INLINE&quot;</p>
<dd> The <tt>&quot;PERL_STATIC_INLINE&quot;</tt> define has been added to provide the best-guess incantation to use for static inline functions, if the C compiler supports C99-style static inline. If it doesn&#8217;t, it&#8217;ll give a plain <tt>&quot;static&quot;</tt>. </p>
<p> <tt>&quot;HAS_STATIC_INLINE&quot;</tt> can be used to check if the compiler actually supports inline functions.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A possible memory leak when using <i>caller()</i> to set <tt>@DB::args</tt> has been fixed.</p>
<dt>&bull;</p>
<dd> Several memory leaks when loading <font SIZE="-1">XS</font> modules were fixed.</p>
<dt>&bull;</p>
<dd> A panic in the regular expression optimizer has been fixed (RT#75762).</p>
<dt>&bull;</p>
<dd> Assignments to lvalue subroutines now honor copy-on-write behavior again, which has been broken since version 5.10.0 (RT#75656).</p>
<dt>&bull;</p>
<dd> Assignments to glob copies now behave just like assignments to regular globs (RT#1804).</p>
<dt>&bull;</p>
<dd> Within signal handlers, <tt>$!</tt> is now implicitly localized.</p>
<dt>&bull;</p>
<dd> readline now honors <tt>&quot;&lt;&gt;&quot;</tt> overloading on tied arguments.</p>
<dt>&bull;</p>
<dd> <i>substr()</i>, <i>pos()</i>, <i>keys()</i>, and <i>vec()</i> could, when used in combination with lvalues, result in leaking the scalar value they operate on, and cause its destruction to happen too late. This has now been fixed.</p>
<dt>&bull;</p>
<dd> Building with <tt>&quot;PERL_GLOBAL_STRUCT&quot;</tt>, which has been broken accidentally in 5.13.3, now works again.</dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</p>
<dd> The changes in <i>substr()</i> broke <tt>&quot;HTML::Parser&quot;</tt> &lt;= 3.66. A fixed <tt>&quot;HTML::Parser&quot;</tt> is available as version 3.67 on <font SIZE="-1">CPAN</font>.</p>
<dt>&bull;</p>
<dd> The changes in prototype handling break <tt>&quot;Switch&quot;</tt>. A patch has been sent upstream and will hopefully appear on <font SIZE="-1">CPAN</font> soon.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.4 represents approximately one month of development since Perl 5.13.3, and contains 91,200 lines of changes across 436 files from 34 authors and committers. </p>
<p> Thank you to the following for contributing to this release: </p>
<p> Abigail, Andy Armstrong, Andy Dougherty, Chas. Owens, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, David Cantrell, David Golden, David Mitchell, Eric Brine, Father Chrysostomos, Florian Ragwitz, George Greer, Gerard Goossen, H.Merijn Brand, James Mastros, Jan Dubois, Jerry D. Hedden, Joshua ben Jore, Karl Williamson, Lars <font SIZE="-1">DXXXXXX</font> <font SIZE="-1">XXX</font>, Leon Brocard, Lubomir Rintel, Nicholas Clark, Paul Marquess, Rafael Garcia-Suarez, Reini Urban, Robin Barker, Slaven Rezic, Steve Peters, Tony Cook, Wolfram Humann, Zefram</p>
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
<dt><a href="#lbAG">Incompatible Changes</a></p>
<dd>
<dt><a href="#lbAL">Deprecations</a></p>
<dd>
<dt><a href="#lbAN">Performance Enhancements</a></p>
<dd>
<dt><a href="#lbAO">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAS">Documentation</a></p>
<dd>
<dt><a href="#lbAU">Configuration and Compilation</a></p>
<dd>
<dt><a href="#lbAV">Testing</a></p>
<dd>
<dt><a href="#lbAW">Platform Support</a></p>
<dd>
<dt><a href="#lbAY">Internal Changes</a></p>
<dd>
<dt><a href="#lbAZ">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbBA">Known Problems</a></p>
<dd>
<dt><a href="#lbBB">Acknowledgements</a></p>
<dd>
<dt><a href="#lbBC">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBD">SEE ALSO</a></p>
<dd></dl>
