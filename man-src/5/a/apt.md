---
title: "apt(5)"
name: "apt"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apt/"
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
<dd>4. the command line options are applied to override the configuration directives or to load even more configuration files.</dl>
<h2>Syntax</h2>
<p>The configuration file is organized in a tree with options organized into functional groups. Option specification is given with a double colon notation; for instance APT::Get::Assume-Yes is an option within the APT tool group, for the Get tool. Options do not inherit from their parent groups. </p>
<p> Syntactically the configuration language is modeled after what the ISC tools such as bind and dhcp use. Lines starting with // are treated as comments (ignored), as well as all text between /* and */, just like C/C++ comments. Each line is of the form APT::Get::Assume-Yes &quot;true&quot;;. The quotation marks and trailing semicolon are required. The value must be on one line, and there is no kind of string concatenation. Values must not include backslashes or extra quotation marks. Option names are made up of alphanumeric characters and the characters &quot;/-:._+&quot;. A new scope can be opened with curly braces, like this: </p>
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
<p> <code>Build-Profiles</code></p>
<dl>
<dd>List of all build profiles enabled for build-dependency resolution, without the &quot;profile.&quot; namespace prefix. By default this list is empty. The <code>DEB_BUILD_PROFILES</code> as used by <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1) overrides the list notation.</dl>
<p> <code>Default-Release</code></p>
<dl>
<dd>Default release to install packages from if more than one version is available. Contains release name, codename or release version. Examples: &#8216;stable&#8217;, &#8216;testing&#8217;, &#8216;unstable&#8217;, &#8216;wheezy&#8217;, &#8216;jessie&#8217;, &#8216;4.0&#8217;, &#8216;5.0*&#8217;. See also <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5).</dl>
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
<p> Before a big operation like dist-upgrade is run with this option disabled you should try to explicitly install the package APT is unable to configure immediately; but please make sure you also report your problem to your distribution and to the APT team with the buglink below, so they can work on improving or correcting the upgrade process.</dl>
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
<p> <code>Check-Valid-Until</code></p>
<dl>
<dd>Security related option defaulting to true, as giving a Release file&#8217;s validation an expiration date prevents replay attacks over a long timescale, and can also for example help users to identify mirrors that are no longer updated &#8211; but the feature depends on the correctness of the clock on the user system. Archive maintainers are encouraged to create Release files with the Valid-Until header, but if they don&#8217;t or a stricter value is desired the Max-ValidTime option below can be used.</dl>
<p> <code>Max-ValidTime</code></p>
<dl>
<dd>Maximum time (in seconds) after its creation (as indicated by the Date header) that the Release file should be considered valid. If the Release file itself includes a Valid-Until header the earlier date of the two is used as the expiration date. The default value is 0 which stands for &quot;valid forever&quot;. Archive specific settings can be made by appending the label of the archive to the option name.</dl>
<p> <code>Min-ValidTime</code></p>
<dl>
<dd>Minimum time (in seconds) after its creation (as indicated by the Date header) that the Release file should be considered valid. Use this if you need to use a seldom updated (local) mirror of a more frequently updated archive with a Valid-Until header instead of completely disabling the expiration date checking. Archive specific settings can and should be used by appending the label of the archive to the option name.</dl>
<p> <code>PDiffs</code></p>
<dl>
<dd>Try to download deltas called PDiffs for indexes (like Packages files) instead of downloading whole ones. True by default. </p>
<p> Two sub-options to limit the use of PDiffs are also available: FileLimit can be used to specify a maximum number of PDiff files should be downloaded to update a file. SizeLimit on the other hand is the maximum percentage of the size of all patches compared to the size of the targeted file. If one of these limits is exceeded the complete file is downloaded instead of the patches.</dl>
<p> <code>Queue-Mode</code></p>
<dl>
<dd>Queuing mode; Queue-Mode can be one of host or access which determines how APT parallelizes outgoing connections. host means that one connection per target host will be opened, access means that one connection per URI type will be opened.</dl>
<p> <code>Retries</code></p>
<dl>
<dd>Number of retries to perform. If this is non-zero APT will retry failed files the given number of times.</dl>
<p> <code>Source-Symlinks</code></p>
<dl>
<dd>Use symlinks for source archives. If set to true then source archives will be symlinked when possible instead of copying. True is the default.</dl>
<p> <code>http</code></p>
<dl>
<dd>http::Proxy sets the default proxy to use for HTTP URIs. It is in the standard form of <a rel="nofollow" href="http://[[user][:pass]@]host[:port]/.">http://[[user][:pass]@]host[:port]/.</a> Per host proxies can also be specified by using the form http::Proxy::&lt;host&gt; with the special keyword DIRECT meaning to use no proxies. If no one of the above settings is specified, <code>http_proxy</code> environment variable will be used. </p>
<p> Three settings are provided for cache control with HTTP/1.1 compliant proxy caches. No-Cache tells the proxy not to use its cached response under any circumstances. Max-Age sets the allowed maximum age (in seconds) of an index file in the cache of the proxy. No-Store specifies that the proxy should not store the requested archive files in its cache, which can be used to prevent the proxy from polluting its cache with (big) .deb files. </p>
<p> The option timeout sets the timeout timer used by the method; this value applies to the connection as well as the data timeout. </p>
<p> The setting Acquire::http::Pipeline-Depth can be used to enable HTTP pipelining (RFC 2616 section 8.1.2.2) which can be beneficial e.g. on high-latency connections. It specifies how many requests are sent in a pipeline. Previous APT versions had a default of 10 for this setting, but the default value is now 0 (= disabled) to avoid problems with the ever-growing amount of webservers and proxies which choose to not conform to the HTTP/1.1 specification. </p>
<p> Acquire::http::AllowRedirect controls whether APT will follow redirects, which is enabled by default. </p>
<p> The used bandwidth can be limited with Acquire::http::Dl-Limit which accepts integer values in kilobytes per second. The default value is 0 which deactivates the limit and tries to use all available bandwidth. Note that this option implicitly disables downloading from multiple servers at the same time. </p>
<p> Acquire::http::User-Agent can be used to set a different User-Agent for the http download method as some proxies allow access for clients only if the client uses a known identifier. </p>
<p> Acquire::http::Proxy-Auto-Detect can be used to specify an external command to discover the http proxy to use. Apt expects the command to output the proxy on stdout in the style <a rel="nofollow" href="http://proxy:port/.">http://proxy:port/.</a> This will override the generic Acquire::http::Proxy but not any specific host proxy configuration set via Acquire::http::Proxy::$HOST. See the <code><a href="/docs/linux/man/1-squid-deb-proxy-client/">squid-deb-proxy-client</a></code>(1) package for an example implementation that uses avahi. This option takes precedence over the legacy option name ProxyAutoDetect.</dl>
<p> <code>https</code></p>
<dl>
<dd>The Cache-control, Timeout, AllowRedirect, Dl-Limit and proxy options work for HTTPS URIs in the same way as for the http method, and default to the same values if they are not explicitly set. The Pipeline-Depth option is not yet supported. </p>
<p> CaInfo suboption specifies place of file that holds info about trusted certificates. &lt;host&gt;::CaInfo is the corresponding per-host option. Verify-Peer boolean suboption determines whether or not the server&#8217;s host certificate should be verified against trusted certificates. &lt;host&gt;::Verify-Peer is the corresponding per-host option. Verify-Host boolean suboption determines whether or not the server&#8217;s hostname should be verified. &lt;host&gt;::Verify-Host is the corresponding per-host option. SslCert determines what certificate to use for client authentication. &lt;host&gt;::SslCert is the corresponding per-host option. SslKey determines what private key to use for client authentication. &lt;host&gt;::SslKey is the corresponding per-host option. SslForceVersion overrides default SSL version to use. It can contain either of the strings &#8216;TLSv1&#8217; or &#8216;SSLv3&#8217;. &lt;host&gt;::SslForceVersion is the corresponding per-host option.</dl>
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
<dd>List of compression types which are understood by the acquire methods. Files like Packages can be available in various compression formats. By default the acquire methods can decompress <code>bzip2</code>, <code>lzma</code> and <code>gzip</code> compressed files; with this setting more formats can be added on the fly or the used method can be changed. The syntax for this is: </p>
<dl>
<dd>
<pre>Acquire::CompressionTypes::<i>FileExtension</i> &quot;<i>Methodname</i>&quot;;</pre>
</dl>
<p> Also, the Order subgroup can be used to define in which order the acquire system will try to download the compressed files. The acquire system will try the first and proceed with the next compression type in this list on error, so to prefer one over the other type simply add the preferred type first &#8211; default types not already added will be implicitly appended to the end of the list, so e.g. </p>
<dl>
<dd>
<pre>Acquire::CompressionTypes::Order:: &quot;gz&quot;;</pre>
</dl>
<p> can be used to prefer <code>gzip</code> compressed files over <code>bzip2</code> and <code>lzma</code>. If <code>lzma</code> should be preferred over <code>gzip</code> and <code>bzip2</code> the configure setting should look like this: </p>
<dl>
<dd>
<pre>Acquire::CompressionTypes::Order { &quot;lzma&quot;; &quot;gz&quot;; };</pre>
</dl>
<p> It is not needed to add bz2 to the list explicitly as it will be added automatically. </p>
<p> Note that the Dir::Bin::<i>Methodname</i> will be checked at run time. If this option has been set, the method will only be used if this file exists; e.g. for the bzip2 method (the inbuilt) setting is: </p>
<dl>
<dd>
<pre>Dir::Bin::bzip2 &quot;/bin/bzip2&quot;;</pre>
</dl>
<p> Note also that list entries specified on the command line will be added at the end of the list specified in the configuration files, but before the default entries. To prefer a type in this case over the ones specified in the configuration files you can set the option direct &#8211; not in list style. This will not override the defined list; it will only prefix the list with this type. </p>
<p> The special type uncompressed can be used to give uncompressed files a preference, but note that most archives don&#8217;t provide uncompressed files so this is mostly only useable for local mirrors.</dl>
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
<h2>Directories</h2>
<p>The Dir::State section has directories that pertain to local state information. lists is the directory to place downloaded package lists in and status is the name of the <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) status file. preferences is the name of the APT preferences file. Dir::State contains the default directory to prefix on all sub-items if they do not start with / or ./. </p>
<p> Dir::Cache contains locations pertaining to local cache information, such as the two package caches srcpkgcache and pkgcache as well as the location to place downloaded archives, Dir::Cache::archives. Generation of caches can be turned off by setting their names to the empty string. This will slow down startup but save disk space. It is probably preferable to turn off the pkgcache rather than the srcpkgcache. Like Dir::State the default directory is contained in Dir::Cache </p>
<p> Dir::Etc contains the location of configuration files, sourcelist gives the location of the sourcelist and main is the default configuration file (setting has no effect, unless it is done from the config file specified by <code>APT_CONFIG</code>). </p>
<p> The Dir::Parts setting reads in all the config fragments in lexical order from the directory specified. After this is done then the main config file is loaded. </p>
<p> Binary programs are pointed to by Dir::Bin. Dir::Bin::Methods specifies the location of the method handlers and gzip, bzip2, lzma, dpkg, apt-getdpkg-sourcedpkg-buildpackage and apt-cache specify the location of the respective programs. </p>
<p> The configuration item RootDir has a special meaning. If set, all paths in Dir:: will be relative to RootDir, <i>even paths that are specified absolutely</i>. So, for instance, if RootDir is set to /tmp/staging and Dir::State::status is set to /var/lib/dpkg/status, then the status file will be looked up in /tmp/staging/var/lib/dpkg/status. </p>
<p> The Ignore-Files-Silently list can be used to specify which files APT should silently ignore while parsing the files in the fragment directories. Per default a file which end with .disabled, ~, .bak or .dpkg-[a-z]+ is silently ignored. As seen in the last default value these patterns can use regular expression syntax.</p>
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
<p> <code>Pre-Invoke</code>, <code>Post-Invoke</code></p>
<dl>
<dd>This is a list of shell commands to run before/after invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). Like options this must be specified in list notation. The commands are invoked in order using /bin/sh; should any fail APT will abort.</dl>
<p> <code>Pre-Install-Pkgs</code></p>
<dl>
<dd>This is a list of shell commands to run before invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). Like options this must be specified in list notation. The commands are invoked in order using /bin/sh; should any fail APT will abort. APT will pass the filenames of all .deb files it is going to install to the commands, one per line on the requested file descriptor, defaulting to standard input. </p>
<p> Version 2 of this protocol dumps more information, including the protocol version, the APT configuration space and the packages, files and versions being changed. Version 3 adds the architecture and MultiArch flag to each version being dumped. </p>
<p> The version of the protocol to be used for the command <i>cmd</i> can be chosen by setting DPkg::Tools::options::<i>cmd</i>::Version accordingly, the default being version 1. If APT isn&#8217;t supporting the requested version it will send the information in the highest version it has support for instead. </p>
<p> The file descriptor to be used to send the information can be requested with DPkg::Tools::options::<i>cmd</i>::InfoFD which defaults to 0 for standard input and is available since version 0.9.11. Support for the option can be detected by looking for the environment variable <code>APT_HOOK_INFO_FD</code> which contains the number of the used file descriptor as a confirmation.</dl>
<p> <code>Run-Directory</code></p>
<dl>
<dd>APT chdirs to this directory before invoking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), the default is /.</dl>
<p> <code>Build-options</code></p>
<dl>
<dd>These options are passed to <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1) when compiling packages; the default is to disable signing and produce all binaries.</dl>
<h3>dpkg trigger usage (and related options)</h3>
<p>APT can call <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) in such a way as to let it make aggressive use of triggers over multiple calls of <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). Without further options <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) will use triggers once each time it runs. Activating these options can therefore decrease the time needed to perform the install or upgrade. Note that it is intended to activate these options per default in the future, but as it drastically changes the way APT calls <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) it needs a lot more testing. <i>These options are therefore currently experimental and should not be used in production environments.</i> It also breaks progress reporting such that all front-ends will currently stay around half (or more) of the time in the 100% state while it actually configures all packages. </p>
<p> Note that it is not guaranteed that APT will support these options or that these options will not cause (big) trouble in the future. If you have understand the current risks and problems with these options, but are brave enough to help testing them, create a new configuration file and test a combination of options. Please report any bugs, problems and improvements you encounter and make sure to note which options you have used in your reports. Asking <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) for help could also be useful for debugging proposes, see e.g. <code>dpkg &#8211;audit</code>. A defensive option combination would be </p>
<dl>
<dd>
<pre>DPkg::NoTriggers &quot;true&quot;;
PackageManager::Configure &quot;smart&quot;;
DPkg::ConfigurePending &quot;true&quot;;
DPkg::TriggersPending &quot;true&quot;;</pre>
</dl>
<p> <code>DPkg::NoTriggers</code></p>
<dl>
<dd>Add the no triggers flag to all <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) calls (except the ConfigurePending call). See <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) if you are interested in what this actually means. In short: <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) will not run the triggers when this flag is present unless it is explicitly called to do so in an extra call. Note that this option exists (undocumented) also in older APT versions with a slightly different meaning: Previously these option only append &#8211;no-triggers to the configure calls to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) &#8211; now APT will also add this flag to the unpack and remove calls.</dl>
<p> <code>PackageManager::Configure</code></p>
<dl>
<dd>Valid values are &quot;all&quot;, &quot;smart&quot; and &quot;no&quot;. The default value is &quot;all&quot;, which causes APT to configure all packages. The &quot;smart&quot; way is to configure only packages which need to be configured before another package can be unpacked (Pre-Depends), and let the rest be configured by <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) with a call generated by the ConfigurePending option (see below). On the other hand, &quot;no&quot; will not configure anything, and totally relies on <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) for configuration (which at the moment will fail if a Pre-Depends is encountered). Setting this option to any value other than all will implicitly also activate the next option by default, as otherwise the system could end in an unconfigured and potentially unbootable state.</dl>
<p> <code>DPkg::ConfigurePending</code></p>
<dl>
<dd>If this option is set APT will call <code>dpkg &#8211;configure &#8211;pending</code> to let <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) handle all required configurations and triggers. This option is activated automatically per default if the previous option is not set to all, but deactivating it could be useful if you want to run APT multiple times in a row &#8211; e.g. in an installer. In these sceneries you could deactivate this option in all but the last run.</dl>
<p> <code>DPkg::TriggersPending</code></p>
<dl>
<dd>Useful for the smart configuration as a package which has pending triggers is not considered as installed, and <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) treats them as unpacked currently which is a showstopper for Pre-Dependencies (see debbugs #526774). Note that this will process all triggers, not only the triggers needed to configure this package.</dl>
<p> <code>OrderList::Score::Immediate</code></p>
<dl>
<dd>Essential packages (and their dependencies) should be configured immediately after unpacking. It is a good idea to do this quite early in the upgrade process as these configure calls also currently require DPkg::TriggersPending which will run quite a few triggers (which may not be needed). Essentials get per default a high score but the immediate flag is relatively low (a package which has a Pre-Depends is rated higher). These option and the others in the same group can be used to change the scoring. The following example shows the settings with their default values. </p>
<dl>
<dd>
<pre>OrderList::Score {
 Delete 500;
 Essential 200;
 Immediate 10;
 PreDepends 50;
};</pre>
</dl>
</dl>
<h2>Periodic And Archives Options</h2>
<p>APT::Periodic and APT::Archives groups of options configure behavior of apt periodic updates, which is done by the /etc/cron.daily/apt script. See the top of this script for the brief documentation of these options.</p>
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
