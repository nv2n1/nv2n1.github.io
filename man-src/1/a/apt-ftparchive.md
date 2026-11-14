---
title: "apt-ftparchive(1)"
name: "apt-ftparchive"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-ftparchive/"
description: "apt-ftparchive – Utility to generate index files"
---

<h2 class="name">NAME</h2>
<p> apt-ftparchive &#8211; Utility to generate index files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>apt-ftparchive</code> [<code>-dsq</code>] [<code>&#8211;md5</code>] [<code>&#8211;delink</code>] [<code>&#8211;readonly</code>] [<code>&#8211;contents</code>] [<code>&#8211;arch&nbsp;</code><i>architecture</i>] [<code>-o=</code><i>config_string</i>] [<code>-c=</code><i>config_file</i>] {packages&nbsp;<i>path</i>&#8230;&nbsp;[<i>override-file</i>&nbsp;[<i>pathprefix</i>]] | sources&nbsp;<i>path</i>&#8230;&nbsp;[<i>override-file</i>&nbsp;[<i>pathprefix</i>]] | contents&nbsp;<i>path</i> | release&nbsp;<i>path</i> | generate&nbsp;<i>config_file</i>&nbsp;<i>section</i>&#8230; | clean&nbsp;<i>config_file</i> | {-v | &#8211;version} | {-h | &#8211;help}}</dl>
<h2>DESCRIPTION</h2>
<p> <code>apt-ftparchive</code></p>
<dd>is the command line tool that generates the index files that APT uses to access a distribution source. The index files should be generated on the origin site based on the content of that site. </p>
<p> <code>apt-ftparchive</code> is a superset of the <code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1) program, incorporating its entire functionality via the packages command. It also contains a contents file generator, contents, and an elaborate means to &#8216;script&#8217; the generation process for a complete archive. </p>
<p> Internally <code>apt-ftparchive</code> can make use of binary databases to cache the contents of a .deb file and it does not rely on any external programs aside from <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1). When doing a full generate it automatically performs file-change checks and builds the desired compressed output files. </p>
<p> Unless the <code>-h</code>, or <code>&#8211;help</code> option is given, one of the commands below must be present. </p>
<p> <code>packages</code></p>
<dl>
<dt>
<dd> The packages command generates a package file from a directory tree. It takes the given directory and recursively searches it for .deb files, emitting a package record to stdout for each. This command is approximately equivalent to <code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1). </p>
<p> The option <code>&#8211;db</code> can be used to specify a binary caching DB.</dl>
<p> <code>sources</code></p>
<dl>
<dt>
<dd> The sources command generates a source index file from a directory tree. It takes the given directory and recursively searches it for .dsc files, emitting a source record to stdout for each. This command is approximately equivalent to <code><a href="/docs/linux/man/1-dpkg-scansources/">dpkg-scansources</a></code>(1). </p>
<p> If an override file is specified then a source override file will be looked for with an extension of .src. The &#8211;source-override option can be used to change the source override file that will be used.</dl>
<p> <code>contents</code></p>
<dl>
<dt>
<dd> The contents command generates a contents file from a directory tree. It takes the given directory and recursively searches it for .deb files, and reads the file list from each file. It then sorts and writes to stdout the list of files matched to packages. Directories are not written to the output. If multiple packages own the same file then each package is separated by a comma in the output. </p>
<p> The option <code>&#8211;db</code> can be used to specify a binary caching DB.</dl>
<p> <code>release</code></p>
<dl>
<dt>
<dd> The release command generates a Release file from a directory tree. It recursively searches the given directory for uncompressed and compressed Packages, Sources, Contents, Components and icons files as well as Release, Index and md5sum.txt files by default (APT::FTPArchive::Release::Default-Patterns). Additional filename patterns can be added by listing them in APT::FTPArchive::Release::Patterns. It then writes to stdout a Release file containing (by default) an MD5, SHA1, SHA256 and SHA512 digest for each file. </p>
<p> Values for the additional metadata fields in the Release file are taken from the corresponding variables under APT::FTPArchive::Release, e.g. APT::FTPArchive::Release::Origin. The supported fields are Origin, Label, Suite, Version, Codename, Date, NotAutomatic, ButAutomaticUpgrades, Acquire-By-Hash, Valid-Until, Signed-By, Architectures, Components and Description.</dl>
<p> <code>generate</code></p>
<dl>
<dt>
<dd> The generate command is designed to be runnable from a cron script and builds indexes according to the given config file. The config language provides a flexible means of specifying which index files are built from which directories, as well as providing a simple means of maintaining the required settings.</dl>
<p> <code>clean</code></p>
<dl>
<dt>
<dd> The clean command tidies the databases used by the given configuration file by removing any records that are no longer necessary.</dl>
<h2>THE GENERATE CONFIGURATION</h2>
<p> The generate command uses a configuration file to describe the archives that are going to be generated. It follows the typical ISC configuration format as seen in ISC tools like bind 8 and dhcpd. <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) contains a description of the syntax. Note that the generate configuration is parsed in sectional manner, but <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) is parsed in a tree manner. This only effects how the scope tag is handled. </p>
<p> The generate configuration has four separate sections, each described below.</p>
<h3>Dir Section</h3>
<p> The Dir section defines the standard directories needed to locate the files required during the generation process. These directories are prepended certain relative paths defined in later sections to produce a complete an absolute path. </p>
<p> <code>ArchiveDir</code></p>
<dl>
<dt>
<dd> Specifies the root of the FTP archive, in a standard Debian configuration this is the directory that contains the ls-LR and dist nodes.</dl>
<p> <code>OverrideDir</code></p>
<dl>
<dt>
<dd> Specifies the location of the override files.</dl>
<p> <code>CacheDir</code></p>
<dl>
<dt>
<dd> Specifies the location of the cache files.</dl>
<p> <code>FileListDir</code></p>
<dl>
<dt>
<dd> Specifies the location of the file list files, if the FileList setting is used below.</dl>
<h3>Default Section</h3>
<p> The Default section specifies default values, and settings that control the operation of the generator. Other sections may override these defaults with a per-section setting. </p>
<p> <code>Packages::Compress</code></p>
<dl>
<dt>
<dd> Sets the default compression schemes to use for the package index files. It is a string that contains a space separated list of at least one of the compressors configured via the <code>APT::Compressor</code> configuration scope. The default for all compression schemes is &#8216;. gzip&#8217;.</dl>
<p> <code>Packages::Extensions</code></p>
<dl>
<dt>
<dd> Sets the default list of file extensions that are package files. This defaults to &#8216;.deb&#8217;.</dl>
<p> <code>Sources::Compress</code></p>
<dl>
<dt>
<dd> This is similar to Packages::Compress except that it controls the compression for the Sources files.</dl>
<p> <code>Sources::Extensions</code></p>
<dl>
<dt>
<dd> Sets the default list of file extensions that are source files. This defaults to &#8216;.dsc&#8217;.</dl>
<p> <code>Contents::Compress</code></p>
<dl>
<dt>
<dd> This is similar to Packages::Compress except that it controls the compression for the Contents files.</dl>
<p> <code>Translation::Compress</code></p>
<dl>
<dt>
<dd> This is similar to Packages::Compress except that it controls the compression for the Translation-en master file.</dl>
<p> <code>DeLinkLimit</code></p>
<dl>
<dt>
<dd> Specifies the number of kilobytes to delink (and replace with hard links) per run. This is used in conjunction with the per-section External-Links setting.</dl>
<p> <code>FileMode</code></p>
<dl>
<dt>
<dd> Specifies the mode of all created index files. It defaults to 0644. All index files are set to this mode with no regard to the umask.</dl>
<p> <code>LongDescription</code></p>
<dl>
<dt>
<dd> Specifies whether long descriptions should be included in the Packages file or split out into a master Translation-en file.</dl>
<h3>TreeDefault Section</h3>
<p> Sets defaults specific to Tree sections. All of these variables are substitution variables and have the strings $(DIST), $(SECTION) and $(ARCH) replaced with their respective values. </p>
<p> <code>MaxContentsChange</code></p>
<dl>
<dt>
<dd> Sets the number of kilobytes of contents files that are generated each day. The contents files are round-robined so that over several days they will all be rebuilt.</dl>
<p> <code>ContentsAge</code></p>
<dl>
<dt>
<dd> Controls the number of days a contents file is allowed to be checked without changing. If this limit is passed the mtime of the contents file is updated. This case can occur if the package file is changed in such a way that does not result in a new contents file [override edit for instance]. A hold off is allowed in hopes that new .debs will be installed, requiring a new file anyhow. The default is 10, the units are in days.</dl>
<p> <code>Directory</code></p>
<dl>
<dt>
<dd> Sets the top of the .deb directory tree. Defaults to $(DIST)/$(SECTION)/binary-$(ARCH)/</dl>
<p> <code>SrcDirectory</code></p>
<dl>
<dt>
<dd> Sets the top of the source package directory tree. Defaults to $(DIST)/$(SECTION)/source/</dl>
<p> <code>Packages</code></p>
<dl>
<dt>
<dd> Sets the output Packages file. Defaults to $(DIST)/$(SECTION)/binary-$(ARCH)/Packages</dl>
<p> <code>Sources</code></p>
<dl>
<dt>
<dd> Sets the output Sources file. Defaults to $(DIST)/$(SECTION)/source/Sources</dl>
<p> <code>Translation</code></p>
<dl>
<dt>
<dd> Sets the output Translation-en master file with the long descriptions if they should be not included in the Packages file. Defaults to $(DIST)/$(SECTION)/i18n/Translation-en</dl>
<p> <code>InternalPrefix</code></p>
<dl>
<dt>
<dd> Sets the path prefix that causes a symlink to be considered an internal link instead of an external link. Defaults to $(DIST)/$(SECTION)/</dl>
<p> <code>Contents</code></p>
<dl>
<dt>
<dd> Sets the output Contents file. Defaults to $(DIST)/$(SECTION)/Contents-$(ARCH). If this setting causes multiple Packages files to map onto a single Contents file (as is the default) then <code>apt-ftparchive</code> will integrate those package files together automatically.</dl>
<p> <code>Contents::Header</code></p>
<dl>
<dt>
<dd> Sets header file to prepend to the contents output.</dl>
<p> <code>BinCacheDB</code></p>
<dl>
<dt>
<dd> Sets the binary cache database to use for this section. Multiple sections can share the same database.</dl>
<p> <code>FileList</code></p>
<dl>
<dt>
<dd> Specifies that instead of walking the directory tree, <code>apt-ftparchive</code> should read the list of files from the given file. Relative files names are prefixed with the archive directory.</dl>
<p> <code>SourceFileList</code></p>
<dl>
<dt>
<dd> Specifies that instead of walking the directory tree, <code>apt-ftparchive</code> should read the list of files from the given file. Relative files names are prefixed with the archive directory. This is used when processing source indexes.</dl>
<h3>Tree Section</h3>
<p> The Tree section defines a standard Debian file tree which consists of a base directory, then multiple sections in that base directory and finally multiple Architectures in each section. The exact pathing used is defined by the Directory substitution variable. </p>
<p> The Tree section takes a scope tag which sets the $(DIST) variable and defines the root of the tree (the path is prefixed by ArchiveDir). Typically this is a setting such as dists/bullseye. </p>
<p> All of the settings defined in the TreeDefault section can be used in a Tree section as well as three new variables. </p>
<p> When processing a Tree section <code>apt-ftparchive</code> performs an operation similar to: </p>
<dl>
<dt>
<dd>
<pre>
for i in Sections do 
   for j in Architectures do
      Generate for DIST=scope SECTION=i ARCH=j
     
