---
title: "rpm(8)"
name: "rpm"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpm/"
description: "rpm – RPM Package Manager"
---

<p>rpm &#8211; RPM Package Manager</p>
<h2>Synopsis</h2>
<h3>Querying And Verifying Packages:</h3>
<p><code>rpm</code> {<code>-q|&#8211;query</code>} [<code>select-options</code>] [<code>query-options</code>] <code>rpm</code> {<code>-V|&#8211;verify</code>} [<code>select-options</code>] [<code>verify-options</code>]</p>
<h3>Installing, Upgrading, And Removing Packages:</h3>
<p><code>rpm</code> {<code>-i|&#8211;install</code>} [<code>install-options</code>] <i>PACKAGE_FILE</i><i> &#8230;</i> <code>rpm</code> {<code>-U|&#8211;upgrade</code>} [<code>install-options</code>] <i>PACKAGE_FILE</i><i> &#8230;</i> <code>rpm</code> {<code>-F|&#8211;freshen</code>} [<code>install-options</code>] <i>PACKAGE_FILE</i><i> &#8230;</i> <code>rpm</code> {<code>-e|&#8211;erase</code>} [<code>&#8211;allmatches</code>] [<code>&#8211;justdb] [&#8211;nodeps</code>] [<code>&#8211;noscripts</code>]<br />
&nbsp;<wbr>[<code>&#8211;notriggers</code>]&nbsp;<wbr>[<code>&#8211;test</code>]&nbsp;<wbr><i>PACKAGE_NAME</i><i>&nbsp;<wbr>&#8230;</i></p>
<h3>Miscellaneous:</h3>
<p><code>rpm</code> {<code>&#8211;querytags|&#8211;showrc</code>} <code>rpm</code> {<code>&#8211;setperms|&#8211;setugids</code>} <i>PACKAGE_NAME</i><i> &#8230;</i></p>
<h3>select-options</h3>
<p>&nbsp;<wbr>[<i>PACKAGE_NAME</i>]&nbsp;<wbr>[<code>-a,&#8211;all</code>]&nbsp;<wbr>[<code>-f,&#8211;file&nbsp;<wbr></code><i>FILE</i>]<br />
&nbsp;<wbr>[<code>-g,&#8211;group&nbsp;<wbr></code><i>GROUP</i>]&nbsp;<wbr>{<code>-p,&#8211;package&nbsp;<wbr></code><i>PACKAGE_FILE</i>]<br />
&nbsp;<wbr>[<code>&#8211;hdrid&nbsp;<wbr></code><i>SHA1</i>]&nbsp;<wbr>[<code>&#8211;pkgid&nbsp;<wbr></code><i>MD5</i>]&nbsp;<wbr>[<code>&#8211;tid&nbsp;<wbr></code><i>TID</i>]<br />
&nbsp;<wbr>[<code>&#8211;querybynumber&nbsp;<wbr></code><i>HDRNUM</i>]&nbsp;<wbr>[<code>&#8211;triggeredby&nbsp;<wbr></code><i>PACKAGE_NAME</i>]<br />
&nbsp;<wbr>[<code>&#8211;whatprovides&nbsp;<wbr></code><i>CAPABILITY</i>]&nbsp;<wbr>[<code>&#8211;whatrequires&nbsp;<wbr></code><i>CAPABILITY</i>]</p>
<h3>query-options</h3>
<p>&nbsp;<wbr>[<code>&#8211;changelog</code>]&nbsp;<wbr>[<code>-c,&#8211;configfiles</code>]&nbsp;<wbr>[<code>&#8211;conflicts</code>]<br />
&nbsp;<wbr>[<code>-d,&#8211;docfiles</code>]&nbsp;<wbr>[<code>&#8211;dump</code>]&nbsp;<wbr>[<code>&#8211;filesbypkg</code>]&nbsp;<wbr>[<code>-i,&#8211;info</code>]<br />
&nbsp;<wbr>[<code>&#8211;last</code>]&nbsp;<wbr>[<code>-l,&#8211;list</code>]&nbsp;<wbr>[<code>&#8211;obsoletes</code>]&nbsp;<wbr>[<code>&#8211;provides</code>]<br />
&nbsp;<wbr>[<code>&#8211;qf,&#8211;queryformat&nbsp;<wbr></code><i>QUERYFMT</i>]&nbsp;<wbr>[<code>-R,&#8211;requires</code>]<br />
&nbsp;<wbr>[<code>&#8211;scripts</code>]&nbsp;<wbr>[<code>-s,&#8211;state</code>]&nbsp;<wbr>[<code>&#8211;triggers,&#8211;triggerscripts</code>]</p>
<h3>verify-options</h3>
<p>&nbsp;<wbr>[<code>&#8211;nodeps</code>]&nbsp;<wbr>[<code>&#8211;nofiles</code>]&nbsp;<wbr>[<code>&#8211;noscripts</code>]<br />
&nbsp;<wbr>[<code>&#8211;nodigest</code>]&nbsp;<wbr>[<code>&#8211;nosignature</code>]<br />
&nbsp;<wbr>[<code>&#8211;nolinkto</code>]&nbsp;<wbr>[<code>&#8211;nofiledigest</code>]&nbsp;<wbr>[<code>&#8211;nosize</code>]&nbsp;<wbr>[<code>&#8211;nouser</code>]<br />
&nbsp;<wbr>[<code>&#8211;nogroup</code>]&nbsp;<wbr>[<code>&#8211;nomtime</code>]&nbsp;<wbr>[<code>&#8211;nomode</code>]&nbsp;<wbr>[<code>&#8211;nordev</code>]<br />
&nbsp;<wbr>[<code>&#8211;nocaps</code>]</p>
<h3>install-options</h3>
<pre><code>[--allfiles] [--badreloc] [--excludepath OLDPATH]
[--excludedocs] [--force] [-h,--hash]
[--ignoresize] [--ignorearch] [--ignoreos]
[--includedocs] [--justdb] [--nocollections]
[--nodeps] [--nodigest] [--nosignature] [--noplugins]
[--noorder] [--noscripts] [--notriggers]
[--oldpackage] [--percent] [--prefix NEWPATH]
[--relocate OLDPATH=NEWPATH]
[--replacefiles] [--replacepkgs]
[--test]
</code></pre>
<h2>Description</h2>
<p><code>rpm</code> is a powerful <code>Package Manager</code>, which can be used to build, install, query, verify, update, and erase individual software packages. A <code>package</code> consists of an archive of files and meta-data used to install and erase the archive files. The meta-data includes helper scripts, file attributes, and descriptive information about the package. <code>Packages</code> come in two varieties: binary packages, used to encapsulate software to be installed, and source packages, containing the source code and recipe necessary to produce binary packages. One of the following basic modes must be selected: <code>Query</code>, <code>Verify</code>, <code>Install/Upgrade/Freshen</code>, <code>Uninstall</code>, <code>Set Owners/Groups</code>, <code>Show Querytags</code>, and <code>Show Configuration</code>.</p>
<h3>General Options</h3>
<p>These options can be used in all the different modes.</p>
<dl>
<dt><code>-?, &#8211;help</code></dt>
<dd>Print a longer usage message then normal.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Print a single line containing the version number of <code>rpm</code> being used.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd>Print as little as possible &#8211; normally only error messages will be displayed.</dd>
<dt><code>-v</code></dt>
<dd>Print verbose information &#8211; normally routine progress messages will be displayed.</dd>
<dt><code>-vv</code></dt>
<dd>Print lots of ugly debugging information.</dd>
<dt><code>&#8211;rcfile </code><i>FILELIST</i></dt>
<dd>Each of the files in the colon separated <i>FILELIST</i> is read sequentially by <code>rpm</code> for configuration information. Only the first file in the list must exist, and tildes will be expanded to the value of <code>$HOME</code>. The default <i>FILELIST</i> is <i>/usr/lib/rpm/rpmrc</i>:<i>/usr/lib/rpm/redhat/rpmrc</i>:<i>/etc/rpmrc</i>:<i>~/.rpmrc</i>.</dd>
<dt><code>&#8211;pipe </code><i>CMD</i></dt>
<dd>Pipes the output of <code>rpm</code> to the command <i>CMD</i>.</dd>
<dt><code>&#8211;dbpath </code><i>DIRECTORY</i></dt>
<dd>Use the database in <i>DIRECTORY</i> rather than the default path <i>/var/lib/rpm</i></dd>
<dt><code>&#8211;root </code><i>DIRECTORY</i></dt>
<dd>Use the file system tree rooted at <i>DIRECTORY</i> for all operations. Note that this means the database within <i>DIRECTORY</i> will be used for dependency checks and any scriptlet(s) (e.g. <code>%post</code> if installing, or <code>%prep</code> if building, a package) will be run after a <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to <i>DIRECTORY</i>.</dd>
<dt><code>-D, &#8211;define=&#8217;</code><i>MACRO EXPR</i><code>&#8216;</code></dt>
<dd>Defines <i>MACRO</i> with value <i>EXPR</i>.</dd>
<dt><code>&#8211;undefine=&#8217;</code><i>MACRO</i><code>&#8216;</code></dt>
<dd>Undefines <i>MACRO</i>.</dd>
<dt><code>-E, &#8211;eval=&#8217;</code><i>EXPR</i><code>&#8216;</code></dt>
<dd>Prints macro expansion of <i>EXPR</i>.</dd></dl>
<h3>Install And Upgrade Options</h3>
<p>In these options, <i>PACKAGE_FILE</i> can be either <code>rpm</code> binary file or ASCII package manifest (see <code>PACKAGE SELECTION OPTIONS</code>), and may be specified as an <code>ftp</code> or <code>http</code> URL, in which case the package will be downloaded before being installed. See <code>FTP/HTTP OPTIONS</code> for information on <code>rpm</code>&#8216;s internal <code>ftp</code> and <code>http</code> client support. The general form of an rpm install command is <code>rpm</code> {<code>-i|&#8211;install</code>} [<code>install-options</code>] <i>PACKAGE_FILE</i><i> &#8230;</i> This installs a new package. The general form of an rpm upgrade command is <code>rpm</code> {<code>-U|&#8211;upgrade</code>} [<code>install-options</code>] <i>PACKAGE_FILE</i><i> &#8230;</i> This upgrades or installs the package currently installed to a newer version. This is the same as install, except all other version(s) of the package are removed after the new package is installed. <code>rpm</code> {<code>-F|&#8211;freshen</code>} [<code>install-options</code>] <i>PACKAGE_FILE</i><i> &#8230;</i> This will upgrade packages, but only ones for which an earlier version is installed.</p>
<dl>
<dt><code>&#8211;allfiles</code></dt>
<dd>Installs or upgrades all the missingok files in the package, regardless if they exist.</dd>
<dt><code>&#8211;badreloc</code></dt>
<dd>Used with <code>&#8211;relocate</code>, permit relocations on all file paths, not just those <i>OLDPATH</i>&#8216;s included in the binary package relocation hint(s).</dd>
<dt><code>&#8211;excludepath </code><i>OLDPATH</i></dt>
<dd>Don&#8217;t install files whose name begins with <i>OLDPATH</i>.</dd>
<dt><code>&#8211;excludedocs</code></dt>
<dd>Don&#8217;t install any files which are marked as documentation (which includes man pages and texinfo documents).</dd>
<dt><code>&#8211;force</code></dt>
<dd>Same as using <code>&#8211;replacepkgs</code>, <code>&#8211;replacefiles</code>, and <code>&#8211;oldpackage</code>.</dd>
<dt><code>-h, &#8211;hash</code></dt>
<dd>Print 50 hash marks as the package archive is unpacked. Use with <code>-v|&#8211;verbose</code> for a nicer display.</dd>
<dt><code>&#8211;ignoresize</code></dt>
<dd>Don&#8217;t check mount file systems for sufficient disk space before installing this package.</dd>
<dt><code>&#8211;ignorearch</code></dt>
<dd>Allow installation or upgrading even if the architectures of the binary package and host don&#8217;t match.</dd>
<dt><code>&#8211;ignoreos</code></dt>
<dd>Allow installation or upgrading even if the operating systems of the binary package and host don&#8217;t match.</dd>
<dt><code>&#8211;includedocs</code></dt>
<dd>Install documentation files. This is the default behavior.</dd>
<dt><code>&#8211;justdb</code></dt>
<dd>Update only the database, not the filesystem.</dd>
<dt><code>&#8211;nodigest</code></dt>
<dd>Don&#8217;t verify package or header digests when reading.</dd>
<dt><code>&#8211;nomanifest</code></dt>
<dd>Don&#8217;t process non-package files as manifests.</dd>
<dt><code>&#8211;nosignature</code></dt>
<dd>Don&#8217;t verify package or header signatures when reading.</dd>
<dt><code>&#8211;nodeps</code></dt>
<dd>Don&#8217;t do a dependency check before installing or upgrading a package.</dd>
<dt><code>&#8211;noorder</code></dt>
<dd>Don&#8217;t reorder the packages for an install. The list of packages would normally be reordered to satisfy dependencies.</dd>
<dt><code>&#8211;noplugins</code></dt>
<dd>Do not load and execute plugins.</dd>
<dt><code>&#8211;noscripts</code></dt>
<dd>
</dd><dt><code>&#8211;nopre</code></dt>
<dd>
</dd><dt><code>&#8211;nopost</code></dt>
<dd>
</dd><dt><code>&#8211;nopreun</code></dt>
<dd>
</dd><dt><code>&#8211;nopostun</code></dt>
<dd>Don&#8217;t execute the scriptlet of the same name. The <code>&#8211;noscripts</code> option is equivalent to <code>&#8211;nopre</code> <code>&#8211;nopost</code> <code>&#8211;nopreun</code> <code>&#8211;nopostun</code> and turns off the execution of the corresponding <code>%pre</code>, <code>%post</code>, <code>%preun</code>, and <code>%postun</code> scriptlet(s).</dd>
<dt><code>&#8211;notriggers</code></dt>
<dd>
</dd><dt><code>&#8211;notriggerin</code></dt>
<dd>
</dd><dt><code>&#8211;notriggerun</code></dt>
<dd>
</dd><dt><code>&#8211;notriggerprein</code></dt>
<dd>
</dd><dt><code>&#8211;notriggerpostun</code></dt>
<dd>Don&#8217;t execute any trigger scriptlet of the named type. The <code>&#8211;notriggers</code> option is equivalent to <code>&#8211;notriggerprein</code> <code>&#8211;notriggerin</code> <code>&#8211;notriggerun</code> <code>&#8211;notriggerpostun</code> and turns off execution of the corresponding <code>%triggerprein</code>, <code>%triggerin</code>, <code>%triggerun</code>, and <code>%triggerpostun</code> scriptlet(s).</dd>
<dt><code>&#8211;oldpackage</code></dt>
<dd>Allow an upgrade to replace a newer package with an older one.</dd>
<dt><code>&#8211;percent</code></dt>
<dd>Print percentages as files are unpacked from the package archive. This is intended to make <code>rpm</code> easy to run from other tools.</dd>
<dt><code>&#8211;prefix </code><i>NEWPATH</i></dt>
<dd>For relocatable binary packages, translate all file paths that start with the installation prefix in the package relocation hint(s) to <i>NEWPATH</i>.</dd>
<dt><code>&#8211;relocate </code><i>OLDPATH</i><code>=</code><i>NEWPATH</i></dt>
<dd>For relocatable binary packages, translate all file paths that start with <i>OLDPATH</i> in the package relocation hint(s) to <i>NEWPATH</i>. This option can be used repeatedly if several <i>OLDPATH</i>&#8216;s in the package are to be relocated.</dd>
<dt><code>&#8211;replacefiles</code></dt>
<dd>Install the packages even if they replace files from other, already installed, packages.</dd>
<dt><code>&#8211;replacepkgs</code></dt>
<dd>Install the packages even if some of them are already installed on this system.</dd>
<dt><code>&#8211;test</code></dt>
<dd>Do not install the package, simply check for and report potential conflicts.</dd></dl>
<h3>Erase Options</h3>
<p>The general form of an rpm erase command is <code>rpm</code> {<code>-e|&#8211;erase</code>} [<code>&#8211;allmatches</code>] [<code>&#8211;justdb] [&#8211;nodeps</code>] [<code>&#8211;noscripts</code>] [<code>&#8211;notriggers</code>] [<code>&#8211;test</code>] <i>PACKAGE_NAME</i><i> &#8230;</i> The following options may also be used:</p>
<dl>
<dt><code>&#8211;allmatches</code></dt>
<dd>Remove all versions of the package which match <i>PACKAGE_NAME</i>. Normally an error is issued if <i>PACKAGE_NAME</i> matches multiple packages.</dd>
<dt><code>&#8211;justdb</code></dt>
<dd>Update only the database, not the filesystem.</dd>
<dt><code>&#8211;nodeps</code></dt>
<dd>Don&#8217;t check dependencies before uninstalling the packages.</dd>
<dt><code>&#8211;noscripts</code></dt>
<dd>
</dd><dt><code>&#8211;nopreun</code></dt>
<dd>
</dd><dt><code>&#8211;nopostun</code></dt>
<dd>Don&#8217;t execute the scriptlet of the same name. The <code>&#8211;noscripts</code> option during package erase is equivalent to <code>&#8211;nopreun</code> <code>&#8211;nopostun</code> and turns off the execution of the corresponding <code>%preun</code>, and <code>%postun</code> scriptlet(s).</dd>
<dt><code>&#8211;notriggers</code></dt>
<dd>
</dd><dt><code>&#8211;notriggerun</code></dt>
<dd>
</dd><dt><code>&#8211;notriggerpostun</code></dt>
<dd>Don&#8217;t execute any trigger scriptlet of the named type. The <code>&#8211;notriggers</code> option is equivalent to <code>&#8211;notriggerun</code> <code>&#8211;notriggerpostun</code> and turns off execution of the corresponding <code>%triggerun</code>, and <code>%triggerpostun</code> scriptlet(s).</dd>
<dt><code>&#8211;test</code></dt>
<dd>Don&#8217;t really uninstall anything, just go through the motions. Useful in conjunction with the <code>-vv</code> option for debugging.</dd></dl>
<h3>Query Options</h3>
<p>The general form of an rpm query command is <code>rpm</code> {<code>-q|&#8211;query</code>} [<code>select-options</code>] [<code>query-options</code>] You may specify the format that package information should be printed in. To do this, you use the<br />
&nbsp;<wbr><code>&#8211;qf|&#8211;queryformat</code>&nbsp;<wbr><i>QUERYFMT</i> option, followed by the <i>QUERYFMT</i> format string. Query formats are modified versions of the standard <code><a href="/docs/linux/man/3-printf/">printf</a>(3)</code> formatting. The format is made up of static strings (which may include standard C character escapes for newlines, tabs, and other special characters) and <code><a href="/docs/linux/man/3-printf/">printf</a>(3)</code> type formatters. As <code>rpm</code> already knows the type to print, the type specifier must be omitted however, and replaced by the name of the header tag to be printed, enclosed by <code>{}</code> characters. Tag names are case insensitive, and the leading <code>RPMTAG_</code> portion of the tag name may be omitted as well. Alternate output formats may be requested by following the tag with <code>:</code><i>typetag</i>. Currently, the following types are supported:</p>
<dl>
<dt><code>:armor</code></dt>
<dd>Wrap a public key in ASCII armor.</dd>
<dt><code>:arraysize</code></dt>
<dd>Display number of elements in array tags.</dd>
<dt><code>:base64</code></dt>
<dd>Encode binary data using base64.</dd>
<dt><code>:date</code></dt>
<dd>Use <a href="/docs/linux/man/3-strftime/">strftime</a>(3) &quot;%c&quot; format.</dd>
<dt><code>:day</code></dt>
<dd>Use <a href="/docs/linux/man/3-strftime/">strftime</a>(3) &quot;%a %b %d %Y&quot; format.</dd>
<dt><code>:depflags</code></dt>
<dd>Format dependency comparison operator.</dd>
<dt><code>:deptype</code></dt>
<dd>Format dependency type.</dd>
<dt><code>:expand</code></dt>
<dd>Perform macro expansion.</dd>
<dt><code>:fflags</code></dt>
<dd>Format file flags.</dd>
<dt><code>:fstate</code></dt>
<dd>Format file state.</dd>
<dt><code>:fstatus</code></dt>
<dd>Format file verify status.</dd>
<dt><code>:hex</code></dt>
<dd>Format in hexadecimal.</dd>
<dt><code>:octal</code></dt>
<dd>Format in octal.</dd>
<dt><code>:perms</code></dt>
<dd>Format file permissions.</dd>
<dt><code>:pgpsig</code></dt>
<dd>Display signature fingerprint and time.</dd>
<dt><code>:shescape</code></dt>
<dd>Escape single quotes for use in a script.</dd>
<dt><code>:triggertype</code></dt>
<dd>Display trigger suffix.</dd>
<dt><code>:vflags</code></dt>
<dd>File verification flags.</dd>
<dt><code>:xml</code></dt>
<dd>Wrap data in simple xml markup.</dd></dl>
<p> For example, to print only the names of the packages queried, you could use <code>%{NAME}</code> as the format string. To print the packages name and distribution information in two columns, you could use <code>%-30{NAME}%{DISTRIBUTION}</code>. <code>rpm</code> will print a list of all of the tags it knows about when it is invoked with the <code>&#8211;querytags</code> argument. There are two subsets of options for querying: package selection, and information selection.</p>
<h3>Package Selection Options:</h3>
<dl>
<dt><i>PACKAGE_NAME</i></dt>
<dd>Query installed package named <i>PACKAGE_NAME</i>.</dd>
<dt><code>-a, &#8211;all</code></dt>
<dd>Query all installed packages.</dd>
<dt><code>-f, &#8211;file </code><i>FILE</i></dt>
<dd>Query package owning <i>FILE</i>.</dd>
<dt><code>-g, &#8211;group </code><i>GROUP</i></dt>
<dd>Query packages with the group of <i>GROUP</i>.</dd>
<dt><code>&#8211;hdrid </code><i>SHA1</i></dt>
<dd>Query package that contains a given header identifier, i.e. the <i>SHA1</i> digest of the immutable header region.</dd>
<dt><code>-p, &#8211;package </code><i>PACKAGE_FILE</i></dt>
<dd>Query an (uninstalled) package <i>PACKAGE_FILE</i>. The <i>PACKAGE_FILE</i> may be specified as an <code>ftp</code> or <code>http</code> style URL, in which case the package header will be downloaded and queried. See <code>FTP/HTTP OPTIONS</code> for information on <code>rpm</code>&#8216;s internal <code>ftp</code> and <code>http</code> client support. The <i>PACKAGE_FILE</i> argument(s), if not a binary package, will be interpreted as an ASCII package manifest unless <code>&#8211;nomanifest</code> option is used. In manifests, comments are permitted, starting with a &#8216;#&#8217;, and each line of a package manifest file may include white space separated glob expressions, including URL&#8217;s, that will be expanded to paths that are substituted in place of the package manifest as additional <i>PACKAGE_FILE</i> arguments to the query.</dd>
<dt><code>&#8211;pkgid </code><i>MD5</i></dt>
<dd>Query package that contains a given package identifier, i.e. the <i>MD5</i> digest of the combined header and payload contents.</dd>
<dt><code>&#8211;querybynumber </code><i>HDRNUM</i></dt>
<dd>Query the <i>HDRNUM</i>th database entry directly; this is useful only for debugging.</dd>
<dt><code>&#8211;specfile </code><i>SPECFILE</i></dt>
<dd>Parse and query <i>SPECFILE</i> as if it were a package. Although not all the information (e.g. file lists) is available, this type of query permits rpm to be used to extract information from spec files without having to write a specfile parser.</dd>
<dt><code>&#8211;tid </code><i>TID</i></dt>
<dd>Query package(s) that have a given <i>TID</i> transaction identifier. A unix time stamp is currently used as a transaction identifier. All package(s) installed or erased within a single transaction have a common identifier.</dd>
<dt><code>&#8211;triggeredby </code><i>PACKAGE_NAME</i></dt>
<dd>Query packages that are triggered by package(s) <i>PACKAGE_NAME</i>.</dd>
<dt><code>&#8211;whatprovides </code><i>CAPABILITY</i></dt>
<dd>Query all packages that provide the <i>CAPABILITY</i> capability.</dd>
<dt><code>&#8211;whatrequires </code><i>CAPABILITY</i></dt>
<dd>Query all packages that require <i>CAPABILITY</i> for proper functioning.</dd></dl>
<h3>Package Query Options:</h3>
<dl>
<dt><code>&#8211;changelog</code></dt>
<dd>Display change information for the package.</dd>
<dt><code>-c, &#8211;configfiles</code></dt>
<dd>List only configuration files (implies <code>-l</code>).</dd>
<dt><code>&#8211;conflicts</code></dt>
<dd>List capabilities this package conflicts with.</dd>
<dt><code>-d, &#8211;docfiles</code></dt>
<dd>List only documentation files (implies <code>-l</code>).</dd>
<dt><code>&#8211;dump</code></dt>
<dd>Dump file information as follows (implies <code>-l</code>):  </dd>
<pre>path size mtime digest mode owner group isconfig isdoc rdev symlink</pre>
</dl>
<dt><code>&#8211;filesbypkg</code></dt>
<dd>List all the files in each selected package.</dd>
<dt><code>-i, &#8211;info</code></dt>
<dd>Display package information, including name, version, and description. This uses the <code>&#8211;queryformat</code> if one was specified.</dd>
<dt><code>&#8211;last</code></dt>
<dd>Orders the package listing by install time such that the latest packages are at the top.</dd>
<dt><code>-L, &#8211;licensefiles</code></dt>
<dd>List only license files (implies <code>-l</code>).</dd>
<dt><code>-l, &#8211;list</code></dt>
<dd>List files in package.</dd>
<dt><code>&#8211;obsoletes</code></dt>
<dd>List packages this package obsoletes.</dd>
<dt><code>&#8211;provides</code></dt>
<dd>List capabilities this package provides.</dd>
<dt><code>-R, &#8211;requires</code></dt>
<dd>List capabilities on which this package depends.</dd>
<dt><code>&#8211;scripts</code></dt>
<dd>List the package specific scriptlet(s) that are used as part of the installation and uninstallation processes.</dd>
<dt><code>-s, &#8211;state</code></dt>
<dd>Display the <i>states</i> of files in the package (implies <code>-l</code>). The state of each file is one of <i>normal</i>, <i>not installed</i>, or <i>replaced</i>.</dd>
<dt><code>&#8211;triggers, &#8211;triggerscripts</code></dt>
<dd>Display the trigger scripts, if any, which are contained in the package.</dd></dl>
<h3>Verify Options</h3>
<p>The general form of an rpm verify command is <code>rpm</code> {<code>-V|&#8211;verify</code>} [<code>select-options</code>] [<code>verify-options</code>] Verifying a package compares information about the installed files in the package with information about the files taken from the package metadata stored in the rpm database. Among other things, verifying compares the size, digest, permissions, type, owner and group of each file. Any discrepancies are displayed. Files that were not installed from the package, for example, documentation files excluded on installation using the &quot;<code>&#8211;excludedocs</code>&quot; option, will be silently ignored. The package selection options are the same as for package querying (including package manifest files as arguments). Other options unique to verify mode are:</p>
<dl>
<dt><code>&#8211;nodeps</code></dt>
<dd>Don&#8217;t verify dependencies of packages.</dd>
<dt><code>&#8211;nodigest</code></dt>
<dd>Don&#8217;t verify package or header digests when reading.</dd>
<dt><code>&#8211;nofiles</code></dt>
<dd>Don&#8217;t verify any attributes of package files.</dd>
<dt><code>&#8211;noscripts</code></dt>
<dd>Don&#8217;t execute the <code>%verifyscript</code> scriptlet (if any).</dd>
<dt><code>&#8211;nosignature</code></dt>
<dd>Don&#8217;t verify package or header signatures when reading.</dd>
<dt><code>&#8211;nolinkto</code></dt>
<dd>
</dd><dt><code>&#8211;nofiledigest</code> (formerly <code>&#8211;nomd5</code>)</dt>
<dd>
</dd><dt><code>&#8211;nosize</code></dt>
<dd>
</dd><dt><code>&#8211;nouser</code></dt>
<dd>
</dd><dt><code>&#8211;nogroup</code></dt>
<dd>
</dd><dt><code>&#8211;nomtime</code></dt>
<dd>
</dd><dt><code>&#8211;nomode</code></dt>
<dd>
</dd><dt><code>&#8211;nordev</code></dt>
<dd>Don&#8217;t verify the corresponding file attribute.</dd></dl>
<p> The format of the output is a string of 9 characters, a possible attribute marker: </p>
<pre><code>c</code> <code>%config</code> configuration file.
<code>d</code> <code>%doc</code> documentation file.
<code>g</code> <code>%ghost</code> file (i.e. the file contents are not included in the package payload).
<code>l</code> <code>%license</code> license file.
<code>r</code> <code>%readme</code> readme file.</pre>
<p>from the package header, followed by the file name. Each of the 9 characters denotes the result of a comparison of attribute(s) of the file to the value of those attribute(s) recorded in the database. A single &quot;<code>.</code>&quot; (period) means the test passed, while a single &quot;<code>?</code>&quot; (question mark) indicates the test could not be performed (e.g. file permissions prevent reading). Otherwise, the (mnemonically em<code>B</code>oldened) character denotes failure of the corresponding <code>&#8211;verify</code> test: </p>
<pre><code>S</code> file <code>S</code>ize differs
<code>M</code> <code>M</code>ode differs (includes permissions and file type)
<code>5</code> digest (formerly MD<code>5</code> sum) differs
<code>D</code> <code>D</code>evice major/minor number mismatch
<code>L</code> read<code>L</code>ink(2) path mismatch
<code>U</code> <code>U</code>ser ownership differs
<code>G</code> <code>G</code>roup ownership differs
<code>T</code> m<code>T</code>ime differs
<code>P</code> ca<code>P</code>abilities differ</pre>
<h3>Miscellaneous Commands</h3>
<dl>
<dt><code>rpm</code> <code>&#8211;showrc</code></dt>
<dd>shows the values <code>rpm</code> will use for all of the options are currently set in <i>rpmrc</i> and <i>macros</i> configuration file(s).</dd>
<dt><code>rpm</code> <code>&#8211;setperms</code> <i>PACKAGE_NAME</i></dt>
<dd>sets permissions of files in the given package.</dd>
<dt><code>rpm</code> <code>&#8211;setugids</code> <i>PACKAGE_NAME</i></dt>
<dd>sets user/group ownership of files in the given package.</dd>
<dt>Options <code>&#8211;setperms</code> and <code>&#8211;setugids</code> are mutually exclusive.</dt>
<dd></dd></dl>
<h3>Ftp/Http Options</h3>
<p><code>rpm</code> can act as an FTP and/or HTTP client so that packages can be queried or installed from the internet. Package files for install, upgrade, and query operations may be specified as an <code>ftp</code> or <code>http</code> style URL: <a href="ftp://USER:PASSWORD@HOST:PORT/path/to/package.rpm">ftp://USER:PASSWORD@HOST:PORT/path/to/package.rpm</a> If the <code>:PASSWORD</code> portion is omitted, the password will be prompted for (once per user/hostname pair). If both the user and password are omitted, anonymous <code>ftp</code> is used. In all cases, passive (PASV) <code>ftp</code> transfers are performed. <code>rpm</code> allows the following options to be used with ftp URLs:</p>
<dl>
<dt><code>&#8211;ftpproxy </code><i>HOST</i></dt>
<dd>The host <i>HOST</i> will be used as a proxy server for all ftp transfers, which allows users to ftp through firewall machines which use proxy systems. This option may also be specified by configuring the macro <code>%_ftpproxy</code>.</dd>
<dt><code>&#8211;ftpport </code><i>PORT</i></dt>
<dd>The TCP <i>PORT</i> number to use for the ftp connection on the proxy ftp server instead of the default port. This option may also be specified by configuring the macro <code>%_ftpport</code>.</dd></dl>
<p> <code>rpm</code> allows the following options to be used with <code>http</code> URLs:</p>
<dl>
<dt><code>&#8211;httpproxy </code><i>HOST</i></dt>
<dd>The host <i>HOST</i> will be used as a proxy server for all <code>http</code> transfers. This option may also be specified by configuring the macro <code>%_httpproxy</code>.</dd>
<dt><code>&#8211;httpport </code><i>PORT</i></dt>
<dd>The TCP <i>PORT</i> number to use for the <code>http</code> connection on the proxy http server instead of the default port. This option may also be specified by configuring the macro <code>%_httpport</code>.</dd></dl>
<h2>Legacy Issues</h2>
<h3>Executing rpmbuild</h3>
<p>The build modes of rpm are now resident in the <i>/usr/bin/rpmbuild</i> executable. Install the package containing <code>rpmbuild</code> (usually <code>rpm-build</code>) and see <code><a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8) for documentation of all the <code>rpm</code> build modes.</p>
<h2>Files</h2>
<h3>rpmrc Configuration</h3>
<pre><i>/usr/lib/rpm/rpmrc</i>
<i>/usr/lib/rpm/redhat/rpmrc</i>
<i>/etc/rpmrc</i>
<i>~/.rpmrc</i></pre>
<h3>Macro Configuration</h3>
<pre><i>/usr/lib/rpm/macros</i>
<i>/usr/lib/rpm/redhat/macros</i>
<i>/etc/rpm/macros</i>
<i>~/.rpmmacros</i></pre>
<h3>Database</h3>
<pre><i>/var/lib/rpm/Basenames</i>
<i>/var/lib/rpm/Conflictname</i>
<i>/var/lib/rpm/Dirnames</i>
<i>/var/lib/rpm/Group</i>
<i>/var/lib/rpm/Installtid</i>
<i>/var/lib/rpm/Name</i>
<i>/var/lib/rpm/Obsoletename</i>
<i>/var/lib/rpm/Packages</i>
<i>/var/lib/rpm/Providename</i>
<i>/var/lib/rpm/Requirename</i>
<i>/var/lib/rpm/Sha1header</i>
<i>/var/lib/rpm/Sigmd5</i>
<i>/var/lib/rpm/Triggername</i></pre>
<h3>Temporary</h3>
<p><i>/var/tmp/rpm*</i></p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/3-popt/">popt</a></code>(3),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmdb/">rpmdb</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmkeys/">rpmkeys</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmsign/">rpmsign</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmspec/">rpmspec</a></code>(8),</pre>
<p><code>rpm &#8211;help</code> &#8211; as rpm supports customizing the options via popt aliases it&#8217;s impossible to guarantee that what&#8217;s described in the manual matches what&#8217;s available. </p>
<p> <code><a rel="nofollow" href="http://www.rpm.org/">http://www.rpm.org/</a> &lt;URL:<a href="http://www.rpm.org/">http://www.rpm.org/</a>&gt; </code></p>
<h2>Authors</h2>
<pre>Marc Ewing &lt;marc [at] redhat.com&gt;
Jeff Johnson &lt;jbj [at] redhat.com&gt;
Erik Troan &lt;ewt [at] redhat.com&gt;</pre>
