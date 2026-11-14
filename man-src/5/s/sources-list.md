---
title: "sources-list(5)"
name: "sources-list"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sources-list/"
description: "sources.list – List of configured APT data sources"
---

<p>sources.list &#8211; List of configured APT data sources</p>
<h2>Description</h2>
<p>The source list /etc/apt/sources.list and the files contained in /etc/apt/sources.list.d/ are designed to support any number of active sources and a variety of source media. The files list one source per line (one-line style) or contain multiline stanzas defining one or more sources per stanza (deb822 style), with the most preferred source listed first (in case a single version is available from more than one source). The information available from the configured sources is acquired by <code>apt-get update</code> (or by an equivalent command from another APT front-end).</p>
<h2>Sources.List.D</h2>
<p>The /etc/apt/sources.list.d directory provides a way to add sources.list entries in separate files. Two different file formats are allowed as described in the next two sections. Filenames need to have either the extension .list or .sources depending on the contained format. The filenames may only contain letters (a-z and A-Z), digits (0-9), underscore (_), hyphen (-) and period (.) characters. Otherwise APT will print a notice that it has ignored a file, unless that file matches a pattern in the Dir::Ignore-Files-Silently configuration list &#8211; in which case it will be silently ignored.</p>
<h2>One-Line-Style Format</h2>
<p>Files in this format have the extension .list. Each line specifying a source starts with a type (e.g. deb-src) followed by options and arguments for this type. Individual entries cannot be continued onto a following line. Empty lines are ignored, and a # character anywhere on a line marks the remainder of that line as a comment. Consequently an entry can be disabled by commenting out the entire line. If options should be provided they are separated by spaces and all of them together are enclosed by square brackets ([]) included in the line after the type separated from it with a space. If an option allows multiple values these are separated from each other with a comma (,). An option name is separated from its value(s) by an equals sign (=). Multivalue options also have -= and += as separators, which instead of replacing the default with the given value(s) modify the default value(s) to remove or include the given values. </p>
<p> This is the traditional format and supported by all apt versions. Note that not all options as described below are supported by all apt versions. Note also that some older applications parsing this format on their own might not expect to encounter options as they were uncommon before the introduction of multi-architecture support.</p>
<h2>Deb822-Style Format</h2>
<p>Files in this format have the extension .sources. The format is similar in syntax to other files used by Debian and its derivatives, such as the metadata files that apt will download from the configured sources or the debian/control file in a Debian source package. Individual entries are separated by an empty line; additional empty lines are ignored, and a # character at the start of the line marks the entire line as a comment. An entry can hence be disabled by commenting out each line belonging to the stanza, but it is usually easier to add the field &quot;Enabled: no&quot; to the stanza to disable the entry. Removing the field or setting it to yes re-enables it. Options have the same syntax as every other field: A field name separated by a colon (:) and optionally spaces from its value(s). Note especially that multiple values are separated by whitespaces (like spaces, tabs and newlines), not by commas as in the one-line format. Multivalue fields like Architectures also have Architectures-Add and Architectures-Remove to modify the default value rather than replacing it. </p>
<p> This is a new format supported by apt itself since version 1.1. Previous versions ignore such files with a notice message as described earlier. It is intended to make this format gradually the default format, deprecating the previously described one-line-style format, as it is easier to create, extend and modify for humans and machines alike especially if a lot of sources and/or options are involved. Developers who are working with and/or parsing apt sources are highly encouraged to add support for this format and to contact the APT team to coordinate and share this work. Users can freely adopt this format already, but may encounter problems with software not supporting the format yet.</p>
<h2>The Deb And Deb-Src Types: General Format</h2>
<p>The deb type references a typical two-level Debian archive, distribution/component. The distribution is generally a suite name like stable or testing or a codename like bullseye or bookworm while component is one of main, contrib or non-free. The deb-src type references a Debian distribution&#8217;s source code in the same form as the deb type. A deb-src line is required to fetch source indexes. </p>
<p> The format for two one-line-style entries using the deb and deb-src types is: </p>
<dl>
<dd>
<pre>deb [ option1=value1 option2=value2 ] uri suite [component1] [component2] [...]
deb-src [ option1=value1 option2=value2 ] uri suite [component1] [component2] [...]</pre>
</dl>
<p> Alternatively the equivalent entry in deb822 style looks like this: </p>
<dl>
<dd>
<pre> Types: deb deb-src
 URIs: uri
 Suites: suite
 Components: [component1] [component2] [...]
 option1: value1
 option2: value2</pre>
