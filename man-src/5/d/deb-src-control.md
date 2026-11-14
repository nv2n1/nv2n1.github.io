---
title: "deb-src-control(5)"
name: "deb-src-control"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-src-control/"
description: "deb-src-control – Debian source packages’ master control file format"
---

<p>deb-src-control &#8211; Debian source packages&#8217; master control file format</p>
<h2>Synopsis</h2>
<p><code>debian/control</code></p>
<h2>Description</h2>
<p>Each Debian source package contains the master &laquo;<code>debian/control</code>&raquo; file, and its <code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5) format is a superset of the <code>control</code> file shipped in Debian binary packages, see <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5). </p>
<p> This file contains at least 2 paragraphs, separated by a blank line. The first paragraph lists all information about the source package in general, while each following paragraph describes exactly one binary package. Each paragraph consists of at least one field. A field starts with a fieldname, such as <code>Package</code> or <code>Section</code> (case insensitive), followed by a colon, the body of the field (case sensitive unless stated otherwise) and a newline. Multi-line fields are also allowed, but each supplementary line, without a fieldname, should start with at least one space. The content of the multi-line fields is generally joined to a single line by the tools (except in the case of the <code>Description</code> field, see below). To insert empty lines into a multi-line field, insert a dot after the space. Lines starting with a &#8216;<code>#</code>&#8216; are treated as comments.</p>
<h2>Source Fields</h2>
<dl>
<dt><code>Source:</code> <i>source-package-name</i> (required)</p>
<dd>The value of this field is the name of the source package, and should match the name of the source package in the debian/changelog file. A package name must consist only of lowercase letters (a-z), digits (0-9), plus (+) and minus (-) signs, and periods (.). Package names must be at least two characters long and must start with a lowercase alphanumeric character (a-z0-9).</p>
<dt><code>Maintainer:</code> <i>fullname-email</i> (recommended)</p>
<dd>Should be in the format &laquo;Joe Bloggs &lt;jbloggs [at] foo.com&gt;&raquo;, and references the person who currently maintains the package, as opposed to the author of the software or the original packager.</p>
<dt><code>Uploaders:</code> <i>fullname-email</i></p>
<dd>Lists all the names and email addresses of co-maintainers of the package, in the same format as the <code>Maintainer</code> field. Multiple co-maintainers should be separated by a comma.</p>
<dt><code>Standards-Version:</code> <i>version-string</i></p>
<dd>This documents the most recent version of the distribution policy standards this package complies with.</p>
<dt><code>Description</code> <i>short-description</i></p>
<dd>
<dt> <i>long-description</i></p>
<dd>The format for the source package description is a short brief summary on the first line (after the <code>Description</code> field). The following lines should be used as a longer, more detailed description. Each line of the long description must be preceded by a space, and blank lines in the long description must contain a single &#8216;<code>.</code>&#8216; following the preceding space.</p>
<dt><code>Homepage:</code> <i>url</i></p>
<dd>The upstream project home page <font SIZE="-1">URL.</font></p>
<dt><code>Bugs:</code> <i>url</i></p>
<dd>The <i>url</i> of the bug tracking system for this package. The current used format is <i>bts-type</i><code>://</code><i>bts-address</i>, like <code>debbugs://bugs.debian.org</code>. This field is usually not needed.</p>
<dt><code>Rules-Requires-Root:</code> <code>no</code>|<code>binary-targets</code>|<i>impl-keywords</i></p>
<dd>This field is used to indicate whether the <code>debian/rules</code> file requires (fake)root privileges to run some of its targets, and if so when.</p>
<dl>
<dd>
<dl>
<dt><code>no</code></p>
<dd>The binary targets will not require (fake)root at all.</p>
<dt><code>binary-targets</code></p>
<dd>The binary targets must always be run under (fake)root. This value is the default when the field is omitted; adding the field with an explicit <code>binary-targets</code> while not strictly needed, marks it as having been analyzed for this requirement.</p>
<dt><i>impl-keywords</i></p>
<dd>This is a space-separated list of keywords which define when (fake)root is required. </p>
<p> Keywords consist of <i>namespace</i>/<i>cases</i>. The <i>namespace</i> part cannot contain &#8220;/&#8221; or whitespace. The <i>cases</i> part cannot contain whitespace. Furthermore, both parts must consist entirely of printable <font SIZE="-1">ASCII</font> characters. </p>
<p> Each tool/package will define a namespace named after itself and provide a number of cases where (fake)root is required. (See &#8220;Implementation provided keywords&#8221; in <i>rootless-builds.txt</i>). </p>
<p> When the field is set to one of the <i>impl-keywords</i>, the builder will expose an interface that is used to run a command under (fake)root. (See &#8220;Gain Root <font SIZE="-1">API&#8221;</font> in <i>rootless-builds.txt</i>.)</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Testsuite:</code> <i>name-list</i></p>
<dd>
<dt><code>Testsuite-Triggers:</code> <i>package-list</i></p>
<dd>These fields are described in the <code><a href="/docs/linux/man/5-dsc/">dsc</a></code>(5) manual page, as they are generated from information inferred from <code>debian/tests/control</code> or copied literally to the source control file.</p>
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
<dd>The <i>url</i> of the Version Control System repository used to maintain this package. Currently supported are <code>Arch</code>, <code>Bzr</code> (Bazaar), <code>Cvs</code>, <code>Darcs</code>, <code>Git</code>, <code>Hg</code> (Mercurial), <code>Mtn</code> (Monotone) and <code>Svn</code> (Subversion). Usually this field points to the latest version of the package, such as the main branch or the trunk.</p>
<dt><code>Vcs-Browser:</code> <i>url</i></p>
<dd>The <i>url</i> of a webinterface to browse the Version Control System repository.</p>
<dt><code>Origin:</code> <i>name</i></p>
<dd>The name of the distribution this package is originating from. This field is usually not needed.</p>
<dt><code>Section:</code> <i>section</i></p>
<dd>This is a general field that gives the package a category based on the software that it installs. Some common sections are <code>utils</code>, <code>net</code>, <code>mail</code>, <code>text</code>, <code>x11</code>, etc.</p>
<dt><code>Priority:</code> <i>priority</i></p>
<dd>Sets the importance of this package in relation to the system as a whole. Common priorities are <code>required</code>, <code>standard</code>, <code>optional</code>, <code>extra</code>, etc. </p>
<p> The <code>Section</code> and <code>Priority</code> fields usually have a defined set of accepted values based on the specific distribution policy.</p>
<dt><code>Build-Depends:</code> <i>package-list</i></p>
<dd>A list of packages that need to be installed and configured to be able to build from source package. These dependencies need to be satisfied when building binary architecture dependent or independent packages and source packages. Including a dependency in this field does not have the exact same effect as including it in both <code>Build-Depends-Arch</code> and <code>Build-Depends-Indep</code>, because the dependency also needs to be satisfied when building the source package.</p>
<dt><code>Build-Depends-Arch:</code> <i>package-list</i></p>
<dd>Same as <code>Build-Depends</code>, but they are only needed when building the architecture dependent packages. The <code>Build-Depends</code> are also installed in this case. This field is supported since dpkg 1.16.4; in order to build with older dpkg versions, <code>Build-Depends</code> should be used instead.</p>
<dt><code>Build-Depends-Indep:</code> <i>package-list</i></p>
<dd>Same as <code>Build-Depends</code>, but they are only needed when building the architecture independent packages. The <code>Build-Depends</code> are also installed in this case.</p>
<dt><code>Build-Conflicts:</code> <i>package-list</i></p>
<dd>A list of packages that should not be installed when the package is built, for example because they interfere with the build system used. Including a dependency in this list has the same effect as including it in both <code>Build-Conflicts-Arch</code> and <code>Build-Conflicts-Indep</code>, with the additional effect of being used for source-only builds.</p>
<dt><code>Build-Conflicts-Arch:</code> <i>package-list</i></p>
<dd>Same as <code>Build-Conflicts</code>, but only when building the architecture dependent packages. This field is supported since dpkg 1.16.4; in order to build with older dpkg versions, <code>Build-Conflicts</code> should be used instead.</p>
<dt><code>Build-Conflicts-Indep:</code> <i>package-list</i></p>
<dd>Same as <code>Build-Conflicts</code>, but only when building the architecture independent packages.</dl>
<p> The syntax of the <code>Build-Depends</code>, <code>Build-Depends-Arch</code> and <code>Build-Depends-Indep</code> fields is a list of groups of alternative packages. Each group is a list of packages separated by vertical bar (or &#8220;pipe&#8221;) symbols, &#8216;<code>|</code>&#8216;. The groups are separated by commas &#8216;<code>,</code>&#8216;, and can end with a trailing comma that will be eliminated when generating the fields for <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5) (since dpkg 1.10.14). Commas are to be read as &#8220;AND&#8221;, and pipes as &#8220;OR&#8221;, with pipes binding more tightly. Each package name is optionally followed by an architecture qualifier appended after a colon &#8216;<code>:</code>&#8216;, optionally followed by a version number specification in parentheses &#8216;<code>(</code>&#8216; and &#8216;<code>)</code>&#8216;, an architecture specification in square brackets &#8216;<code>[</code>&#8216; and &#8216;<code>]</code>&#8216;, and a restriction formula consisting of one or more lists of profile names in angle brackets &#8216;<code>&lt;</code>&#8216; and &#8216;<code>&gt;</code>&#8216;. </p>
<p> The syntax of the <code>Build-Conflicts</code>, <code>Build-Conflicts-Arch</code> and <code>Build-Conflicts-Indep</code> fields is a list of comma-separated package names, where the comma is read as an &#8220;AND&#8221;, and where the list can end with a trailing comma that will be eliminated when generating the fields for <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5) (since dpkg 1.10.14). Specifying alternative packages using a &#8220;pipe&#8221; is not supported. Each package name is optionally followed by a version number specification in parentheses, an architecture specification in square brackets, and a restriction formula consisting of one or more lists of profile names in angle brackets. </p>
<p> An architecture qualifier name can be a real Debian architecture name (since dpkg 1.16.5), <code>any</code> (since dpkg 1.16.2) or <code>native</code> (since dpkg 1.16.5). If omitted, the default for <code>Build-Depends</code> fields is the current host architecture, the default for <code>Build-Conflicts</code> fields is <code>any</code>. A real Debian architecture name will match exactly that architecture for that package name, <code>any</code> will match any architecture for that package name if the package is marked with <code>Multi-Arch: allowed</code>, and <code>native</code> will match the current build architecture if the package is not marked with <code>Multi-Arch: foreign</code>. </p>
<p> A version number may start with a &#8216;<code>&gt;&gt;</code>&#8216;, in which case any later version will match, and may specify or omit the Debian packaging revision (separated by a hyphen). Accepted version relationships are &#8216;<code>&gt;&gt;</code>&#8216; for greater than, &#8216;<code>&lt;&lt;</code>&#8216; for less than, &#8216;<code>&gt;=</code>&#8216; for greater than or equal to, &#8216;<code>&lt;=</code>&#8216; for less than or equal to, and &#8216;<code>=</code>&#8216; for equal to. </p>
<p> An architecture specification consists of one or more architecture names, separated by whitespace. Exclamation marks may be prepended to each of the names, meaning &#8220;NOT&#8221;. </p>
<p> A restriction formula consists of one or more restriction lists, separated by whitespace. Each restriction list is enclosed in angle brackets. Items in the restriction list are build profile names, separated by whitespace and can be prefixed with an exclamation mark, meaning &#8220;NOT&#8221;. A restriction formula represents a disjunctive normal form expression. </p>
<p> Note that dependencies on packages in the <code>build-essential</code> set can be omitted and that declaring build conflicts against them is impossible. A list of these packages is in the build-essential package.</p>
<h2>Binary Fields</h2>
<p>Note that the <code>Priority</code>, <code>Section</code> and <code>Homepage</code> fields can also be in a binary paragraph to override the global value from the source package.</p>
<dl>
<dt><code>Package:</code> <i>binary-package-name</i> (required)</p>
<dd>This field is used to name the binary package name. The same restrictions as to a source package name apply.</p>
<dt><code>Package-Type:</code> <code>deb</code>|<code>udeb</code>|<i>type</i></p>
<dd>This field defines the type of the package. <code>udeb</code> is for size-constrained packages used by the debian installer. <code>deb</code> is the default value, it is assumed if the field is absent. More types might be added in the future.</p>
<dt><code>Architecture:</code> <i>arch</i>|<code>all</code>|<code>any</code> (required)</p>
<dd>The architecture specifies on which type of hardware this package runs. For packages that run on all architectures, use the <code>any</code> value. For packages that are architecture independent, such as shell and Perl scripts or documentation, use the <code>all</code> value. To restrict the packages to a certain set of architectures, specify the architecture names, separated by a space. It&#8217;s also possible to put architecture wildcards in that list (see <code><a href="/docs/linux/man/1-dpkg-architecture/">dpkg-architecture</a></code>(1) for more information about them).</p>
<dt><code>Build-Profiles:</code> <i>restriction-formula</i></p>
<dd>This field specifies the conditions for which this binary package does or does not build. To express that condition, the same restriction formula syntax from the <code>Build-Depends</code> field is used. </p>
<p> If a binary package paragraph does not contain this field, then it implicitly means that it builds with all build profiles (including none at all). </p>
<p> In other words, if a binary package paragraph is annotated with a non-empty <code>Build-Profiles</code> field, then this binary package is generated if and only if the condition expressed by the conjunctive normal form expression evaluates to true.</p>
<dt><code>Protected:</code> <code>Byes</code>|<code>no</code></p>
<dd>
<dt><code>Essential:</code> <code>yes</code>|<code>no</code></p>
<dd>
<dt><code>Build-Essential:</code> <code>yes</code>|<code>no</code></p>
<dd>
<dt><code>Multi-Arch:</code> <code>same</code>|<code>foreign</code>|<code>allowed</code>|<code>no</code></p>
<dd>
<dt><code>Tag:</code> <i>tag-list</i></p>
<dd>
<dt><code>Description:</code> <i>short-description</i> (recommended)</p>
<dd>These fields are described in the <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5) manual page, as they are copied literally to the control file of the binary package.</p>
<dt><code>Depends:</code> <i>package-list</i></p>
<dd>
<dt><code>Pre-Depends:</code> <i>package-list</i></p>
<dd>
<dt><code>Recommends:</code> <i>package-list</i></p>
<dd>
<dt><code>Suggests:</code> <i>package-list</i></p>
<dd>
<dt><code>Breaks:</code> <i>package-list</i></p>
<dd>
<dt><code>Enhances:</code> <i>package-list</i></p>
<dd>
<dt><code>Replaces:</code> <i>package-list</i></p>
<dd>
<dt><code>Conflicts:</code> <i>package-list</i></p>
<dd>
<dt><code>Provides:</code> <i>package-list</i></p>
<dd>
<dt><code>Built-Using:</code> <i>package-list</i></p>
<dd>These fields declare relationships between packages. They are discussed in the <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5) manpage. When these fields are found in <i>debian/control</i> they can also end with a trailing comma (since dpkg 1.10.14), have architecture specifications and restriction formulas which will all get reduced when generating the fields for <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5).</p>
<dt><code>Subarchitecture:</code> <i>value</i></p>
<dd>
<dt><code>Kernel-Version:</code> <i>value</i></p>
<dd>
<dt><code>Installer-Menu-Item:</code> <i>value</i></p>
<dd>These fields are used by the debian-installer in <code>udeb</code>s and are usually not needed. See /usr/share/doc/debian-installer/devel/modules.txt from the <code>debian-installer</code> package for more details about them.</dl>
<h2>User-Defined Fields</h2>
<p>It is allowed to add additional user-defined fields to the control file. The tools will ignore these fields. If you want the fields to be copied over to the output files, such as the binary packages, you need to use a custom naming scheme: the fields should start with an <code>X</code>, followed by zero or more of the letters <font SIZE="-1"><code>SBC</code></font> and a hyphen.</p>
<dl>
<dt><code>S</code></p>
<dd>The field will appear in the source package control file, see <code><a href="/docs/linux/man/5-dsc/">dsc</a></code>(5).</p>
<dt><code>B</code></p>
<dd>The field will appear in the control file in the binary package, see <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5).</p>
<dt><code>C</code></p>
<dd>The field will appear in the upload control (.changes) file, see <code><a href="/docs/linux/man/5-deb-changes/">deb-changes</a></code>(5).</dl>
<p> Note that the <code>X</code>[<font SIZE="-1"><code>SBC</code></font>]<code>&#8211;</code> prefixes are stripped when the fields are copied over to the output files. A field <code>XC-Approved-By</code> will appear as <code>Approved-By</code> in the changes file and will not appear in the binary or source package control files. </p>
<p> Take into account that these user-defined fields will be using the global namespace, which might at some point in the future collide with officially recognized fields. To avoid such potential situation you can prefix those fields with <code>Private-</code>, such as <code>XB-Private-New-Field</code>.</p>
<h2>Example</h2>
<pre> # Comment
 Source: dpkg
 Section: admin
 Priority: required
 Maintainer: Dpkg Developers &lt;debian-dpkg [at] lists.debian.org&gt;
 # this field is copied to the binary and source packages
 XBS-Upstream-Release-Status: stable
 Homepage: <a rel="nofollow" href="https://wiki.debian.org/Teams/Dpkg">https://wiki.debian.org/Teams/Dpkg</a>
 Vcs-Browser: <a rel="nofollow" href="https://git.dpkg.org/cgit/dpkg/dpkg.git">https://git.dpkg.org/cgit/dpkg/dpkg.git</a>
 Vcs-Git: <a rel="nofollow" href="https://git.dpkg.org/git/dpkg/dpkg.git">https://git.dpkg.org/git/dpkg/dpkg.git</a>
 Standards-Version: 3.7.3
 Build-Depends: pkg-config, debhelper (&gt;= 4.1.81),
 libselinux1-dev (&gt;= 1.28-4) [!linux-any]
 Package: dpkg-dev
 Section: utils
 Priority: optional
 Architecture: all
 # this is a custom field in the binary package
 XB-Mentoring-Contact: Raphael Hertzog &lt;hertzog [at] debian.org&gt;
 Depends: dpkg (&gt;= 1.14.6), perl5, perl-modules, cpio (&gt;= 2.4.2-2),
 bzip2, lzma, patch (&gt;= 2.2-1), make, binutils, libtimedate-perl
 Recommends: gcc | c-compiler, build-essential
 Suggests: gnupg, debian-keyring
 Conflicts: dpkg-cross (&lt;&lt; 2.0.0), devscripts (&lt;&lt; 2.10.26)
 Replaces: manpages-pl (&lt;= 20051117-1)
 Description: Debian package development tools
 This package provides the development tools (including dpkg-source)
 required to unpack, build and upload Debian source packages.
 .
 Most Debian source packages will require additional tools to build;
 for example, most packages need make and the C compiler gcc.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5), <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5), <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7), <code><a href="/docs/linux/man/1-dpkg-source/">dpkg-source</a></code>(1) </p>
