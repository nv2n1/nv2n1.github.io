---
title: "perl5138delta(1)"
name: "perl5138delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5138delta/"
description: "perl5138delta – what is new for perl v5.13.8"
---

<h2 class="name">NAME</h2>
<p> perl5138delta &#8211; what is new for perl v5.13.8 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.7 release and the 5.13.8 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.6, first read perl5137delta, which describes differences between 5.13.6 and 5.13.7.</p>
<h2>Core Enhancements</h2>
<h3>-d:-foo calls Devel::foo::unimport</h3>
<p> The syntax <tt>&quot;-d</tt>:foo<tt>&quot;</tt> was extended in 5.6.1 to make <tt>&quot;-d</tt>:foo=bar<tt>&quot;</tt> equivalent to <tt>&quot;-MDevel::foo=bar&quot;</tt>, which expands internally to <tt>&quot;use Devel::foo 'bar';&quot;</tt>. <i>perl</i> now allows prefixing the module name with <tt>&quot;-&quot;</tt>, with the same semantics as <tt>&quot;-M&quot;</tt>, <i>i.e.</i></p>
<dl>
<dt>&quot;-d:-foo&quot;</p>
<dd> Equivalent to <tt>&quot;-M-Devel::foo&quot;</tt>, expands to <tt>&quot;no Devel::foo;&quot;</tt>, calls <tt>&quot;Devel::foo-&gt;unimport()&quot;</tt> if the method exists.</p>
<dt>&quot;-d:-foo=bar&quot;</p>
<dd> Equivalent to <tt>&quot;-M-Devel::foo=bar&quot;</tt>, expands to <tt>&quot;no Devel::foo 'bar';&quot;</tt>, calls <tt>&quot;Devel::foo-&gt;unimport('bar')&quot;</tt> if the method exists.</dl>
<p> This is particularly useful to suppresses the default actions of a <tt>&quot;Devel::*&quot;</tt> module&#8217;s <tt>&quot;import&quot;</tt> method whilst still loading it for debugging.</p>
<h3>Filehandle method calls load IO::File on demand</h3>
<p> When a method call on a filehandle would die because the method cannot be resolved, and IO::File has not been loaded, Perl now loads IO::File via <tt>&quot;require&quot;</tt> and attempts method resolution again: </p>
<pre><code>
open my $fh, "&gt;", $file;
$fh-&gt;binmode(":raw");
#loads IO::File and succeeds
</code></pre>
<p> This also works for globs like <font SIZE="-1">STDOUT</font>, <font SIZE="-1">STDERR</font> and <font SIZE="-1">STDIN:</font> </p>
<p>STDOUT-&gt;autoflush(1);</p>
<p> Because this on-demand load only happens if method resolution fails, the legacy approach of manually loading an IO::File parent class for partial method support still works as expected: </p>
<p>use IO::Handle;<br />
open my $fh, &#8220;&gt;&#8221;, $file;<br />
$fh-&gt;autoflush(1);<br />
#IO::File not loaded</p>
<h3>Full functionality for use feature &#8216;unicode_strings&#8217;</h3>
<p> This release provides full functionality for <tt>&quot;use feature 'unicode_strings'&quot;</tt>. Under its scope, all string operations executed and regular expressions compiled (even if executed outside its scope) have Unicode semantics. See feature. </p>
<p> This feature avoids most forms of the &#8220;Unicode Bug&#8221; (See &#8220;The &#8221;Unicode Bug&quot;&quot; in perlunicode for details.) If there is a possibility that your code will process Unicode strings, you are <code>strongly</code> encouraged to use this subpragma to avoid nasty surprises. </p>
<p> The availability of this should strongly affect the whole tone of various documents, such as perlunicode and perluniintro, but this work has not been done yet.</p>
<h3>Exception Handling Backcompat Hack</h3>
<p> When an exception is thrown in an <tt>&quot;eval BLOCK&quot;</tt>, <tt>$@</tt> is now set before unwinding, as well as being set after unwinding as the eval block exits. This early setting supports code that has historically treated <tt>$@</tt> during unwinding as an indicator of whether the unwinding was due to an exception. These modules had been broken by 5.13.1&#8217;s change from setting <tt>$@</tt> early to setting it late. This double setting arrangement is a stopgap until the reason for unwinding can be made properly introspectable. <tt>$@</tt> has never been a reliable indicator of the reason for unwinding.</p>
<h3>printf-like functions understand post-1980 size modifiers</h3>
<p> Perl&#8217;s printf and sprintf operators, and Perl&#8217;s internal printf replacement function, now understand the C90 size modifiers &#8220;hh&#8221; (<tt>&quot;char&quot;</tt>), &#8220;z&#8221; (<tt>&quot;size_t&quot;</tt>), and &#8220;t&#8221; (<tt>&quot;ptrdiff_t&quot;</tt>). Also, when compiled with a C99 compiler, Perl now understands the size modifier &#8220;j&#8221; (<tt>&quot;intmax_t&quot;</tt>). </p>
<p> So, for example, on any modern machine, <tt>&quot;sprintf('%hhd', 257)&quot;</tt> returns &#8216;1&#8217;.</p>
<h3>DTrace probes now include package name</h3>
<p> The DTrace probes now include an additional argument (<tt>&quot;arg3&quot;</tt>) which contains the package the subroutine being entered or left was compiled in. </p>
<p> For example using the following DTrace script: </p>
<p>perl$target:: : sub &#8211; entry<br />
{<br />
    printf(&#8220;%s::%s
&#8221;, copyinstr(arg0), copyinstr(arg3));<br />
}</p>
<p> and then running: </p>
<pre>
  perl -e'sub test { }; test'
</pre>
<p> DTrace will print: </p>
<pre>
  main::test
</pre>
<h3>Stacked labels</h3>
<p> Multiple statement labels can now appear before a single statement.</p>
<h2>Incompatible Changes</h2>
<h3>:= is now a syntax error</h3>
<p> Previously <tt>&quot;my $pi := 4;&quot;</tt> was exactly equivalent to <tt>&quot;my $pi : = 4;&quot;</tt>, with the <tt>&quot;:&quot;</tt> being treated as the start of an attribute list, ending before the <tt>&quot;=&quot;</tt>. The use of <tt>&quot;:=&quot;</tt> to mean <tt>&quot;: =&quot;</tt> was deprecated in 5.12.0, and is now a syntax error. This will allow the future use of <tt>&quot;:=&quot;</tt> as a new token. </p>
<p> We find no Perl 5 code on <font SIZE="-1">CPAN</font> using this construction, outside the core&#8217;s tests for it, so we believe that this change will have very little impact on real-world codebases. </p>
<p> If it is absolutely necessary to have empty attribute lists (for example, because of a code generator) then avoid the error by adding a space before the <tt>&quot;=&quot;</tt>.</p>
<h3>Run-time code block in regular expressions</h3>
<p> Code blocks in regular expressions (<tt>&quot;(?{...})&quot;</tt> and <tt>&quot;(??{...})&quot;</tt>) used not to inherit any pragmata (strict, warnings, etc.) if the regular expression was compiled at run time as happens in cases like these two: </p>
<pre><code>
use re 'eval';
$foo = ~$bar;
#when $bar contains(? {...})
                          $foo = ~ / $bar(? {$finished = 1}) / ;
</code></pre>
<p> This was a bug, which has now been fixed. But it has the potential to break any code that was relying on this bug.</p>
<h2>Deprecations</h2>
<h3>?PATTERN? is deprecated</h3>
<p> <tt>&quot;?PATTERN?&quot;</tt> (without the initial m) has been deprecated and now produces a warning. This is to allow future use of <tt>&quot;?&quot;</tt> in new operators. The match-once functionality is still available in the form of <tt>&quot;m?PATTERN?&quot;</tt>.</p>
<h3>sv_compile_2op() is now deprecated</h3>
<p> The <tt>&quot;sv_compile_2op()&quot;</tt> <font SIZE="-1">API</font> function is now deprecated. Searches suggest that nothing on <font SIZE="-1">CPAN</font> is using it, so this should have zero impact. </p>
<p> It attempted to provide an <font SIZE="-1">API</font> to compile code down to an optree, but failed to bind correctly to lexicals in the enclosing scope. It&#8217;s not possible to fix this problem within the constraints of its parameters and return value.</p>
<h3>Tie functions on scalars holding typeglobs</h3>
<p> Calling a tie function (<tt>&quot;tie&quot;</tt>, <tt>&quot;tied&quot;</tt>, <tt>&quot;untie&quot;</tt>) with a scalar argument acts on a file handle if the scalar happens to hold a typeglob. </p>
<p> This is a long-standing bug that will be removed in Perl 5.16, as there is currently no way to tie the scalar itself when it holds a typeglob, and no way to untie a scalar that has had a typeglob assigned to it. </p>
<p> This bug was fixed in 5.13.7 but, because of the breakage it caused, the fix has been reverted. Now there is a deprecation warning whenever a tie function is used on a handle without an explicit <tt>&quot;*&quot;</tt>.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Archive::Tar&quot;</tt> has been upgraded from version 1.72 to 1.74. </p>
<p> Skip extracting pax extended headers.</p>
<dt>&bull;</p>
<dd> <tt>&quot;autodie&quot;</tt> has been upgraded from version 2.10 to 2.1001. </p>
<p> Test fix in blead for <font SIZE="-1">VMS</font>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B&quot;</tt> has been upgraded from version 1.26 to 1.27. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Concise&quot;</tt> has been upgraded from version 0.81 to 0.82. </p>
<p> It no longer produces mangled output with the <tt>&quot;-tree&quot;</tt> option [perl #80632] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=80632">http://rt.perl.org/rt3/Public/Bug/Display.html?id=80632</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Deparse&quot;</tt> has been upgraded from version 1.01 to 1.02. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Cwd&quot;</tt> has been upgraded from version 3.34 to 3.35. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Data::Dumper&quot;</tt> has been upgraded from version 2.130_01 to 2.130_02. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::Peek&quot;</tt> has been upgraded from version 1.05 to 1.06. </p>
<p> Avoid compiler warnings. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::SelfStubber&quot;</tt> has been upgraded from version 1.03 to 1.05. </p>
<p> Whitespace changes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest::SHA&quot;</tt> has been upgraded from 5.48 to 5.50. </p>
<p> <tt>&quot;shasum&quot;</tt> now more closely mimics <tt>&quot;sha1sum&quot;</tt>/<tt>&quot;md5sum&quot;</tt>. </p>
<p> <tt>&quot;Addfile&quot;</tt> accepts all <font SIZE="-1">POSIX</font> filenames.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Dumpvalue&quot;</tt> has been upgraded from version 1.14 to 1.15. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;DynaLoader&quot;</tt> has been upgraded from version 1.11 to 1.12. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Env&quot;</tt> has been upgraded from version 1.01 to 1.02. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::CBuilder&quot;</tt> has been upgraded from 0.2703 to 0.280201. </p>
<p> Handle C and C<font SIZE="-2">++</font> compilers separately. </p>
<p> Preserves exit status on <font SIZE="-1">VMS</font>. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Constant::Utils&quot;</tt> has been upgraded from 0.02 to 0.03. </p>
<p> Refactoring and fixing of backcompat code, preparing for resynchronisation with <font SIZE="-1">CPAN</font>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Embed&quot;</tt> has been upgraded from 1.29 to 1.30. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::ParseXS&quot;</tt> has been upgraded from 2.2207 to 2.2208. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Fcntl&quot;</tt> has been upgraded from 1.10 to 1.11. </p>
<p> Avoid compiler warnings. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;feature&quot;</tt> has been upgraded from 1.18 to 1.19. </p>
<p> Documentation and test updates for the <tt>&quot;unicode_strings&quot;</tt> feature. See &quot;Full functionality for <tt>&quot;use feature 'unicode_strings'&quot;</tt>&quot;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::CheckTree&quot;</tt> has been upgraded from 4.4 to 4.41. </p>
<p> Whitespace changes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Glob&quot;</tt> has been upgraded from 1.10 to 1.11. </p>
<p> Avoid compiler warnings. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;GDBM_File&quot;</tt> has been upgraded from 1.12 to 1.13. </p>
<p> Test improvements. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Hash::Util::FieldHash&quot;</tt> has been upgraded from 1.06 to 1.07. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;I18N::Collate&quot;</tt> has been upgraded from 1.01 to 1.02. </p>
<p> Whitespace changes. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;if&quot;</tt> has been upgraded from 0.06 to 0.0601. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;IO&quot;</tt> has been upgraded from 1.25_02 to 1.25_03. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Cmd&quot;</tt> has been upgraded from 0.64 to 0.66. </p>
<p> Resolves an issue with splitting Win32 command lines. </p>
<p> Documentation enhancements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Open3&quot;</tt> has been upgraded from 1.07 to 1.08. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Codes&quot;</tt> has been upgraded from version 3.14 to 3.15. </p>
<p> Adds some codes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt&quot;</tt> has been upgraded from 1.99_01 to 1.99_02. </p>
<p> Documentation and comment spelling fixes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Memoize&quot;</tt> has been upgraded from version 1.01_03 to 1.02. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords. </p>
<p> Whitespace changes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;MIME::Base64&quot;</tt> has been upgraded from 3.10 to 3.13. </p>
<p> Now provides <tt>&quot;encode_base64url&quot;</tt> and <tt>&quot;decode_base64url&quot;</tt> functions to process the base64 scheme for &#8220;<font SIZE="-1">URL</font> applications&#8221;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;mro&quot;</tt> has been upgraded from version 1.05 to 1.06. </p>
<p> <tt>&quot;next::method&quot;</tt> <i>et al.</i> now take into account that every class inherits from <font SIZE="-1">UNIVERSAL</font> [perl #68654] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=68654">http://rt.perl.org/rt3/Public/Bug/Display.html?id=68654</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;NDBM_File&quot;</tt> has been upgraded from 1.10 to 1.11. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Net::Ping&quot;</tt> has been upgraded from 2.36 to 2.37. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ODBM_File&quot;</tt> has been upgraded from 1.09 to 1.10. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Opcode&quot;</tt> has been upgraded from 1.17 to 1.18. </p>
<p> Avoid compiler warnings. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;overload&quot;</tt> has been upgraded from 1.11 to 1.12. </p>
<p> Avoid a taint problem in use of sprintf. </p>
<p> Test asymmetric fallback cases [perl #71286] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=71286">http://rt.perl.org/rt3/Public/Bug/Display.html?id=71286</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::encoding&quot;</tt> has been upgraded from 0.13 to 0.14. </p>
<p> Avoid compiler warnings. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt> has been upgraded from 0.10 to 0.11. </p>
<p> A <tt>&quot;read&quot;</tt> after a <tt>&quot;seek&quot;</tt> beyond the end of the string no longer thinks it has data to read [perl #78716] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78716">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78716</a>&gt;. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::via&quot;</tt> has been upgraded from 0.10 to 0.11. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX&quot;</tt> has been upgraded from 1.22 to 1.23. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;re&quot;</tt> has been upgraded from 0.14 to 0.15. </p>
<p> Enforce that <tt>&quot;/d&quot;</tt>, <tt>&quot;/u&quot;</tt>, and <tt>&quot;/l&quot;</tt> are mutually exclusive.</p>
<dt>&bull;</p>
<dd> <tt>&quot;SDBM_File&quot;</tt> has been upgraded from 1.08 to 1.09. </p>
<p> Avoid compiler warnings. </p>
<p> Remove obsolete <font SIZE="-1">RCS</font> keywords. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Socket&quot;</tt> has been upgraded from 1.91 to 1.92. </p>
<p> It has several new functions for handling IPv6 addresses.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Storable&quot;</tt> has been upgraded from 2.24 to 2.25. </p>
<p> This adds support for serialising code references that contain <font SIZE="-1">UTF-8</font> strings correctly. The Storable minor version number changed as a result, meaning that Storable users who set <tt>$Storable::accept_future_minor</tt> to a <tt>&quot;FALSE&quot;</tt> value will see errors (see &#8220;<font SIZE="-1">FORWARD</font> <font SIZE="-1">COMPATIBILITY</font>&#8221; in Storable for more details). </p>
<p> Freezing no longer gets confused if the Perl stack gets reallocated during freezing [perl #80074] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=80074">http://rt.perl.org/rt3/Public/Bug/Display.html?id=80074</a>&gt;. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt> has been upgraded from 1.81_02 to 1.81_03. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads::shared&quot;</tt> has been upgraded from 1.34 to 1.35. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Time::HiRes&quot;</tt> has been upgraded from 1.9721 to 1.9721_01. </p>
<p> Build fix in blead for <font SIZE="-1">VMS</font>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate&quot;</tt> has been upgraded from 0.67 to 0.6801. </p>
<p> Documentation clarification. </p>
<p> Test improvements.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Normalize&quot;</tt> has been upgraded from 1.07 to 1.08. </p>
<p> Avoid compiler warnings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::UCD&quot;</tt> has been upgraded from 0.29 to 0.30. </p>
<p> Add info about named sequence alternatives. </p>
<p> Don&#8217;t use <tt>&quot;CompositionExclusions.txt&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;version&quot;</tt> has been upgraded from 0.82 to 0.86. </p>
<p> Modify export logic for <tt>&quot;is_strict&quot;</tt> and <tt>&quot;is_lax&quot;</tt>. </p>
<p> Various backcompat fixes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Win32&quot;</tt> has been upgraded from 0.39 to 0.41. </p>
<p> Add several functions. </p>
<p> Corrections to names returned by <tt>&quot;Win32::GetOSName&quot;</tt> and <tt>&quot;Win32::GetOSDisplayName&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;XS::APItest&quot;</tt> has been upgraded from 0.26 to 0.27. </p>
<p> Test new <font SIZE="-1">API</font> functions. </p>
<p> Avoid compiler warnings.</dl>
<h3>Dual-life Modules and Pragmata</h3>
<p> These modules were formerly distributed only in the Perl core distribution, and are now dual-lifed (meaning they are now also available separately on <font SIZE="-1">CPAN</font>):</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;autouse&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::SelfStubber&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;Dumpvalue&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;Env&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;File::CheckTree&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;I18N::Collate&quot;</tt></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> There is a new &#8220;Closure prototype called&#8221; error [perl #68560] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=68560">http://rt.perl.org/rt3/Public/Bug/Display.html?id=68560</a>&gt;.</dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> The &#8220;Found = in conditional&#8221; warning that is emitted when a constant is assigned to a variable in a condition is now withheld if the constant is actually a subroutine or one generated by <tt>&quot;use constant&quot;</tt>, since the value of the constant may not be known at the time the program is written [perl #77762] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77762">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77762</a>&gt;.</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;Encode&quot;</tt> module can now (once again) be included in a static Perl build. The special-case handling for this situation got broken in Perl 5.11.0, and has now been repaired.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> Tests for <tt>&quot;Fcntl&quot;</tt>, <tt>&quot;File::Glob&quot;</tt>, <tt>&quot;GDBM_File&quot;</tt>, <tt>&quot;IPC::Open3&quot;</tt>, <tt>&quot;NDBM_File&quot;</tt>, <tt>&quot;ODBM_File&quot;</tt>, <tt>&quot;Opcode&quot;</tt>, <tt>&quot;PerlIO::encoding&quot;</tt>, <tt>&quot;SDBM_File&quot;</tt>, and <tt>&quot;Storable&quot;</tt> now use the Test::More framework.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>NetBSD</p>
<dd> The NetBSD hints file has been changed to make the system&#8217;s malloc the default.</p>
<dt>Windows</p>
<dd> The option to use an externally-supplied <tt>&quot;crypt()&quot;</tt>, or to build with no <tt>&quot;crypt()&quot;</tt> at all, has been removed. Perl supplies its own <tt>&quot;crypt()&quot;</tt> implementation for Windows, and the political situation that required this part of the distribution to sometimes be omitted is long gone.</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;mg_findext()&quot;</tt> and <tt>&quot;sv_unmagicext()&quot;</tt> functions have been added to the <font SIZE="-1">API</font>. They allow extension authors to find and remove magic attached to scalars based on both the magic type and the magic virtual table, similar to how <tt>&quot;sv_magicext()&quot;</tt> attaches magic of a certain type and with a given virtual table to a scalar. This eliminates the need for extensions to walk the list of <tt>&quot;MAGIC&quot;</tt> pointers of an <tt>&quot;SV&quot;</tt> to find the magic that belongs to them.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;parse_fullexpr()&quot;</tt>, <tt>&quot;parse_listexpr()&quot;</tt>, <tt>&quot;parse_termexpr()&quot;</tt>, and <tt>&quot;parse_arithexpr()&quot;</tt> functions have been added to the <font SIZE="-1">API</font>. They perform recursive-descent parsing of expressions at various precedence levels. They are expected to be used by syntax plugins.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;BEGIN {require 5.12.0}&quot;</tt> now behaves as documented, rather than behaving identically to <tt>&quot;use 5.12.0;&quot;</tt>. Previously, <tt>&quot;require&quot;</tt> in a <tt>&quot;BEGIN&quot;</tt> block was erroneously executing the <tt>&quot;use feature ':5.12.0'&quot;</tt> and <tt>&quot;use strict; use warnings;&quot;</tt> behaviour, which only <tt>&quot;use&quot;</tt> was documented to provide [perl #69050] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=69050">http://rt.perl.org/rt3/Public/Bug/Display.html?id=69050</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;use 5.42&quot;</tt> [perl #69050] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=69050">http://rt.perl.org/rt3/Public/Bug/Display.html?id=69050</a>&gt;, <tt>&quot;use 6&quot;</tt> and <tt>&quot;no 5&quot;</tt> no longer leak memory.</p>
<dt>&bull;</p>
<dd> <tt>&quot;eval &quot;BEGIN{die}&quot;&quot;</tt> no longer leaks memory on non-threaded builds.</p>
<dt>&bull;</p>
<dd> PerlIO no longer crashes when called recursively, e.g., from a signal handler. Now it just leaks memory [perl #75556] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75556">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75556</a>&gt;.</p>
<dt>&bull;</p>
<dd> Defining a constant with the same name as one of perl&#8217;s special blocks (e.g., <font SIZE="-1">INIT</font>) stopped working in 5.12.0, but has now been fixed [perl #78634] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78634">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78634</a>&gt;.</p>
<dt>&bull;</p>
<dd> A reference to a literal value used as a hash key (<tt>$hash{\&quot;foo&quot;}</tt>) used to be stringified, even if the hash was tied [perl #79178] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=79178">http://rt.perl.org/rt3/Public/Bug/Display.html?id=79178</a>&gt;.</p>
<dt>&bull;</p>
<dd> A closure containing an <tt>&quot;if&quot;</tt> statement followed by a constant or variable is no longer treated as a constant [perl #63540] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=63540">http://rt.perl.org/rt3/Public/Bug/Display.html?id=63540</a>&gt;.</p>
<dt>&bull;</p>
<dd> Calling a closure prototype (what is passed to an attribute handler for a closure) now results in a &#8220;Closure prototype called&#8221; error message instead of a crash [perl #68560] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=68560">http://rt.perl.org/rt3/Public/Bug/Display.html?id=68560</a>&gt;.</p>
<dt>&bull;</p>
<dd> A regular expression optimisation would sometimes cause a match with a <tt>&quot;{n,m}&quot;</tt> quantifier to fail when it should match [perl #79152] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=79152">http://rt.perl.org/rt3/Public/Bug/Display.html?id=79152</a>&gt;.</p>
<dt>&bull;</p>
<dd> What has become known as the &#8220;Unicode Bug&#8221; is mostly resolved in this release. Under <tt>&quot;use feature 'unicode_strings'&quot;</tt>, the internal storage format of a string no longer affects the external semantics. There are two known exceptions. User-defined case changing functions, which are planned to be deprecated in 5.14, require utf8-encoded strings to function; and the character <tt>&quot;LATIN SMALL LETTER SHARP S&quot;</tt> in regular expression case-insensitive matching has a somewhat different set of bugs depending on the internal storage format. Case-insensitive matching of all characters that have multi-character matches, as this one does, is problematical in Perl. [perl #58182] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=58182">http://rt.perl.org/rt3/Public/Bug/Display.html?id=58182</a>&gt;.</p>
<dt>&bull;</p>
<dd> Mentioning a read-only lexical variable from the enclosing scope in a string <tt>&quot;eval&quot;</tt> no longer causes the variable to become writable [perl #19135] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=19135">http://rt.perl.org/rt3/Public/Bug/Display.html?id=19135</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;state&quot;</tt> can now be used with attributes. It used to mean the same thing as <tt>&quot;my&quot;</tt> if attributes were present [perl #68658] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=68658">http://rt.perl.org/rt3/Public/Bug/Display.html?id=68658</a>&gt;.</p>
<dt>&bull;</p>
<dd> Expressions like <tt>&quot;@$a &gt; 3&quot;</tt> no longer cause <tt>$a</tt> to be mentioned in the &#8220;Use of uninitialized value in numeric gt&#8221; warning when <tt>$a</tt> is undefined (since it is not part of the <tt>&quot;&gt;&quot;</tt> expression, but the operand of the <tt>&quot;@&quot;</tt>) [perl #72090] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72090">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72090</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;require&quot;</tt> no longer causes <tt>&quot;caller&quot;</tt> to return the wrong file name for the scope that called <tt>&quot;require&quot;</tt> and other scopes higher up that had the same file name [perl #68712] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=68712">http://rt.perl.org/rt3/Public/Bug/Display.html?id=68712</a>&gt;.</p>
<dt>&bull;</p>
<dd> The ref types in the typemap for <font SIZE="-1">XS</font> bindings now support magical variables [perl #72684] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72684">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72684</a>&gt;.</p>
<dt>&bull;</p>
<dd> Match variables (e.g., <tt>$1</tt>) no longer persist between calls to a sort subroutine [perl #76026] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=76026">http://rt.perl.org/rt3/Public/Bug/Display.html?id=76026</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;B&quot;</tt> module was returning <tt>&quot;B::OP&quot;</tt>s instead of <tt>&quot;B::LOGOP&quot;</tt>s for <tt>&quot;entertry&quot;</tt> [perl #80622] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=80622">http://rt.perl.org/rt3/Public/Bug/Display.html?id=80622</a>&gt;. This was due to a bug in the perl core, not in <tt>&quot;B&quot;</tt> itself.</p>
<dt>&bull;</p>
<dd> Some numeric operators were converting integers to floating point, resulting in loss of precision on 64-bit platforms [perl #77456] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77456">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77456</a>&gt;.</p>
<dt>&bull;</p>
<dd> The fallback behaviour of overloading on binary operators was asymmetric [perl #71286] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=71286">http://rt.perl.org/rt3/Public/Bug/Display.html?id=71286</a>&gt;.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.8 represents approximately one month of development since Perl 5.13.7 and contains 38715 lines of changes across 546 files from 38 authors and committers. </p>
<p> Thank you to the following for contributing to this release: </p>
<p> Abhijit Menon-Sen, Abigail, Andreas Ko.nig, Ben Morrow, Brad Gilbert, brian d foy, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, David Golden, David Leadbeater, David Mitchell, Father Chrysostomos, Florian Ragwitz, Goro Fuji, H.Merijn Brand, Jan Dubois, Jerry D. Hedden, Jesse Vincent, John Peacock, Karl Williamson, Lukas Mai, Marvin Humphrey, Max Maischein, Michael Breen, Michael Fig, Nicholas Clark, Nick Cleaton, Paul Evans, Peter J. Holzer, Peter John Acklam, Rafael Garcia-Suarez, Reini Urban, Renee Baecker, Ricardo Signes, Tony Cook, Yves Orton, Zefram</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