</dl>
<p> The URI for the deb type must specify the base of the Debian distribution, from which APT will find the information it needs. suite can specify an exact path, in which case the components must be omitted and suite must end with a slash (/). This is useful for the case when only a particular sub-directory of the archive denoted by the URI is of interest. If suite does not specify an exact path, at least one component must be present. </p>
<p> suite may also contain a variable, $(ARCH) which expands to the Debian architecture (such as amd64 or armel) used on the system. This permits architecture-independent sources.list files to be used. In general this is only of interest when specifying an exact path; APT will automatically generate a URI with the current architecture otherwise. </p>
<p> Especially in the one-line-style format since only one distribution can be specified per line it may be necessary to have multiple lines for the same URI, if a subset of all available distributions or components at that location is desired. APT will sort the URI list after it has generated a complete set internally, and will collapse multiple references to the same Internet host, for instance, into a single connection, so that it does not inefficiently establish a connection, close it, do something else, and then re-establish a connection to that same host. APT also parallelizes connections to different hosts to more effectively deal with sites with low bandwidth. </p>
<p> It is important to list sources in order of preference, with the most preferred source listed first. Typically this will result in sorting by speed from fastest to slowest (CD-ROM followed by hosts on a local network, followed by distant Internet hosts, for example). </p>
<p> As an example, the sources for your distribution could look like this in one-line-style format: </p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://us.archive.ubuntu.com/ubuntu">http://us.archive.ubuntu.com/ubuntu</a> hirsute main restricted
deb <a rel="nofollow" href="http://security.ubuntu.com/ubuntu">http://security.ubuntu.com/ubuntu</a> hirsute-security main restricted
deb <a rel="nofollow" href="http://us.archive.ubuntu.com/ubuntu">http://us.archive.ubuntu.com/ubuntu</a> hirsute-updates main restricted</pre>
</dl>
<p> or like this in deb822 style format: </p>
<dl>
<dd>
<pre>Types: deb
URIs: <a rel="nofollow" href="http://us.archive.ubuntu.com/ubuntu">http://us.archive.ubuntu.com/ubuntu</a>
Suites: hirsute hirsute-updates
Components: main restricted
Types: deb
URIs: <a rel="nofollow" href="http://security.ubuntu.com/ubuntu">http://security.ubuntu.com/ubuntu</a>
Suites: hirsute-security
Components: main restricted</pre>
</dl>
<h2>The Deb And Deb-Src Types: Options</h2>
<p>Each source entry can have options specified to modify which source is accessed and how data is acquired from it. Format, syntax and names of the options vary between the one-line-style and deb822-style formats as described, but they both have the same options available. For simplicity we list the deb822 field name and provide the one-line name in brackets. Remember that besides setting multivalue options explicitly, there is also the option to modify them based on the default, but we aren&#8217;t listing those names explicitly here. Unsupported options are silently ignored by all APT versions. </p>
<dl>
<dd>&bull; <code>Architectures</code> (<code>arch</code>) is a multivalue option defining for which architectures information should be downloaded. If this option isn&#8217;t set the default is all architectures as defined by the <code>APT::Architectures</code> config option.</dl>
<dl>
<dd>&bull; <code>Languages</code> (<code>lang</code>) is a multivalue option defining for which languages information such as translated package descriptions should be downloaded. If this option isn&#8217;t set the default is all languages as defined by the <code>Acquire::Languages</code> config option.</dl>
<dl>
<dd>&bull; <code>Targets</code> (<code>target</code>) is a multivalue option defining which download targets apt will try to acquire from this source. If not specified, the default set is defined by the <code>Acquire::IndexTargets</code> configuration scope (targets are specified by their name in the Created-By field). Additionally, targets can be enabled or disabled by using the Identifier field as an option with a boolean value instead of using this multivalue option.</dl>
<dl>
<dd>&bull; <code>PDiffs</code> (<code>pdiffs</code>) is a yes/no value which controls if APT should try to use PDiffs to update old indexes instead of downloading the new indexes entirely. The value of this option is ignored if the repository doesn&#8217;t announce the availability of PDiffs. Defaults to the value of the option with the same name for a specific index file defined in the <code>Acquire::IndexTargets</code> scope, which itself defaults to the value of configuration option <code>Acquire::PDiffs</code> which defaults to yes.</dl>
<dl>
<dd>&bull; <code>By-Hash</code> (<code>by-hash</code>) can have the value yes, no or force and controls if APT should try to acquire indexes via a URI constructed from a hashsum of the expected file instead of using the well-known stable filename of the index. Using this can avoid hashsum mismatches, but requires a supporting mirror. A yes or no value activates/disables the use of this feature if this source indicates support for it, while force will enable the feature regardless of what the source indicates. Defaults to the value of the option of the same name for a specific index file defined in the <code>Acquire::IndexTargets</code> scope, which itself defaults to the value of configuration option <code>Acquire::By-Hash</code> which defaults to yes.</dl>
<p> Furthermore, there are options which if set affect <i>all</i> sources with the same URI and Suite, so they have to be set on all such entries and can not be varied between different components. APT will try to detect and error out on such anomalies. </p>
<dl>
<dd>&bull; <code>Allow-Insecure</code> (<code>allow-insecure</code>), <code>Allow-Weak</code> (<code>allow-weak</code>) and <code>Allow-Downgrade-To-Insecure</code> (<code>allow-downgrade-to-insecure</code>) are boolean values which all default to no. If set to yes they circumvent parts of <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) and should therefore not be used lightly!</dl>
<dl>
<dd>&bull; <code>Trusted</code> (<code>trusted</code>) is a tri-state value which defaults to APT deciding if a source is considered trusted or if warnings should be raised before e.g. packages are installed from this source. This option can be used to override that decision. The value yes tells APT always to consider this source as trusted, even if it doesn&#8217;t pass authentication checks. It disables parts of <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8), and should therefore only be used in a local and trusted context (if at all) as otherwise security is breached. The value no does the opposite, causing the source to be handled as untrusted even if the authentication checks passed successfully. The default value can&#8217;t be set explicitly.</dl>
<dl>
<dd>&bull; <code>Signed-By</code> (<code>signed-by</code>) is an option to require a repository to pass <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) verification with a certain set of keys rather than all trusted keys apt has configured. It is specified as a list of absolute paths to keyring files (have to be accessible and readable for the _apt system user, so ensure everyone has read-permissions on the file) and fingerprints of keys to select from these keyrings. The recommended locations for keyrings are /usr/share/keyrings for keyrings managed by packages, and /etc/apt/keyrings for keyrings managed by the system operator. If no keyring files are specified the default is the trusted.gpg keyring and all keyrings in the trusted.gpg.d/ directory (see <code>apt-key fingerprint</code>). If no fingerprint is specified all keys in the keyrings are selected. A fingerprint will accept also all signatures by a subkey of this key, if this isn&#8217;t desired an exclamation mark (!) can be appended to the fingerprint to disable this behaviour. The option defaults to the value of the option with the same name if set in the previously acquired Release file of this repository (only fingerprints can be specified there through). Otherwise all keys in the trusted keyrings are considered valid signers for this repository. The option may also be set directly to an embedded GPG public key block. Special care is needed to encode the empty line with leading spaces and &quot;.&quot;: </p>
<dl>
<dd>
<pre>Types: deb
URIs: <a rel="nofollow" href="https://deb.debian.org">https://deb.debian.org</a>
Suites: stable
Components: main contrib non-free
Signed-By:
 -----BEGIN PGP PUBLIC KEY BLOCK-----
 .
 mDMEYCQjIxYJKwYBBAHaRw8BAQdAD/P5Nvvnvk66SxBBHDbhRml9ORg1WV5CvzKY
 CuMfoIS0BmFiY2RlZoiQBBMWCgA4FiEErCIG1VhKWMWo2yfAREZd5NfO31cFAmAk
 IyMCGyMFCwkIBwMFFQoJCAsFFgIDAQACHgECF4AACgkQREZd5NfO31fbOwD6ArzS
 dM0Dkd5h2Ujy1b6KcAaVW9FOa5UNfJ9FFBtjLQEBAJ7UyWD3dZzhvlaAwunsk7DG
 3bHcln8DMpIJVXht78sL
 =IE0r
 -----END PGP PUBLIC KEY BLOCK-----</pre>
