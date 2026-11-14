---
title: "deb-buildinfo(5)"
name: "deb-buildinfo"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-buildinfo/"
description: "deb-buildinfo – Debian build information file format"
---

<p>deb-buildinfo &#8211; Debian build information file format</p>
<h2>Synopsis</h2>
<p><i>filename</i><code>.buildinfo</code></p>
<h2>Description</h2>
<p>Each Debian source package build can record the build information in a <code>.buildinfo</code> control file, which contains a number of fields in <code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5) format. </p>
<p> Each field begins with a tag, such as <code>Source</code> or <code>Binary</code> (case insensitive), followed by a colon, and the body of the field (case sensitive unless stated otherwise). Fields are delimited only by field tags. In other words, field text may be multiple lines in length, but the installation tools will generally join lines when processing the body of the field (except in case of the multiline fields <code>Binary-Only-Changes</code>, <code>Installed-Build-Depends</code>, <code>Environment</code>, <code>Checksums-Md5</code>, <code>Checksums-Sha1</code> and <code>Checksums-Sha256</code>, see below). </p>
<p> The control data might be enclosed in an OpenPGP <font SIZE="-1">ASCII</font> Armored signature, as specified in <font SIZE="-1">RFC4880.</font> </p>
<p> The name of the <code>.buildinfo</code> file will depend on the type of build and will be as specific as necessary but not more; for a build that includes <code>any</code> the name will be <i>source-name</i><code>_</code><i>binary-version</i><code>_</code><i>arch</i><code>.buildinfo</code>, or otherwise for a build that includes <code>all</code> the name will be <i>source-name</i><code>_</code><i>binary-version</i><code>_</code><code>all.buildinfo</code>, or otherwise for a build that includes <code>source</code> the name will be <i>source-name</i><code>_</code><i>source-version</i><code>_</code><code>source.buildinfo</code>.</p>
<h2>Fields</h2>
<dl>
<dt><code>Format:</code> <i>format-version</i> (required)</p>
<dd>The value of this field declares the format version of the file. The syntax of the field value is a version number with a major and minor component. Backward incompatible changes to the format will bump the major version, and backward compatible changes (such as field additions) will bump the minor version. The current format version is <code>1.0</code>.</p>
<dt><code>Source:</code> <i>source-name</i> [<code>(</code><i>source-version</i><code>)</code>] (required)</p>
<dd>The name of the source package. If the source version differs from the binary version, then the <i>source-name</i> will be followed by a <i>source-version</i> in parenthesis. This can happen when the build is for a binary-only non-maintainer upload.</p>
<dt><code>Binary:</code> <i>binary-package-list</i> (required in context)</p>
<dd>This folded field is a space-separated list of binary packages built. If the build is source-only, then the field is omitted (since dpkg 1.20.0).</p>
<dt><code>Architecture:</code> <i>arch-list</i> (required)</p>
<dd>This space-separated field lists the architectures of the files currently being built. Common architectures are <code>amd64</code>, <code>armel</code>, <code>i386</code>, etc. Note that the <code>all</code> value is meant for packages that are architecture independent. If the source for the package is also being built, the special entry <code>source</code> is also present. Architecture wildcards must never be present in the list.</p>
<dt><code>Version:</code> <i>version-string</i> (required)</p>
<dd>Typically, this is the original package&#8217;s version number in whatever form the program&#8217;s author uses. It may also include a Debian revision number (for non-native packages). The exact format and sorting algorithm are described in <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7).</p>
<dt><code>Binary-Only-Changes:</code></p>
<dd>
<dt> <i>changelog-entry</i></p>
<dd>This multiline field contains the concatenated text of the changelog entry for a binary-only non-maintainer upload (binNMU) if that is the case. To make this a valid multiline field empty lines are replaced with a single full stop (&#8216;.&#8217;) and all lines are indented by one space character. The exact content depends on the changelog format.</p>
<dt><code>Checksums-Md5:</code> (required)</p>
<dd>
<dt><code>Checksums-Sha1:</code> (required)</p>
<dd>
<dt><code>Checksums-Sha256:</code> (required)</p>
<dd>
<dt> <i>checksum</i> <i>size</i> <i>filename</i></p>
<dd>These multiline fields contain a list of files with a checksum and size for each one. These fields have the same syntax and differ only in the checksum algorithm used: <font SIZE="-1">MD5</font> for <code>Checksums-Md5</code>, <font SIZE="-1">SHA-1</font> for <code>Checksums-Sha1</code> and <font SIZE="-1">SHA-256</font> for <code>Checksums-Sha256</code>. </p>
<p> The first line of the field value (the part on the same line as the field name followed by a colon) is always empty. The content of the field is expressed as continuation lines, one line per file. Each line consists of space-separated entries describing the file: the checksum, the file size, and the file name. </p>
<p> These fields list all files that make up the build.</p>
<dt><code>Build-Origin:</code> <i>name</i></p>
<dd>The name of the distribution this package is originating from.</p>
<dt><code>Build-Architecture:</code> <i>arch</i> (required)</p>
<dd>The Debian architecture for the installation the packages is being built in. Common architectures are <code>amd64</code>, <code>armel</code>, <code>i386</code>, etc.</p>
<dt><code>Build-Date:</code> <i>build-date</i></p>
<dd>The date the package was built. It must be in the same format as the date in a <code><a href="/docs/linux/man/5-deb-changelog/">deb-changelog</a></code>(5) entry.</p>
<dt><code>Build-Kernel-Version:</code> <i>build-kernel-version</i></p>
<dd>The release and version (in an unspecified format) of the kernel running on the build system. This field is only going to be present if the builder has explicitly requested it, to avoid leaking possibly sensitive information.</p>
<dt><code>Build-Path:</code> <i>build-path</i></p>
<dd>The absolute build path, which correspond to the unpacked source tree. This field is only going to be present if the vendor has allowed it via some pattern match to avoid leaking possibly sensitive information. </p>
<p> On Debian and derivatives only build paths starting with <i>/build/</i> will emit this field.</p>
<dt><code>Build-Tainted-By:</code></p>
<dd>
<dt> <i>taint-reason-list</i></p>
<dd>This folded field contains a space-separated list of non-exhaustive reason tags (formed by alphanumeric and dash characters) which identify why the current build has been tainted (since dpkg 1.19.5). </p>
<p> On Debian and derivatives the following reason tags can be emitted:</p>
<dl>
<dd>
<dl>
<dt><code>merged-usr-via-aliased-dirs</code></p>
<dd>The system has a merged <i>/usr</i> via aliased directories (previously known as <code>merged-usr-via-symlinks</code>). This will confuse <code>dpkg-query</code>, <code>dpkg-statoverride</code>, <code>dpkg-trigger</code>, <code>update-alternatives</code> and any other tool using pathnames as keys into their databases, as it creates filesystem aliasing problems, and messes with the understanding of the filesystem that <code>dpkg</code> has recorded in its database. For build systems that hardcode pathnames to specific binaries or libraries on the resulting artifacts, it can also produce packages that will be incompatible with non-/usr-merged filesystems.</p>
<dt><code>usr-local-has-configs</code></p>
<dd>The system has configuration files under <i>/usr/local/etc</i>.</p>
<dt><code>usr-local-has-includes</code></p>
<dd>The system has header files under <i>/usr/local/include</i>.</p>
<dt><code>usr-local-has-programs</code></p>
<dd>The system has programs under <i>/usr/local/bin</i> or <i>/usr/local/sbin</i>.</p>
<dt><code>usr-local-has-libraries</code></p>
<dd>The system has libraries, either static or shared under <i>/usr/local/lib</i>.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Installed-Build-Depends:</code> (required)</p>
<dd>
<dt> <i>package-list</i></p>
<dd>The list of installed and configured packages that might affect the package build process. </p>
<p> The list consists of each package name, optionally arch-qualified for foreign architectures, with an exact version restriction, separated by commas. </p>
<p> The list includes all essential packages, packages listed in <code>Build-Depends</code>, <code>Build-Depends-Arch</code>, <code>Build-Depends-Indep</code> source control fields, any vendor specific builtin dependencies, and all their recursive dependencies. On Debian and derivatives the dependency builtin is <code>build-essential</code>. </p>
<p> For dependencies coming from the source control fields, all dependency alternatives and all providers of virtual packages depended on will be included.</p>
<dt><code>Environment:</code></p>
<dd>
<dt> <i>variable-list</i></p>
<dd>The list of environment variables that are known to affect the package build process, with each environment variable followed by an equal sign (&#8216;=&#8217;) and the variable&#8217;s quoted value, using double quotes (&#8216;&quot;&#8217;), and backslashes escaped (&#8216;\&#8217;).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5), <code><a href="/docs/linux/man/5-deb-changes/">deb-changes</a></code>(5), <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7), <code><a href="/docs/linux/man/1-dpkg-genbuildinfo/">dpkg-genbuildinfo</a></code>(1). </p>
