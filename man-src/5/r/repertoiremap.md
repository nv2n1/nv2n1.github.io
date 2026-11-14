---
title: "repertoiremap(5)"
name: "repertoiremap"
section: "5"
letter: "r"
url: "/docs/linux/man/5-repertoiremap/"
description: "repertoiremap – map symbolic character names to Unicode code points"
---

<p>repertoiremap &#8211; map symbolic character names to Unicode code points</p>
<h2>Description</h2>
<p>A repertoire map defines mappings between symbolic character names (mnemonics) and Unicode code points when compiling a locale with <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1). Using a repertoire map is optional, it is needed only when symbolic names are used instead of now preferred Unicode code points.</p>
<h3>Syntax</h3>
<p>The repertoiremap file starts with a header that may consist of the following keywords:</p>
<dl>
<dt><i>comment_char</i></p>
<dd>is followed by a character that will be used as the comment character for the rest of the file. It defaults to the number sign (#).</p>
<dt><i>escape_char</i></p>
<dd>is followed by a character that should be used as the escape character for the rest of the file to mark characters that should be interpreted in a special way. It defaults to the backslash (\).</dl>
<p> The mapping section starts with the keyword <i>CHARIDS</i> in the first column. </p>
<p> The mapping lines have the following form:</p>
<dl>
<dt><i>&lt;symbolic-name&gt; &lt;code-point&gt; comment</i></p>
<dd>This defines exactly one mapping, <i>comment</i> being optional.</dl>
<p> The mapping section ends with the string <i>END CHARIDS</i>.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/i18n/repertoiremaps</i></p>
<dd>Usual default repertoire map path.</dl>
<h2>Conforming To</h2>
<p>POSIX.2.</p>
<h2>Notes</h2>
<p>Repertoire maps are deprecated in favor of Unicode code points.</p>
<h2>Examples</h2>
<p>A mnemonic for the Euro sign can be defined as follows: </p>
<pre>&lt;Eu&gt; &lt;U20AC&gt; EURO SIGN</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/5-charmap/">charmap</a></code>(5), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
