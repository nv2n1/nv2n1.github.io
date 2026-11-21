---

title: "perlhacktips(1)"
name: "perlhacktips"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhacktips/"
description: "perlhacktips – Tips for Perl core C code hacking"
---

<p> perlhacktips &#8211; Tips for Perl core C code hacking </p>
<h2>DESCRIPTION</h2>
<p> This document will help you learn the best way to go about hacking on the Perl core C code. It covers common problems, debugging, profiling, and more. </p>
<p> If you haven&#8217;t read perlhack and perlhacktut yet, you might want to do that first.</p>
<h2>COMMON PROBLEMS</h2>
<p> Perl source plays by <font SIZE="-1">ANSI C89</font> rules: no C99 (or C<font SIZE="-2">++</font>) extensions. You don&#8217;t care about some particular platform having broken Perl? I hear there is still a strong demand for J2EE programmers.</p>
<h3>Perl environment problems</h3>
<dl>
<dt>&bull;</dt>
<dd> Not compiling with threading </dd>
<p> Compiling with threading (-Duseithreads) completely rewrites the function prototypes of Perl. You better try your changes with that. Related to this is the difference between &#8220;Perl_-less&#8221; and &#8220;Perl_-ly&#8221; APIs, for example: </p>
<pre><code>
Perl_sv_setiv(aTHX_...);
sv_setiv(...);
</code></pre>
<p> The first one explicitly passes in the context, which is needed for e.g. threaded builds. The second one does that implicitly; do not get them mixed. If you are not passing in a aTHX_, you will need to do a dTHX (or a dVAR) as the first thing in the function. </p>
<p> See &#8220;How multiple interpreters and concurrency are supported&#8221; in perlguts for further discussion about context.</p>
<dt>&bull;</dt>
<dd> Not compiling with -DDEBUGGING </dd>
<p> The <font SIZE="-1">DEBUGGING</font> define exposes more code to the compiler, therefore more ways for things to go wrong. You should try it.</p>
<dt>&bull;</dt>
<dd> Introducing (non-read-only) globals </dd>
<p> Do not introduce any modifiable globals, truly global or file static. They are bad form and complicate multithreading and other forms of concurrency. The right way is to introduce them as new interpreter variables, see <i>intrpvar.h</i> (at the very end for binary compatibility). </p>
<p> Introducing read-only (const) globals is okay, as long as you verify with e.g. <tt>&quot;nm libperl.a|egrep -v ' [TURtr] '&quot;</tt> (if your <tt>&quot;nm&quot;</tt> has BSD-style output) that the data you added really is read-only. (If it is, it shouldn&#8217;t show up in the output of that command.) </p>
<p> If you want to have static strings, make them constant: </p>
<p>static const char etc[] = &#8220;&#8230;&#8221;;</p>
<p> If you want to have arrays of constant strings, note carefully the right combination of <tt>&quot;const&quot;</tt>s: </p>
<p>static const char *const yippee[] =<br />
    {&#8220;hi&#8221;, &#8220;ho&#8221;, &#8220;silver&#8221;};</p>
<p> There is a way to completely hide any modifiable globals (they are all moved to heap), the compilation setting <tt>&quot;-DPERL_GLOBAL_STRUCT_PRIVATE&quot;</tt>. It is not normally used, but can be used for testing, read more about it in &#8220;Background and <font SIZE="-1">PERL_IMPLICIT_CONTEXT&#8221;</font> in perlguts.</p>
<dt>&bull;</dt>
<dd> Not exporting your new function </dd>
<p> Some platforms (Win32, <font SIZE="-1">AIX, VMS, OS/2,</font> to name a few) require any function that is part of the public <font SIZE="-1">API</font> (the shared Perl library) to be explicitly marked as exported. See the discussion about <i>embed.pl</i> in perlguts.</p>
<dt>&bull;</dt>
<dd> Exporting your new function </dd>
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
<dt>&bull;</dt>
<dd> Casting pointers to integers or casting integers to pointers </dd>
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
<dt>&bull;</dt>
<dd> Casting between function pointers and data pointers </dd>
<p> Technically speaking casting between function pointers and data pointers is unportable and undefined, but practically speaking it seems to work, but you should use the <font SIZE="-1"><code>FPTR2DPTR</code></font><code>()</code> and <font SIZE="-1"><code>DPTR2FPTR</code></font><code>()</code> macros. Sometimes you can also play games with unions.</p>
<dt>&bull;</dt>
<dd> Assuming sizeof(int) == sizeof(long) </dd>
<p> There are platforms where longs are 64 bits, and platforms where ints are 64 bits, and while we are out to shock you, even platforms where shorts are 64 bits. This is all legal according to the C standard. (In other words, &#8220;long long&#8221; is not a portable way to specify 64 bits, and &#8220;long long&#8221; is not even guaranteed to be any wider than &#8220;long&#8221;.) </p>
<p> Instead, use the definitions <font SIZE="-1">IV, UV, IVSIZE, I32SIZE,</font> and so forth. Avoid things like I32 because they are <code>not</code> guaranteed to be <i>exactly</i> 32 bits, they are <i>at least</i> 32 bits, nor are they guaranteed to be <code>int</code> or <code>long</code>. If you really explicitly need 64-bit variables, use I64 and U64, but only if guarded by <font SIZE="-1">HAS_QUAD.</font></p>
<dt>&bull;</dt>
<dd> Assuming one can dereference any type of pointer for any type of data </dd>
<p>char *p = &#8230;;<br />
long pony = *(long *)p; /* BAD */</p>
<p> Many platforms, quite rightly so, will give you a core dump instead of a pony if the p happens not to be correctly aligned.</p>
<dt>&bull;</dt>
<dd> Lvalue casts </dd>
<pre>
  (int)*p = ...;    /* BAD */
</pre>
<p> Simply not portable. Get your lvalue to be of the right type, or maybe use temporary variables, or dirty tricks with unions.</p>
<dt>&bull;</dt>
<dd> Assume <code>anything</code> about structs (especially the ones you don&#8217;t control, like the ones coming from the system headers)</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> That a certain field exists in a struct</dd>
<dt>&bull;</dt>
<dd> That no other fields exist besides the ones you know of</dd>
<dt>&bull;</dt>
<dd> That a field is of certain signedness, sizeof, or type</dd>
<dt>&bull;</dt>
<dd> That the fields are in a certain order</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> While C guarantees the ordering specified in the struct definition, between different platforms the definitions might differ</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> That the sizeof(struct) or the alignments are the same everywhere</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> There might be padding bytes between the fields to align the fields &#8211; the bytes can be anything</dd>
<dt>&bull;</dt>
<dd> Structs are required to be aligned to the maximum alignment required by the fields &#8211; which for native types is for usually equivalent to <code>sizeof()</code> of the field</dd></dl>
</dl>
<dl>
</dl>
</dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> Assuming the character set is ASCIIish </dd>
<p> Perl can compile and run under <font SIZE="-1">EBCDIC</font> platforms. See perlebcdic. This is transparent for the most part, but because the character sets differ, you shouldn&#8217;t use numeric (decimal, octal, nor hex) constants to refer to characters. You can safely say <tt>'A'</tt>, but not <tt>0x41</tt>. You can safely say <tt>'
'</tt>, but not <tt>&quot;
&quot;</tt>. However, you can use macros defined in <i>utf8.h</i> to specify any code point portably. <tt>&quot;LATIN1_TO_NATIVE(0xDF)&quot;</tt> is going to be the code point that means <font SIZE="-1">LATIN SMALL LETTER SHARP S</font> on whatever platform you are running on (on <font SIZE="-1">ASCII</font> platforms it compiles without adding any extra code, so there is zero performance hit on those). The acceptable inputs to <tt>&quot;LATIN1_TO_NATIVE&quot;</tt> are from <tt>0x00</tt> through <tt>0xFF</tt>. If your input isn&#8217;t guaranteed to be in that range, use <tt>&quot;UNICODE_TO_NATIVE&quot;</tt> instead. <tt>&quot;NATIVE_TO_LATIN1&quot;</tt> and <tt>&quot;NATIVE_TO_UNICODE&quot;</tt> translate the opposite direction. </p>
<p> If you need the string representation of a character that doesn&#8217;t have a mnemonic name in C, you should add it to the list in <i>regen/unicode_constants.pl</i>, and have Perl create <tt>&quot;#define&quot;</tt>&#8216;s for you, based on the current platform. </p>
<p> Note that the <tt>&quot;is</tt>FOO<tt>&quot;</tt> and <tt>&quot;to</tt>FOO<tt>&quot;</tt> macros in <i>handy.h</i> work properly on native code points and strings. </p>
<p> Also, the range &#8216;A&#8217; &#8211; &#8216;Z&#8217; in <font SIZE="-1">ASCII</font> is an unbroken sequence of 26 upper case alphabetic characters. That is not true in <font SIZE="-1">EBCDIC.</font> Nor for &#8216;a&#8217; to &#8216;z&#8217;. But &#8216;0&#8217; &#8211; &#8216;9&#8217; is an unbroken range in both systems. Don&#8217;t assume anything about other ranges. (Note that special handling of ranges in regular expression patterns and transliterations makes it appear to Perl code that the aforementioned ranges are all unbroken.) </p>
<p> Many of the comments in the existing code ignore the possibility of <font SIZE="-1">EBCDIC,</font> and may be wrong therefore, even if the code works. This is actually a tribute to the successful transparent insertion of being able to handle <font SIZE="-1">EBCDIC</font> without having to change pre-existing code. </p>
<p> <font SIZE="-1">UTF-8</font> and UTF-EBCDIC are two different encodings used to represent Unicode code points as sequences of bytes. Macros with the same names (but different definitions) in <i>utf8.h</i> and <i>utfebcdic.h</i> are used to allow the calling code to think that there is only one such encoding. This is almost always referred to as <tt>&quot;utf8&quot;</tt>, but it means the <font SIZE="-1">EBCDIC</font> version as well. Again, comments in the code may well be wrong even if the code itself is right. For example, the concept of <font SIZE="-1">UTF-8</font> <tt>&quot;invariant characters&quot;</tt> differs between <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC.</font> On <font SIZE="-1">ASCII</font> platforms, only characters that do not have the high-order bit set (i.e. whose ordinals are strict <font SIZE="-1">ASCII, 0</font> &#8211; 127) are invariant, and the documentation and comments in the code may assume that, often referring to something like, say, <tt>&quot;hibit&quot;</tt>. The situation differs and is not so simple on <font SIZE="-1">EBCDIC</font> machines, but as long as the code itself uses the <tt>&quot;NATIVE_IS_INVARIANT()&quot;</tt> macro appropriately, it works, even if the comments are wrong. </p>
<p> As noted in &#8220;<font SIZE="-1">TESTING&#8221;</font> in perlhack, when writing test scripts, the file <i>t/charset_tools.pl</i> contains some helpful functions for writing tests valid on both <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font> platforms. Sometimes, though, a test can&#8217;t use a function and it&#8217;s inconvenient to have different test versions depending on the platform. There are 20 code points that are the same in all 4 character sets currently recognized by Perl (the 3 <font SIZE="-1">EBCDIC</font> code pages plus <font SIZE="-1">ISO 8859-1</font> (ASCII/Latin1)). These can be used in such tests, though there is a small possibility that Perl will become available in yet another character set, breaking your test. All but one of these code points are C0 control characters. The most significant controls that are the same are <tt>&quot;</tt>\0&quot;</code>, <code>&quot;\r&quot;</code>, and <code>&quot;\N{VT}&quot;</code> (also specifiable as <code>&quot;\cK&quot;</code>, <code>&quot;\x0B&quot;</code>, <code>&quot;\N{U+0B}&quot;</code>, or <code>&quot;\013&quot;</code>). The single non-control is U+00B6 <font SIZE="-1">PILCROW SIGN.</font> The controls that are the same have the same bit pattern in all 4 character sets, regardless of the UTF8ness of the string containing them. The bit pattern for U+B6 is the same in all 4 for non-UTF8 strings, but differs in each when its containing string is <font SIZE="-1">UTF-8</font> encoded. The only other code points that have some sort of sameness across all 4 character sets are the pair 0xDC and 0xFC. Together these represent upper- and lowercase <font SIZE="-1">LATIN LETTER U WITH DIAERESIS,</font> but which is upper and which is lower may be reversed: 0xDC is the capital in Latin1 and 0xFC is the small letter, while 0xFC is the capital in <font SIZE="-1">EBCDIC</font> and 0xDC is the small one. This factoid may be exploited in writing case insensitive tests that are the same across all 4 character sets. </p>
<dt>&bull;</dt>
<dd> <p> Assuming the character set is just <font SIZE="-1">ASCII</font> </p>
<p> <font SIZE="-1">ASCII</font> is a 7 bit encoding, but bytes have 8 bits in them. The 128 extra characters have different meanings depending on the locale. Absent a locale, currently these extra characters are generally considered to be unassigned, and this has presented some problems. This has being changed starting in 5.12 so that these characters can be considered to be Latin-1 (<font SIZE="-1">ISO-8859-1</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mixing #define and #ifdef </p>
<pre><code>  #define BURGLE(x) ... \
  #ifdef BURGLE_OLD_STYLE /* BAD */
  ... do it the old way ... \
  #else
  ... do it the new way ... \
  #endif
</code></pre>
<p> You cannot portably ``stack&#8217;&#8216; cpp directives. For example in the above you need two separate <font SIZE="-1"><code>BURGLE</code></font><code>()</code> #defines, one for each #ifdef branch. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Adding non-comment stuff after #endif or #else </p>
<pre><code>  #ifdef SNOSH
  ...
  #else !SNOSH /* BAD */
  ...
  #endif SNOSH /* BAD */
</code></pre>
<p> The #endif and #else cannot portably have anything non-comment after them. If you want to document what is going (which is a good idea especially if the branches are long), use (C) comments: </p>
<pre><code>  #ifdef SNOSH
  ...
  #else /* !SNOSH */
  ...
  #endif /* SNOSH */
</code></pre>
<p> The gcc option <code>&quot;-Wendif-labels&quot;</code> warns about the bad variant (by default on starting from Perl 5.9.4). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Having a comma after the last element of an enum list </p>
<pre><code>  enum color {
    CERULEAN,
    CHARTREUSE,
    CINNABAR, /* BAD */
  };
</code></pre>
<p> is not portable. Leave out the last comma. </p>
<p> Also note that whether enums are implicitly morphable to ints varies between compilers, you might need to (int). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using //-comments </p>
<pre><code>  // This function bamfoodles the zorklator. /* BAD */
</code></pre>
<p> That is C99 or C<font SIZE="-2">++</font>. Perl is C89. Using the //-comments is silently allowed by many C compilers but cranking up the <font SIZE="-1">ANSI C89</font> strictness (which we like to do) causes the compilation to fail. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mixing declarations and code </p>
<pre><code>  void zorklator()
  {
    int n = 3;set_zorkmids(n); /* BAD */
    int q = 4;
</code></pre>
<p> That is C99 or C<font SIZE="-2">++</font>. Some C compilers allow that, but you shouldn&#8217;t. </p>
<p> The gcc option <code>&quot;-Wdeclaration-after-statements&quot;</code> scans for such problems (by default on starting from Perl 5.9.4). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Introducing variables inside <code>for()</code> </p>
<pre><code>  for(int i = ...; ...; ...) { /* BAD */
</code></pre>
<p> That is C99 or C<font SIZE="-2">++</font>. While it would indeed be awfully nice to have that also in C89, to limit the scope of the loop variable, alas, we cannot. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mixing signed char pointers with unsigned char pointers </p>
<pre><code>  int foo(char *s) { ... }
  ...
  unsigned char *t = ...; /* Or U8* t = ... */
  foo(t); /* BAD */
</code></pre>
<p> While this is legal practice, it is certainly dubious, and downright fatal in at least one platform: for example <font SIZE="-1">VMS</font> cc considers this a fatal error. One cause for people often making this mistake is that a ``naked char&#8217;&#8216; and therefore dereferencing a ``naked char pointer&#8217;&#8216; have an undefined signedness: it depends on the compiler and the flags of the compiler and the underlying platform whether the result is signed or unsigned. For this very same reason using a &#8216;char&#8217; as an array index is bad. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Macros that have string constants and their arguments as substrings of the string constants </p>
<pre><code>  #defineFOO(n) printf(&quot;number = %d\n&quot;, n) /* BAD */
  FOO(10);
</code></pre>
<p> Pre-ANSI semantics for that was equivalent to </p>
<pre><code>  printf(&quot;10umber = %d\10&quot;);
</code></pre>
<p> which is probably not what you were expecting. Unfortunately at least one reasonably common and modern C compiler does ``real backward compatibility&#8217;&#8216; here, in <font SIZE="-1">AIX</font> that is what still happens even though the rest of the <font SIZE="-1">AIX</font> compiler is very happily C89. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using printf formats for non-basic C types </p>
<pre><code>   IV i = ...;
   printf(&quot;i = %d\n&quot;, i); /* BAD */
</code></pre>
<p> While this might by accident work in some platform (where <font SIZE="-1">IV</font> happens to be an <code>&quot;int&quot;</code>), in general it cannot. <font SIZE="-1">IV</font> might be something larger. Even worse the situation is with more specific types (defined by Perl&#8217;s configuration step in <i>config.h</i>): </p>
<pre><code>   Uid_t who = ...;
   printf(&quot;who = %d\n&quot;, who); /* BAD */
</code></pre>
<p> The problem here is that Uid_t might be not only not <code>&quot;int&quot;</code>-wide but it might also be unsigned, in which case large uids would be printed as negative values. </p>
<p> There is no simple solution to this because of <code>printf()</code>&#8216;s limited intelligence, but for many types the right format is available as with either &#8216;f&#8217; or &#8216;_f&#8217; suffix, for example: </p>
<pre><code>   IVdf /* IV in decimal */
   UVxf /* UV is hexadecimal */
   printf(&quot;i = %&quot;IVdf&quot;\n&quot;, i); /* The IVdf is a string constant. */
   Uid_t_f /* Uid_t in decimal */
   printf(&quot;who = %&quot;Uid_t_f&quot;\n&quot;, who);
</code></pre>
<p> Or you can try casting to a ``wide enough&#8217;&#8216; type: </p>
<pre><code>   printf(&quot;i = %&quot;IVdf&quot;\n&quot;, (IV)something_very_small_and_signed);
</code></pre>
<p> See ``Formatted Printing of Size_t and SSize_t&#8217;&#8216; in perlguts for how to print those. </p>
<p> Also remember that the <code>%p</code> format really does require a void pointer: </p>
<pre><code>   U8* p = ...;
   printf(&quot;p = %p\n&quot;, (void*)p);
</code></pre>
<p> The gcc option <code>&quot;-Wformat&quot;</code> scans for such problems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Blindly using variadic macros </p>
<p> gcc has had them for a while with its own syntax, and C99 brought them with a standardized syntax. Don&#8217;t use the former, and use the latter only if the <font SIZE="-1">HAS_C99_VARIADIC_MACROS</font> is defined. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Blindly passing va_list </p>
<p> Not all platforms support passing va_list to further varargs (stdarg) functions. The right thing to do is to copy the va_list using the <code>Perl_va_copy()</code> if the <font SIZE="-1">NEED_VA_COPY</font> is defined. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using gcc statement expressions </p>
<pre><code>   val = ({...;...;...}); /* BAD */
</code></pre>
<p> While a nice extension, it&#8217;s not portable. The Perl code does admittedly use them if available to gain some extra speed (essentially as a funky form of inlining), but you shouldn&#8217;t. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Binding together several statements in a macro </p>
<p> Use the macros <font SIZE="-1">STMT_START</font> and <font SIZE="-1">STMT_END.</font> </p>
<pre><code>   STMT_START {
      ...
   } STMT_END
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Testing for operating systems or versions when should be testing for features </p>
<pre><code>  #ifdef __FOONIX__ /* BAD */
  foo = quux();
  #endif
</code></pre>
<p> Unless you know with 100% certainty that <code>quux()</code> is only ever available for the ``Foonix&#8217;&#8216; operating system <code>and</code> that is available <code>and</code> correctly working for <code>all</code> past, present, <code>and</code> future versions of ``Foonix&#8217;&#8216;, the above is very wrong. This is more correct (though still not perfect, because the below is a compile-time check): </p>
<pre><code>  #ifdef HAS_QUUX
  foo = quux();
  #endif
</code></pre>
<p> How does the <font SIZE="-1">HAS_QUUX</font> become defined where it needs to be? Well, if Foonix happens to be Unixy enough to be able to run the Configure script, and Configure has been taught about detecting and testing <code>quux()</code>, the <font SIZE="-1">HAS_QUUX</font> will be correctly defined. In other platforms, the corresponding configuration step will hopefully do the same. </p>
<p> In a pinch, if you cannot wait for Configure to be educated, or if you have a good hunch of where <code>quux()</code> might be available, you can temporarily try the following: </p>
<pre><code>  #if (defined(__FOONIX__) || defined(__BARNIX__))
  # define HAS_QUUX
  #endif
  ...
  #ifdef HAS_QUUX
  foo = quux();
  #endif
</code></pre>
<p> But in any case, try to keep the features and operating systems separate. </p>
<p> A good resource on the predefined macros for various operating systems, compilers, and so forth is &lt;<a rel="nofollow" href="http://sourceforge.net/p/predef/wiki/Home/">http://sourceforge.net/p/predef/wiki/Home/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assuming the contents of static memory pointed to by the return values of Perl wrappers for C library functions doesn&#8217;t change. Many C library functions return pointers to static storage that can be overwritten by subsequent calls to the same or related functions. Perl has light-weight wrappers for some of these functions, and which don&#8217;t make copies of the static memory. A good example is the interface to the environment variables that are in effect for the program. Perl has <code>&quot;PerlEnv_getenv&quot;</code> to get values from the environment. But the return is a pointer to static memory in the C library. If you are using the value to immediately test for something, that&#8217;s fine, but if you save the value and expect it to be unchanged by later processing, you would be wrong, but perhaps you wouldn&#8217;t know it because different C library implementations behave differently, and the one on the platform you&#8217;re testing on might work for your situation. But on some platforms, a subsequent call to <code>&quot;PerlEnv_getenv&quot;</code> or related function <font SIZE="-1">WILL</font> overwrite the memory that your first call points to. This has led to some hard-to-debug problems. Do a ``savepv&#8217;&#8216; in perlapi to make a copy, thus avoiding these problems. You will have to free the copy when you&#8217;re done to avoid memory leaks. If you don&#8217;t have control over when it gets freed, you&#8217;ll need to make the copy in a mortal scalar, like so: </p>
<pre><code> if ((s = PerlEnv_getenv(&quot;foo&quot;) == NULL) {
    ... /* handle NULL case */
 }
 else {
     s = SvPVX(sv_2mortal(newSVpv(s, 0)));
 }
</code></pre>
<p> The above example works only if <code>&quot;s&quot;</code> is <code>&quot;NUL&quot;</code>-terminated; otherwise you have to pass its length to <code>&quot;newSVpv&quot;</code>. </p>
 </dd></dl>
<h3>Problematic System Interfaces</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>malloc</code>(0), <code>realloc</code>(0), calloc(0, 0) are non-portable. To be portable allocate at least one byte. (In general you should rarely need to work at this low level, but instead use the various malloc wrappers.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>snprintf()</code> &#8211; the return type is unportable. Use <code>my_snprintf()</code> instead. </p>
 </dd></dl>
<h3>Security problems</h3>
<p> Last but not least, here are various tips for safer coding. See also perlclib for libc/stdio replacements one should use. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Do not use <code>gets()</code> </p>
<p> Or we will publicly ridicule you. Seriously. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Do not use <code>tmpfile()</code> </p>
<p> Use <code>mkstemp()</code> instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Do not use <code>strcpy()</code> or <code>strcat()</code> or <code>strncpy()</code> or <code>strncat()</code> </p>
<p> Use <code>my_strlcpy()</code> and <code>my_strlcat()</code> instead: they either use the native implementation, or Perl&#8217;s own implementation (borrowed from the public domain implementation of <font SIZE="-1">INN</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Do not use <code>sprintf()</code> or <code>vsprintf()</code> </p>
<p> If you really want just plain byte strings, use <code>my_snprintf()</code> and <code>my_vsnprintf()</code> instead, which will try to use <code>snprintf()</code> and <code>vsnprintf()</code> if those safer APIs are available. If you want something fancier than a plain byte string, use <code>&quot;Perl_form&quot;</code>() or SVs and <code>&quot;Perl_sv_catpvf()&quot;</code>. </p>
<p> Note that glibc <code>&quot;printf()&quot;</code>, <code>&quot;sprintf()&quot;</code>, etc. are buggy before glibc version 2.17. They won&#8217;t allow a <code>&quot;%.s&quot;</code> format with a precision to create a string that isn&#8217;t valid <font SIZE="-1">UTF-8</font> if the current underlying locale of the program is <font SIZE="-1">UTF-8.</font> What happens is that the <code>%s</code> and its operand are simply skipped without any notice. &lt;<a rel="nofollow" href="https://sourceware.org/bugzilla/show_bug.cgi?id=6530">https://sourceware.org/bugzilla/show_bug.cgi?id=6530</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Do not use <code>atoi()</code> </p>
<p> Use <code>grok_atoUV()</code> instead. <code>atoi()</code> has ill-defined behavior on overflows, and cannot be used for incremental parsing. It is also affected by locale, which is bad. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Do not use <code>strtol()</code> or <code>strtoul()</code> </p>
<p> Use <code>grok_atoUV()</code> instead. <code>strtol()</code> or <code>strtoul()</code> (or their IV/UV-friendly macro disguises, <code>Strtol()</code> and <code>Strtoul()</code>, or <code>Atol()</code> and <code>Atoul()</code> are affected by locale, which is bad. </p>
 </dd></dl>
<h2>DEBUGGING</h2>
<p> You can compile a special debugging version of Perl, which allows you to use the <code>&quot;-D&quot;</code> option of Perl to tell more about what Perl is doing. But sometimes there is no alternative than to dive in with a debugger, either to see the stack trace of a core dump (very useful in a bug report), or trying to figure out what went wrong before the core dump happened, or how did we end up having wrong or unexpected results.  </p>
<h3>Poking at Perl</h3>
<p> To really poke around with Perl, you&#8217;ll probably want to build Perl for debugging, like this: </p>
<pre><code>    ./Configure -d -DDEBUGGING
    make
</code></pre>
<p> <code>&quot;-DDEBUGGING&quot;</code> turns on the C compiler&#8217;s <code>&quot;-g&quot;</code> flag to have it produce debugging information which will allow us to step through a running program, and to see in which C function we are at (without the debugging information we might see only the numerical addresses of the functions, which is not very helpful). It will also turn on the <code>&quot;DEBUGGING&quot;</code> compilation symbol which enables all the internal debugging code in Perl. There are a whole bunch of things you can debug with this: perlrun lists them all, and the best way to find out about them is to play about with them. The most useful options are probably </p>
<pre><code>    l Context (loop) stack processing
    s Stack snapshots (with v, displays all stacks)
    t Trace execution
    o Method and overloading resolution
    c String/numeric conversions
</code></pre>
<p> For example </p>
<pre><code>    $ perl -Dst -e '$a + 1'
    ....
    (-e:1) gvsv(main::a)
        =&gt; UNDEF
    (-e:1) const(IV(1))
        =&gt; UNDEFIV(1)
    (-e:1) add
        =&gt;NV(1)
</code></pre>
<p> Some of the functionality of the debugging code can be achieved with a non-debugging perl by using <font SIZE="-1">XS</font> modules: </p>
<pre><code>    -Dr =&gt; use re 'debug'
    -Dx =&gt; use O 'Debug'
</code></pre>
<h3>Using a source-level debugger</h3>
<p> If the debugging output of <code>&quot;-D&quot;</code> doesn&#8217;t help you, it&#8217;s time to step through perl&#8217;s execution with a source-level debugger. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> We&#8217;ll use <code>&quot;gdb&quot;</code> for our examples here; the principles will apply to any debugger (many vendors call their debugger <code>&quot;dbx&quot;</code>), but check the manual of the one you&#8217;re using. </p>
 </dd></dl>
<p> To fire up the debugger, type </p>
<pre><code>    gdb ./perl
</code></pre>
<p> Or if you have a core dump: </p>
<pre><code>    gdb ./perl core
</code></pre>
<p> You&#8217;ll want to do that in your Perl source tree so the debugger can read the source code. You should see the copyright message, followed by the prompt. </p>
<pre><code>    (gdb)
</code></pre>
<p> <code>&quot;help&quot;</code> will get you into the documentation, but here are the most useful commands: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> run [args] </p>
<p> Run the program with the given arguments. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> break function_name </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> break source.c:xxx </p>
<p> Tells the debugger that we&#8217;ll want to pause execution when we reach either the named function (but see ``Internal Functions&#8217;&#8216; in perlguts!) or the given line in the named source file. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> step </p>
<p> Steps through the program a line at a time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> next </p>
<p> Steps through the program a line at a time, without descending into functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> continue </p>
<p> Run until the next breakpoint. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> finish </p>
<p> Run until the end of the current function, then stop again. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;enter&#8217; </p>
<p> Just pressing Enter will do the most recent operation again &#8211; it&#8217;s a blessing when stepping through miles of source code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ptype </p>
<p> Prints the C definition of the argument given. </p>
<pre><code>  (gdb) ptype PL_op
  type = struct op {
      OP *op_next;
      OP *op_sibparent;
      OP *(*op_ppaddr)(void);
      PADOFFSET op_targ;
      unsigned int op_type : 9;
      unsigned int op_opt : 1;
      unsigned int op_slabbed : 1;
      unsigned int op_savefree : 1;
      unsigned int op_static : 1;
      unsigned int op_folded : 1;
      unsigned int op_spare : 2;
      U8 op_flags;
      U8 op_private;
  } *
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> print </p>
<p> Execute the given C code and print its results. <font SIZE="-1"><code>WARNING</code></font>: Perl makes heavy use of macros, and <i>gdb</i> does not necessarily support macros (see later ``gdb macro support&#8217;&#8216;). You&#8217;ll have to substitute them yourself, or to invoke cpp on the source code files (see ``The .i Targets&#8217;&#8216;) So, for instance, you can&#8217;t say </p>
<pre><code>    print SvPV_nolen(sv)
</code></pre>
<p> but you have to say </p>
<pre><code>    print Perl_sv_2pv_nolen(sv)
</code></pre>
 </dd></dl>
<p> You may find it helpful to have a ``macro dictionary&#8217;&#8216;, which you can produce by saying <code>&quot;cpp -dM perl.c | sort&quot;</code>. Even then, <i>cpp</i> won&#8217;t recursively apply those macros for you.  </p>
<h3>gdb macro support</h3>
<p> Recent versions of <i>gdb</i> have fairly good macro support, but in order to use it you&#8217;ll need to compile perl with macro definitions included in the debugging information. Using <i>gcc</i> version 3.1, this means configuring with <code>&quot;-Doptimize=-g3&quot;</code>. Other compilers might use a different switch (if they support debugging macros at all).  </p>
<h3>Dumping Perl Data Structures</h3>
<p> One way to get around this macro hell is to use the dumping functions in <i>dump.c</i>; these work a little like an internal Devel::Peek, but they also cover OPs and other structures that you can&#8217;t get at from Perl. Let&#8217;s take an example. We&#8217;ll use the <code>&quot;$a = $b + $c&quot;</code> we used before, but give it a bit of context: <code>&quot;$b = &quot;6XXXX&quot;; $c = 2.3;&quot;</code>. Where&#8217;s a good place to stop and poke around? </p>
<p> What about <code>&quot;pp_add&quot;</code>, the function we examined earlier to implement the <code>&quot;+&quot;</code> operator: </p>
<pre><code>    (gdb) break Perl_pp_add
    Breakpoint 1 at 0x46249f: file pp_hot.c, line 309.
</code></pre>
<p> Notice we use <code>&quot;Perl_pp_add&quot;</code> and not <code>&quot;pp_add&quot;</code> &#8211; see ``Internal Functions&#8217;&#8216; in perlguts. With the breakpoint in place, we can run our program: </p>
<pre><code>    (gdb) run -e '$b = &quot;6XXXX&quot;; $c = 2.3; $a = $b + $c'
</code></pre>
<p> Lots of junk will go past as gdb reads in the relevant source files and libraries, and then: </p>
<pre><code>    Breakpoint 1, Perl_pp_add () at pp_hot.c:309
    1396 dSP; dATARGET; bool useleft; SV *svl, *svr;
    (gdb) step
    311 dPOPTOPnnrl_ul;
    (gdb)
</code></pre>
<p> We looked at this bit of code before, and we said that <code>&quot;dPOPTOPnnrl_ul&quot;</code> arranges for two <code>&quot;NV&quot;</code>s to be placed into <code>&quot;left&quot;</code> and <code>&quot;right&quot;</code> &#8211; let&#8217;s slightly expand it: </p>
<pre><code> #define dPOPTOPnnrl_ul NV right = POPn; \
                         SV *leftsv = TOPs; \
                         NV left = USE_LEFT(leftsv) ? SvNV(leftsv) : 0.0
</code></pre>
<p> <code>&quot;POPn&quot;</code> takes the <font SIZE="-1">SV</font> from the top of the stack and obtains its <font SIZE="-1">NV</font> either directly (if <code>&quot;SvNOK&quot;</code> is set) or by calling the <code>&quot;sv_2nv&quot;</code> function. <code>&quot;TOPs&quot;</code> takes the next <font SIZE="-1">SV</font> from the top of the stack &#8211; yes, <code>&quot;POPn&quot;</code> uses <code>&quot;TOPs&quot;</code> &#8211; but doesn&#8217;t remove it. We then use <code>&quot;SvNV&quot;</code> to get the <font SIZE="-1">NV</font> from <code>&quot;leftsv&quot;</code> in the same way as before &#8211; yes, <code>&quot;POPn&quot;</code> uses <code>&quot;SvNV&quot;</code>. </p>
<p> Since we don&#8217;t have an <font SIZE="-1">NV</font> for <code>$b</code>, we&#8217;ll have to use <code>&quot;sv_2nv&quot;</code> to convert it. If we step again, we&#8217;ll find ourselves there: </p>
<pre><code>    (gdb) step
    Perl_sv_2nv (sv=0xa0675d0) at sv.c:1669
    1669 if (!sv)
    (gdb)
</code></pre>
<p> We can now use <code>&quot;Perl_sv_dump&quot;</code> to investigate the <font SIZE="-1">SV:</font> </p>
<pre><code>    (gdb) print Perl_sv_dump(sv)
    SV = PV(0xa057cc0) at 0xa0675d0
    REFCNT = 1
    FLAGS = (POK,pPOK)
    PV = 0xa06a510 &quot;6XXXX&quot;\0
    CUR = 5
    LEN = 6
    $1 = void
</code></pre>
<p> We know we&#8217;re going to get <code>6</code> from this, so let&#8217;s finish the subroutine: </p>
<pre><code>    (gdb) finish
    Run till exit from #0 Perl_sv_2nv (sv=0xa0675d0) at sv.c:1671
    0x462669 in Perl_pp_add () at pp_hot.c:311
    311 dPOPTOPnnrl_ul;
</code></pre>
<p> We can also dump out this op: the current op is always stored in <code>&quot;PL_op&quot;</code>, and we can dump it with <code>&quot;Perl_op_dump&quot;</code>. This&#8217;ll give us similar output to <font SIZE="-1">CPAN</font> module B::Debug. </p>
<pre><code>    (gdb) print Perl_op_dump(PL_op)
    {
    13 TYPE = add ===&gt; 14
        TARG = 1
        FLAGS = (SCALAR,KIDS)
        {
            TYPE = null ===&gt; (12)
              (was rv2sv)
            FLAGS = (SCALAR,KIDS)
            {
    11 TYPE = gvsv ===&gt; 12
                FLAGS = (SCALAR)
                GV = main::b
            }
        }
</code></pre>
<p> # finish this later #  </p>
<h3>Using gdb to look at specific parts of a program</h3>
<p> With the example above, you knew to look for <code>&quot;Perl_pp_add&quot;</code>, but what if there were multiple calls to it all over the place, or you didn&#8217;t know what the op was you were looking for? </p>
<p> One way to do this is to inject a rare call somewhere near what you&#8217;re looking for. For example, you could add <code>&quot;study&quot;</code> before your method: </p>
<pre><code>    study;
</code></pre>
<p> And in gdb do: </p>
<pre><code>    (gdb) break Perl_pp_study
</code></pre>
<p> And then step until you hit what you&#8217;re looking for. This works well in a loop if you want to only break at certain iterations: </p>
<pre><code>    for my $c (1..100) {
        study if $c == 50;
    }
</code></pre>
<h3>Using gdb to look at what the parser/lexer are doing</h3>
<p> If you want to see what perl is doing when parsing/lexing your code, you can use <code>&quot;BEGIN {}&quot;</code>: </p>
<pre><code>    print &quot;Before\n&quot;;
    BEGIN { study; }
    print &quot;After\n&quot;;
</code></pre>
<p> And in gdb: </p>
<pre><code>    (gdb) break Perl_pp_study
</code></pre>
<p> If you want to see what the parser/lexer is doing inside of <code>&quot;if&quot;</code> blocks and the like you need to be a little trickier: </p>
<pre><code>    if ($a &amp;&amp; $b &amp;&amp; do { BEGIN { study } 1 } &amp;&amp; $c) { ... }
</code></pre>
<h2>SOURCE CODE STATIC ANALYSIS</h2>
<p> Various tools exist for analysing C source code <code>statically</code>, as opposed to <code>dynamically</code>, that is, without executing the code. It is possible to detect resource leaks, undefined behaviour, type mismatches, portability problems, code paths that would cause illegal memory accesses, and other similar problems by just parsing the C code and looking at the resulting graph, what does it tell about the execution and data flows. As a matter of fact, this is exactly how C compilers know to give warnings about dubious code.  </p>
<h3>lint</h3>
<p> The good old C code quality inspector, <code>&quot;lint&quot;</code>, is available in several platforms, but please be aware that there are several different implementations of it by different vendors, which means that the flags are not identical across different platforms. </p>
<p> There is a <code>&quot;lint&quot;</code> target in Makefile, but you may have to diddle with the flags (see above).  </p>
<h3>Coverity</h3>
<p> Coverity (&lt;<a rel="nofollow" href="http://www.coverity.com/">http://www.coverity.com/</a>&gt;) is a product similar to lint and as a testbed for their product they periodically check several open source projects, and they give out accounts to open source developers to the defect databases. </p>
<p> There is Coverity setup for the perl5 project: &lt;<a rel="nofollow" href="https://scan.coverity.com/projects/perl5">https://scan.coverity.com/projects/perl5</a>&gt;  </p>
<h3>HP-UX cadvise (Code Advisor)</h3>
<p> <font SIZE="-1">HP</font> has a C/C<font SIZE="-2">++</font> static analyzer product for HP-UX caller Code Advisor. (Link not given here because the <font SIZE="-1">URL</font> is horribly long and seems horribly unstable; use the search engine of your choice to find it.) The use of the <code>&quot;cadvise_cc&quot;</code> recipe with <code>&quot;Configure ... -Dcc=./cadvise_cc&quot;</code> (see cadvise ``User Guide&#8217;&#8216;) is recommended; as is the use of <code>&quot;+wall&quot;</code>.  </p>
<h3>cpd (cut-and-paste detector)</h3>
<p> The cpd tool detects cut-and-paste coding. If one instance of the cut-and-pasted code changes, all the other spots should probably be changed, too. Therefore such code should probably be turned into a subroutine or a macro. </p>
<p> cpd (&lt;<a rel="nofollow" href="http://pmd.sourceforge.net/cpd.html">http://pmd.sourceforge.net/cpd.html</a>&gt;) is part of the pmd project (&lt;<a rel="nofollow" href="http://pmd.sourceforge.net/">http://pmd.sourceforge.net/</a>&gt;). pmd was originally written for static analysis of Java code, but later the cpd part of it was extended to parse also C and C<font SIZE="-2">++</font>. </p>
<p> Download the pmd-bin-X.Y.zip () from the SourceForge site, extract the pmd-X.Y.jar from it, and then run that on source code thusly: </p>
<pre><code>  java -cp pmd-X.Y.jar net.sourceforge.pmd.cpd.CPD \
   --minimum-tokens 100 --files /some/where/src --language c &gt; cpd.txt
</code></pre>
<p> You may run into memory limits, in which case you should use the -Xmx option: </p>
<pre><code>  java -Xmx512M ...
</code></pre>
<h3>gcc warnings</h3>
<p> Though much can be written about the inconsistency and coverage problems of gcc warnings (like <code>&quot;-Wall&quot;</code> not meaning ``all the warnings&#8217;&#8216;, or some common portability problems not being covered by <code>&quot;-Wall&quot;</code>, or <code>&quot;-ansi&quot;</code> and <code>&quot;-pedantic&quot;</code> both being a poorly defined collection of warnings, and so forth), gcc is still a useful tool in keeping our coding nose clean. </p>
<p> The <code>&quot;-Wall&quot;</code> is by default on. </p>
<p> The <code>&quot;-ansi&quot;</code> (and its sidekick, <code>&quot;-pedantic&quot;</code>) would be nice to be on always, but unfortunately they are not safe on all platforms, they can for example cause fatal conflicts with the system headers (Solaris being a prime example). If Configure <code>&quot;-Dgccansipedantic&quot;</code> is used, the <code>&quot;cflags&quot;</code> frontend selects <code>&quot;-ansi -pedantic&quot;</code> for the platforms where they are known to be safe. </p>
<p> The following extra flags are added: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Wendif-labels&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Wextra&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Wc++-compat&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Wwrite-strings&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Werror=declaration-after-statement&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Werror=pointer-arith&quot;</code> </p>
 </dd></dl>
<p> The following flags would be nice to have but they would first need their own Augean stablemaster: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Wshadow&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Wstrict-prototypes&quot;</code> </p>
 </dd></dl>
<p> The <code>&quot;-Wtraditional&quot;</code> is another example of the annoying tendency of gcc to bundle a lot of warnings under one switch (it would be impossible to deploy in practice because it would complain a lot) but it does contain some warnings that would be beneficial to have available on their own, such as the warning about string constants inside macros containing the macro arguments: this behaved differently pre-ANSI than it does in <font SIZE="-1">ANSI,</font> and some C compilers are still in transition, <font SIZE="-1">AIX</font> being an example.  </p>
<h3>Warnings of other C compilers</h3>
<p> Other C compilers (yes, there <code>are</code> other C compilers than gcc) often have their ``strict <font SIZE="-1">ANSI&#8217;&#8216;</font> or ``strict <font SIZE="-1">ANSI</font> with some portability extensions&#8217;&#8216; modes on, like for example the Sun Workshop has its <code>&quot;-Xa&quot;</code> mode on (though implicitly), or the <font SIZE="-1">DEC</font> (these days, <font SIZE="-1">HP...</font>) has its <code>&quot;-std1&quot;</code> mode on.  </p>
<h2>MEMORY DEBUGGERS</h2>
<p> <font SIZE="-1"><code>NOTE 1</code></font>: Running under older memory debuggers such as Purify, valgrind or Third Degree greatly slows down the execution: seconds become minutes, minutes become hours. For example as of Perl 5.8.1, the ext/Encode/t/Unicode.t takes extraordinarily long to complete under e.g. Purify, Third Degree, and valgrind. Under valgrind it takes more than six hours, even on a snappy computer. The said test must be doing something that is quite unfriendly for memory debuggers. If you don&#8217;t feel like waiting, that you can simply kill away the perl process. Roughly valgrind slows down execution by factor 10, AddressSanitizer by factor 2. </p>
<p> <font SIZE="-1"><code>NOTE 2</code></font>: To minimize the number of memory leak false alarms (see ``<font SIZE="-1">PERL_DESTRUCT_LEVEL&#8217;&#8216;</font> for more information), you have to set the environment variable <font SIZE="-1">PERL_DESTRUCT_LEVEL</font> to 2. For example, like this: </p>
<pre><code>    env PERL_DESTRUCT_LEVEL=2 valgrind ./perl -Ilib ...
</code></pre>
<p> <font SIZE="-1"><code>NOTE 3</code></font>: There are known memory leaks when there are compile-time errors within eval or require, seeing <code>&quot;S_doeval&quot;</code> in the call stack is a good sign of these. Fixing these leaks is non-trivial, unfortunately, but they must be fixed eventually. </p>
<p> <font SIZE="-1"><code>NOTE 4</code></font>: DynaLoader will not clean up after itself completely unless Perl is built with the Configure option <code>&quot;-Accflags=-DDL_UNLOAD_ALL_AT_EXIT&quot;</code>.  </p>
<h3>valgrind</h3>
<p> The valgrind tool can be used to find out both memory leaks and illegal heap memory accesses. As of version 3.3.0, Valgrind only supports Linux on x86, x86-64 and PowerPC and Darwin (<font SIZE="-1">OS X</font>) on x86 and x86-64. The special ``test.valgrind&#8217;&#8216; target can be used to run the tests under valgrind. Found errors and memory leaks are logged in files named <i>testfile.valgrind</i> and by default output is displayed inline. </p>
<p> Example usage: </p>
<pre><code>    make test.valgrind
</code></pre>
<p> Since valgrind adds significant overhead, tests will take much longer to run. The valgrind tests support being run in parallel to help with this: </p>
<pre><code>    TEST_JOBS=9 make test.valgrind
</code></pre>
<p> Note that the above two invocations will be very verbose as reachable memory and leak-checking is enabled by default. If you want to just see pure errors, try: </p>
<pre><code>    VG_OPTS='-q --leak-check=no --show-reachable=no' TEST_JOBS=9 \
        make test.valgrind
</code></pre>
<p> Valgrind also provides a cachegrind tool, invoked on perl as: </p>
<pre><code>    VG_OPTS=--tool=cachegrind make test.valgrind
</code></pre>
<p> As system libraries (most notably glibc) are also triggering errors, valgrind allows to suppress such errors using suppression files. The default suppression file that comes with valgrind already catches a lot of them. Some additional suppressions are defined in <i>t/perl.supp</i>. </p>
<p> To get valgrind and for more information see </p>
<pre><code>http://valgrind.org/
</code></pre>
<h3>AddressSanitizer</h3>
<p> AddressSanitizer is a clang and gcc extension, included in clang since v3.1 and gcc since v4.8. It checks illegal heap pointers, global pointers, stack pointers and use after free errors, and is fast enough that you can easily compile your debugging or optimized perl with it. It does not check memory leaks though. AddressSanitizer is available for Linux, Mac <font SIZE="-1">OS X</font> and soon on Windows. </p>
<p> To build perl with AddressSanitizer, your Configure invocation should look like: </p>
<pre><code>    sh Configure -des -Dcc=clang \
       -Accflags=-faddress-sanitizer -Aldflags=-faddress-sanitizer \
       -Alddlflags=-shared\ -faddress-sanitizer
</code></pre>
<p> where these arguments mean: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> -Dcc=clang </p>
<p> This should be replaced by the full path to your clang executable if it is not in your path. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -Accflags=-faddress-sanitizer </p>
<p> Compile perl and extensions sources with AddressSanitizer. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -Aldflags=-faddress-sanitizer </p>
<p> Link the perl executable with AddressSanitizer. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -Alddlflags=-shared\ -faddress-sanitizer </p>
<p> Link dynamic extensions with AddressSanitizer. You must manually specify <code>&quot;-shared&quot;</code> because using <code>&quot;-Alddlflags=-shared&quot;</code> will prevent Configure from setting a default value for <code>&quot;lddlflags&quot;</code>, which usually contains <code>&quot;-shared&quot;</code> (at least on Linux). </p>
 </dd></dl>
<p> See also &lt;<a rel="nofollow" href="http://code.google.com/p/address-sanitizer/wiki/AddressSanitizer">http://code.google.com/p/address-sanitizer/wiki/AddressSanitizer</a>&gt;.  </p>
<h2>PROFILING</h2>
<p> Depending on your platform there are various ways of profiling Perl. </p>
<p> There are two commonly used techniques of profiling executables: <i>statistical time-sampling</i> and <i>basic-block counting</i>. </p>
<p> The first method takes periodically samples of the <font SIZE="-1">CPU</font> program counter, and since the program counter can be correlated with the code generated for functions, we get a statistical view of in which functions the program is spending its time. The caveats are that very small/fast functions have lower probability of showing up in the profile, and that periodically interrupting the program (this is usually done rather frequently, in the scale of milliseconds) imposes an additional overhead that may skew the results. The first problem can be alleviated by running the code for longer (in general this is a good idea for profiling), the second problem is usually kept in guard by the profiling tools themselves. </p>
<p> The second method divides up the generated code into <i>basic blocks</i>. Basic blocks are sections of code that are entered only in the beginning and exited only at the end. For example, a conditional jump starts a basic block. Basic block profiling usually works by <i>instrumenting</i> the code by adding <i>enter basic block #nnnn</i> book-keeping code to the generated code. During the execution of the code the basic block counters are then updated appropriately. The caveat is that the added extra code can skew the results: again, the profiling tools usually try to factor their own effects out of the results.  </p>
<h3>Gprof Profiling</h3>
<p> <i>gprof</i> is a profiling tool available in many Unix platforms which uses <i>statistical time-sampling</i>. You can build a profiled version of <i>perl</i> by compiling using gcc with the flag <code>&quot;-pg&quot;</code>. Either edit <i>config.sh</i> or re-run <i>Configure</i>. Running the profiled version of Perl will create an output file called <i>gmon.out</i> which contains the profiling data collected during the execution. </p>
<p> quick hint: </p>
<pre><code>    $ sh Configure -des -Dusedevel -Accflags='-pg' \
        -Aldflags='-pg' -Alddlflags='-pg -shared' \
        &amp;&amp; make perl
    $ ./perl ... # creates gmon.out in current directory
    $ gprof ./perl &gt; out
    $ less out
</code></pre>
<p> (you probably need to add <code>&quot;-shared&quot;</code> to the &lt;-Alddlflags&gt; line until <font SIZE="-1">RT</font> #118199 is resolved) </p>
<p> The <i>gprof</i> tool can then display the collected data in various ways. Usually <i>gprof</i> understands the following options: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> -a </p>
<p> Suppress statically defined functions from the profile. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -b </p>
<p> Suppress the verbose descriptions in the profile. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -e routine </p>
<p> Exclude the given routine and its descendants from the profile. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -f routine </p>
<p> Display only the given routine and its descendants in the profile. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -s </p>
<p> Generate a summary file called <i>gmon.sum</i> which then may be given to subsequent gprof runs to accumulate data over several runs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> -z </p>
<p> Display routines that have zero usage. </p>
 </dd></dl>
<p> For more detailed explanation of the available commands and output formats, see your own local documentation of <i>gprof</i>.  </p>
<font SIZE="-1"></font><h3>GCC gcov Profiling</h3>
<p> <i>basic block profiling</i> is officially available in gcc 3.0 and later. You can build a profiled version of <i>perl</i> by compiling using gcc with the flags <code>&quot;-fprofile-arcs -ftest-coverage&quot;</code>. Either edit <i>config.sh</i> or re-run <i>Configure</i>. </p>
<p> quick hint: </p>
<pre><code>    $ sh Configure -des -Dusedevel -Doptimize='-g' \
        -Accflags='-fprofile-arcs -ftest-coverage' \
        -Aldflags='-fprofile-arcs -ftest-coverage' \
        -Alddlflags='-fprofile-arcs -ftest-coverage -shared' \
        &amp;&amp; make perl
    $ rm -f regexec.c.gcov regexec.gcda
    $ ./perl ...
    $ gcov regexec.c
    $ less regexec.c.gcov
</code></pre>
<p> (you probably need to add <code>&quot;-shared&quot;</code> to the &lt;-Alddlflags&gt; line until <font SIZE="-1">RT</font> #118199 is resolved) </p>
<p> Running the profiled version of Perl will cause profile output to be generated. For each source file an accompanying <i>.gcda</i> file will be created. </p>
<p> To display the results you use the <i>gcov</i> utility (which should be installed if you have gcc 3.0 or newer installed). <i>gcov</i> is run on source code files, like this </p>
<pre><code>    gcov sv.c
</code></pre>
<p> which will cause <i>sv.c.gcov</i> to be created. The <i>.gcov</i> files contain the source code annotated with relative frequencies of execution indicated by ``#&#8216;&#8216; markers. If you want to generate <i>.gcov</i> files for all profiled object files, you can run something like this: </p>
<pre><code>    for file in `find . -name \*.gcno`
    do sh -c &quot;cd `dirname $file` &amp;&amp; gcov `basename $file .gcno`&quot;
    done
</code></pre>
<p> Useful options of <i>gcov</i> include <code>&quot;-b&quot;</code> which will summarise the basic block, branch, and function call coverage, and <code>&quot;-c&quot;</code> which instead of relative frequencies will use the actual counts. For more information on the use of <i>gcov</i> and basic block profiling with gcc, see the latest <font SIZE="-1">GNU CC</font> manual. As of gcc 4.8, this is at &lt;<a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/gcc/Gcov-Intro.html#Gcov-Intro">http://gcc.gnu.org/onlinedocs/gcc/Gcov-Intro.html#Gcov-Intro</a>&gt;  </p>
<h2>MISCELLANEOUS TRICKS</h2>
<font SIZE="-1"></font><h3>PERL_DESTRUCT_LEVEL</h3>
<p> If you want to run any of the tests yourself manually using e.g. valgrind, please note that by default perl <code>does not</code> explicitly cleanup all the memory it has allocated (such as global memory arenas) but instead lets the <code>exit()</code> of the whole program ``take care&#8217;&#8216; of such allocations, also known as ``global destruction of objects&#8217;&#8216;. </p>
<p> There is a way to tell perl to do complete cleanup: set the environment variable <font SIZE="-1">PERL_DESTRUCT_LEVEL</font> to a non-zero value. The t/TEST wrapper does set this to 2, and this is what you need to do too, if you don&#8217;t want to see the ``global leaks&#8217;&#8216;: For example, for running under valgrind </p>
<pre><code>    env PERL_DESTRUCT_LEVEL=2 valgrind ./perl -Ilib t/foo/bar.t
</code></pre>
<p> (Note: the mod_perl apache module uses also this environment variable for its own purposes and extended its semantics. Refer to the mod_perl documentation for more information. Also, spawned threads do the equivalent of setting this variable to the value 1.) </p>
<p> If, at the end of a run you get the message <i>N scalars leaked</i>, you can recompile with <code>&quot;-DDEBUG_LEAKING_SCALARS&quot;</code>, (<code>&quot;Configure -Accflags=-DDEBUG_LEAKING_SCALARS&quot;</code>), which will cause the addresses of all those leaked SVs to be dumped along with details as to where each <font SIZE="-1">SV</font> was originally allocated. This information is also displayed by Devel::Peek. Note that the extra details recorded with each <font SIZE="-1">SV</font> increases memory usage, so it shouldn&#8217;t be used in production environments. It also converts <code>&quot;new_SV()&quot;</code> from a macro into a real function, so you can use your favourite debugger to discover where those pesky SVs were allocated. </p>
<p> If you see that you&#8217;re leaking memory at runtime, but neither valgrind nor <code>&quot;-DDEBUG_LEAKING_SCALARS&quot;</code> will find anything, you&#8217;re probably leaking SVs that are still reachable and will be properly cleaned up during destruction of the interpreter. In such cases, using the <code>&quot;-Dm&quot;</code> switch can point you to the source of the leak. If the executable was built with <code>&quot;-DDEBUG_LEAKING_SCALARS&quot;</code>, <code>&quot;-Dm&quot;</code> will output <font SIZE="-1">SV</font> allocations in addition to memory allocations. Each <font SIZE="-1">SV</font> allocation has a distinct serial number that will be written on creation and destruction of the <font SIZE="-1">SV.</font> So if you&#8217;re executing the leaking code in a loop, you need to look for SVs that are created, but never destroyed between each cycle. If such an <font SIZE="-1">SV</font> is found, set a conditional breakpoint within <code>&quot;new_SV()&quot;</code> and make it break only when <code>&quot;PL_sv_serial&quot;</code> is equal to the serial number of the leaking <font SIZE="-1">SV.</font> Then you will catch the interpreter in exactly the state where the leaking <font SIZE="-1">SV</font> is allocated, which is sufficient in many cases to find the source of the leak. </p>
<p> As <code>&quot;-Dm&quot;</code> is using the PerlIO layer for output, it will by itself allocate quite a bunch of SVs, which are hidden to avoid recursion. You can bypass the PerlIO layer if you use the <font SIZE="-1">SV</font> logging provided by <code>&quot;-DPERL_MEM_LOG&quot;</code> instead.  </p>
<font SIZE="-1"></font><h3>PERL_MEM_LOG</h3>
<p> If compiled with <code>&quot;-DPERL_MEM_LOG&quot;</code> (<code>&quot;-Accflags=-DPERL_MEM_LOG&quot;</code>), both memory and <font SIZE="-1">SV</font> allocations go through logging functions, which is handy for breakpoint setting. </p>
<p> Unless <code>&quot;-DPERL_MEM_LOG_NOIMPL&quot;</code> (<code>&quot;-Accflags=-DPERL_MEM_LOG_NOIMPL&quot;</code>) is also compiled, the logging functions read <code>$ENV</code>{<font SIZE="-1">PERL_MEM_LOG</font>} to determine whether to log the event, and if so how: </p>
<pre><code>    $ENV{PERL_MEM_LOG} =~ /m/ Log all memory ops
    $ENV{PERL_MEM_LOG} =~ /s/ Log all SV ops
    $ENV{PERL_MEM_LOG} =~ /t/ include timestamp in Log
    $ENV{PERL_MEM_LOG} =~ /^(\d+)/ write to FD given (default is 2)
</code></pre>
<p> Memory logging is somewhat similar to <code>&quot;-Dm&quot;</code> but is independent of <code>&quot;-DDEBUGGING&quot;</code>, and at a higher level; all uses of <code>Newx()</code>, <code>Renew()</code>, and <code>Safefree()</code> are logged with the caller&#8217;s source code file and line number (and C function name, if supported by the C compiler). In contrast, <code>&quot;-Dm&quot;</code> is directly at the point of <code>&quot;malloc()&quot;</code>. <font SIZE="-1">SV</font> logging is similar. </p>
<p> Since the logging doesn&#8217;t use PerlIO, all <font SIZE="-1">SV</font> allocations are logged and no extra <font SIZE="-1">SV</font> allocations are introduced by enabling the logging. If compiled with <code>&quot;-DDEBUG_LEAKING_SCALARS&quot;</code>, the serial number for each <font SIZE="-1">SV</font> allocation is also logged.  </p>
<font SIZE="-1"></font><h3>DDD over gdb</h3>
<p> Those debugging perl with the <font SIZE="-1">DDD</font> frontend over gdb may find the following useful: </p>
<p> You can extend the data conversion shortcuts menu, so for example you can display an <font SIZE="-1">SV</font>&#8216;s <font SIZE="-1">IV</font> value with one click, without doing any typing. To do that simply edit ~/.ddd/init file and add after: </p>
<pre><code>  ! Display shortcuts.
  Ddd*gdbDisplayShortcuts: \
  /t () // Convert to Bin\n\
  /d () // Convert to Dec\n\
  /x () // Convert to Hex\n\
  /o () // Convert to Oct(\n\
</code></pre>
<p> the following two lines: </p>
<pre><code>  ((XPV*) (())-&gt;sv_any )-&gt;xpv_pv // 2pvx\n\
  ((XPVIV*) (())-&gt;sv_any )-&gt;xiv_iv // 2ivx
</code></pre>
<p> so now you can do ivx and pvx lookups or you can plug there the sv_peek ``conversion&#8217;&#8216;: </p>
<pre><code>  Perl_sv_peek(my_perl, (SV*)()) // sv_peek
</code></pre>
<p> (The my_perl is for threaded builds.) Just remember that every line, but the last one, should end with \n\ </p>
<p> Alternatively edit the init file interactively via: 3rd mouse button -&gt; New Display -&gt; Edit Menu </p>
<p> Note: you can define up to 20 conversion shortcuts in the gdb section.  </p>
<h3>C backtrace</h3>
<p> On some platforms Perl supports retrieving the C level backtrace (similar to what symbolic debuggers like gdb do). </p>
<p> The backtrace returns the stack trace of the C call frames, with the symbol names (function names), the object names (like ``perl&#8217;&#8216;), and if it can, also the source code locations (file:line). </p>
<p> The supported platforms are Linux, and <font SIZE="-1">OS X</font> (some *BSD might work at least partly, but they have not yet been tested). </p>
<p> This feature hasn&#8217;t been tested with multiple threads, but it will only show the backtrace of the thread doing the backtracing. </p>
<p> The feature needs to be enabled with <code>&quot;Configure -Dusecbacktrace&quot;</code>. </p>
<p> The <code>&quot;-Dusecbacktrace&quot;</code> also enables keeping the debug information when compiling/linking (often: <code>&quot;-g&quot;</code>). Many compilers/linkers do support having both optimization and keeping the debug information. The debug information is needed for the symbol names and the source locations. </p>
<p> Static functions might not be visible for the backtrace. </p>
<p> Source code locations, even if available, can often be missing or misleading if the compiler has e.g. inlined code. Optimizer can make matching the source code and the object code quite challenging. </p>
<dl>
<dt>Linux</dt>
<dd> <p> You <code>must</code> have the <font SIZE="-1">BFD</font> (-lbfd) library installed, otherwise <code>&quot;perl&quot;</code> will fail to link. The <font SIZE="-1">BFD</font> is usually distributed as part of the <font SIZE="-1">GNU</font> binutils. </p>
<p> Summary: <code>&quot;Configure ... -Dusecbacktrace&quot;</code> and you need <code>&quot;-lbfd&quot;</code>. </p>
 </dd>
<dt><font SIZE="-1">OS X</font></dt>
<dd> <p> The source code locations are supported <code>only</code> if you have the Developer Tools installed. (<font SIZE="-1">BFD</font> is <code>not</code> needed.) </p>
<p> Summary: <code>&quot;Configure ... -Dusecbacktrace&quot;</code> and installing the Developer Tools would be good. </p>
 </dd></dl>
<p> Optionally, for trying out the feature, you may want to enable automatic dumping of the backtrace just before a warning or croak (die) message is emitted, by adding <code>&quot;-Accflags=-DUSE_C_BACKTRACE_ON_ERROR&quot;</code> for Configure. </p>
<p> Unless the above additional feature is enabled, nothing about the backtrace functionality is visible, except for the Perl/XS level. </p>
<p> Furthermore, even if you have enabled this feature to be compiled, you need to enable it in runtime with an environment variable: <code>&quot;PERL_C_BACKTRACE_ON_ERROR=10&quot;</code>. It must be an integer higher than zero, telling the desired frame count. </p>
<p> Retrieving the backtrace from Perl level (using for example an <font SIZE="-1">XS</font> extension) would be much less exciting than one would hope: normally you would see <code>&quot;runops&quot;</code>, <code>&quot;entersub&quot;</code>, and not much else. This <font SIZE="-1">API</font> is intended to be called <code>from within</code> the Perl implementation, not from Perl level execution. </p>
<p> The C <font SIZE="-1">API</font> for the backtrace is as follows: </p>
<dl>
<dt>get_c_backtrace</dt>
<dd>  </dd>
<dt>free_c_backtrace</dt>
<dd>  </dd>
<dt>get_c_backtrace_dump</dt>
<dd>  </dd>
<dt>dump_c_backtrace</dt>
<dd>  </dd></dl>
<h3>Poison</h3>
<p> If you see in a debugger a memory area mysteriously full of 0xABABABAB or 0xEFEFEFEF, you may be seeing the effect of the <code>Poison()</code> macros, see perlclib.  </p>
<h3>Read-only optrees</h3>
<p> Under ithreads the optree is read only. If you want to enforce this, to check for write accesses from buggy code, compile with <code>&quot;-Accflags=-DPERL_DEBUG_READONLY_OPS&quot;</code> to enable code that allocates op memory via <code>&quot;mmap&quot;</code>, and sets it read-only when it is attached to a subroutine. Any write access to an op results in a <code>&quot;SIGBUS&quot;</code> and abort. </p>
<p> This code is intended for development only, and may not be portable even to all Unix variants. Also, it is an 80% solution, in that it isn&#8217;t able to make all ops read only. Specifically it does not apply to op slabs belonging to <code>&quot;BEGIN&quot;</code> blocks. </p>
<p> However, as an 80% solution it is still effective, as it has caught bugs in the past.  </p>
<h3>When is a bool not a bool?</h3>
<p> On pre-C99 compilers, <code>&quot;bool&quot;</code> is defined as equivalent to <code>&quot;char&quot;</code>. Consequently assignment of any larger type to a <code>&quot;bool&quot;</code> is unsafe and may be truncated. The <code>&quot;cBOOL&quot;</code> macro exists to cast it correctly; you may also find that using it is shorter and clearer than writing out the equivalent conditional expression longhand. </p>
<p> On those platforms and compilers where <code>&quot;bool&quot;</code> really is a boolean (C<font SIZE="-2">++</font>, C99), it is easy to forget the cast. You can force <code>&quot;bool&quot;</code> to be a <code>&quot;char&quot;</code> by compiling with <code>&quot;-Accflags=-DPERL_BOOL_AS_CHAR&quot;</code>. You may also wish to run <code>&quot;Configure&quot;</code> with something like </p>
<pre><code>    -Accflags='-Wconversion -Wno-sign-conversion -Wno-shorten-64-to-32'
</code></pre>
<p> or your compiler&#8217;s equivalent to make it easier to spot any unsafe truncations that show up. </p>
<p> The <code>&quot;TRUE&quot;</code> and <code>&quot;FALSE&quot;</code> macros are available for situations where using them would clarify intent. (But they always just mean the same as the integers 1 and 0 regardless, so using them isn&#8217;t compulsory.)  </p>
<h3>The .i Targets</h3>
<p> You can expand the macros in a <i>foo.c</i> file by saying </p>
<pre><code>    make foo.i
</code></pre>
<p> which will expand the macros using cpp. Don&#8217;t be scared by the results.  </p>
<h2>AUTHOR</h2>
<p> This document was originally written by Nathan Torkington, and is maintained by the perl5-porters mailing list. </p>
