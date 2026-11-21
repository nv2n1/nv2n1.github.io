---

title: "perl5137delta(1)"
name: "perl5137delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5137delta/"
description: "perl5137delta – what is new for perl v5.13.7"
---

<p> This document describes differences between the 5.13.6 release and the 5.13.7 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.5, first read perl5136delta, which describes differences between 5.13.5 and 5.13.6.  </p>
<h2>Core Enhancements</h2>
<h3>Single term prototype</h3>
<p> The <code>&quot;+&quot;</code> prototype is a special alternative to <code>&quot;$&quot;</code> that will act like <code>&quot;\[@%]&quot;</code> when given a literal array or hash variable, but will otherwise force scalar context on the argument. This is useful for functions which should accept either a literal array or an array reference as the argument: </p>
<pre><code>    sub smartpush (+@) {
        my $aref = shift;
        die &quot;Not an array or arrayref&quot; unless ref $aref eq 'ARRAY';
        push @$aref, @_;
    }
</code></pre>
<p> When using the <code>&quot;+&quot;</code> prototype, your function must check that the argument is of an acceptable type.  </p>
<h3>use re '/flags';</h3>
<p> The <code>&quot;re&quot;</code> pragma now has the ability to turn on regular expression flags till the end of the lexical scope: </p>
<pre><code>    use re '/x';
    &quot;foo&quot; =~ / (.+) /; # /x implied
</code></pre>
<p> See ``&#8216;/flags&#8217; mode&#8217;&#8216; in re for details.  </p>
<h3>Statement labels can appear in more places</h3>
<p> Statement labels can now occur before any type of statement or declaration, such as <code>&quot;package&quot;</code>.  </p>
<h3>use feature unicode_strings now applies to more regex matching</h3>
<p> Another chunk of the ``The &#8216;&#8216;Unicode Bug&quot;&quot; in perlunicode is fixed in this release. Now, regular expressions compiled within the scope of the ``unicode_strings&#8217;&#8216; feature (or under the ``u&#8217;&#8216; regex modifier (specifiable currently only with infix notation <code>&quot;(?u:...)&quot;</code> or via <code>&quot;use re &#8216;/u&#8217;&quot;</code>) will match the same whether or not the target string is encoded in utf8, with regard to <code>&quot;[[:posix:]]&quot;</code> character classes </p>
<p> Work is underway to add the case sensitive matching to the control of this feature, but was not complete in time for this dot release.  </p>
<h3>Array and hash container functions accept references</h3>
<p> All built-in functions that operate directly on array or hash containers now also accept hard references to arrays or hashes: </p>
<pre><code>  |----------------------------+---------------------------|
  | Traditional syntax | Terse syntax |
  |----------------------------+---------------------------|
  | push @$arrayref, @stuff | push $arrayref, @stuff |
  | unshift @$arrayref, @stuff | unshift $arrayref, @stuff |
  | pop @$arrayref | pop $arrayref |
  | shift @$arrayref | shift $arrayref |
  | splice @$arrayref, 0, 2 | splice $arrayref, 0, 2 |
  | keys %$hashref | keys $hashref |
  | keys @$arrayref | keys $arrayref |
  | values %$hashref | values $hashref |
  | values @$arrayref | values $arrayref |
  | ($k,$v) = each %$hashref | ($k,$v) = each $hashref |
  | ($k,$v) = each @$arrayref | ($k,$v) = each $arrayref |
  |----------------------------+---------------------------|
</code></pre>
<p> This allows these built-in functions to act on long dereferencing chains or on the return value of subroutines without needing to wrap them in <code>&quot;@{}&quot;</code> or <code>&quot;%{}&quot;</code>: </p>
<pre><code>  push @{$obj-&gt;tags}, $new_tag; # old way
  push $obj-&gt;tags, $new_tag; # new way
  for ( keys %{$hoh-&gt;{genres}{artists}} ) {...} # old way
  for ( keys $hoh-&gt;{genres}{artists} ) {...} # new way
