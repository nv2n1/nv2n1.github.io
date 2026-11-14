---
title: "perlguts(1)"
name: "perlguts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlguts/"
description: "perlguts – Introduction to the Perl API"
---

<h2 class="name">NAME</h2>
<p> perlguts &#8211; Introduction to the Perl API </p>
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
s[len + newlen] = &#8216;
