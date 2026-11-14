---
title: "dpkg-source(1)"
name: "dpkg-source"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-source/"
description: "dpkg-source – Debian source package (.dsc) manipulation tool"
---

<h2 class="name">NAME</h2>
<p> dpkg-source &#8211; Debian source package (.dsc) manipulation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-source</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-source</code> packs and unpacks Debian source archives. </p>
<p> None of these commands allow multiple options to be combined into one, and they do not allow the value for an option to be specified in a separate argument.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-x</code>, <code>&#8211;extract</code> <i>filename</i>.dsc [<i>output-directory</i>]</p>
<dd> Extract a source package (<code>&#8211;extract</code> since dpkg 1.17.14). One non-option argument must be supplied, the name of the Debian source control file (<code>.dsc</code>). An optional second non-option argument may be supplied to specify the directory to extract the source package to, this must not exist. If no output directory is specified, the source package is extracted into a directory named <i>source</i>&#8211;<i>version</i> under the current working directory. </p>
<p> <code>dpkg-source</code> will read the names of the other file(s) making up the source package from the control file; they are assumed to be in the same directory as the <code>.dsc</code>. </p>
<p> The files in the extracted package will have their permissions and ownerships set to those which would have been expected if the files and directories had simply been created &#8211; directories and executable files will be 0777 and plain files will be 0666, both modified by the extractors&#8217; umask; if the parent directory is setgid then the extracted directories will be too, and all the files and directories will inherit its group ownership. </p>
<p> If the source package uses a non-standard format (currently this means all formats except &#8220;1.0&#8221;), its name will be stored in <code>debian/source/format</code> so that the following builds of the source package use the same format by default.</p>
<dt><code>-b</code>, <code>&#8211;build</code> <i>directory</i> [<i>format-specific-parameters</i>]</p>
<dd> Build a source package (<code>&#8211;build</code> since dpkg 1.17.14). The first non-option argument is taken as the name of the directory containing the debianized source tree (i.e. with a debian sub-directory and maybe changes to the original files). Depending on the source package format used to build the package, additional parameters might be accepted. </p>
<p> <code>dpkg-source</code> will build the source package with the first format found in this ordered list: the format indicated with the <i>&#8211;format</i> command line option, the format indicated in <code>debian/source/format</code>, &#8220;1.0&#8221;. The fallback to &#8220;1.0&#8221; is deprecated and will be removed at some point in the future, you should always document the desired source format in <code>debian/source/format</code>. See section <font SIZE="-1"><code>SOURCE PACKAGE FORMATS</code></font> for an extensive description of the various source package formats.</p>
<dt><code>&#8211;print-format</code> <i>directory</i></p>
<dd> Print the source format that would be used to build the source package if <code>dpkg-source &#8211;build</code> <i>directory</i> was called (in the same conditions and with the same parameters; since dpkg 1.15.5).</p>
<dt><code>&#8211;before-build</code> <i>directory</i></p>
<dd> Run the corresponding hook of the source package format (since dpkg 1.15.8). This hook is called before any build of the package (<code>dpkg-buildpackage</code> calls it very early even before <code>debian/rules clean</code>). This command is idempotent and can be called multiple times. Not all source formats implement something in this hook, and those that do usually prepare the source tree for the build for example by ensuring that the Debian patches are applied.</p>
<dt><code>&#8211;after-build</code> <i>directory</i></p>
<dd> Run the corresponding hook of the source package format (since dpkg 1.15.8). This hook is called after any build of the package (<code>dpkg-buildpackage</code> calls it last). This command is idempotent and can be called multiple times. Not all source formats implement something in this hook, and those that do usually use it to undo what <code>&#8211;before-build</code> has done.</p>
<dt><code>&#8211;commit</code> [<i>directory</i>] &#8230;</p>
<dd> Record changes in the source tree unpacked in <i>directory</i> (since dpkg 1.16.1). This command can take supplementary parameters depending on the source format. It will error out for formats where this operation doesn&#8217;t mean anything.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit. The format specific build and extract options can be shown by using the <code>&#8211;format</code> option.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<h3>Generic build options</h3>
<dl>
<dt><code>-c</code><i>control-file</i></p>
<dd> Specifies the main source control file to read information from. The default is <code>debian/control</code>. If given with relative pathname this is interpreted starting at the source tree&#8217;s top level directory.</p>
<dt><code>-l</code><i>changelog-file</i></p>
<dd> Specifies the changelog file to read information from. The default is <code>debian/changelog</code>. If given with relative pathname this is interpreted starting at the source tree&#8217;s top level directory.</p>
<dt><code>-F</code><i>changelog-format</i></p>
<dd> Specifies the format of the changelog. See <code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1) for information about alternative formats.</p>
<dt><code>&#8211;format=</code><i>value</i></p>
<dd> Use the given format for building the source package (since dpkg 1.14.17). It does override any format given in <code>debian/source/format</code>.</p>
<dt><code>-V</code><i>name</i><code>=</code><i>value</i></p>
<dd> Set an output substitution variable. See <code><a href="/docs/linux/man/5-deb-substvars/">deb-substvars</a></code>(5) for a discussion of output substitution.</p>
<dt><code>-T</code><i>substvars-file</i></p>
<dd> Read substitution variables in <i>substvars-file</i>; the default is to not read any file. This option can be used multiple times to read substitution variables from multiple files (since dpkg 1.15.6).</p>
<dt><code>-D</code><i>field</i><code>=</code><i>value</i></p>
<dd> Override or add an output control file field.</p>
<dt><code>-U</code><i>field</i></p>
<dd> Remove an output control file field.</p>
<dt><code>-Z</code><i>compression</i>, <code>&#8211;compression</code>=<i>compression</i></p>
<dd> Specify the compression to use for created tarballs and diff files (<code>&#8211;compression</code> since dpkg 1.15.5). Note that this option will not cause existing tarballs to be recompressed, it only affects new files. Supported values are: <i>gzip</i>, <i>bzip2</i>, <i>lzma</i> and <i>xz</i>. The default is <i>xz</i> for formats 2.0 and newer, and <i>gzip</i> for format 1.0. <i>xz</i> is only supported since dpkg 1.15.5.</p>
<dt><code>-z</code><i>level</i>, <code>&#8211;compression-level</code>=<i>level</i></p>
<dd> Compression level to use (<code>&#8211;compression-level</code> since dpkg 1.15.5). As with <code>-Z</code> it only affects newly created files. Supported values are: <i>1</i> to <i>9</i>, <i>best</i>, and <i>fast</i>. The default is <i>9</i> for gzip and bzip2, <i>6</i> for xz and lzma.</p>
<dt><code>-i</code>[<i>regex</i>], <code>&#8211;diff-ignore</code>[=<i>regex</i>]</p>
<dd> You may specify a perl regular expression to match files you want filtered out of the list of files for the diff (<code>&#8211;diff-ignore</code> since dpkg 1.15.6). (This list is generated by a find command.) (If the source package is being built as a version 3 source package using a <font SIZE="-1">VCS,</font> this can be used to ignore uncommitted changes on specific files. Using -i.* will ignore all of them.) </p>
<p> The <code>-i</code> option by itself enables this setting with a default regex (preserving any modification to the default regex done by a previous use of <code>&#8211;extend-diff-ignore</code>) that will filter out control files and directories of the most common revision control systems, backup and swap files and Libtool build output directories. There can only be one active regex, of multiple <code>-i</code> options only the last one will take effect. </p>
<p> This is very helpful in cutting out extraneous files that get included in the diff, e.g. if you maintain your source in a revision control system and want to use a checkout to build a source package without including the additional files and directories that it will usually contain (e.g. <font SIZE="-1">CVS/,</font> .cvsignore, .svn/). The default regex is already very exhaustive, but if you need to replace it, please note that by default it can match any part of a path, so if you want to match the begin of a filename or only full filenames, you will need to provide the necessary anchors (e.g. &#8216;(^|/)&#8217;, &#8216;($|/)&#8217;) yourself.</p>
<dt><code>&#8211;extend-diff-ignore</code>=<i>regex</i></p>
<dd> The perl regular expression specified will extend the default value used by <code>&#8211;diff-ignore</code> and its current value, if set (since dpkg 1.15.6). It does this by concatenating &#8220;<code>|</code><i>regex</i>&#8221; to the existing value. This option is convenient to use in <code>debian/source/options</code> to exclude some auto-generated files from the automatic patch generation.</p>
<dt><code>-I</code>[<i>file-pattern</i>], <code>&#8211;tar-ignore</code>[=<i>file-pattern</i>]</p>
<dd> If this option is specified, the pattern will be passed to <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1)&#8217;s <code>&#8211;exclude</code> option when it is called to generate a .orig.tar or .tar file (<code>&#8211;tar-ignore</code> since dpkg 1.15.6). For example, <code>-I</code><font SIZE="-1">CVS</font> will make tar skip over <font SIZE="-1">CVS</font> directories when generating a .tar.gz file. The option may be repeated multiple times to list multiple patterns to exclude. </p>
<p> <code>-I</code> by itself adds default <code>&#8211;exclude</code> options that will filter out control files and directories of the most common revision control systems, backup and swap files and Libtool build output directories.</dl>
<p> <code>Note:</code> While they have similar purposes, <code>-i</code> and <code>-I</code> have very different syntax and semantics. <code>-i</code> can only be specified once and takes a perl compatible regular expression which is matched against the full relative path of each file. <code>-I</code> can specified multiple times and takes a filename pattern with shell wildcards. The pattern is applied to the full relative path but also to each part of the path individually. The exact semantic of tar&#8217;s <code>&#8211;exclude</code> option is somewhat complicated, see &lt;<a rel="nofollow" href="https://www.gnu.org/software/tar/manual/tar.html#wildcards">https://www.gnu.org/software/tar/manual/tar.html#wildcards</a>&gt; for a full documentation. </p>
<p> The default regex and patterns for both options can be seen in the output of the <code>&#8211;help</code> command.</p>
<h3>Generic extract options</h3>
<dl>
<dt><code>&#8211;no-copy</code></p>
<dd> Do not copy original tarballs near the extracted source package (since dpkg 1.14.17).</p>
<dt><code>&#8211;no-check</code></p>
<dd> Do not check signatures and checksums before unpacking (since dpkg 1.14.17).</p>
<dt><code>&#8211;no-overwrite-dir</code></p>
<dd> Do not overwrite the extraction directory if it already exists (since dpkg 1.18.8).</p>
<dt><code>&#8211;require-valid-signature</code></p>
<dd> Refuse to unpack the source package if it doesn&#8217;t contain an OpenPGP signature that can be verified (since dpkg 1.15.0) either with the user&#8217;s <i>trustedkeys.gpg</i> keyring, one of the vendor-specific keyrings, or one of the official Debian keyrings (<i>/usr/share/keyrings/debian-keyring.gpg</i>, <i>/usr/share/keyrings/debian-nonupload.gpg</i> and <i>/usr/share/keyrings/debian-maintainers.gpg</i>).</p>
<dt><code>&#8211;require-strong-checksums</code></p>
<dd> Refuse to unpack the source package if it does not contain any strong checksums (since dpkg 1.18.7). Currently the only known checksum considered strong is <font SIZE="-1"><code>SHA-256</code></font>.</p>
<dt><code>&#8211;ignore-bad-version</code></p>
<dd> Turns the bad source package version check into a non-fatal warning (since dpkg 1.17.7). This option should only be necessary when extracting ancient source packages with broken versions, just for backwards compatibility.</dl>
<h2>SOURCE PACKAGE FORMATS</h2>
<p> If you don&#8217;t know what source format to use, you should probably pick either &#8220;3.0 (quilt)&#8221; or &#8220;3.0 (native)&#8221;. See &lt;<a rel="nofollow" href="https://wiki.debian.org/Projects/DebSrc3.0">https://wiki.debian.org/Projects/DebSrc3.0</a>&gt; for information on the deployment of those formats within Debian.</p>
<h3>Format: 1.0</h3>
<p> A source package in this format consists either of a <code>.orig.tar.gz</code> associated to a <code>.diff.gz</code> or a single <code>.tar.gz</code> (in that case the package is said to be <i>native</i>). Optionally the original tarball might be accompanied by a detached upstream signature <code>.orig.tar.gz.asc</code>, extraction supported since dpkg 1.18.5. </p>
<p> <code>Extracting</code> </p>
<p> Extracting a native package is a simple extraction of the single tarball in the target directory. Extracting a non-native package is done by first unpacking the <code>.orig.tar.gz</code> and then applying the patch contained in the <code>.diff.gz</code> file. The timestamp of all patched files is reset to the extraction time of the source package (this avoids timestamp skews leading to problems when autogenerated files are patched). The diff can create new files (the whole debian directory is created that way) but cannot remove files (empty files will be left over) and cannot create or change symlinks. </p>
<p> <code>Building</code> </p>
<p> Building a native package is just creating a single tarball with the source directory. Building a non-native package involves extracting the original tarball in a separate &#8220;.orig&#8221; directory and regenerating the <code>.diff.gz</code> by comparing the source package <i>directory</i> with the .orig directory. </p>
<p> <code>Build options (with &#8211;build):</code> </p>
<p> If a second non-option argument is supplied it should be the name of the original source directory or tarfile or the empty string if the package is a Debian-specific one and so has no debianization diffs. If no second argument is supplied then <code>dpkg-source</code> will look for the original source tarfile <i>package</i><code>_</code><i>upstream-version</i><code>.orig.tar.gz</code> or the original source directory <i>directory</i><code>.orig</code> depending on the <code>-sX</code> arguments. </p>
<p> <code>-sa</code>, <code>-sp</code>, <code>-sk</code>, <code>-su</code> and <code>-sr</code> will not overwrite existing tarfiles or directories. If this is desired then <code>-sA</code>, <code>-sP</code>, <code>-sK</code>, <code>-sU</code> and <code>-sR</code> should be used instead.</p>
<dl>
<dt><code>-sk</code></p>
<dd> Specifies to expect the original source as a tarfile, by default <i>package</i><code>_</code><i>upstream-version</i><code>.orig.tar.</code><i>extension</i>. It will leave this original source in place as a tarfile, or copy it to the current directory if it isn&#8217;t already there. The tarball will be unpacked into <i>directory</i><code>.orig</code> for the generation of the diff.</p>
<dt><code>-sp</code></p>
<dd> Like <code>-sk</code> but will remove the directory again afterwards.</p>
<dt><code>-su</code></p>
<dd> Specifies that the original source is expected as a directory, by default <i>package</i><code>&#8211;</code><i>upstream-version</i><code>.orig</code> and <code>dpkg-source</code> will create a new original source archive from it.</p>
<dt><code>-sr</code></p>
<dd> Like <code>-su</code> but will remove that directory after it has been used.</p>
<dt><code>-ss</code></p>
<dd> Specifies that the original source is available both as a directory and as a tarfile. <code>dpkg-source</code> will use the directory to create the diff, but the tarfile to create the <code>.dsc</code>. This option must be used with care &#8211; if the directory and tarfile do not match a bad source archive will be generated.</p>
<dt><code>-sn</code></p>
<dd> Specifies to not look for any original source, and to not generate a diff. The second argument, if supplied, must be the empty string. This is used for Debian-specific packages which do not have a separate upstream source and therefore have no debianization diffs.</p>
<dt><code>-sa</code> or <code>-sA</code></p>
<dd> Specifies to look for the original source archive as a tarfile or as a directory &#8211; the second argument, if any, may be either, or the empty string (this is equivalent to using <code>-sn</code>). If a tarfile is found it will unpack it to create the diff and remove it afterwards (this is equivalent to <code>-sp</code>); if a directory is found it will pack it to create the original source and remove it afterwards (this is equivalent to <code>-sr</code>); if neither is found it will assume that the package has no debianization diffs, only a straightforward source archive (this is equivalent to <code>-sn</code>). If both are found then <code>dpkg-source</code> will ignore the directory, overwriting it, if <code>-sA</code> was specified (this is equivalent to <code>-sP</code>) or raise an error if <code>-sa</code> was specified. <code>-sa</code> is the default.</p>
<dt><code>&#8211;abort-on-upstream-changes</code></p>
<dd> The process fails if the generated diff contains changes to files outside of the debian sub-directory (since dpkg 1.15.8). This option is not allowed in <code>debian/source/options</code> but can be used in <code>debian/source/local-options</code>.</dl>
<p> <code>Extract options (with &#8211;extract):</code> </p>
<p> In all cases any existing original source tree will be removed.</p>
<dl>
<dt><code>-sp</code></p>
<dd> Used when extracting then the original source (if any) will be left as a tarfile. If it is not already located in the current directory or if an existing but different file is there it will be copied there. (<code>This is the default</code>).</p>
<dt><code>-su</code></p>
<dd> Unpacks the original source tree.</p>
<dt><code>-sn</code></p>
<dd> Ensures that the original source is neither copied to the current directory nor unpacked. Any original source tree that was in the current directory is still removed.</dl>
<p> All the <code>-s</code><i>X</i> options are mutually exclusive. If you specify more than one only the last one will be used.</p>
<dl>
<dt><code>&#8211;skip-debianization</code></p>
<dd> Skips application of the debian diff on top of the upstream sources (since dpkg 1.15.1).</dl>
<h3>Format: 2.0</h3>
<p> Extraction supported since dpkg 1.13.9, building supported since dpkg 1.14.8. Also known as wig&amp;pen. This format is not recommended for wide-spread usage, the format &#8220;3.0 (quilt)&#8221; replaces it. Wig&amp;pen was the first specification of a new-generation source package format. </p>
<p> The behaviour of this format is the same as the &#8220;3.0 (quilt)&#8221; format except that it doesn&#8217;t use an explicit list of patches. All files in <code>debian/patches/</code> matching the perl regular expression <code>[\w-]+</code> must be valid patches: they are applied at extraction time. </p>
<p> When building a new source package, any change to the upstream source is stored in a patch named <code>zz_debian-diff-auto</code>.</p>
<h3>Format: 3.0 (native)</h3>
<p> Supported since dpkg 1.14.17. This format is an extension of the native package format as defined in the 1.0 format. It supports all compression methods and will ignore by default any <font SIZE="-1">VCS</font> specific files and directories as well as many temporary files (see default value associated to <code>-I</code> option in the <code>&#8211;help</code> output).</p>
<h3>Format: 3.0 (quilt)</h3>
<p> Supported since dpkg 1.14.17. A source package in this format contains at least an original tarball (<code>.orig.tar.</code><i>ext</i> where <i>ext</i> can be <code>gz</code>, <code>bz2</code>, <code>lzma</code> and <code>xz</code>) and a debian tarball (<code>.debian.tar.</code><i>ext</i>). It can also contain additional original tarballs (<code>.orig-</code><i>component</i><code>.tar.</code><i>ext</i>). <i>component</i> can only contain alphanumeric (&#8216;a-zA-Z0-9&#8217;) characters and hyphens (&#8216;-&#8216;). Optionally each original tarball can be accompanied by a detached upstream signature (<code>.orig.tar.</code><i>ext</i><code>.asc</code> and <code>.orig-</code><i>component</i><code>.tar.</code><i>ext</i><code>.asc</code>), extraction supported since dpkg 1.17.20, building supported since dpkg 1.18.5. </p>
<p> <code>Extracting</code> </p>
<p> The main original tarball is extracted first, then all additional original tarballs are extracted in subdirectories named after the <i>component</i> part of their filename (any pre-existing directory is replaced). The debian tarball is extracted on top of the source directory after prior removal of any pre-existing <code>debian</code> directory. Note that the debian tarball must contain a <code>debian</code> sub-directory but it can also contain binary files outside of that directory (see <code>&#8211;include-binaries</code> option). </p>
<p> All patches listed in <code>debian/patches/</code><i>vendor</i><code>.series</code> or <code>debian/patches/series</code> are then applied, where <i>vendor</i> will be the lowercase name of the current vendor, or <code>debian</code> if there is no vendor defined. If the former file is used and the latter one doesn&#8217;t exist (or is a symlink), then the latter is replaced with a symlink to the former. This is meant to simplify usage of <code>quilt</code> to manage the set of patches. Vendor-specific series files are intended to make it possible to serialize multiple development branches based on the vendor, in a declarative way, in preference to open-coding this handling in <code>debian/rules</code>. This is particularly useful when the source would need to be patched conditionally because the affected files do not have built-in conditional occlusion support. Note however that while <code>dpkg-source</code> parses correctly series files with explicit options used for patch application (stored on each line after the patch filename and one or more spaces), it does ignore those options and always expects patches that can be applied with the <code>-p1</code> option of <code>patch</code>. It will thus emit a warning when it encounters such options, and the build is likely to fail. </p>
<p> Note that <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) will emit unconditional warnings when using vendor series due to a controversial Debian specific ruling, which should not affect any external usage; to silence these, the dpkg lintian profile can be used by passing &laquo;<code>&#8211;profile dpkg</code>&raquo; to <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1). </p>
<p> The timestamp of all patched files is reset to the extraction time of the source package (this avoids timestamp skews leading to problems when autogenerated files are patched). </p>
<p> Contrary to <code>quilt</code>&#8216;s default behaviour, patches are expected to apply without any fuzz. When that is not the case, you should refresh such patches with <code>quilt</code>, or <code>dpkg-source</code> will error out while trying to apply them. </p>
<p> Similarly to <code>quilt</code>&#8216;s default behaviour, the patches can remove files too. </p>
<p> The file <code>.pc/applied-patches</code> is created if some patches have been applied during the extraction. </p>
<p> <code>Building</code> </p>
<p> All original tarballs found in the current directory are extracted in a temporary directory by following the same logic as for the unpack, the debian directory is copied over in the temporary directory, and all patches except the automatic patch (<code>debian-changes-</code><i>version</i> or <code>debian-changes</code>, depending on <code>&#8211;single-debian-patch</code>) are applied. The temporary directory is compared to the source package directory. When the diff is non-empty, the build fails unless <code>&#8211;single-debian-patch</code> or <code>&#8211;auto-commit</code> has been used, in which case the diff is stored in the automatic patch. If the automatic patch is created/deleted, it&#8217;s added/removed from the series file and from the <code>quilt</code> metadata. </p>
<p> Any change on a binary file is not representable in a diff and will thus lead to a failure unless the maintainer deliberately decided to include that modified binary file in the debian tarball (by listing it in <code>debian/source/include-binaries</code>). The build will also fail if it finds binary files in the debian sub-directory unless they have been allowed through <code>debian/source/include-binaries</code>. </p>
<p> The updated debian directory and the list of modified binaries is then used to generate the debian tarball. </p>
<p> The automatically generated diff doesn&#8217;t include changes on <font SIZE="-1">VCS</font> specific files as well as many temporary files (see default value associated to <code>-i</code> option in the <code>&#8211;help</code> output). In particular, the <code>.pc</code> directory used by <code>quilt</code> is ignored during generation of the automatic patch. </p>
<p> <code>Note:</code> <code>dpkg-source</code> <code>&#8211;before-build</code> (and <code>&#8211;build</code>) will ensure that all patches listed in the series file are applied so that a package build always has all patches applied. It does this by finding unapplied patches (they are listed in the <code>series</code> file but not in <code>.pc/applied-patches</code>), and if the first patch in that set can be applied without errors, it will apply them all. The option <code>&#8211;no-preparation</code> can be used to disable this behavior. </p>
<p> <code>Recording changes</code></p>
<dl>
<dt><code>&#8211;commit</code> [<i>directory</i>] [<i>patch-name</i>] [<i>patch-file</i>]</p>
<dd> Generates a patch corresponding to the local changes that are not managed by the <code>quilt</code> patch system and integrates it in the patch system under the name <i>patch-name</i>. If the name is missing, it will be asked interactively. If <i>patch-file</i> is given, it is used as the patch corresponding to the local changes to integrate. Once integrated, an editor is launched so that you can edit the meta-information in the patch header. </p>
<p> Passing <i>patch-file</i> is mainly useful after a build failure that pre-generated this file, and on this ground the given file is removed after integration. Note also that the changes contained in the patch file must already be applied on the tree and that the files modified by the patch must not have supplementary unrecorded changes. </p>
<p> If the patch generation detects modified binary files, they will be automatically added to <code>debian/source/include-binaries</code> so that they end up in the debian tarball (exactly like <code>dpkg-source &#8211;include-binaries &#8211;build</code> would do).</dl>
<p> <code>Build options</code></p>
<dl>
<dt><code>&#8211;allow-version-of-quilt-db=</code><i>version</i></p>
<dd> Allow <code>dpkg-source</code> to build the source package if the version of the <code>quilt</code> metadata is the one specified, even if <code>dpkg-source</code> doesn&#8217;t know about it (since dpkg 1.15.5.4). Effectively this says that the given version of the <code>quilt</code> metadata is compatible with the version 2 that <code>dpkg-source</code> currently supports. The version of the <code>quilt</code> metadata is stored in <code>.pc/.version</code>.</p>
<dt><code>&#8211;include-removal</code></p>
<dd> Do not ignore removed files and include them in the automatically generated patch.</p>
<dt><code>&#8211;include-timestamp</code></p>
<dd> Include timestamp in the automatically generated patch.</p>
<dt><code>&#8211;include-binaries</code></p>
<dd> Add all modified binaries in the debian tarball. Also add them to <code>debian/source/include-binaries</code>: they will be added by default in subsequent builds and this option is thus no more needed.</p>
<dt><code>&#8211;no-preparation</code></p>
<dd> Do not try to prepare the build tree by applying patches which are apparently unapplied (since dpkg 1.14.18).</p>
<dt><code>&#8211;single-debian-patch</code></p>
<dd> Use <code>debian/patches/debian-changes</code> instead of <code>debian/patches/debian-changes-</code><i>version</i> for the name of the automatic patch generated during build (since dpkg 1.15.5.4). This option is particularly useful when the package is maintained in a <font SIZE="-1">VCS</font> and a patch set can&#8217;t reliably be generated. Instead the current diff with upstream should be stored in a single patch. The option would be put in <code>debian/source/local-options</code> and would be accompanied by a <code>debian/source/local-patch-header</code> file explaining how the Debian changes can be best reviewed, for example in the <font SIZE="-1">VCS</font> that is used.</p>
<dt><code>&#8211;create-empty-orig</code></p>
<dd> Automatically create the main original tarball as empty if it&#8217;s missing and if there are supplementary original tarballs (since dpkg 1.15.6). This option is meant to be used when the source package is just a bundle of multiple upstream software and where there&#8217;s no &#8220;main&#8221; software.</p>
<dt><code>&#8211;no-unapply-patches, &#8211;unapply-patches</code></p>
<dd> By default, <code>dpkg-source</code> will automatically unapply the patches in the <code>&#8211;after-build</code> hook if it did apply them during <code>&#8211;before-build</code> (<code>&#8211;unapply-patches</code> since dpkg 1.15.8, <code>&#8211;no-unapply-patches</code> since dpkg 1.16.5). Those options allow you to forcefully disable or enable the patch unapplication process. Those options are only allowed in <code>debian/source/local-options</code> so that all generated source packages have the same behavior by default.</p>
<dt><code>&#8211;abort-on-upstream-changes</code></p>
<dd> The process fails if an automatic patch has been generated (since dpkg 1.15.8). This option can be used to ensure that all changes were properly recorded in separate <code>quilt</code> patches prior to the source package build. This option is not allowed in <code>debian/source/options</code> but can be used in <code>debian/source/local-options</code>.</p>
<dt><code>&#8211;auto-commit</code></p>
<dd> The process doesn&#8217;t fail if an automatic patch has been generated, instead it&#8217;s immediately recorded in the <code>quilt</code> series.</dl>
<p> <code>Extract options</code></p>
<dl>
<dt><code>&#8211;skip-debianization</code></p>
<dd> Skips extraction of the debian tarball on top of the upstream sources (since dpkg 1.15.1).</p>
<dt><code>&#8211;skip-patches</code></p>
<dd> Do not apply patches at the end of the extraction (since dpkg 1.14.18).</dl>
<h3>Format: 3.0 (custom)</h3>
<p> Supported since dpkg 1.14.17. This format is special. It doesn&#8217;t represent a real source package format but can be used to create source packages with arbitrary files. </p>
<p> <code>Build options</code> </p>
<p> All non-option arguments are taken as files to integrate in the generated source package. They must exist and are preferably in the current directory. At least one file must be given.</p>
<dl>
<dt><code>&#8211;target-format=</code><i>value</i></p>
<dd> <code>Required</code>. Defines the real format of the generated source package. The generated .dsc file will contain this value in its <code>Format</code> field and not &#8220;3.0 (custom)&#8221;.</dl>
<h3>Format: 3.0 (git)</h3>
<p> Supported since dpkg 1.14.17. This format is experimental. </p>
<p> A source package in this format consists of a single bundle of a git repository <code>.git</code> to hold the source of a package. There may also be a <code>.gitshallow</code> file listing revisions for a shallow git clone. </p>
<p> <code>Extracting</code> </p>
<p> The bundle is cloned as a git repository to the target directory. If there is a gitshallow file, it is installed as <i>.git/shallow</i> inside the cloned git repository. </p>
<p> Note that by default the new repository will have the same branch checked out that was checked out in the original source. (Typically &#8220;master&#8221;, but it could be anything.) Any other branches will be available under <i>remotes/origin/</i>. </p>
<p> <code>Building</code> </p>
<p> Before going any further, some checks are done to ensure that we don&#8217;t have any non-ignored uncommitted changes. </p>
<p> <code><a href="/docs/linux/man/1-git-bundle/">git-bundle</a></code>(1) is used to generate a bundle of the git repository. By default, all branches and tags in the repository are included in the bundle. </p>
<p> <code>Build options</code></p>
<dl>
<dt><code>&#8211;git-ref=</code><i>ref</i></p>
<dd> Allows specifying a git ref to include in the git bundle. Use disables the default behavior of including all branches and tags. May be specified multiple times. The <i>ref</i> can be the name of a branch or tag to include. It may also be any parameter that can be passed to <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1). For example, to include only the master branch, use <code>&#8211;git-ref=</code>master. To include all tags and branches, except for the private branch, use <code>&#8211;git-ref=</code>&#8211;all <code>&#8211;git-ref=</code>^private</p>
<dt><code>&#8211;git-depth=</code><i>number</i></p>
<dd> Creates a shallow clone with a history truncated to the specified number of revisions.</dl>
<h3>Format: 3.0 (bzr)</h3>
<p> Supported since dpkg 1.14.17. This format is experimental. It generates a single tarball containing the bzr repository. </p>
<p> <code>Extracting</code> </p>
<p> The tarball is unpacked and then bzr is used to checkout the current branch. </p>
<p> <code>Building</code> </p>
<p> Before going any further, some checks are done to ensure that we don&#8217;t have any non-ignored uncommitted changes. </p>
<p> Then the <font SIZE="-1">VCS</font> specific part of the source directory is copied over to a temporary directory. Before this temporary directory is packed in a tarball, various cleanup are done to save space.</p>
<h2>DIAGNOSTICS</h2>
<h3>no source format specified in debian/source/format</h3>
<p> The file <code>debian/source/format</code> should always exist and indicate the desired source format. For backwards compatibility, format &#8220;1.0&#8221; is assumed when the file doesn&#8217;t exist but you should not rely on this: at some point in the future <code>dpkg-source</code> will be modified to fail when that file doesn&#8217;t exist. </p>
<p> The rationale is that format &#8220;1.0&#8221; is no longer the recommended format, you should usually pick one of the newer formats (&#8220;3.0 (quilt)&#8221;, &#8220;3.0 (native)&#8221;) but <code>dpkg-source</code> will not do this automatically for you. If you want to continue using the old format, you should be explicit about it and put &#8220;1.0&#8221; in <code>debian/source/format</code>.</p>
<h3>the diff modifies the following upstream files</h3>
<p> When using source format &#8220;1.0&#8221; it is usually a bad idea to modify upstream files directly as the changes end up hidden and mostly undocumented in the .diff.gz file. Instead you should store your changes as patches in the debian directory and apply them at build-time. To avoid this complexity you can also use the format &#8220;3.0 (quilt)&#8221; that offers this natively.</p>
<h3>cannot represent change to <i>file</i></h3>
<p> Changes to upstream sources are usually stored with patch files, but not all changes can be represented with patches: they can only alter the content of plain text files. If you try replacing a file with something of a different type (for example replacing a plain file with a symlink or a directory), you will get this error message.</p>
<h3>newly created empty file <i>file</i> will not be represented in diff</h3>
<p> Empty files can&#8217;t be created with patch files. Thus this change is not recorded in the source package and you are warned about it.</p>
<h3>executable mode <i>perms</i> of <i>file</i> will not be represented in diff</h3>
<p> Patch files do not record permissions of files and thus executable permissions are not stored in the source package. This warning reminds you of that fact.</p>
<h3>special mode <i>perms</i> of <i>file</i> will not be represented in diff</h3>
<p> Patch files do not record permissions of files and thus modified permissions are not stored in the source package. This warning reminds you of that fact.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</p>
<dt><font SIZE="-1"><code>SOURCE_DATE_EPOCH</code></font></p>
<dd> If set, it will be used as the timestamp (as seconds since the epoch) to clamp the mtime in the <code><a href="/docs/linux/man/5-tar/">tar</a></code>(5) file entries.</p>
<dt><font SIZE="-1"><code>VISUAL</code></font></p>
<dd>
<dt><font SIZE="-1"><code>EDITOR</code></font></p>
<dd> Used by the &#8220;2.0&#8221; and &#8220;3.0 (quilt)&#8221; source format modules.</p>
<dt><font SIZE="-1"><code>GIT_DIR</code></font></p>
<dd>
<dt><font SIZE="-1"><code>GIT_INDEX_FILE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>GIT_OBJECT_DIRECTORY</code></font></p>
<dd>
<dt><font SIZE="-1"><code>GIT_ALTERNATE_OBJECT_DIRECTORIES</code></font></p>
<dd>
<dt><font SIZE="-1"><code>GIT_WORK_TREE</code></font></p>
<dd> Used by the &#8220;3.0 (git)&#8221; source format modules.</dl>
<h2>FILES</h2>
<h3>debian/source/format</h3>
<p> This file contains on a single line the format that should be used to build the source package (possible formats are described above). No leading or trailing spaces are allowed.</p>
<h3>debian/source/include-binaries</h3>
<p> This file contains a list of pathnames of binary files (one per line) relative to the source root directory that should be included in the debian tarball. Leading and trailing spaces are stripped. Lines starting with &#8216;<code>#</code>&#8216; are comments and are skipped. Empty lines are ignored.</p>
<h3>debian/source/options</h3>
<p> This file contains a list of long options that should be automatically prepended to the set of command line options of a <code>dpkg-source &#8211;build</code> or <code>dpkg-source &#8211;print-format</code> call. Options like <code>&#8211;compression</code> and <code>&#8211;compression-level</code> are well suited for this file. </p>
<p> Each option should be put on a separate line. Empty lines and lines starting with &#8216;<code>#</code>&#8216; are ignored. The leading &#8216;<code>&#8212;</code>&#8216; should be stripped and short options are not allowed. Optional spaces are allowed around the &#8216;<code>=</code>&#8216; symbol and optional quotes are allowed around the value. Here&#8217;s an example of such a file: </p>
<pre>
 # let dpkg-source create a debian.tar.bz2 with maximal compression
 compression = &quot;bzip2&quot;
 compression-level = 9
 # use debian/patches/debian-changes as automatic patch
 single-debian-patch
 # ignore changes on config.{sub,guess}
 extend-diff-ignore = &quot;(^|/)(config.sub|config.guess)$&quot;
</pre>
<p> <code>Note:</code> <code>format</code> options are not accepted in this file, you should use <code>debian/source/format</code> instead.</p>
<h3>debian/source/local-options</h3>
<p> Exactly like <code>debian/source/options</code> except that the file is not included in the generated source package. It can be useful to store a preference tied to the maintainer or to the <font SIZE="-1">VCS</font> repository where the source package is maintained.</p>
<h3>debian/source/local-patch-header</h3>
<h3>debian/source/patch-header</h3>
<p> Free form text that is put on top of the automatic patch generated in formats &#8220;2.0&#8221; or &#8220;3.0 (quilt)&#8221;. <code>local-patch-header</code> is not included in the generated source package while <code>patch-header</code> is.</p>
<h3>debian/patches/<i>vendor</i>.series</h3>
<h3>debian/patches/series</h3>
<p> This file lists all patches that have to be applied (in the given order) on top of the upstream source package. Leading and trailing spaces are stripped. The <i>vendor</i> will be the lowercase name of the current vendor, or <code>debian</code> if there is no vendor defined. If the vendor-specific series file does not exist, the vendor-less series file will be used. Lines starting with &#8216;<code>#</code>&#8216; are comments and are skipped. Empty lines are ignored. Remaining lines start with a patch filename (relative to the <code>debian/patches/</code> directory) up to the first space character or the end of line. Optional <code>quilt</code> options can follow up to the end of line or the first &#8216;<code>#</code>&#8216; preceded by one or more spaces (which marks the start of a comment up to the end of line).</p>
<h2>BUGS</h2>
<p> The point at which field overriding occurs compared to certain standard output field settings is rather confused.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5), <code><a href="/docs/linux/man/5-deb-changelog/">deb-changelog</a></code>(5), <code><a href="/docs/linux/man/5-dsc/">dsc</a></code>(5). </p>
<h2>Index</h2>
<dt><a href="#lbAX">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAY">FILES</a></p>
<dd>
<dt><a href="#lbBH">BUGS</a></p>
<dd>
<dt><a href="#lbBI">SEE ALSO</a></p>
<dd></dl>
