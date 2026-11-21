---
title: "dpkg-genchanges(1)"
name: "dpkg-genchanges"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-genchanges/"
description: "dpkg-genchanges – generate Debian .changes files"
---

<h2 class="name">NAME</h2>
<p> dpkg-genchanges &#8211; generate Debian .changes files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-genchanges</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-genchanges</code> reads information from an unpacked and built Debian source tree and from the files it has generated and generates a Debian upload control file (<code>.changes</code> file).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;build=</code><i>type</i></dt>
<dd> Specifies the build <i>type</i> from a comma-separated list of components (since dpkg 1.18.5). </dd>
<p> The allowed values are:</p>
<dl>
<dl>
<dt><code>source</code></dt>
<dd> Upload the source package.</dd>
<dt><code>any</code></dt>
<dd> Upload the architecture specific binary packages.</dd>
<dt><code>all</code></dt>
<dd> Upload the architecture independent binary packages.</dd>
<dt><code>binary</code></dt>
<dd> Upload the architecture specific and independent binary packages. This is an alias for <code>any,all</code>.</dd>
<dt><code>full</code></dt>
<dd> Upload everything. This is alias for <code>source,any,all</code>, and the same as the default case when no build option is specified.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-g</code></dt>
<dd> Equivalent to <code>&#8211;build=source,all</code> (since dpkg 1.17.11).</dd>
<dt><code>-G</code></dt>
<dd> Equivalent to <code>&#8211;build=source,any</code> (since dpkg 1.17.11).</dd>
<dt><code>-b</code></dt>
<dd> Equivalent to <code>&#8211;build=binary</code> or <code>&#8211;build=any,all</code>.</dd>
<dt><code>-B</code></dt>
<dd> Equivalent to <code>&#8211;build=any</code>.</dd>
<dt><code>-A</code></dt>
<dd> Equivalent to <code>&#8211;build=all</code>.</dd>
<dt><code>-S</code></dt>
<dd> Equivalent to <code>&#8211;build=source</code>.</dd></dl>
<p> The <code>-s</code><i>x</i> options control whether the original source archive is included in the upload if any source is being generated (i.e. <code>-b</code> or <code>-B</code> haven&#8217;t been used).</p>
<dl>
<dt><code>-si</code></dt>
<dd> By default, or if specified, the original source will be included only if the upstream version number (the version without epoch and without Debian revision) differs from the upstream version number of the previous changelog entry.</dd>
<dt><code>-sa</code></dt>
<dd> Forces the inclusion of the original source.</dd>
<dt><code>-sd</code></dt>
<dd> Forces the exclusion of the original source and includes only the diff.</dd>
<dt><code>-v</code><i>version</i></dt>
<dd> Causes changelog information from all versions strictly later than <i>version</i> to be used.</dd>
<dt><code>-C</code><i>changes-description</i></dt>
<dd> Read the description of the changes from the file <i>changes-description</i> rather than using the information from the source tree&#8217;s changelog file.</dd>
<dt><code>-m</code><i>maintainer-address</i></dt>
<dd> Use <i>maintainer-address</i> as the name and email address of the maintainer for this package, rather than using the information from the source tree&#8217;s control file.</dd>
<dt><code>-e</code><i>maintainer-address</i></dt>
<dd> Use <i>maintainer-address</i> as the name and email address of the maintainer for this upload, rather than using the information from the source tree&#8217;s changelog.</dd>
<dt><code>-V</code><i>name</i><code>=</code><i>value</i></dt>
<dd> Set an output substitution variable. See <code><a href="/docs/linux/man/5-deb-substvars/">deb-substvars</a></code>(5) for a discussion of output substitution.</dd>
<dt><code>-T</code><i>substvars-file</i></dt>
<dd> Read substitution variables in <i>substvars-file</i>; the default is <code>debian/substvars</code>. No variable substitution is done on any of the fields that are output, except for the contents extracted from each binary package <code>Description</code> field (since dpkg 1.19.0), however the special variable <i>Format</i> will override the field of the same name. This option can be used multiple times to read substitution variables from multiple files (since dpkg 1.15.6).</dd>
<dt><code>-D</code><i>field</i><code>=</code><i>value</i></dt>
<dd> Override or add an output control file field.</dd>
<dt><code>-U</code><i>field</i></dt>
<dd> Remove an output control file field.</dd>
<dt><code>-c</code><i>controlfile</i></dt>
<dd> Specifies the main source control file to read information from. The default is <code>debian/control</code>.</dd>
<dt><code>-l</code><i>changelog-file</i></dt>
<dd> Specifies the changelog file to read information from. The default is <code>debian/changelog</code>.</dd>
<dt><code>-f</code><i>files-list-file</i></dt>
<dd> Read the list of files to be uploaded here, rather than using <code>debian/files</code>.</dd>
<dt><code>-F</code><i>changelog-format</i></dt>
<dd> Specifies the format of the changelog. See <code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1) for information about alternative formats.</dd>
<dt><code>-u</code><i>upload-files-dir</i></dt>
<dd> Look for the files to be uploaded in <i>upload-files-dir</i> rather than <code>..</code> (<code>dpkg-genchanges</code> needs to find these files so that it can include their sizes and checksums in the <code>.changes</code> file).</dd>
<dt><code>-q</code></dt>
<dd> Usually <code>dpkg-genchanges</code> will produce informative messages on standard error, for example about how many of the package&#8217;s source files are being uploaded. <code>-q</code> suppresses these messages.</dd>
<dt><code>-O</code>[<i>filename</i>]</dt>
<dd> Print the changes file to standard output (the default) or to <i>filename</i> if specified (since dpkg 1.18.5).</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Show the usage message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></dt>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dd>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></dt>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>debian/files</code></dt>
<dd> The list of generated files which are part of the upload being prepared. <code>dpkg-genchanges</code> reads the data here when producing a <code>.changes</code> file.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-substvars/">deb-substvars</a></code>(5), <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5), <code><a href="/docs/linux/man/5-deb-src-files/">deb-src-files</a></code>(5), <code><a href="/docs/linux/man/5-deb-changelog/">deb-changelog</a></code>(5), <code><a href="/docs/linux/man/5-deb-changes/">deb-changes</a></code>(5). </p>
