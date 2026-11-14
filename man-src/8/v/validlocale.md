---
title: "validlocale(8)"
name: "validlocale"
section: "8"
letter: "v"
url: "/docs/linux/man/8-validlocale/"
description: "validlocale – Test if a given locale is available"
---

<p>validlocale &#8211; Test if a given locale is available</p>
<h2>Syntax</h2>
<p>validlocale &lt;<i>locale</i>&gt;</p>
<h2>Description</h2>
<p>Test if the locale given as argument is a valid locale. If it isn&#8217;t, print on stdout the string to add to /etc/locale.gen to make locale-gen generate the locale (if it exists at all).</p>
<h2>Files</h2>
<p><i>/usr/sbin/validlocale</i><br />
 <i>/usr/share/i18n/SUPPORTED</i></p>
<h2>Environment Variables</h2>
<dl>
<dt><code>DEFAULTCHARSET</code></p>
<dd>Which charset to assume if the given locale is missing from the list of supported locales.</dl>
<h2>Examples</h2>
<p>If you give a valid locale as parameter, it outputs a string specifying this on stderr: </p>
<dl>
<dd>% validlocale C<br />
 locale &#8216;C&#8217; valid and available</dl>
<p> When given a invalid (not generated or just nonexistent), it outputs a string on stderr telling that this is an invalid locale, and a string to stdout with the string to add to /etc/locale.gen to have this locale generated: </p>
<dl>
<dd>% validlocale de_AU [at] euro<br />
 locale &#8216;de_AU [at] euro&#8217; not available<br />
 de_AU [at] euro ISO-8859-15</dl>
<h2>Authors</h2>
<p>Petter Reinholdtsen &lt;pere [at] hungry.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-locale-gen/">locale-gen</a>(8), <a href="/docs/linux/man/1-localedef/">localedef</a>(1), <a href="/docs/linux/man/1-locale/">locale</a>(1) </p>