</code></pre>
<p> For <code>&quot;push&quot;</code>, <code>&quot;unshift&quot;</code> and <code>&quot;splice&quot;</code>, the reference will auto-vivify if it is not defined, just as if it were wrapped with <code>&quot;@{}&quot;</code>. </p>
<p> Calling <code>&quot;keys&quot;</code> or <code>&quot;values&quot;</code> directly on a reference gives a substantial performance improvement over explicit dereferencing. </p>
<p> For <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code>, <code>&quot;each&quot;</code>, when overloaded dereferencing is present, the overloaded dereference is used instead of dereferencing the underlying reftype. Warnings are issued about assumptions made in the following three ambiguous cases: </p>
<pre><code>  (a) If both %{} and @{} overloading exists, %{} is used
  (b) If %{} overloading exists on a blessed arrayref, %{} is used
  (c) If @{} overloading exists on a blessed hashref, @{} is used
</code></pre>
<h3>y///r</h3>
<p> The <code>&quot;/r&quot;</code> flag, which was added to <code>&quot;s///&quot;</code> in 5.13.2, has been extended to the <code>&quot;y///&quot;</code> operator. </p>
<p> It causes it to perform the substitution on a <i>copy</i> of its operand, returning that copy instead of a character count.  </p>
<h3>New global variable ${^GLOBAL_PHASE}</h3>
<p> A new global variable, <code>&quot;${^GLOBAL_PHASE}&quot;</code>, has been added to allow introspection of the current phase of the perl interpreter. It&#8217;s explained in detail in ``${^GLOBAL_PHASE}&#8216;&#8216; in perlvar and ``<font SIZE="-1">BEGIN</font>, <font SIZE="-1">UNITCHECK</font>, <font SIZE="-1">CHECK</font>, <font SIZE="-1">INIT</font> and <font SIZE="-1">END</font>&#8216;&#8216; in perlmod.  </p>
<h3>Unicode Version 6.0 is now supported (mostly)</h3>
<p> Perl comes with the Unicode 6.0 data base updated with Corrigendum #8 &lt;<a rel="nofollow" href="http://www.unicode.org/versions/corrigendum8.html">http://www.unicode.org/versions/corrigendum8.html</a>&gt;, with one exception noted below. See &lt;<a rel="nofollow" href="http://unicode.org/versions/Unicode6.0.0">http://unicode.org/versions/Unicode6.0.0</a>&gt; for details on the new release. Perl does not support any Unicode provisional properties, including the new ones for this release, but their database files are packaged with Perl. </p>
<p> Unicode 6.0 has chosen to use the name <code>&quot;BELL&quot;</code> for the character at U+1F514, which is a symbol that looks like a bell, and used in Japanese cell phones. This conflicts with the long-standing Perl usage of having <code>&quot;BELL&quot;</code> mean the <font SIZE="-1">ASCII</font> <code>&quot;BEL&quot;</code> character, U+0007. In Perl 5.14, <code>&quot;\N{BELL}&quot;</code> will continue to mean U+0007, but its use will generate a deprecated warning message, unless such warnings are turned off. The new name for U+0007 in Perl will be <code>&quot;ALERT&quot;</code>, which corresponds nicely with the existing shorthand sequence for it, <code>&quot;\a&quot;</code>. <code>&quot;\N{BEL}&quot;</code> will mean U+0007, with no warning given. The character at U+1F514 will not have a name in 5.14, but can be referred to by <code>&quot;\N{U+1F514}&quot;</code>. The plan is that in Perl 5.16, <code>&quot;\N{BELL}&quot;</code> will refer to U+1F514, and so all code that uses <code>&quot;\N{BELL}&quot;</code> should convert by then to using <code>&quot;\N{ALERT}&quot;</code>, <code>&quot;\N{BEL}&quot;</code>, or <code>&quot;\a&quot;</code> instead.  </p>
<h3>Improved support for custom OPs</h3>
<p> Custom ops can now be registered with the new <code>&quot;custom_op_register&quot;</code> C function and the <code>&quot;XOP&quot;</code> structure. This will make it easier to add new properties of custom ops in the future. Two new properties have been added already, <code>&quot;xop_class&quot;</code> and <code>&quot;xop_peep&quot;</code>. </p>
<p> <code>&quot;xop_class&quot;</code> is one of the OA_*OP constants, and allows B and other introspection mechanisms to work with custom ops that aren&#8217;t BASEOPs. <code>&quot;xop_peep&quot;</code> is a pointer to a function that will be called for ops of this type from <code>&quot;Perl_rpeep&quot;</code>. </p>
<p> See ``Custom Operators&#8217;&#8216; in perlguts and ``Custom Operators&#8217;&#8216; in perlapi for more detail. </p>
<p> The old <code>&quot;PL_custom_op_names&quot;</code>/<code>&quot;PL_custom_op_descs&quot;</code> interface is still supported but discouraged.  </p>
<h2>Incompatible Changes</h2>
<h3>Dereferencing typeglobs</h3>
<p> If you assign a typeglob to a scalar variable: </p>
<pre><code>    $glob = *foo;
</code></pre>
<p> the glob that is copied to <code>$glob</code> is marked with a special flag indicating that the glob is just a copy. This allows subsequent assignments to <code>$glob</code> to overwrite the glob. The original glob, however, is immutable. </p>
<p> Many Perl operators did not distinguish between these two types of globs. This would result in strange behaviour in edge cases: <code>&quot;untie $scalar&quot;</code> would do nothing if the last thing assigned to the scalar was a glob (because it treated it as <code>&quot;untie *$scalar&quot;</code>, which unties a handle). Assignment to a glob slot (e.g., <code>&quot;(*$glob) = \@some_array&quot;</code>) would simply assign <code>&quot;\@some_array&quot;</code> to <code>$glob</code>. </p>
<p> To fix this, the <code>&quot;*{}&quot;</code> operator (including the <code>*foo</code> and <code>*$foo</code> forms) has been modified to make a new immutable glob if its operand is a glob copy. Various operators that make a distinction between globs and scalars have been modified to treat only immutable globs as globs. </p>
<p> This causes an incompatible change in code that assigns a glob to the return value of <code>&quot;*{}&quot;</code> when that operator was passed a glob copy. Take the following code, for instance: </p>
<pre><code>    $glob = *foo;
    *$glob = *bar;
