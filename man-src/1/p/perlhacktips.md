---
title: "perlhacktips(1)"
name: "perlhacktips"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhacktips/"
description: "perlhacktips – Tips for Perl core C code hacking"
---

<h2 class="name">NAME</h2>
<p> perlhacktips &#8211; Tips for Perl core C code hacking </p>
<h2>DESCRIPTION</h2>
<p> This document will help you learn the best way to go about hacking on the Perl core C code. It covers common problems, debugging, profiling, and more. </p>
<p> If you haven&#8217;t read perlhack and perlhacktut yet, you might want to do that first.</p>
<h2>COMMON PROBLEMS</h2>
<p> Perl source plays by <font SIZE="-1">ANSI C89</font> rules: no C99 (or C<font SIZE="-2">++</font>) extensions. You don&#8217;t care about some particular platform having broken Perl? I hear there is still a strong demand for J2EE programmers.</p>
<h3>Perl environment problems</h3>
<dl>
<dt>&bull;</p>
<dd> Not compiling with threading </p>
<p> Compiling with threading (-Duseithreads) completely rewrites the function prototypes of Perl. You better try your changes with that. Related to this is the difference between &#8220;Perl_-less&#8221; and &#8220;Perl_-ly&#8221; APIs, for example: </p>
<pre><code>
Perl_sv_setiv(aTHX_...);
sv_setiv(...);
</code></pre>
<p> The first one explicitly passes in the context, which is needed for e.g. threaded builds. The second one does that implicitly; do not get them mixed. If you are not passing in a aTHX_, you will need to do a dTHX (or a dVAR) as the first thing in the function. </p>
<p> See &#8220;How multiple interpreters and concurrency are supported&#8221; in perlguts for further discussion about context.</p>
<dt>&bull;</p>
<dd> Not compiling with -DDEBUGGING </p>
<p> The <font SIZE="-1">DEBUGGING</font> define exposes more code to the compiler, therefore more ways for things to go wrong. You should try it.</p>
<dt>&bull;</p>
<dd> Introducing (non-read-only) globals </p>
<p> Do not introduce any modifiable globals, truly global or file static. They are bad form and complicate multithreading and other forms of concurrency. The right way is to introduce them as new interpreter variables, see <i>intrpvar.h</i> (at the very end for binary compatibility). </p>
<p> Introducing read-only (const) globals is okay, as long as you verify with e.g. <tt>&quot;nm libperl.a|egrep -v ' [TURtr] '&quot;</tt> (if your <tt>&quot;nm&quot;</tt> has BSD-style output) that the data you added really is read-only. (If it is, it shouldn&#8217;t show up in the output of that command.) </p>
<p> If you want to have static strings, make them constant: </p>
<p>static const char etc[] = &#8220;&#8230;&#8221;;</p>
<p> If you want to have arrays of constant strings, note carefully the right combination of <tt>&quot;const&quot;</tt>s: </p>
<p>static const char *const yippee[] =<br />
    {&#8220;hi&#8221;, &#8220;ho&#8221;, &#8220;silver&#8221;};</p>
<p> There is a way to completely hide any modifiable globals (they are all moved to heap), the compilation setting <tt>&quot;-DPERL_GLOBAL_STRUCT_PRIVATE&quot;</tt>. It is not normally used, but can be used for testing, read more about it in &#8220;Background and <font SIZE="-1">PERL_IMPLICIT_CONTEXT&#8221;</font> in perlguts.</p>
<dt>&bull;</p>
<dd> Not exporting your new function </p>
<p> Some platforms (Win32, <font SIZE="-1">AIX, VMS, OS/2,</font> to name a few) require any function that is part of the public <font SIZE="-1">API</font> (the shared Perl library) to be explicitly marked as exported. See the discussion about <i>embed.pl</i> in perlguts.</p>
<dt>&bull;</p>
<dd> Exporting your new function </p>
<p> The new shiny result of either genuine new functionality or your arduous refactoring is now ready and correctly exported. So what could possibly go wrong? </p>
<p> Maybe simply that your function did not need to be exported in the first place. Perl has a long and not so glorious history of exporting functions that it should not have. </p>
<p> If the function is used only inside one source code file, make it static. See the discussion about <i>embed.pl</i> in perlguts. </p>
<p> If the function is used across several files, but intended only for Perl&#8217;s internal use (and this should be the common case), do not export it to the public <font SIZE="-1">API.</font> See the discussion about <i>embed.pl</i> in perlguts.</dl>
<h3>Portability problems</h3>
<p> The following are common causes of compilation and/or execution failures, not common to Perl as such. The C <font SIZE="-1">FAQ</font> is good bedtime reading. Please test your changes with as many C compilers and platforms as possible; we will, anyway, and it&#8217;s nice to save oneself from public embarrassment. </p>
<p> If using gcc, you can add the <tt>&quot;-std=c89&quot;</tt> option which will hopefully catch most of these unportabilities. (However it might also catch incompatibilities in your system&#8217;s header files.) </p>
<p> Use the Configure <tt>&quot;-Dgccansipedantic&quot;</tt> flag to enable the gcc <tt>&quot;-ansi -pedantic&quot;</tt> flags which enforce stricter <font SIZE="-1">ANSI</font> rules. </p>
<p> If using the <tt>&quot;gcc -Wall&quot;</tt> note that not all the possible warnings (like <tt>&quot;-Wuninitialized&quot;</tt>) are given unless you also compile with <tt>&quot;-O&quot;</tt>. </p>
<p> Note that if using gcc, starting from Perl 5.9.5 the Perl core source code files (the ones at the top level of the source code distribution, but not e.g. the extensions under ext/) are automatically compiled with as many as possible of the <tt>&quot;-std=c89&quot;</tt>, <tt>&quot;-ansi&quot;</tt>, <tt>&quot;-pedantic&quot;</tt>, and a selection of <tt>&quot;-W&quot;</tt> flags (see cflags.SH). </p>
<p> Also study perlport carefully to avoid any bad assumptions about the operating system, filesystems, character set, and so forth. </p>
<p> You may once in a while try a &#8220;make microperl&#8221; to see whether we can still compile Perl with just the bare minimum of interfaces. (See <font SIZE="-1">README</font>.micro.) </p>
<p> Do not assume an operating system indicates a certain compiler.</p>
<dl>
<dt>&bull;</p>
<dd> Casting pointers to integers or casting integers to pointers </p>
<pre>
    void castaway(U8* p)
    {
      IV i = p;
</pre>
<p> or </p>
<p>void castaway(U8 *p)<br />
{<br />
    IV i = (IV)p;</p>
<p> Both are bad, and broken, and unportable. Use the <font SIZE="-1"><code>PTR2IV</code></font><code>()</code> macro that does it right. (Likewise, there are <font SIZE="-1"><code>PTR2UV</code></font><code>()</code>, <font SIZE="-1"><code>PTR2NV</code></font><code>()</code>, <font SIZE="-1"><code>INT2PTR</code></font><code>()</code>, and <font SIZE="-1"><code>NUM2PTR</code></font><code>()</code>.)</p>
<dt>&bull;</p>
<dd> Casting between function pointers and data pointers </p>
<p> Technically speaking casting between function pointers and data pointers is unportable and undefined, but practically speaking it seems to work, but you should use the <font SIZE="-1"><code>FPTR2DPTR</code></font><code>()</code> and <font SIZE="-1"><code>DPTR2FPTR</code></font><code>()</code> macros. Sometimes you can also play games with unions.</p>
<dt>&bull;</p>
<dd> Assuming sizeof(int) == sizeof(long) </p>
<p> There are platforms where longs are 64 bits, and platforms where ints are 64 bits, and while we are out to shock you, even platforms where shorts are 64 bits. This is all legal according to the C standard. (In other words, &#8220;long long&#8221; is not a portable way to specify 64 bits, and &#8220;long long&#8221; is not even guaranteed to be any wider than &#8220;long&#8221;.) </p>
<p> Instead, use the definitions <font SIZE="-1">IV, UV, IVSIZE, I32SIZE,</font> and so forth. Avoid things like I32 because they are <code>not</code> guaranteed to be <i>exactly</i> 32 bits, they are <i>at least</i> 32 bits, nor are they guaranteed to be <code>int</code> or <code>long</code>. If you really explicitly need 64-bit variables, use I64 and U64, but only if guarded by <font SIZE="-1">HAS_QUAD.</font></p>
<dt>&bull;</p>
<dd> Assuming one can dereference any type of pointer for any type of data </p>
<p>char *p = &#8230;;<br />
long pony = *(long *)p; /* BAD */</p>
<p> Many platforms, quite rightly so, will give you a core dump instead of a pony if the p happens not to be correctly aligned.</p>
<dt>&bull;</p>
<dd> Lvalue casts </p>
<pre>
  (int)*p = ...;    /* BAD */
</pre>
<p> Simply not portable. Get your lvalue to be of the right type, or maybe use temporary variables, or dirty tricks with unions.</p>
<dt>&bull;</p>
<dd> Assume <code>anything</code> about structs (especially the ones you don&#8217;t control, like the ones coming from the system headers)</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> That a certain field exists in a struct</p>
<dt>&bull;</p>
<dd> That no other fields exist besides the ones you know of</p>
<dt>&bull;</p>
<dd> That a field is of certain signedness, sizeof, or type</p>
<dt>&bull;</p>
<dd> That the fields are in a certain order</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> While C guarantees the ordering specified in the struct definition, between different platforms the definitions might differ</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> That the sizeof(struct) or the alignments are the same everywhere</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> There might be padding bytes between the fields to align the fields &#8211; the bytes can be anything</p>
<dt>&bull;</p>
<dd> Structs are required to be aligned to the maximum alignment required by the fields &#8211; which for native types is for usually equivalent to <code>sizeof()</code> of the field</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> Assuming the character set is ASCIIish </p>
<p> Perl can compile and run under <font SIZE="-1">EBCDIC</font> platforms. See perlebcdic. This is transparent for the most part, but because the character sets differ, you shouldn&#8217;t use numeric (decimal, octal, nor hex) constants to refer to characters. You can safely say <tt>'A'</tt>, but not <tt>0x41</tt>. You can safely say <tt>'
'</tt>, but not <tt>&quot;
&quot;</tt>. However, you can use macros defined in <i>utf8.h</i> to specify any code point portably. <tt>&quot;LATIN1_TO_NATIVE(0xDF)&quot;</tt> is going to be the code point that means <font SIZE="-1">LATIN SMALL LETTER SHARP S</font> on whatever platform you are running on (on <font SIZE="-1">ASCII</font> platforms it compiles without adding any extra code, so there is zero performance hit on those). The acceptable inputs to <tt>&quot;LATIN1_TO_NATIVE&quot;</tt> are from <tt>0x00</tt> through <tt>0xFF</tt>. If your input isn&#8217;t guaranteed to be in that range, use <tt>&quot;UNICODE_TO_NATIVE&quot;</tt> instead. <tt>&quot;NATIVE_TO_LATIN1&quot;</tt> and <tt>&quot;NATIVE_TO_UNICODE&quot;</tt> translate the opposite direction. </p>
<p> If you need the string representation of a character that doesn&#8217;t have a mnemonic name in C, you should add it to the list in <i>regen/unicode_constants.pl</i>, and have Perl create <tt>&quot;#define&quot;</tt>&#8216;s for you, based on the current platform. </p>
<p> Note that the <tt>&quot;is</tt>FOO<tt>&quot;</tt> and <tt>&quot;to</tt>FOO<tt>&quot;</tt> macros in <i>handy.h</i> work properly on native code points and strings. </p>
<p> Also, the range &#8216;A&#8217; &#8211; &#8216;Z&#8217; in <font SIZE="-1">ASCII</font> is an unbroken sequence of 26 upper case alphabetic characters. That is not true in <font SIZE="-1">EBCDIC.</font> Nor for &#8216;a&#8217; to &#8216;z&#8217;. But &#8216;0&#8217; &#8211; &#8216;9&#8217; is an unbroken range in both systems. Don&#8217;t assume anything about other ranges. (Note that special handling of ranges in regular expression patterns and transliterations makes it appear to Perl code that the aforementioned ranges are all unbroken.) </p>
<p> Many of the comments in the existing code ignore the possibility of <font SIZE="-1">EBCDIC,</font> and may be wrong therefore, even if the code works. This is actually a tribute to the successful transparent insertion of being able to handle <font SIZE="-1">EBCDIC</font> without having to change pre-existing code. </p>
<p> <font SIZE="-1">UTF-8</font> and UTF-EBCDIC are two different encodings used to represent Unicode code points as sequences of bytes. Macros with the same names (but different definitions) in <i>utf8.h</i> and <i>utfebcdic.h</i> are used to allow the calling code to think that there is only one such encoding. This is almost always referred to as <tt>&quot;utf8&quot;</tt>, but it means the <font SIZE="-1">EBCDIC</font> version as well. Again, comments in the code may well be wrong even if the code itself is right. For example, the concept of <font SIZE="-1">UTF-8</font> <tt>&quot;invariant characters&quot;</tt> differs between <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC.</font> On <font SIZE="-1">ASCII</font> platforms, only characters that do not have the high-order bit set (i.e. whose ordinals are strict <font SIZE="-1">ASCII, 0</font> &#8211; 127) are invariant, and the documentation and comments in the code may assume that, often referring to something like, say, <tt>&quot;hibit&quot;</tt>. The situation differs and is not so simple on <font SIZE="-1">EBCDIC</font> machines, but as long as the code itself uses the <tt>&quot;NATIVE_IS_INVARIANT()&quot;</tt> macro appropriately, it works, even if the comments are wrong. </p>
<p> As noted in &#8220;<font SIZE="-1">TESTING&#8221;</font> in perlhack, when writing test scripts, the file <i>t/charset_tools.pl</i> contains some helpful functions for writing tests valid on both <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font> platforms. Sometimes, though, a test can&#8217;t use a function and it&#8217;s inconvenient to have different test versions depending on the platform. There are 20 code points that are the same in all 4 character sets currently recognized by Perl (the 3 <font SIZE="-1">EBCDIC</font> code pages plus <font SIZE="-1">ISO 8859-1</font> (ASCII/Latin1)). These can be used in such tests, though there is a small possibility that Perl will become available in yet another character set, breaking your test. All but one of these code points are C0 control characters. The most significant controls that are the same are <tt>&quot;
