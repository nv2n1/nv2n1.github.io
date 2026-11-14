---
title: "dsc(5)"
name: "dsc"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dsc/"
description: "dsc – Debian source packages’ control file format"
---

<p>dsc &#8211; Debian source packages&#8217; control file format</p>
<h2>Synopsis</h2>
<p><i>filename</i><code>.dsc</code></p>
<h2>Description</h2>
<p>Each Debian source package is composed of a .dsc control file, which contains a number of fields, in <code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5) format. </p>
<p> Each field begins with a tag, such as <code>Source</code> or <code>Binary</code> (case insensitive), followed by a colon, and the body of the field (case sensitive unless stated otherwise). Fields are delimited only by field tags. In other words, field text may be multiple lines in length, but the installation tools will generally join lines when processing the body of the field (except in case of the multiline fields <code>Package-List</code>, <code>Files</code>, <code>Checksums-Sha1</code> and <code>Checksums-Sha256</code>, see below). </p>
<p> The control data might be enclosed in an OpenPGP <font SIZE="-1">ASCII</font> Armored signature, as specified in <font SIZE="-1">RFC4880.</font></p>
<h2>Fields</h2>
<dl>
<dt><code>Format:</code> <i>format-version</i> (required)</p>
<dd>The value of this field declares the format version of the source package. The field value is used by programs acting on a source package to interpret the list of files in the source package and determine how to unpack it. The syntax of the field value is a numeric major revision (&#8220;0-9&#8221;), a period (&#8220;.&#8221;), a numeric minor revision (&#8220;0-9&#8243;), and then an optional subtype after whitespace (&#8221; 	&#8221;), which if specified is a lowercase alphanumeric (&#8220;a-z0-9&#8221;) word in parentheses (&#8220;()&#8221;). The subtype is optional in the syntax but may be mandatory for particular source format revisions. </p>
<p> The source formats currently supported by <code>dpkg</code> are <code>1.0</code>, <code>2.0</code>, <code>3.0 (native)</code>, <code>3.0 (quilt)</code>, <code>3.0 (git)</code>, <code>3.0 (bzr)</code> and <code>3.0 (custom)</code>. See <code><a href="/docs/linux/man/1-dpkg-source/">dpkg-source</a></code>(1) for their description.</p>
<dt><code>Source:</code> <i>source-name</i> (required)</p>
<dd>The value of this field determines the package name, and is used to generate file names by most installation tools.</p>
<dt><code>Binary:</code> <i>binary-package-list</i></p>
<dd>This folded field lists binary packages which this source package can produce, separated by commas. </p>
<p> This field has now been superseded by the <code>Package-List</code> field, which gives enough information about what binary packages are produced on which architecture, build-profile and other involved restrictions.</p>
<dt><code>Architecture:</code> <i>arch-list</i> (recommended)</p>
<dd>A list of architectures and architecture wildcards separated by spaces which specify the type of hardware this package can be compiled for. Common architecture names and architecture wildcards are <code>amd64</code>, <code>armel</code>, <code>i386</code>, <code>linux-any</code>, <code>any-amd64</code>, etc. </p>
<p> Note that the <code>all</code> value is meant for packages that are architecture independent, and <code>any</code> for packages that are architecture dependent. The list may include (or consist solely of) the special value <code>all</code>. When the list contains the architecture wildcard <code>any</code>, the only other value allowed in the list is <code>all</code>. </p>
<p> The field value is generally generated from <code>Architecture</code> fields from in the <i>debian/control</i> in the source package.</p>
<dt><code>Version:</code> <i>version-string</i> (required)</p>
<dd>Typically, this is the original package&#8217;s version number in whatever form the program&#8217;s author uses. It may also include a Debian revision number (for non-native packages). The exact format and sorting algorithm are described in <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7).</p>
<dt><code>Origin:</code> <i>name</i></p>
<dd>The name of the distribution this package is originating from.</p>
<dt><code>Maintainer:</code> <i>fullname-email</i> (recommended)</p>
<dd>Should be in the format &#8220;Joe Bloggs &lt;jbloggs [at] foo.com&gt;&#8221;, and is typically the person who created the package, as opposed to the author of the software that was packaged.</p>
<dt><code>Uploaders:</code> <i>fullname-email-list</i></p>
<dd>Lists all the names and email addresses of co-maintainers of the package, in the same format as the <code>Maintainer</code> field. Multiple co-maintainers should be separated by a comma.</p>
<dt><code>Description</code> <i>short-description</i></p>
<dd>
<dt> <i>long-description</i></p>
<dd>The format for the source package description is a short brief summary on the first line (after the <code>Description</code> field). The following lines should be used as a longer, more detailed description. Each line of the long description must be preceded by a space, and blank lines in the long description must contain a single &#8216;<code>.</code>&#8216; following the preceding space.</p>
<dt><code>Homepage:</code> <i>url</i></p>
<dd>The upstream project home page <i>url</i>.</p>
<dt><code>Standards-Version:</code> <i>version-string</i> (recommended)</p>
<dd>This documents the most recent version of the distribution policy standards this package complies with.</p>
<dt><code>Vcs-Browser:</code> <i>url</i></p>
<dd>The <i>url</i> of a web interface to browse the Version Control System repository.</p>
<dt><code>Vcs-Arch:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Bzr:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Cvs:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Darcs:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Git:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Hg:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Mtn:</code> <i>url</i></p>
<dd>
<dt><code>Vcs-Svn:</code> <i>url</i></p>
<dd>These fields declare the <i>url</i> of the Version Control System repository used to maintain this package. See <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5) for more details.</p>
<dt><code>Testsuite:</code> <i>name-list</i></p>
<dd>This field declares that the source package contains the specified test suites. The value is a comma-separated list of test suites. If the <code>autopkgtest</code> value is present, a <i>debian/tests/control</i> is expected to be present, if the file is present but not the value, then <code>dpkg-source</code> will automatically add it, preserving previous values.</p>
<dt><code>Testsuite-Triggers:</code> <i>package-list</i></p>
<dd>This field declares the comma-separated union of all test dependencies (<code>Depends</code> fields in <i>debian/tests/control</i> file), with all restrictions removed, and <font SIZE="-1">OR</font> dependencies flattened (that is, converted to separate <font SIZE="-1">AND</font> relationships), except for binaries generated by this source package and its meta-dependency equivalent <code>@</code>. </p>
<p> Rationale: this field is needed because otherwise to be able to get the test dependencies, each source package would need to be unpacked.</p>
<dt><code>Build-Depends:</code> <i>package-list</i></p>
<dd>
<dt><code>Build-Depends-Arch:</code> <i>package-list</i></p>
<dd>
<dt><code>Build-Depends-Indep:</code> <i>package-list</i></p>
<dd>
<dt><code>Build-Conflicts:</code> <i>package-list</i></p>
<dd>
<dt><code>Build-Conflicts-Arch:</code> <i>package-list</i></p>
<dd>
<dt><code>Build-Conflicts-Indep:</code> <i>package-list</i></p>
<dd>These fields declare relationships between the source package and packages used to build it. They are discussed in the <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5) manpage.</p>
<dt><code>Package-List:</code></p>
<dd>
<dt> <i>package</i> <i>package-type</i> <i>section</i> <i>priority</i> <i>key-value-list</i></p>
<dd>This multiline field contains a list of binary packages generated by this source package. </p>
<p> The <i>package</i> is the binary package name. </p>
<p> The <i>package-type</i> is the binary package type, usually <code>deb</code>, another common value is <code>udeb</code>. </p>
<p> The <i>section</i> and <i>priority</i> match the binary package fields of the same name. </p>
<p> The <i>key-value-list</i> is a space separated <i>key</i><code>=</code><i>value</i> list, and the currently known optional keys are:</p>
<dl>
<dd>
<dl>
<dt><code>arch</code></p>
<dd>The architecture restriction from the binary package <code>Architecture</code> field, with spaces converted to &#8216;,&#8217;.</p>
<dt><code>profile</code></p>
<dd>The normalized build-profile restriction formula from the binary package <code>Build-Profile</code> field, with ORs converted to &#8216;+&#8217; and ANDs to &#8216;,&#8217;.</p>
<dt><code>protected</code></p>
<dd>If the binary package is protected, this key will contain the value of the <code>Protected</code> field, that is a <code>yes</code> value. </p>
<p> Supported since dpkg 1.20.1.</p>
<dt><code>essential</code></p>
<dd>If the binary package is essential, this key will contain the value of the <code>Essential</code> field, that is a <code>yes</code> value.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Files:</code> (required)</p>
<dd>
<dt><code>Checksums-Sha1:</code> (required)</p>
<dd>
<dt><code>Checksums-Sha256:</code> (required)</p>
<dd>
<dt> <i>checksum</i> <i>size</i> <i>filename</i></p>
<dd>These multiline fields contain a list of files with a checksum and size for each one. These fields have the same syntax and differ only in the checksum algorithm used: <font SIZE="-1">MD5</font> for <code>Files</code>, <font SIZE="-1">SHA-1</font> for <code>Checksums-Sha1</code> and <font SIZE="-1">SHA-256</font> for <code>Checksums-Sha256</code>. </p>
<p> The first line of the field value (the part on the same line as the field name followed by a colon) is always empty. The content of the field is expressed as continuation lines, one line per file. Each line consists of the checksum, a space, the file size, a space, and the file name. </p>
<p> These fields list all files that make up the source package. The list of files in these fields must match the list of files in the other related fields.</dl>
<h2>Bugs</h2>
<p>The <code>Format</code> field conflates the format for the <code>.dsc</code> file itself and the format of the extracted source package.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5), <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5), <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7), <code><a href="/docs/linux/man/1-dpkg-source/">dpkg-source</a></code>(1). </p>
