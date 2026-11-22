---

title: "install-info(1)"
name: "install-info"
section: "1"
letter: "i"
url: "/docs/linux/man/1-install-info/"
description: "install-info – update info/dir entries"
---

<p> install-info &#8211; update info/dir entries </p>
<h2>SYNOPSIS</h2>
<p> <code>install-info</code> [<i>,OPTION/</i>]&#8230; [<i>,INFO-FILE /</i>[<i>,DIR-FILE/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Add or remove entries in INFO-FILE from the Info directory DIR-FILE. INFO-FILE and DIR-FILE are required unless the <code>&#8211;info-file</code> or <code>&#8211;dir-file</code> (or <code>&#8211;info-dir</code>) options are given, respectively.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;add-once</code></dt>
<dd> add only to first matching section, not all.</dd>
<dt><code>&#8211;align</code>=<i>,COL/</i></dt>
<dd> start description of new entries at column COL.</dd>
<dt><code>&#8211;calign</code>=<i>,COL/</i></dt>
<dd> format second and subsequent description lines to start at column COL.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> report what is being done.</dd>
<dt><code>&#8211;delete</code></dt>
<dd> delete existing entries for INFO-FILE from DIR-FILE; don&#8217;t insert any new entries.</dd>
<dt><code>&#8211;defsection</code>=<i>,TEXT/</i></dt>
<dd> like <code>&#8211;section</code>, but only use TEXT if no sections are present in INFO-FILE (replacing &quot;Miscellaneous&quot;).</dd>
<dt><code>&#8211;description</code>=<i>,TEXT/</i></dt>
<dd> the description of the entry is TEXT; used with the <code>&#8211;name</code> option to become synonymous with the <code>&#8211;entry</code> option.</dd>
<dt><code>&#8211;dir-file</code>=<i>,NAME/</i></dt>
<dd> specify file name of Info directory file; equivalent to using the DIR-FILE argument.</dd>
<dt><code>&#8211;dry-run</code></dt>
<dd> same as <code>&#8211;test</code>.</dd>
<dt><code>&#8211;entry</code>=<i>,TEXT/</i></dt>
<dd> insert TEXT as an Info directory entry, overriding any corresponding entry from DIR-FILE. TEXT is written as an Info menu item line followed</dd>
<dt>by zero or more extra lines starting with whitespace.</dt>
<dd> If you specify more than one entry, all are added. If you don&#8217;t specify any entries, they are determined</dd>
<dt>
</dt><dd> from information in the Info file itself.</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit.</dd>
<dt><code>&#8211;info-dir</code>=<i>,DIR/</i></dt>
<dd> same as <code>&#8211;dir-file</code>=<i>,DIR/</i>/dir.</dd>
<dt><code>&#8211;info-file</code>=<i>,FILE/</i></dt>
<dd> specify Info file to install in the directory; equivalent to using the INFO-FILE argument.</dd>
<dt><code>&#8211;item</code>=<i>,TEXT/</i></dt>
<dd> same as <code>&#8211;entry</code>=<i>,TEXT/</i>.</dd>
<dt><code>&#8211;keep-old</code></dt>
<dd> do not replace entries, or remove empty sections.</dd>
<dt><code>&#8211;maxwidth</code>, <code>&#8211;max-width</code>=<i>,COL/</i></dt>
<dd> wrap description at column COL.</dd>
<dt><code>&#8211;menuentry</code>=<i>,TEXT/</i></dt>
<dd> same as <code>&#8211;name</code>=<i>,TEXT/</i>.</dd>
<dt><code>&#8211;name</code>=<i>,TEXT/</i></dt>
<dd> the name of the entry is TEXT; used with <code>&#8211;description</code> to become synonymous with the <code>&#8211;entry</code> option.</dd>
<dt><code>&#8211;no-indent</code></dt>
<dd> do not format new entries in the DIR file.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> suppress warnings.</dd>
<dt><code>&#8211;regex</code>=<i>,R/</i></dt>
<dd> put this file&#8217;s entries in all sections that match the regular expression R (ignoring case).</dd>
<dt><code>&#8211;remove</code></dt>
<dd> same as <code>&#8211;delete</code>.</dd>
<dt><code>&#8211;remove-exactly</code></dt>
<dd> only remove if the info file name matches exactly; suffixes such as .info and .gz are not ignored.</dd>
<dt><code>&#8211;section</code>=<i>,SEC/</i></dt>
<dd> put entries in section SEC of the directory. If you specify more than one section, all the entries</dd>
<dt>are added in each of the sections.</dt>
<dd> If you don&#8217;t specify any sections, they are determined</dd>
<dt>from information in the Info file itself;</dt>
<dd> if nothing is available there, the <code>&#8211;defsection</code> value is used; if that is not specified, the final default is &quot;Miscellaneous&quot;.</dd>
<dt><code>&#8211;section</code> R SEC</dt>
<dd> equivalent to <code>&#8211;regex</code>=<i>,R/</i> <code>&#8211;section</code>=<i>,SEC/</i> <code>&#8211;add-once</code>.</dd>
<dt><code>&#8211;silent</code></dt>
<dd> suppress warnings.</dd>
<dt><code>&#8211;test</code></dt>
<dd> suppress updating of DIR-FILE.</dd>
<dt><code>&#8211;version</code></dt>
<dd> display version information and exit.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Email bug reports to bug-texinfo [at] gnu.org, general questions and discussion to help-texinfo [at] gnu.org.<br/>
 Texinfo home page: <a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>install-info</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>install-info</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info install-info</code></dd></dl>
<p> should give you access to the complete manual. </p>
