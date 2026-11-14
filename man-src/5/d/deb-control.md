---
title: "deb-control(5)"
name: "deb-control"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-control/"
description: "deb-control – Debian binary packages’ master control file format"
---

<p>deb-control &#8211; Debian binary packages&#8217; master control file format</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/control</code></p>
<h2>Description</h2>
<p>Each Debian binary package contains a <code>control</code> file in its <code>control</code> member, and its <code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5) format is a subset of the master <code>debian/control</code> file in Debian source packages, see <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5). </p>
<p> This file contains a number of fields. Each field begins with a tag, such as <code>Package</code> or <code>Version</code> (case insensitive), followed by a colon, and the body of the field (case sensitive unless stated otherwise). Fields are delimited only by field tags. In other words, field text may be multiple lines in length, but the installation tools will generally join lines when processing the body of the field (except in the case of the <code>Description</code> field, see below).</p>
<h2>Fields</h2>
<dl>
<dt><code>Package:</code> <i>package-name</i> (required)</p>
<dd>The value of this field determines the package name, and is used to generate file names by most installation tools.</p>
<dt><code>Package-Type:</code> <code>deb</code>|<code>udeb</code>|<i>type</i></p>
<dd>This field defines the type of the package. <code>udeb</code> is for size-constrained packages used by the debian installer. <code>deb</code> is the default value, it is assumed if the field is absent. More types might be added in the future.</p>
<dt><code>Version:</code> <i>version-string</i> (required)</p>
<dd>Typically, this is the original package&#8217;s version number in whatever form the program&#8217;s author uses. It may also include a Debian revision number (for non-native packages). The exact format and sorting algorithm are described in <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7).</p>
<dt><code>Maintainer:</code> <i>fullname-email</i> (recommended)</p>
<dd>Should be in the format &#8220;Joe Bloggs &lt;jbloggs [at] foo.com&gt;&#8221;, and is typically the person who created the package, as opposed to the author of the software that was packaged.</p>
<dt><code>Description:</code> <i>short-description</i> (recommended)</p>
<dd>
<dt> <i>long-description</i></p>
<dd>The format for the package description is a short brief summary on the first line (after the <code>Description</code> field). The following lines should be used as a longer, more detailed description. Each line of the long description must be preceded by a space, and blank lines in the long description must contain a single &#8216;<code>.</code>&#8216; following the preceding space.</p>
<dt><code>Section:</code> <i>section</i></p>
<dd>This is a general field that gives the package a category based on the software that it installs. Some common sections are <code>utils</code>, <code>net</code>, <code>mail</code>, <code>text</code>, <code>x11</code>, etc.</p>
<dt><code>Priority:</code> <i>priority</i></p>
<dd>Sets the importance of this package in relation to the system as a whole. Common priorities are <code>required</code>, <code>standard</code>, <code>optional</code>, <code>extra</code>, etc.</dl>
<p> The <code>Section</code> and <code>Priority</code> fields usually have a defined set of accepted values based on the specific distribution policy.</p>
<dl>
<dt><code>Installed-Size:</code> <i>size</i></p>
<dd>The approximate total size of the package&#8217;s installed files, in KiB units. The algorithm to compute the size is described in <code><a href="/docs/linux/man/5-deb-substvars/">deb-substvars</a></code>(5).</p>
<dt><code>Protected:</code> <code>yes</code>|<code>no</code></p>
<dd>This field is usually only needed when the answer is <code>yes</code>. It denotes a package that is required for proper booting of the system. <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) or any other installation tool will not allow a <code>Protected</code> package to be removed (at least not without using one of the force options). </p>
<p> Supported since dpkg 1.20.1.</p>
<dt><code>Essential:</code> <code>yes</code>|<code>no</code></p>
<dd>This field is usually only needed when the answer is <code>yes</code>. It denotes a package that is required for proper operation of the system. <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) or any other installation tool will not allow an <code>Essential</code> package to be removed (at least not without using one of the force options).</p>
<dt><code>Build-Essential:</code> <code>yes</code>|<code>no</code></p>
<dd>This field is usually only needed when the answer is <code>yes</code>, and is commonly injected by the archive software. It denotes a package that is required when building other packages.</p>
<dt><code>Architecture:</code> <i>arch</i>|<code>all</code> (required)</p>
<dd>The architecture specifies which type of hardware this package was compiled for. Common architectures are <code>amd64</code>, <code>armel</code>, <code>i386</code>, <code>powerpc</code>, etc. Note that the <code>all</code> value is meant for packages that are architecture independent. Some examples of this are shell and Perl scripts, and documentation.</p>
<dt><code>Origin:</code> <i>name</i></p>
<dd>The name of the distribution this package is originating from.</p>
<dt><code>Bugs:</code> <i>url</i></p>
<dd>The <i>url</i> of the bug tracking system for this package. The current used format is <i>bts-type</i><code>://</code><i>bts-address</i>, like <code>debbugs://bugs.debian.org</code>.</p>
<dt><code>Homepage:</code> <i>url</i></p>
<dd>The upstream project home page <i>url</i>.</p>
<dt><code>Tag:</code> <i>tag-list</i></p>
<dd>List of tags describing the qualities of the package. The description and list of supported tags can be found in the <code>debtags</code> package.</p>
<dt><code>Multi-Arch:</code> <code>no</code>|<code>same</code>|<code>foreign</code>|<code>allowed</code></p>
<dd>This field is used to indicate how this package should behave on a multi-arch installations.</p>
<dl>
<dd>
<dl>
<dt><code>no</code></p>
<dd>This value is the default when the field is omitted, in which case adding the field with an explicit <code>no</code> value is generally not needed.</p>
<dt><code>same</code></p>
<dd>This package is co-installable with itself, but it must not be used to satisfy the dependency of any package of a different architecture from itself.</p>
<dt><code>foreign</code></p>
<dd>This package is not co-installable with itself, but should be allowed to satisfy a non-arch-qualified dependency of a package of a different arch from itself (if a dependency has an explicit arch-qualifier then the value <code>foreign</code> is ignored).</p>
<dt><code>allowed</code></p>
<dd>This allows reverse-dependencies to indicate in their <code>Depends</code> field that they accept this package from a foreign architecture by qualifying the package name with <code>:any</code>, but has no effect otherwise.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Source:</code> <i>source-name</i> [<code>(</code><i>source-version</i><code>)</code>]</p>
<dd>The name of the source package that this binary package came from, if it is different than the name of the package itself. If the source version differs from the binary version, then the <i>source-name</i> will be followed by a <i>source-version</i> in parenthesis. This can happen for example on a binary-only non-maintainer upload, or when setting a different binary version via &laquo;<code>dpkg-gencontrol -v</code>&raquo;.</p>
<dt><code>Subarchitecture:</code> <i>value</i></p>
<dd>
<dt><code>Kernel-Version:</code> <i>value</i></p>
<dd>
<dt><code>Installer-Menu-Item:</code> <i>value</i></p>
<dd>These fields are used by the debian-installer and are usually not needed. See /usr/share/doc/debian-installer/devel/modules.txt from the <code>debian-installer</code> package for more details about them.</p>
<dt><code>Depends:</code> <i>package-list</i></p>
<dd>List of packages that are required for this package to provide a non-trivial amount of functionality. The package maintenance software will not allow a package to be installed if the packages listed in its <code>Depends</code> field aren&#8217;t installed (at least not without using the force options). In an installation, the postinst scripts of packages listed in <code>Depends</code> fields are run before those of the packages which depend on them. On the opposite, in a removal, the prerm script of a package is run before those of the packages listed in its <code>Depends</code> field.</p>
<dt><code>Pre-Depends:</code> <i>package-list</i></p>
<dd>List of packages that must be installed <code>and</code> configured before this one can be installed. This is usually used in the case where this package requires another package for running its preinst script.</p>
<dt><code>Recommends:</code> <i>package-list</i></p>
<dd>Lists packages that would be found together with this one in all but unusual installations. The package maintenance software will warn the user if they install a package without those listed in its <code>Recommends</code> field.</p>
<dt><code>Suggests:</code> <i>package-list</i></p>
<dd>Lists packages that are related to this one and can perhaps enhance its usefulness, but without which installing this package is perfectly reasonable.</dl>
<p> The syntax of <code>Depends</code>, <code>Pre-Depends</code>, <code>Recommends</code> and <code>Suggests</code> fields is a list of groups of alternative packages. Each group is a list of packages separated by vertical bar (or &#8220;pipe&#8221;) symbols, &#8216;<code>|</code>&#8216;. The groups are separated by commas. Commas are to be read as &#8220;AND&#8221;, and pipes as &#8220;OR&#8221;, with pipes binding more tightly. Each package name is optionally followed by an architecture qualifier appended after a colon &#8216;<code>:</code>&#8216;, optionally followed by a version number specification in parentheses. </p>
<p> An architecture qualifier name can be a real Debian architecture name (since dpkg 1.16.5) or <code>any</code> (since dpkg 1.16.2). If omitted, the default is the current binary package architecture. A real Debian architecture name will match exactly that architecture for that package name, <code>any</code> will match any architecture for that package name if the package has been marked as <code>Multi-Arch: allowed</code>. </p>
<p> A version number may start with a &#8216;<code>&gt;&gt;</code>&#8216;, in which case any later version will match, and may specify or omit the Debian packaging revision (separated by a hyphen). Accepted version relationships are &#8216;<code>&gt;&gt;</code>&#8216; for greater than, &#8216;<code>&lt;&lt;</code>&#8216; for less than, &#8216;<code>&gt;=</code>&#8216; for greater than or equal to, &#8216;<code>&lt;=</code>&#8216; for less than or equal to, and &#8216;<code>=</code>&#8216; for equal to.</p>
<dl>
<dt><code>Breaks:</code> <i>package-list</i></p>
<dd>Lists packages that this one breaks, for example by exposing bugs when the named packages rely on this one. The package maintenance software will not allow broken packages to be configured; generally the resolution is to upgrade the packages named in a <code>Breaks</code> field.</p>
<dt><code>Conflicts:</code> <i>package-list</i></p>
<dd>Lists packages that conflict with this one, for example by containing files with the same names. The package maintenance software will not allow conflicting packages to be installed at the same time. Two conflicting packages should each include a <code>Conflicts</code> line mentioning the other.</p>
<dt><code>Replaces:</code> <i>package-list</i></p>
<dd>List of packages files from which this one replaces. This is used for allowing this package to overwrite the files of another package and is usually used with the <code>Conflicts</code> field to force removal of the other package, if this one also has the same files as the conflicted package.</dl>
<p> The syntax of <code>Breaks</code>, <code>Conflicts</code> and <code>Replaces</code> is a list of package names, separated by commas (and optional whitespace). In the <code>Breaks</code> and <code>Conflicts</code> fields, the comma should be read as &#8220;OR&#8221;. An optional architecture qualifier can also be appended to the package name with the same syntax as above, but the default is <code>any</code> instead of the binary package architecture. An optional version can also be given with the same syntax as above for the <code>Breaks</code>, <code>Conflicts</code> and <code>Replaces</code> fields.</p>
<dl>
<dt><code>Enhances:</code> <i>package-list</i></p>
<dd>This is a list of packages that this one enhances. It is similar to <code>Suggests</code> but in the opposite direction.</p>
<dt><code>Provides:</code> <i>package-list</i></p>
<dd>This is a list of virtual packages that this one provides. Usually this is used in the case of several packages all providing the same service. For example, sendmail and exim can serve as a mail server, so they provide a common package (&#8220;mail-transport-agent&#8221;) on which other packages can depend. This will allow sendmail or exim to serve as a valid option to satisfy the dependency. This prevents the packages that depend on a mail server from having to know the package names for all of them, and using &#8216;<code>|</code>&#8216; to separate the list.</dl>
<p> The syntax of <code>Provides</code> is a list of package names, separated by commas (and optional whitespace). An optional architecture qualifier can also be appended to the package name with the same syntax as above. If omitted, the default is the current binary package architecture. An optional exact (equal to) version can also be given with the same syntax as above (honored since dpkg 1.17.11).</p>
<dl>
<dt><code>Built-Using:</code> <i>package-list</i></p>
<dd>This field lists extra source packages that were used during the build of this binary package. This is an indication to the archive maintenance software that these extra source packages must be kept whilst this binary package is maintained. This field must be a list of source package names with strict &#8216;<code>=</code>&#8216; version relationships. Note that the archive maintenance software is likely to refuse to accept an upload which declares a <code>Built-Using</code> relationship which cannot be satisfied within the archive.</p>
<dt><code>Built-For-Profiles:</code> <i>profile-list</i> (obsolete)</p>
<dd>This field used to specify a whitespace separated list of build profiles that this binary packages was built with (since dpkg 1.17.2 until 1.18.18). The information previously found in this field can now be found in the <code>.buildinfo</code> file, which supersedes it.</p>
<dt><code>Auto-Built-Package:</code> <i>reason-list</i></p>
<dd>This field specifies a whitespace separated list of reasons why this package was auto-generated. Binary packages marked with this field will not appear in the <i>debian/control</i> master source control file. The only currently used reason is <code>debug-symbols</code>.</p>
<dt><code>Build-Ids:</code> <i>elf-build-id-list</i></p>
<dd>This field specifies a whitespace separated list of <font SIZE="-1">ELF</font> build-ids. These are unique identifiers for semantically identical <font SIZE="-1">ELF</font> objects, for each of these within the package. </p>
<p> The format or the way to compute each build-id is not defined by design.</dl>
<h2>Example</h2>
<pre> Package: grep
 Essential: yes
 Priority: required
 Section: base
 Maintainer: Wichert Akkerman &lt;wakkerma [at] debian.org&gt;
 Architecture: sparc
 Version: 2.4-1
 Pre-Depends: libc6 (&gt;= 2.0.105)
 Provides: rgrep
 Conflicts: rgrep
 Description: GNU grep, egrep and fgrep.
 The GNU family of grep utilities may be the &quot;fastest grep in the west&quot;.
 GNU grep is based on a fast lazy-state deterministic matcher (about
 twice as fast as stock Unix egrep) hybridized with a Boyer-Moore-Gosper
 search for a fixed string that eliminates impossible text from being
 considered by the full regexp matcher without necessarily having to
 look at every character. The result is typically many times faster
 than Unix grep or egrep. (Regular expressions containing backreferencing
 will run more slowly, however).</pre>
<h2>Bugs</h2>
<p>The <code>Build-Ids</code> field uses a rather generic name out of its original context within an <font SIZE="-1">ELF</font> object, which serves a very specific purpose and executable format.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5), <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5), <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5), <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7), <code><a href="/docs/linux/man/1-debtags/">debtags</a></code>(1), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1). </p>
