---
title: "perl5137delta(1)"
name: "perl5137delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5137delta/"
description: "perl5137delta – what is new for perl v5.13.7"
---

<h2 class="name">NAME</h2>
<p> perl5137delta &#8211; what is new for perl v5.13.7 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.6 release and the 5.13.7 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.5, first read perl5136delta, which describes differences between 5.13.5 and 5.13.6.</p>
<h2>Core Enhancements</h2>
<h3>Single term prototype</h3>
<p> The <tt>&quot;+&quot;</tt> prototype is a special alternative to <tt>&quot;$&quot;</tt> that will act like <tt>&quot;\[@%]&quot;</tt> when given a literal array or hash variable, but will otherwise force scalar context on the argument. This is useful for functions which should accept either a literal array or an array reference as the argument: </p>
<pre><code>
sub smartpush(+@)
{
    my $aref = shift;
    die "Not an array or arrayref" unless ref $aref eq 'ARRAY';
    push @$aref, @_;
}
</code></pre>
<p> When using the <tt>&quot;+&quot;</tt> prototype, your function must check that the argument is of an acceptable type.</p>
<h3>use re &#8216;/flags&#8217;;</h3>
<p> The <tt>&quot;re&quot;</tt> pragma now has the ability to turn on regular expression flags till the end of the lexical scope: </p>
<pre>
    use re '/x';
    &quot;foo&quot; =~ / (.+) /;  # /x implied
</pre>
<p> See &#8220;&#8217;/flags&#8217; mode&#8221; in re for details.</p>
<h3>Statement labels can appear in more places</h3>
<p> Statement labels can now occur before any type of statement or declaration, such as <tt>&quot;package&quot;</tt>.</p>
<h3>use feature unicode_strings now applies to more regex matching</h3>
<p> Another chunk of the &#8220;The &#8221;Unicode Bug&quot;&quot; in perlunicode is fixed in this release. Now, regular expressions compiled within the scope of the &#8220;unicode_strings&#8221; feature (or under the &#8220;u&#8221; regex modifier (specifiable currently only with infix notation <tt>&quot;(?u:...)&quot;</tt> or via <tt>&quot;use re '/u'&quot;</tt>) will match the same whether or not the target string is encoded in utf8, with regard to <tt>&quot;[[:posix:]]&quot;</tt> character classes </p>
<p> Work is underway to add the case sensitive matching to the control of this feature, but was not complete in time for this dot release.</p>
<h3>Array and hash container functions accept references</h3>
<p> All built-in functions that operate directly on array or hash containers now also accept hard references to arrays or hashes: </p>
<p>| &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; |<br />
    | Traditional syntax | Terse syntax |<br />
    | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; |<br />
    | push @$arrayref,<br />
    @stuff | push $arrayref, @stuff | | unshift @$arrayref, @stuff | unshift $arrayref, @stuff | | pop @$arrayref | pop $arrayref | | shift @$arrayref | shift $arrayref | | splice @$arrayref, 0, 2 | splice $arrayref, 0, 2 | | keys % $hashref | keys $hashref | | keys @$arrayref | keys $arrayref | | values % $hashref | values $hashref | | values @$arrayref | values $arrayref | | ($k, $v) = each % $hashref | ($k, $v) = each $hashref | | ($k, $v) = each @$arrayref | ($k, $v) = each $arrayref | | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; |</p>
<p> This allows these built-in functions to act on long dereferencing chains or on the return value of subroutines without needing to wrap them in <tt>&quot;@{}&quot;</tt> or <tt>&quot;%{}&quot;</tt>: </p>
<p>push @{$obj-&gt;tags}, $new_tag;<br />
#old way<br />
    push $obj-&gt;tags,<br />
    $new_tag;<br />
