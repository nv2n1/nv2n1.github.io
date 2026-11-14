---
title: "install-info(1)"
name: "install-info"
section: "1"
letter: "i"
url: "/docs/linux/man/1-install-info/"
description: "install-info – update info/dir entries"
---

<h2 class="name">NAME</h2>
<p> install-info &#8211; update info/dir entries </p>
<h2>SYNOPSIS</h2>
<p> <code>install-info</code> [<i>,OPTION/</i>]&#8230; [<i>,INFO-FILE /</i>[<i>,DIR-FILE/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Add or remove entries in INFO-FILE from the Info directory DIR-FILE. INFO-FILE and DIR-FILE are required unless the <code>&#8211;info-file</code> or <code>&#8211;dir-file</code> (or <code>&#8211;info-dir</code>) options are given, respectively.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;add-once</code></p>
<dd> add only to first matching section, not all.</p>
<dt><code>&#8211;align</code>=<i>,COL/</i></p>
<dd> start description of new entries at column COL.</p>
<dt><code>&#8211;calign</code>=<i>,COL/</i></p>
<dd> format second and subsequent description lines to start at column COL.</p>
<dt><code>&#8211;debug</code></p>
<dd> report what is being done.</p>
<dt><code>&#8211;delete</code></p>
<dd> delete existing entries for INFO-FILE from DIR-FILE; don&#8217;t insert any new entries.</p>
<dt><code>&#8211;defsection</code>=<i>,TEXT/</i></p>
<dd> like <code>&#8211;section</code>, but only use TEXT if no sections are present in INFO-FILE (replacing &quot;Miscellaneous&quot;).</p>
<dt><code>&#8211;description</code>=<i>,TEXT/</i></p>
<dd> the description of the entry is TEXT; used with the <code>&#8211;name</code> option to become synonymous with the <code>&#8211;entry</code> option.</p>
<dt><code>&#8211;dir-file</code>=<i>,NAME/</i></p>
<dd> specify file name of Info directory file; equivalent to using the DIR-FILE argument.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> same as <code>&#8211;test</code>.</p>
<dt><code>&#8211;entry</code>=<i>,TEXT/</i></p>
<dd> insert TEXT as an Info directory entry, overriding any corresponding entry from DIR-FILE. TEXT is written as an Info menu item line followed</p>
<dt>by zero or more extra lines starting with whitespace.</p>
<dd> If you specify more than one entry, all are added. If you don&#8217;t specify any entries, they are determined</p>
<dt>
<dd> from information in the Info file itself.</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit.</p>
<dt><code>&#8211;info-dir</code>=<i>,DIR/</i></p>
<dd> same as <code>&#8211;dir-file</code>=<i>,DIR/</i>/dir.</p>
<dt><code>&#8211;info-file</code>=<i>,FILE/</i></p>
<dd> specify Info file to install in the directory; equivalent to using the INFO-FILE argument.</p>
<dt><code>&#8211;item</code>=<i>,TEXT/</i></p>
<dd> same as <code>&#8211;entry</code>=<i>,TEXT/</i>.</p>
<dt><code>&#8211;keep-old</code></p>
<dd> do not replace entries, or remove empty sections.</p>
<dt><code>&#8211;maxwidth</code>, <code>&#8211;max-width</code>=<i>,COL/</i></p>
<dd> wrap description at column COL.</p>
<dt><code>&#8211;menuentry</code>=<i>,TEXT/</i></p>
<dd> same as <code>&#8211;name</code>=<i>,TEXT/</i>.</p>
<dt><code>&#8211;name</code>=<i>,TEXT/</i></p>
<dd> the name of the entry is TEXT; used with <code>&#8211;description</code> to become synonymous with the <code>&#8211;entry</code> option.</p>
<dt><code>&#8211;no-indent</code></p>
<dd> do not format new entries in the DIR file.</p>
<dt><code>&#8211;quiet</code></p>
<dd> suppress warnings.</p>
<dt><code>&#8211;regex</code>=<i>,R/</i></p>
<dd> put this file&#8217;s entries in all sections that match the regular expression R (ignoring case).</p>
<dt><code>&#8211;remove</code></p>
<dd> same as <code>&#8211;delete</code>.</p>
<dt><code>&#8211;remove-exactly</code></p>
<dd> only remove if the info file name matches exactly; suffixes such as .info and .gz are not ignored.</p>
<dt><code>&#8211;section</code>=<i>,SEC/</i></p>
<dd> put entries in section SEC of the directory. If you specify more than one section, all the entries</p>
<dt>are added in each of the sections.</p>
<dd> If you don&#8217;t specify any sections, they are determined</p>
<dt>from information in the Info file itself;</p>
<dd> if nothing is available there, the <code>&#8211;defsection</code> value is used; if that is not specified, the final default is &quot;Miscellaneous&quot;.</p>
<dt><code>&#8211;section</code> R SEC</p>
<dd> equivalent to <code>&#8211;regex</code>=<i>,R/</i> <code>&#8211;section</code>=<i>,SEC/</i> <code>&#8211;add-once</code>.</p>
<dt><code>&#8211;silent</code></p>
<dd> suppress warnings.</p>
<dt><code>&#8211;test</code></p>
<dd> suppress updating of DIR-FILE.</p>
<dt><code>&#8211;version</code></p>
<dd> display version information and exit.</dl>
<h2>REPORTING BUGS</h2>
<p> Email bug reports to bug-texinfo [at] gnu.org, general questions and discussion to help-texinfo [at] gnu.org.<br />
 Texinfo home page: <a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>install-info</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>install-info</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info install-info</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
