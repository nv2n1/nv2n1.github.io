---
title: "unicode_default_chset(3)"
name: "unicode_default_chset"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_default_chset/"
description: "unicode_default_chset, unicode_locale_chset – return the system character set name"
---

<p>unicode_default_chset, unicode_locale_chset &#8211; return the system character set name</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

const char *unicode_default_chset(void);

const char *unicode_locale_chset(void);</code></pre>
<h2>Description</h2>
<p><code>unicode_default_chset</code>() returns the name of the system environment character set (usually &#8220;nl_langinfo(CODESET)&#8221;, or from some suitable environment variable). <code>unicode_locale_chset</code>() returns the name of the current application locale&#8217;s character set.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_convert_tocase/">unicode_convert_tocase</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>
<dd>Author</dl>
