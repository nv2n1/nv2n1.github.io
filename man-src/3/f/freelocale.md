---
title: "freelocale(3)"
name: "freelocale"
section: "3"
letter: "f"
url: "/docs/linux/man/3-freelocale/"
---

<h2 class="name">NAME</h2>
 

 newlocale, freelocale - create, modify, and free a locale object 

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;locale.h&gt;
locale_t newlocale(int category_mask, const char *locale,
                   locale_t base);
void freelocale(locale_t locobj);
</code></pre> 

 Feature Test Macro Requirements for glibc (see <b><a HREF="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></b>(7)): 

 <b>newlocale</b>(), <b>freelocale</b>():
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;700
<dt>Before glibc 2.10:
<dd> _GNU_SOURCE</dl>
</dl>

<h2>DESCRIPTION</h2>

 The <b>newlocale</b>() function creates a new locale object, or modifies an existing object, returning a reference to the new or modified object as the function result. Whether the call creates a new object or modifies an existing object is determined by the value of <i>base</i>:
<dl>
<dt>*
<dd> If <i>base</i> is <i>(locale_t)&nbsp;0</i>, a new object is created.
<dt>*
<dd> If <i>base</i> refers to valid existing locale object (i.e., an object returned by a previous call to <b>newlocale</b>() or <b><a HREF="/docs/linux/man/3-duplocale/">duplocale</a></b>(3)), then that object is modified by the call. If the call is successful, the contents of <i>base</i> are unspecified (in particular, the object referred to by <i>base</i> may be freed, and a new object created). Therefore, the caller should ensure that it stops using <i>base</i> before the call to <b>newlocale</b>(), and should subsequently refer to the modified object via the reference returned as the function result. If the call fails, the contents of <i>base</i> remain valid and unchanged.</dl>
 

 If <i>base</i> is the special locale object <b>LC_GLOBAL_LOCALE</b> (see <b><a HREF="/docs/linux/man/3-duplocale/">duplocale</a></b>(3)), or is not <i>(locale_t)&nbsp;0</i> and is not a valid locale object handle, the behavior is undefined. 

 The <i>category_mask</i> argument is a bit mask that specifies the locale categories that are to be set in a newly created locale object or modified in an existing object. The mask is constructed by a bitwise OR of the constants <b>LC_ADDRESS_MASK</b>, <b>LC_CTYPE_MASK</b>, <b>LC_COLLATE_MASK</b>, <b>LC_IDENTIFICATION_MASK</b>, <b>LC_MEASUREMENT_MASK</b>, <b>LC_MESSAGES_MASK</b>, <b>LC_MONETARY_MASK</b>, <b>LC_NUMERIC_MASK</b>, <b>LC_NAME_MASK</b>, <b>LC_PAPER_MASK</b>, <b>LC_TELEPHONE_MASK</b>, and <b>LC_TIME_MASK</b>. Alternatively, the mask can be specified as <b>LC_ALL_MASK</b>, which is equivalent to ORing all of the preceding constants. 

 For each category specified in <i>category_mask</i>, the locale data from <i>locale</i> will be used in the object returned by <b>newlocale</b>(). If a new locale object is being created, data for all categories not specified in <i>category_mask</i> is taken from the default (&quot;POSIX&quot;) locale. 

 The following preset values of <i>locale</i> are defined for all categories that can be specified in <i>category_mask</i>:
<dl>
<dt>&quot;POSIX&quot;
<dd> A minimal locale environment for C language programs.
<dt>&quot;C&quot;
<dd> Equivalent to &quot;POSIX&quot;.
<dt>&quot;&quot;
<dd> An implementation-defined native environment corresponding to the values of the <b>LC_*</b> and <b>LANG</b> environment variables (see <b><a HREF="/docs/linux/man/7-locale/">locale</a></b>(7)).</dl>

<h3>freelocale()</h3>

 The <b>freelocale</b>() function deallocates the resources associated with <i>locobj</i>, a locale object previously returned by a call to <b>newlocale</b>() or <b><a HREF="/docs/linux/man/3-duplocale/">duplocale</a></b>(3). If <i>locobj</i> is <b>LC_GLOBAL_LOCALE</b> or is not valid locale object handle, the results are undefined. 

 Once a locale object has been freed, the program should make no further use of it.

<h2>RETURN VALUE</h2>

 On success, <b>newlocale</b>() returns a handle that can be used in calls to <b><a HREF="/docs/linux/man/3-duplocale/">duplocale</a></b>(3), <b>freelocale</b>(), and other functions that take a <i>locale_t</i> argument. On error, <b>newlocale</b>() returns <i>(locale_t)&nbsp;0,</i> and sets <i>errno</i> to indicate the cause of the error.

<h2>ERRORS</h2>

<dl>
<dt><b>EINVAL</b>
<dd> One or more bits in <i>category_mask</i> do not correspond to a valid locale category.
<dt><b>EINVAL</b>
<dd> <i>locale</i> is NULL.
<dt><b>ENOENT</b>
<dd> <i>locale</i> is not a string pointer referring to a valid locale.
<dt><b>ENOMEM</b>
<dd> Insufficient memory to create a locale object.</dl>

<h2>VERSIONS</h2>

 The <b>newlocale</b>() and <b>freelocale</b>() functions first appeared in version 2.3 of the GNU C library.

<h2>CONFORMING TO</h2>

 POSIX.1-2008.

<h2>NOTES</h2>

 Each locale object created by <b>newlocale</b>() should be deallocated using <b>freelocale</b>().

<h2>EXAMPLES</h2>

 The program below takes up to two command-line arguments, which each identify locales. The first argument is required, and is used to set the <b>LC_NUMERIC</b> category in a locale object created using <b>newlocale</b>(). The second command-line argument is optional; if it is present, it is used to set the <b>LC_TIME</b> category of the locale object. 

 Having created and initialized the locale object, the program then applies it using <b><a HREF="/docs/linux/man/3-uselocale/">uselocale</a></b>(3), and then tests the effect of the locale changes by:
<dl>
<dt>1.
<dd> Displaying a floating-point number with a fractional part. This output will be affected by the <b>LC_NUMERIC</b> setting. In many European-language locales, the fractional part of the number is separated from the integer part using a comma, rather than a period.
<dt>2.
<dd> Displaying the date. The format and language of the output will be affected by the <b>LC_TIME</b> setting.</dl>
 

 The following shell sessions show some example runs of this program. 

 Set the <b>LC_NUMERIC</b> category to <i>fr_FR</i> (French): 

 $ <b>./a.out fr_FR</b> 123456,789 Fri Mar 7 00:25:08 2014 

 Set the <b>LC_NUMERIC</b> category to <i>fr_FR</i> (French), and the <b>LC_TIME</b> category to <i>it_IT</i> (Italian): 

 $ <b>./a.out fr_FR it_IT</b> 123456,789 ven 07 mar 2014 00:26:01 CET 

 Specify the <b>LC_TIME</b> setting as an empty string, which causes the value to be taken from environment variable settings (which, here, specify <i>mi_NZ</i>, New Zealand Māori): 

 $ LC_ALL=mi_NZ ./a.out fr_FR &quot;&quot; 123456,789 Te Paraire, te 07 o Poutū-te-rangi, 2014 00:38:44 CET

<h3>Program source</h3>

 #define _XOPEN_SOURCE 700 #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;locale.h&gt; #include &lt;time.h&gt; 

 #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) 

 int main(int argc, char *argv[]) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[100]; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t t; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t s; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct tm&nbsp;*tm; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locale_t loc, nloc; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s locale1&nbsp;[locale2]\n&quot;, argv[0]); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a new locale object, taking the LC_NUMERIC settings 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;from the locale specified in argv[1]&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loc&nbsp;=&nbsp;newlocale(LC_NUMERIC_MASK, argv[1],&nbsp;(locale_t)&nbsp;0); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(loc&nbsp;==&nbsp;(locale_t)&nbsp;0) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;newlocale&quot;); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If a second command-line argument was specified, modify the 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locale object to take the LC_TIME settings from the locale 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specified in argv[2]. We assign the result of this newlocale() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call to&nbsp;'nloc'&nbsp;rather than&nbsp;'loc', since in some cases, we might 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;want to preserve&nbsp;'loc'&nbsp;if this call fails.&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;2)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nloc&nbsp;=&nbsp;newlocale(LC_TIME_MASK, argv[2], loc); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nloc&nbsp;==&nbsp;(locale_t)&nbsp;0) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;newlocale&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loc&nbsp;=&nbsp;nloc; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Apply the newly created locale to this thread&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uselocale(loc); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Test effect of LC_NUMERIC&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%8.3f\n&quot;, 123456.789); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Test effect of LC_TIME&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t&nbsp;=&nbsp;time(NULL); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm&nbsp;=&nbsp;localtime(&amp;t); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(tm&nbsp;==&nbsp;NULL) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;time&quot;); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;strftime(buf, sizeof(buf),&nbsp;&quot;%c&quot;, tm); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;0) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;strftime&quot;); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s\n&quot;, buf); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Free the locale object&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uselocale(LC_GLOBAL_HANDLE);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;So&nbsp;'loc'&nbsp;is no longer in use&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freelocale(loc); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-locale/">locale</a></b>(1), <b><a HREF="/docs/linux/man/3-duplocale/">duplocale</a></b>(3), <b><a HREF="/docs/linux/man/3-setlocale/">setlocale</a></b>(3), <b><a HREF="/docs/linux/man/3-uselocale/">uselocale</a></b>(3), <b><a HREF="/docs/linux/man/5-locale/">locale</a></b>(5), <b><a HREF="/docs/linux/man/7-locale/">locale</a></b>(7)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 

<h2>Index</h2>