</pre>
</dl>
<p> <code>Sections</code></p>
<dl>
<dt>
<dd> This is a space separated list of sections which appear under the distribution; typically this is something like main contrib non-free</dl>
<p> <code>Architectures</code></p>
<dl>
<dt>
<dd> This is a space separated list of all the architectures that appear under search section. The special architecture &#8216;source&#8217; is used to indicate that this tree has a source archive. The architecture &#8216;all&#8217; signals that architecture specific files like Packages should not include information about architecture all packages in all files as they will be available in a dedicated file.</dl>
<p> <code>LongDescription</code></p>
<dl>
<dt>
<dd> Specifies whether long descriptions should be included in the Packages file or split out into a master Translation-en file.</dl>
<p> <code>BinOverride</code></p>
<dl>
<dt>
<dd> Sets the binary override file. The override file contains section, priority and maintainer address information.</dl>
<p> <code>SrcOverride</code></p>
<dl>
<dt>
<dd> Sets the source override file. The override file contains section information.</dl>
<p> <code>ExtraOverride</code></p>
<dl>
<dt>
<dd> Sets the binary extra override file.</dl>
<p> <code>SrcExtraOverride</code></p>
<dl>
<dt>
<dd> Sets the source extra override file.</dl>
<h3>BinDirectory Section</h3>
<p> The bindirectory section defines a binary directory tree with no special structure. The scope tag specifies the location of the binary directory and the settings are similar to the Tree section with no substitution variables or SectionArchitecture settings. </p>
<p> <code>Packages</code></p>
<dl>
<dt>
<dd> Sets the Packages file output.</dl>
<p> <code>Sources</code></p>
<dl>
<dt>
<dd> Sets the Sources file output. At least one of Packages or Sources is required.</dl>
<p> <code>Contents</code></p>
<dl>
<dt>
<dd> Sets the Contents file output (optional).</dl>
<p> <code>BinOverride</code></p>
<dl>
<dt>
<dd> Sets the binary override file.</dl>
<p> <code>SrcOverride</code></p>
<dl>
<dt>
<dd> Sets the source override file.</dl>
<p> <code>ExtraOverride</code></p>
<dl>
<dt>
<dd> Sets the binary extra override file.</dl>
<p> <code>SrcExtraOverride</code></p>
<dl>
<dt>
<dd> Sets the source extra override file.</dl>
<p> <code>BinCacheDB</code></p>
<dl>
<dt>
<dd> Sets the cache DB.</dl>
<p> <code>PathPrefix</code></p>
<dl>
<dt>
<dd> Appends a path to all the output paths.</dl>
<p> <code>FileList</code>, <code>SourceFileList</code></p>
<dl>
<dt>
<dd> Specifies the file list file.</dl>
<h2>THE BINARY OVERRIDE FILE</h2>
<p> The binary override file is fully compatible with <code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1). It contains four fields separated by spaces. The first field is the package name, the second is the priority to force that package to, the third is the section to force that package to and the final field is the maintainer permutation field. </p>
<p> The general form of the maintainer field is: </p>
<dl>
<dt>
<dd>
<pre>
old [// oldn]* =&gt; new
</pre>
</dl>
<p> or simply, </p>
<dl>
<dt>
<dd>
<pre>
new
</pre>
</dl>
<p> The first form allows a double-slash separated list of old email addresses to be specified. If any of those are found then new is substituted for the maintainer field. The second form unconditionally substitutes the maintainer field.</p>
<h2>THE SOURCE OVERRIDE FILE</h2>
<p> The source override file is fully compatible with <code><a href="/docs/linux/man/1-dpkg-scansources/">dpkg-scansources</a></code>(1). It contains two fields separated by spaces. The first field is the source package name, the second is the section to assign it.</p>
<h2>THE EXTRA OVERRIDE FILE</h2>
<p> The extra override file allows any arbitrary tag to be added or replaced in the output. It has three columns, the first is the package, the second is the tag and the remainder of the line is the new value.</p>
<h2>OPTIONS</h2>
<p> All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>&#8211;md5</code>, <code>&#8211;sha1</code>, <code>&#8211;sha256</code>, <code>&#8211;sha512</code></p>
<dl>
<dt>
<dd> Generate the given checksum. These options default to on, when turned off the generated index files will not have the checksum fields where possible. Configuration Items: APT::FTPArchive::<i>Checksum</i> and APT::FTPArchive::<i>Index</i>::<i>Checksum</i> where <i>Index</i> can be Packages, Sources or Release and <i>Checksum</i> can be MD5, SHA1, SHA256 or SHA512.</dl>
<p> <code>-d</code>, <code>&#8211;db</code></p>
<dl>
<dt>
<dd> Use a binary caching DB. This has no effect on the generate command. Configuration Item: APT::FTPArchive::DB.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quiet; produces output suitable for logging, omitting progress indicators. More q&#8217;s will produce more quiet up to a maximum of 2. You can also use <code>-q=#</code> to set the quiet level, overriding the configuration file. Configuration Item: quiet.</dl>
<p> <code>&#8211;delink</code></p>
<dl>
<dt>
<dd> Perform Delinking. If the External-Links setting is used then this option actually enables delinking of the files. It defaults to on and can be turned off with <code>&#8211;no-delink</code>. Configuration Item: APT::FTPArchive::DeLinkAct.</dl>
<p> <code>&#8211;contents</code></p>
<dl>
<dt>
<dd> Perform contents generation. When this option is set and package indexes are being generated with a cache DB then the file listing will also be extracted and stored in the DB for later use. When using the generate command this option also allows the creation of any Contents files. The default is on. Configuration Item: APT::FTPArchive::Contents.</dl>
<p> <code>-s</code>, <code>&#8211;source-override</code></p>
<dl>
<dt>
<dd> Select the source override file to use with the sources command. Configuration Item: APT::FTPArchive::SourceOverride.</dl>
<p> <code>&#8211;readonly</code></p>
<dl>
<dt>
<dd> Make the caching databases read only. Configuration Item: APT::FTPArchive::ReadOnlyDB.</dl>
<p> <code>-a</code>, <code>&#8211;arch</code></p>
<dl>
<dt>
<dd> Accept in the packages and contents commands only package files matching *_arch.deb or *_all.deb instead of all package files in the given path. Configuration Item: APT::FTPArchive::Architecture.</dl>
<p> <code>APT::FTPArchive::AlwaysStat</code></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-apt-ftparchive/">apt-ftparchive</a></code>(1) caches as much as possible of metadata in a cachedb. If packages are recompiled and/or republished with the same version again, this will lead to problems as the now outdated cached metadata like size and checksums will be used. With this option enabled this will no longer happen as it will be checked if the file was changed. Note that this option is set to &quot;false&quot; by default as it is not recommend to upload multiple versions/builds of a package with the same version number, so in theory nobody will have these problems and therefore all these extra checks are useless.</dl>
<p> <code>APT::FTPArchive::LongDescription</code></p>
<dl>
<dt>
<dd> This configuration option defaults to &quot;true&quot; and should only be set to &quot;false&quot; if the Archive generated with <code><a href="/docs/linux/man/1-apt-ftparchive/">apt-ftparchive</a></code>(1) also provides Translation files. Note that the Translation-en master file can only be created in the generate command.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a short usage summary.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the program version.</dl>
<p> <code>-c</code>, <code>&#8211;config-file</code></p>
<dl>
<dt>
<dd> Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file. If configuration settings need to be set before the default configuration files are parsed specify a file with the <code>APT_CONFIG</code> environment variable. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for syntax information.</dl>
<p> <code>-o</code>, <code>&#8211;option</code></p>
<dl>
<dt>
<dd> Set a Configuration Option; This will set an arbitrary configuration option. The syntax is <code>-o Foo::Bar=bar</code>. <code>-o</code> and <code>&#8211;option</code> can be used multiple times to set different options.</dl>
<h2>EXAMPLES</h2>
<p> To create a compressed Packages file for a directory containing binary packages (.deb): </p>
<dl>
<dt>
<dd>
<pre>
<code>apt-ftparchive</code> packages <i>directory</i> | <code>gzip</code> &gt; Packages.gz
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5)</p>
<h2>DIAGNOSTICS</h2>
<p> <code>apt-ftparchive</code> returns zero on normal operation, decimal 100 on error.</p>
<h2>BUGS</h2>
<p> m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>AUTHORS</h2>
<p> <code>Jason Gunthorpe</code></p>
<dl>
<dt>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dt>
<dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> APT bug page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
</dl>
<h2>Index</h2>
