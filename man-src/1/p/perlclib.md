---
title: "perlclib(1)"
name: "perlclib"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlclib/"
description: "perlclib – Internal replacements for standard C library functions"
---

<h2 class="name">NAME</h2>
<p> perlclib &#8211; Internal replacements for standard C library functions </p>
<h2>DESCRIPTION</h2>
<p> One thing Perl porters should note is that <i>perl</i> doesn&#8217;t tend to use that much of the C standard library internally; you&#8217;ll see very little use of, for example, the <i>ctype.h</i> functions in there. This is because Perl tends to reimplement or abstract standard library functions, so that we know exactly how they&#8217;re going to operate. </p>
<p> This is a reference card for people who are familiar with the C library and who want to do things the Perl way; to tell them which functions they ought to use instead of the more normal C functions.</p>
<h3>Conventions</h3>
<p> In the following tables:</p>
<dl>
<dt>&quot;t&quot;</p>
<dd> is a type.</p>
<dt>&quot;p&quot;</p>
<dd> is a pointer.</p>
<dt>&quot;n&quot;</p>
<dd> is a number.</p>
<dt>&quot;s&quot;</p>
<dd> is a string.</dl>
<p> <tt>&quot;sv&quot;</tt>, <tt>&quot;av&quot;</tt>, <tt>&quot;hv&quot;</tt>, etc. represent variables of their respective types.</p>
<h3>File Operations</h3>
<p> Instead of the <i>stdio.h</i> functions, you should use the Perl abstraction layer. Instead of <tt>&quot;FILE*&quot;</tt> types, you need to be handling <tt>&quot;PerlIO*&quot;</tt> types. Don&#8217;t forget that with the new PerlIO layered I/O abstraction <tt>&quot;FILE*&quot;</tt> types may not even be available. See also the <tt>&quot;perlapio&quot;</tt> documentation for more information about the following functions: </p>
<pre>
 Instead Of:                 Use:
 stdin                       PerlIO_stdin()
 stdout                      PerlIO_stdout()
 stderr                      PerlIO_stderr()
 fopen(fn, mode)             PerlIO_open(fn, mode)
 freopen(fn, mode, stream)   PerlIO_reopen(fn, mode, perlio) (Dep-
                               recated)
 fflush(stream)              PerlIO_flush(perlio)
 fclose(stream)              PerlIO_close(perlio)
</pre>
<h3>File Input and Output</h3>
<pre><code>
Instead Of : Use : fprintf(stream, fmt, ...) PerlIO_printf(perlio, fmt, ...)
                       [f] getc(stream) PerlIO_getc(perlio)
                           [f] putc(stream, n) PerlIO_putc(perlio, n)
                               ungetc(n, stream) PerlIO_ungetc(perlio, n)
</code></pre>
<p> Note that the PerlIO equivalents of <tt>&quot;fread&quot;</tt> and <tt>&quot;fwrite&quot;</tt> are slightly different from their C library counterparts: </p>
<pre>
 fread(p, size, n, stream)   PerlIO_read(perlio, buf, numbytes)
 fwrite(p, size, n, stream)  PerlIO_write(perlio, buf, numbytes)
 fputs(s, stream)            PerlIO_puts(perlio, s)
</pre>
<p> There is no equivalent to <tt>&quot;fgets&quot;</tt>; one should use <tt>&quot;sv_gets&quot;</tt> instead: </p>
<pre>
 fgets(s, n, stream)         sv_gets(sv, perlio, append)
</pre>
<h3>File Positioning</h3>
<pre>
 Instead Of:                 Use:
 feof(stream)                PerlIO_eof(perlio)
 fseek(stream, n, whence)    PerlIO_seek(perlio, n, whence)
 rewind(stream)              PerlIO_rewind(perlio)
 fgetpos(stream, p)          PerlIO_getpos(perlio, sv)
 fsetpos(stream, p)          PerlIO_setpos(perlio, sv)
 ferror(stream)              PerlIO_error(perlio)
 clearerr(stream)            PerlIO_clearerr(perlio)
