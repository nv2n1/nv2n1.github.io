---
title: "newlocale(3)"
name: "newlocale"
section: "3"
letter: "n"
url: "/docs/linux/man/3-newlocale/"
description: "newlocale, freelocale – create, modify, and free a locale object"
---

<p>newlocale, freelocale &#8211; create, modify, and free a locale object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;locale.h&gt;

locale_t newlocale(int category_mask, const char *locale,
                   locale_t base);

void freelocale(locale_t locobj);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>newlocale</code>(), <code>freelocale</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;700</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>newlocale</code>() function creates a new locale object, or modifies an existing object, returning a reference to the new or modified object as the function result. Whether the call creates a new object or modifies an existing object is determined by the value of <i>base</i>:</p>
<dl>
<dt>*</p>
<dd>If <i>base</i> is <i>(locale_t)&nbsp;0</i>, a new object is created.</p>
<dt>*</p>
<dd>If <i>base</i> refers to valid existing locale object (i.e., an object returned by a previous call to <code>newlocale</code>() or <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)), then that object is modified by the call. If the call is successful, the contents of <i>base</i> are unspecified (in particular, the object referred to by <i>base</i> may be freed, and a new object created). Therefore, the caller should ensure that it stops using <i>base</i> before the call to <code>newlocale</code>(), and should subsequently refer to the modified object via the reference returned as the function result. If the call fails, the contents of <i>base</i> remain valid and unchanged.</dl>
<p> If <i>base</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> (see <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)), or is not <i>(locale_t)&nbsp;0</i> and is not a valid locale object handle, the behavior is undefined. </p>
<p> The <i>category_mask</i> argument is a bit mask that specifies the locale categories that are to be set in a newly created locale object or modified in an existing object. The mask is constructed by a bitwise OR of the constants <code>LC_ADDRESS_MASK</code>, <code>LC_CTYPE_MASK</code>, <code>LC_COLLATE_MASK</code>, <code>LC_IDENTIFICATION_MASK</code>, <code>LC_MEASUREMENT_MASK</code>, <code>LC_MESSAGES_MASK</code>, <code>LC_MONETARY_MASK</code>, <code>LC_NUMERIC_MASK</code>, <code>LC_NAME_MASK</code>, <code>LC_PAPER_MASK</code>, <code>LC_TELEPHONE_MASK</code>, and <code>LC_TIME_MASK</code>. Alternatively, the mask can be specified as <code>LC_ALL_MASK</code>, which is equivalent to ORing all of the preceding constants. </p>
<p> For each category specified in <i>category_mask</i>, the locale data from <i>locale</i> will be used in the object returned by <code>newlocale</code>(). If a new locale object is being created, data for all categories not specified in <i>category_mask</i> is taken from the default (&quot;POSIX&quot;) locale. </p>
<p> The following preset values of <i>locale</i> are defined for all categories that can be specified in <i>category_mask</i>:</p>
<dl>
<dt>&quot;POSIX&quot;</p>
<dd>A minimal locale environment for C language programs.</p>
<dt>&quot;C&quot;</p>
<dd>Equivalent to &quot;POSIX&quot;.</p>
<dt>&quot;&quot;</p>
<dd>An implementation-defined native environment corresponding to the values of the <code>LC_*</code> and <code>LANG</code> environment variables (see <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)).</dl>
<h3>freelocale()</h3>
<p>The <code>freelocale</code>() function deallocates the resources associated with <i>locobj</i>, a locale object previously returned by a call to <code>newlocale</code>() or <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3). If <i>locobj</i> is <code>LC_GLOBAL_LOCALE</code> or is not valid locale object handle, the results are undefined. </p>
<p> Once a locale object has been freed, the program should make no further use of it.</p>
<h2>Return Value</h2>
<p>On success, <code>newlocale</code>() returns a handle that can be used in calls to <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3), <code>freelocale</code>(), and other functions that take a <i>locale_t</i> argument. On error, <code>newlocale</code>() returns <i>(locale_t)&nbsp;0,</i> and sets <i>errno</i> to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>One or more bits in <i>category_mask</i> do not correspond to a valid locale category.</p>
<dt><code>EINVAL</code></p>
<dd><i>locale</i> is NULL.</p>
<dt><code>ENOENT</code></p>
<dd><i>locale</i> is not a string pointer referring to a valid locale.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory to create a locale object.</dl>
<h2>Versions</h2>
<p>The <code>newlocale</code>() and <code>freelocale</code>() functions first appeared in version 2.3 of the GNU C library.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2008.</p>
<h2>Notes</h2>
<p>Each locale object created by <code>newlocale</code>() should be deallocated using <code>freelocale</code>().</p>
<h2>Examples</h2>
<p>The program below takes up to two command-line arguments, which each identify locales. The first argument is required, and is used to set the <code>LC_NUMERIC</code> category in a locale object created using <code>newlocale</code>(). The second command-line argument is optional; if it is present, it is used to set the <code>LC_TIME</code> category of the locale object. Having created and initialized the locale object, the program then applies it using <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), and then tests the effect of the locale changes by:</p>
<dl>
<dt>1.</p>
<dd>Displaying a floating-point number with a fractional part. This output will be affected by the <code>LC_NUMERIC</code> setting. In many European-language locales, the fractional part of the number is separated from the integer part using a comma, rather than a period.</p>
<dt>2.</p>
<dd>Displaying the date. The format and language of the output will be affected by the <code>LC_TIME</code> setting.</dl>
<p> The following shell sessions show some example runs of this program. Set the <code>LC_NUMERIC</code> category to <i>fr_FR</i> (French): $ <code>./a.out fr_FR</code> 123456,789 Fri Mar 7 00:25:08 2014 Set the <code>LC_NUMERIC</code> category to <i>fr_FR</i> (French), and the <code>LC_TIME</code> category to <i>it_IT</i> (Italian): $ <code>./a.out fr_FR it_IT</code> 123456,789 ven 07 mar 2014 00:26:01 CET Specify the <code>LC_TIME</code> setting as an empty string, which causes the value to be taken from environment variable settings (which, here, specify <i>mi_NZ</i>, New Zealand Māori): </p>
<pre><code>$ LC_ALL=mi_NZ ./a.out fr_FR &quot;&quot;
123456,789
Te Paraire, te 07 o Poutū-te-rangi, 2014 00:38:44 CET



