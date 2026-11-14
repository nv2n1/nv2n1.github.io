---
title: "uselocale(3)"
name: "uselocale"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uselocale/"
description: "uselocale – set/get the locale for the calling thread"
---

<p>uselocale &#8211; set/get the locale for the calling thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;locale.h&gt;

locale_t uselocale(locale_t newloc);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>uselocale</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;700</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>uselocale</code>() function sets the current locale for the calling thread, and returns the thread&#8217;s previously current locale. After a successful call to <code>uselocale</code>(), any calls by this thread to functions that depend on the locale will operate as though the locale has been set to <i>newloc</i>. </p>
<p> The <i>newloc</i> argument can have one of the following values:</p>
<dl>
<dt>A handle returned by a call to <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3) or <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)</p>
<dd>The calling thread&#8217;s current locale is set to the specified locale.</p>
<dt>The special locale object handle <code>LC_GLOBAL_LOCALE</code></p>
<dd>The calling thread&#8217;s current locale is set to the global locale determined by <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3).</p>
<dt><i>(locale_t) 0</i></p>
<dd>The calling thread&#8217;s current locale is left unchanged (and the current locale is returned as the function result).</dl>
<h2>Return Value</h2>
<p>On success, <code>uselocale</code>() returns the locale handle that was set by the previous call to <code>uselocale</code>() in this thread, or <code>LC_GLOBAL_LOCALE</code> if there was no such previous call. On error, it returns <i>(locale_t)&nbsp;0</i>, and sets <i>errno</i> to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>newloc</i> does not refer to a valid locale object.</dl>
<h2>Versions</h2>
<p>The <code>uselocale</code>() function first appeared in version 2.3 of the GNU C library.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2008.</p>
<h2>Notes</h2>
<p>Unlike <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code>uselocale</code>() does not allow selective replacement of individual locale categories. To employ a locale that differs in only a few categories from the current locale, use calls to <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3) and <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3) to obtain a locale object equivalent to the current locale and modify the desired categories in that object.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3) and <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3), <code><a href="/docs/linux/man/3-freelocale/">freelocale</a></code>(3), <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