</dl>
</dl>
<dl>
<dd>&bull; <code>Check-Valid-Until</code> (<code>check-valid-until</code>) is a yes/no value which controls if APT should try to detect replay attacks. A repository creator can declare a time until which the data provided in the repository should be considered valid, and if this time is reached, but no new data is provided, the data is considered expired and an error is raised. Besides increasing security, as a malicious attacker can&#8217;t send old data forever to prevent a user from upgrading to a new version, this also helps users identify mirrors which are no longer updated. However, some repositories such as historic archives are not updated any more by design, so this check can be disabled by setting this option to no. Defaults to the value of configuration option <code>Acquire::Check-Valid-Until</code> which itself defaults to yes.</dl>
<dl>
<dd>&bull; <code>Valid-Until-Min</code> (<code>valid-until-min</code>) and <code>Valid-Until-Max</code> (<code>valid-until-max</code>) can be used to raise or lower the time period in seconds in which the data from this repository is considered valid. -Max can be especially useful if the repository provides no Valid-Until field on its Release file to set your own value, while -Min can be used to increase the valid time on seldom updated (local) mirrors of a more frequently updated but less accessible archive (which is in the sources.list as well) instead of disabling the check entirely. Default to the value of the configuration options <code>Acquire::Min-ValidTime</code> and <code>Acquire::Max-ValidTime</code> which are both unset by default.</dl>
<dl>
<dd>&bull; <code>Check-Date</code> (<code>check-date</code>) is a yes/no value which controls if APT should consider the machine&#8217;s time correct and hence perform time related checks, such as verifying that a Release file is not from the future. Disabling it also disables the <code>Check-Valid-Until</code> option mentioned above.</dl>
<dl>
<dd>&bull; <code>Date-Max-Future</code> (<code>date-max-future</code>) controls how far from the future a repository may be. Default to the value of the configuration option <code>Acquire::Max-FutureTime</code> which is 10 seconds by default.</dl>
<dl>
<dd>&bull; <code>InRelease-Path</code> (<code>inrelease-path</code>) determines the path to the InRelease file, relative to the normal position of an InRelease file. By default, this option is unset and APT will try to fetch an InRelease or, if that fails, a Release file and its associated Release.gpg file. By setting this option, the specified path will be tried instead of the InRelease file, and the fallback to Release files will be disabled.</dl>
<h2>Uri Specification</h2>
<p>The currently recognized URI types are: </p>
<p> <code>http</code> (<code><a href="/docs/linux/man/1-apt-transport-http/">apt-transport-http</a></code>(1))</p>
<dl>
<dd>The http scheme specifies an HTTP server for an archive and is the most commonly used method. The URI can directly include login information if the archive requires it, but the use of <code><a href="/docs/linux/man/5-apt_auth-conf/">apt_auth.conf</a></code>(5) should be preferred. The method also supports SOCKS5 and HTTP(S) proxies either configured via apt-specific configuration or specified by the environment variable <code>http_proxy</code> in the format (assuming an HTTP proxy requiring authentication) <i><a rel="nofollow" href="http://user:pass@server:port/">http://user:pass@server:port/</a></i>. The authentication details for proxies can also be supplied via <code><a href="/docs/linux/man/5-apt_auth-conf/">apt_auth.conf</a></code>(5). </p>
<p> Note that these forms of authentication are insecure as the whole communication with the remote server (or proxy) is not encrypted so a sufficiently capable attacker can observe and record login as well as all other interactions. The attacker can <i>not</i> modify the communication through as APT&#8217;s data security model is independent of the chosen transport method. See <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) for details.</dl>
<p> <code>https</code> (<code><a href="/docs/linux/man/1-apt-transport-https/">apt-transport-https</a></code>(1))</p>
<dl>
<dd>The https scheme specifies an HTTPS server for an archive and is very similar in use and available options to the http scheme. The main difference is that the communication between apt and server (or proxy) is encrypted. Note that the encryption does not prevent an attacker from knowing which server (or proxy) apt is communicating with and deeper analysis can potentially still reveal which data was downloaded. If this is a concern the Tor-based schemes mentioned further below might be a suitable alternative.</dl>
<p> <code>mirror</code>, <code>mirror+</code><i>scheme</i> (<code><a href="/docs/linux/man/1-apt-transport-mirror/">apt-transport-mirror</a></code>(1))</p>
<dl>
<dd>The mirror scheme specifies the location of a mirrorlist. By default the scheme used for the location is http, but any other scheme can be used via <code>mirror+</code><i>scheme</i>. The mirrorlist itself can contain many different URIs for mirrors the APT client can transparently pick, choose and fallback between intended to help both with distributing the load over the available mirrors and ensuring that clients can acquire data even if some configured mirrors are not available.</dl>
<p> <code>file</code></p>
<dl>
<dd>The file scheme allows an arbitrary directory in the file system to be considered an archive. This is useful for NFS mounts and local mirrors or archives.</dl>
<p> <code>cdrom</code></p>
<dl>
<dd>The cdrom scheme allows APT to use a local CD-ROM, DVD or USB drive with media swapping. Use the <code><a href="/docs/linux/man/8-apt-cdrom/">apt-cdrom</a></code>(8) program to create cdrom entries in the source list.</dl>
<p> <code>ftp</code></p>
<dl>
<dd>The ftp scheme specifies an FTP server for an archive. Use of FTP is on the decline in favour of http and https and many archives either never offered or are retiring FTP access. If you still need this method many configuration options for it are available in the Acquire::ftp scope and detailed in <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5). </p>
<p> Please note that an FTP proxy can be specified by using the <code>ftp_proxy</code> environment variable. It is possible to specify an HTTP proxy (HTTP proxy servers often understand FTP URLs) using this environment variable and <i>only</i> this environment variable. Proxies using HTTP specified in the configuration file will be ignored.</dl>
<p> <code>copy</code></p>
<dl>
<dd>The copy scheme is identical to the file scheme except that packages are copied into the cache directory instead of used directly at their location. This is useful for people using removable media to copy files around with APT.</dl>
<p> <code>rsh</code>, <code>ssh</code></p>
<dl>
<dd>The rsh/ssh method invokes RSH/SSH to connect to a remote host and access the files as a given user. Prior configuration of rhosts or RSA keys is recommended. The standard <code>find</code> and <code>dd</code> commands are used to perform the file transfers from the remote host.</dl>
<p> adding more recognizable URI types</p>
<dl>
<dd>APT can be extended with more methods shipped in other optional packages, which should follow the naming scheme apt-transport-<i>method</i>. For instance, the APT team also maintains the package apt-transport-tor, which provides access methods for HTTP and HTTPS URIs routed via the Tor network.</dl>
<h2>Examples</h2>
<p>Uses the archive stored locally (or NFS mounted) at /home/apt/debian for stable/main, stable/contrib, and stable/non-free. </p>
<dl>
<dd>
<pre>deb file:/home/apt/debian stable main contrib non-free</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: file:/home/apt/debian
Suites: stable
Components: main contrib non-free</pre>
</dl>
<p> As above, except this uses the unstable (development) distribution. </p>
<dl>
<dd>
<pre>deb file:/home/apt/debian unstable main contrib non-free</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: file:/home/apt/debian
Suites: unstable
Components: main contrib non-free</pre>
</dl>
<p> Sources specification for the above. </p>
<dl>
<dd>
<pre>deb-src file:/home/apt/debian unstable main contrib non-free</pre>
</dl>
<dl>
<dd>
<pre>Types: deb-src
URIs: file:/home/apt/debian
Suites: unstable
Components: main contrib non-free</pre>
</dl>
<p> The first line gets package information for the architectures in APT::Architectures while the second always retrieves amd64 and armel. </p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> bullseye main
deb [ arch=amd64,armel ] <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> bullseye main</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a>
Suites: bullseye
Components: main
Types: deb
URIs: <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a>
Suites: bullseye
Components: main
Architectures: amd64 armel</pre>
</dl>
<p> Uses HTTP to access the archive at archive.debian.org, and uses only the hamm/main area. </p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://archive.debian.org/debian-archive">http://archive.debian.org/debian-archive</a> hamm main</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: <a rel="nofollow" href="http://archive.debian.org/debian-archive">http://archive.debian.org/debian-archive</a>
Suites: hamm
Components: main</pre>
</dl>
<p> Uses FTP to access the archive at <a href="ftp://ftp.debian.org">ftp.debian.org</a>, under the debian directory, and uses only the bullseye/contrib area. </p>
<dl>
<dd>
<pre>deb <a href="ftp://ftp.debian.org/debian">ftp://ftp.debian.org/debian</a> bullseye contrib</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: <a href="ftp://ftp.debian.org/debian">ftp://ftp.debian.org/debian</a>
Suites: bullseye
Components: contrib</pre>
</dl>
<p> Uses FTP to access the archive at <a href="ftp://ftp.debian.org">ftp.debian.org</a>, under the debian directory, and uses only the unstable/contrib area. If this line appears as well as the one in the previous example in sources.list a single FTP session will be used for both resource lines. </p>
<dl>
<dd>
<pre>deb <a href="ftp://ftp.debian.org/debian">ftp://ftp.debian.org/debian</a> unstable contrib</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: <a href="ftp://ftp.debian.org/debian">ftp://ftp.debian.org/debian</a>
Suites: unstable
Components: contrib</pre>
</dl>
<p> Uses HTTP to access the archive at <a href="ftp://ftp.tlh.debian.org">ftp.tlh.debian.org</a>, under the universe directory, and uses only files found under unstable/binary-i386 on i386 machines, unstable/binary-amd64 on amd64, and so forth for other supported architectures. [Note this example only illustrates how to use the substitution variable; official debian archives are not structured like this] </p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://ftp.tlh.debian.org/universe">http://ftp.tlh.debian.org/universe</a> unstable/binary-$(ARCH)/</pre>
</dl>
<dl>
<dd>
<pre>Types: deb
URIs: <a rel="nofollow" href="http://ftp.tlh.debian.org/universe">http://ftp.tlh.debian.org/universe</a>
Suites: unstable/binary-$(ARCH)/</pre>
</dl>
<p> Uses HTTP to get binary packages as well as sources from the stable, testing and unstable suites and the components main and contrib. </p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> stable main contrib
deb-src <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> stable main contrib
deb <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> testing main contrib
deb-src <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> testing main contrib
deb <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> unstable main contrib
deb-src <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> unstable main contrib</pre>
</dl>
<dl>
<dd>
<pre>Types: deb deb-src
URIs: <a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a>
Suites: stable testing unstable
Components: main contrib</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5), /usr/share/doc/apt/acquire-additional-files.md.gz</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Authors</h2>
<p><code>Jason Gunthorpe</code></p>
<dl>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
