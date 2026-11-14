---
title: "stringprep_locale_charset(3)"
name: "stringprep_locale_charset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_locale_charset/"
description: "stringprep_locale_charset – API function"
---

<p>stringprep_locale_charset &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
const char *stringprep_locale_charset(void);</code></pre>
<h2>Arguments</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>Description</h2>
<p>Find out current locale charset. The function respect the CHARSET environment variable, but typically uses nl_langinfo(CODESET) when it is supported. It fall back on &quot;ASCII&quot; if CHARSET isn&#8217;t set and nl_langinfo isn&#8217;t supported or return anything. </p>
<p> Note that this function return the application&#8217;s locale&#8217;s preferred charset (or thread&#8217;s locale&#8217;s preffered charset, if your system support thread-specific locales). It does not return what the system may be using. Thus, if you receive data from external sources you cannot in general use this function to guess what charset it is encoded in. Use stringprep_convert from the external representation into the charset returned by this function, to have data in the locale encoding.</p>
<h2>Return Value</h2>
<p>Return the character set used by the current locale. It will never return NULL, but use &quot;ASCII&quot; as a fallback.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-libidn [at] gnu.org&gt;. GNU Libidn home page: <a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2013 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>See Also</h2>
<p>The full documentation for <code>libidn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libidn</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info libidn</code></dl>
<p> should give you access to the complete manual. </p>
