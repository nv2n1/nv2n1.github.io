---
title: "debconf-gettextize(1)"
name: "debconf-gettextize"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-gettextize/"
description: "debconf-gettextize – extract translations of debconf templates into PO files"
---

<h2 class="name">NAME</h2>
<p> debconf-gettextize &#8211; extract translations of debconf templates into PO files </p>
<h2>SYNOPSIS</h2>
<p> <code>debconf-gettextize</code> [<code>-v</code>] [<code>-h</code>] [<code>&#8211;podir=</code><font SIZE="-1">DIR</font>] [<code>&#8211;choices</code>] [<code>&#8211;merge</code>] <i>master</i> [<i>master</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>/var/lib/dpkg/info/*.templates</i> files read by debconf contain English text and translations in the same file. But in source packages, translations are managed in separate files to help translators. In the initial implementation, a master <i>templates</i> file contained only English text, and <i>templates.xx</i> files contained both original and translated strings for the language <i>xx</i>. The <code>debconf-mergetemplate</code> program was merging master and translated templates files. </p>
<p> The new implementation with <tt>&quot;po-debconf&quot;</tt> is based on <tt>&quot;gettext&quot;</tt>. Maintainers mark translatable fields by prepending them with an underscore, English strings are automatically extracted into a <font SIZE="-1">POT</font> file, translators work on normal <font SIZE="-1">PO</font> files, and <code>po2debconf</code> generates a merged templates file with the same structure. </p>
<p> The <code>debconf-gettextize</code> program was initially designed to help migrating to the new implementation.</p>
<dl>
<dt>&bull;</p>
<dd> It reads a list of master files and their associated translations, and generates <i>po/*.po</i> files for each language containing translated strings.</p>
<dt>&bull;</p>
<dd> Each input file receives an <tt>&quot;.old&quot;</tt> suffix, and a new master file overwrites the old one; it is identical to the previous master file except that an underscore is prepended to translatable fields. Developers can then choose which fields translators have to work on and which ones are skipped because their values are not locale-dependent.</p>
<dt>&bull;</p>
<dd> A <i>po/POTFILES.in</i> file is also created, it contains the list of <i>templates</i> files <code>debconf-updatepo</code> has to process.</dl>
<p> Typically the <code>debconf-gettextize</code> program must be run only once when transforming from the first implementation to the <tt>&quot;po-debconf&quot;</tt> format, but it can also be used afterwards to transform a <tt>&quot;_Choices&quot;</tt> field into <tt>&quot;__Choices&quot;</tt> (or vice-versa) without losing translations, when using the <tt>&quot;--merge&quot;</tt> flag (alongside with <tt>&quot;--choices&quot;</tt> or not). The desired template containing the <tt>&quot;_Choices&quot;</tt> or <tt>&quot;__Choices&quot;</tt> fields to modify has to be copied into a temporary template file, which is passed to <code>debconf-gettextize</code> as an argument. Then the following steps are performed:</p>
<dl>
<dt>1.</p>
<dd> <code>po2debconf</code> is run on this template file to generate a translated templates file.</p>
<dt>2.</p>
<dd> This translated templates file is processed as described above and <font SIZE="-1">PO</font> files are generated.</p>
<dt>3.</p>
<dd> Newly created <font SIZE="-1">PO</font> files are merged with existing ones.</dl>
<p> When <font SIZE="-1">PO</font> files are merged, <tt>&quot;_Choices&quot;</tt> fields have to be replaced by <tt>&quot;__Choices&quot;</tt> (or vice-versa) in the original templates file before running <code>debconf-updatepo</code>, otherwise new translations will be fuzzy.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a usage summary for the program and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Process in verbose mode.</p>
<dt><code>&#8211;podir=</code><font SIZE="-1">DIR</font></p>
<dd> Set directory for <font SIZE="-1">PO</font> files. Default is to search for <font SIZE="-1">PO</font> files in the <i>po</i> subdirectory below the location of the first master file.</p>
<dt><code>&#8211;choices</code></p>
<dd> By default, <code>debconf-gettextize</code> replaces <tt>&quot;Choices&quot;</tt> fields by <tt>&quot;_Choices&quot;</tt>. With this flag, <tt>&quot;__Choices&quot;</tt> fields are written instead.</p>
<dt><code>&#8211;merge</code></p>
<dd> When this flag is set, the strings are merged with existing <font SIZE="-1">PO</font> files. The templates files and <i>po/POTFILES.in</i> are not modified.</dl>
<h2>CAVEATS</h2>
<p> The <tt>&quot;Default&quot;</tt> field is special when template type is <tt>&quot;Select&quot;</tt> or <tt>&quot;Multiselect&quot;</tt>, because a value has to be chosen amongst the <code>English</code> list of choices, even for localized values. Normally this field must not be changed, but in rare circumstances localized values are meaningful (e.g. to choose the default language of an application). In order to let translators know that this localized <tt>&quot;Default&quot;</tt> field is special, you must by convention call it <tt>&quot;_DefaultChoice&quot;</tt> instead of <tt>&quot;_Default&quot;</tt>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debconf-updatepo/">debconf-updatepo</a></code>(1), <code><a href="/docs/linux/man/1-po2debconf/">po2debconf</a></code>(1), <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7), <code><a href="/docs/linux/man/7-po-debconf/">po-debconf</a></code>(7).</p>
<h2>AUTHORS</h2>
<pre><code>
Denis Barbier&lt;barbier[at] linuxfr.org&gt;
    Martin Quinson&lt;martin.quinson[at] ens - lyon.fr&gt;
</code></pre>
<h2>Index</h2>
