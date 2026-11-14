---
title: "apt-conf(5)"
name: "apt-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apt-conf/"
description: "apt.conf – Configuration file for APT"
---

<p>apt.conf &#8211; Configuration file for APT</p>
<h2>Description</h2>
<p>/etc/apt/apt.conf is the main configuration file shared by all the tools in the APT suite of tools, though it is by no means the only place options can be set. The suite also shares a common command line parser to provide a uniform environment. </p>
<p> When an APT tool starts up it will read the configuration files in the following order: </p>
<dl>
<dd>1. the file specified by the <code>APT_CONFIG</code> environment variable (if any)</dl>
<dl>
<dd>2. all files in Dir::Etc::Parts in alphanumeric ascending order which have either no or &quot;conf&quot; as filename extension and which only contain alphanumeric, hyphen (-), underscore (_) and period (.) characters. Otherwise APT will print a notice that it has ignored a file, unless that file matches a pattern in the Dir::Ignore-Files-Silently configuration list &#8211; in which case it will be silently ignored.</dl>
<dl>
<dd>3. the main configuration file specified by Dir::Etc::main</dl>
<dl>
<dd>4. all options set in the binary specific configuration subtree are moved into the root of the tree.</dl>
<dl>
<dd>5. the command line options are applied to override the configuration directives or to load even more configuration files.</dl>
<h2>Syntax</h2>
<p>The configuration file is organized in a tree with options organized into functional groups. Option specification is given with a double colon notation; for instance APT::Get::Assume-Yes is an option within the APT tool group, for the Get tool. Options do not inherit from their parent groups. </p>
<p> Syntactically the configuration language is modeled after what the ISC tools such as bind and dhcp use. Lines starting with // are treated as comments (ignored), as well as all text between /* and */, just like C/C++ comments. Lines starting with # are also treated as comments. Each line is of the form APT::Get::Assume-Yes &quot;true&quot;;. The quotation marks and trailing semicolon are required. The value must be on one line, and there is no kind of string concatenation. Values must not include backslashes or extra quotation marks. Option names are made up of alphanumeric characters and the characters &quot;/-:._+&quot;. A new scope can be opened with curly braces, like this: </p>
<dl>
<dd>
<pre>APT {
 Get {
 Assume-Yes &quot;true&quot;;
 Fix-Broken &quot;true&quot;;
 };
};</pre>
</dl>
<p> with newlines placed to make it more readable. Lists can be created by opening a scope and including a single string enclosed in quotes followed by a semicolon. Multiple entries can be included, separated by a semicolon. </p>
<dl>
<dd>
<pre>DPkg::Pre-Install-Pkgs {&quot;/usr/sbin/dpkg-preconfigure --apt&quot;;};</pre>
</dl>
<p> In general the sample configuration file /usr/share/doc/apt/examples/configure-index.gz is a good guide for how it should look. </p>
<p> Case is not significant in names of configuration items, so in the previous example you could use dpkg::pre-install-pkgs. </p>
<p> Names for the configuration items are optional if a list is defined as can be seen in the DPkg::Pre-Install-Pkgs example above. If you don&#8217;t specify a name a new entry will simply add a new option to the list. If you specify a name you can override the option in the same way as any other option by reassigning a new value to the option. </p>
<p> Two special commands are defined: #include (which is deprecated and not supported by alternative implementations) and #clear. #include will include the given file, unless the filename ends in a slash, in which case the whole directory is included. #clear is used to erase a part of the configuration tree. The specified element and all its descendants are erased. (Note that these lines also need to end with a semicolon.) </p>
<p> The #clear command is the only way to delete a list or a complete scope. Reopening a scope (or using the syntax described below with an appended ::) will <i>not</i> override previously written entries. Options can only be overridden by addressing a new value to them &#8211; lists and scopes can&#8217;t be overridden, only cleared. </p>
<p> All of the APT tools take an -o option which allows an arbitrary configuration directive to be specified on the command line. The syntax is a full option name (APT::Get::Assume-Yes for instance) followed by an equals sign then the new value of the option. To append a new element to a list, add a trailing :: to the name of the list. (As you might suspect, the scope syntax can&#8217;t be used on the command line.) </p>
<p> Note that appending items to a list using :: only works for one item per line, and that you should not use it in combination with the scope syntax (which adds :: implicitly). Using both syntaxes together will trigger a bug which some users unfortunately depend on: an option with the unusual name &quot;::&quot; which acts like every other option with a name. This introduces many problems; for one thing, users who write multiple lines in this <i>wrong</i> syntax in the hope of appending to a list will achieve the opposite, as only the last assignment for this option &quot;::&quot; will be used. Future versions of APT will raise errors and stop working if they encounter this misuse, so please correct such statements now while APT doesn&#8217;t explicitly complain about them.</p>
<h2>The Apt Group</h2>
<p>This group of options controls general APT behavior as well as holding the options for all of the tools. </p>
<p> <code>Architecture</code></p>
<dl>
<dd>System Architecture; sets the architecture to use when fetching files and parsing package lists. The internal default is the architecture apt was compiled for.</dl>
<p> <code>Architectures</code></p>
<dl>
<dd>All Architectures the system supports. For instance, CPUs implementing the amd64 (also called x86-64) instruction set are also able to execute binaries compiled for the i386 (x86) instruction set. This list is used when fetching files and parsing package lists. The initial default is always the system&#8217;s native architecture (APT::Architecture), and foreign architectures are added to the default list when they are registered via <code>dpkg &#8211;add-architecture</code>.</dl>
<p> <code>Compressor</code></p>
<dl>
<dd>This scope defines which compression formats are supported, how compression and decompression can be performed if support for this format isn&#8217;t built into apt directly and a cost-value indicating how costly it is to compress something in this format. As an example the following configuration stanza would allow apt to download and uncompress as well as create and store files with the low-cost .reversed file extension which it will pass to the command <code>rev</code> without additional commandline parameters for compression and uncompression: </p>
<dl>
<dd>
<pre>APT::Compressor::rev {
 Name &quot;rev&quot;;
 Extension &quot;.reversed&quot;;
 Binary &quot;rev&quot;;
 CompressArg {};
 UncompressArg {};
 Cost &quot;10&quot;;
};</pre>
</dl>
</dl>
<p> <code>Build-Profiles</code></p>
<dl>
<dd>List of all build profiles enabled for build-dependency resolution, without the &quot;profile.&quot; namespace prefix. By default this list is empty. The <code>DEB_BUILD_PROFILES</code> as used by <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1) overrides the list notation.</dl>
<p> <code>Default-Release</code></p>
<dl>
<dd>Default release to install packages from if more than one version is available. Contains release name, codename or release version. Examples: &#8216;stable&#8217;, &#8216;testing&#8217;, &#8216;unstable&#8217;, &#8216;bullseye&#8217;, &#8216;bookworm&#8217;, &#8216;4.0&#8217;, &#8216;5.0*&#8217;. See also <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5).</dl>
<p> <code>Ignore-Hold</code></p>
<dl>
<dd>Ignore held packages; this global option causes the problem resolver to ignore held packages in its decision making.</dl>
<p> <code>Clean-Installed</code></p>
<dl>
<dd>Defaults to on. When turned on the autoclean feature will remove any packages which can no longer be downloaded from the cache. If turned off then packages that are locally installed are also excluded from cleaning &#8211; but note that APT provides no direct means to reinstall them.</dl>
<p> <code>Immediate-Configure</code></p>
<dl>
<dd>Defaults to on, which will cause APT to install essential and important packages as soon as possible in an install/upgrade operation, in order to limit the effect of a failing <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) call. If this option is disabled, APT treats an important package in the same way as an extra package: between the unpacking of the package A and its configuration there can be many other unpack or configuration calls for other unrelated packages B, C etc. If these cause the <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) call to fail (e.g. because package B&#8217;s maintainer scripts generate an error), this results in a system state in which package A is unpacked but unconfigured &#8211; so any package depending on A is now no longer guaranteed to work, as its dependency on A is no longer satisfied. </p>
<p> The immediate configuration marker is also applied in the potentially problematic case of circular dependencies, since a dependency with the immediate flag is equivalent to a Pre-Dependency. In theory this allows APT to recognise a situation in which it is unable to perform immediate configuration, abort, and suggest to the user that the option should be temporarily deactivated in order to allow the operation to proceed. Note the use of the word &quot;theory&quot; here; in the real world this problem has rarely been encountered, in non-stable distribution versions, and was caused by wrong dependencies of the package in question or by a system in an already broken state; so you should not blindly disable this option, as the scenario mentioned above is not the only problem it can help to prevent in the first place. </p>
<p> Before a big operation like dist-upgrade is run with this option disabled you should try to explicitly install the package APT is unable to configure immediately; but please make sure you also report your problem to your distribution and to the APT team with the bug link below, so they can work on improving or correcting the upgrade process.</dl>
<p> <code>Force-LoopBreak</code></p>
<dl>
<dd>Never enable this option unless you <i>really</i> know what you are doing. It permits APT to temporarily remove an essential package to break a Conflicts/Conflicts or Conflicts/Pre-Depends loop between two essential packages. <i>Such a loop should never exist and is a grave bug</i>. This option will work if the essential packages are not <code>tar</code>, <code>gzip</code>, <code>libc</code>, <code>dpkg</code>, <code>dash</code> or anything that those packages depend on.</dl>
<p> <code>Cache-Start</code>, <code>Cache-Grow</code>, <code>Cache-Limit</code></p>
<dl>
<dd>APT uses since version 0.7.26 a resizable memory mapped cache file to store the available information. Cache-Start acts as a hint of the size the cache will grow to, and is therefore the amount of memory APT will request at startup. The default value is 20971520 bytes (~20 MB). Note that this amount of space needs to be available for APT; otherwise it will likely fail ungracefully, so for memory restricted devices this value should be lowered while on systems with a lot of configured sources it should be increased. Cache-Grow defines in bytes with the default of 1048576 (~1 MB) how much the cache size will be increased in the event the space defined by Cache-Start is not enough. This value will be applied again and again until either the cache is big enough to store all information or the size of the cache reaches the Cache-Limit. The default of Cache-Limit is 0 which stands for no limit. If Cache-Grow is set to 0 the automatic growth of the cache is disabled.</dl>
<p> <code>Build-Essential</code></p>
<dl>
<dd>Defines which packages are considered essential build dependencies.</dl>
<p> <code>Get</code></p>
<dl>
<dd>The Get subsection controls the <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) tool; please see its documentation for more information about the options here.</dl>
<p> <code>Cache</code></p>
<dl>
<dd>The Cache subsection controls the <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8) tool; please see its documentation for more information about the options here.</dl>
<p> <code>CDROM</code></p>
<dl>
<dd>The CDROM subsection controls the <code><a href="/docs/linux/man/8-apt-cdrom/">apt-cdrom</a></code>(8) tool; please see its documentation for more information about the options here.</dl>
<h2>The Acquire Group</h2>
<p>The Acquire group of options controls the download of packages as well as the various &quot;acquire methods&quot; responsible for the download itself (see also <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5)). </p>
<p> <code>Check-Date</code></p>
<dl>
<dd>Security related option defaulting to true, enabling time-related checks. Disabling it means that the machine&#8217;s time cannot be trusted, and APT will hence disable all time-related checks, such as <code>Check-Valid-Until</code> and verifying that the Date field of a release file is not in the future.</dl>
<p> <code>Max-FutureTime</code></p>
<dl>
<dd>Maximum time (in seconds) before its creation (as indicated by the Date header) that the Release file should be considered valid. The default value is 10. Archive specific settings can be made by appending the label of the archive to the option name. Preferably, the same can be achieved for specific <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries by using the <code>Date-Max-Future</code> option there.</dl>
<p> <code>Check-Valid-Until</code></p>
<dl>
<dd>Security related option defaulting to true, as giving a Release file&#8217;s validation an expiration date prevents replay attacks over a long timescale, and can also for example help users to identify mirrors that are no longer updated &#8211; but the feature depends on the correctness of the clock on the user system. Archive maintainers are encouraged to create Release files with the Valid-Until header, but if they don&#8217;t or a stricter value is desired the Max-ValidTime option below can be used. The <code>Check-Valid-Until</code> option of <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries should be preferred to disable the check selectively instead of using this global override.</dl>
<p> <code>Max-ValidTime</code></p>
<dl>
<dd>Maximum time (in seconds) after its creation (as indicated by the Date header) that the Release file should be considered valid. If the Release file itself includes a Valid-Until header the earlier date of the two is used as the expiration date. The default value is 0 which stands for &quot;valid forever&quot;. Archive specific settings can be made by appending the label of the archive to the option name. Preferably, the same can be achieved for specific <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries by using the <code>Valid-Until-Max</code> option there.</dl>
<p> <code>Min-ValidTime</code></p>
<dl>
<dd>Minimum time (in seconds) after its creation (as indicated by the Date header) that the Release file should be considered valid. Use this if you need to use a seldom updated (local) mirror of a more frequently updated archive with a Valid-Until header instead of completely disabling the expiration date checking. Archive specific settings can and should be used by appending the label of the archive to the option name. Preferably, the same can be achieved for specific <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries by using the <code>Valid-Until-Min</code> option there.</dl>
<p> <code>AllowTLS</code></p>
<dl>
<dd>Allow use of the internal TLS support in the http method. If set to false, this completely disables support for TLS in apt&#8217;s own methods (excluding the curl-based https method). No TLS-related functions will be called anymore.</dl>
<p> <code>PDiffs</code></p>
<dl>
<dd>Try to download deltas called PDiffs for indexes (like Packages files) instead of downloading whole ones. True by default. Preferably, this can be set for specific <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries or index files by using the <code>PDiffs</code> option there. </p>
<p> Two sub-options to limit the use of PDiffs are also available: FileLimit can be used to specify a maximum number of PDiff files should be downloaded to update a file. SizeLimit on the other hand is the maximum percentage of the size of all patches compared to the size of the targeted file. If one of these limits is exceeded the complete file is downloaded instead of the patches.</dl>
<p> <code>By-Hash</code></p>
<dl>
<dd>Try to download indexes via an URI constructed from a hashsum of the expected file rather than downloaded via a well-known stable filename. True by default, but automatically disabled if the source indicates no support for it. Usage can be forced with the special value &quot;force&quot;. Preferably, this can be set for specific <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries or index files by using the <code>By-Hash</code> option there.</dl>
<p> <code>Queue-Mode</code></p>
<dl>
<dd>Queuing mode; Queue-Mode can be one of host or access which determines how APT parallelizes outgoing connections. host means that one connection per target host will be opened, access means that one connection per URI type will be opened.</dl>
<p> <code>Retries</code></p>
<dl>
<dd>Number of retries to perform. If this is non-zero APT will retry failed files the given number of times.</dl>
<p> <code>Source-Symlinks</code></p>
<dl>
<dd>Use symlinks for source archives. If set to true then source archives will be symlinked when possible instead of copying. True is the default.</dl>
<p> <code>http</code> <code>https</code></p>
<dl>
<dd>The options in these scopes configure APT&#8217;s acquire transports for the protocols HTTP and HTTPS and are documented in the <code><a href="/docs/linux/man/1-apt-transport-http/">apt-transport-http</a></code>(1) and <code><a href="/docs/linux/man/1-apt-transport-https/">apt-transport-https</a></code>(1) manpages respectively.</dl>
<p> <code>ftp</code></p>
<dl>
<dd>ftp::Proxy sets the default proxy to use for FTP URIs. It is in the standard form of <a href="ftp://[[user][:pass]@]host[:port]/.">ftp://[[user][:pass]@]host[:port]/.</a> Per host proxies can also be specified by using the form ftp::Proxy::&lt;host&gt; with the special keyword DIRECT meaning to use no proxies. If no one of the above settings is specified, <code>ftp_proxy</code> environment variable will be used. To use an FTP proxy you will have to set the ftp::ProxyLogin script in the configuration file. This entry specifies the commands to send to tell the proxy server what to connect to. Please see /usr/share/doc/apt/examples/configure-index.gz for an example of how to do this. The substitution variables representing the corresponding URI component are $(PROXY_USER), $(PROXY_PASS), $(SITE_USER), $(SITE_PASS), $(SITE) and $(SITE_PORT). </p>
<p> The option timeout sets the timeout timer used by the method; this value applies to the connection as well as the data timeout. </p>
<p> Several settings are provided to control passive mode. Generally it is safe to leave passive mode on; it works in nearly every environment. However, some situations require that passive mode be disabled and port mode FTP used instead. This can be done globally or for connections that go through a proxy or for a specific host (see the sample config file for examples). </p>
<p> It is possible to proxy FTP over HTTP by setting the <code>ftp_proxy</code> environment variable to an HTTP URL &#8211; see the discussion of the http method above for syntax. You cannot set this in the configuration file and it is not recommended to use FTP over HTTP due to its low efficiency. </p>
<p> The setting ForceExtended controls the use of RFC2428 EPSV and EPRT commands. The default is false, which means these commands are only used if the control connection is IPv6. Setting this to true forces their use even on IPv4 connections. Note that most FTP servers do not support RFC2428.</dl>
<p> <code>cdrom</code></p>
<dl>
<dd>For URIs using the cdrom method, the only configurable option is the mount point, cdrom::Mount, which must be the mount point for the CD-ROM (or DVD, or whatever) drive as specified in /etc/fstab. It is possible to provide alternate mount and unmount commands if your mount point cannot be listed in the fstab. The syntax is to put </p>
<dl>
<dd>
<pre>/cdrom/::Mount &quot;foo&quot;;</pre>
</dl>
<p> within the cdrom block. It is important to have the trailing slash. Unmount commands can be specified using UMount.</dl>
<p> <code>gpgv</code></p>
<dl>
<dd>For GPGV URIs the only configurable option is gpgv::Options, which passes additional parameters to gpgv.</dl>
<p> <code>CompressionTypes</code></p>
<dl>
<dd>List of compression types which are understood by the acquire methods. Files like Packages can be available in various compression formats. By default the acquire methods can decompress and recompress many common formats like <code>xz</code> and <code>gzip</code>; with this scope the supported formats can be queried, modified as well as support for more formats added (see also <code>APT::Compressor</code>). The syntax for this is: </p>
<dl>
<dd>
<pre>Acquire::CompressionTypes::<i>FileExtension</i> &quot;<i>Methodname</i>&quot;;</pre>
</dl>
<p> Also, the Order subgroup can be used to define in which order the acquire system will try to download the compressed files. The acquire system will try the first and proceed with the next compression type in this list on error, so to prefer one over the other type simply add the preferred type first &#8211; types not already added will be implicitly appended to the end of the list, so e.g. </p>
<dl>
<dd>
<pre>Acquire::CompressionTypes::Order:: &quot;gz&quot;;</pre>
</dl>
<p> can be used to prefer <code>gzip</code> compressed files over all other compression formats. If <code>xz</code> should be preferred over <code>gzip</code> and <code>bzip2</code> the configure setting should look like this: </p>
<dl>
<dd>
<pre>Acquire::CompressionTypes::Order { &quot;xz&quot;; &quot;gz&quot;; };</pre>
</dl>
<p> It is not needed to add bz2 to the list explicitly as it will be added automatically. </p>
<p> Note that the Dir::Bin::<i>Methodname</i> will be checked at run time. If this option has been set and support for this format isn&#8217;t directly built into apt, the method will only be used if this file exists; e.g. for the bzip2 method (the inbuilt) setting is: </p>
<dl>
<dd>
<pre>Dir::Bin::bzip2 &quot;/bin/bzip2&quot;;</pre>
</dl>
<p> Note also that list entries specified on the command line will be added at the end of the list specified in the configuration files, but before the default entries. To prefer a type in this case over the ones specified in the configuration files you can set the option direct &#8211; not in list style. This will not override the defined list; it will only prefix the list with this type. </p>
<p> The special type uncompressed can be used to give uncompressed files a preference, but note that most archives don&#8217;t provide uncompressed files so this is mostly only usable for local mirrors.</dl>
<p> <code>GzipIndexes</code></p>
<dl>
<dd>When downloading gzip compressed indexes (Packages, Sources, or Translations), keep them gzip compressed locally instead of unpacking them. This saves quite a lot of disk space at the expense of more CPU requirements when building the local package caches. False by default.</dl>
<p> <code>Languages</code></p>
<dl>
<dd>The Languages subsection controls which Translation files are downloaded and in which order APT tries to display the description-translations. APT will try to display the first available description in the language which is listed first. Languages can be defined with their short or long language codes. Note that not all archives provide Translation files for every language &#8211; the long language codes are especially rare. </p>
<p> The default list includes &quot;environment&quot; and &quot;en&quot;. &quot;environment&quot; has a special meaning here: it will be replaced at runtime with the language codes extracted from the LC_MESSAGES environment variable. It will also ensure that these codes are not included twice in the list. If LC_MESSAGES is set to &quot;C&quot; only the Translation-en file (if available) will be used. To force APT to use no Translation file use the setting Acquire::Languages=none. &quot;none&quot; is another special meaning code which will stop the search for a suitable Translation file. This tells APT to download these translations too, without actually using them unless the environment specifies the languages. So the following example configuration will result in the order &quot;en, de&quot; in an English locale or &quot;de, en&quot; in a German one. Note that &quot;fr&quot; is downloaded, but not used unless APT is used in a French locale (where the order would be &quot;fr, de, en&quot;). </p>
<dl>
<dd>
<pre>Acquire::Languages { &quot;environment&quot;; &quot;de&quot;; &quot;en&quot;; &quot;none&quot;; &quot;fr&quot;; };</pre>
</dl>
<p> Note: To prevent problems resulting from APT being executed in different environments (e.g. by different users or by other programs) all Translation files which are found in /var/lib/apt/lists/ will be added to the end of the list (after an implicit &quot;none&quot;).</dl>
<p> <code>ForceIPv4</code></p>
<dl>
<dd>When downloading, force to use only the IPv4 protocol.</dl>
<p> <code>ForceIPv6</code></p>
<dl>
<dd>When downloading, force to use only the IPv6 protocol.</dl>
<p> <code>MaxReleaseFileSize</code></p>
<dl>
<dd>The maximum file size of Release/Release.gpg/InRelease files. The default is 10MB.</dl>
<p> <code>EnableSrvRecords</code></p>
<dl>
<dd>This option controls if apt will use the DNS SRV server record as specified in RFC 2782 to select an alternative server to connect to. The default is &quot;true&quot;.</dl>
<p> <code>AllowInsecureRepositories</code></p>
<dl>
<dd>Allow update operations to load data files from repositories without sufficient security information. The default value is &quot;false&quot;. Concept, implications as well as alternatives are detailed in <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8).</dl>
<p> <code>AllowWeakRepositories</code></p>
<dl>
<dd>Allow update operations to load data files from repositories which provide security information, but these are deemed no longer cryptographically strong enough. The default value is &quot;false&quot;. Concept, implications as well as alternatives are detailed in <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8).</dl>
<p> <code>AllowDowngradeToInsecureRepositories</code></p>
<dl>
<dd>Allow that a repository that was previously gpg signed to become unsigned during an update operation. When there is no valid signature for a previously trusted repository apt will refuse the update. This option can be used to override this protection. You almost certainly never want to enable this. The default is false. Concept, implications as well as alternatives are detailed in <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8).</dl>
<p> <code>Changelogs::URI</code> scope</p>
<dl>
<dd>Acquiring changelogs can only be done if an URI is known from where to get them. Preferable the Release file indicates this in a &#8216;Changelogs&#8217; field. If this isn&#8217;t available the Label/Origin field of the Release file is used to check if a Acquire::Changelogs::URI::Label::<i>LABEL</i> or Acquire::Changelogs::URI::Origin::<i>ORIGIN</i> option exists and if so this value is taken. The value in the Release file can be overridden with Acquire::Changelogs::URI::Override::Label::<i>LABEL</i> or Acquire::Changelogs::URI::Override::Origin::<i>ORIGIN</i>. The value should be a normal URI to a text file, except that package specific data is replaced with the placeholder @CHANGEPATH@. The value for it is: 1. if the package is from a component (e.g. main) this is the first part otherwise it is omitted, 2. the first letter of source package name, except if the source package name starts with &#8216;lib&#8217; in which case it will be the first four letters. 3. The complete source package name. 4. the complete name again and 5. the source version. The first (if present), second, third and fourth part are separated by a slash (&#8216;/&#8217;) and between the fourth and fifth part is an underscore (&#8216;_&#8217;). The special value &#8216;no&#8217; is available for this option indicating that this source can&#8217;t be used to acquire changelog files from. Another source will be tried if available in this case.</dl>
<h2>Binary Specific Configuration</h2>
<p>Especially with the introduction of the <code>apt</code> binary it can be useful to set certain options only for a specific binary as even options which look like they would effect only a certain binary like <code>APT::Get::Show-Versions</code> effect <code>apt-get</code> as well as <code>apt</code>. </p>
<p> Setting an option for a specific binary only can be achieved by setting the option inside the <code>Binary::</code><i>specific-binary</i> scope. Setting the option <code>APT::Get::Show-Versions</code> for the <code>apt</code> only can e.g. by done by setting <code>Binary::apt::APT::Get::Show-Versions</code> instead. </p>
<p> Note that as seen in the DESCRIPTION section further above you can&#8217;t set binary-specific options on the commandline itself nor in configuration files loaded via the commandline.</p>
<h2>Directories</h2>
<p>The Dir::State section has directories that pertain to local state information. lists is the directory to place downloaded package lists in and status is the name of the <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) status file. preferences is the name of the APT preferences file. Dir::State contains the default directory to prefix on all sub-items if they do not start with / or ./. </p>
<p> Dir::Cache contains locations pertaining to local cache information, such as the two package caches srcpkgcache and pkgcache as well as the location to place downloaded archives, Dir::Cache::archives. Generation of caches can be turned off by setting pkgcache or srcpkgcache to &quot;&quot;. This will slow down startup but save disk space. It is probably preferable to turn off the pkgcache rather than the srcpkgcache. Like Dir::State the default directory is contained in Dir::Cache </p>
<p> Dir::Etc contains the location of configuration files, sourcelist gives the location of the sourcelist and main is the default configuration file (setting has no effect, unless it is done from the config file specified by <code>APT_CONFIG</code>). </p>
<p> The Dir::Parts setting reads in all the config fragments in lexical order from the directory specified. After this is done then the main config file is loaded. </p>
<p> Binary programs are pointed to by Dir::Bin. Dir::Bin::Methods specifies the location of the method handlers and gzip, bzip2, lzma, dpkg, apt-get dpkg-source dpkg-buildpackage and apt-cache specify the location of the respective programs. </p>
<p> The configuration item RootDir has a special meaning. If set, all paths will be relative to RootDir, <i>even paths that are specified absolutely</i>. So, for instance, if RootDir is set to /tmp/staging and Dir::State::status is set to /var/lib/dpkg/status, then the status file will be looked up in /tmp/staging/var/lib/dpkg/status. If you want to prefix only relative paths, set Dir instead. </p>
<p> The Ignore-Files-Silently list can be used to specify which files APT should silently ignore while parsing the files in the fragment directories. Per default a file which ends with .disabled, ~, .bak or .dpkg-[a-z]+ is silently ignored. As seen in the last default value these patterns can use regular expression syntax.</p>
<h2>Apt In Dselect</h2>
<p>When APT is used as a <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1) method several configuration directives control the default behavior. These are in the DSelect section. </p>
<p> <code>Clean</code></p>
<dl>
<dd>Cache Clean mode; this value may be one of always, prompt, auto, pre-auto and never. always and prompt will remove all packages from the cache after upgrading, prompt (the default) does so conditionally. auto removes only those packages which are no longer downloadable (replaced with a new version for instance). pre-auto performs this action before downloading new packages.</dl>
<p> <code>options</code></p>
<dl>
<dd>The contents of this variable are passed to <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) as command line options when it is run for the install phase.</dl>
<p> <code>Updateoptions</code></p>
<dl>
<dd>The contents of this variable are passed to <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) as command line options when it is run for the update phase.</dl>
<p> <code>PromptAfterUpdate</code></p>
<dl>
<dd>If true the [U]pdate operation in <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1) will always prompt to continue. The default is to prompt only on error.</dl>
<h2>HOW APT CALLS <a href="/docs/linux/man/1-dpkg/">DPKG</a>(1)</h2>
<p>Several configuration directives control how APT invokes <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). These are in the DPkg section. </p>
<p> <code>options</code></p>
<dl>
<dd>This is a list of options to pass to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). The options must be specified using the list notation and each list item is passed as a single argument to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1).</dl>
<p> <code>Path</code></p>
<dl>
<dd>This is a string that defines the <code>PATH</code> environment variable used when running dpkg. It may be set to any valid value of that environment variable; or the empty string, in which case the variable is not changed.</dl>
<p> <code>Pre-Invoke</code>, <code>Post-Invoke</code></p>
<dl>
<dd>This is a list of shell commands to run before/after invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). Like options this must be specified in list notation. The commands are invoked in order using /bin/sh; should any fail APT will abort.</dl>
<p> <code>Pre-Install-Pkgs</code></p>
<dl>
<dd>This is a list of shell commands to run before invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). Like options this must be specified in list notation. The commands are invoked in order using /bin/sh; should any fail APT will abort. APT will pass the filenames of all .deb files it is going to install to the commands, one per line on the requested file descriptor, defaulting to standard input. </p>
<p> Version 2 of this protocol sends more information through the requested file descriptor: a line with the text VERSION 2, the APT configuration space, and a list of package actions with filename and version information. </p>
<p> Each configuration directive line has the form key=value. Special characters (equal signs, newlines, nonprintable characters, quotation marks, and percent signs in key and newlines, nonprintable characters, and percent signs in value) are %-encoded. Lists are represented by multiple key::=value lines with the same key. The configuration section ends with a blank line. </p>
<p> Package action lines consist of five fields in Version 2: package name (without architecture qualification even if foreign), old version, direction of version change (&lt; for upgrades, &gt; for downgrades, = for no change), new version, action. The version fields are &quot;-&quot; for no version at all (for example when installing a package for the first time; no version is treated as earlier than any real version, so that is an upgrade, indicated as &#8211; &lt; 1.23.4). The action field is &quot;**CONFIGURE**&quot; if the package is being configured, &quot;**REMOVE**&quot; if it is being removed, or the filename of a .deb file if it is being unpacked. </p>
<p> In Version 3 after each version field follows the architecture of this version, which is &quot;-&quot; if there is no version, and a field showing the MultiArch type &quot;same&quot;, &quot;foreign&quot;, &quot;allowed&quot; or &quot;none&quot;. Note that &quot;none&quot; is an incorrect typename which is just kept to remain compatible, it should be read as &quot;no&quot; and users are encouraged to support both. </p>
<p> The version of the protocol to be used for the command <i>cmd</i> can be chosen by setting DPkg::Tools::options::<i>cmd</i>::Version accordingly, the default being version 1. If APT isn&#8217;t supporting the requested version it will send the information in the highest version it has support for instead. </p>
<p> The file descriptor to be used to send the information can be requested with DPkg::Tools::options::<i>cmd</i>::InfoFD which defaults to 0 for standard input and is available since version 0.9.11. Support for the option can be detected by looking for the environment variable <code>APT_HOOK_INFO_FD</code> which contains the number of the used file descriptor as a confirmation.</dl>
<p> <code>Run-Directory</code></p>
<dl>
<dd>APT chdirs to this directory before invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), the default is /.</dl>
<p> <code>Build-options</code></p>
<dl>
<dd>These options are passed to <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1) when compiling packages; the default is to disable signing and produce all binaries.</dl>
<p> <code>DPkg::ConfigurePending</code></p>
<dl>
<dd>If this option is set APT will call <code>dpkg &#8211;configure &#8211;pending</code> to let <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) handle all required configurations and triggers. This option is activated by default, but deactivating it could be useful if you want to run APT multiple times in a row &#8211; e.g. in an installer. In this scenario you could deactivate this option in all but the last run.</dl>
<h2>Periodic And Archives Options</h2>
<p>APT::Periodic and APT::Archives groups of options configure behavior of apt periodic updates, which is done by the /usr/lib/apt/apt.systemd.daily script. See the top of this script for the brief documentation of these options.</p>
<h2>Debug Options</h2>
<p>Enabling options in the Debug:: section will cause debugging information to be sent to the standard error stream of the program utilizing the apt libraries, or enable special program modes that are primarily useful for debugging the behavior of apt. Most of these options are not interesting to a normal user, but a few may be: </p>
<dl>
<dd>&bull; Debug::pkgProblemResolver enables output about the decisions made by dist-upgrade, upgrade, install, remove, purge.</dl>
<dl>
<dd>&bull; Debug::NoLocking disables all file locking. This can be used to run some operations (for instance, apt-get -s install) as a non-root user.</dl>
<dl>
<dd>&bull; Debug::pkgDPkgPM prints out the actual command line each time that apt invokes <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1).</dl>
<dl>
<dd>&bull; Debug::IdentCdrom disables the inclusion of statfs data in CD-ROM IDs.</dl>
<p> A full list of debugging options to apt follows. </p>
<p> <code>Debug::Acquire::cdrom</code></p>
<dl>
<dd>Print information related to accessing cdrom:// sources.</dl>
<p> <code>Debug::Acquire::ftp</code></p>
<dl>
<dd>Print information related to downloading packages using FTP.</dl>
<p> <code>Debug::Acquire::http</code></p>
<dl>
<dd>Print information related to downloading packages using HTTP.</dl>
<p> <code>Debug::Acquire::https</code></p>
<dl>
<dd>Print information related to downloading packages using HTTPS.</dl>
<p> <code>Debug::Acquire::gpgv</code></p>
<dl>
<dd>Print information related to verifying cryptographic signatures using gpg.</dl>
<p> <code>Debug::aptcdrom</code></p>
<dl>
<dd>Output information about the process of accessing collections of packages stored on CD-ROMs.</dl>
<p> <code>Debug::BuildDeps</code></p>
<dl>
<dd>Describes the process of resolving build-dependencies in <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8).</dl>
<p> <code>Debug::Hashes</code></p>
<dl>
<dd>Output each cryptographic hash that is generated by the apt libraries.</dl>
<p> <code>Debug::IdentCDROM</code></p>
<dl>
<dd>Do not include information from statfs, namely the number of used and free blocks on the CD-ROM filesystem, when generating an ID for a CD-ROM.</dl>
<p> <code>Debug::NoLocking</code></p>
<dl>
<dd>Disable all file locking. For instance, this will allow two instances of &#8220;apt-get update&#8221; to run at the same time.</dl>
<p> <code>Debug::pkgAcquire</code></p>
<dl>
<dd>Log when items are added to or removed from the global download queue.</dl>
<p> <code>Debug::pkgAcquire::Auth</code></p>
<dl>
<dd>Output status messages and errors related to verifying checksums and cryptographic signatures of downloaded files.</dl>
<p> <code>Debug::pkgAcquire::Diffs</code></p>
<dl>
<dd>Output information about downloading and applying package index list diffs, and errors relating to package index list diffs.</dl>
<p> <code>Debug::pkgAcquire::RRed</code></p>
<dl>
<dd>Output information related to patching apt package lists when downloading index diffs instead of full indices.</dl>
<p> <code>Debug::pkgAcquire::Worker</code></p>
<dl>
<dd>Log all interactions with the sub-processes that actually perform downloads.</dl>
<p> <code>Debug::pkgAutoRemove</code></p>
<dl>
<dd>Log events related to the automatically-installed status of packages and to the removal of unused packages.</dl>
<p> <code>Debug::pkgDepCache::AutoInstall</code></p>
<dl>
<dd>Generate debug messages describing which packages are being automatically installed to resolve dependencies. This corresponds to the initial auto-install pass performed in, e.g., apt-get install, and not to the full apt dependency resolver; see Debug::pkgProblemResolver for that.</dl>
<p> <code>Debug::pkgDepCache::Marker</code></p>
<dl>
<dd>Generate debug messages describing which packages are marked as keep/install/remove while the ProblemResolver does his work. Each addition or deletion may trigger additional actions; they are shown indented two additional spaces under the original entry. The format for each line is MarkKeep, MarkDelete or MarkInstall followed by package-name &lt;a.b.c -&gt; d.e.f | x.y.z&gt; (section) where a.b.c is the current version of the package, d.e.f is the version considered for installation and x.y.z is a newer version, but not considered for installation (because of a low pin score). The later two can be omitted if there is none or if it is the same as the installed version. section is the name of the section the package appears in.</dl>
<p> <code>Debug::pkgDPkgPM</code></p>
<dl>
<dd>When invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), output the precise command line with which it is being invoked, with arguments separated by a single space character.</dl>
<p> <code>Debug::pkgDPkgProgressReporting</code></p>
<dl>
<dd>Output all the data received from <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) on the status file descriptor and any errors encountered while parsing it.</dl>
<p> <code>Debug::pkgOrderList</code></p>
<dl>
<dd>Generate a trace of the algorithm that decides the order in which apt should pass packages to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1).</dl>
<p> <code>Debug::pkgPackageManager</code></p>
<dl>
<dd>Output status messages tracing the steps performed when invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1).</dl>
<p> <code>Debug::pkgPolicy</code></p>
<dl>
<dd>Output the priority of each package list on startup.</dl>
<p> <code>Debug::pkgProblemResolver</code></p>
<dl>
<dd>Trace the execution of the dependency resolver (this applies only to what happens when a complex dependency problem is encountered).</dl>
<p> <code>Debug::pkgProblemResolver::ShowScores</code></p>
<dl>
<dd>Display a list of all installed packages with their calculated score used by the pkgProblemResolver. The description of the package is the same as described in Debug::pkgDepCache::Marker</dl>
<p> <code>Debug::sourceList</code></p>
<dl>
<dd>Print information about the vendors read from /etc/apt/vendors.list.</dl>
<p> <code>Debug::RunScripts</code></p>
<dl>
<dd>Display the external commands that are called by apt hooks. This includes e.g. the config options DPkg::{Pre,Post}-Invoke or APT::Update::{Pre,Post}-Invoke.</dl>
<h2>Examples</h2>
<p>/usr/share/doc/apt/examples/configure-index.gz is a configuration file showing example values for all possible options.</p>
<h2>Files</h2>
<p>/etc/apt/apt.conf</p>
<dl>
<dd>APT configuration file. Configuration Item: Dir::Etc::Main.</dl>
<p> /etc/apt/apt.conf.d/</p>
<dl>
<dd>APT configuration file fragments. Configuration Item: Dir::Etc::Parts.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8), <code><a href="/docs/linux/man/8-apt-config/">apt-config</a></code>(8), <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5).</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Authors</h2>
<p><code>Jason Gunthorpe</code></p>
<dl>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dd></dl>
<p> <code>Daniel Burrows</code> &lt;dburrows [at] debian.org&gt;</p>
<dl>
<dd>Initial documentation of Debug::*.</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
