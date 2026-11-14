---
title: "locale-gen(8)"
name: "locale-gen"
section: "8"
letter: "l"
url: "/docs/linux/man/8-locale-gen/"
description: "locale-gen — generates localisation files from templates"
---

<p>locale-gen &#8212; generates localisation files from templates</p>
<h2>Synopsis</h2>
<p><code>locale-gen</code></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>locale-gen</code> command. </p>
<p> By default, the locale package which provides the base support for localisation of libc-based programs does not contain usable localisation files for every supported language. This limitation has became necessary because of the substantial size of such files and the large number of languages supported by libc. As a result, Debian uses a special mechanism where we prepare the actual localisation files on the target host and distribute only the templates for them. </p>
<p> <code>locale-gen</code> is a program that reads the file <code>/etc/locale.gen</code> and invokes <code>localedef</code> for the chosen localisation profiles. Run <code>locale-gen</code> after you have modified the <code>/etc/locale.gen</code> file.<br />
&nbsp;<br />
&nbsp;</p>
<h2>Files</h2>
<p><code>/etc/locale.gen</code> </p>
<p> The main configuration file, which has a simple format: every line that is not empty and does not begin with a # is treated as a locale definition that is to be built.<br />
&nbsp; <code>/var/lib/locales/supported.d/</code> </p>
<p> A directory containing locale.gen snippets provided by language-pack packages. Do not edit these manually, they will be overwritten on package upgrades.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-localedef/">localedef</a>(1), <a href="/docs/linux/man/1-locale/">locale</a>(1), <a href="/docs/linux/man/5-locale-gen/">locale.gen</a>(5).</p>
<h2>Author</h2>
<p>This manual page was written by Eduard Bloch &lt;blade [at] debian.org&gt; for the <code>Debian GNU/Linux</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
