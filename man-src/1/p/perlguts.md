---
title: "perlguts(1)"
name: "perlguts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlguts/"
description: "perlguts – Introduction to the Perl API"
---

<h2>DESCRIPTION</h2>
<p> This document attempts to describe how to use the Perl <font SIZE="-1">API,</font> as well as to provide some info on the basic workings of the Perl core. It is far from complete and probably contains many errors. Please refer any questions or comments to the author below.</p>
<h2>Variables</h2>
<h3>Datatypes</h3>
<p> Perl has three typedefs that handle Perl&#8217;s three main data types: </p>
<pre>
    SV  Scalar Value
    AV  Array Value
    HV  Hash Value
</pre>
<p> Each typedef has specific routines that manipulate the various data types.</p>
<h3>What is an <font SIZE="-1">IV</font>?</h3>
<p> Perl uses a special typedef <font SIZE="-1">IV</font> which is a simple signed integer type that is guaranteed to be large enough to hold a pointer (as well as an integer). Additionally, there is the <font SIZE="-1">UV,</font> which is simply an unsigned <font SIZE="-1">IV.</font> </p>
<p> Perl also uses two special typedefs, I32 and I16, which will always be at least 32-bits and 16-bits long, respectively. (Again, there are U32 and U16, as well.) They will usually be exactly 32 and 16 bits long, but on Crays they will both be 64 bits.</p>
<h3>Working with SVs</h3>
<p> An <font SIZE="-1">SV</font> can be created and loaded with one command. There are five types of values that can be loaded: an integer value (<font SIZE="-1">IV</font>), an unsigned integer value (<font SIZE="-1">UV</font>), a double (<font SIZE="-1">NV</font>), a string (<font SIZE="-1">PV</font>), and another scalar (<font SIZE="-1">SV</font>). (&#8220;<font SIZE="-1">PV&#8221;</font> stands for &#8220;Pointer Value&#8221;. You might think that it is misnamed because it is described as pointing only to strings. However, it is possible to have it point to other things. For example, it could point to an array of UVs. But, using it for non-strings requires care, as the underlying assumption of much of the internals is that PVs are just for strings. Often, for example, a trailing <tt>&quot;NUL&quot;</tt> is tacked on automatically. The non-string use is documented only in this paragraph.) </p>
<p> The seven routines are: </p>
<pre><code>
SV *newSViv(IV);
SV *newSVuv(UV);
SV *newSVnv(double);
SV *newSVpv(const char *, STRLEN);
SV *newSVpvn(const char *, STRLEN);
SV *newSVpvf(const char *, ...);
SV *newSVsv(SV *);
</code></pre>
<p> <tt>&quot;STRLEN&quot;</tt> is an integer type (<tt>&quot;Size_t&quot;</tt>, usually defined as <tt>&quot;size_t&quot;</tt> in <i>config.h</i>) guaranteed to be large enough to represent the size of any string that perl can handle. </p>
<p> In the unlikely case of a <font SIZE="-1">SV</font> requiring more complex initialization, you can create an empty <font SIZE="-1">SV</font> with newSV(len). If <tt>&quot;len&quot;</tt> is 0 an empty <font SIZE="-1">SV</font> of type <font SIZE="-1">NULL</font> is returned, else an <font SIZE="-1">SV</font> of type <font SIZE="-1">PV</font> is returned with len + 1 (for the <tt>&quot;NUL&quot;</tt>) bytes of storage allocated, accessible via SvPVX. In both cases the <font SIZE="-1">SV</font> has the undef value. </p>
<p>SV *sv = newSV(0);  /* no storage allocated  */<br />
SV *sv = newSV(10); /* 10 (+1) bytes of uninitialised storage<br />
                     * allocated */</p>
<p> To change the value of an <i>already-existing</i> <font SIZE="-1">SV,</font> there are eight routines: </p>
<p>void sv_setiv(SV *, IV);<br />
void sv_setuv(SV *, UV);<br />
void sv_setnv(SV *, double);<br />
void sv_setpv(SV *, const char *);<br />
void sv_setpvn(SV *, const char *, STRLEN) void sv_setpvf(SV *, const char *, &#8230;);<br />
void sv_vsetpvfn(SV *, const char *, STRLEN, va_list *,<br />
                 SV **, Size_t, bool *);<br />
void sv_setsv(SV *, SV *);</p>
<p> Notice that you can choose to specify the length of the string to be assigned by using <tt>&quot;sv_setpvn&quot;</tt>, <tt>&quot;newSVpvn&quot;</tt>, or <tt>&quot;newSVpv&quot;</tt>, or you may allow Perl to calculate the length by using <tt>&quot;sv_setpv&quot;</tt> or by specifying 0 as the second argument to <tt>&quot;newSVpv&quot;</tt>. Be warned, though, that Perl will determine the string&#8217;s length by using <tt>&quot;strlen&quot;</tt>, which depends on the string terminating with a <tt>&quot;NUL&quot;</tt> character, and not otherwise containing NULs. </p>
<p> The arguments of <tt>&quot;sv_setpvf&quot;</tt> are processed like <tt>&quot;sprintf&quot;</tt>, and the formatted output becomes the value. </p>
<p> <tt>&quot;sv_vsetpvfn&quot;</tt> is an analogue of <tt>&quot;vsprintf&quot;</tt>, but it allows you to specify either a pointer to a variable argument list or the address and length of an array of SVs. The last argument points to a boolean; on return, if that boolean is true, then locale-specific information has been used to format the string, and the string&#8217;s contents are therefore untrustworthy (see perlsec). This pointer may be <font SIZE="-1">NULL</font> if that information is not important. Note that this function requires you to specify the length of the format. </p>
<p> The <tt>&quot;sv_set*()&quot;</tt> functions are not generic enough to operate on values that have &#8220;magic&#8221;. See &#8220;Magic Virtual Tables&#8221; later in this document. </p>
<p> All SVs that contain strings should be terminated with a <tt>&quot;NUL&quot;</tt> character. If it is not <tt>&quot;NUL&quot;</tt>-terminated there is a risk of core dumps and corruptions from code which passes the string to C functions or system calls which expect a <tt>&quot;NUL&quot;</tt>-terminated string. Perl&#8217;s own functions typically add a trailing <tt>&quot;NUL&quot;</tt> for this reason. Nevertheless, you should be very careful when you pass a string stored in an <font SIZE="-1">SV</font> to a C function or system call. </p>
<p> To access the actual value that an <font SIZE="-1">SV</font> points to, you can use the macros: </p>
<pre>
    SvIV(SV*)
    SvUV(SV*)
    SvNV(SV*)
    SvPV(SV*, STRLEN len)
    SvPV_nolen(SV*)
</pre>
<p> which will automatically coerce the actual scalar type into an <font SIZE="-1">IV, UV,</font> double, or string. </p>
<p> In the <tt>&quot;SvPV&quot;</tt> macro, the length of the string returned is placed into the variable <tt>&quot;len&quot;</tt> (this is a macro, so you do <i>not</i> use <tt>&amp;len</tt>). If you do not care what the length of the data is, use the <tt>&quot;SvPV_nolen&quot;</tt> macro. Historically the <tt>&quot;SvPV&quot;</tt> macro with the global variable <tt>&quot;PL_na&quot;</tt> has been used in this case. But that can be quite inefficient because <tt>&quot;PL_na&quot;</tt> must be accessed in thread-local storage in threaded Perl. In any case, remember that Perl allows arbitrary strings of data that may both contain NULs and might not be terminated by a <tt>&quot;NUL&quot;</tt>. </p>
<p> Also remember that C doesn&#8217;t allow you to safely say <tt>&quot;foo(SvPV(s, len), len);&quot;</tt>. It might work with your compiler, but it won&#8217;t work for everyone. Break this sort of statement up into separate assignments: </p>
<p>SV *s;<br />
STRLEN len;<br />
char *ptr;<br />
ptr = SvPV(s, len);<br />
foo(ptr, len);</p>
<p> If you want to know if the scalar value is <font SIZE="-1">TRUE,</font> you can use: </p>
<pre>
    SvTRUE(SV*)
</pre>
<p> Although Perl will automatically grow strings for you, if you need to force Perl to allocate more memory for your <font SIZE="-1">SV,</font> you can use the macro </p>
<pre>
    SvGROW(SV*, STRLEN newlen)
</pre>
<p> which will determine if more memory needs to be allocated. If so, it will call the function <tt>&quot;sv_grow&quot;</tt>. Note that <tt>&quot;SvGROW&quot;</tt> can only increase, not decrease, the allocated memory of an <font SIZE="-1">SV</font> and that it does not automatically add space for the trailing <tt>&quot;NUL&quot;</tt> byte (perl&#8217;s own string functions typically do <tt>&quot;SvGROW(sv, len + 1)&quot;</tt>). </p>
<p> If you want to write to an existing <font SIZE="-1">SV</font>&#8216;s buffer and set its value to a string, use <code>SvPV_force()</code> or one of its variants to force the <font SIZE="-1">SV</font> to be a <font SIZE="-1">PV.</font> This will remove any of various types of non-stringness from the <font SIZE="-1">SV</font> while preserving the content of the <font SIZE="-1">SV</font> in the <font SIZE="-1">PV.</font> This can be used, for example, to append data from an <font SIZE="-1">API</font> function to a buffer without extra copying: </p>
<p>(void)SvPVbyte_force(sv, len);<br />
s = SvGROW(sv, len + needlen + 1);<br />
/* something that modifies up to needlen bytes at s+len, but<br />
   modifies newlen bytes<br />
     eg. newlen = read(fd, s + len, needlen);<br />
   ignoring errors for these examples<br />
 */<br />
s[len + newlen] = &#8216;\0&#8217;; SvCUR_set(sv, len + newlen); SvUTF8_off(sv); SvSETMAGIC(sv); </code></pre>
 </p>
<p> If you already have the data in memory or if you want to keep your code simple, you can use one of the sv_cat*() variants, such as <code>sv_catpvn()</code>. If you want to insert anywhere in the string you can use <code>sv_insert()</code> or <code>sv_insert_flags()</code>. </p>
<p> If you don&#8217;t need the existing content of the <font SIZE="-1">SV,</font> you can avoid some copying with: </p>
<pre><code>    SvPVCLEAR(sv);
    s = SvGROW(sv, needlen + 1);
    /* something that modifies up to needlen bytes at s, but modifies
       newlen bytes
         eg. newlen = read(fd, s. needlen);
     */
    s[newlen] = '\0';
    SvCUR_set(sv, newlen);
    SvPOK_only(sv); /* also clears SVf_UTF8 */
    SvSETMAGIC(sv);
</code></pre>
<p> Again, if you already have the data in memory or want to avoid the complexity of the above, you can use <code>sv_setpvn()</code>. </p>
<p> If you have a buffer allocated with <code>Newx()</code> and want to set that as the <font SIZE="-1">SV</font>&#8216;s value, you can use <code>sv_usepvn_flags()</code>. That has some requirements if you want to avoid perl re-allocating the buffer to fit the trailing <font SIZE="-1">NUL:</font> </p>
<pre><code>   Newx(buf, somesize+1, char);
   /* ... fill in buf ... */
   buf[somesize] = '\0';
   sv_usepvn_flags(sv, buf, somesize, SV_SMAGIC | SV_HAS_TRAILING_NUL);
   /* buf now belongs to perl, don't release it */
</code></pre>
<p> If you have an <font SIZE="-1">SV</font> and want to know what kind of data Perl thinks is stored in it, you can use the following macros to check the type of <font SIZE="-1">SV</font> you have. </p>
<pre><code>    SvIOK(SV*)
    SvNOK(SV*)
    SvPOK(SV*)
</code></pre>
<p> You can get and set the current length of the string stored in an <font SIZE="-1">SV</font> with the following macros: </p>
<pre><code>    SvCUR(SV*)
    SvCUR_set(SV*, I32 val)
</code></pre>
<p> You can also get a pointer to the end of the string stored in the <font SIZE="-1">SV</font> with the macro: </p>
<pre><code>    SvEND(SV*)
</code></pre>
<p> But note that these last three macros are valid only if <code>&quot;SvPOK()&quot;</code> is true. </p>
<p> If you want to append something to the end of string stored in an <code>&quot;SV*&quot;</code>, you can use the following functions: </p>
<pre><code>    void sv_catpv(SV*, const char*);
    void sv_catpvn(SV*, const char*, STRLEN);
    void sv_catpvf(SV*, const char*, ...);
    void sv_vcatpvfn(SV*, const char*, STRLEN, va_list *, SV **,
                                                             I32, bool);
    void sv_catsv(SV*, SV*);
</code></pre>
<p> The first function calculates the length of the string to be appended by using <code>&quot;strlen&quot;</code>. In the second, you specify the length of the string yourself. The third function processes its arguments like <code>&quot;sprintf&quot;</code> and appends the formatted output. The fourth function works like <code>&quot;vsprintf&quot;</code>. You can specify the address and length of an array of SVs instead of the va_list argument. The fifth function extends the string stored in the first <font SIZE="-1">SV</font> with the string stored in the second <font SIZE="-1">SV.</font> It also forces the second <font SIZE="-1">SV</font> to be interpreted as a string. </p>
<p> The <code>&quot;sv_cat*()&quot;</code> functions are not generic enough to operate on values that have ``magic&#8217;&#8216;. See ``Magic Virtual Tables&#8217;&#8216; later in this document. </p>
<p> If you know the name of a scalar variable, you can get a pointer to its <font SIZE="-1">SV</font> by using the following: </p>
<pre><code>    SV* get_sv(&quot;package::varname&quot;, 0);
</code></pre>
<p> This returns <font SIZE="-1">NULL</font> if the variable does not exist. </p>
<p> If you want to know if this variable (or any other <font SIZE="-1">SV</font>) is actually <code>&quot;defined&quot;</code>, you can call: </p>
<pre><code>    SvOK(SV*)
</code></pre>
<p> The scalar <code>&quot;undef&quot;</code> value is stored in an <font SIZE="-1">SV</font> instance called <code>&quot;PL_sv_undef&quot;</code>. </p>
<p> Its address can be used whenever an <code>&quot;SV*&quot;</code> is needed. Make sure that you don&#8217;t try to compare a random sv with <code>&amp;PL_sv_undef</code>. For example when interfacing Perl code, it&#8217;ll work correctly for: </p>
<pre><code>  foo(undef);
</code></pre>
<p> But won&#8217;t work when called as: </p>
<pre><code>  $x = undef;
  foo($x);
</code></pre>
<p> So to repeat always use <code>SvOK()</code> to check whether an sv is defined. </p>
<p> Also you have to be careful when using <code>&amp;PL_sv_undef</code> as a value in AVs or HVs (see ``AVs, HVs and undefined values&#8217;&#8216;). </p>
<p> There are also the two values <code>&quot;PL_sv_yes&quot;</code> and <code>&quot;PL_sv_no&quot;</code>, which contain boolean <font SIZE="-1">TRUE</font> and <font SIZE="-1">FALSE</font> values, respectively. Like <code>&quot;PL_sv_undef&quot;</code>, their addresses can be used whenever an <code>&quot;SV*&quot;</code> is needed. </p>
<p> Do not be fooled into thinking that <code>&quot;(SV *) 0&quot;</code> is the same as <code>&amp;PL_sv_undef</code>. Take this code: </p>
<pre><code>    SV* sv = (SV*) 0;
    if (I-am-to-return-a-real-value) {
            sv = sv_2mortal(newSViv(42));
    }
    sv_setsv(ST(0), sv);
</code></pre>
<p> This code tries to return a new <font SIZE="-1">SV</font> (which contains the value 42) if it should return a real value, or undef otherwise. Instead it has returned a <font SIZE="-1">NULL</font> pointer which, somewhere down the line, will cause a segmentation violation, bus error, or just weird results. Change the zero to <code>&amp;PL_sv_undef</code> in the first line and all will be well. </p>
<p> To free an <font SIZE="-1">SV</font> that you&#8217;ve created, call <code>&quot;SvREFCNT_dec(SV*)&quot;</code>. Normally this call is not necessary (see ``Reference Counts and Mortality&#8217;&#8216;).  </p>
<h3>Offsets</h3>
<p> Perl provides the function <code>&quot;sv_chop&quot;</code> to efficiently remove characters from the beginning of a string; you give it an <font SIZE="-1">SV</font> and a pointer to somewhere inside the <font SIZE="-1">PV,</font> and it discards everything before the pointer. The efficiency comes by means of a little hack: instead of actually removing the characters, <code>&quot;sv_chop&quot;</code> sets the flag <code>&quot;OOK&quot;</code> (offset <font SIZE="-1">OK</font>) to signal to other functions that the offset hack is in effect, and it moves the <font SIZE="-1">PV</font> pointer (called <code>&quot;SvPVX&quot;</code>) forward by the number of bytes chopped off, and adjusts <code>&quot;SvCUR&quot;</code> and <code>&quot;SvLEN&quot;</code> accordingly. (A portion of the space between the old and new <font SIZE="-1">PV</font> pointers is used to store the count of chopped bytes.) </p>
<p> Hence, at this point, the start of the buffer that we allocated lives at <code>&quot;SvPVX(sv) &#8211; SvIV(sv)&quot;</code> in memory and the <font SIZE="-1">PV</font> pointer is pointing into the middle of this allocated storage. </p>
<p> This is best demonstrated by example. Normally copy-on-write will prevent the substitution from operator from using this hack, but if you can craft a string for which copy-on-write is not possible, you can see it in play. In the current implementation, the final byte of a string buffer is used as a copy-on-write reference count. If the buffer is not big enough, then copy-on-write is skipped. First have a look at an empty string: </p>
<pre><code>  % ./perl -Ilib -MDevel::Peek -le '$a=&quot;&quot;; $a .= &quot;&quot;; Dump $a'
  SV = PV(0x7ffb7c008a70) at 0x7ffb7c030390
    REFCNT = 1
    FLAGS = (POK,pPOK)
    PV = 0x7ffb7bc05b50 &quot;&quot;\0
    CUR = 0
    LEN = 10
</code></pre>
<p> Notice here the <font SIZE="-1">LEN</font> is 10. (It may differ on your platform.) Extend the length of the string to one less than 10, and do a substitution: </p>
<pre><code> % ./perl -Ilib -MDevel::Peek -le '$a=&quot;&quot;; $a.=&quot;123456789&quot;; $a=~s/.//; \
                                                            Dump($a)'
 SV = PV(0x7ffa04008a70) at 0x7ffa04030390
   REFCNT = 1
   FLAGS = (POK,OOK,pPOK)
   OFFSET = 1
   PV = 0x7ffa03c05b61 ( &quot;\1&quot; . ) &quot;23456789&quot;\0
   CUR = 8
   LEN = 9
</code></pre>
<p> Here the number of bytes chopped off (1) is shown next as the <font SIZE="-1">OFFSET.</font> The portion of the string between the ``real&#8217;&#8216; and the ``fake&#8217;&#8216; beginnings is shown in parentheses, and the values of <code>&quot;SvCUR&quot;</code> and <code>&quot;SvLEN&quot;</code> reflect the fake beginning, not the real one. (The first character of the string buffer happens to have changed to ``\1&#8217;&#8216; here, not ``1&#8217;&#8216;, because the current implementation stores the offset count in the string buffer. This is subject to change.) </p>
<p> Something similar to the offset hack is performed on AVs to enable efficient shifting and splicing off the beginning of the array; while <code>&quot;AvARRAY&quot;</code> points to the first element in the array that is visible from Perl, <code>&quot;AvALLOC&quot;</code> points to the real start of the C array. These are usually the same, but a <code>&quot;shift&quot;</code> operation can be carried out by increasing <code>&quot;AvARRAY&quot;</code> by one and decreasing <code>&quot;AvFILL&quot;</code> and <code>&quot;AvMAX&quot;</code>. Again, the location of the real start of the C array only comes into play when freeing the array. See <code>&quot;av_shift&quot;</code> in <i>av.c</i>.  </p>
<font SIZE="-1"></font><h3>What's Really Stored in an SV ?</h3>
<p> Recall that the usual method of determining the type of scalar you have is to use <code>&quot;Sv*OK&quot;</code> macros. Because a scalar can be both a number and a string, usually these macros will always return <font SIZE="-1">TRUE</font> and calling the <code>&quot;Sv*V&quot;</code> macros will do the appropriate conversion of string to integer/double or integer/double to string. </p>
<p> If you <i>really</i> need to know if you have an integer, double, or string pointer in an <font SIZE="-1">SV,</font> you can use the following three macros instead: </p>
<pre><code>    SvIOKp(SV*)
    SvNOKp(SV*)
    SvPOKp(SV*)
</code></pre>
<p> These will tell you if you truly have an integer, double, or string pointer stored in your <font SIZE="-1">SV.</font> The ``p&#8217;&#8216; stands for private. </p>
<p> There are various ways in which the private and public flags may differ. For example, in perl 5.16 and earlier a tied <font SIZE="-1">SV</font> may have a valid underlying value in the <font SIZE="-1">IV</font> slot (so SvIOKp is true), but the data should be accessed via the <font SIZE="-1">FETCH</font> routine rather than directly, so SvIOK is false. (In perl 5.18 onwards, tied scalars use the flags the same way as untied scalars.) Another is when numeric conversion has occurred and precision has been lost: only the private flag is set on &#8216;lossy&#8217; values. So when an <font SIZE="-1">NV</font> is converted to an <font SIZE="-1">IV</font> with loss, SvIOKp, SvNOKp and SvNOK will be set, while SvIOK wont be. </p>
<p> In general, though, it&#8217;s best to use the <code>&quot;Sv*V&quot;</code> macros.  </p>
<h3>Working with AVs</h3>
<p> There are two ways to create and load an <font SIZE="-1">AV.</font> The first method creates an empty <font SIZE="-1">AV:</font> </p>
<pre><code>    AV* newAV();
</code></pre>
<p> The second method both creates the <font SIZE="-1">AV</font> and initially populates it with SVs: </p>
<pre><code>    AV* av_make(SSize_t num, SV **ptr);
</code></pre>
<p> The second argument points to an array containing <code>&quot;num&quot;</code> <code>&quot;SV*&quot;</code>&#8216;s. Once the <font SIZE="-1">AV</font> has been created, the SVs can be destroyed, if so desired. </p>
<p> Once the <font SIZE="-1">AV</font> has been created, the following operations are possible on it: </p>
<pre><code>    void av_push(AV*, SV*);
    SV* av_pop(AV*);
    SV* av_shift(AV*);
    void av_unshift(AV*, SSize_t num);
</code></pre>
<p> These should be familiar operations, with the exception of <code>&quot;av_unshift&quot;</code>. This routine adds <code>&quot;num&quot;</code> elements at the front of the array with the <code>&quot;undef&quot;</code> value. You must then use <code>&quot;av_store&quot;</code> (described below) to assign values to these new elements. </p>
<p> Here are some other functions: </p>
<pre><code>    SSize_t av_top_index(AV*);
    SV** av_fetch(AV*, SSize_t key, I32 lval);
    SV** av_store(AV*, SSize_t key, SV* val);
</code></pre>
<p> The <code>&quot;av_top_index&quot;</code> function returns the highest index value in an array (just like $#array in Perl). If the array is empty, -1 is returned. The <code>&quot;av_fetch&quot;</code> function returns the value at index <code>&quot;key&quot;</code>, but if <code>&quot;lval&quot;</code> is non-zero, then <code>&quot;av_fetch&quot;</code> will store an undef value at that index. The <code>&quot;av_store&quot;</code> function stores the value <code>&quot;val&quot;</code> at index <code>&quot;key&quot;</code>, and does not increment the reference count of <code>&quot;val&quot;</code>. Thus the caller is responsible for taking care of that, and if <code>&quot;av_store&quot;</code> returns <font SIZE="-1">NULL,</font> the caller will have to decrement the reference count to avoid a memory leak. Note that <code>&quot;av_fetch&quot;</code> and <code>&quot;av_store&quot;</code> both return <code>&quot;SV**&quot;</code>&#8216;s, not <code>&quot;SV*&quot;</code>&#8216;s as their return value. </p>
<p> A few more: </p>
<pre><code>    void av_clear(AV*);
    void av_undef(AV*);
    void av_extend(AV*, SSize_t key);
</code></pre>
<p> The <code>&quot;av_clear&quot;</code> function deletes all the elements in the AV* array, but does not actually delete the array itself. The <code>&quot;av_undef&quot;</code> function will delete all the elements in the array plus the array itself. The <code>&quot;av_extend&quot;</code> function extends the array so that it contains at least <code>&quot;key+1&quot;</code> elements. If <code>&quot;key+1&quot;</code> is less than the currently allocated length of the array, then nothing is done. </p>
<p> If you know the name of an array variable, you can get a pointer to its <font SIZE="-1">AV</font> by using the following: </p>
<pre><code>    AV* get_av(&quot;package::varname&quot;, 0);
</code></pre>
<p> This returns <font SIZE="-1">NULL</font> if the variable does not exist. </p>
<p> See ``Understanding the Magic of Tied Hashes and Arrays&#8217;&#8216; for more information on how to use the array access functions on tied arrays.  </p>
<h3>Working with HVs</h3>
<p> To create an <font SIZE="-1">HV,</font> you use the following routine: </p>
<pre><code>    HV* newHV();
</code></pre>
<p> Once the <font SIZE="-1">HV</font> has been created, the following operations are possible on it: </p>
<pre><code>    SV** hv_store(HV*, const char* key, U32 klen, SV* val, U32 hash);
    SV** hv_fetch(HV*, const char* key, U32 klen, I32 lval);
</code></pre>
<p> The <code>&quot;klen&quot;</code> parameter is the length of the key being passed in (Note that you cannot pass 0 in as a value of <code>&quot;klen&quot;</code> to tell Perl to measure the length of the key). The <code>&quot;val&quot;</code> argument contains the <font SIZE="-1">SV</font> pointer to the scalar being stored, and <code>&quot;hash&quot;</code> is the precomputed hash value (zero if you want <code>&quot;hv_store&quot;</code> to calculate it for you). The <code>&quot;lval&quot;</code> parameter indicates whether this fetch is actually a part of a store operation, in which case a new undefined value will be added to the <font SIZE="-1">HV</font> with the supplied key and <code>&quot;hv_fetch&quot;</code> will return as if the value had already existed. </p>
<p> Remember that <code>&quot;hv_store&quot;</code> and <code>&quot;hv_fetch&quot;</code> return <code>&quot;SV**&quot;</code>&#8216;s and not just <code>&quot;SV*&quot;</code>. To access the scalar value, you must first dereference the return value. However, you should check to make sure that the return value is not <font SIZE="-1">NULL</font> before dereferencing it. </p>
<p> The first of these two functions checks if a hash table entry exists, and the second deletes it. </p>
<pre><code>    bool hv_exists(HV*, const char* key, U32 klen);
    SV* hv_delete(HV*, const char* key, U32 klen, I32 flags);
</code></pre>
<p> If <code>&quot;flags&quot;</code> does not include the <code>&quot;G_DISCARD&quot;</code> flag then <code>&quot;hv_delete&quot;</code> will create and return a mortal copy of the deleted value. </p>
<p> And more miscellaneous functions: </p>
<pre><code>    void hv_clear(HV*);
    void hv_undef(HV*);
</code></pre>
<p> Like their <font SIZE="-1">AV</font> counterparts, <code>&quot;hv_clear&quot;</code> deletes all the entries in the hash table but does not actually delete the hash table. The <code>&quot;hv_undef&quot;</code> deletes both the entries and the hash table itself. </p>
<p> Perl keeps the actual data in a linked list of structures with a typedef of <font SIZE="-1">HE.</font> These contain the actual key and value pointers (plus extra administrative overhead). The key is a string pointer; the value is an <code>&quot;SV*&quot;</code>. However, once you have an <code>&quot;HE*&quot;</code>, to get the actual key and value, use the routines specified below. </p>
<pre><code>    I32 hv_iterinit(HV*);
            /* Prepares starting point to traverse hash table */
    HE* hv_iternext(HV*);
            /* Get the next entry, and return a pointer to a
               structure that has both the key and value */
    char* hv_iterkey(HE* entry, I32* retlen);
            /* Get the key from an HE structure and also return
               the length of the key string */
    SV* hv_iterval(HV*, HE* entry);
            /* Return an SV pointer to the value of the HE
               structure */
    SV* hv_iternextsv(HV*, char** key, I32* retlen);
            /* This convenience routine combines hv_iternext,
               hv_iterkey, and hv_iterval. The key and retlen
               arguments are return values for the key and its
               length. The value is returned in the SV* argument */
</code></pre>
<p> If you know the name of a hash variable, you can get a pointer to its <font SIZE="-1">HV</font> by using the following: </p>
<pre><code>    HV* get_hv(&quot;package::varname&quot;, 0);
</code></pre>
<p> This returns <font SIZE="-1">NULL</font> if the variable does not exist. </p>
<p> The hash algorithm is defined in the <code>&quot;PERL_HASH&quot;</code> macro: </p>
<pre><code>    PERL_HASH(hash, key, klen)
</code></pre>
<p> The exact implementation of this macro varies by architecture and version of perl, and the return value may change per invocation, so the value is only valid for the duration of a single perl process. </p>
<p> See ``Understanding the Magic of Tied Hashes and Arrays&#8217;&#8216; for more information on how to use the hash access functions on tied hashes.  </p>
<font SIZE="-1"></font><h3>Hash API Extensions</h3>
<p> Beginning with version 5.004, the following functions are also supported: </p>
<pre><code>    HE* hv_fetch_ent (HV* tb, SV* key, I32 lval, U32 hash);
    HE* hv_store_ent (HV* tb, SV* key, SV* val, U32 hash);
    bool hv_exists_ent (HV* tb, SV* key, U32 hash);
    SV* hv_delete_ent (HV* tb, SV* key, I32 flags, U32 hash);
    SV* hv_iterkeysv (HE* entry);
</code></pre>
<p> Note that these functions take <code>&quot;SV*&quot;</code> keys, which simplifies writing of extension code that deals with hash structures. These functions also allow passing of <code>&quot;SV*&quot;</code> keys to <code>&quot;tie&quot;</code> functions without forcing you to stringify the keys (unlike the previous set of functions). </p>
<p> They also return and accept whole hash entries (<code>&quot;HE*&quot;</code>), making their use more efficient (since the hash number for a particular string doesn&#8217;t have to be recomputed every time). See perlapi for detailed descriptions. </p>
<p> The following macros must always be used to access the contents of hash entries. Note that the arguments to these macros must be simple variables, since they may get evaluated more than once. See perlapi for detailed descriptions of these macros. </p>
<pre><code>    HePV(HE* he, STRLEN len)
    HeVAL(HE* he)
    HeHASH(HE* he)
    HeSVKEY(HE* he)
    HeSVKEY_force(HE* he)
    HeSVKEY_set(HE* he, SV* sv)
</code></pre>
<p> These two lower level macros are defined, but must only be used when dealing with keys that are not <code>&quot;SV*&quot;</code>s: </p>
<pre><code>    HeKEY(HE* he)
    HeKLEN(HE* he)
</code></pre>
<p> Note that both <code>&quot;hv_store&quot;</code> and <code>&quot;hv_store_ent&quot;</code> do not increment the reference count of the stored <code>&quot;val&quot;</code>, which is the caller&#8217;s responsibility. If these functions return a <font SIZE="-1">NULL</font> value, the caller will usually have to decrement the reference count of <code>&quot;val&quot;</code> to avoid a memory leak.  </p>
<h3>AVs, HVs and undefined values</h3>
<p> Sometimes you have to store undefined values in AVs or HVs. Although this may be a rare case, it can be tricky. That&#8217;s because you&#8217;re used to using <code>&amp;PL_sv_undef</code> if you need an undefined <font SIZE="-1">SV.</font> </p>
<p> For example, intuition tells you that this <font SIZE="-1">XS</font> code: </p>
<pre><code>    AV *av = newAV();
    av_store( av, 0, &amp;PL_sv_undef );
</code></pre>
<p> is equivalent to this Perl code: </p>
<pre><code>    my @av;
    $av[0] = undef;
</code></pre>
<p> Unfortunately, this isn&#8217;t true. In perl 5.18 and earlier, AVs use <code>&amp;PL_sv_undef</code> as a marker for indicating that an array element has not yet been initialized. Thus, <code>&quot;exists $av[0]&quot;</code> would be true for the above Perl code, but false for the array generated by the <font SIZE="-1">XS</font> code. In perl 5.20, storing &amp;PL_sv_undef will create a read-only element, because the scalar &amp;PL_sv_undef itself is stored, not a copy. </p>
<p> Similar problems can occur when storing <code>&amp;PL_sv_undef</code> in HVs: </p>
<pre><code>    hv_store( hv, &quot;key&quot;, 3, &amp;PL_sv_undef, 0 );
</code></pre>
<p> This will indeed make the value <code>&quot;undef&quot;</code>, but if you try to modify the value of <code>&quot;key&quot;</code>, you&#8217;ll get the following error: </p>
<pre><code>    Modification of non-creatable hash value attempted
</code></pre>
<p> In perl 5.8.0, <code>&amp;PL_sv_undef</code> was also used to mark placeholders in restricted hashes. This caused such hash entries not to appear when iterating over the hash or when checking for the keys with the <code>&quot;hv_exists&quot;</code> function. </p>
<p> You can run into similar problems when you store <code>&amp;PL_sv_yes</code> or <code>&amp;PL_sv_no</code> into AVs or HVs. Trying to modify such elements will give you the following error: </p>
<pre><code>    Modification of a read-only value attempted
</code></pre>
<p> To make a long story short, you can use the special variables <code>&amp;PL_sv_undef</code>, <code>&amp;PL_sv_yes</code> and <code>&amp;PL_sv_no</code> with AVs and HVs, but you have to make sure you know what you&#8217;re doing. </p>
<p> Generally, if you want to store an undefined value in an <font SIZE="-1">AV</font> or <font SIZE="-1">HV,</font> you should not use <code>&amp;PL_sv_undef</code>, but rather create a new undefined value using the <code>&quot;newSV&quot;</code> function, for example: </p>
<pre><code>    av_store( av, 42, newSV(0) );
    hv_store( hv, &quot;foo&quot;, 3, newSV(0), 0 );
</code></pre>
<h3>References</h3>
<p> References are a special type of scalar that point to other data types (including other references). </p>
<p> To create a reference, use either of the following functions: </p>
<pre><code>    SV* newRV_inc((SV*) thing);
    SV* newRV_noinc((SV*) thing);
</code></pre>
<p> The <code>&quot;thing&quot;</code> argument can be any of an <code>&quot;SV*&quot;</code>, <code>&quot;AV*&quot;</code>, or <code>&quot;HV*&quot;</code>. The functions are identical except that <code>&quot;newRV_inc&quot;</code> increments the reference count of the <code>&quot;thing&quot;</code>, while <code>&quot;newRV_noinc&quot;</code> does not. For historical reasons, <code>&quot;newRV&quot;</code> is a synonym for <code>&quot;newRV_inc&quot;</code>. </p>
<p> Once you have a reference, you can use the following macro to dereference the reference: </p>
<pre><code>    SvRV(SV*)
</code></pre>
<p> then call the appropriate routines, casting the returned <code>&quot;SV*&quot;</code> to either an <code>&quot;AV*&quot;</code> or <code>&quot;HV*&quot;</code>, if required. </p>
<p> To determine if an <font SIZE="-1">SV</font> is a reference, you can use the following macro: </p>
<pre><code>    SvROK(SV*)
</code></pre>
<p> To discover what type of value the reference refers to, use the following macro and then check the return value. </p>
<pre><code>    SvTYPE(SvRV(SV*))
</code></pre>
<p> The most useful types that will be returned are: </p>
<pre><code>    SVt_PVAV Array
    SVt_PVHV Hash
    SVt_PVCV Code
    SVt_PVGV Glob (possibly a file handle)
</code></pre>
<p> Any numerical value returned which is less than SVt_PVAV will be a scalar of some form. </p>
<p> See ``svtype&#8217;&#8216; in perlapi for more details.  </p>
<h3>Blessed References and Class Objects</h3>
<p> References are also used to support object-oriented programming. In perl&#8217;s <font SIZE="-1">OO</font> lexicon, an object is simply a reference that has been blessed into a package (or class). Once blessed, the programmer may now use the reference to access the various methods in the class. </p>
<p> A reference can be blessed into a package with the following function: </p>
<pre><code>    SV* sv_bless(SV* sv, HV* stash);
</code></pre>
<p> The <code>&quot;sv&quot;</code> argument must be a reference value. The <code>&quot;stash&quot;</code> argument specifies which class the reference will belong to. See ``Stashes and Globs&#8217;&#8216; for information on converting class names into stashes. </p>
<p> /* Still under construction */ </p>
<p> The following function upgrades rv to reference if not already one. Creates a new <font SIZE="-1">SV</font> for rv to point to. If <code>&quot;classname&quot;</code> is non-null, the <font SIZE="-1">SV</font> is blessed into the specified class. <font SIZE="-1">SV</font> is returned. </p>
<pre><code>        SV* newSVrv(SV* rv, const char* classname);
</code></pre>
<p> The following three functions copy integer, unsigned integer or double into an <font SIZE="-1">SV</font> whose reference is <code>&quot;rv&quot;</code>. <font SIZE="-1">SV</font> is blessed if <code>&quot;classname&quot;</code> is non-null. </p>
<pre><code>        SV* sv_setref_iv(SV* rv, const char* classname, IV iv);
        SV* sv_setref_uv(SV* rv, const char* classname, UV uv);
        SV* sv_setref_nv(SV* rv, const char* classname, NV iv);
</code></pre>
<p> The following function copies the pointer value (<i>the address, not the string!</i>) into an <font SIZE="-1">SV</font> whose reference is rv. <font SIZE="-1">SV</font> is blessed if <code>&quot;classname&quot;</code> is non-null. </p>
<pre><code>        SV* sv_setref_pv(SV* rv, const char* classname, void* pv);
</code></pre>
<p> The following function copies a string into an <font SIZE="-1">SV</font> whose reference is <code>&quot;rv&quot;</code>. Set length to 0 to let Perl calculate the string length. <font SIZE="-1">SV</font> is blessed if <code>&quot;classname&quot;</code> is non-null. </p>
<pre><code>    SV* sv_setref_pvn(SV* rv, const char* classname, char* pv,
                                                         STRLEN length);
</code></pre>
<p> The following function tests whether the <font SIZE="-1">SV</font> is blessed into the specified class. It does not check inheritance relationships. </p>
<pre><code>        int sv_isa(SV* sv, const char* name);
</code></pre>
<p> The following function tests whether the <font SIZE="-1">SV</font> is a reference to a blessed object. </p>
<pre><code>        int sv_isobject(SV* sv);
</code></pre>
<p> The following function tests whether the <font SIZE="-1">SV</font> is derived from the specified class. <font SIZE="-1">SV</font> can be either a reference to a blessed object or a string containing a class name. This is the function implementing the <code>&quot;UNIVERSAL::isa&quot;</code> functionality. </p>
<pre><code>        bool sv_derived_from(SV* sv, const char* name);
</code></pre>
<p> To check if you&#8217;ve got an object derived from a specific class you have to write: </p>
<pre><code>        if (sv_isobject(sv) &amp;&amp; sv_derived_from(sv, class)) { ... }
</code></pre>
<h3>Creating New Variables</h3>
<p> To create a new Perl variable with an undef value which can be accessed from your Perl script, use the following routines, depending on the variable type. </p>
<pre><code>    SV* get_sv(&quot;package::varname&quot;, GV_ADD);
    AV* get_av(&quot;package::varname&quot;, GV_ADD);
    HV* get_hv(&quot;package::varname&quot;, GV_ADD);
</code></pre>
<p> Notice the use of <font SIZE="-1">GV_ADD</font> as the second parameter. The new variable can now be set, using the routines appropriate to the data type. </p>
<p> There are additional macros whose values may be bitwise <font SIZE="-1">OR</font>&#8216;ed with the <code>&quot;GV_ADD&quot;</code> argument to enable certain extra features. Those bits are: </p>
<dl>
<dt><font SIZE="-1">GV_ADDMULTI</font></dt>
<dd> <p> Marks the variable as multiply defined, thus preventing the: </p>
<pre><code>  Name &lt;varname&gt; used only once: possible typo
</code></pre>
<p> warning. </p>
 </dd>
<dt><font SIZE="-1">GV_ADDWARN</font></dt>
<dd> <p> Issues the warning: </p>
<pre><code>  Had to create &lt;varname&gt; unexpectedly
</code></pre>
<p> if the variable did not exist before the function was called. </p>
 </dd></dl>
<p> If you do not specify a package name, the variable is created in the current package.  </p>
<h3>Reference Counts and Mortality</h3>
<p> Perl uses a reference count-driven garbage collection mechanism. SVs, AVs, or HVs (xV for short in the following) start their life with a reference count of 1. If the reference count of an xV ever drops to 0, then it will be destroyed and its memory made available for reuse. At the most basic internal level, reference counts can be manipulated with the following macros: </p>
<pre><code>    int SvREFCNT(SV* sv);
    SV* SvREFCNT_inc(SV* sv);
    void SvREFCNT_dec(SV* sv);
</code></pre>
<p> (There are also suffixed versions of the increment and decrement macros, for situations where the full generality of these basic macros can be exchanged for some performance.) </p>
<p> However, the way a programmer should think about references is not so much in terms of the bare reference count, but in terms of <i>ownership</i> of references. A reference to an xV can be owned by any of a variety of entities: another xV, the Perl interpreter, an <font SIZE="-1">XS</font> data structure, a piece of running code, or a dynamic scope. An xV generally does not know what entities own the references to it; it only knows how many references there are, which is the reference count. </p>
<p> To correctly maintain reference counts, it is essential to keep track of what references the <font SIZE="-1">XS</font> code is manipulating. The programmer should always know where a reference has come from and who owns it, and be aware of any creation or destruction of references, and any transfers of ownership. Because ownership isn&#8217;t represented explicitly in the xV data structures, only the reference count need be actually maintained by the code, and that means that this understanding of ownership is not actually evident in the code. For example, transferring ownership of a reference from one owner to another doesn&#8217;t change the reference count at all, so may be achieved with no actual code. (The transferring code doesn&#8217;t touch the referenced object, but does need to ensure that the former owner knows that it no longer owns the reference, and that the new owner knows that it now does.) </p>
<p> An xV that is visible at the Perl level should not become unreferenced and thus be destroyed. Normally, an object will only become unreferenced when it is no longer visible, often by the same means that makes it invisible. For example, a Perl reference value (<font SIZE="-1">RV</font>) owns a reference to its referent, so if the <font SIZE="-1">RV</font> is overwritten that reference gets destroyed, and the no-longer-reachable referent may be destroyed as a result. </p>
<p> Many functions have some kind of reference manipulation as part of their purpose. Sometimes this is documented in terms of ownership of references, and sometimes it is (less helpfully) documented in terms of changes to reference counts. For example, the <code>newRV_inc()</code> function is documented to create a new <font SIZE="-1">RV</font> (with reference count 1) and increment the reference count of the referent that was supplied by the caller. This is best understood as creating a new reference to the referent, which is owned by the created <font SIZE="-1">RV,</font> and returning to the caller ownership of the sole reference to the <font SIZE="-1">RV.</font> The <code>newRV_noinc()</code> function instead does not increment the reference count of the referent, but the <font SIZE="-1">RV</font> nevertheless ends up owning a reference to the referent. It is therefore implied that the caller of <code>&quot;newRV_noinc()&quot;</code> is relinquishing a reference to the referent, making this conceptually a more complicated operation even though it does less to the data structures. </p>
<p> For example, imagine you want to return a reference from an <font SIZE="-1">XSUB</font> function. Inside the <font SIZE="-1">XSUB</font> routine, you create an <font SIZE="-1">SV</font> which initially has just a single reference, owned by the <font SIZE="-1">XSUB</font> routine. This reference needs to be disposed of before the routine is complete, otherwise it will leak, preventing the <font SIZE="-1">SV</font> from ever being destroyed. So to create an <font SIZE="-1">RV</font> referencing the <font SIZE="-1">SV,</font> it is most convenient to pass the <font SIZE="-1">SV</font> to <code>&quot;newRV_noinc()&quot;</code>, which consumes that reference. Now the <font SIZE="-1">XSUB</font> routine no longer owns a reference to the <font SIZE="-1">SV,</font> but does own a reference to the <font SIZE="-1">RV,</font> which in turn owns a reference to the <font SIZE="-1">SV.</font> The ownership of the reference to the <font SIZE="-1">RV</font> is then transferred by the process of returning the <font SIZE="-1">RV</font> from the <font SIZE="-1">XSUB.</font> </p>
<p> There are some convenience functions available that can help with the destruction of xVs. These functions introduce the concept of ``mortality&#8217;&#8216;. Much documentation speaks of an xV itself being mortal, but this is misleading. It is really <i>a reference to</i> an xV that is mortal, and it is possible for there to be more than one mortal reference to a single xV. For a reference to be mortal means that it is owned by the temps stack, one of perl&#8217;s many internal stacks, which will destroy that reference ``a short time later&#8217;&#8216;. Usually the ``short time later&#8217;&#8216; is the end of the current Perl statement. However, it gets more complicated around dynamic scopes: there can be multiple sets of mortal references hanging around at the same time, with different death dates. Internally, the actual determinant for when mortal xV references are destroyed depends on two macros, <font SIZE="-1">SAVETMPS</font> and <font SIZE="-1">FREETMPS.</font> See perlcall and perlxs for more details on these macros. </p>
<p> Mortal references are mainly used for xVs that are placed on perl&#8217;s main stack. The stack is problematic for reference tracking, because it contains a lot of xV references, but doesn&#8217;t own those references: they are not counted. Currently, there are many bugs resulting from xVs being destroyed while referenced by the stack, because the stack&#8217;s uncounted references aren&#8217;t enough to keep the xVs alive. So when putting an (uncounted) reference on the stack, it is vitally important to ensure that there will be a counted reference to the same xV that will last at least as long as the uncounted reference. But it&#8217;s also important that that counted reference be cleaned up at an appropriate time, and not unduly prolong the xV&#8217;s life. For there to be a mortal reference is often the best way to satisfy this requirement, especially if the xV was created especially to be put on the stack and would otherwise be unreferenced. </p>
<p> To create a mortal reference, use the functions: </p>
<pre><code>    SV* sv_newmortal()
    SV* sv_mortalcopy(SV*)
    SV* sv_2mortal(SV*)
</code></pre>
<p> <code>&quot;sv_newmortal()&quot;</code> creates an <font SIZE="-1">SV</font> (with the undefined value) whose sole reference is mortal. <code>&quot;sv_mortalcopy()&quot;</code> creates an xV whose value is a copy of a supplied xV and whose sole reference is mortal. <code>&quot;sv_2mortal()&quot;</code> mortalises an existing xV reference: it transfers ownership of a reference from the caller to the temps stack. Because <code>&quot;sv_newmortal&quot;</code> gives the new <font SIZE="-1">SV</font> no value, it must normally be given one via <code>&quot;sv_setpv&quot;</code>, <code>&quot;sv_setiv&quot;</code>, etc. : </p>
<pre><code>    SV *tmp = sv_newmortal();
    sv_setiv(tmp, an_integer);
</code></pre>
<p> As that is multiple C statements it is quite common so see this idiom instead: </p>
<pre><code>    SV *tmp = sv_2mortal(newSViv(an_integer));
</code></pre>
<p> The mortal routines are not just for SVs; AVs and HVs can be made mortal by passing their address (type-casted to <code>&quot;SV*&quot;</code>) to the <code>&quot;sv_2mortal&quot;</code> or <code>&quot;sv_mortalcopy&quot;</code> routines.  </p>
<h3>Stashes and Globs</h3>
<p> A <code>stash</code> is a hash that contains all variables that are defined within a package. Each key of the stash is a symbol name (shared by all the different types of objects that have the same name), and each value in the hash table is a <font SIZE="-1">GV</font> (Glob Value). This <font SIZE="-1">GV</font> in turn contains references to the various objects of that name, including (but not limited to) the following: </p>
<pre><code>    Scalar Value
    Array Value
    Hash Value
    I/O Handle
    Format
    Subroutine
</code></pre>
<p> There is a single stash called <code>&quot;PL_defstash&quot;</code> that holds the items that exist in the <code>&quot;main&quot;</code> package. To get at the items in other packages, append the string ``::&#8216;&#8216; to the package name. The items in the <code>&quot;Foo&quot;</code> package are in the stash <code>&quot;Foo::&quot;</code> in PL_defstash. The items in the <code>&quot;Bar::Baz&quot;</code> package are in the stash <code>&quot;Baz::&quot;</code> in <code>&quot;Bar::&quot;</code>&#8216;s stash. </p>
<p> To get the stash pointer for a particular package, use the function: </p>
<pre><code>    HV* gv_stashpv(const char* name, I32 flags)
    HV* gv_stashsv(SV*, I32 flags)
</code></pre>
<p> The first function takes a literal string, the second uses the string stored in the <font SIZE="-1">SV.</font> Remember that a stash is just a hash table, so you get back an <code>&quot;HV*&quot;</code>. The <code>&quot;flags&quot;</code> flag will create a new package if it is set to <font SIZE="-1">GV_ADD.</font> </p>
<p> The name that <code>&quot;gv_stash*v&quot;</code> wants is the name of the package whose symbol table you want. The default package is called <code>&quot;main&quot;</code>. If you have multiply nested packages, pass their names to <code>&quot;gv_stash*v&quot;</code>, separated by <code>&quot;::&quot;</code> as in the Perl language itself. </p>
<p> Alternately, if you have an <font SIZE="-1">SV</font> that is a blessed reference, you can find out the stash pointer by using: </p>
<pre><code>    HV* SvSTASH(SvRV(SV*));
</code></pre>
<p> then use the following to get the package name itself: </p>
<pre><code>    char* HvNAME(HV* stash);
</code></pre>
<p> If you need to bless or re-bless an object you can use the following function: </p>
<pre><code>    SV* sv_bless(SV*, HV* stash)
</code></pre>
<p> where the first argument, an <code>&quot;SV*&quot;</code>, must be a reference, and the second argument is a stash. The returned <code>&quot;SV*&quot;</code> can now be used in the same way as any other <font SIZE="-1">SV.</font> </p>
<p> For more information on references and blessings, consult perlref.  </p>
<h3>Double-Typed SVs</h3>
<p> Scalar variables normally contain only one type of value, an integer, double, pointer, or reference. Perl will automatically convert the actual scalar data from the stored type into the requested type. </p>
<p> Some scalar variables contain more than one type of scalar data. For example, the variable <code>$!</code> contains either the numeric value of <code>&quot;errno&quot;</code> or its string equivalent from either <code>&quot;strerror&quot;</code> or <code>&quot;sys_errlist[]&quot;</code>. </p>
<p> To force multiple data values into an <font SIZE="-1">SV,</font> you must do two things: use the <code>&quot;sv_set*v&quot;</code> routines to add the additional scalar type, then set a flag so that Perl will believe it contains more than one type of data. The four macros to set the flags are: </p>
<pre><code>        SvIOK_on
        SvNOK_on
        SvPOK_on
        SvROK_on
</code></pre>
<p> The particular macro you must use depends on which <code>&quot;sv_set*v&quot;</code> routine you called first. This is because every <code>&quot;sv_set*v&quot;</code> routine turns on only the bit for the particular type of data being set, and turns off all the rest. </p>
<p> For example, to create a new Perl variable called ``dberror&#8217;&#8216; that contains both the numeric and descriptive string error values, you could use the following code: </p>
<pre><code>    extern int dberror;
    extern char *dberror_list;
    SV* sv = get_sv(&quot;dberror&quot;, GV_ADD);
    sv_setiv(sv, (IV) dberror);
    sv_setpv(sv, dberror_list[dberror]);
    SvIOK_on(sv);
</code></pre>
<p> If the order of <code>&quot;sv_setiv&quot;</code> and <code>&quot;sv_setpv&quot;</code> had been reversed, then the macro <code>&quot;SvPOK_on&quot;</code> would need to be called instead of <code>&quot;SvIOK_on&quot;</code>.  </p>
<h3>Read-Only Values</h3>
<p> In Perl 5.16 and earlier, copy-on-write (see the next section) shared a flag bit with read-only scalars. So the only way to test whether <code>&quot;sv_setsv&quot;</code>, etc., will raise a ``Modification of a read-only value&#8217;&#8216; error in those versions is: </p>
<pre><code>    SvREADONLY(sv) &amp;&amp; !SvIsCOW(sv)
</code></pre>
<p> Under Perl 5.18 and later, SvREADONLY only applies to read-only variables, and, under 5.20, copy-on-write scalars can also be read-only, so the above check is incorrect. You just want: </p>
<pre><code>    SvREADONLY(sv)
</code></pre>
<p> If you need to do this check often, define your own macro like this: </p>
<pre><code>    #if PERL_VERSION &gt;= 18
    # define SvTRULYREADONLY(sv) SvREADONLY(sv)
    #else
    # define SvTRULYREADONLY(sv) (SvREADONLY(sv) &amp;&amp; !SvIsCOW(sv))
    #endif
</code></pre>
<h3>Copy on Write</h3>
<p> Perl implements a copy-on-write (<font SIZE="-1">COW</font>) mechanism for scalars, in which string copies are not immediately made when requested, but are deferred until made necessary by one or the other scalar changing. This is mostly transparent, but one must take care not to modify string buffers that are shared by multiple SVs. </p>
<p> You can test whether an <font SIZE="-1">SV</font> is using copy-on-write with <code>&quot;SvIsCOW(sv)&quot;</code>. </p>
<p> You can force an <font SIZE="-1">SV</font> to make its own copy of its string buffer by calling <code>&quot;sv_force_normal(sv)&quot;</code> or SvPV_force_nolen(sv). </p>
<p> If you want to make the <font SIZE="-1">SV</font> drop its string buffer, use <code>&quot;sv_force_normal_flags(sv, SV_COW_DROP_PV)&quot;</code> or simply <code>&quot;sv_setsv(sv, NULL)&quot;</code>. </p>
<p> All of these functions will croak on read-only scalars (see the previous section for more on those). </p>
<p> To test that your code is behaving correctly and not modifying <font SIZE="-1">COW</font> buffers, on systems that support <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) (i.e., Unix) you can configure perl with <code>&quot;-Accflags=-DPERL_DEBUG_READONLY_COW&quot;</code> and it will turn buffer violations into crashes. You will find it to be marvellously slow, so you may want to skip perl&#8217;s own tests.  </p>
<h3>Magic Variables</h3>
<p> [This section still under construction. Ignore everything here. Post no bills. Everything not permitted is forbidden.] </p>
<p> Any <font SIZE="-1">SV</font> may be magical, that is, it has special features that a normal <font SIZE="-1">SV</font> does not have. These features are stored in the <font SIZE="-1">SV</font> structure in a linked list of <code>&quot;struct magic&quot;</code>&#8216;s, typedef&#8217;ed to <code>&quot;MAGIC&quot;</code>. </p>
<pre><code>    struct magic {
        MAGIC* mg_moremagic;
        MGVTBL* mg_virtual;
        U16 mg_private;
        char mg_type;
        U8 mg_flags;
        I32 mg_len;
        SV* mg_obj;
        char* mg_ptr;
    };
</code></pre>
<p> Note this is current as of patchlevel 0, and could change at any time.  </p>
<h3>Assigning Magic</h3>
<p> Perl adds magic to an <font SIZE="-1">SV</font> using the sv_magic function: </p>
<pre><code>  void sv_magic(SV* sv, SV* obj, int how, const char* name, I32 namlen);
</code></pre>
<p> The <code>&quot;sv&quot;</code> argument is a pointer to the <font SIZE="-1">SV</font> that is to acquire a new magical feature. </p>
<p> If <code>&quot;sv&quot;</code> is not already magical, Perl uses the <code>&quot;SvUPGRADE&quot;</code> macro to convert <code>&quot;sv&quot;</code> to type <code>&quot;SVt_PVMG&quot;</code>. Perl then continues by adding new magic to the beginning of the linked list of magical features. Any prior entry of the same type of magic is deleted. Note that this can be overridden, and multiple instances of the same type of magic can be associated with an <font SIZE="-1">SV.</font> </p>
<p> The <code>&quot;name&quot;</code> and <code>&quot;namlen&quot;</code> arguments are used to associate a string with the magic, typically the name of a variable. <code>&quot;namlen&quot;</code> is stored in the <code>&quot;mg_len&quot;</code> field and if <code>&quot;name&quot;</code> is non-null then either a <code>&quot;savepvn&quot;</code> copy of <code>&quot;name&quot;</code> or <code>&quot;name&quot;</code> itself is stored in the <code>&quot;mg_ptr&quot;</code> field, depending on whether <code>&quot;namlen&quot;</code> is greater than zero or equal to zero respectively. As a special case, if <code>&quot;(name &amp;&amp; namlen == HEf_SVKEY)&quot;</code> then <code>&quot;name&quot;</code> is assumed to contain an <code>&quot;SV*&quot;</code> and is stored as-is with its <font SIZE="-1">REFCNT</font> incremented. </p>
<p> The sv_magic function uses <code>&quot;how&quot;</code> to determine which, if any, predefined ``Magic Virtual Table&#8217;&#8216; should be assigned to the <code>&quot;mg_virtual&quot;</code> field. See the ``Magic Virtual Tables&#8217;&#8216; section below. The <code>&quot;how&quot;</code> argument is also stored in the <code>&quot;mg_type&quot;</code> field. The value of <code>&quot;how&quot;</code> should be chosen from the set of macros <code>&quot;PERL_MAGIC_foo&quot;</code> found in <i>perl.h</i>. Note that before these macros were added, Perl internals used to directly use character literals, so you may occasionally come across old code or documentation referring to &#8216;U&#8217; magic rather than <code>&quot;PERL_MAGIC_uvar&quot;</code> for example. </p>
<p> The <code>&quot;obj&quot;</code> argument is stored in the <code>&quot;mg_obj&quot;</code> field of the <code>&quot;MAGIC&quot;</code> structure. If it is not the same as the <code>&quot;sv&quot;</code> argument, the reference count of the <code>&quot;obj&quot;</code> object is incremented. If it is the same, or if the <code>&quot;how&quot;</code> argument is <code>&quot;PERL_MAGIC_arylen&quot;</code>, <code>&quot;PERL_MAGIC_regdatum&quot;</code>, <code>&quot;PERL_MAGIC_regdata&quot;</code>, or if it is a <font SIZE="-1">NULL</font> pointer, then <code>&quot;obj&quot;</code> is merely stored, without the reference count being incremented. </p>
<p> See also <code>&quot;sv_magicext&quot;</code> in perlapi for a more flexible way to add magic to an <font SIZE="-1">SV.</font> </p>
<p> There is also a function to add magic to an <code>&quot;HV&quot;</code>: </p>
<pre><code>    void hv_magic(HV *hv, GV *gv, int how);
</code></pre>
<p> This simply calls <code>&quot;sv_magic&quot;</code> and coerces the <code>&quot;gv&quot;</code> argument into an <code>&quot;SV&quot;</code>. </p>
<p> To remove the magic from an <font SIZE="-1">SV,</font> call the function sv_unmagic: </p>
<pre><code>    int sv_unmagic(SV *sv, int type);
</code></pre>
<p> The <code>&quot;type&quot;</code> argument should be equal to the <code>&quot;how&quot;</code> value when the <code>&quot;SV&quot;</code> was initially made magical. </p>
<p> However, note that <code>&quot;sv_unmagic&quot;</code> removes all magic of a certain <code>&quot;type&quot;</code> from the <code>&quot;SV&quot;</code>. If you want to remove only certain magic of a <code>&quot;type&quot;</code> based on the magic virtual table, use <code>&quot;sv_unmagicext&quot;</code> instead: </p>
<pre><code>    int sv_unmagicext(SV *sv, int type, MGVTBL *vtbl);
</code></pre>
<h3>Magic Virtual Tables</h3>
<p> The <code>&quot;mg_virtual&quot;</code> field in the <code>&quot;MAGIC&quot;</code> structure is a pointer to an <code>&quot;MGVTBL&quot;</code>, which is a structure of function pointers and stands for ``Magic Virtual Table&#8217;&#8216; to handle the various operations that might be applied to that variable. </p>
<p> The <code>&quot;MGVTBL&quot;</code> has five (or sometimes eight) pointers to the following routine types: </p>
<pre><code>    int (*svt_get) (pTHX_ SV* sv, MAGIC* mg);
    int (*svt_set) (pTHX_ SV* sv, MAGIC* mg);
    U32 (*svt_len) (pTHX_ SV* sv, MAGIC* mg);
    int (*svt_clear)(pTHX_ SV* sv, MAGIC* mg);
    int (*svt_free) (pTHX_ SV* sv, MAGIC* mg);
    int (*svt_copy) (pTHX_ SV *sv, MAGIC* mg, SV *nsv,
                                          const char *name, I32 namlen);
    int (*svt_dup) (pTHX_ MAGIC *mg, CLONE_PARAMS *param);
    int (*svt_local)(pTHX_ SV *nsv, MAGIC *mg);
</code></pre>
<p> This <font SIZE="-1">MGVTBL</font> structure is set at compile-time in <i>perl.h</i> and there are currently 32 types. These different structures contain pointers to various routines that perform additional actions depending on which function is being called. </p>
<pre><code>   Function pointer Action taken
   ---------------- ------------
   svt_get Do something before the value of the SV is
                       retrieved.
   svt_set Do something after the SV is assigned a value.
   svt_len Report on the SV's length.
   svt_clear Clear something the SV represents.
   svt_free Free any extra storage associated with the SV.
   svt_copy copy tied variable magic to a tied element
   svt_dup duplicate a magic structure during thread cloning
   svt_local copy magic to local value during 'local'
</code></pre>
<p> For instance, the <font SIZE="-1">MGVTBL</font> structure called <code>&quot;vtbl_sv&quot;</code> (which corresponds to an <code>&quot;mg_type&quot;</code> of <code>&quot;PERL_MAGIC_sv&quot;</code>) contains: </p>
<pre><code>    { magic_get, magic_set, magic_len, 0, 0 }
</code></pre>
<p> Thus, when an <font SIZE="-1">SV</font> is determined to be magical and of type <code>&quot;PERL_MAGIC_sv&quot;</code>, if a get operation is being performed, the routine <code>&quot;magic_get&quot;</code> is called. All the various routines for the various magical types begin with <code>&quot;magic_&quot;</code>. <font SIZE="-1">NOTE:</font> the magic routines are not considered part of the Perl <font SIZE="-1">API,</font> and may not be exported by the Perl library. </p>
<p> The last three slots are a recent addition, and for source code compatibility they are only checked for if one of the three flags MGf_COPY, MGf_DUP or MGf_LOCAL is set in mg_flags. This means that most code can continue declaring a vtable as a 5-element value. These three are currently used exclusively by the threading code, and are highly subject to change. </p>
<p> The current kinds of Magic Virtual Tables are: </p>
<pre><code> mg_type
 (old-style char and macro) MGVTBL Type of magic
 -------------------------- ------ -------------
 \0 PERL_MAGIC_sv vtbl_sv Special scalar variable
 # PERL_MAGIC_arylen vtbl_arylen Array length ($#ary)
 % PERL_MAGIC_rhash (none) Extra data for restricted
                                             hashes
 * PERL_MAGIC_debugvar vtbl_debugvar $DB::single, signal, trace
                                             vars
 . PERL_MAGIC_pos vtbl_pos pos() lvalue
 : PERL_MAGIC_symtab (none) Extra data for symbol
                                             tables
 &lt; PERL_MAGIC_backref vtbl_backref For weak ref data
 @ PERL_MAGIC_arylen_p (none) To move arylen out of XPVAV
 B PERL_MAGIC_bm vtbl_regexp Boyer-Moore
                                             (fast string search)
 c PERL_MAGIC_overload_table vtbl_ovrld Holds overload table
                                             (AMT) on stash
 D PERL_MAGIC_regdata vtbl_regdata Regex match position data
                                             (@+ and @- vars)
 d PERL_MAGIC_regdatum vtbl_regdatum Regex match position data
                                             element
 E PERL_MAGIC_env vtbl_env %ENV hash
 e PERL_MAGIC_envelem vtbl_envelem %ENV hash element
 f PERL_MAGIC_fm vtbl_regexp Formline
                                             ('compiled' format)
 g PERL_MAGIC_regex_global vtbl_mglob m//g target
 H PERL_MAGIC_hints vtbl_hints %^H hash
 h PERL_MAGIC_hintselem vtbl_hintselem %^H hash element
 I PERL_MAGIC_isa vtbl_isa @ISA array
 i PERL_MAGIC_isaelem vtbl_isaelem @ISA array element
 k PERL_MAGIC_nkeys vtbl_nkeys scalar(keys()) lvalue
 L PERL_MAGIC_dbfile (none) Debugger %_&lt;filename
 l PERL_MAGIC_dbline vtbl_dbline Debugger %_&lt;filename
                                             element
 N PERL_MAGIC_shared (none) Shared between threads
 n PERL_MAGIC_shared_scalar (none) Shared between threads
 o PERL_MAGIC_collxfrm vtbl_collxfrm Locale transformation
 P PERL_MAGIC_tied vtbl_pack Tied array or hash
 p PERL_MAGIC_tiedelem vtbl_packelem Tied array or hash element
 q PERL_MAGIC_tiedscalar vtbl_packelem Tied scalar or handle
 r PERL_MAGIC_qr vtbl_regexp Precompiled qr// regex
 S PERL_MAGIC_sig (none) %SIG hash
 s PERL_MAGIC_sigelem vtbl_sigelem %SIG hash element
 t PERL_MAGIC_taint vtbl_taint Taintedness
 U PERL_MAGIC_uvar vtbl_uvar Available for use by
                                             extensions
 u PERL_MAGIC_uvar_elem (none) Reserved for use by
                                             extensions
 V PERL_MAGIC_vstring (none) SV was vstring literal
 v PERL_MAGIC_vec vtbl_vec vec() lvalue
 w PERL_MAGIC_utf8 vtbl_utf8 Cached UTF-8 information
 x PERL_MAGIC_substr vtbl_substr substr() lvalue
 Y PERL_MAGIC_nonelem vtbl_nonelem Array element that does not
                                             exist
 y PERL_MAGIC_defelem vtbl_defelem Shadow &quot;foreach&quot; iterator
                                             variable / smart parameter
                                             vivification
 \ PERL_MAGIC_lvref vtbl_lvref Lvalue reference
                                             constructor
 ] PERL_MAGIC_checkcall vtbl_checkcall Inlining/mutation of call
                                             to this CV
 ~ PERL_MAGIC_ext (none) Available for use by
                                             extensions
</code></pre>
<p> When an uppercase and lowercase letter both exist in the table, then the uppercase letter is typically used to represent some kind of composite type (a list or a hash), and the lowercase letter is used to represent an element of that composite type. Some internals code makes use of this case relationship. However, &#8216;v&#8217; and &#8216;V&#8217; (vec and v-string) are in no way related. </p>
<p> The <code>&quot;PERL_MAGIC_ext&quot;</code> and <code>&quot;PERL_MAGIC_uvar&quot;</code> magic types are defined specifically for use by extensions and will not be used by perl itself. Extensions can use <code>&quot;PERL_MAGIC_ext&quot;</code> magic to &#8216;attach&#8217; private information to variables (typically objects). This is especially useful because there is no way for normal perl code to corrupt this private information (unlike using extra elements of a hash object). </p>
<p> Similarly, <code>&quot;PERL_MAGIC_uvar&quot;</code> magic can be used much like <code>tie()</code> to call a C function any time a scalar&#8217;s value is used or changed. The <code>&quot;MAGIC&quot;</code>&#8216;s <code>&quot;mg_ptr&quot;</code> field points to a <code>&quot;ufuncs&quot;</code> structure: </p>
<pre><code>    struct ufuncs {
        I32 (*uf_val)(pTHX_ IV, SV*);
        I32 (*uf_set)(pTHX_ IV, SV*);
        IV uf_index;
    };
</code></pre>
<p> When the <font SIZE="-1">SV</font> is read from or written to, the <code>&quot;uf_val&quot;</code> or <code>&quot;uf_set&quot;</code> function will be called with <code>&quot;uf_index&quot;</code> as the first arg and a pointer to the <font SIZE="-1">SV</font> as the second. A simple example of how to add <code>&quot;PERL_MAGIC_uvar&quot;</code> magic is shown below. Note that the ufuncs structure is copied by sv_magic, so you can safely allocate it on the stack. </p>
<pre><code>    void
    Umagic(sv)
        SV *sv;
    PREINIT:
        struct ufuncs uf;
    CODE:
        uf.uf_val = &amp;my_get_fn;
        uf.uf_set = &amp;my_set_fn;
        uf.uf_index = 0;
        sv_magic(sv, 0, PERL_MAGIC_uvar, (char*)&amp;uf, sizeof(uf));
</code></pre>
<p> Attaching <code>&quot;PERL_MAGIC_uvar&quot;</code> to arrays is permissible but has no effect. </p>
<p> For hashes there is a specialized hook that gives control over hash keys (but not values). This hook calls <code>&quot;PERL_MAGIC_uvar&quot;</code> &#8216;get&#8217; magic if the ``set&#8217;&#8216; function in the <code>&quot;ufuncs&quot;</code> structure is <font SIZE="-1">NULL.</font> The hook is activated whenever the hash is accessed with a key specified as an <code>&quot;SV&quot;</code> through the functions <code>&quot;hv_store_ent&quot;</code>, <code>&quot;hv_fetch_ent&quot;</code>, <code>&quot;hv_delete_ent&quot;</code>, and <code>&quot;hv_exists_ent&quot;</code>. Accessing the key as a string through the functions without the <code>&quot;..._ent&quot;</code> suffix circumvents the hook. See ``<font SIZE="-1">GUTS&#8217;&#8216;</font> in Hash::Util::FieldHash for a detailed description. </p>
<p> Note that because multiple extensions may be using <code>&quot;PERL_MAGIC_ext&quot;</code> or <code>&quot;PERL_MAGIC_uvar&quot;</code> magic, it is important for extensions to take extra care to avoid conflict. Typically only using the magic on objects blessed into the same class as the extension is sufficient. For <code>&quot;PERL_MAGIC_ext&quot;</code> magic, it is usually a good idea to define an <code>&quot;MGVTBL&quot;</code>, even if all its fields will be <code>0</code>, so that individual <code>&quot;MAGIC&quot;</code> pointers can be identified as a particular kind of magic using their magic virtual table. <code>&quot;mg_findext&quot;</code> provides an easy way to do that: </p>
<pre><code>    STATIC MGVTBL my_vtbl = { 0, 0, 0, 0, 0, 0, 0, 0 };
    MAGIC *mg;
    if ((mg = mg_findext(sv, PERL_MAGIC_ext, &amp;my_vtbl))) {
        /* this is really ours, not another module's PERL_MAGIC_ext */
        my_priv_data_t *priv = (my_priv_data_t *)mg-&gt;mg_ptr;
        ...
    }
</code></pre>
<p> Also note that the <code>&quot;sv_set*()&quot;</code> and <code>&quot;sv_cat*()&quot;</code> functions described earlier do <code>not</code> invoke &#8216;set&#8217; magic on their targets. This must be done by the user either by calling the <code>&quot;SvSETMAGIC()&quot;</code> macro after calling these functions, or by using one of the <code>&quot;sv_set*_mg()&quot;</code> or <code>&quot;sv_cat*_mg()&quot;</code> functions. Similarly, generic C code must call the <code>&quot;SvGETMAGIC()&quot;</code> macro to invoke any &#8216;get&#8217; magic if they use an <font SIZE="-1">SV</font> obtained from external sources in functions that don&#8217;t handle magic. See perlapi for a description of these functions. For example, calls to the <code>&quot;sv_cat*()&quot;</code> functions typically need to be followed by <code>&quot;SvSETMAGIC()&quot;</code>, but they don&#8217;t need a prior <code>&quot;SvGETMAGIC()&quot;</code> since their implementation handles &#8216;get&#8217; magic.  </p>
<h3>Finding Magic</h3>
<pre><code>    MAGIC *mg_find(SV *sv, int type); /* Finds the magic pointer of that
                                       * type */
</code></pre>
<p> This routine returns a pointer to a <code>&quot;MAGIC&quot;</code> structure stored in the <font SIZE="-1">SV.</font> If the <font SIZE="-1">SV</font> does not have that magical feature, <code>&quot;NULL&quot;</code> is returned. If the <font SIZE="-1">SV</font> has multiple instances of that magical feature, the first one will be returned. <code>&quot;mg_findext&quot;</code> can be used to find a <code>&quot;MAGIC&quot;</code> structure of an <font SIZE="-1">SV</font> based on both its magic type and its magic virtual table: </p>
<pre><code>    MAGIC *mg_findext(SV *sv, int type, MGVTBL *vtbl);
</code></pre>
<p> Also, if the <font SIZE="-1">SV</font> passed to <code>&quot;mg_find&quot;</code> or <code>&quot;mg_findext&quot;</code> is not of type SVt_PVMG, Perl may core dump. </p>
<pre><code>    int mg_copy(SV* sv, SV* nsv, const char* key, STRLEN klen);
</code></pre>
<p> This routine checks to see what types of magic <code>&quot;sv&quot;</code> has. If the mg_type field is an uppercase letter, then the mg_obj is copied to <code>&quot;nsv&quot;</code>, but the mg_type field is changed to be the lowercase letter.  </p>
<h3>Understanding the Magic of Tied Hashes and Arrays</h3>
<p> Tied hashes and arrays are magical beasts of the <code>&quot;PERL_MAGIC_tied&quot;</code> magic type. </p>
<p> <font SIZE="-1">WARNING:</font> As of the 5.004 release, proper usage of the array and hash access functions requires understanding a few caveats. Some of these caveats are actually considered bugs in the <font SIZE="-1">API,</font> to be fixed in later releases, and are bracketed with [<font SIZE="-1">MAYCHANGE</font>] below. If you find yourself actually applying such information in this section, be aware that the behavior may change in the future, umm, without warning. </p>
<p> The perl tie function associates a variable with an object that implements the various <font SIZE="-1">GET, SET,</font> etc methods. To perform the equivalent of the perl tie function from an <font SIZE="-1">XSUB,</font> you must mimic this behaviour. The code below carries out the necessary steps --- firstly it creates a new hash, and then creates a second hash which it blesses into the class which will implement the tie methods. Lastly it ties the two hashes together, and returns a reference to the new tied hash. Note that the code below does <font SIZE="-1">NOT</font> call the <font SIZE="-1">TIEHASH</font> method in the MyTie class &#8211; see ``Calling Perl Routines from within C Programs&#8217;&#8216; for details on how to do this. </p>
<pre><code>    SV*
    mytie()
    PREINIT:
        HV *hash;
        HV *stash;
        SV *tie;
    CODE:
        hash = newHV();
        tie = newRV_noinc((SV*)newHV());
        stash = gv_stashpv(&quot;MyTie&quot;, GV_ADD);
        sv_bless(tie, stash);
        hv_magic(hash, (GV*)tie, PERL_MAGIC_tied);
        RETVAL = newRV_noinc(hash);
    OUTPUT:
        RETVAL
</code></pre>
<p> The <code>&quot;av_store&quot;</code> function, when given a tied array argument, merely copies the magic of the array onto the value to be ``stored&#8217;&#8216;, using <code>&quot;mg_copy&quot;</code>. It may also return <font SIZE="-1">NULL,</font> indicating that the value did not actually need to be stored in the array. [<font SIZE="-1">MAYCHANGE</font>] After a call to <code>&quot;av_store&quot;</code> on a tied array, the caller will usually need to call <code>&quot;mg_set(val)&quot;</code> to actually invoke the perl level ``<font SIZE="-1">STORE&#8217;&#8216;</font> method on the <font SIZE="-1">TIEARRAY</font> object. If <code>&quot;av_store&quot;</code> did return <font SIZE="-1">NULL,</font> a call to <code>&quot;SvREFCNT_dec(val)&quot;</code> will also be usually necessary to avoid a memory leak. [/MAYCHANGE] </p>
<p> The previous paragraph is applicable verbatim to tied hash access using the <code>&quot;hv_store&quot;</code> and <code>&quot;hv_store_ent&quot;</code> functions as well. </p>
<p> <code>&quot;av_fetch&quot;</code> and the corresponding hash functions <code>&quot;hv_fetch&quot;</code> and <code>&quot;hv_fetch_ent&quot;</code> actually return an undefined mortal value whose magic has been initialized using <code>&quot;mg_copy&quot;</code>. Note the value so returned does not need to be deallocated, as it is already mortal. [<font SIZE="-1">MAYCHANGE</font>] But you will need to call <code>&quot;mg_get()&quot;</code> on the returned value in order to actually invoke the perl level ``<font SIZE="-1">FETCH&#8217;&#8216;</font> method on the underlying <font SIZE="-1">TIE</font> object. Similarly, you may also call <code>&quot;mg_set()&quot;</code> on the return value after possibly assigning a suitable value to it using <code>&quot;sv_setsv&quot;</code>, which will invoke the ``<font SIZE="-1">STORE&#8217;&#8216;</font> method on the <font SIZE="-1">TIE</font> object. [/MAYCHANGE] </p>
<p> [<font SIZE="-1">MAYCHANGE</font>] In other words, the array or hash fetch/store functions don&#8217;t really fetch and store actual values in the case of tied arrays and hashes. They merely call <code>&quot;mg_copy&quot;</code> to attach magic to the values that were meant to be ``stored&#8217;&#8216; or ``fetched&#8217;&#8216;. Later calls to <code>&quot;mg_get&quot;</code> and <code>&quot;mg_set&quot;</code> actually do the job of invoking the <font SIZE="-1">TIE</font> methods on the underlying objects. Thus the magic mechanism currently implements a kind of lazy access to arrays and hashes. </p>
<p> Currently (as of perl version 5.004), use of the hash and array access functions requires the user to be aware of whether they are operating on ``normal&#8217;&#8216; hashes and arrays, or on their tied variants. The <font SIZE="-1">API</font> may be changed to provide more transparent access to both tied and normal data types in future versions. [/MAYCHANGE] </p>
<p> You would do well to understand that the <font SIZE="-1">TIEARRAY</font> and <font SIZE="-1">TIEHASH</font> interfaces are mere sugar to invoke some perl method calls while using the uniform hash and array syntax. The use of this sugar imposes some overhead (typically about two to four extra opcodes per <font SIZE="-1">FETCH/STORE</font> operation, in addition to the creation of all the mortal variables required to invoke the methods). This overhead will be comparatively small if the <font SIZE="-1">TIE</font> methods are themselves substantial, but if they are only a few statements long, the overhead will not be insignificant.  </p>
<h3>Localizing changes</h3>
<p> Perl has a very handy construction </p>
<pre><code>  {
    local $var = 2;
    ...
  }
</code></pre>
<p> This construction is <i>approximately</i> equivalent to </p>
<pre><code>  {
    my $oldvar = $var;
    $var = 2;
    ...
    $var = $oldvar;
  }
</code></pre>
<p> The biggest difference is that the first construction would reinstate the initial value of <code>$var</code>, irrespective of how control exits the block: <code>&quot;goto&quot;</code>, <code>&quot;return&quot;</code>, <code>&quot;die&quot;</code>/<code>&quot;eval&quot;</code>, etc. It is a little bit more efficient as well. </p>
<p> There is a way to achieve a similar task from C via Perl <font SIZE="-1">API:</font> create a <i>pseudo-block</i>, and arrange for some changes to be automatically undone at the end of it, either explicit, or via a non-local exit (via <code>die()</code>). A <i>block</i>-like construct is created by a pair of <code>&quot;ENTER&quot;</code>/<code>&quot;LEAVE&quot;</code> macros (see ``Returning a Scalar&#8217;&#8216; in perlcall). Such a construct may be created specially for some important localized task, or an existing one (like boundaries of enclosing Perl subroutine/block, or an existing pair for freeing TMPs) may be used. (In the second case the overhead of additional localization must be almost negligible.) Note that any <font SIZE="-1">XSUB</font> is automatically enclosed in an <code>&quot;ENTER&quot;</code>/<code>&quot;LEAVE&quot;</code> pair. </p>
<p> Inside such a <i>pseudo-block</i> the following service is available: </p>
<dl>
<dt>&quot;SAVEINT(int i)&quot;</dt>
<dd>  </dd>
<dt>&quot;SAVEIV(IV i)&quot;</dt>
<dd>  </dd>
<dt>&quot;SAVEI32(I32 i)&quot;</dt>
<dd>  </dd>
<dt>&quot;SAVELONG(long i)&quot;</dt>
<dd> <p> These macros arrange things to restore the value of integer variable <code>&quot;i&quot;</code> at the end of enclosing <i>pseudo-block</i>. </p>
 </dd>
<dt>SAVESPTR(s)</dt>
<dd>  </dd>
<dt>SAVEPPTR(p)</dt>
<dd> <p> These macros arrange things to restore the value of pointers <code>&quot;s&quot;</code> and <code>&quot;p&quot;</code>. <code>&quot;s&quot;</code> must be a pointer of a type which survives conversion to <code>&quot;SV*&quot;</code> and back, <code>&quot;p&quot;</code> should be able to survive conversion to <code>&quot;char*&quot;</code> and back. </p>
 </dd>
<dt>&quot;SAVEFREESV(SV *sv)&quot;</dt>
<dd> <p> The refcount of <code>&quot;sv&quot;</code> will be decremented at the end of <i>pseudo-block</i>. This is similar to <code>&quot;sv_2mortal&quot;</code> in that it is also a mechanism for doing a delayed <code>&quot;SvREFCNT_dec&quot;</code>. However, while <code>&quot;sv_2mortal&quot;</code> extends the lifetime of <code>&quot;sv&quot;</code> until the beginning of the next statement, <code>&quot;SAVEFREESV&quot;</code> extends it until the end of the enclosing scope. These lifetimes can be wildly different. </p>
<p> Also compare <code>&quot;SAVEMORTALIZESV&quot;</code>. </p>
 </dd>
<dt>&quot;SAVEMORTALIZESV(SV *sv)&quot;</dt>
<dd> <p> Just like <code>&quot;SAVEFREESV&quot;</code>, but mortalizes <code>&quot;sv&quot;</code> at the end of the current scope instead of decrementing its reference count. This usually has the effect of keeping <code>&quot;sv&quot;</code> alive until the statement that called the currently live scope has finished executing. </p>
 </dd>
<dt>&quot;SAVEFREEOP(OP *op)&quot;</dt>
<dd> <p> The <code>&quot;OP *&quot;</code> is <code>op_free()</code>ed at the end of <i>pseudo-block</i>. </p>
 </dd>
<dt>SAVEFREEPV(p)</dt>
<dd> <p> The chunk of memory which is pointed to by <code>&quot;p&quot;</code> is <code>Safefree()</code>ed at the end of <i>pseudo-block</i>. </p>
 </dd>
<dt>&quot;SAVECLEARSV(SV *sv)&quot;</dt>
<dd> <p> Clears a slot in the current scratchpad which corresponds to <code>&quot;sv&quot;</code> at the end of <i>pseudo-block</i>. </p>
 </dd>
<dt>&quot;SAVEDELETE(HV *hv, char *key, I32 length)&quot;</dt>
<dd> <p> The key <code>&quot;key&quot;</code> of <code>&quot;hv&quot;</code> is deleted at the end of <i>pseudo-block</i>. The string pointed to by <code>&quot;key&quot;</code> is <code>Safefree()</code>ed. If one has a <i>key</i> in short-lived storage, the corresponding string may be reallocated like this: </p>
<pre><code>  SAVEDELETE(PL_defstash, savepv(tmpbuf), strlen(tmpbuf));
</code></pre>
 </dd>
<dt>&quot;SAVEDESTRUCTOR(DESTRUCTORFUNC_NOCONTEXT_t f, void *p)&quot;</dt>
<dd> <p> At the end of <i>pseudo-block</i> the function <code>&quot;f&quot;</code> is called with the only argument <code>&quot;p&quot;</code>. </p>
 </dd>
<dt>&quot;SAVEDESTRUCTOR_X(DESTRUCTORFUNC_t f, void *p)&quot;</dt>
<dd> <p> At the end of <i>pseudo-block</i> the function <code>&quot;f&quot;</code> is called with the implicit context argument (if any), and <code>&quot;p&quot;</code>. </p>
 </dd>
<dt>&quot;SAVESTACK_POS()&quot;</dt>
<dd> <p> The current offset on the Perl internal stack (cf. <code>&quot;SP&quot;</code>) is restored at the end of <i>pseudo-block</i>. </p>
 </dd></dl>
<p> The following <font SIZE="-1">API</font> list contains functions, thus one needs to provide pointers to the modifiable data explicitly (either C pointers, or Perlish <code>&quot;GV *&quot;</code>s). Where the above macros take <code>&quot;int&quot;</code>, a similar function takes <code>&quot;int *&quot;</code>. </p>
<dl>
<dt>&quot;SV* save_scalar(GV *gv)&quot;</dt>
<dd> <p> Equivalent to Perl code <code>&quot;local $gv&quot;</code>. </p>
 </dd>
<dt>&quot;AV* save_ary(GV *gv)&quot;</dt>
<dd>  </dd>
<dt>&quot;HV* save_hash(GV *gv)&quot;</dt>
<dd> <p> Similar to <code>&quot;save_scalar&quot;</code>, but localize <code>@gv</code> and <code>%gv</code>. </p>
 </dd>
<dt>&quot;void save_item(SV *item)&quot;</dt>
<dd> <p> Duplicates the current value of <code>&quot;SV&quot;</code>, on the exit from the current <code>&quot;ENTER&quot;</code>/<code>&quot;LEAVE&quot;</code> <i>pseudo-block</i> will restore the value of <code>&quot;SV&quot;</code> using the stored value. It doesn&#8217;t handle magic. Use <code>&quot;save_scalar&quot;</code> if magic is affected. </p>
 </dd>
<dt>&quot;void save_list(SV **sarg, I32 maxsarg)&quot;</dt>
<dd> <p> A variant of <code>&quot;save_item&quot;</code> which takes multiple arguments via an array <code>&quot;sarg&quot;</code> of <code>&quot;SV*&quot;</code> of length <code>&quot;maxsarg&quot;</code>. </p>
 </dd>
<dt>&quot;SV* save_svref(SV **sptr)&quot;</dt>
<dd> <p> Similar to <code>&quot;save_scalar&quot;</code>, but will reinstate an <code>&quot;SV *&quot;</code>. </p>
 </dd>
<dt>&quot;void save_aptr(AV **aptr)&quot;</dt>
<dd>  </dd>
<dt>&quot;void save_hptr(HV **hptr)&quot;</dt>
<dd> <p> Similar to <code>&quot;save_svref&quot;</code>, but localize <code>&quot;AV *&quot;</code> and <code>&quot;HV *&quot;</code>. </p>
 </dd></dl>
<p> The <code>&quot;Alias&quot;</code> module implements localization of the basic types within the <i>caller&#8217;s scope</i>. People who are interested in how to localize things in the containing scope should take a look there too.  </p>
<h2>Subroutines</h2>
<h3>XSUBs and the Argument Stack</h3>
<p> The <font SIZE="-1">XSUB</font> mechanism is a simple way for Perl programs to access C subroutines. An <font SIZE="-1">XSUB</font> routine will have a stack that contains the arguments from the Perl program, and a way to map from the Perl data structures to a C equivalent. </p>
<p> The stack arguments are accessible through the <code><a href="/docs/linux/man/n-ST/">ST</a>(n)</code> macro, which returns the <code>&quot;n&quot;</code>&#8216;th stack argument. Argument 0 is the first argument passed in the Perl subroutine call. These arguments are <code>&quot;SV*&quot;</code>, and can be used anywhere an <code>&quot;SV*&quot;</code> is used. </p>
<p> Most of the time, output from the C routine can be handled through use of the <font SIZE="-1">RETVAL</font> and <font SIZE="-1">OUTPUT</font> directives. However, there are some cases where the argument stack is not already long enough to handle all the return values. An example is the <font SIZE="-1">POSIX</font> <code>tzname()</code> call, which takes no arguments, but returns two, the local time zone&#8217;s standard and summer time abbreviations. </p>
<p> To handle this situation, the <font SIZE="-1">PPCODE</font> directive is used and the stack is extended using the macro: </p>
<pre><code>    EXTEND(SP, num);
</code></pre>
<p> where <code>&quot;SP&quot;</code> is the macro that represents the local copy of the stack pointer, and <code>&quot;num&quot;</code> is the number of elements the stack should be extended by. </p>
<p> Now that there is room on the stack, values can be pushed on it using <code>&quot;PUSHs&quot;</code> macro. The pushed values will often need to be ``mortal&#8217;&#8216; (See ``Reference Counts and Mortality&#8217;&#8216;): </p>
<pre><code>    PUSHs(sv_2mortal(newSViv(an_integer)))
    PUSHs(sv_2mortal(newSVuv(an_unsigned_integer)))
    PUSHs(sv_2mortal(newSVnv(a_double)))
    PUSHs(sv_2mortal(newSVpv(&quot;Some String&quot;,0)))
    /* Although the last example is better written as the more
     * efficient: */
    PUSHs(newSVpvs_flags(&quot;Some String&quot;, SVs_TEMP))
</code></pre>
<p> And now the Perl program calling <code>&quot;tzname&quot;</code>, the two values will be assigned as in: </p>
<pre><code>    ($standard_abbrev, $summer_abbrev) = POSIX::tzname;
</code></pre>
<p> An alternate (and possibly simpler) method to pushing values on the stack is to use the macro: </p>
<pre><code>    XPUSHs(SV*)
</code></pre>
<p> This macro automatically adjusts the stack for you, if needed. Thus, you do not need to call <code>&quot;EXTEND&quot;</code> to extend the stack. </p>
<p> Despite their suggestions in earlier versions of this document the macros <code>&quot;(X)PUSH[iunp]&quot;</code> are <i>not</i> suited to XSUBs which return multiple results. For that, either stick to the <code>&quot;(X)PUSHs&quot;</code> macros shown above, or use the new <code>&quot;m(X)PUSH[iunp]&quot;</code> macros instead; see ``Putting a C value on Perl stack&#8217;&#8216;. </p>
<p> For more information, consult perlxs and perlxstut.  </p>
<h3>Autoloading with XSUBs</h3>
<p> If an <font SIZE="-1">AUTOLOAD</font> routine is an <font SIZE="-1">XSUB,</font> as with Perl subroutines, Perl puts the fully-qualified name of the autoloaded subroutine in the <code>$AUTOLOAD</code> variable of the <font SIZE="-1">XSUB</font>&#8216;s package. </p>
<p> But it also puts the same information in certain fields of the <font SIZE="-1">XSUB</font> itself: </p>
<pre><code>    HV *stash = CvSTASH(cv);
    const char *subname = SvPVX(cv);
    STRLEN name_length = SvCUR(cv); /* in bytes */
    U32 is_utf8 = SvUTF8(cv);
</code></pre>
<p> <code>&quot;SvPVX(cv)&quot;</code> contains just the sub name itself, not including the package. For an <font SIZE="-1">AUTOLOAD</font> routine in <font SIZE="-1">UNIVERSAL</font> or one of its superclasses, <code>&quot;CvSTASH(cv)&quot;</code> returns <font SIZE="-1">NULL</font> during a method call on a nonexistent package. </p>
<p> <code>Note</code>: Setting <code>$AUTOLOAD</code> stopped working in 5.6.1, which did not support <font SIZE="-1">XS AUTOLOAD</font> subs at all. Perl 5.8.0 introduced the use of fields in the <font SIZE="-1">XSUB</font> itself. Perl 5.16.0 restored the setting of <code>$AUTOLOAD</code>. If you need to support 5.8-5.14, use the <font SIZE="-1">XSUB</font>&#8216;s fields.  </p>
<h3>Calling Perl Routines from within C Programs</h3>
<p> There are four routines that can be used to call a Perl subroutine from within a C program. These four are: </p>
<pre><code>    I32 call_sv(SV*, I32);
    I32 call_pv(const char*, I32);
    I32 call_method(const char*, I32);
    I32 call_argv(const char*, I32, char**);
</code></pre>
<p> The routine most often used is <code>&quot;call_sv&quot;</code>. The <code>&quot;SV*&quot;</code> argument contains either the name of the Perl subroutine to be called, or a reference to the subroutine. The second argument consists of flags that control the context in which the subroutine is called, whether or not the subroutine is being passed arguments, how errors should be trapped, and how to treat return values. </p>
<p> All four routines return the number of arguments that the subroutine returned on the Perl stack. </p>
<p> These routines used to be called <code>&quot;perl_call_sv&quot;</code>, etc., before Perl v5.6.0, but those names are now deprecated; macros of the same name are provided for compatibility. </p>
<p> When using any of these routines (except <code>&quot;call_argv&quot;</code>), the programmer must manipulate the Perl stack. These include the following macros and functions: </p>
<pre><code>    dSP
    SP
    PUSHMARK()
    PUTBACK
    SPAGAIN
    ENTER
    SAVETMPS
    FREETMPS
    LEAVE
    XPUSH*()
    POP*()
</code></pre>
<p> For a detailed description of calling conventions from C to Perl, consult perlcall.  </p>
<h3>Putting a C value on Perl stack</h3>
<p> A lot of opcodes (this is an elementary operation in the internal perl stack machine) put an SV* on the stack. However, as an optimization the corresponding <font SIZE="-1">SV</font> is (usually) not recreated each time. The opcodes reuse specially assigned SVs (<i>target</i>s) which are (as a corollary) not constantly freed/created. </p>
<p> Each of the targets is created only once (but see ``Scratchpads and recursion&#8217;&#8216; below), and when an opcode needs to put an integer, a double, or a string on stack, it just sets the corresponding parts of its <i>target</i> and puts the <i>target</i> on stack. </p>
<p> The macro to put this target on stack is <code>&quot;PUSHTARG&quot;</code>, and it is directly used in some opcodes, as well as indirectly in zillions of others, which use it via <code>&quot;(X)PUSH[iunp]&quot;</code>. </p>
<p> Because the target is reused, you must be careful when pushing multiple values on the stack. The following code will not do what you think: </p>
<pre><code>    XPUSHi(10);
    XPUSHi(20);
</code></pre>
<p> This translates as &quot;set <code>&quot;TARG&quot;</code> to 10, push a pointer to <code>&quot;TARG&quot;</code> onto the stack; set <code>&quot;TARG&quot;</code> to 20, push a pointer to <code>&quot;TARG&quot;</code> onto the stack&quot;. At the end of the operation, the stack does not contain the values 10 and 20, but actually contains two pointers to <code>&quot;TARG&quot;</code>, which we have set to 20. </p>
<p> If you need to push multiple different values then you should either use the <code>&quot;(X)PUSHs&quot;</code> macros, or else use the new <code>&quot;m(X)PUSH[iunp]&quot;</code> macros, none of which make use of <code>&quot;TARG&quot;</code>. The <code>&quot;(X)PUSHs&quot;</code> macros simply push an SV* on the stack, which, as noted under ``XSUBs and the Argument Stack&#8217;&#8216;, will often need to be ``mortal&#8217;&#8216;. The new <code>&quot;m(X)PUSH[iunp]&quot;</code> macros make this a little easier to achieve by creating a new mortal for you (via <code>&quot;(X)PUSHmortal&quot;</code>), pushing that onto the stack (extending it if necessary in the case of the <code>&quot;mXPUSH[iunp]&quot;</code> macros), and then setting its value. Thus, instead of writing this to ``fix&#8217;&#8216; the example above: </p>
<pre><code>    XPUSHs(sv_2mortal(newSViv(10)))
    XPUSHs(sv_2mortal(newSViv(20)))
</code></pre>
<p> you can simply write: </p>
<pre><code>    mXPUSHi(10)
    mXPUSHi(20)
</code></pre>
<p> On a related note, if you do use <code>&quot;(X)PUSH[iunp]&quot;</code>, then you&#8217;re going to need a <code>&quot;dTARG&quot;</code> in your variable declarations so that the <code>&quot;*PUSH*&quot;</code> macros can make use of the local variable <code>&quot;TARG&quot;</code>. See also <code>&quot;dTARGET&quot;</code> and <code>&quot;dXSTARG&quot;</code>.  </p>
<h3>Scratchpads</h3>
<p> The question remains on when the SVs which are <i>target</i>s for opcodes are created. The answer is that they are created when the current unit---a subroutine or a file (for opcodes for statements outside of subroutines)--is compiled. During this time a special anonymous Perl array is created, which is called a scratchpad for the current unit. </p>
<p> A scratchpad keeps SVs which are lexicals for the current unit and are targets for opcodes. A previous version of this document stated that one can deduce that an <font SIZE="-1">SV</font> lives on a scratchpad by looking on its flags: lexicals have <code>&quot;SVs_PADMY&quot;</code> set, and <i>target</i>s have <code>&quot;SVs_PADTMP&quot;</code> set. But this has never been fully true. <code>&quot;SVs_PADMY&quot;</code> could be set on a variable that no longer resides in any pad. While <i>target</i>s do have <code>&quot;SVs_PADTMP&quot;</code> set, it can also be set on variables that have never resided in a pad, but nonetheless act like <i>target</i>s. As of perl 5.21.5, the <code>&quot;SVs_PADMY&quot;</code> flag is no longer used and is defined as 0. <code>&quot;SvPADMY()&quot;</code> now returns true for anything without <code>&quot;SVs_PADTMP&quot;</code>. </p>
<p> The correspondence between OPs and <i>target</i>s is not 1-to-1. Different OPs in the compile tree of the unit can use the same target, if this would not conflict with the expected life of the temporary.  </p>
<h3>Scratchpads and recursion</h3>
<p> In fact it is not 100% true that a compiled unit contains a pointer to the scratchpad <font SIZE="-1">AV.</font> In fact it contains a pointer to an <font SIZE="-1">AV</font> of (initially) one element, and this element is the scratchpad <font SIZE="-1">AV.</font> Why do we need an extra level of indirection? </p>
<p> The answer is <code>recursion</code>, and maybe <code>threads</code>. Both these can create several execution pointers going into the same subroutine. For the subroutine-child not write over the temporaries for the subroutine-parent (lifespan of which covers the call to the child), the parent and the child should have different scratchpads. (<i>And</i> the lexicals should be separate anyway!) </p>
<p> So each subroutine is born with an array of scratchpads (of length 1). On each entry to the subroutine it is checked that the current depth of the recursion is not more than the length of this array, and if it is, new scratchpad is created and pushed into the array. </p>
<p> The <i>target</i>s on this scratchpad are <code>&quot;undef&quot;</code>s, but they are already marked with correct flags.  </p>
<h2>Memory Allocation</h2>
<h3>Allocation</h3>
<p> All memory meant to be used with the Perl <font SIZE="-1">API</font> functions should be manipulated using the macros described in this section. The macros provide the necessary transparency between differences in the actual malloc implementation that is used within perl. </p>
<p> It is suggested that you enable the version of malloc that is distributed with Perl. It keeps pools of various sizes of unallocated memory in order to satisfy allocation requests more quickly. However, on some platforms, it may cause spurious malloc or free errors. </p>
<p> The following three macros are used to initially allocate memory : </p>
<pre><code>    Newx(pointer, number, type);
    Newxc(pointer, number, type, cast);
    Newxz(pointer, number, type);
</code></pre>
<p> The first argument <code>&quot;pointer&quot;</code> should be the name of a variable that will point to the newly allocated memory. </p>
<p> The second and third arguments <code>&quot;number&quot;</code> and <code>&quot;type&quot;</code> specify how many of the specified type of data structure should be allocated. The argument <code>&quot;type&quot;</code> is passed to <code>&quot;sizeof&quot;</code>. The final argument to <code>&quot;Newxc&quot;</code>, <code>&quot;cast&quot;</code>, should be used if the <code>&quot;pointer&quot;</code> argument is different from the <code>&quot;type&quot;</code> argument. </p>
<p> Unlike the <code>&quot;Newx&quot;</code> and <code>&quot;Newxc&quot;</code> macros, the <code>&quot;Newxz&quot;</code> macro calls <code>&quot;memzero&quot;</code> to zero out all the newly allocated memory.  </p>
<h3>Reallocation</h3>
<pre><code>    Renew(pointer, number, type);
    Renewc(pointer, number, type, cast);
    Safefree(pointer)
</code></pre>
<p> These three macros are used to change a memory buffer size or to free a piece of memory no longer needed. The arguments to <code>&quot;Renew&quot;</code> and <code>&quot;Renewc&quot;</code> match those of <code>&quot;New&quot;</code> and <code>&quot;Newc&quot;</code> with the exception of not needing the ``magic cookie&#8217;&#8216; argument.  </p>
<h3>Moving</h3>
<pre><code>    Move(source, dest, number, type);
    Copy(source, dest, number, type);
    Zero(dest, number, type);
</code></pre>
<p> These three macros are used to move, copy, or zero out previously allocated memory. The <code>&quot;source&quot;</code> and <code>&quot;dest&quot;</code> arguments point to the source and destination starting points. Perl will move, copy, or zero out <code>&quot;number&quot;</code> instances of the size of the <code>&quot;type&quot;</code> data structure (using the <code>&quot;sizeof&quot;</code> function).  </p>
<h2>PerlIO</h2>
<p> The most recent development releases of Perl have been experimenting with removing Perl&#8217;s dependency on the ``normal&#8217;&#8216; standard I/O suite and allowing other stdio implementations to be used. This involves creating a new abstraction layer that then calls whichever implementation of stdio Perl was compiled with. All XSUBs should now use the functions in the PerlIO abstraction layer and not make any assumptions about what kind of stdio is being used. </p>
<p> For a complete description of the PerlIO abstraction, consult perlapio.  </p>
<h2>Compiled code</h2>
<h3>Code tree</h3>
<p> Here we describe the internal form your code is converted to by Perl. Start with a simple example: </p>
<pre><code>  $a = $b + $c;
</code></pre>
<p> This is converted to a tree similar to this one: </p>
<pre><code>             assign-to
           / \
          + $a
        / \
      $b $c
</code></pre>
<p> (but slightly more complicated). This tree reflects the way Perl parsed your code, but has nothing to do with the execution order. There is an additional ``thread&#8217;&#8216; going through the nodes of the tree which shows the order of execution of the nodes. In our simplified example above it looks like: </p>
<pre><code>     $b ---&gt; $c ---&gt; + ---&gt; $a ---&gt; assign-to
</code></pre>
<p> But with the actual compile tree for <code>&quot;$a = $b + $c&quot;</code> it is different: some nodes <i>optimized away</i>. As a corollary, though the actual tree contains more nodes than our simplified example, the execution order is the same as in our example.  </p>
<h3>Examining the tree</h3>
<p> If you have your perl compiled for debugging (usually done with <code>&quot;-DDEBUGGING&quot;</code> on the <code>&quot;Configure&quot;</code> command line), you may examine the compiled tree by specifying <code>&quot;-Dx&quot;</code> on the Perl command line. The output takes several lines per node, and for <code>&quot;$b+$c&quot;</code> it looks like this: </p>
<pre><code>    5 TYPE = add ===&gt; 6
                TARG = 1
                FLAGS = (SCALAR,KIDS)
                {
                    TYPE = null ===&gt; (4)
                      (was rv2sv)
                    FLAGS = (SCALAR,KIDS)
                    {
    3 TYPE = gvsv ===&gt; 4
                        FLAGS = (SCALAR)
                        GV = main::b
                    }
                }
                {
                    TYPE = null ===&gt; (5)
                      (was rv2sv)
                    FLAGS = (SCALAR,KIDS)
                    {
    4 TYPE = gvsv ===&gt; 5
                        FLAGS = (SCALAR)
                        GV = main::c
                    }
                }
</code></pre>
<p> This tree has 5 nodes (one per <code>&quot;TYPE&quot;</code> specifier), only 3 of them are not optimized away (one per number in the left column). The immediate children of the given node correspond to <code>&quot;{}&quot;</code> pairs on the same level of indentation, thus this listing corresponds to the tree: </p>
<pre><code>                   add
                 / \
               null null
                | |
               gvsv gvsv
</code></pre>
<p> The execution order is indicated by <code>&quot;===&gt;&quot;</code> marks, thus it is <code>&quot;3 4 5 6&quot;</code> (node <code>6</code> is not included into above listing), i.e., <code>&quot;gvsv gvsv add whatever&quot;</code>. </p>
<p> Each of these nodes represents an op, a fundamental operation inside the Perl core. The code which implements each operation can be found in the <i>pp*.c</i> files; the function which implements the op with type <code>&quot;gvsv&quot;</code> is <code>&quot;pp_gvsv&quot;</code>, and so on. As the tree above shows, different ops have different numbers of children: <code>&quot;add&quot;</code> is a binary operator, as one would expect, and so has two children. To accommodate the various different numbers of children, there are various types of op data structure, and they link together in different ways. </p>
<p> The simplest type of op structure is <code>&quot;OP&quot;</code>: this has no children. Unary operators, <code>&quot;UNOP&quot;</code>s, have one child, and this is pointed to by the <code>&quot;op_first&quot;</code> field. Binary operators (<code>&quot;BINOP&quot;</code>s) have not only an <code>&quot;op_first&quot;</code> field but also an <code>&quot;op_last&quot;</code> field. The most complex type of op is a <code>&quot;LISTOP&quot;</code>, which has any number of children. In this case, the first child is pointed to by <code>&quot;op_first&quot;</code> and the last child by <code>&quot;op_last&quot;</code>. The children in between can be found by iteratively following the <code>&quot;OpSIBLING&quot;</code> pointer from the first child to the last (but see below). </p>
<p> There are also some other op types: a <code>&quot;PMOP&quot;</code> holds a regular expression, and has no children, and a <code>&quot;LOOP&quot;</code> may or may not have children. If the <code>&quot;op_children&quot;</code> field is non-zero, it behaves like a <code>&quot;LISTOP&quot;</code>. To complicate matters, if a <code>&quot;UNOP&quot;</code> is actually a <code>&quot;null&quot;</code> op after optimization (see ``Compile pass 2: context propagation&#8217;&#8216;) it will still have children in accordance with its former type. </p>
<p> Finally, there is a <code>&quot;LOGOP&quot;</code>, or logic op. Like a <code>&quot;LISTOP&quot;</code>, this has one or more children, but it doesn&#8217;t have an <code>&quot;op_last&quot;</code> field: so you have to follow <code>&quot;op_first&quot;</code> and then the <code>&quot;OpSIBLING&quot;</code> chain itself to find the last child. Instead it has an <code>&quot;op_other&quot;</code> field, which is comparable to the <code>&quot;op_next&quot;</code> field described below, and represents an alternate execution path. Operators like <code>&quot;and&quot;</code>, <code>&quot;or&quot;</code> and <code>&quot;?&quot;</code> are <code>&quot;LOGOP&quot;</code>s. Note that in general, <code>&quot;op_other&quot;</code> may not point to any of the direct children of the <code>&quot;LOGOP&quot;</code>. </p>
<p> Starting in version 5.21.2, perls built with the experimental define <code>&quot;-DPERL_OP_PARENT&quot;</code> add an extra boolean flag for each op, <code>&quot;op_moresib&quot;</code>. When not set, this indicates that this is the last op in an <code>&quot;OpSIBLING&quot;</code> chain. This frees up the <code>&quot;op_sibling&quot;</code> field on the last sibling to point back to the parent op. Under this build, that field is also renamed <code>&quot;op_sibparent&quot;</code> to reflect its joint role. The macro <code>OpSIBLING(o)</code> wraps this special behaviour, and always returns <font SIZE="-1">NULL</font> on the last sibling. With this build the <code>op_parent(o)</code> function can be used to find the parent of any op. Thus for forward compatibility, you should always use the <code>OpSIBLING(o)</code> macro rather than accessing <code>&quot;op_sibling&quot;</code> directly. </p>
<p> Another way to examine the tree is to use a compiler back-end module, such as B::Concise.  </p>
<h3>Compile pass 1: check routines</h3>
<p> The tree is created by the compiler while <i>yacc</i> code feeds it the constructions it recognizes. Since <i>yacc</i> works bottom-up, so does the first pass of perl compilation. </p>
<p> What makes this pass interesting for perl developers is that some optimization may be performed on this pass. This is optimization by so-called ``check routines&#8217;&#8216;. The correspondence between node names and corresponding check routines is described in <i>opcode.pl</i> (do not forget to run <code>&quot;make regen_headers&quot;</code> if you modify this file). </p>
<p> A check routine is called when the node is fully constructed except for the execution-order thread. Since at this time there are no back-links to the currently constructed node, one can do most any operation to the top-level node, including freeing it and/or creating new nodes above/below it. </p>
<p> The check routine returns the node which should be inserted into the tree (if the top-level node was not modified, check routine returns its argument). </p>
<p> By convention, check routines have names <code>&quot;ck_*&quot;</code>. They are usually called from <code>&quot;new*OP&quot;</code> subroutines (or <code>&quot;convert&quot;</code>) (which in turn are called from <i>perly.y</i>).  </p>
<h3>Compile pass 1a: constant folding</h3>
<p> Immediately after the check routine is called the returned node is checked for being compile-time executable. If it is (the value is judged to be constant) it is immediately executed, and a <i>constant</i> node with the ``return value&#8217;&#8216; of the corresponding subtree is substituted instead. The subtree is deleted. </p>
<p> If constant folding was not performed, the execution-order thread is created.  </p>
<h3>Compile pass 2: context propagation</h3>
<p> When a context for a part of compile tree is known, it is propagated down through the tree. At this time the context can have 5 values (instead of 2 for runtime context): void, boolean, scalar, list, and lvalue. In contrast with the pass 1 this pass is processed from top to bottom: a node&#8217;s context determines the context for its children. </p>
<p> Additional context-dependent optimizations are performed at this time. Since at this moment the compile tree contains back-references (via ``thread&#8217;&#8216; pointers), nodes cannot be <code>free()</code>d now. To allow optimized-away nodes at this stage, such nodes are <code>null()</code>ified instead of <code>free()</code>ing (i.e. their type is changed to <font SIZE="-1">OP_NULL</font>).  </p>
<h3>Compile pass 3: peephole optimization</h3>
<p> After the compile tree for a subroutine (or for an <code>&quot;eval&quot;</code> or a file) is created, an additional pass over the code is performed. This pass is neither top-down or bottom-up, but in the execution order (with additional complications for conditionals). Optimizations performed at this stage are subject to the same restrictions as in the pass 2. </p>
<p> Peephole optimizations are done by calling the function pointed to by the global variable <code>&quot;PL_peepp&quot;</code>. By default, <code>&quot;PL_peepp&quot;</code> just calls the function pointed to by the global variable <code>&quot;PL_rpeepp&quot;</code>. By default, that performs some basic op fixups and optimisations along the execution-order op chain, and recursively calls <code>&quot;PL_rpeepp&quot;</code> for each side chain of ops (resulting from conditionals). Extensions may provide additional optimisations or fixups, hooking into either the per-subroutine or recursive stage, like this: </p>
<pre><code>    static peep_t prev_peepp;
    static void my_peep(pTHX_ OP *o)
    {
        /* custom per-subroutine optimisation goes here */
        prev_peepp(aTHX_ o);
        /* custom per-subroutine optimisation may also go here */
    }
    BOOT:
        prev_peepp = PL_peepp;
        PL_peepp = my_peep;
    static peep_t prev_rpeepp;
    static void my_rpeep(pTHX_ OP *o)
    {
        OP *orig_o = o;
        for(; o; o = o-&gt;op_next) {
            /* custom per-op optimisation goes here */
        }
        prev_rpeepp(aTHX_ orig_o);
    }
    BOOT:
        prev_rpeepp = PL_rpeepp;
        PL_rpeepp = my_rpeep;
</code></pre>
<h3>Pluggable runops</h3>
<p> The compile tree is executed in a runops function. There are two runops functions, in <i>run.c</i> and in <i>dump.c</i>. <code>&quot;Perl_runops_debug&quot;</code> is used with <font SIZE="-1">DEBUGGING</font> and <code>&quot;Perl_runops_standard&quot;</code> is used otherwise. For fine control over the execution of the compile tree it is possible to provide your own runops function. </p>
<p> It&#8217;s probably best to copy one of the existing runops functions and change it to suit your needs. Then, in the <font SIZE="-1">BOOT</font> section of your <font SIZE="-1">XS</font> file, add the line: </p>
<pre><code>  PL_runops = my_runops;
</code></pre>
<p> This function should be as efficient as possible to keep your programs running as fast as possible.  </p>
<h3>Compile-time scope hooks</h3>
<p> As of perl 5.14 it is possible to hook into the compile-time lexical scope mechanism using <code>&quot;Perl_blockhook_register&quot;</code>. This is used like this: </p>
<pre><code>    STATIC void my_start_hook(pTHX_ int full);
    STATIC BHK my_hooks;
    BOOT:
        BhkENTRY_set(&amp;my_hooks, bhk_start, my_start_hook);
        Perl_blockhook_register(aTHX_ &amp;my_hooks);
</code></pre>
<p> This will arrange to have <code>&quot;my_start_hook&quot;</code> called at the start of compiling every lexical scope. The available hooks are: </p>
<dl>
<dt>&quot;void bhk_start(pTHX_ int full)&quot;</dt>
<dd> <p> This is called just after starting a new lexical scope. Note that Perl code like </p>
<pre><code>    if ($x) { ... }
</code></pre>
<p> creates two scopes: the first starts at the <code>&quot;(&quot;</code> and has <code>&quot;full == 1&quot;</code>, the second starts at the <code>&quot;{&quot;</code> and has <code>&quot;full == 0&quot;</code>. Both end at the <code>&quot;}&quot;</code>, so calls to <code>&quot;start&quot;</code> and <code>&quot;pre&quot;</code>/<code>&quot;post_end&quot;</code> will match. Anything pushed onto the save stack by this hook will be popped just before the scope ends (between the <code>&quot;pre_&quot;</code> and <code>&quot;post_end&quot;</code> hooks, in fact). </p>
 </dd>
<dt>&quot;void bhk_pre_end(pTHX_ OP **o)&quot;</dt>
<dd> <p> This is called at the end of a lexical scope, just before unwinding the stack. <i>o</i> is the root of the optree representing the scope; it is a double pointer so you can replace the <font SIZE="-1">OP</font> if you need to. </p>
 </dd>
<dt>&quot;void bhk_post_end(pTHX_ OP **o)&quot;</dt>
<dd> <p> This is called at the end of a lexical scope, just after unwinding the stack. <i>o</i> is as above. Note that it is possible for calls to <code>&quot;pre_&quot;</code> and <code>&quot;post_end&quot;</code> to nest, if there is something on the save stack that calls string eval. </p>
 </dd>
<dt>&quot;void bhk_eval(pTHX_ OP *const o)&quot;</dt>
<dd> <p> This is called just before starting to compile an <code>&quot;eval STRING&quot;</code>, <code>&quot;do FILE&quot;</code>, <code>&quot;require&quot;</code> or <code>&quot;use&quot;</code>, after the eval has been set up. <i>o</i> is the <font SIZE="-1">OP</font> that requested the eval, and will normally be an <code>&quot;OP_ENTEREVAL&quot;</code>, <code>&quot;OP_DOFILE&quot;</code> or <code>&quot;OP_REQUIRE&quot;</code>. </p>
 </dd></dl>
<p> Once you have your hook functions, you need a <code>&quot;BHK&quot;</code> structure to put them in. It&#8217;s best to allocate it statically, since there is no way to free it once it&#8217;s registered. The function pointers should be inserted into this structure using the <code>&quot;BhkENTRY_set&quot;</code> macro, which will also set flags indicating which entries are valid. If you do need to allocate your <code>&quot;BHK&quot;</code> dynamically for some reason, be sure to zero it before you start. </p>
<p> Once registered, there is no mechanism to switch these hooks off, so if that is necessary you will need to do this yourself. An entry in <code>&quot;%^H&quot;</code> is probably the best way, so the effect is lexically scoped; however it is also possible to use the <code>&quot;BhkDISABLE&quot;</code> and <code>&quot;BhkENABLE&quot;</code> macros to temporarily switch entries on and off. You should also be aware that generally speaking at least one scope will have opened before your extension is loaded, so you will see some <code>&quot;pre&quot;</code>/<code>&quot;post_end&quot;</code> pairs that didn&#8217;t have a matching <code>&quot;start&quot;</code>.  </p>
<h2>Examining internal data structures with the dump functions</h2>
<p> To aid debugging, the source file <i>dump.c</i> contains a number of functions which produce formatted output of internal data structures. </p>
<p> The most commonly used of these functions is <code>&quot;Perl_sv_dump&quot;</code>; it&#8217;s used for dumping SVs, AVs, HVs, and CVs. The <code>&quot;Devel::Peek&quot;</code> module calls <code>&quot;sv_dump&quot;</code> to produce debugging output from Perl-space, so users of that module should already be familiar with its format. </p>
<p> <code>&quot;Perl_op_dump&quot;</code> can be used to dump an <code>&quot;OP&quot;</code> structure or any of its derivatives, and produces output similar to <code>&quot;perl -Dx&quot;</code>; in fact, <code>&quot;Perl_dump_eval&quot;</code> will dump the main root of the code being evaluated, exactly like <code>&quot;-Dx&quot;</code>. </p>
<p> Other useful functions are <code>&quot;Perl_dump_sub&quot;</code>, which turns a <code>&quot;GV&quot;</code> into an op tree, <code>&quot;Perl_dump_packsubs&quot;</code> which calls <code>&quot;Perl_dump_sub&quot;</code> on all the subroutines in a package like so: (Thankfully, these are all xsubs, so there is no op tree) </p>
<pre><code>    (gdb) print Perl_dump_packsubs(PL_defstash)
    SUB attributes::bootstrap = (xsub 0x811fedc 0)
    SUB UNIVERSAL::can = (xsub 0x811f50c 0)
    SUB UNIVERSAL::isa = (xsub 0x811f304 0)
    SUB UNIVERSAL::VERSION = (xsub 0x811f7ac 0)
    SUB DynaLoader::boot_DynaLoader = (xsub 0x805b188 0)
</code></pre>
<p> and <code>&quot;Perl_dump_all&quot;</code>, which dumps all the subroutines in the stash and the op tree of the main root.  </p>
<h2>How multiple interpreters and concurrency are supported</h2>
<font SIZE="-1"></font><h3>Background and PERL_IMPLICIT_CONTEXT</h3>
<p> The Perl interpreter can be regarded as a closed box: it has an <font SIZE="-1">API</font> for feeding it code or otherwise making it do things, but it also has functions for its own use. This smells a lot like an object, and there are ways for you to build Perl so that you can have multiple interpreters, with one interpreter represented either as a C structure, or inside a thread-specific structure. These structures contain all the context, the state of that interpreter. </p>
<p> One macro controls the major Perl build flavor: <font SIZE="-1">MULTIPLICITY.</font> The <font SIZE="-1">MULTIPLICITY</font> build has a C structure that packages all the interpreter state. With multiplicity-enabled perls, <font SIZE="-1">PERL_IMPLICIT_CONTEXT</font> is also normally defined, and enables the support for passing in a ``hidden&#8217;&#8216; first argument that represents all three data structures. <font SIZE="-1">MULTIPLICITY</font> makes multi-threaded perls possible (with the ithreads threading model, related to the macro <font SIZE="-1">USE_ITHREADS.</font>) </p>
<p> Two other ``encapsulation&#8217;&#8216; macros are the <font SIZE="-1">PERL_GLOBAL_STRUCT</font> and <font SIZE="-1">PERL_GLOBAL_STRUCT_PRIVATE</font> (the latter turns on the former, and the former turns on <font SIZE="-1">MULTIPLICITY.</font>) The <font SIZE="-1">PERL_GLOBAL_STRUCT</font> causes all the internal variables of Perl to be wrapped inside a single global struct, struct perl_vars, accessible as (globals) &amp;PL_Vars or PL_VarsPtr or the function <code>Perl_GetVars()</code>. The <font SIZE="-1">PERL_GLOBAL_STRUCT_PRIVATE</font> goes one step further, there is still a single struct (allocated in <code>main()</code> either from heap or from stack) but there are no global data symbols pointing to it. In either case the global struct should be initialized as the very first thing in <code>main()</code> using <code>Perl_init_global_struct()</code> and correspondingly tear it down after <code>perl_free()</code> using <code>Perl_free_global_struct()</code>, please see <i>miniperlmain.c</i> for usage details. You may also need to use <code>&quot;dVAR&quot;</code> in your coding to ``declare the global variables&#8217;&#8216; when you are using them. dTHX does this for you automatically. </p>
<p> To see whether you have non-const data you can use a <font SIZE="-1">BSD</font> (or <font SIZE="-1">GNU</font>) compatible <code>&quot;nm&quot;</code>: </p>
<pre><code>  nm libperl.a | grep -v ' [TURtr] '
</code></pre>
<p> If this displays any <code>&quot;D&quot;</code> or <code>&quot;d&quot;</code> symbols (or possibly <code>&quot;C&quot;</code> or <code>&quot;c&quot;</code>), you have non-const data. The symbols the <code>&quot;grep&quot;</code> removed are as follows: <code>&quot;Tt&quot;</code> are <i>text</i>, or code, the <code>&quot;Rr&quot;</code> are <i>read-only</i> (const) data, and the <code>&quot;U&quot;</code> is &lt;undefined&gt;, external symbols referred to. </p>
<p> The test <i>t/porting/libperl.t</i> does this kind of symbol sanity checking on <code>&quot;libperl.a&quot;</code>. </p>
<p> For backward compatibility reasons defining just <font SIZE="-1">PERL_GLOBAL_STRUCT</font> doesn&#8217;t actually hide all symbols inside a big global struct: some PerlIO_xxx vtables are left visible. The <font SIZE="-1">PERL_GLOBAL_STRUCT_PRIVATE</font> then hides everything (see how the <font SIZE="-1">PERLIO_FUNCS_DECL</font> is used). </p>
<p> All this obviously requires a way for the Perl internal functions to be either subroutines taking some kind of structure as the first argument, or subroutines taking nothing as the first argument. To enable these two very different ways of building the interpreter, the Perl source (as it does in so many other situations) makes heavy use of macros and subroutine naming conventions. </p>
<p> First problem: deciding which functions will be public <font SIZE="-1">API</font> functions and which will be private. All functions whose names begin <code>&quot;S_&quot;</code> are private (think ``S&#8217;&#8216; for ``secret&#8217;&#8216; or ``static&#8217;&#8216;). All other functions begin with ``Perl_&#8216;&#8216;, but just because a function begins with ``Perl_&#8216;&#8216; does not mean it is part of the <font SIZE="-1">API.</font> (See ``Internal Functions&#8217;&#8216;.) The easiest way to be <code>sure</code> a function is part of the <font SIZE="-1">API</font> is to find its entry in perlapi. If it exists in perlapi, it&#8217;s part of the <font SIZE="-1">API.</font> If it doesn&#8217;t, and you think it should be (i.e., you need it for your extension), send mail via perlbug explaining why you think it should be. </p>
<p> Second problem: there must be a syntax so that the same subroutine declarations and calls can pass a structure as their first argument, or pass nothing. To solve this, the subroutines are named and declared in a particular way. Here&#8217;s a typical start of a static function used within the Perl guts: </p>
<pre><code>  STATIC void
  S_incline(pTHX_ char *s)
</code></pre>
<p> <font SIZE="-1">STATIC</font> becomes ``static&#8217;&#8216; in C, and may be #define&#8217;d to nothing in some configurations in the future. </p>
<p> A public function (i.e. part of the internal <font SIZE="-1">API,</font> but not necessarily sanctioned for use in extensions) begins like this: </p>
<pre><code>  void
  Perl_sv_setiv(pTHX_ SV* dsv, IV num)
</code></pre>
<p> <code>&quot;pTHX_&quot;</code> is one of a number of macros (in <i>perl.h</i>) that hide the details of the interpreter&#8217;s context. <font SIZE="-1">THX</font> stands for ``thread&#8217;&#8216;, ``this&#8217;&#8216;, or ``thingy&#8217;&#8216;, as the case may be. (And no, George Lucas is not involved. :-) The first character could be &#8216;p&#8217; for a <code>p</code>rototype, &#8216;a&#8217; for <code>a</code>rgument, or &#8216;d&#8217; for <code>d</code>eclaration, so we have <code>&quot;pTHX&quot;</code>, <code>&quot;aTHX&quot;</code> and <code>&quot;dTHX&quot;</code>, and their variants. </p>
<p> When Perl is built without options that set <font SIZE="-1">PERL_IMPLICIT_CONTEXT,</font> there is no first argument containing the interpreter&#8217;s context. The trailing underscore in the pTHX_ macro indicates that the macro expansion needs a comma after the context argument because other arguments follow it. If <font SIZE="-1">PERL_IMPLICIT_CONTEXT</font> is not defined, pTHX_ will be ignored, and the subroutine is not prototyped to take the extra argument. The form of the macro without the trailing underscore is used when there are no additional explicit arguments. </p>
<p> When a core function calls another, it must pass the context. This is normally hidden via macros. Consider <code>&quot;sv_setiv&quot;</code>. It expands into something like this: </p>
<pre><code>    #ifdef PERL_IMPLICIT_CONTEXT
      #define sv_setiv(a,b) Perl_sv_setiv(aTHX_ a, b)
      /* can't do this for vararg functions, see below */
    #else
      #define sv_setiv Perl_sv_setiv
    #endif
</code></pre>
<p> This works well, and means that <font SIZE="-1">XS</font> authors can gleefully write: </p>
<pre><code>    sv_setiv(foo, bar);
</code></pre>
<p> and still have it work under all the modes Perl could have been compiled with. </p>
<p> This doesn&#8217;t work so cleanly for varargs functions, though, as macros imply that the number of arguments is known in advance. Instead we either need to spell them out fully, passing <code>&quot;aTHX_&quot;</code> as the first argument (the Perl core tends to do this with functions like Perl_warner), or use a context-free version. </p>
<p> The context-free version of Perl_warner is called Perl_warner_nocontext, and does not take the extra argument. Instead it does dTHX; to get the context from thread-local storage. We <code>&quot;#define warner Perl_warner_nocontext&quot;</code> so that extensions get source compatibility at the expense of performance. (Passing an arg is cheaper than grabbing it from thread-local storage.) </p>
<p> You can ignore [pad]THXx when browsing the Perl headers/sources. Those are strictly for use within the core. Extensions and embedders need only be aware of [pad]THX.  </p>
<h3>So what happened to dTHR?</h3>
<p> <code>&quot;dTHR&quot;</code> was introduced in perl 5.005 to support the older thread model. The older thread model now uses the <code>&quot;THX&quot;</code> mechanism to pass context pointers around, so <code>&quot;dTHR&quot;</code> is not useful any more. Perl 5.6.0 and later still have it for backward source compatibility, but it is defined to be a no-op.  </p>
<h3>How do I use all this in extensions?</h3>
<p> When Perl is built with <font SIZE="-1">PERL_IMPLICIT_CONTEXT,</font> extensions that call any functions in the Perl <font SIZE="-1">API</font> will need to pass the initial context argument somehow. The kicker is that you will need to write it in such a way that the extension still compiles when Perl hasn&#8217;t been built with <font SIZE="-1">PERL_IMPLICIT_CONTEXT</font> enabled. </p>
<p> There are three ways to do this. First, the easy but inefficient way, which is also the default, in order to maintain source compatibility with extensions: whenever <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> is #included, it redefines the aTHX and aTHX_ macros to call a function that will return the context. Thus, something like: </p>
<pre><code>        sv_setiv(sv, num);
</code></pre>
<p> in your extension will translate to this when <font SIZE="-1">PERL_IMPLICIT_CONTEXT</font> is in effect: </p>
<pre><code>        Perl_sv_setiv(Perl_get_context(), sv, num);
</code></pre>
<p> or to this otherwise: </p>
<pre><code>        Perl_sv_setiv(sv, num);
</code></pre>
<p> You don&#8217;t have to do anything new in your extension to get this; since the Perl library provides <code>Perl_get_context()</code>, it will all just work. </p>
<p> The second, more efficient way is to use the following template for your Foo.xs: </p>
<pre><code>        #define PERL_NO_GET_CONTEXT /* we want efficiency */
        #include &quot;EXTERN.h&quot;
        #include &quot;perl.h&quot;
        #include &quot;XSUB.h&quot;
        STATIC void my_private_function(int arg1, int arg2);
        STATIC void
        my_private_function(int arg1, int arg2)
        {
            dTHX; /* fetch context */
            ... call many Perl API functions ...
        }
        [... etc ...]
        MODULE = Foo PACKAGE = Foo
        /* typical XSUB */
        void
        my_xsub(arg)
                int arg
            CODE:
                my_private_function(arg, 10);
</code></pre>
<p> Note that the only two changes from the normal way of writing an extension is the addition of a <code>&quot;#define PERL_NO_GET_CONTEXT&quot;</code> before including the Perl headers, followed by a <code>&quot;dTHX;&quot;</code> declaration at the start of every function that will call the Perl <font SIZE="-1">API.</font> (You&#8217;ll know which functions need this, because the C compiler will complain that there&#8217;s an undeclared identifier in those functions.) No changes are needed for the XSUBs themselves, because the <font SIZE="-1"><code>XS</code></font><code>()</code> macro is correctly defined to pass in the implicit context if needed. </p>
<p> The third, even more efficient way is to ape how it is done within the Perl guts: </p>
<pre><code>        #define PERL_NO_GET_CONTEXT /* we want efficiency */
        #include &quot;EXTERN.h&quot;
        #include &quot;perl.h&quot;
        #include &quot;XSUB.h&quot;
        /* pTHX_ only needed for functions that call Perl API */
        STATIC void my_private_function(pTHX_ int arg1, int arg2);
        STATIC void
        my_private_function(pTHX_ int arg1, int arg2)
        {
            /* dTHX; not needed here, because THX is an argument */
            ... call Perl API functions ...
        }
        [... etc ...]
        MODULE = Foo PACKAGE = Foo
        /* typical XSUB */
        void
        my_xsub(arg)
                int arg
            CODE:
                my_private_function(aTHX_ arg, 10);
</code></pre>
<p> This implementation never has to fetch the context using a function call, since it is always passed as an extra argument. Depending on your needs for simplicity or efficiency, you may mix the previous two approaches freely. </p>
<p> Never add a comma after <code>&quot;pTHX&quot;</code> yourself---always use the form of the macro with the underscore for functions that take explicit arguments, or the form without the argument for functions with no explicit arguments. </p>
<p> If one is compiling Perl with the <code>&quot;-DPERL_GLOBAL_STRUCT&quot;</code> the <code>&quot;dVAR&quot;</code> definition is needed if the Perl global variables (see <i>perlvars.h</i> or <i>globvar.sym</i>) are accessed in the function and <code>&quot;dTHX&quot;</code> is not used (the <code>&quot;dTHX&quot;</code> includes the <code>&quot;dVAR&quot;</code> if necessary). One notices the need for <code>&quot;dVAR&quot;</code> only with the said compile-time define, because otherwise the Perl global variables are visible as-is.  </p>
<h3>Should I do anything special if I call perl from multiple threads?</h3>
<p> If you create interpreters in one thread and then proceed to call them in another, you need to make sure perl&#8217;s own Thread Local Storage (<font SIZE="-1">TLS</font>) slot is initialized correctly in each of those threads. </p>
<p> The <code>&quot;perl_alloc&quot;</code> and <code>&quot;perl_clone&quot;</code> <font SIZE="-1">API</font> functions will automatically set the <font SIZE="-1">TLS</font> slot to the interpreter they created, so that there is no need to do anything special if the interpreter is always accessed in the same thread that created it, and that thread did not create or call any other interpreters afterwards. If that is not the case, you have to set the <font SIZE="-1">TLS</font> slot of the thread before calling any functions in the Perl <font SIZE="-1">API</font> on that particular interpreter. This is done by calling the <code>&quot;PERL_SET_CONTEXT&quot;</code> macro in that thread as the first thing you do: </p>
<pre><code>        /* do this before doing anything else with some_perl */
        PERL_SET_CONTEXT(some_perl);
        ... other Perl API calls on some_perl go here ...
</code></pre>
<font SIZE="-1"></font><h3>Future Plans and PERL_IMPLICIT_SYS</h3>
<p> Just as <font SIZE="-1">PERL_IMPLICIT_CONTEXT</font> provides a way to bundle up everything that the interpreter knows about itself and pass it around, so too are there plans to allow the interpreter to bundle up everything it knows about the environment it&#8217;s running on. This is enabled with the <font SIZE="-1">PERL_IMPLICIT_SYS</font> macro. Currently it only works with <font SIZE="-1">USE_ITHREADS</font> on Windows. </p>
<p> This allows the ability to provide an extra pointer (called the ``host&#8217;&#8216; environment) for all the system calls. This makes it possible for all the system stuff to maintain their own state, broken down into seven C structures. These are thin wrappers around the usual system calls (see <i>win32/perllib.c</i>) for the default perl executable, but for a more ambitious host (like the one that would do <code>fork()</code> emulation) all the extra work needed to pretend that different interpreters are actually different ``processes&#8217;&#8216;, would be done here. </p>
<p> The Perl engine/interpreter and the host are orthogonal entities. There could be one or more interpreters in a process, and one or more ``hosts&#8217;&#8216;, with free association between them.  </p>
<h2>Internal Functions</h2>
<p> All of Perl&#8217;s internal functions which will be exposed to the outside world are prefixed by <code>&quot;Perl_&quot;</code> so that they will not conflict with <font SIZE="-1">XS</font> functions or functions used in a program in which Perl is embedded. Similarly, all global variables begin with <code>&quot;PL_&quot;</code>. (By convention, static functions start with <code>&quot;S_&quot;</code>.) </p>
<p> Inside the Perl core (<code>&quot;PERL_CORE&quot;</code> defined), you can get at the functions either with or without the <code>&quot;Perl_&quot;</code> prefix, thanks to a bunch of defines that live in <i>embed.h</i>. Note that extension code should <i>not</i> set <code>&quot;PERL_CORE&quot;</code>; this exposes the full perl internals, and is likely to cause breakage of the <font SIZE="-1">XS</font> in each new perl release. </p>
<p> The file <i>embed.h</i> is generated automatically from <i>embed.pl</i> and <i>embed.fnc</i>. <i>embed.pl</i> also creates the prototyping header files for the internal functions, generates the documentation and a lot of other bits and pieces. It&#8217;s important that when you add a new function to the core or change an existing one, you change the data in the table in <i>embed.fnc</i> as well. Here&#8217;s a sample entry from that table: </p>
<pre><code>    Apd |SV** |av_fetch |AV* ar|I32 key|I32 lval
</code></pre>
<p> The second column is the return type, the third column the name. Columns after that are the arguments. The first column is a set of flags: </p>
<dl>
<dt>A</dt>
<dd> <p> This function is a part of the public <font SIZE="-1">API.</font> All such functions should also have &#8216;d&#8217;, very few do not. </p>
 </dd>
<dt>p</dt>
<dd> <p> This function has a <code>&quot;Perl_&quot;</code> prefix; i.e. it is defined as <code>&quot;Perl_av_fetch&quot;</code>. </p>
 </dd>
<dt>d</dt>
<dd> <p> This function has documentation using the <code>&quot;apidoc&quot;</code> feature which we&#8217;ll look at in a second. Some functions have &#8216;d&#8217; but not &#8216;A&#8217;; docs are good. </p>
 </dd></dl>
<p> Other available flags are: </p>
<dl>
<dt>s</dt>
<dd> <p> This is a static function and is defined as <code>&quot;STATIC S_whatever&quot;</code>, and usually called within the sources as <code>&quot;whatever(...)&quot;</code>. </p>
 </dd>
<dt>n</dt>
<dd> <p> This does not need an interpreter context, so the definition has no <code>&quot;pTHX&quot;</code>, and it follows that callers don&#8217;t use <code>&quot;aTHX&quot;</code>. (See ``Background and <font SIZE="-1">PERL_IMPLICIT_CONTEXT&#8217;&#8216;</font>.) </p>
 </dd>
<dt>r</dt>
<dd> <p> This function never returns; <code>&quot;croak&quot;</code>, <code>&quot;exit&quot;</code> and friends. </p>
 </dd>
<dt>f</dt>
<dd> <p> This function takes a variable number of arguments, <code>&quot;printf&quot;</code> style. The argument list should end with <code>&quot;...&quot;</code>, like this: </p>
<pre><code>    Afprd |void |croak |const char* pat|...
</code></pre>
 </dd>
<dt>M</dt>
<dd> <p> This function is part of the experimental development <font SIZE="-1">API,</font> and may change or disappear without notice. </p>
 </dd>
<dt>o</dt>
<dd> <p> This function should not have a compatibility macro to define, say, <code>&quot;Perl_parse&quot;</code> to <code>&quot;parse&quot;</code>. It must be called as <code>&quot;Perl_parse&quot;</code>. </p>
 </dd>
<dt>x</dt>
<dd> <p> This function isn&#8217;t exported out of the Perl core. </p>
 </dd>
<dt>m</dt>
<dd> <p> This is implemented as a macro. </p>
 </dd>
<dt>X</dt>
<dd> <p> This function is explicitly exported. </p>
 </dd>
<dt>E</dt>
<dd> <p> This function is visible to extensions included in the Perl core. </p>
 </dd>
<dt>b</dt>
<dd> <p> Binary backward compatibility; this function is a macro but also has a <code>&quot;Perl_&quot;</code> implementation (which is exported). </p>
 </dd>
<dt>others</dt>
<dd> <p> See the comments at the top of <code>&quot;embed.fnc&quot;</code> for others. </p>
 </dd></dl>
<p> If you edit <i>embed.pl</i> or <i>embed.fnc</i>, you will need to run <code>&quot;make regen_headers&quot;</code> to force a rebuild of <i>embed.h</i> and other auto-generated files.  </p>
<h3>Formatted Printing of IVs, UVs, and NVs</h3>
<p> If you are printing IVs, UVs, or <font SIZE="-1">NVS</font> instead of the <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) style formatting codes like <code>%d</code>, <code>%ld</code>, <code>%f</code>, you should use the following macros for portability </p>
<pre><code>        IVdf IV in decimal
        UVuf UV in decimal
        UVof UV in octal
        UVxf UV in hexadecimal
        NVef NV %e-like
        NVff NV %f-like
        NVgf NV %g-like
</code></pre>
<p> These will take care of 64-bit integers and long doubles. For example: </p>
<pre><code>        printf(&quot;IV is %&quot;IVdf&quot;\n&quot;, iv);
</code></pre>
<p> The IVdf will expand to whatever is the correct format for the IVs. </p>
<p> Note that there are different ``long doubles&#8217;&#8216;: Perl will use whatever the compiler has. </p>
<p> If you are printing addresses of pointers, use UVxf combined with <font SIZE="-1"><code>PTR2UV</code></font><code>()</code>, do not use <code>%lx</code> or <code>%p</code>.  </p>
<h3>Formatted Printing of Size_t and SSize_t</h3>
<p> The most general way to do this is to cast them to a <font SIZE="-1">UV</font> or <font SIZE="-1">IV,</font> and print as in the previous section. </p>
<p> But if you&#8217;re using <code>&quot;PerlIO_printf()&quot;</code>, it&#8217;s less typing and visual clutter to use the <code>&quot;%z&quot;</code> length modifier (for <i>siZe</i>): </p>
<pre><code>        PerlIO_printf(&quot;STRLEN is %zu\n&quot;, len);
</code></pre>
<p> This modifier is not portable, so its use should be restricted to <code>&quot;PerlIO_printf()&quot;</code>.  </p>
<h3>Pointer-To-Integer and Integer-To-Pointer</h3>
<p> Because pointer size does not necessarily equal integer size, use the follow macros to do it right. </p>
<pre><code>        PTR2UV(pointer)
        PTR2IV(pointer)
        PTR2NV(pointer)
        INT2PTR(pointertotype, integer)
</code></pre>
<p> For example: </p>
<pre><code>        IV iv = ...;
        SV *sv = INT2PTR(SV*, iv);
</code></pre>
<p> and </p>
<pre><code>        AV *av = ...;
        UV uv = PTR2UV(av);
</code></pre>
<h3>Exception Handling</h3>
<p> There are a couple of macros to do very basic exception handling in <font SIZE="-1">XS</font> modules. You have to define <code>&quot;NO_XSLOCKS&quot;</code> before including <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> to be able to use these macros: </p>
<pre><code>        #define NO_XSLOCKS
        #include &quot;XSUB.h&quot;
</code></pre>
<p> You can use these macros if you call code that may croak, but you need to do some cleanup before giving control back to Perl. For example: </p>
<pre><code>        dXCPT; /* set up necessary variables */
        XCPT_TRY_START {
          code_that_may_croak();
        } XCPT_TRY_END
        XCPT_CATCH
        {
          /* do cleanup here */
          XCPT_RETHROW;
        }
</code></pre>
<p> Note that you always have to rethrow an exception that has been caught. Using these macros, it is not possible to just catch the exception and ignore it. If you have to ignore the exception, you have to use the <code>&quot;call_*&quot;</code> function. </p>
<p> The advantage of using the above macros is that you don&#8217;t have to setup an extra function for <code>&quot;call_*&quot;</code>, and that using these macros is faster than using <code>&quot;call_*&quot;</code>.  </p>
<h3>Source Documentation</h3>
<p> There&#8217;s an effort going on to document the internal functions and automatically produce reference manuals from them --- perlapi is one such manual which details all the functions which are available to <font SIZE="-1">XS</font> writers. perlintern is the autogenerated manual for the functions which are not part of the <font SIZE="-1">API</font> and are supposedly for internal use only. </p>
<p> Source documentation is created by putting <font SIZE="-1">POD</font> comments into the C source, like this: </p>
<pre><code> /*
 =for apidoc sv_setiv
 Copies an integer into the given SV. Does not handle 'set' magic. See
 L&lt;perlapi/sv_setiv_mg&gt;.
 =cut
 */
</code></pre>
<p> Please try and supply some documentation if you add functions to the Perl core.  </p>
<h3>Backwards compatibility</h3>
<p> The Perl <font SIZE="-1">API</font> changes over time. New functions are added or the interfaces of existing functions are changed. The <code>&quot;Devel::PPPort&quot;</code> module tries to provide compatibility code for some of these changes, so <font SIZE="-1">XS</font> writers don&#8217;t have to code it themselves when supporting multiple versions of Perl. </p>
<p> <code>&quot;Devel::PPPort&quot;</code> generates a C header file <i>ppport.h</i> that can also be run as a Perl script. To generate <i>ppport.h</i>, run: </p>
<pre><code>    perl -MDevel::PPPort -eDevel::PPPort::WriteFile
</code></pre>
<p> Besides checking existing <font SIZE="-1">XS</font> code, the script can also be used to retrieve compatibility information for various <font SIZE="-1">API</font> calls using the <code>&quot;--api-info&quot;</code> command line switch. For example: </p>
<pre><code>  % perl ppport.h --api-info=sv_magicext
</code></pre>
<p> For details, see <code>&quot;perldoc ppport.h&quot;</code>.  </p>
<h2>Unicode Support</h2>
<p> Perl 5.6.0 introduced Unicode support. It&#8217;s important for porters and <font SIZE="-1">XS</font> writers to understand this support and make sure that the code they write does not corrupt Unicode data.  </p>
<code></code><h3>What is Unicode, anyway?</h3>
<p> In the olden, less enlightened times, we all used to use <font SIZE="-1">ASCII.</font> Most of us did, anyway. The big problem with <font SIZE="-1">ASCII</font> is that it&#8217;s American. Well, no, that&#8217;s not actually the problem; the problem is that it&#8217;s not particularly useful for people who don&#8217;t use the Roman alphabet. What used to happen was that particular languages would stick their own alphabet in the upper range of the sequence, between 128 and 255. Of course, we then ended up with plenty of variants that weren&#8217;t quite <font SIZE="-1">ASCII,</font> and the whole point of it being a standard was lost. </p>
<p> Worse still, if you&#8217;ve got a language like Chinese or Japanese that has hundreds or thousands of characters, then you really can&#8217;t fit them into a mere 256, so they had to forget about <font SIZE="-1">ASCII</font> altogether, and build their own systems using pairs of numbers to refer to one character. </p>
<p> To fix this, some people formed Unicode, Inc. and produced a new character set containing all the characters you can possibly think of and more. There are several ways of representing these characters, and the one Perl uses is called <font SIZE="-1">UTF-8.</font> <font SIZE="-1">UTF-8</font> uses a variable number of bytes to represent a character. You can learn more about Unicode and Perl&#8217;s Unicode model in perlunicode. </p>
<p> (On <font SIZE="-1">EBCDIC</font> platforms, Perl uses instead UTF-EBCDIC, which is a form of <font SIZE="-1">UTF-8</font> adapted for <font SIZE="-1">EBCDIC</font> platforms. Below, we just talk about <font SIZE="-1">UTF-8.</font> UTF-EBCDIC is like <font SIZE="-1">UTF-8,</font> but the details are different. The macros hide the differences from you, just remember that the particular numbers and bit patterns presented below will differ in UTF-EBCDIC.)  </p>
<font SIZE="-1"></font><h3>How can I recognise a UTF-8 string?</h3>
<p> You can&#8217;t. This is because <font SIZE="-1">UTF-8</font> data is stored in bytes just like non-UTF-8 data. The Unicode character 200, (<code>0xC8</code> for you hex types) capital E with a grave accent, is represented by the two bytes <code>&quot;v196.172&quot;</code>. Unfortunately, the non-Unicode string <code>&quot;chr(196).chr(172)&quot;</code> has that byte sequence as well. So you can&#8217;t tell just by looking --- this is what makes Unicode input an interesting problem. </p>
<p> In general, you either have to know what you&#8217;re dealing with, or you have to guess. The <font SIZE="-1">API</font> function <code>&quot;is_utf8_string&quot;</code> can help; it&#8217;ll tell you if a string contains only valid <font SIZE="-1">UTF-8</font> characters, and the chances of a non-UTF-8 string looking like valid <font SIZE="-1">UTF-8</font> become very small very quickly with increasing string length. On a character-by-character basis, <code>&quot;isUTF8_CHAR&quot;</code> will tell you whether the current character in a string is valid <font SIZE="-1">UTF-8.</font>  </p>
<font SIZE="-1"></font><h3>How does UTF-8 represent Unicode characters?</h3>
<p> As mentioned above, <font SIZE="-1">UTF-8</font> uses a variable number of bytes to store a character. Characters with values 0...127 are stored in one byte, just like good ol&#8217; <font SIZE="-1">ASCII.</font> Character 128 is stored as <code>&quot;v194.128&quot;</code>; this continues up to character 191, which is <code>&quot;v194.191&quot;</code>. Now we&#8217;ve run out of bits (191 is binary <code>10111111</code>) so we move on; character 192 is <code>&quot;v195.128&quot;</code>. And so it goes on, moving to three bytes at character 2048. ``Unicode Encodings&#8217;&#8216; in perlunicode has pictures of how this works. </p>
<p> Assuming you know you&#8217;re dealing with a <font SIZE="-1">UTF-8</font> string, you can find out how long the first character in it is with the <code>&quot;UTF8SKIP&quot;</code> macro: </p>
<pre><code>    char *utf = &quot;\305\233\340\240\201&quot;;
    I32 len;
    len = UTF8SKIP(utf); /* len is 2 here */
    utf += len;
    len = UTF8SKIP(utf); /* len is 3 here */
</code></pre>
<p> Another way to skip over characters in a <font SIZE="-1">UTF-8</font> string is to use <code>&quot;utf8_hop&quot;</code>, which takes a string and a number of characters to skip over. You&#8217;re on your own about bounds checking, though, so don&#8217;t use it lightly. </p>
<p> All bytes in a multi-byte <font SIZE="-1">UTF-8</font> character will have the high bit set, so you can test if you need to do something special with this character like this (the <code>&quot;UTF8_IS_INVARIANT()&quot;</code> is a macro that tests whether the byte is encoded as a single byte even in <font SIZE="-1">UTF-8</font>): </p>
<pre><code>    U8 *utf; /* Initialize this to point to the beginning of the
                    sequence to convert */
    U8 *utf_end; /* Initialize this to 1 beyond the end of the sequence
                    pointed to by 'utf' */
    UV uv; /* Returned code point; note: a UV, not a U8, not a
                    char */
    STRLEN len; /* Returned length of character in bytes */
    if (!UTF8_IS_INVARIANT(*utf))
        /* Must treat this as UTF-8 */
        uv = utf8_to_uvchr_buf(utf, utf_end, &amp;len);
    else
        /* OK to treat this character as a byte */
        uv = *utf;
</code></pre>
<p> You can also see in that example that we use <code>&quot;utf8_to_uvchr_buf&quot;</code> to get the value of the character; the inverse function <code>&quot;uvchr_to_utf8&quot;</code> is available for putting a <font SIZE="-1">UV</font> into <font SIZE="-1">UTF-8:</font> </p>
<pre><code>    if (!UVCHR_IS_INVARIANT(uv))
        /* Must treat this as UTF8 */
        utf8 = uvchr_to_utf8(utf8, uv);
    else
        /* OK to treat this character as a byte */
        *utf8++ = uv;
</code></pre>
<p> You <code>must</code> convert characters to UVs using the above functions if you&#8217;re ever in a situation where you have to match <font SIZE="-1">UTF-8</font> and non-UTF-8 characters. You may not skip over <font SIZE="-1">UTF-8</font> characters in this case. If you do this, you&#8217;ll lose the ability to match hi-bit non-UTF-8 characters; for instance, if your <font SIZE="-1">UTF-8</font> string contains <code>&quot;v196.172&quot;</code>, and you skip that character, you can never match a <code>&quot;chr(200)&quot;</code> in a non-UTF-8 string. So don&#8217;t do that! </p>
<p> (Note that we don&#8217;t have to test for invariant characters in the examples above. The functions work on any well-formed <font SIZE="-1">UTF-8</font> input. It&#8217;s just that its faster to avoid the function overhead when it&#8217;s not needed.)  </p>
<font SIZE="-1"></font><h3>How does Perl store UTF-8 strings?</h3>
<p> Currently, Perl deals with <font SIZE="-1">UTF-8</font> strings and non-UTF-8 strings slightly differently. A flag in the <font SIZE="-1">SV,</font> <code>&quot;SVf_UTF8&quot;</code>, indicates that the string is internally encoded as <font SIZE="-1">UTF-8.</font> Without it, the byte value is the codepoint number and vice versa. This flag is only meaningful if the <font SIZE="-1">SV</font> is <code>&quot;SvPOK&quot;</code> or immediately after stringification via <code>&quot;SvPV&quot;</code> or a similar macro. You can check and manipulate this flag with the following macros: </p>
<pre><code>    SvUTF8(sv)
    SvUTF8_on(sv)
    SvUTF8_off(sv)
</code></pre>
<p> This flag has an important effect on Perl&#8217;s treatment of the string: if <font SIZE="-1">UTF-8</font> data is not properly distinguished, regular expressions, <code>&quot;length&quot;</code>, <code>&quot;substr&quot;</code> and other string handling operations will have undesirable (wrong) results. </p>
<p> The problem comes when you have, for instance, a string that isn&#8217;t flagged as <font SIZE="-1">UTF-8,</font> and contains a byte sequence that could be <font SIZE="-1">UTF-8</font> --- especially when combining non-UTF-8 and <font SIZE="-1">UTF-8</font> strings. </p>
<p> Never forget that the <code>&quot;SVf_UTF8&quot;</code> flag is separate from the <font SIZE="-1">PV</font> value; you need to be sure you don&#8217;t accidentally knock it off while you&#8217;re manipulating SVs. More specifically, you cannot expect to do this: </p>
<pre><code>    SV *sv;
    SV *nsv;
    STRLEN len;
    char *p;
    p = SvPV(sv, len);
    frobnicate(p);
    nsv = newSVpvn(p, len);
</code></pre>
<p> The <code>&quot;char*&quot;</code> string does not tell you the whole story, and you can&#8217;t copy or reconstruct an <font SIZE="-1">SV</font> just by copying the string value. Check if the old <font SIZE="-1">SV</font> has the <font SIZE="-1">UTF8</font> flag set (<i>after</i> the <code>&quot;SvPV&quot;</code> call), and act accordingly: </p>
<pre><code>    p = SvPV(sv, len);
    is_utf8 = SvUTF8(sv);
    frobnicate(p, is_utf8);
    nsv = newSVpvn(p, len);
    if (is_utf8)
        SvUTF8_on(nsv);
</code></pre>
<p> In the above, your <code>&quot;frobnicate&quot;</code> function has been changed to be made aware of whether or not it&#8217;s dealing with <font SIZE="-1">UTF-8</font> data, so that it can handle the string appropriately. </p>
<p> Since just passing an <font SIZE="-1">SV</font> to an <font SIZE="-1">XS</font> function and copying the data of the <font SIZE="-1">SV</font> is not enough to copy the <font SIZE="-1">UTF8</font> flags, even less right is just passing a <code>&quot;char *&quot;</code> to an <font SIZE="-1">XS</font> function. </p>
<p> For full generality, use the <code>&quot;DO_UTF8&quot;</code> macro to see if the string in an <font SIZE="-1">SV</font> is to be <i>treated</i> as <font SIZE="-1">UTF-8.</font> This takes into account if the call to the <font SIZE="-1">XS</font> function is being made from within the scope of <code>&quot;use bytes&quot;</code>. If so, the underlying bytes that comprise the <font SIZE="-1">UTF-8</font> string are to be exposed, rather than the character they represent. But this pragma should only really be used for debugging and perhaps low-level testing at the byte level. Hence most <font SIZE="-1">XS</font> code need not concern itself with this, but various areas of the perl core do need to support it. </p>
<p> And this isn&#8217;t the whole story. Starting in Perl v5.12, strings that aren&#8217;t encoded in <font SIZE="-1">UTF-8</font> may also be treated as Unicode under various conditions (see ``<font SIZE="-1">ASCII</font> Rules versus Unicode Rules&#8217;&#8216; in perlunicode). This is only really a problem for characters whose ordinals are between 128 and 255, and their behavior varies under <font SIZE="-1">ASCII</font> versus Unicode rules in ways that your code cares about (see ``The &#8216;&#8216;Unicode Bug&quot;&quot; in perlunicode). There is no published <font SIZE="-1">API</font> for dealing with this, as it is subject to change, but you can look at the code for <code>&quot;pp_lc&quot;</code> in <i>pp.c</i> for an example as to how it&#8217;s currently done.  </p>
<font SIZE="-1"></font><h3>How do I convert a string to UTF-8 ?</h3>
<p> If you&#8217;re mixing <font SIZE="-1">UTF-8</font> and non-UTF-8 strings, it is necessary to upgrade the non-UTF-8 strings to <font SIZE="-1">UTF-8.</font> If you&#8217;ve got an <font SIZE="-1">SV,</font> the easiest way to do this is: </p>
<pre><code>    sv_utf8_upgrade(sv);
</code></pre>
<p> However, you must not do this, for example: </p>
<pre><code>    if (!SvUTF8(left))
        sv_utf8_upgrade(left);
</code></pre>
<p> If you do this in a binary operator, you will actually change one of the strings that came into the operator, and, while it shouldn&#8217;t be noticeable by the end user, it can cause problems in deficient code. </p>
<p> Instead, <code>&quot;bytes_to_utf8&quot;</code> will give you a UTF-8-encoded <code>copy</code> of its string argument. This is useful for having the data available for comparisons and so on, without harming the original <font SIZE="-1">SV.</font> There&#8217;s also <code>&quot;utf8_to_bytes&quot;</code> to go the other way, but naturally, this will fail if the string contains any characters above 255 that can&#8217;t be represented in a single byte.  </p>
<h3>How do I compare strings?</h3>
<p> ``sv_cmp&#8217;&#8216; in perlapi and ``sv_cmp_flags&#8217;&#8216; in perlapi do a lexigraphic comparison of two <font SIZE="-1">SV</font>&#8216;s, and handle UTF-8ness properly. Note, however, that Unicode specifies a much fancier mechanism for collation, available via the Unicode::Collate module. </p>
<p> To just compare two strings for equality/non-equality, you can just use <code>&quot;memEQ()&quot;</code> and <code>&quot;memNE()&quot;</code> as usual, except the strings must be both <font SIZE="-1">UTF-8</font> or not <font SIZE="-1">UTF-8</font> encoded. </p>
<p> To compare two strings case-insensitively, use <code>&quot;foldEQ_utf8()&quot;</code> (the strings don&#8217;t have to have the same UTF-8ness).  </p>
<h3>Is there anything else I need to know?</h3>
<p> Not really. Just remember these things: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> There&#8217;s no way to tell if a <code>&quot;char *&quot;</code> or <code>&quot;U8 *&quot;</code> string is <font SIZE="-1">UTF-8</font> or not. But you can tell if an <font SIZE="-1">SV</font> is to be treated as <font SIZE="-1">UTF-8</font> by calling <code>&quot;DO_UTF8&quot;</code> on it, after stringifying it with <code>&quot;SvPV&quot;</code> or a similar macro. And, you can tell if <font SIZE="-1">SV</font> is actually <font SIZE="-1">UTF-8</font> (even if it is not to be treated as such) by looking at its <code>&quot;SvUTF8&quot;</code> flag (again after stringifying it). Don&#8217;t forget to set the flag if something should be <font SIZE="-1">UTF-8.</font> Treat the flag as part of the <font SIZE="-1">PV,</font> even though it&#8217;s not --- if you pass on the <font SIZE="-1">PV</font> to somewhere, pass on the flag too. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If a string is <font SIZE="-1">UTF-8,</font> <code>always</code> use <code>&quot;utf8_to_uvchr_buf&quot;</code> to get at the value, unless <code>&quot;UTF8_IS_INVARIANT(*s)&quot;</code> in which case you can use <code>*s</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When writing a character <font SIZE="-1">UV</font> to a <font SIZE="-1">UTF-8</font> string, <code>always</code> use <code>&quot;uvchr_to_utf8&quot;</code>, unless <code>&quot;UVCHR_IS_INVARIANT(uv))&quot;</code> in which case you can use <code>&quot;*s = uv&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mixing <font SIZE="-1">UTF-8</font> and non-UTF-8 strings is tricky. Use <code>&quot;bytes_to_utf8&quot;</code> to get a new string which is <font SIZE="-1">UTF-8</font> encoded, and then combine them. </p>
 </dd></dl>
<h2>Custom Operators</h2>
<p> Custom operator support is an experimental feature that allows you to define your own ops. This is primarily to allow the building of interpreters for other languages in the Perl core, but it also allows optimizations through the creation of ``macro-ops&#8217;&#8216; (ops which perform the functions of multiple ops which are usually executed together, such as <code>&quot;gvsv, gvsv, add&quot;</code>.) </p>
<p> This feature is implemented as a new op type, <code>&quot;OP_CUSTOM&quot;</code>. The Perl core does not ``know&#8217;&#8216; anything special about this op type, and so it will not be involved in any optimizations. This also means that you can define your custom ops to be any op structure --- unary, binary, list and so on --- you like. </p>
<p> It&#8217;s important to know what custom operators won&#8217;t do for you. They won&#8217;t let you add new syntax to Perl, directly. They won&#8217;t even let you add new keywords, directly. In fact, they won&#8217;t change the way Perl compiles a program at all. You have to do those changes yourself, after Perl has compiled the program. You do this either by manipulating the op tree using a <code>&quot;CHECK&quot;</code> block and the <code>&quot;B::Generate&quot;</code> module, or by adding a custom peephole optimizer with the <code>&quot;optimize&quot;</code> module. </p>
<p> When you do this, you replace ordinary Perl ops with custom ops by creating ops with the type <code>&quot;OP_CUSTOM&quot;</code> and the <code>&quot;op_ppaddr&quot;</code> of your own <font SIZE="-1">PP</font> function. This should be defined in <font SIZE="-1">XS</font> code, and should look like the <font SIZE="-1">PP</font> ops in <code>&quot;pp_*.c&quot;</code>. You are responsible for ensuring that your op takes the appropriate number of values from the stack, and you are responsible for adding stack marks if necessary. </p>
<p> You should also ``register&#8217;&#8216; your op with the Perl interpreter so that it can produce sensible error and warning messages. Since it is possible to have multiple custom ops within the one ``logical&#8217;&#8216; op type <code>&quot;OP_CUSTOM&quot;</code>, Perl uses the value of <code>&quot;o-&gt;op_ppaddr&quot;</code> to determine which custom op it is dealing with. You should create an <code>&quot;XOP&quot;</code> structure for each ppaddr you use, set the properties of the custom op with <code>&quot;XopENTRY_set&quot;</code>, and register the structure against the ppaddr using <code>&quot;Perl_custom_op_register&quot;</code>. A trivial example might look like: </p>
<pre><code>    static XOP my_xop;
    static OP *my_pp(pTHX);
    BOOT:
        XopENTRY_set(&amp;my_xop, xop_name, &quot;myxop&quot;);
        XopENTRY_set(&amp;my_xop, xop_desc, &quot;Useless custom op&quot;);
        Perl_custom_op_register(aTHX_ my_pp, &amp;my_xop);
</code></pre>
<p> The available fields in the structure are: </p>
<dl>
<dt>xop_name</dt>
<dd> <p> A short name for your op. This will be included in some error messages, and will also be returned as <code>&quot;$op-&gt;name&quot;</code> by the B module, so it will appear in the output of module like B::Concise. </p>
 </dd>
<dt>xop_desc</dt>
<dd> <p> A short description of the function of the op. </p>
 </dd>
<dt>xop_class</dt>
<dd> <p> Which of the various <code>*OP</code> structures this op uses. This should be one of the <code>&quot;OA_*&quot;</code> constants from <i>op.h</i>, namely </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><font SIZE="-1">OA_BASEOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_UNOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_BINOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_LOGOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_LISTOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_PMOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_SVOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_PADOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_PVOP_OR_SVOP</font></dt>
<dd> <p> This should be interpreted as &#8216;<code>&quot;PVOP&quot;</code>&#8216; only. The <code>&quot;_OR_SVOP&quot;</code> is because the only core <code>&quot;PVOP&quot;</code>, <code>&quot;OP_TRANS&quot;</code>, can sometimes be a <code>&quot;SVOP&quot;</code> instead. </p>
 </dd>
<dt><font SIZE="-1">OA_LOOP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">OA_COP</font></dt>
<dd>  </dd></dl>
</dl>
<dl>
<dd> <p> The other <code>&quot;OA_*&quot;</code> constants should not be used. </p>
 </dd></dl>
<dt>xop_peep</dt>
<dd> <p> This member is of type <code>&quot;Perl_cpeep_t&quot;</code>, which expands to <code>&quot;void (*Perl_cpeep_t)(aTHX_ OP *o, OP *oldop)&quot;</code>. If it is set, this function will be called from <code>&quot;Perl_rpeep&quot;</code> when ops of this type are encountered by the peephole optimizer. <i>o</i> is the <font SIZE="-1">OP</font> that needs optimizing; <i>oldop</i> is the previous <font SIZE="-1">OP</font> optimized, whose <code>&quot;op_next&quot;</code> points to <i>o</i>. </p>
 </dd></dl>
<p> <code>&quot;B::Generate&quot;</code> directly supports the creation of custom ops by name.  </p>
<h2>Dynamic Scope and the Context Stack</h2>
<p> <code>Note:</code> this section describes a non-public internal <font SIZE="-1">API</font> that is subject to change without notice.  </p>
<h3>Introduction to the context stack</h3>
<p> In Perl, dynamic scoping refers to the runtime nesting of things like subroutine calls, evals etc, as well as the entering and exiting of block scopes. For example, the restoring of a <code>&quot;local&quot;</code>ised variable is determined by the dynamic scope. </p>
<p> Perl tracks the dynamic scope by a data structure called the context stack, which is an array of <code>&quot;PERL_CONTEXT&quot;</code> structures, and which is itself a big union for all the types of context. Whenever a new scope is entered (such as a block, a <code>&quot;for&quot;</code> loop, or a subroutine call), a new context entry is pushed onto the stack. Similarly when leaving a block or returning from a subroutine call etc. a context is popped. Since the context stack represents the current dynamic scope, it can be searched. For example, <code>&quot;next LABEL&quot;</code> searches back through the stack looking for a loop context that matches the label; <code>&quot;return&quot;</code> pops contexts until it finds a sub or eval context or similar; <code>&quot;caller&quot;</code> examines sub contexts on the stack. </p>
<p> Each context entry is labelled with a context type, <code>&quot;cx_type&quot;</code>. Typical context types are <code>&quot;CXt_SUB&quot;</code>, <code>&quot;CXt_EVAL&quot;</code> etc., as well as <code>&quot;CXt_BLOCK&quot;</code> and <code>&quot;CXt_NULL&quot;</code> which represent a basic scope (as pushed by <code>&quot;pp_enter&quot;</code>) and a sort block. The type determines which part of the context union are valid. </p>
<p> The main division in the context struct is between a substitution scope (<code>&quot;CXt_SUBST&quot;</code>) and block scopes, which are everything else. The former is just used while executing <code>&quot;s///e&quot;</code>, and won&#8217;t be discussed further here. </p>
<p> All the block scope types share a common base, which corresponds to <code>&quot;CXt_BLOCK&quot;</code>. This stores the old values of various scope-related variables like <code>&quot;PL_curpm&quot;</code>, as well as information about the current scope, such as <code>&quot;gimme&quot;</code>. On scope exit, the old variables are restored. </p>
<p> Particular block scope types store extra per-type information. For example, <code>&quot;CXt_SUB&quot;</code> stores the currently executing <font SIZE="-1">CV,</font> while the various for loop types might hold the original loop variable <font SIZE="-1">SV.</font> On scope exit, the per-type data is processed; for example the <font SIZE="-1">CV</font> has its reference count decremented, and the original loop variable is restored. </p>
<p> The macro <code>&quot;cxstack&quot;</code> returns the base of the current context stack, while <code>&quot;cxstack_ix&quot;</code> is the index of the current frame within that stack. </p>
<p> In fact, the context stack is actually part of a stack-of-stacks system; whenever something unusual is done such as calling a <code>&quot;DESTROY&quot;</code> or tie handler, a new stack is pushed, then popped at the end. </p>
<p> Note that the <font SIZE="-1">API</font> described here changed considerably in perl 5.24; prior to that, big macros like <code>&quot;PUSHBLOCK&quot;</code> and <code>&quot;POPSUB&quot;</code> were used; in 5.24 they were replaced by the inline static functions described below. In addition, the ordering and detail of how these macros/function work changed in many ways, often subtly. In particular they didn&#8217;t handle saving the savestack and temps stack positions, and required additional <code>&quot;ENTER&quot;</code>, <code>&quot;SAVETMPS&quot;</code> and <code>&quot;LEAVE&quot;</code> compared to the new functions. The old-style macros will not be described further.  </p>
<h3>Pushing contexts</h3>
<p> For pushing a new context, the two basic functions are <code>&quot;cx = cx_pushblock()&quot;</code>, which pushes a new basic context block and returns its address, and a family of similar functions with names like <code>&quot;cx_pushsub(cx)&quot;</code> which populate the additional type-dependent fields in the <code>&quot;cx&quot;</code> struct. Note that <code>&quot;CXt_NULL&quot;</code> and <code>&quot;CXt_BLOCK&quot;</code> don&#8217;t have their own push functions, as they don&#8217;t store any data beyond that pushed by <code>&quot;cx_pushblock&quot;</code>. </p>
<p> The fields of the context struct and the arguments to the <code>&quot;cx_*&quot;</code> functions are subject to change between perl releases, representing whatever is convenient or efficient for that release. </p>
<p> A typical context stack pushing can be found in <code>&quot;pp_entersub&quot;</code>; the following shows a simplified and stripped-down example of a non-XS call, along with comments showing roughly what each function does. </p>
<pre><code> dMARK;
 U8 gimme = GIMME_V;
 bool hasargs = cBOOL(PL_op-&gt;op_flags &amp; OPf_STACKED);
 OP *retop = PL_op-&gt;op_next;
 I32 old_ss_ix = PL_savestack_ix;
 CV *cv = ....;
 /* ... make mortal copies of stack args which are PADTMPs here ... */
 /* ... do any additional savestack pushes here ... */
 /* Now push a new context entry of type 'CXt_SUB'; initially just
  * doing the actions common to all block types: */
 cx = cx_pushblock(CXt_SUB, gimme, MARK, old_ss_ix);
     /* this does (approximately):
         CXINC; /* cxstack_ix++ (grow if necessary) */
         cx = CX_CUR(); /* and get the address of new frame */
         cx-&gt;cx_type = CXt_SUB;
         cx-&gt;blk_gimme = gimme;
         cx-&gt;blk_oldsp = MARK - PL_stack_base;
         cx-&gt;blk_oldsaveix = old_ss_ix;
         cx-&gt;blk_oldcop = PL_curcop;
         cx-&gt;blk_oldmarksp = PL_markstack_ptr - PL_markstack;
         cx-&gt;blk_oldscopesp = PL_scopestack_ix;
         cx-&gt;blk_oldpm = PL_curpm;
         cx-&gt;blk_old_tmpsfloor = PL_tmps_floor;
         PL_tmps_floor = PL_tmps_ix;
     */
 /* then update the new context frame with subroutine-specific info,
  * such as the CV about to be executed: */
 cx_pushsub(cx, cv, retop, hasargs);
     /* this does (approximately):
         cx-&gt;blk_sub.cv = cv;
         cx-&gt;blk_sub.olddepth = CvDEPTH(cv);
         cx-&gt;blk_sub.prevcomppad = PL_comppad;
         cx-&gt;cx_type |= (hasargs) ? CXp_HASARGS : 0;
         cx-&gt;blk_sub.retop = retop;
         SvREFCNT_inc_simple_void_NN(cv);
     */
</code></pre>
<p> Note that <code>&quot;cx_pushblock()&quot;</code> sets two new floors: for the args stack (to <code>&quot;MARK&quot;</code>) and the temps stack (to <code>&quot;PL_tmps_ix&quot;</code>). While executing at this scope level, every <code>&quot;nextstate&quot;</code> (amongst others) will reset the args and tmps stack levels to these floors. Note that since <code>&quot;cx_pushblock&quot;</code> uses the current value of <code>&quot;PL_tmps_ix&quot;</code> rather than it being passed as an arg, this dictates at what point <code>&quot;cx_pushblock&quot;</code> should be called. In particular, any new mortals which should be freed only on scope exit (rather than at the next <code>&quot;nextstate&quot;</code>) should be created first. </p>
<p> Most callers of <code>&quot;cx_pushblock&quot;</code> simply set the new args stack floor to the top of the previous stack frame, but for <code>&quot;CXt_LOOP_LIST&quot;</code> it stores the items being iterated over on the stack, and so sets <code>&quot;blk_oldsp&quot;</code> to the top of these items instead. Note that, contrary to its name, <code>&quot;blk_oldsp&quot;</code> doesn&#8217;t always represent the value to restore <code>&quot;PL_stack_sp&quot;</code> to on scope exit. </p>
<p> Note the early capture of <code>&quot;PL_savestack_ix&quot;</code> to <code>&quot;old_ss_ix&quot;</code>, which is later passed as an arg to <code>&quot;cx_pushblock&quot;</code>. In the case of <code>&quot;pp_entersub&quot;</code>, this is because, although most values needing saving are stored in fields of the context struct, an extra value needs saving only when the debugger is running, and it doesn&#8217;t make sense to bloat the struct for this rare case. So instead it is saved on the savestack. Since this value gets calculated and saved before the context is pushed, it is necessary to pass the old value of <code>&quot;PL_savestack_ix&quot;</code> to <code>&quot;cx_pushblock&quot;</code>, to ensure that the saved value gets freed during scope exit. For most users of <code>&quot;cx_pushblock&quot;</code>, where nothing needs pushing on the save stack, <code>&quot;PL_savestack_ix&quot;</code> is just passed directly as an arg to <code>&quot;cx_pushblock&quot;</code>. </p>
<p> Note that where possible, values should be saved in the context struct rather than on the save stack; it&#8217;s much faster that way. </p>
<p> Normally <code>&quot;cx_pushblock&quot;</code> should be immediately followed by the appropriate <code>&quot;cx_pushfoo&quot;</code>, with nothing between them; this is because if code in-between could die (e.g. a warning upgraded to fatal), then the context stack unwinding code in <code>&quot;dounwind&quot;</code> would see (in the example above) a <code>&quot;CXt_SUB&quot;</code> context frame, but without all the subroutine-specific fields set, and crashes would soon ensue. </p>
<p> Where the two must be separate, initially set the type to <code>&quot;CXt_NULL&quot;</code> or <code>&quot;CXt_BLOCK&quot;</code>, and later change it to <code>&quot;CXt_foo&quot;</code> when doing the <code>&quot;cx_pushfoo&quot;</code>. This is exactly what <code>&quot;pp_enteriter&quot;</code> does, once it&#8217;s determined which type of loop it&#8217;s pushing.  </p>
<h3>Popping contexts</h3>
<p> Contexts are popped using <code>&quot;cx_popsub()&quot;</code> etc. and <code>&quot;cx_popblock()&quot;</code>. Note however, that unlike <code>&quot;cx_pushblock&quot;</code>, neither of these functions actually decrement the current context stack index; this is done separately using <code>&quot;CX_POP()&quot;</code>. </p>
<p> There are two main ways that contexts are popped. During normal execution as scopes are exited, functions like <code>&quot;pp_leave&quot;</code>, <code>&quot;pp_leaveloop&quot;</code> and <code>&quot;pp_leavesub&quot;</code> process and pop just one context using <code>&quot;cx_popfoo&quot;</code> and <code>&quot;cx_popblock&quot;</code>. On the other hand, things like <code>&quot;pp_return&quot;</code> and <code>&quot;next&quot;</code> may have to pop back several scopes until a sub or loop context is found, and exceptions (such as <code>&quot;die&quot;</code>) need to pop back contexts until an eval context is found. Both of these are accomplished by <code>&quot;dounwind()&quot;</code>, which is capable of processing and popping all contexts above the target one. </p>
<p> Here is a typical example of context popping, as found in <code>&quot;pp_leavesub&quot;</code> (simplified slightly): </p>
<pre><code> U8 gimme;
 PERL_CONTEXT *cx;
 SV **oldsp;
 OP *retop;
 cx = CX_CUR();
 gimme = cx-&gt;blk_gimme;
 oldsp = PL_stack_base + cx-&gt;blk_oldsp; /* last arg of previous frame */
 if (gimme == G_VOID)
     PL_stack_sp = oldsp;
 else
     leave_adjust_stacks(oldsp, oldsp, gimme, 0);
 CX_LEAVE_SCOPE(cx);
 cx_popsub(cx);
 cx_popblock(cx);
 retop = cx-&gt;blk_sub.retop;
 CX_POP(cx);
 return retop;
</code></pre>
<p> The steps above are in a very specific order, designed to be the reverse order of when the context was pushed. The first thing to do is to copy and/or protect any any return arguments and free any temps in the current scope. Scope exits like an rvalue sub normally return a mortal copy of their return args (as opposed to lvalue subs). It is important to make this copy before the save stack is popped or variables are restored, or bad things like the following can happen: </p>
<pre><code>    sub f { my $x =...; $x } # $x freed before we get to copy it
    sub f { /(...)/; $1 } # PL_curpm restored before $1 copied
</code></pre>
<p> Although we wish to free any temps at the same time, we have to be careful not to free any temps which are keeping return args alive; nor to free the temps we have just created while mortal copying return args. Fortunately, <code>&quot;leave_adjust_stacks()&quot;</code> is capable of making mortal copies of return args, shifting args down the stack, and only processing those entries on the temps stack that are safe to do so. </p>
<p> In void context no args are returned, so it&#8217;s more efficient to skip calling <code>&quot;leave_adjust_stacks()&quot;</code>. Also in void context, a <code>&quot;nextstate&quot;</code> op is likely to be imminently called which will do a <code>&quot;FREETMPS&quot;</code>, so there&#8217;s no need to do that either. </p>
<p> The next step is to pop savestack entries: <code>&quot;CX_LEAVE_SCOPE(cx)&quot;</code> is just defined as <code>&quot;LEAVE_SCOPE(cx-&gt;blk_oldsaveix)&quot;</code>. Note that during the popping, it&#8217;s possible for perl to call destructors, call <code>&quot;STORE&quot;</code> to undo localisations of tied vars, and so on. Any of these can die or call <code>&quot;exit()&quot;</code>. In this case, <code>&quot;dounwind()&quot;</code> will be called, and the current context stack frame will be re-processed. Thus it is vital that all steps in popping a context are done in such a way to support reentrancy. The other alternative, of decrementing <code>&quot;cxstack_ix&quot;</code> <i>before</i> processing the frame, would lead to leaks and the like if something died halfway through, or overwriting of the current frame. </p>
<p> <code>&quot;CX_LEAVE_SCOPE&quot;</code> itself is safely re-entrant: if only half the savestack items have been popped before dying and getting trapped by eval, then the <code>&quot;CX_LEAVE_SCOPE&quot;</code>s in <code>&quot;dounwind&quot;</code> or <code>&quot;pp_leaveeval&quot;</code> will continue where the first one left off. </p>
<p> The next step is the type-specific context processing; in this case <code>&quot;cx_popsub&quot;</code>. In part, this looks like: </p>
<pre><code>    cv = cx-&gt;blk_sub.cv;
    CvDEPTH(cv) = cx-&gt;blk_sub.olddepth;
    cx-&gt;blk_sub.cv = NULL;
    SvREFCNT_dec(cv);
</code></pre>
<p> where its processing the just-executed <font SIZE="-1">CV.</font> Note that before it decrements the <font SIZE="-1">CV</font>&#8216;s reference count, it nulls the <code>&quot;blk_sub.cv&quot;</code>. This means that if it re-enters, the <font SIZE="-1">CV</font> won&#8217;t be freed twice. It also means that you can&#8217;t rely on such type-specific fields having useful values after the return from <code>&quot;cx_popfoo&quot;</code>. </p>
<p> Next, <code>&quot;cx_popblock&quot;</code> restores all the various interpreter vars to their previous values or previous high water marks; it expands to: </p>
<pre><code>    PL_markstack_ptr = PL_markstack + cx-&gt;blk_oldmarksp;
    PL_scopestack_ix = cx-&gt;blk_oldscopesp;
    PL_curpm = cx-&gt;blk_oldpm;
    PL_curcop = cx-&gt;blk_oldcop;
    PL_tmps_floor = cx-&gt;blk_old_tmpsfloor;
</code></pre>
<p> Note that it <i>doesn&#8217;t</i> restore <code>&quot;PL_stack_sp&quot;</code>; as mentioned earlier, which value to restore it to depends on the context type (specifically <code>&quot;for (list) {}&quot;</code>), and what args (if any) it returns; and that will already have been sorted out earlier by <code>&quot;leave_adjust_stacks()&quot;</code>. </p>
<p> Finally, the context stack pointer is actually decremented by <code>&quot;CX_POP(cx)&quot;</code>. After this point, it&#8217;s possible that that the current context frame could be overwritten by other contexts being pushed. Although things like ties and <code>&quot;DESTROY&quot;</code> are supposed to work within a new context stack, it&#8217;s best not to assume this. Indeed on debugging builds, <code>&quot;CX_POP(cx)&quot;</code> deliberately sets <code>&quot;cx&quot;</code> to null to detect code that is still relying on the field values in that context frame. Note in the <code>&quot;pp_leavesub()&quot;</code> example above, we grab <code>&quot;blk_sub.retop&quot;</code> <i>before</i> calling <code>&quot;CX_POP&quot;</code>.  </p>
<h3>Redoing contexts</h3>
<p> Finally, there is <code>&quot;cx_topblock(cx)&quot;</code>, which acts like a super-<code>&quot;nextstate&quot;</code> as regards to resetting various vars to their base values. It is used in places like <code>&quot;pp_next&quot;</code>, <code>&quot;pp_redo&quot;</code> and <code>&quot;pp_goto&quot;</code> where rather than exiting a scope, we want to re-initialise the scope. As well as resetting <code>&quot;PL_stack_sp&quot;</code> like <code>&quot;nextstate&quot;</code>, it also resets <code>&quot;PL_markstack_ptr&quot;</code>, <code>&quot;PL_scopestack_ix&quot;</code> and <code>&quot;PL_curpm&quot;</code>. Note that it doesn&#8217;t do a <code>&quot;FREETMPS&quot;</code>.  </p>
<h2>Slab-based operator allocation</h2>
<p> <code>Note:</code> this section describes a non-public internal <font SIZE="-1">API</font> that is subject to change without notice. </p>
<p> Perl&#8217;s internal error-handling mechanisms implement <code>&quot;die&quot;</code> (and its internal equivalents) using longjmp. If this occurs during lexing, parsing or compilation, we must ensure that any ops allocated as part of the compilation process are freed. (Older Perl versions did not adequately handle this situation: when failing a parse, they would leak ops that were stored in C <code>&quot;auto&quot;</code> variables and not linked anywhere else.) </p>
<p> To handle this situation, Perl uses <i>op slabs</i> that are attached to the currently-compiling <font SIZE="-1">CV. A</font> slab is a chunk of allocated memory. New ops are allocated as regions of the slab. If the slab fills up, a new one is created (and linked from the previous one). When an error occurs and the <font SIZE="-1">CV</font> is freed, any ops remaining are freed. </p>
<p> Each op is preceded by two pointers: one points to the next op in the slab, and the other points to the slab that owns it. The next-op pointer is needed so that Perl can iterate over a slab and free all its ops. (Op structures are of different sizes, so the slab&#8217;s ops can&#8217;t merely be treated as a dense array.) The slab pointer is needed for accessing a reference count on the slab: when the last op on a slab is freed, the slab itself is freed. </p>
<p> The slab allocator puts the ops at the end of the slab first. This will tend to allocate the leaves of the op tree first, and the layout will therefore hopefully be cache-friendly. In addition, this means that there&#8217;s no need to store the size of the slab (see below on why slabs vary in size), because Perl can follow pointers to find the last op. </p>
<p> It might seem possible eliminate slab reference counts altogether, by having all ops implicitly attached to <code>&quot;PL_compcv&quot;</code> when allocated and freed when the <font SIZE="-1">CV</font> is freed. That would also allow <code>&quot;op_free&quot;</code> to skip <code>&quot;FreeOp&quot;</code> altogether, and thus free ops faster. But that doesn&#8217;t work in those cases where ops need to survive beyond their CVs, such as re-evals. </p>
<p> The <font SIZE="-1">CV</font> also has to have a reference count on the slab. Sometimes the first op created is immediately freed. If the reference count of the slab reaches 0, then it will be freed with the <font SIZE="-1">CV</font> still pointing to it. </p>
<p> CVs use the <code>&quot;CVf_SLABBED&quot;</code> flag to indicate that the <font SIZE="-1">CV</font> has a reference count on the slab. When this flag is set, the slab is accessible via <code>&quot;CvSTART&quot;</code> when <code>&quot;CvROOT&quot;</code> is not set, or by subtracting two pointers <code>&quot;(2*sizeof(I32 *))&quot;</code> from <code>&quot;CvROOT&quot;</code> when it is set. The alternative to this approach of sneaking the slab into <code>&quot;CvSTART&quot;</code> during compilation would be to enlarge the <code>&quot;xpvcv&quot;</code> struct by another pointer. But that would make all CVs larger, even though slab-based op freeing is typically of benefit only for programs that make significant use of string eval. </p>
<p> When the <code>&quot;CVf_SLABBED&quot;</code> flag is set, the <font SIZE="-1">CV</font> takes responsibility for freeing the slab. If <code>&quot;CvROOT&quot;</code> is not set when the <font SIZE="-1">CV</font> is freed or undeffed, it is assumed that a compilation error has occurred, so the op slab is traversed and all the ops are freed. </p>
<p> Under normal circumstances, the <font SIZE="-1">CV</font> forgets about its slab (decrementing the reference count) when the root is attached. So the slab reference counting that happens when ops are freed takes care of freeing the slab. In some cases, the <font SIZE="-1">CV</font> is told to forget about the slab (<code>&quot;cv_forget_slab&quot;</code>) precisely so that the ops can survive after the <font SIZE="-1">CV</font> is done away with. </p>
<p> Forgetting the slab when the root is attached is not strictly necessary, but avoids potential problems with <code>&quot;CvROOT&quot;</code> being written over. There is code all over the place, both in core and on <font SIZE="-1">CPAN,</font> that does things with <code>&quot;CvROOT&quot;</code>, so forgetting the slab makes things more robust and avoids potential problems. </p>
<p> Since the <font SIZE="-1">CV</font> takes ownership of its slab when flagged, that flag is never copied when a <font SIZE="-1">CV</font> is cloned, as one <font SIZE="-1">CV</font> could free a slab that another <font SIZE="-1">CV</font> still points to, since forced freeing of ops ignores the reference count (but asserts that it looks right). </p>
<p> To avoid slab fragmentation, freed ops are marked as freed and attached to the slab&#8217;s freed chain (an idea stolen from DBM::Deep). Those freed ops are reused when possible. Not reusing freed ops would be simpler, but it would result in significantly higher memory usage for programs with large <code>&quot;if (DEBUG) {...}&quot;</code> blocks. </p>
<p> <code>&quot;SAVEFREEOP&quot;</code> is slightly problematic under this scheme. Sometimes it can cause an op to be freed after its <font SIZE="-1">CV.</font> If the <font SIZE="-1">CV</font> has forcibly freed the ops on its slab and the slab itself, then we will be fiddling with a freed slab. Making <code>&quot;SAVEFREEOP&quot;</code> a no-op doesn&#8217;t help, as sometimes an op can be savefreed when there is no compilation error, so the op would never be freed. It holds a reference count on the slab, so the whole slab would leak. So <code>&quot;SAVEFREEOP&quot;</code> now sets a special flag on the op (<code>&quot;-&gt;op_savefree&quot;</code>). The forced freeing of ops after a compilation error won&#8217;t free any ops thus marked. </p>
<p> Since many pieces of code create tiny subroutines consisting of only a few ops, and since a huge slab would be quite a bit of baggage for those to carry around, the first slab is always very small. To avoid allocating too many slabs for a single <font SIZE="-1">CV,</font> each subsequent slab is twice the size of the previous. </p>
<p> Smartmatch expects to be able to allocate an op at run time, run it, and then throw it away. For that to work the op is simply malloced when PL_compcv hasn&#8217;t been set up. So all slab-allocated ops are marked as such (<code>&quot;-&gt;op_slabbed&quot;</code>), to distinguish them from malloced ops.  </p>
<h2>AUTHORS</h2>
<p> Until May 1997, this document was maintained by Jeff Okamoto &lt;okamoto [at] corp.hp.com&gt;. It is now maintained as part of Perl itself by the Perl 5 Porters &lt;perl5-porters [at] perl.org&gt;. </p>
<p> With lots of help and suggestions from Dean Roehrich, Malcolm Beattie, Andreas Koenig, Paul Hudson, Ilya Zakharevich, Paul Marquess, Neil Bowers, Matthew Green, Tim Bunce, Spider Boardman, Ulrich Pfeifer, Stephen McCamant, and Gurusamy Sarathy.  </p>
<h2>SEE ALSO</h2>
<p> perlapi, perlintern, perlxs, perlembed </p>