#new way for (keys % {$hoh-&gt;{genres} {artists}})<br />
{<br />
    &#8230;<br />
}<br />
#old way for (keys $hoh-&gt;{genres} {artists})<br />
{<br />
    &#8230;<br />
}<br />
#new way</p>
<p> For <tt>&quot;push&quot;</tt>, <tt>&quot;unshift&quot;</tt> and <tt>&quot;splice&quot;</tt>, the reference will auto-vivify if it is not defined, just as if it were wrapped with <tt>&quot;@{}&quot;</tt>. </p>
<p> Calling <tt>&quot;keys&quot;</tt> or <tt>&quot;values&quot;</tt> directly on a reference gives a substantial performance improvement over explicit dereferencing. </p>
<p> For <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt>, <tt>&quot;each&quot;</tt>, when overloaded dereferencing is present, the overloaded dereference is used instead of dereferencing the underlying reftype. Warnings are issued about assumptions made in the following three ambiguous cases: </p>
<pre><code>
(a) If both % {} and @{} overloading exists, %
{
}
is used(b) If %
{
}
overloading exists on a blessed arrayref, %
{
}
is used(c) If @{} overloading exists on a blessed hashref, @{} is used
</code></pre>
<h3>y///r</h3>
<p> The <tt>&quot;/r&quot;</tt> flag, which was added to <tt>&quot;s///&quot;</tt> in 5.13.2, has been extended to the <tt>&quot;y///&quot;</tt> operator. </p>
<p> It causes it to perform the substitution on a <i>copy</i> of its operand, returning that copy instead of a character count.</p>
<h3>New global variable ${^GLOBAL_PHASE}</h3>
<p> A new global variable, <tt>&quot;${^GLOBAL_PHASE}&quot;</tt>, has been added to allow introspection of the current phase of the perl interpreter. It&#8217;s explained in detail in &#8220;${^GLOBAL_PHASE}&#8221; in perlvar and &#8220;<font SIZE="-1">BEGIN</font>, <font SIZE="-1">UNITCHECK</font>, <font SIZE="-1">CHECK</font>, <font SIZE="-1">INIT</font> and <font SIZE="-1">END</font>&#8221; in perlmod.</p>
<h3>Unicode Version 6.0 is now supported (mostly)</h3>
<p> Perl comes with the Unicode 6.0 data base updated with Corrigendum #8 &lt;<a rel="nofollow" href="http://www.unicode.org/versions/corrigendum8.html">http://www.unicode.org/versions/corrigendum8.html</a>&gt;, with one exception noted below. See &lt;<a rel="nofollow" href="http://unicode.org/versions/Unicode6.0.0">http://unicode.org/versions/Unicode6.0.0</a>&gt; for details on the new release. Perl does not support any Unicode provisional properties, including the new ones for this release, but their database files are packaged with Perl. </p>
<p> Unicode 6.0 has chosen to use the name <tt>&quot;BELL&quot;</tt> for the character at U+1F514, which is a symbol that looks like a bell, and used in Japanese cell phones. This conflicts with the long-standing Perl usage of having <tt>&quot;BELL&quot;</tt> mean the <font SIZE="-1">ASCII</font> <tt>&quot;BEL&quot;</tt> character, U+0007. In Perl 5.14, <tt>&quot;\N{BELL}&quot;</tt> will continue to mean U+0007, but its use will generate a deprecated warning message, unless such warnings are turned off. The new name for U+0007 in Perl will be <tt>&quot;ALERT&quot;</tt>, which corresponds nicely with the existing shorthand sequence for it, <tt>&quot;&quot;</tt>. <tt>&quot;\N{BEL}&quot;</tt> will mean U+0007, with no warning given. The character at U+1F514 will not have a name in 5.14, but can be referred to by <tt>&quot;\N{U+1F514}&quot;</tt>. The plan is that in Perl 5.16, <tt>&quot;\N{BELL}&quot;</tt> will refer to U+1F514, and so all code that uses <tt>&quot;\N{BELL}&quot;</tt> should convert by then to using <tt>&quot;\N{ALERT}&quot;</tt>, <tt>&quot;\N{BEL}&quot;</tt>, or <tt>&quot;&quot;</tt> instead.</p>
<h3>Improved support for custom OPs</h3>
<p> Custom ops can now be registered with the new <tt>&quot;custom_op_register&quot;</tt> C function and the <tt>&quot;XOP&quot;</tt> structure. This will make it easier to add new properties of custom ops in the future. Two new properties have been added already, <tt>&quot;xop_class&quot;</tt> and <tt>&quot;xop_peep&quot;</tt>. </p>
<p> <tt>&quot;xop_class&quot;</tt> is one of the OA_*OP constants, and allows B and other introspection mechanisms to work with custom ops that aren&#8217;t BASEOPs. <tt>&quot;xop_peep&quot;</tt> is a pointer to a function that will be called for ops of this type from <tt>&quot;Perl_rpeep&quot;</tt>. </p>
<p> See &#8220;Custom Operators&#8221; in perlguts and &#8220;Custom Operators&#8221; in perlapi for more detail. </p>
<p> The old <tt>&quot;PL_custom_op_names&quot;</tt>/<tt>&quot;PL_custom_op_descs&quot;</tt> interface is still supported but discouraged.</p>
<h2>Incompatible Changes</h2>
<h3>Dereferencing typeglobs</h3>
<p> If you assign a typeglob to a scalar variable: </p>
<pre>
    $glob = *foo;
