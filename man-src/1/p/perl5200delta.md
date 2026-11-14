---
title: "perl5200delta(1)"
name: "perl5200delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5200delta/"
description: "perl5200delta – what is new for perl v5.20.0"
---

<h2 class="name">NAME</h2>
<p> perl5200delta &#8211; what is new for perl v5.20.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.18.0 release and the 5.20.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.16.0, first read perl5180delta, which describes differences between 5.16.0 and 5.18.0.</p>
<h2>Core Enhancements</h2>
<h3>Experimental Subroutine signatures</h3>
<p> Declarative syntax to unwrap argument list into lexical variables. <tt>&quot;sub foo ($a,$b) {...}&quot;</tt> checks the number of arguments and puts the arguments into lexical variables. Signatures are not equivalent to the existing idiom of <tt>&quot;sub foo { my($a,$b) = @_; ... }&quot;</tt>. Signatures are only available by enabling a non-default feature, and generate warnings about being experimental. The syntactic clash with prototypes is managed by disabling the short prototype syntax when signatures are enabled. </p>
<p> See &#8220;Signatures&#8221; in perlsub for details.</p>
<h3>subs now take a prototype attribute</h3>
<p> When declaring or defining a <tt>&quot;sub&quot;</tt>, the prototype can now be specified inside of a <tt>&quot;prototype&quot;</tt> attribute instead of in parens following the name. </p>
<p> For example, <tt>&quot;sub foo($$){}&quot;</tt> could be rewritten as <tt>&quot;sub foo : prototype($$){}&quot;</tt>.</p>
<h3>More consistent prototype parsing</h3>
<p> Multiple semicolons in subroutine prototypes have long been tolerated and treated as a single semicolon. There was one case where this did not happen. A subroutine whose prototype begins with &#8220;*&#8221; or &#8220;;*&#8221; can affect whether a bareword is considered a method name or sub call. This now applies also to &#8220;;;;*&#8221;. </p>
<p> Whitespace has long been allowed inside subroutine prototypes, so <tt>&quot;sub( $ $ )&quot;</tt> is equivalent to <tt>&quot;sub($$)&quot;</tt>, but until now it was stripped when the subroutine was parsed. Hence, whitespace was <i>not</i> allowed in prototypes set by <tt>&quot;Scalar::Util::set_prototype&quot;</tt>. Now it is permitted, and the parser no longer strips whitespace. This means <tt>&quot;prototype &amp;mysub&quot;</tt> returns the original prototype, whitespace and all.</p>
<h3>rand now uses a consistent random number generator</h3>
<p> Previously perl would use a platform specific random number generator, varying between the libc <code>rand()</code>, <code>random()</code> or <code>drand48()</code>. </p>
<p> This meant that the quality of perl&#8217;s random numbers would vary from platform to platform, from the 15 bits of <code>rand()</code> on Windows to 48-bits on <font SIZE="-1">POSIX</font> platforms such as Linux with <code>drand48()</code>. </p>
<p> Perl now uses its own internal <code>drand48()</code> implementation on all platforms. This does not make perl&#8217;s <tt>&quot;rand&quot;</tt> cryptographically secure. [perl #115928]</p>
<h3>New slice syntax</h3>
<p> The new <tt>%hash{...}</tt> and <tt>%array[...]</tt> syntax returns a list of key/value (or index/value) pairs. See &#8220;Key/Value Hash Slices&#8221; in perldata.</p>
<h3>Experimental Postfix Dereferencing</h3>
<p> When the <tt>&quot;postderef&quot;</tt> feature is in effect, the following syntactical equivalencies are set up: </p>
<pre><code>
$sref-&gt;$ *;
#same as ${$sref } #interpolates $aref-&gt;@ *;
#same as @{$aref } #interpolates $href-&gt;% *;
#same as % {$href } $cref-&gt;&amp;*;
#same as &amp;{$cref } $gref-&gt;**;
#same as *{$gref } $aref-&gt;$ #*;
#same as $ #{$aref } $gref-&gt;*{$slot };
#same as *{$gref } {$slot } $aref-&gt;@[...];
#same as @$aref[...] #interpolates $href-&gt;@{... };
#same as @$href{... } #interpolates $aref-&gt;% [...];
#same as % $aref[...] $href-&gt;% {... };
#same as % $href
{
    ...
}
</code></pre>
<p> Those marked as interpolating only interpolate if the associated <tt>&quot;postderef_qq&quot;</tt> feature is also enabled. This feature is <code>experimental</code> and will trigger <tt>&quot;experimental::postderef&quot;</tt>-category warnings when used, unless they are suppressed. </p>
<p> For more information, consult the Postfix Dereference Syntax section of perlref.</p>
<h3>Unicode 6.3 now supported</h3>
<p> Perl now supports and is shipped with Unicode 6.3 (though Perl may be recompiled with any previous Unicode release as well). A detailed list of Unicode 6.3 changes is at &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode6.3.0/">http://www.unicode.org/versions/Unicode6.3.0/</a>&gt;.</p>
<h3>New \p{Unicode} regular expression pattern property</h3>
<p> This is a synonym for <tt>&quot;\p{Any}&quot;</tt> and matches the set of Unicode-defined code points 0 &#8211; 0x10FFFF.</p>
<h3>Better 64-bit support</h3>
<p> On 64-bit platforms, the internal array functions now use 64-bit offsets, allowing Perl arrays to hold more than 2**31 elements, if you have the memory available. </p>
<p> The regular expression engine now supports strings longer than 2**31 characters. [perl #112790, #116907] </p>
<p> The functions PerlIO_get_bufsiz, PerlIO_get_cnt, PerlIO_set_cnt and PerlIO_set_ptrcnt now have SSize_t, rather than int, return values and parameters.</p>
<h3>use locale now works on <font SIZE="-1">UTF-8</font> locales</h3>
<p> Until this release, only single-byte locales, such as the <font SIZE="-1">ISO 8859</font> series were supported. Now, the increasingly common multi-byte <font SIZE="-1">UTF-8</font> locales are also supported. A <font SIZE="-1">UTF-8</font> locale is one in which the character set is Unicode and the encoding is <font SIZE="-1">UTF-8.</font> The <font SIZE="-1">POSIX</font> <tt>&quot;LC_CTYPE&quot;</tt> category operations (case changing (like <tt>&quot;lc()&quot;</tt>, <tt>&quot;