</pre>
<h3>Memory Management and String Handling</h3>
<pre>
 Instead Of:                    Use:
 t* p = <a href="//www.systutorials.com/docs/linux/man/n-malloc/">malloc</a>(n)               Newx(p, n, t)
 t* p = calloc(n, s)            Newxz(p, n, t)
 p = realloc(p, n)              Renew(p, n, t)
 memcpy(dst, src, n)            Copy(src, dst, n, t)
 memmove(dst, src, n)           Move(src, dst, n, t)
 memcpy(dst, src, sizeof(t))    StructCopy(src, dst, t)
 memset(dst, 0, n * sizeof(t))  Zero(dst, n, t)
 memzero(dst, 0)                Zero(dst, n, char)
 free(p)                        Safefree(p)
 strdup(p)                      savepv(p)
 strndup(p, n)                  savepvn(p, n) (Hey, strndup doesn't
                                               exist!)
 strstr(big, little)            instr(big, little)
 strcmp(s1, s2)                 strLE(s1, s2) / strEQ(s1, s2)
                                              / strGT(s1,s2)
 strncmp(s1, s2, n)             strnNE(s1, s2, n) / strnEQ(s1, s2, n)
 memcmp(p1, p2, n)              memNE(p1, p2, n)
 !memcmp(p1, p2, n)             memEQ(p1, p2, n)
</pre>
<p> Notice the different order of arguments to <tt>&quot;Copy&quot;</tt> and <tt>&quot;Move&quot;</tt> than used in <tt>&quot;memcpy&quot;</tt> and <tt>&quot;memmove&quot;</tt>. </p>
<p> Most of the time, though, you&#8217;ll want to be dealing with SVs internally instead of raw <tt>&quot;char *&quot;</tt> strings: </p>
<pre>
 strlen(s)                   sv_len(sv)
 strcpy(dt, src)             sv_setpv(sv, s)
 strncpy(dt, src, n)         sv_setpvn(sv, s, n)
 strcat(dt, src)             sv_catpv(sv, s)
 strncat(dt, src)            sv_catpvn(sv, s)
 sprintf(s, fmt, ...)        sv_setpvf(sv, fmt, ...)
</pre>
<p> Note also the existence of <tt>&quot;sv_catpvf&quot;</tt> and <tt>&quot;sv_vcatpvfn&quot;</tt>, combining concatenation with formatting. </p>
<p> Sometimes instead of zeroing the allocated heap by using <code>Newxz()</code> you should consider &#8220;poisoning&#8221; the data. This means writing a bit pattern into it that should be illegal as pointers (and floating point numbers), and also hopefully surprising enough as integers, so that any code attempting to use the data without forethought will break sooner rather than later. Poisoning can be done using the <code>Poison()</code> macros, which have similar arguments to <code>Zero()</code>: </p>
<pre>
 PoisonWith(dst, n, t, b)    scribble memory with byte b
 PoisonNew(dst, n, t)        equal to PoisonWith(dst, n, t, 0xAB)
 PoisonFree(dst, n, t)       equal to PoisonWith(dst, n, t, 0xEF)
 Poison(dst, n, t)           equal to PoisonFree(dst, n, t)
</pre>
<h3>Character Class Tests</h3>
<p> There are several types of character class tests that Perl implements. The only ones described here are those that directly correspond to C library functions that operate on 8-bit characters, but there are equivalents that operate on wide characters, and <font SIZE="-1">UTF-8</font> encoded strings. All are more fully described in &#8220;Character classification&#8221; in perlapi and &#8220;Character case changing&#8221; in perlapi. </p>
<p> The C library routines listed in the table below return values based on the current locale. Use the entries in the final column for that functionality. The other two columns always assume a <font SIZE="-1">POSIX</font> (or C) locale. The entries in the <font SIZE="-1">ASCII</font> column are only meaningful for <font SIZE="-1">ASCII</font> inputs, returning <font SIZE="-1">FALSE</font> for anything else. Use these only when you <code>know</code> that is what you want. The entries in the Latin1 column assume that the non-ASCII 8-bit characters are as Unicode defines, them, the same as <font SIZE="-1">ISO-8859-1,</font> often called Latin 1. </p>
<pre>
 Instead Of:  Use for ASCII:   Use for Latin1:      Use for locale:
 isalnum(c)  isALPHANUMERIC(c) isALPHANUMERIC_L1(c) isALPHANUMERIC_LC(c)
 isalpha(c)  isALPHA(c)        isALPHA_L1(c)        isALPHA_LC(u )
 isascii(c)  isASCII(c)                             isASCII_LC(c)
 isblank(c)  isBLANK(c)        isBLANK_L1(c)        isBLANK_LC(c)
 iscntrl(c)  isCNTRL(c)        isCNTRL_L1(c)        isCNTRL_LC(c)
 isdigit(c)  isDIGIT(c)        isDIGIT_L1(c)        isDIGIT_LC(c)
 isgraph(c)  isGRAPH(c)        isGRAPH_L1(c)        isGRAPH_LC(c)
 islower(c)  isLOWER(c)        isLOWER_L1(c)        isLOWER_LC(c)
 isprint(c)  isPRINT(c)        isPRINT_L1(c)        isPRINT_LC(c)
 ispunct(c)  isPUNCT(c)        isPUNCT_L1(c)        isPUNCT_LC(c)
 isspace(c)  isSPACE(c)        isSPACE_L1(c)        isSPACE_LC(c)
 isupper(c)  isUPPER(c)        isUPPER_L1(c)        isUPPER_LC(c)
 isxdigit(c) isXDIGIT(c)       isXDIGIT_L1(c)       isXDIGIT_LC(c)
 tolower(c)  toLOWER(c)        toLOWER_L1(c)        toLOWER_LC(c)
 toupper(c)  toUPPER(c)                             toUPPER_LC(c)
