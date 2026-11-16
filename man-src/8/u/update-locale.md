---
title: "update-locale(8)"
name: "update-locale"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-locale/"
description: "update-locale – Modify global locale settings"
---

<p>update-locale &#8211; Modify global locale settings</p>
<h2>Syntax</h2>
<p>update-locale [<i>OPTIONS</i>] [<i>var</i>=<i>locale</i> | <i>var</i>] [&#8230;]</p>
<h2>Description</h2>
<p>This program can be called by maintainer scripts when Debian packages are installed or removed, it updates the <code>/etc/default/locale</code> file to reflect changes in system configuration related to global locale settings. When variables have no value assigned, they are removed from the locale file. Some basic checks are performed to ensure that requested settings are valid.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>Display an help message and exit.</dd>
<dt><code>&#8211;reset</code></dt>
<dd>Variables which are not set on command-line are cleared out.</dd>
<dt><code>&#8211;locale-file</code><i> FILE</i></dt>
<dd>Define file containing locale variables. (Default: <code>/etc/default/locale</code>)</dd>
<dt><code>&#8211;no-checks</code></dt>
<dd>Do not perform sanity checks on locale variables.</dd></dl>
<h2>Example</h2>
<pre>The command
<code> update-locale LANG=en_CA.UTF-8 LANGUAGE
</code>sets <code>LANG</code> to <code>en_CA.UTF-8</code> and removes definitions for <code>LANGUAGE</code>.</pre>
<h2>Files</h2>
<dl>
<dt><code>/etc/default/locale</code></dt>
<dd>File where global locale settings are stored.</dd></dl>
<h2>Author</h2>
<p>Denis Barbier &lt;barbier [at] linuxfr.org&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-locale-gen/">locale-gen</a>(8), <a href="/docs/linux/man/1-locale/">locale</a>(1) </p>
