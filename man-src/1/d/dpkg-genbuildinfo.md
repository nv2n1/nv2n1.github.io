---

title: "dpkg-genbuildinfo(1)"
name: "dpkg-genbuildinfo"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-genbuildinfo/"
description: "dpkg-genbuildinfo – generate Debian .buildinfo files"
---

<p> dpkg-genbuildinfo &#8211; generate Debian .buildinfo files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-genbuildinfo</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-genbuildinfo</code> reads information from an unpacked and built Debian source tree and from the files it has generated and generates a Debian control file describing the build environment and the build artifacts (<code>.buildinfo</code> file). </p>
<p> This command was introduced in dpkg 1.18.11.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;build=</code><i>type</i></dt>
<dd> Specifies the build <i>type</i> from a comma-separated list of components. </dd>
<p> The allowed values are:</p>
<dl>
<dl>
<dt><code>any</code></dt>
<dd> Generate build information including unqualified build dependencies (<code>Build-Depends</code>) and architecture specific build dependencies (<code>Build-Depends-Arch</code>).</dd>
<dt><code>all</code></dt>
<dd> Generate build information including unqualified build dependencies (<code>Build-Depends</code>) and architecture independent build dependencies (<code>Build-Depends-Indep</code>).</dd>
<dt><code>source</code></dt>
<dd> Effectively ignored; generate build information with just the unqualified build dependencies (<code>Build-Depends</code>).</dd>
<dt><code>binary</code></dt>
<dd> Generate build information with all three types of build dependencies. This is an alias for <code>any,all</code>.</dd>
<dt><code>full</code></dt>
<dd> Generate build information with all three types of build dependencies. This is an alias for <code>any,all,source</code>, and the same as the default case when no build option is specified.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-c</code><i>controlfile</i></dt>
<dd> Specifies the main source control file to read information from. The default is <code>debian/control</code>.</dd>
<dt><code>-l</code><i>changelog-file</i></dt>
<dd> Specifies the changelog file to read information from. The default is <code>debian/changelog</code>.</dd>
<dt><code>-f</code><i>files-list-file</i></dt>
<dd> Specifies where is the list of files that have been produced by the build, rather than using <code>debian/files</code>.</dd>
<dt><code>-F</code><i>changelog-format</i></dt>
<dd> Specifies the format of the changelog. See <code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1) for information about alternative formats.</dd>
<dt><code>-O</code>[<i>filename</i>]</dt>
<dd> Print the buildinfo file to standard output (or <i>filename</i> if specified) rather than to <i>dir</i><code>/</code><i>source-name</i><code>_</code><i>binary-version</i><code>_</code><i>arch</i><code>.buildinfo</code> (where <i>dir</i> is <code>..</code> by default or <i>upload-files-dir</i> if <code>-u</code> was used).</dd>
<dt><code>-u</code><i>upload-files-dir</i></dt>
<dd> Look for the files to be uploaded in <i>upload-files-dir</i> rather than <code>..</code> (<code>dpkg-genbuildinfo</code> needs to find these files so that it can include their sizes and checksums in the <code>.buildinfo</code> file).</dd>
<dt><code>&#8211;always-include-kernel</code></dt>
<dd> By default, the <code>Build-Kernel-Version</code> field will not be written out. </dd>
<p> Specify this option (since dpkg 1.19.0) to always write a <code>Build-Kernel-Version</code> field when generating the <code>.buildinfo</code>.</p>
<dt><code>&#8211;always-include-path</code></dt>
<dd> By default, the <code>Build-Path</code> field will only be written if the current directory starts with an allowed pattern. </dd>
<p> On Debian and derivatives the pattern matches on <code>/build/</code> at the start of the pathname. </p>
<p> Specify this option to always write a <code>Build-Path</code> field when generating the <code>.buildinfo</code>.</p>
<dt><code>&#8211;admindir=</code><i>dir</i></dt>
<dd> Change the location of the <code>dpkg</code> database. The default location is <i>/var/lib/dpkg</i>.</dd>
<dt><code>-q</code></dt>
<dd> <code>dpkg-genbuildinfo</code> might produce informative messages on standard error. <code>-q</code> suppresses these messages.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Show the usage message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font></dt>
<dd> This variable can be used to enable or disable various features that affect the information included in the .buildinfo file, via the <code>buildinfo</code> option (since dpkg 1.18.19). This option contains a comma-separated list of features, prefixed with the &#8216;<code>+</code>&#8216; or &#8216;<code>&#8211;</code>&#8216; modifiers, to denote whether to enable or disable them. The special feature &#8220;<code>all</code>&#8221; can be used to enable or disable all other features. The feature &#8220;<code>path</code>&#8221; controls whether to unconditionally include the <code>Build-Path</code> field.</dd>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></dt>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dd>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></dt>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>debian/files</code></dt>
<dd> The list of generated files. <code>dpkg-genbuildinfo</code> reads the data here when producing a <code>.buildinfo</code> file.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-buildinfo/">deb-buildinfo</a></code>(5). </p>
