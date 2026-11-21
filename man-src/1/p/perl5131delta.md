---
title: "perl5131delta(1)"
name: "perl5131delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5131delta/"
description: "perl5131delta – what is new for perl v5.13.1"
---

<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.0 release and the 5.13.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.10, first read perl5120delta, which describes differences between 5.10 and 5.12.</p>
<h2>Incompatible Changes</h2>
<h3>
</h2>
  <i></i><h3>\c X</h3>
<p> The backslash-c construct was designed as a way of specifying non-printable characters, but there were no restrictions (on <font SIZE="-1">ASCII</font> platforms) on what the character following the <code>&quot;c&quot;</code> could be. Now, that character must be one of the <font SIZE="-1">ASCII</font> characters.  </p>
<h3>localised tied hashes, arrays and scalars are no longed tied</h3>
<p> In the following: </p>
<pre><code>    tie @a, ...;
    {
        local @a;
        # here, @a is a now a new, untied array
    }
    # here, @a refers again to the old, tied array
</code></pre>
<p> The new local array used to be made tied too, which was fairly pointless, and has now been fixed. This fix could however potentially cause a change in behaviour of some code.  </p>
<h3>given return values</h3>
<p> Starting from this release, <code>&quot;given&quot;</code> blocks returns the last evaluated expression, or an empty list if the block was exited by <code>&quot;break&quot;</code>. Thus you can now write: </p>
<pre><code>    my $type = do {
     given ($num) {
      break when undef;
      'integer' when /^[+-]?[0-9]+$/;
      'float' when /^[+-]?[0-9]+(?:\.[0-9]+)?$/;
      'unknown';
     }
    };
</code></pre>
<p> See ``Return value&#8217;&#8216; in perlsyn for details.  </p>
<h2>Core Enhancements</h2>
<h3>Exception Handling Reliability</h3>
<p> Several changes have been made to the way <code>&quot;die&quot;</code>, <code>&quot;warn&quot;</code>, and <code>$@</code> behave, in order to make them more reliable and consistent. </p>
<p> When an exception is thrown inside an <code>&quot;eval&quot;</code>, the exception is no longer at risk of being clobbered by code running during unwinding (e.g., destructors). Previously, the exception was written into <code>$@</code> early in the throwing process, and would be overwritten if <code>&quot;eval&quot;</code> was used internally in the destructor for an object that had to be freed while exiting from the outer <code>&quot;eval&quot;</code>. Now the exception is written into <code>$@</code> last thing before exiting the outer <code>&quot;eval&quot;</code>, so the code running immediately thereafter can rely on the value in <code>$@</code> correctly corresponding to that <code>&quot;eval&quot;</code>. </p>
<p> Likewise, a <code>&quot;local $@&quot;</code> inside an <code>&quot;eval&quot;</code> will no longer clobber any exception thrown in its scope. Previously, the restoration of <code>$@</code> upon unwinding would overwrite any exception being thrown. Now the exception gets to the <code>&quot;eval&quot;</code> anyway. So <code>&quot;local $@&quot;</code> is safe inside an <code>&quot;eval&quot;</code>, albeit of rather limited use. </p>
<p> Exceptions thrown from object destructors no longer modify the <code>$@</code> of the surrounding context. (If the surrounding context was exception unwinding, this used to be another way to clobber the exception being thrown. Due to the above change it no longer has that significance, but there are other situations where <code>$@</code> is significant.) Previously such an exception was sometimes emitted as a warning, and then either string-appended to the surrounding <code>$@</code> or completely replaced the surrounding <code>$@</code>, depending on whether that exception and the surrounding <code>$@</code> were strings or objects. Now, an exception in this situation is always emitted as a warning, leaving the surrounding <code>$@</code> untouched. In addition to object destructors, this also affects any function call performed by <font SIZE="-1">XS</font> code using the <code>&quot;G_KEEPERR&quot;</code> flag. </p>
<p> <code>$@</code> is also no longer used as an internal temporary variable when preparing to <code>&quot;die&quot;</code>. Previously it was internally necessary to put any exception object (any non-string exception) into <code>$@</code> first, before it could be used as an exception. (The C <font SIZE="-1">API</font> still offers the old option, so an <font SIZE="-1">XS</font> module might still clobber <code>$@</code> in the old way.) This change together with the foregoing means that, in various places, <code>$@</code> may be observed to contain its previously-assigned value, rather than having been overwritten by recent exception-related activity. </p>
<p> Warnings for <code>&quot;warn&quot;</code> can now be objects, in the same way as exceptions for <code>&quot;die&quot;</code>. If an object-based warning gets the default handling, of writing to standard error, it will of course still be stringified along the way. But a <code>$SIG{__WARN__}</code> handler will now receive an object-based warning as an object, where previously it was passed the result of stringifying the object.  </p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Errno&quot;</dt>
<dd> <p> The implementation of <code>&quot;Errno&quot;</code> has been refactored to use about 55% less memory. There should be no user-visible changes. </p>
 </dd>