Program source


#define _XOPEN_SOURCE 700
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;locale.h&gt;
#include &lt;time.h&gt;
#define errExit(msg)    do { perror(msg); exit(EXIT_FAILURE); \
} while (0)
int
main(int argc, char *argv[])
{
    char buf[100];
    time_t t;
    size_t s;
    struct tm *tm;
    locale_t loc, nloc;
    if (argc &lt; 2) {
        fprintf(stderr, &quot;Usage: %s locale1 [locale2]
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    /* Create a new locale object, taking the LC_NUMERIC settings
    from the locale specified in argv[1] */
    loc = newlocale(LC_NUMERIC_MASK, argv[1], (locale_t) 0);
    if (loc == (locale_t) 0)
    errExit(&quot;newlocale&quot;);
    /* If a second command-line argument was specified, modify the
    locale object to take the LC_TIME settings from the locale
    specified in argv[2]. We assign the result of this newlocale()
    call to 'nloc' rather than 'loc', since in some cases, we might
    want to preserve 'loc' if this call fails. */
    if (argc &gt; 2) {
        nloc = newlocale(LC_TIME_MASK, argv[2], loc);
        if (nloc == (locale_t) 0)
        errExit(&quot;newlocale&quot;);
        loc = nloc;
    }
    /* Apply the newly created locale to this thread */
    uselocale(loc);
    /* Test effect of LC_NUMERIC */
    printf(&quot;%8.3f
&quot;, 123456.789);
    /* Test effect of LC_TIME */
    t = time(NULL);
    tm = localtime(&amp;t);
    if (tm == NULL)
    errExit(&quot;time&quot;);
    s = strftime(buf, sizeof(buf), &quot;%c&quot;, tm);
    if (s == 0)
    errExit(&quot;strftime&quot;);
    printf(&quot;%s
&quot;, buf);
    /* Free the locale object */
    uselocale(LC_GLOBAL_HANDLE);    /* So 'loc' is no longer in use */
    freelocale(loc);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