</pre>
<p> To emphasize that you are operating only on <font SIZE="-1">ASCII</font> characters, you can append <tt>&quot;_A&quot;</tt> to each of the macros in the <font SIZE="-1">ASCII</font> column: <tt>&quot;isALPHA_A&quot;</tt>, <tt>&quot;isDIGIT_A&quot;</tt>, and so on. </p>
<p> (There is no entry in the Latin1 column for <tt>&quot;isascii&quot;</tt> even though there is an <tt>&quot;isASCII_L1&quot;</tt>, which is identical to <tt>&quot;isASCII&quot;</tt>; the latter name is clearer. There is no entry in the Latin1 column for <tt>&quot;toupper&quot;</tt> because the result can be non-Latin1. You have to use <tt>&quot;toUPPER_uni&quot;</tt>, as described in &#8220;Character case changing&#8221; in perlapi.)</p>
<h3><i>stdlib.h</i> functions</h3>
<pre>
 Instead Of:                 Use:
 atof(s)                     Atof(s)
 atoi(s)                     grok_atoUV(s, &amp;uv, &amp;e)
 atol(s)                     grok_atoUV(s, &amp;uv, &amp;e)
 strtod(s, &amp;p)               my_atof3(s, &amp;nv, &amp;p) is the closest we have
 strtol(s, &amp;p, n)            grok_atoUV(s, &amp;uv, &amp;e)
 strtoul(s, &amp;p, n)           grok_atoUV(s, &amp;uv, &amp;e)
</pre>
<p> Typical use is to do range checks on <tt>&quot;uv&quot;</tt> before casting: </p>
<p>int i;<br />
UV uv;<br />
char *end_ptr = input_end;<br />
if (grok_atoUV(input, &amp;uv, &amp;end_ptr) &amp;&amp; uv &lt;= INT_MAX)<br />
    i = (int)uv;<br />
&#8230; /* continue parsing from end_ptr */<br />
}<br />
else<br />
{<br />
    &#8230; /* parse error: not a decimal integer in range 0 .. MAX_IV */<br />
}</p>
<p> Notice also the <tt>&quot;grok_bin&quot;</tt>, <tt>&quot;grok_hex&quot;</tt>, and <tt>&quot;grok_oct&quot;</tt> functions in <i>numeric.c</i> for converting strings representing numbers in the respective bases into <tt>&quot;NV&quot;</tt>s. Note that <code>grok_atoUV()</code> doesn&#8217;t handle negative inputs, or leading whitespace (being purposefully strict). </p>
<p> Note that <code>strtol()</code> and <code>strtoul()</code> may be disguised as <code>Strtol()</code>, <code>Strtoul()</code>, <code>Atol()</code>, <code>Atoul()</code>. Avoid those, too. </p>
<p> In theory <tt>&quot;Strtol&quot;</tt> and <tt>&quot;Strtoul&quot;</tt> may not be defined if the machine perl is built on doesn&#8217;t actually have strtol and strtoul. But as those 2 functions are part of the 1989 <font SIZE="-1">ANSI C</font> spec we suspect you&#8217;ll find them everywhere by now. </p>
<pre><code>
int rand() double Drand01()
    srand(n)
{
    seedDrand01((Rand_seed_t)n);
    PL_srand_called = TRUE;
}
exit(n) my_exit(n)
    system(s) Don't. Look at pp_system or use my_popen. getenv(s) PerlEnv_getenv(s)
        setenv(s, val) my_setenv(s, val)
</code></pre>
<h3>Miscellaneous functions</h3>
<p> You should not even <code>want</code> to use <i>setjmp.h</i> functions, but if you think you do, use the <tt>&quot;JMPENV&quot;</tt> stack in <i>scope.h</i> instead. </p>
<p> For <tt>&quot;signal&quot;</tt>/<tt>&quot;sigaction&quot;</tt>, use <tt>&quot;rsignal(signo, handler)&quot;</tt>.</p>
<h2>SEE ALSO</h2>
<p> perlapi, perlapio, perlguts </p>
<h2>Index</h2>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd></dl>