<dt>Perl 4 &quot;.pl&quot; libraries</dt>
<dd> <p> These historical libraries have been minimally modified to avoid using <code>$[</code>. This is to prepare them for the deprecation of <code>$[</code>. </p>
 </dd>
<dt>&quot;B::Deparse&quot;</dt>
<dd> <p> A bug has been fixed when deparsing a nextstate op that has both a change of package (relative to the previous nextstate), or a change of <code>&quot;%^H&quot;</code> or other state, and a label. Previously the label was emitted first, leading to syntactically invalid output because a label is not permitted immediately before a package declaration, <font SIZE="-1"><code>BEGIN</code></font> block, or some other things. Now the label is emitted last. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<p> The following modules have been removed from the core distribution, and if needed should be installed from <font SIZE="-1">CPAN</font> instead. </p>
<dl>
<dt>&quot;Class::ISA&quot;</dt>
<dd>  </dd>
<dt>&quot;Pod::Plainer&quot;</dt>
<dd>  </dd>
<dt>&quot;Switch&quot;</dt>
<dd>  </dd></dl>
<p> The removal of <code>&quot;Shell&quot;</code> has been deferred until after 5.14, as the implementation of <code>&quot;Shell&quot;</code> shipped with 5.12.0 did not correctly issue the warning that it was to be removed from core.  </p>
<h2>New Documentation</h2>
<dl>
<dt>perlgpl</dt>
<dd> <p> perlgpl has been updated to contain <font SIZE="-1">GPL</font> version 1, as is included in the <i></i><font SIZE="-1"><i>README</i></font><i></i> distributed with perl. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Naming a deprecated character in \N{...} will not leak memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">FETCH</font> is no longer called needlessly on some tied variables. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The trie runtime code should no longer allocate massive amounts of memory, fixing #74484. </p>
 </dd></dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The protocol for unwinding the C stack at the last stage of a <code>&quot;die&quot;</code> has changed how it identifies the target stack frame. This now uses a separate variable <code>&quot;PL_restartjmpenv&quot;</code>, where previously it relied on the <code>&quot;blk_eval.cur_top_env&quot;</code> pointer in the <code>&quot;eval&quot;</code> context frame that has nominally just been discarded. This change means that code running during various stages of Perl-level unwinding no longer needs to take care to avoid destroying the ghost frame. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The format of entries on the scope stack has been changed, resulting in a reduction of memory usage of about 10%. In particular, the memory used by the scope stack to record each active lexical variable has been halved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Memory allocation for pointer tables has been changed. Previously <code>&quot;Perl_ptr_table_store&quot;</code> allocated memory from the same arena system as <code>&quot;SV&quot;</code> bodies and <code>&quot;HE&quot;</code>s, with freed memory remaining bound to those arenas until interpreter exit. Now it allocates memory from arenas private to the specific pointer table, and that memory is returned to the system when <code>&quot;Perl_ptr_table_free&quot;</code> is called. Additionally, allocation and release are both less <font SIZE="-1">CPU</font> intensive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function, Perl_magic_methcall has been added that wraps the setup needed to call a magic method like <font SIZE="-1">FETCH</font> (the existing S_magic_methcall function has been renamed S_magic_methcall1). </p>
 </dd></dl>
<h2>Deprecations</h2>
<p> The following items are now deprecated. </p>
<dl>
<dt>&quot;Perl_ptr_table_clear&quot;</dt>
<dd> <p> <code>&quot;Perl_ptr_table_clear&quot;</code> is no longer part of Perl&#8217;s public <font SIZE="-1">API</font>. Calling it now generates a deprecation warning, and it will be removed in a future release. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.1 represents thirty days of development since Perl 5.13.0 and contains 15390 lines of changes across 289 files from 34 authors and committers. </p>
<p> Thank you to the following for contributing to this release: </p>
<p> var Arnfjo.rd <i>-</i> Bjarmason, Arkturuz, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Curtis Jewell, Dan Dascalescu, David Golden, David Mitchell, Father Chrysostomos, Gene Sullivan, gfx, Gisle Aas, H.Merijn Brand, James E Keenan, James Mastros, Jan Dubois, Jesse Vincent, Karl Williamson, Leon Brocard, Lubomir Rintel (GoodData), Nicholas Clark, Philippe Bruhat (BooK), Rafael Garcia-Suarez, Rainer Tammer, Ricardo Signes, Richard Soderberg, Robin Barker, Ruslan Zakirov, Steffen Mueller, Todd Rinaldo, Tony Cook, Vincent Pit, Zefram  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