</code></pre>
<p> The <code>*$glob</code> on the second line returns a new immutable glob. That new glob is made an alias to <code>*bar</code>. Then it is discarded. So the second assignment has no effect. </p>
<p> It also means that <code>&quot;tie $handle&quot;</code> will now tie <code>$handle</code> as a scalar, even if it has had a glob assigned to it. </p>
<p> The upside to this incompatible change is that bugs [perl #77496] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77496">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77496</a>&gt;, [perl #77502] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77502">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77502</a>&gt;, [perl #77508] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77508">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77508</a>&gt;, [perl #77688] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77688">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77688</a>&gt;, and [perl #77812] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77812">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77812</a>&gt;, and maybe others, too, have been fixed. </p>
<p> See &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77810">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77810</a>&gt; for even more detail.  </p>
<h3>Clearing stashes</h3>
<p> Stash list assignment <code>&quot;%foo:: = ()&quot;</code> used to make the stash anonymous temporarily while it was being emptied. Consequently, any of its subroutines referenced elsewhere would become anonymous (showing up as ``(unknown)&#8216;&#8216; in <code>&quot;caller&quot;</code>). Now they retain their package names, such that <code>&quot;caller&quot;</code> will return the original sub name if there is still a reference to its typeglob, or ``foo::__ANON__&#8216;&#8216; otherwise [perl #79208] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=79208">http://rt.perl.org/rt3/Public/Bug/Display.html?id=79208</a>&gt;.  </p>
<h2>Deprecations</h2>
<h3>\N{BELL} is deprecated</h3>
<p> This is because Unicode is using that name for a different character. See ``Unicode Version 6.0 is now supported (mostly)&#8216;&#8216; for more explanation.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> When an object has many weak references to it, freeing that object can under some some circumstances take O(N^2) time to free (where N is the number of references). The number of circumstances has been reduced. [perl #75254] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75254">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75254</a>&gt;. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The following modules were added by the <code>&quot;Unicode::Collate&quot;</code> upgrade from 0.63 to 0.67. See below for details. </p>
<p> <code>&quot;Unicode::Collate::CJK::Big5&quot;</code> </p>
<p> <code>&quot;Unicode::Collate::CJK::GB2312&quot;</code> </p>
<p> <code>&quot;Unicode::Collate::CJK::JISX0208&quot;</code> </p>
<p> <code>&quot;Unicode::Collate::CJK::Korean&quot;</code> </p>
<p> <code>&quot;Unicode::Collate::CJK::Pinyin&quot;</code> </p>
<p> <code>&quot;Unicode::Collate::CJK::Stroke&quot;</code> </p>
 </dd></dl>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Archive::Extract&quot;</code> has been upgraded from 0.44 to 0.46 </p>
<p> Resolves an issue with NetBSD-current and its new unzip executable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Archive::Tar&quot;</code> has been upgraded from 1.68 to 1.72 </p>
<p> This adds the ptargrep utility for using regular expressions against the contents of files in a tar archive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;B&quot;</code> has been upgraded from 1.24 to 1.26. </p>
<p> It no longer crashes when taking apart a <code>&quot;y///&quot;</code> containing characters outside the octet range or compiled in a <code>&quot;use utf8&quot;</code> scope. </p>
<p> The size of the shared object has been reduced by about 40%, with no reduction in functionality. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;B::Deparse&quot;</code> has been upgraded from 0.99 to 1.01. </p>
<p> It fixes deparsing of <code>&quot;our&quot;</code> followed by a variable with funny characters (as permitted under the <code>&quot;utf8&quot;</code> pragma) [perl #33752] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=33752">http://rt.perl.org/rt3/Public/Bug/Display.html?id=33752</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CGI&quot;</code> has been upgraded from 3.49 to 3.50 </p>
<p> This provides the following security fixes: the <font SIZE="-1">MIME</font> boundary in multipart_init is now random and improvements to the handling of newlines embedded in header values. </p>
<p> The documentation for <i>param_fetch()</i> has been corrected and clarified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CPAN&quot;</code> has been upgraded from 1.94_61 to 1.94_62 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CPANPLUS&quot;</code> has been upgraded from 0.9007 to 0.9010 </p>
<p> Fixes for the SQLite source engine and resolving of issues with the testsuite when run under local::lib and/or cpanminus </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CPANPLUS::Dist::Build&quot;</code> has been upgraded from 0.48 to 0.50 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Data::Dumper&quot;</code> has been upgraded from 2.129 to 2.130_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;DynaLoader&quot;</code> has been upgraded from 1.10 to 1.11. </p>
<p> It fixes a buffer overflow when passed a very long file name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ExtUtils::Constant&quot;</code> has been upgraded from 0.22 to 0.23. </p>
<p> The <code>&quot;AUTOLOAD&quot;</code> helper code generated by <code>&quot;ExtUtils::Constant::ProxySubs&quot;</code> can now <code>&quot;croak&quot;</code> for missing constants, or generate a complete <code>&quot;AUTOLOAD&quot;</code> subroutine in <font SIZE="-1">XS</font>, allowing simplification of many modules that use it. (<code>&quot;Fcntl&quot;</code>, <code>&quot;File::Glob&quot;</code>, <code>&quot;GDBM_File&quot;</code>, <code>&quot;I18N::Langinfo&quot;</code>, <code>&quot;POSIX&quot;</code>, <code>&quot;Socket&quot;</code>) </p>
<p> <code>&quot;ExtUtils::Constant::ProxySubs&quot;</code> can now optionally push the names of all constants onto the package&#8217;s C{@EXPORT_OK}. This has been used to replace less space-efficient code in <code>&quot;B&quot;</code>, helping considerably shrink the size of its shared object. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Fcntl&quot;</code> has been upgraded from 1.09 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Fetch&quot;</code> has been upgraded from 0.24 to 0.28 </p>
<p> <code>&quot;HTTP::Lite&quot;</code> is now supported for &#8216;http&#8217; scheme. </p>
<p> The <code>&quot;fetch&quot;</code> utility is supported on FreeBSD, NetBSD and Dragonfly <font SIZE="-1">BSD</font> for the <code>&quot;http&quot;</code> and <code>&quot;ftp&quot;</code> schemes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Glob&quot;</code> has been upgraded from 1.09 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::stat&quot;</code> has been upgraded from 1.03 to 1.04. </p>
<p> The <code>&quot;-x&quot;</code> and <code>&quot;-X&quot;</code> file test operators now work correctly under the root user. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;GDBM_File&quot;</code> has been upgraded from 1.11 to 1.12. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Hash::Util&quot;</code> has been upgraded from 0.09 to 0.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Hash::Util::FieldHash&quot;</code> has been upgraded from 1.05 to 1.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;I18N::Langinfo&quot;</code> has been upgraded from 0.06 to 0.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Locale::Maketext&quot;</code> has been upgraded from 1.16 to 1.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Math::BigInt&quot;</code> has been upgraded from 1.97 to 1.99_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Math::BigRat&quot;</code> has been upgraded from 0.26 to 0.26_01 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Math::BigInt::FastCalc&quot;</code> has been upgraded from 0.22 to 0.24_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;MIME::Base64&quot;</code> has been upgraded from 3.09 to 3.10 </p>
<p> Includes new functions to calculate the length of encoded and decoded base64 strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;mro&quot;</code> has been upgraded from 1.04 to 1.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;NDBM_File&quot;</code> has been upgraded from 1.09 to 1.10. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ODBM_File&quot;</code> has been upgraded from 1.08 to 1.09. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Opcode&quot;</code> has been upgraded from 1.16 to 1.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;parent&quot;</code> has been upgraded from 0.223 to 0.224 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Pod::Simple&quot;</code> has been upgraded from 3.14 to 3.15 </p>
<p> Includes various fixes to <code>&quot;HTML&quot;</code> and <code>&quot;XHTML&quot;</code> handling. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;POSIX&quot;</code> has been upgraded from 1.21 to 1.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;re&quot;</code> has been upgraded from 0.13 to 0.14, for the sake of the new <code>&quot;use re &quot;/flags&quot;&quot;</code> pragma. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Safe&quot;</code> has been upgraded from 2.28 to 2.29. </p>
<p> It adds <code>&amp;version::vxs::VCMP</code> to the default share. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;SDBM_File&quot;</code> has been upgraded from 1.07 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;SelfLoader&quot;</code> has been upgraded from 1.17 to 1.18. </p>
<p> It now works in taint mode [perl #72062] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72062">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72062</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Socket&quot;</code> has been upgraded from 1.90 to 1.91. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Storable&quot;</code> has been upgraded from 2.22 to 2.24 </p>
<p> Includes performance improvement for overloaded classes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Sys::Hostname&quot;</code> has been upgraded from 1.13 to 1.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Unicode::Collate&quot;</code> has been upgraded from 0.63 to 0.67 </p>
<p> This release newly adds locales <code>&quot;ja&quot;</code> <code>&quot;ko&quot;</code> and <code>&quot;zh&quot;</code> and its variants ( <code>&quot;zh__big5han&quot;</code>, <code>&quot;zh__gb2312han&quot;</code>, <code>&quot;zh__pinyin&quot;</code>, <code>&quot;zh__stroke&quot;</code> ). </p>
<p> Supported UCA_Version 22 for Unicode 6.0.0. </p>
<p> The following modules have been added: </p>
<p> <code>&quot;Unicode::Collate::CJK::Big5&quot;</code> for <code>&quot;zh__big5han&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s big5han ordering. </p>
<p> <code>&quot;Unicode::Collate::CJK::GB2312&quot;</code> for <code>&quot;zh__gb2312han&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s gb2312han ordering. </p>
<p> <code>&quot;Unicode::Collate::CJK::JISX0208&quot;</code> which makes tailoring of 6355 kanji (<font SIZE="-1">CJK</font> Unified Ideographs) in the <font SIZE="-1">JIS</font> X 0208 order. </p>
<p> <code>&quot;Unicode::Collate::CJK::Korean&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s Korean ordering. </p>
<p> <code>&quot;Unicode::Collate::CJK::Pinyin&quot;</code> for <code>&quot;zh__pinyin&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s pinyin ordering. </p>
<p> <code>&quot;Unicode::Collate::CJK::Stroke&quot;</code> for <code>&quot;zh__stroke&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s stroke ordering. </p>
 </dd></dl>
<h2>Documentation</h2>
<p> perlvar reorders the variables and groups them by topic. Each variable introduced after Perl 5.000 notes the first version in which it is available. perlvar also has a new section for deprecated variables to note when they were removed.  </p>
<h3>New Documentation</h3>
<p> <i>perlpodstyle</i> </p>
<p> New style guide for <font SIZE="-1">POD</font> documentation, split mostly from the <font SIZE="-1">NOTES</font> section of the pod2man man page. </p>
<p> ( This was added to <code>&quot;v5.13.6&quot;</code> but was not documented with that release ).  </p>
<h3>Changes to Existing Documentation</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Array and hash slices in scalar context are now documented in perldata. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlform and perllocale have been corrected to state that <code>&quot;use locale&quot;</code> affects formats. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> ``Using !~ with <code>%s</code> doesn&#8217;t make sense&#8217;&#8216;: This message was actually added in 5.13.2, but was omitted from perldelta. It now applies also to the <code>&quot;y///&quot;</code> operator, and has been documented. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> <i>ptargrep</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> ptargrep is a utility to apply pattern matching to the contents of files in a tar archive. It comes with <code>&quot;Archive::Tar&quot;</code>. </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The new <i>t/mro/isa_aliases.t</i> has been added, which tests that <code>&quot;*Foo::ISA = *Bar::ISA&quot;</code> works properly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/mro/isarev.t</i> has been added, which tests that <code>&quot;PL_isarev&quot;</code> (accessible at the Perl level via <code>&quot;mro::get_isarev&quot;</code>) is updated properly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/run/switchd-78586.t</i> has been added, which tests that [perl #78586] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78586">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78586</a>&gt; has been fixed (related to line numbers in the debugger). </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Windows</dt>
<dd> <p> Directory handles are now properly cloned when threads are created. In perl 5.13.6, child threads simply stopped inheriting directory handles. In previous versions, threads would share handles, resulting in crashes. </p>
<p> Support for building with Visual C<font SIZE="-2">++</font> 2010 is now underway, but is not yet complete. See <i></i><font SIZE="-1"><i>README</i></font><i>.win32</i> for more details. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd> <p> Record-oriented files (record format variable or variable with fixed control) opened for write by the perlio layer will now be line buffered to prevent the introduction of spurious line breaks whenever the perlio buffer fills up. </p>
 </dd></dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;lex_start&quot;</code> has been added to the <font SIZE="-1">API</font>, but is considered experimental. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <code>&quot;parse_block&quot;</code> function has been added to the <font SIZE="-1">API</font> [perl #78222] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new, experimental <font SIZE="-1">API</font> has been added for accessing the internal structure that Perl uses for <code>&quot;%^H&quot;</code>. See the functions beginning with <code>&quot;cophh_&quot;</code> in perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A stash can now have a list of effective names in addition to its usual name. The first effective name can be accessed via the <code>&quot;HvENAME&quot;</code> macro, which is now the recommended name to use in <font SIZE="-1">MRO</font> linearisations (<code>&quot;HvNAME&quot;</code> being a fallback if there is no <code>&quot;HvENAME&quot;</code>). </p>
<p> These names are added and deleted via <code>&quot;hv_ename_add&quot;</code> and <code>&quot;hv_ename_delete&quot;</code>. These two functions are <i>not</i> part of the <font SIZE="-1">API</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The way the parser handles labels has been cleaned up and refactored. As a result, the <code>&quot;newFOROP()&quot;</code> constructor function no longer takes a parameter stating what label is to go in the state op. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;newWHILEOP()&quot;</code> and <code>&quot;newFOROP()&quot;</code> functions no longer accept a line number as a parameter. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <code>&quot;parse_barestmt()&quot;</code> function has been added, for parsing a statement without a label. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <code>&quot;parse_label()&quot;</code> function has been added, that parses a statement label, separate from statements. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;CvSTASH()&quot;</code> macro can now only be used as an rvalue. <code>&quot;CvSTASH_set()&quot;</code> has been added to replace assignment to <code>&quot;CvSTASH()&quot;</code>. This is to ensure that backreferences are handled properly. These macros are not part of the <font SIZE="-1">API</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;op_scope()&quot;</code> and <code>&quot;op_lvalue()&quot;</code> functions have been added to the <font SIZE="-1">API</font>, but are considered experimental. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;parse_stmt&quot;</code> C function added in earlier in the 5.13.x series has been fixed to work with statements ending with <code>&quot;}&quot;</code> [perl #78222] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;parse_fullstmt&quot;</code> C function added in 5.13.5 has been fixed to work when called while an expression is being parsed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Characters in the Latin-1 non-ASCII range (0x80 to 0xFF) used not to match themselves if the string happened to be UTF8-encoded internally, the regular expression was not, and the character in the regular expression was inside a repeated group (e.g., <code>&quot;Encode::decode_utf8(&quot;\303\200&quot;) =~ /(\xc0)+/&quot;</code>) [perl #78464] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78464">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78464</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;(?d)&quot;</code> regular expression construct now overrides a previous <code>&quot;(?u)&quot;</code> or <code>&quot;use feature &quot;unicode_string&quot;&quot;</code> [perl #78508] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78508">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78508</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A memory leak in <code>&quot;do &quot;file&quot;&quot;</code>, introduced in perl 5.13.6, has been fixed [perl #78488] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78488">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78488</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various bugs related to typeglob dereferencing have been fixed. See ``Dereferencing typeglobs&#8217;&#8216;, above. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;SvPVbyte&quot;</code> function available to <font SIZE="-1">XS</font> modules now calls magic before downgrading the <font SIZE="-1">SV</font>, to avoid warnings about wide characters [perl #72398] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72398">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72398</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;=&quot;</code> operator used to ignore magic (e.g., tie methods) on its right-hand side if the scalar happened to hold a typeglob. This could happen if a typeglob was the last thing returned from or assigned to a tied scalar [perl #77498] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77498">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77498</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sprintf&quot;</code> was ignoring locales when called with constant arguments [perl #78632] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78632">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78632</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A non-ASCII character in the Latin-1 range could match both a Posix class, such as <code>&quot;[[:alnum:]]&quot;</code>, and its inverse <code>&quot;[[:^alnum:]]&quot;</code>. This is now fixed for regular expressions compiled under the <code>&quot;u&quot;</code> modifier. See &quot;<code>&quot;use feature &quot;unicode_strings&quot;&quot;</code> now applies to more regex matching&quot;. [perl #18281] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=18281">http://rt.perl.org/rt3/Public/Bug/Display.html?id=18281</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Concatenating long strings under <code>&quot;use encoding&quot;</code> no longer causes perl to crash [perl #78674] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78674">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78674</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Typeglob assignments would crash if the glob&#8217;s stash no longer existed, so long as the glob assigned to was named &#8216;<font SIZE="-1">ISA</font>&#8216; or the glob on either side of the assignment contained a subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;-&gt;import&quot;</code> on a class lacking an import method could corrupt the stack, resulting in strange behaviour. For instance, </p>
<pre><code>  push @a, &quot;foo&quot;, $b = bar-&gt;import;
</code></pre>
<p> would assign &#8216;foo&#8217; to <code>$b</code> [perl #63790] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=63790">http://rt.perl.org/rt3/Public/Bug/Display.html?id=63790</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Creating an alias to a package when that package had been detached from the symbol table would result in corrupted isa caches [perl #77358] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77358">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77358</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;.=&quot;</code> followed by <code>&quot;&lt;&gt;&quot;</code> or <code>&quot;readline&quot;</code> would leak memory if <code>$/</code> contained characters beyond the octet range and the scalar assigned to happened to be encoded as <font SIZE="-1">UTF8</font> internally [perl #72246] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72246">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72246</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;recv&quot;</code> function could crash when called with the <font SIZE="-1">MSG_TRUNC</font> flag [perl #75082] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75082">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75082</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Evaluating a simple glob (like <code>*a</code>) was calling get-magic on the glob, even when its contents were not being used [perl #78580] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78580">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78580</a>&gt;. </p>
<p> This bug was introduced in 5.13.2 and did not affect earlier perl versions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Matching a Unicode character against an alternation containing characters that happened to match continuation bytes in the former&#8217;s <font SIZE="-1">UTF8</font> representation (<code>&quot;qq{\x{30ab}} =~ /\xab|\xa9/&quot;</code>) would cause erroneous warnings [perl #70998] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=70998">http://rt.perl.org/rt3/Public/Bug/Display.html?id=70998</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s///r&quot;</code> (added in 5.13.2) no longer leaks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The trie optimisation was not taking empty groups into account, preventing &#8216;foo&#8217; from matching <code>&quot;/\A(?:(?:)foo|bar|zot)\z/&quot;</code> [perl #78356] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78356">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78356</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A pattern containing a <code>&quot;+&quot;</code> inside a lookahead would sometimes cause an incorrect match failure in a global match (e.g., <code>&quot;/(?=(\S+))/g&quot;</code>) [perl #68564] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=68564">http://rt.perl.org/rt3/Public/Bug/Display.html?id=68564</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Iterating with <code>&quot;foreach&quot;</code> over an array returned by an lvalue sub now works [perl #23790] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=23790">http://rt.perl.org/rt3/Public/Bug/Display.html?id=23790</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$@</code> is now localised during calls to <code>&quot;binmode&quot;</code> to prevent action at a distance [perl #78844] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78844">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78844</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_isarev&quot;</code>, which is accessible to Perl via <code>&quot;mro::get_isarev&quot;</code> is now updated properly when packages are deleted or removed from the <code>@ISA</code> of other classes. This allows many packages to be created and deleted without causing a memory leak [perl #75176] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75176">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75176</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef *Foo::&quot;</code> and <code>&quot;undef *Foo::ISA&quot;</code> and <code>&quot;delete $package::{ISA}&quot;</code> used not to update the internal isa caches if the stash or <code>@ISA</code> array had a reference elsewhere. In fact, <code>&quot;undef *Foo::ISA&quot;</code> would stop a new <code>@Foo::ISA</code> array from updating caches. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@ISA</code> arrays can now be shared between classes via <code>&quot;*Foo::ISA = \@Bar::ISA&quot;</code> or <code>&quot;*Foo::ISA = *Bar::ISA&quot;</code> [perl #77238] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77238">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77238</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parser no longer hangs when encountering certain Unicode characters, such as U+387 [perl #74022] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74022">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74022</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;formline&quot;</code> no longer crashes when passed a tainted format picture. It also taints <code>$^A</code> now if its arguments are tainted [perl #79138] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=79138">http://rt.perl.org/rt3/Public/Bug/Display.html?id=79138</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A signal handler called within a signal handler could cause leaks or double-frees. Now fixed. [perl #76248] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=76248">http://rt.perl.org/rt3/Public/Bug/Display.html?id=76248</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When trying to report <code>&quot;Use of uninitialized value $Foo::BAR&quot;</code>, crashes could occur if the <font SIZE="-1">GLOB</font> of the global variable causing the warning has been detached from its original stash by, for example <code>&quot;delete $::{&#8216;Foo::&#8216;}&quot;</code>. This has been fixed by disabling the reporting of variable names in the warning in those cases. </p>
 </dd></dl>
<h2>Obituary</h2>
<p> Randy Kobes, creator of the kobesearch alternative to search.cpan.org and contributor/maintainer to several core Perl toolchain modules, passed away on September 18, 2010 after a battle with lung cancer. His contributions to the Perl community will be missed.  </p>
<h2>Acknowledgements</h2>
<p> Perl 5.13.7 represents approximately one month of development since Perl 5.13.6 and contains 73100 lines of changes across 518 files from 39 authors and committers: </p>
<p> Abhijit Menon-Sen, Abigail, Ben Morrow, Chas. J. Owens <font SIZE="-1">IV</font>, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, David Golden, David Mitchell, Father Chrysostomos, Fingle Nark, Florian Ragwitz, George Greer, Grant McLean, H.Merijn Brand, Ian Goodacre, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Karl Williamson, Lubomir Rintel, Marty Pauley, Moritz Lenz, Nicholas Clark, Nicolas Kaiser, Niko Tyni, Peter John Acklam, Rafael Garcia-Suarez, Shlomi Fish, Steffen Mueller, Steve Hay, Tatsuhiko Miyagawa, Tim Bunce, Todd Rinaldo, Tom Christiansen, Tom Hukins, Tony Cook, Yves Orton, Zefram and brian d foy </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
