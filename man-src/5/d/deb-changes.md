---
title: "deb-changes(5)"
name: "deb-changes"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-changes/"
description: "deb-changes – Debian changes file format"
---

<p>deb-changes &#8211; Debian changes file format</p>
<h2>Synopsis</h2>
<p><i>filename</i><code>.changes</code></p>
<h2>Description</h2>
<p>Each Debian upload is composed of a .changes control file, which contains a number of fields in <code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5) format. </p>
<p> Each field begins with a tag, such as <code>Source</code> or <code>Binary</code> (case insensitive), followed by a colon, and the body of the field (case sensitive unless stated otherwise). Fields are delimited only by field tags. In other words, field text may be multiple lines in length, but the installation tools will generally join lines when processing the body of the field (except in case of the multiline fields <code>Description</code>, <code>Changes</code>, <code>Files</code>, <code>Checksums-Sha1</code> and <code>Checksums-Sha256</code>, see below). </p>
<p> The control data might be enclosed in an OpenPGP <font SIZE="-1">ASCII</font> Armored signature, as specified in <font SIZE="-1">RFC4880.</font></p>
<h2>Fields</h2>
<dl>
<dt><code>Format:</code> <i>format-version</i> (required)</p>
<dd>The value of this field declares the format version of the file. The syntax of the field value is a version number with a major and minor component. Backward incompatible changes to the format will bump the major version, and backward compatible changes (such as field additions) will bump the minor version. The current format version is <code>1.8</code>.</p>
<dt><code>Date:</code> <i>release-date</i> (required)</p>
<dd>The date the package was built or last edited. It must be in the same format as the date in a <code><a href="/docs/linux/man/5-deb-changelog/">deb-changelog</a></code>(5) entry. </p>
<p> The value of this field is usually extracted from the <i>debian/changelog</i> file.</p>
<dt><code>Source:</code> <i>source-name</i> [<code>(</code><i>source-version</i><code>)</code>] (required)</p>
<dd>The name of the source package. If the source version differs from the binary version, then the <i>source-name</i> will be followed by a <i>source-version</i> in parenthesis. This can happen when the upload is a binary-only non-maintainer upload.</p>
<dt><code>Binary:</code> <i>binary-package-list</i> (required in context)</p>
<dd>This folded field is a space-separated list of binary packages to upload. If the upload is source-only, then the field is omitted (since dpkg 1.19.3).</p>
<dt><code>Architecture:</code> <i>arch-list</i></p>
<dd>Lists the architectures of the files currently being uploaded. Common architectures are <code>amd64</code>, <code>armel</code>, <code>i386</code>, etc. Note that the <code>all</code> value is meant for packages that are architecture independent. If the source for the package is also being uploaded, the special entry <code>source</code> is also present. Architecture wildcards must never be present in the list.</p>
<dt><code>Version:</code> <i>version-string</i> (required)</p>
<dd>Typically, this is the original package&#8217;s version number in whatever form the program&#8217;s author uses. It may also include a Debian revision number (for non-native packages). The exact format and sorting algorithm are described in <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7).</p>
<dt><code>Distribution:</code> <i>distribution</i>s (required)</p>
<dd>Lists one or more space-separated distributions where this version should be installed when it is uploaded to the archive.</p>
<dt><code>Urgency:</code> <i>urgency</i> (recommended)</p>
<dd>The urgency of the upload. The currently known values, in increasing order of urgency, are: <code>low</code>, <code>medium</code>, <code>high</code>, <code>critical</code> and <code>emergency</code>.</p>
<dt><code>Maintainer:</code> <i>fullname-email</i> (required)</p>
<dd>Should be in the format &#8220;Joe Bloggs &lt;jbloggs [at] example.org&gt;&#8221;, and is typically the person who created the package, as opposed to the author of the software that was packaged.</p>
<dt><code>Changed-By:</code> <i>fullname-email</i></p>
<dd>Should be in the format &#8220;Joe Bloggs &lt;jbloggs [at] example.org&gt;&#8221;, and is typically the person who prepared the package changes for this release.</p>
<dt><code>Description:</code> (recommended)</p>
<dd>
<dt> <i>binary-package-name</i> <code>&#8211;</code> <i>binary-package-summary</i></p>
<dd>This multiline field contains a list of binary package names followed by a space, a dash (&#8216;<code>&#8211;</code>&#8216;) and their possibly truncated short descriptions. If the upload is source-only, then the field is omitted (since dpkg 1.19.3).</p>
<dt><code>Closes:</code> <i>bug-number-list</i></p>
<dd>A space-separated list of bug report numbers for bug reports that have been resolved with this upload. The distribution archive software might use this field to automatically close the referred bug numbers in the distribution bug tracking system.</p>
<dt><code>Binary-Only: yes</code></p>
<dd>This field denotes that the upload is a binary-only non-maintainer build. It originates from the <code>binary-only=yes</code> key/value from the changelog metadata entry.</p>
<dt><code>Built-For-Profiles:</code> <i>profile-list</i></p>
<dd>This field specifies a whitespace separated list of build profiles that this upload was built with.</p>
<dt><code>Changes:</code> (required)</p>
<dd>
<dt> <i>changelog-entries</i></p>
<dd>This multiline field contains the concatenated text of all changelog entries that are part of the upload. To make this a valid multiline field empty lines are replaced with a single full stop (&#8216;.&#8217;) and all lines are indented by one space character. The exact content depends on the changelog format.</p>
<dt><code>Files:</code> (required)</p>
<dd>
<dt> <i>md5sum</i> <i>size</i> <i>section</i> <i>priority</i> <i>filename</i></p>
<dd>This multiline field contains a list of files with an md5sum, size, section and priority for each one. </p>
<p> The first line of the field value (the part on the same line as the field name followed by a colon) is always empty. The content of the field is expressed as continuation lines, one line per file. Each line consists of space-separated entries describing the file: the md5sum, the file size, the file section, the file priority, and the file name. </p>
<p> This field lists all files that make up the upload. The list of files in this field must match the list of files in the other related <code>Checksums</code> fields.</p>
<dt><code>Checksums-Sha1:</code> (required)</p>
<dd>
<dt><code>Checksums-Sha256:</code> (required)</p>
<dd>
<dt> <i>checksum</i> <i>size</i> <i>filename</i></p>
<dd>These multiline fields contain a list of files with a checksum and size for each one. These fields have the same syntax and differ only in the checksum algorithm used: <font SIZE="-1">SHA-1</font> for <code>Checksums-Sha1</code> and <font SIZE="-1">SHA-256</font> for <code>Checksums-Sha256</code>. </p>
<p> The first line of the field value (the part on the same line as the field name followed by a colon) is always empty. The content of the field is expressed as continuation lines, one line per file. Each line consists of space-separated entries describing the file: the checksum, the file size, and the file name. </p>
<p> These fields list all files that make up the upload. The list of files in these fields must match the list of files in the <code>Files</code> field and the other related <code>Checksums</code> fields.</dl>
<h2>Bugs</h2>
<p>The <code>Files</code> field is inconsistent with the other <code>Checksums</code> fields. The <code>Changed-By</code> and <code>Maintainer</code> fields have confusing names. The <code>Distribution</code> field contains information about what is commonly referred to as a suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5), <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5), <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7). </p>