</pre>
<p> the glob that is copied to <tt>$glob</tt> is marked with a special flag indicating that the glob is just a copy. This allows subsequent assignments to <tt>$glob</tt> to overwrite the glob. The original glob, however, is immutable. </p>
<p> Many Perl operators did not distinguish between these two types of globs. This would result in strange behaviour in edge cases: <tt>&quot;untie $scalar&quot;</tt> would do nothing if the last thing assigned to the scalar was a glob (because it treated it as <tt>&quot;untie *$scalar&quot;</tt>, which unties a handle). Assignment to a glob slot (e.g., <tt>&quot;(*$glob) = \@some_array&quot;</tt>) would simply assign <tt>&quot;\@some_array&quot;</tt> to <tt>$glob</tt>. </p>
<p> To fix this, the <tt>&quot;*{}&quot;</tt> operator (including the <tt>*foo</tt> and <tt>*$foo</tt> forms) has been modified to make a new immutable glob if its operand is a glob copy. Various operators that make a distinction between globs and scalars have been modified to treat only immutable globs as globs. </p>
<p> This causes an incompatible change in code that assigns a glob to the return value of <tt>&quot;*{}&quot;</tt> when that operator was passed a glob copy. Take the following code, for instance: </p>
<pre>
    $glob = *foo;
    *$glob = *bar;
