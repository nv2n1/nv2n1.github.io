---
title: "wcstok(3)"
name: "wcstok"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcstok/"
description: "wcstok – split wide-character string into tokens"
---

<p>wcstok &#8211; split wide-character string into tokens</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcstok(wchar_t *wcs, const wchar_t *delim, wchar_t **ptr);</code></pre>
<h2>Description</h2>
<p>The <code>wcstok</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3) function, with an added argument to make it multithread-safe. It can be used to split a wide-character string <i>wcs</i> into tokens, where a token is defined as a substring not containing any wide-characters from <i>delim</i>. </p>
<p> The search starts at <i>wcs</i>, if <i>wcs</i> is not NULL, or at <i>*ptr</i>, if <i>wcs</i> is NULL. First, any delimiter wide-characters are skipped, that is, the pointer is advanced beyond any wide-characters which occur in <i>delim</i>. If the end of the wide-character string is now reached, <code>wcstok</code>() returns NULL, to indicate that no tokens were found, and stores an appropriate value in <i>*ptr</i>, so that subsequent calls to <code>wcstok</code>() will continue to return NULL. Otherwise, the <code>wcstok</code>() function recognizes the beginning of a token and returns a pointer to it, but before doing that, it zero-terminates the token by replacing the next wide-character which occurs in <i>delim</i> with a null wide character (L&#8217;
