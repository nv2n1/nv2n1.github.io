---
title: "ne_i18n_init(3)"
name: "ne_i18n_init"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_i18n_init/"
description: "ne_i18n_init – functions to initialize internationalization support"
---

<p>ne_i18n_init &#8211; functions to initialize internationalization support</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_i18n.h&gt;

void ne_i18n_init(const char *encoding);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_i18n_init</code> function can be used to enable support for translated messages in the neon library. The <i>encoding</i> parameter, if non-NULL, specifies the character encoding required for generated translated string. If it is NULL, the appropriate character encoding for the process locale will be used. </p>
<p> This call is only strictly necessary if either: </p>
<dl>
<dd>1. neon has been installed into a different prefix than the gettext implementation on which it depends for i18n purposes, or</dl>
<dl>
<dd>2. the caller requires that translated messages are in a particular character encoding.</dl>
<p> If <code>ne_i18n_init</code> is never called, the message catalogs will not be found if case (a) applies (and so English error messages will be used), and will use the default character encoding specified by the process locale. The library will otherwise operate correctly. </p>
<p> Note that the encoding used is a process-global setting and so results may be unexpected if other users of neon within the process call <code>ne_i18n_init</code> with a different encoding parameter.</p>
<h2>See Also</h2>
<p>ne_sock_init</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