</pre>
<p> The <tt>*$glob</tt> on the second line returns a new immutable glob. That new glob is made an alias to <tt>*bar</tt>. Then it is discarded. So the second assignment has no effect. </p>
<p> It also means that <tt>&quot;tie $handle&quot;</tt> will now tie <tt>$handle</tt> as a scalar, even if it has had a glob assigned to it. </p>
<p> The upside to this incompatible change is that bugs [perl #77496] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77496">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77496</a>&gt;, [perl #77502] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77502">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77502</a>&gt;, [perl #77508] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77508">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77508</a>&gt;, [perl #77688] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77688">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77688</a>&gt;, and [perl #77812] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77812">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77812</a>&gt;, and maybe others, too, have been fixed. </p>
<p> See &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77810">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77810</a>&gt; for even more detail.</p>
<h3>Clearing stashes</h3>
<p> Stash list assignment <tt>&quot;%foo:: = ()&quot;</tt> used to make the stash anonymous temporarily while it was being emptied. Consequently, any of its subroutines referenced elsewhere would become anonymous (showing up as &#8220;(unknown)&#8221; in <tt>&quot;caller&quot;</tt>). Now they retain their package names, such that <tt>&quot;caller&quot;</tt> will return the original sub name if there is still a reference to its typeglob, or &#8220;foo::__ANON__&#8221; otherwise [perl #79208] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=79208">http://rt.perl.org/rt3/Public/Bug/Display.html?id=79208</a>&gt;.</p>
<h2>Deprecations</h2>
<h3>\N{BELL} is deprecated</h3>
<p> This is because Unicode is using that name for a different character. See &#8220;Unicode Version 6.0 is now supported (mostly)&#8221; for more explanation.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> When an object has many weak references to it, freeing that object can under some some circumstances take O(N^2) time to free (where N is the number of references). The number of circumstances has been reduced. [perl #75254] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75254">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75254</a>&gt;.</dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> The following modules were added by the <tt>&quot;Unicode::Collate&quot;</tt> upgrade from 0.63 to 0.67. See below for details. </p>
<p> <tt>&quot;Unicode::Collate::CJK::Big5&quot;</tt> </p>
<p> <tt>&quot;Unicode::Collate::CJK::GB2312&quot;</tt> </p>
<p> <tt>&quot;Unicode::Collate::CJK::JISX0208&quot;</tt> </p>
<p> <tt>&quot;Unicode::Collate::CJK::Korean&quot;</tt> </p>
<p> <tt>&quot;Unicode::Collate::CJK::Pinyin&quot;</tt> </p>
<p> <tt>&quot;Unicode::Collate::CJK::Stroke&quot;</tt></dl>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Archive::Extract&quot;</tt> has been upgraded from 0.44 to 0.46 </p>
<p> Resolves an issue with NetBSD-current and its new unzip executable.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Archive::Tar&quot;</tt> has been upgraded from 1.68 to 1.72 </p>
<p> This adds the ptargrep utility for using regular expressions against the contents of files in a tar archive.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B&quot;</tt> has been upgraded from 1.24 to 1.26. </p>
<p> It no longer crashes when taking apart a <tt>&quot;y///&quot;</tt> containing characters outside the octet range or compiled in a <tt>&quot;use utf8&quot;</tt> scope. </p>
<p> The size of the shared object has been reduced by about 40%, with no reduction in functionality.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Deparse&quot;</tt> has been upgraded from 0.99 to 1.01. </p>
<p> It fixes deparsing of <tt>&quot;our&quot;</tt> followed by a variable with funny characters (as permitted under the <tt>&quot;utf8&quot;</tt> pragma) [perl #33752] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=33752">http://rt.perl.org/rt3/Public/Bug/Display.html?id=33752</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CGI&quot;</tt> has been upgraded from 3.49 to 3.50 </p>
<p> This provides the following security fixes: the <font SIZE="-1">MIME</font> boundary in multipart_init is now random and improvements to the handling of newlines embedded in header values. </p>
<p> The documentation for <i>param_fetch()</i> has been corrected and clarified.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN&quot;</tt> has been upgraded from 1.94_61 to 1.94_62</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPANPLUS&quot;</tt> has been upgraded from 0.9007 to 0.9010 </p>
<p> Fixes for the SQLite source engine and resolving of issues with the testsuite when run under local::lib and/or cpanminus</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPANPLUS::Dist::Build&quot;</tt> has been upgraded from 0.48 to 0.50</p>
<dt>&bull;</p>
<dd> <tt>&quot;Data::Dumper&quot;</tt> has been upgraded from 2.129 to 2.130_01.</p>
<dt>&bull;</p>
<dd> <tt>&quot;DynaLoader&quot;</tt> has been upgraded from 1.10 to 1.11. </p>
<p> It fixes a buffer overflow when passed a very long file name.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Constant&quot;</tt> has been upgraded from 0.22 to 0.23. </p>
<p> The <tt>&quot;AUTOLOAD&quot;</tt> helper code generated by <tt>&quot;ExtUtils::Constant::ProxySubs&quot;</tt> can now <tt>&quot;croak&quot;</tt> for missing constants, or generate a complete <tt>&quot;AUTOLOAD&quot;</tt> subroutine in <font SIZE="-1">XS</font>, allowing simplification of many modules that use it. (<tt>&quot;Fcntl&quot;</tt>, <tt>&quot;File::Glob&quot;</tt>, <tt>&quot;GDBM_File&quot;</tt>, <tt>&quot;I18N::Langinfo&quot;</tt>, <tt>&quot;POSIX&quot;</tt>, <tt>&quot;Socket&quot;</tt>) </p>
<p> <tt>&quot;ExtUtils::Constant::ProxySubs&quot;</tt> can now optionally push the names of all constants onto the package&#8217;s C{@EXPORT_OK}. This has been used to replace less space-efficient code in <tt>&quot;B&quot;</tt>, helping considerably shrink the size of its shared object.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Fcntl&quot;</tt> has been upgraded from 1.09 to 1.10.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Fetch&quot;</tt> has been upgraded from 0.24 to 0.28 </p>
<p> <tt>&quot;HTTP::Lite&quot;</tt> is now supported for &#8216;http&#8217; scheme. </p>
<p> The <tt>&quot;fetch&quot;</tt> utility is supported on FreeBSD, NetBSD and Dragonfly <font SIZE="-1">BSD</font> for the <tt>&quot;http&quot;</tt> and <tt>&quot;ftp&quot;</tt> schemes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Glob&quot;</tt> has been upgraded from 1.09 to 1.10.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::stat&quot;</tt> has been upgraded from 1.03 to 1.04. </p>
<p> The <tt>&quot;-x&quot;</tt> and <tt>&quot;-X&quot;</tt> file test operators now work correctly under the root user.</p>
<dt>&bull;</p>
<dd> <tt>&quot;GDBM_File&quot;</tt> has been upgraded from 1.11 to 1.12. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Hash::Util&quot;</tt> has been upgraded from 0.09 to 0.10.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Hash::Util::FieldHash&quot;</tt> has been upgraded from 1.05 to 1.06.</p>
<dt>&bull;</p>
<dd> <tt>&quot;I18N::Langinfo&quot;</tt> has been upgraded from 0.06 to 0.07.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Maketext&quot;</tt> has been upgraded from 1.16 to 1.17.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt&quot;</tt> has been upgraded from 1.97 to 1.99_01.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigRat&quot;</tt> has been upgraded from 0.26 to 0.26_01</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt::FastCalc&quot;</tt> has been upgraded from 0.22 to 0.24_01.</p>
<dt>&bull;</p>
<dd> <tt>&quot;MIME::Base64&quot;</tt> has been upgraded from 3.09 to 3.10 </p>
<p> Includes new functions to calculate the length of encoded and decoded base64 strings.</p>
<dt>&bull;</p>
<dd> <tt>&quot;mro&quot;</tt> has been upgraded from 1.04 to 1.05.</p>
<dt>&bull;</p>
<dd> <tt>&quot;NDBM_File&quot;</tt> has been upgraded from 1.09 to 1.10. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ODBM_File&quot;</tt> has been upgraded from 1.08 to 1.09. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Opcode&quot;</tt> has been upgraded from 1.16 to 1.17.</p>
<dt>&bull;</p>
<dd> <tt>&quot;parent&quot;</tt> has been upgraded from 0.223 to 0.224</p>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Simple&quot;</tt> has been upgraded from 3.14 to 3.15 </p>
<p> Includes various fixes to <tt>&quot;HTML&quot;</tt> and <tt>&quot;XHTML&quot;</tt> handling.</p>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX&quot;</tt> has been upgraded from 1.21 to 1.22.</p>
<dt>&bull;</p>
<dd> <tt>&quot;re&quot;</tt> has been upgraded from 0.13 to 0.14, for the sake of the new <tt>&quot;use re &quot;/flags&quot;&quot;</tt> pragma.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Safe&quot;</tt> has been upgraded from 2.28 to 2.29. </p>
<p> It adds <tt>&amp;version::vxs::VCMP</tt> to the default share.</p>
<dt>&bull;</p>
<dd> <tt>&quot;SDBM_File&quot;</tt> has been upgraded from 1.07 to 1.08.</p>
<dt>&bull;</p>
<dd> <tt>&quot;SelfLoader&quot;</tt> has been upgraded from 1.17 to 1.18. </p>
<p> It now works in taint mode [perl #72062] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72062">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72062</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Socket&quot;</tt> has been upgraded from 1.90 to 1.91.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Storable&quot;</tt> has been upgraded from 2.22 to 2.24 </p>
<p> Includes performance improvement for overloaded classes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Sys::Hostname&quot;</tt> has been upgraded from 1.13 to 1.14.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate&quot;</tt> has been upgraded from 0.63 to 0.67 </p>
<p> This release newly adds locales <tt>&quot;ja&quot;</tt> <tt>&quot;ko&quot;</tt> and <tt>&quot;zh&quot;</tt> and its variants ( <tt>&quot;zh__big5han&quot;</tt>, <tt>&quot;zh__gb2312han&quot;</tt>, <tt>&quot;zh__pinyin&quot;</tt>, <tt>&quot;zh__stroke&quot;</tt> ). </p>
<p> Supported UCA_Version 22 for Unicode 6.0.0. </p>
<p> The following modules have been added: </p>
<p> <tt>&quot;Unicode::Collate::CJK::Big5&quot;</tt> for <tt>&quot;zh__big5han&quot;</tt> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s big5han ordering. </p>
<p> <tt>&quot;Unicode::Collate::CJK::GB2312&quot;</tt> for <tt>&quot;zh__gb2312han&quot;</tt> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s gb2312han ordering. </p>
<p> <tt>&quot;Unicode::Collate::CJK::JISX0208&quot;</tt> which makes tailoring of 6355 kanji (<font SIZE="-1">CJK</font> Unified Ideographs) in the <font SIZE="-1">JIS</font> X 0208 order. </p>
<p> <tt>&quot;Unicode::Collate::CJK::Korean&quot;</tt> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s Korean ordering. </p>
<p> <tt>&quot;Unicode::Collate::CJK::Pinyin&quot;</tt> for <tt>&quot;zh__pinyin&quot;</tt> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s pinyin ordering. </p>
<p> <tt>&quot;Unicode::Collate::CJK::Stroke&quot;</tt> for <tt>&quot;zh__stroke&quot;</tt> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s stroke ordering.</dl>
<h2>Documentation</h2>
<p> perlvar reorders the variables and groups them by topic. Each variable introduced after Perl 5.000 notes the first version in which it is available. perlvar also has a new section for deprecated variables to note when they were removed.</p>
<h3>New Documentation</h3>
<p> <i>perlpodstyle</i> </p>
<p> New style guide for <font SIZE="-1">POD</font> documentation, split mostly from the <font SIZE="-1">NOTES</font> section of the pod2man man page. </p>
<p> ( This was added to <tt>&quot;v5.13.6&quot;</tt> but was not documented with that release ).</p>
<h3>Changes to Existing Documentation</h3>
<dl>
<dt>&bull;</p>
<dd> Array and hash slices in scalar context are now documented in perldata.</p>
<dt>&bull;</p>
<dd> perlform and perllocale have been corrected to state that <tt>&quot;use locale&quot;</tt> affects formats.</dl>
<h2>Diagnostics</h2>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> &#8220;Using !~ with <tt>%s</tt> doesn&#8217;t make sense&#8221;: This message was actually added in 5.13.2, but was omitted from perldelta. It now applies also to the <tt>&quot;y///&quot;</tt> operator, and has been documented.</dl>
<h2>Utility Changes</h2>
<p> <i>ptargrep</i></p>
<dl>
<dt>&bull;</p>
<dd> ptargrep is a utility to apply pattern matching to the contents of files in a tar archive. It comes with <tt>&quot;Archive::Tar&quot;</tt>.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> The new <i>t/mro/isa_aliases.t</i> has been added, which tests that <tt>&quot;*Foo::ISA = *Bar::ISA&quot;</tt> works properly.</p>
<dt>&bull;</p>
<dd> <i>t/mro/isarev.t</i> has been added, which tests that <tt>&quot;PL_isarev&quot;</tt> (accessible at the Perl level via <tt>&quot;mro::get_isarev&quot;</tt>) is updated properly.</p>
<dt>&bull;</p>
<dd> <i>t/run/switchd-78586.t</i> has been added, which tests that [perl #78586] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78586">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78586</a>&gt; has been fixed (related to line numbers in the debugger).</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Windows</p>
<dd> Directory handles are now properly cloned when threads are created. In perl 5.13.6, child threads simply stopped inheriting directory handles. In previous versions, threads would share handles, resulting in crashes. </p>
<p> Support for building with Visual C<font SIZE="-2">++</font> 2010 is now underway, but is not yet complete. See <i></i><font SIZE="-1"><i>README</i></font><i>.win32</i> for more details.</p>
<dt><font SIZE="-1">VMS</font></p>
<dd> Record-oriented files (record format variable or variable with fixed control) opened for write by the perlio layer will now be line buffered to prevent the introduction of spurious line breaks whenever the perlio buffer fills up.</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;lex_start&quot;</tt> has been added to the <font SIZE="-1">API</font>, but is considered experimental.</p>
<dt>&bull;</p>
<dd> A new <tt>&quot;parse_block&quot;</tt> function has been added to the <font SIZE="-1">API</font> [perl #78222] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222</a>&gt;.</p>
<dt>&bull;</p>
<dd> A new, experimental <font SIZE="-1">API</font> has been added for accessing the internal structure that Perl uses for <tt>&quot;%^H&quot;</tt>. See the functions beginning with <tt>&quot;cophh_&quot;</tt> in perlapi.</p>
<dt>&bull;</p>
<dd> A stash can now have a list of effective names in addition to its usual name. The first effective name can be accessed via the <tt>&quot;HvENAME&quot;</tt> macro, which is now the recommended name to use in <font SIZE="-1">MRO</font> linearisations (<tt>&quot;HvNAME&quot;</tt> being a fallback if there is no <tt>&quot;HvENAME&quot;</tt>). </p>
<p> These names are added and deleted via <tt>&quot;hv_ename_add&quot;</tt> and <tt>&quot;hv_ename_delete&quot;</tt>. These two functions are <i>not</i> part of the <font SIZE="-1">API</font>.</p>
<dt>&bull;</p>
<dd> The way the parser handles labels has been cleaned up and refactored. As a result, the <tt>&quot;newFOROP()&quot;</tt> constructor function no longer takes a parameter stating what label is to go in the state op.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;newWHILEOP()&quot;</tt> and <tt>&quot;newFOROP()&quot;</tt> functions no longer accept a line number as a parameter.</p>
<dt>&bull;</p>
<dd> A new <tt>&quot;parse_barestmt()&quot;</tt> function has been added, for parsing a statement without a label.</p>
<dt>&bull;</p>
<dd> A new <tt>&quot;parse_label()&quot;</tt> function has been added, that parses a statement label, separate from statements.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;CvSTASH()&quot;</tt> macro can now only be used as an rvalue. <tt>&quot;CvSTASH_set()&quot;</tt> has been added to replace assignment to <tt>&quot;CvSTASH()&quot;</tt>. This is to ensure that backreferences are handled properly. These macros are not part of the <font SIZE="-1">API</font>.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;op_scope()&quot;</tt> and <tt>&quot;op_lvalue()&quot;</tt> functions have been added to the <font SIZE="-1">API</font>, but are considered experimental.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;parse_stmt&quot;</tt> C function added in earlier in the 5.13.x series has been fixed to work with statements ending with <tt>&quot;}&quot;</tt> [perl #78222] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78222</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;parse_fullstmt&quot;</tt> C function added in 5.13.5 has been fixed to work when called while an expression is being parsed.</p>
<dt>&bull;</p>
<dd> Characters in the Latin-1 non-ASCII range (0x80 to 0xFF) used not to match themselves if the string happened to be UTF8-encoded internally, the regular expression was not, and the character in the regular expression was inside a repeated group (e.g., <tt>&quot;Encode::decode_utf8(&quot;\303\200&quot;) =~ /(�)+/&quot;</tt>) [perl #78464] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78464">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78464</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;(?d)&quot;</tt> regular expression construct now overrides a previous <tt>&quot;(?u)&quot;</tt> or <tt>&quot;use feature &quot;unicode_string&quot;&quot;</tt> [perl #78508] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78508">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78508</a>&gt;.</p>
<dt>&bull;</p>
<dd> A memory leak in <tt>&quot;do &quot;file&quot;&quot;</tt>, introduced in perl 5.13.6, has been fixed [perl #78488] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78488">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78488</a>&gt;.</p>
<dt>&bull;</p>
<dd> Various bugs related to typeglob dereferencing have been fixed. See &#8220;Dereferencing typeglobs&#8221;, above.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;SvPVbyte&quot;</tt> function available to <font SIZE="-1">XS</font> modules now calls magic before downgrading the <font SIZE="-1">SV</font>, to avoid warnings about wide characters [perl #72398] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72398">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72398</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;=&quot;</tt> operator used to ignore magic (e.g., tie methods) on its right-hand side if the scalar happened to hold a typeglob. This could happen if a typeglob was the last thing returned from or assigned to a tied scalar [perl #77498] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77498">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77498</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;sprintf&quot;</tt> was ignoring locales when called with constant arguments [perl #78632] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78632">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78632</a>&gt;.</p>
<dt>&bull;</p>
<dd> A non-ASCII character in the Latin-1 range could match both a Posix class, such as <tt>&quot;[[:alnum:]]&quot;</tt>, and its inverse <tt>&quot;[[:^alnum:]]&quot;</tt>. This is now fixed for regular expressions compiled under the <tt>&quot;u&quot;</tt> modifier. See &quot;<tt>&quot;use feature &quot;unicode_strings&quot;&quot;</tt> now applies to more regex matching&quot;. [perl #18281] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=18281">http://rt.perl.org/rt3/Public/Bug/Display.html?id=18281</a>&gt;.</p>
<dt>&bull;</p>
<dd> Concatenating long strings under <tt>&quot;use encoding&quot;</tt> no longer causes perl to crash [perl #78674] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78674">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78674</a>&gt;.</p>
<dt>&bull;</p>
<dd> Typeglob assignments would crash if the glob&#8217;s stash no longer existed, so long as the glob assigned to was named &#8216;<font SIZE="-1">ISA</font>&#8216; or the glob on either side of the assignment contained a subroutine.</p>
<dt>&bull;</p>
<dd> Calling <tt>&quot;-&gt;import&quot;</tt> on a class lacking an import method could corrupt the stack, resulting in strange behaviour. For instance, </p>
<pre>
  push @a, &quot;foo&quot;, $b = bar-&gt;import;
</pre>
<p> would assign &#8216;foo&#8217; to <tt>$b</tt> [perl #63790] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=63790">http://rt.perl.org/rt3/Public/Bug/Display.html?id=63790</a>&gt;.</p>
<dt>&bull;</p>
<dd> Creating an alias to a package when that package had been detached from the symbol table would result in corrupted isa caches [perl #77358] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77358">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77358</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;.=&quot;</tt> followed by <tt>&quot;&lt;&gt;&quot;</tt> or <tt>&quot;readline&quot;</tt> would leak memory if <tt>$/</tt> contained characters beyond the octet range and the scalar assigned to happened to be encoded as <font SIZE="-1">UTF8</font> internally [perl #72246] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72246">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72246</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;recv&quot;</tt> function could crash when called with the <font SIZE="-1">MSG_TRUNC</font> flag [perl #75082] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75082">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75082</a>&gt;.</p>
<dt>&bull;</p>
<dd> Evaluating a simple glob (like <tt>*a</tt>) was calling get-magic on the glob, even when its contents were not being used [perl #78580] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78580">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78580</a>&gt;. </p>
<p> This bug was introduced in 5.13.2 and did not affect earlier perl versions.</p>
<dt>&bull;</p>
<dd> Matching a Unicode character against an alternation containing characters that happened to match continuation bytes in the former&#8217;s <font SIZE="-1">UTF8</font> representation (<tt>&quot;qq{
