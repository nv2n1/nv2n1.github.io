---
title: "apt-get(8)"
name: "apt-get"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-get/"
description: "apt-get – APT package handling utility — command-line interface"
---

<p>apt-get &#8211; APT package handling utility &#8212; command-line interface</p>
<h2>Synopsis</h2>
<pre><code>apt-get [-asqdyfmubV] [-o=config_string] [-c=config_file] [-t=target_release] [-a=architecture] {update | upgrade | dselect-upgrade | dist-upgrade | install pkg [{=pkg_version_number | /target_release}]...  | remove pkg...  | purge pkg...  | source pkg [{=pkg_version_number | /target_release}]...  | build-dep pkg [{=pkg_version_number | /target_release}]...  | download pkg [{=pkg_version_number | /target_release}]...  | check | clean | autoclean | autoremove | {-v | --version} | {-h | --help}}</code></pre>
<h2>Description</h2>
<p><code>apt-get</code></p>
<dd>is the command-line tool for handling packages, and may be considered the user&#8217;s &quot;back-end&quot; to other tools using the APT library. Several &quot;front-end&quot; interfaces exist, such as <code><a href="/docs/linux/man/8-aptitude/">aptitude</a></code>(8), <code><a href="/docs/linux/man/8-synaptic/">synaptic</a></code>(8) and <code><a href="/docs/linux/man/1-wajig/">wajig</a></code>(1). Unless the <code>-h</code>, or <code>&#8211;help</code> option is given, one of the commands below must be present. <code>update</code></p>
<dl>
<dd>update is used to resynchronize the package index files from their sources. The indexes of available packages are fetched from the location(s) specified in /etc/apt/sources.list. For example, when using a Debian archive, this command retrieves and scans the Packages.gz files, so that information about new and updated packages is available. An update should always be performed before an upgrade or dist-upgrade. Please be aware that the overall progress meter will be incorrect as the size of the package files cannot be known in advance.</dl>
<p> <code>upgrade</code></p>
<dl>
<dd>upgrade is used to install the newest versions of all packages currently installed on the system from the sources enumerated in /etc/apt/sources.list. Packages currently installed with new versions available are retrieved and upgraded; under no circumstances are currently installed packages removed, or packages not already installed retrieved and installed. New versions of currently installed packages that cannot be upgraded without changing the install status of another package will be left at their current version. An update must be performed first so that <code>apt-get</code> knows that new versions of packages are available.</dl>
<p> <code>dist-upgrade</code></p>
<dl>
<dd>dist-upgrade in addition to performing the function of upgrade, also intelligently handles changing dependencies with new versions of packages; <code>apt-get</code> has a &quot;smart&quot; conflict resolution system, and it will attempt to upgrade the most important packages at the expense of less important ones if necessary. The dist-upgrade command may therefore remove some packages. The /etc/apt/sources.list file contains a list of locations from which to retrieve desired package files. See also <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5) for a mechanism for overriding the general settings for individual packages.</dl>
<p> <code>dselect-upgrade</code></p>
<dl>
<dd>dselect-upgrade is used in conjunction with the traditional Debian packaging front-end, <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1). dselect-upgrade follows the changes made by <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1) to the Status field of available packages, and performs the actions necessary to realize that state (for instance, the removal of old and the installation of new packages).</dl>
<p> <code>install</code></p>
<dl>
<dd>install is followed by one or more packages desired for installation or upgrading. Each package is a package name, not a fully qualified filename (for instance, in a Debian system, apt-utils would be the argument provided, not apt-utils_2.4.8_amd64.deb). All packages required by the package(s) specified for installation will also be retrieved and installed. The /etc/apt/sources.list file is used to locate the desired packages. If a hyphen is appended to the package name (with no intervening space), the identified package will be removed if it is installed. Similarly a plus sign can be used to designate a package to install. These latter features may be used to override decisions made by apt-get&#8217;s conflict resolution system. A specific version of a package can be selected for installation by following the package name with an equals and the version of the package to select. This will cause that version to be located and selected for install. Alternatively a specific distribution can be selected by following the package name with a slash and the version of the distribution or the Archive name (stable, testing, unstable). Both of the version selection mechanisms can downgrade packages and must be used with care. This is also the target to use if you want to upgrade one or more already-installed packages without upgrading every package you have on your system. Unlike the &quot;upgrade&quot; target, which installs the newest version of all currently installed packages, &quot;install&quot; will install the newest version of only the package(s) specified. Simply provide the name of the package(s) you wish to upgrade, and if a newer version is available, it (and its dependencies, as described above) will be downloaded and installed. Finally, the <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5) mechanism allows you to create an alternative installation policy for individual packages. If no package matches the given expression and the expression contains one of &#8216;.&#8217;, &#8216;?&#8217; or &#8216;*&#8217; then it is assumed to be a POSIX regular expression, and it is applied to all package names in the database. Any matches are then installed (or removed). Note that matching is done by substring so &#8216;lo.*&#8217; matches &#8216;how-lo&#8217; and &#8216;lowest&#8217;. If this is undesired, anchor the regular expression with a &#8216;^&#8217; or &#8216;$&#8217; character, or create a more specific regular expression. Fallback to regular expressions is deprecated in APT 2.0, has been removed in <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8), except for anchored expressions, and will be removed from <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) in a future version. Use <code><a href="/docs/linux/man/5-apt-patterns/">apt-patterns</a></code>(5) instead.</dl>
<p> <code>reinstall</code></p>
<dl>
<dd>reinstall is an alias for install &#8211;reinstall.</dl>
<p> <code>remove</code></p>
<dl>
<dd>remove is identical to install except that packages are removed instead of installed. Note that removing a package leaves its configuration files on the system. If a plus sign is appended to the package name (with no intervening space), the identified package will be installed instead of removed.</dl>
<p> <code>purge</code></p>
<dl>
<dd>purge is identical to remove except that packages are removed and purged (any configuration files are deleted too).</dl>
<p> <code>source</code></p>
<dl>
<dd>source causes <code>apt-get</code> to fetch source packages. APT will examine the available packages to decide which source package to fetch. It will then find and download into the current directory the newest available version of that source package while respecting the default release, set with the option APT::Default-Release, the <code>-t</code> option or per package with the pkg/release syntax, if possible. The arguments are interpreted as binary and source package names. See the <code>&#8211;only-source</code> option if you want to change that. Source packages are tracked separately from binary packages via deb-src lines in the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file. This means that you will need to add such a line for each repository you want to get sources from; otherwise you will probably get either the wrong (too old/too new) source versions or none at all. If the <code>&#8211;compile</code> option is specified then the package will be compiled to a binary .deb using <code>dpkg-buildpackage</code> for the architecture as defined by the <code>&#8211;host-architecture</code> option. If <code>&#8211;download-only</code> is specified then the source package will not be unpacked. A specific source version can be retrieved by postfixing the source name with an equals and then the version to fetch, similar to the mechanism used for the package files. This enables exact matching of the source package name and version, implicitly enabling the APT::Get::Only-Source option. Note that source packages are not installed and tracked in the <code>dpkg</code> database like binary packages; they are simply downloaded to the current directory, like source tarballs.</dl>
<p> <code>build-dep</code></p>
<dl>
<dd>build-dep causes apt-get to install/remove packages in an attempt to satisfy the build dependencies for a source package. By default the dependencies are satisfied to build the package natively. If desired a host-architecture can be specified with the <code>&#8211;host-architecture</code> option instead. The arguments are interpreted as binary or source package names. See the <code>&#8211;only-source</code> option if you want to change that.</dl>
<p> <code>satisfy</code></p>
<dl>
<dd>satisfy causes apt-get to satisfy the given dependency strings. The dependency strings may have build profiles and architecture restriction list as in build dependencies. They may optionally be prefixed with &quot;Conflicts: &quot; to unsatisfy the dependency string. Multiple strings of the same type can be specified. </p>
<pre><code>Example:
apt-get satisfy &quot;foo&quot; &quot;Conflicts: bar&quot; &quot;baz (&gt;&gt; 1.0) | bar (= 2.0), moo&quot;</code></pre>
<p> The legacy operator &#8216;&lt;/&gt;&#8217; is not supported, use &#8216;&lt;=/&gt;=&#8217; instead.</dl>
<p> <code>check</code></p>
<dl>
<dd>check is a diagnostic tool; it updates the package cache and checks for broken dependencies.</dl>
<p> <code>download</code></p>
<dl>
<dd>download will download the given binary package into the current directory.</dl>
<p> <code>clean</code></p>
<dl>
<dd>clean clears out the local repository of retrieved package files. It removes everything but the lock file from /var/cache/apt/archives/ and /var/cache/apt/archives/partial/.</dl>
<p> <code>autoclean</code> (and the <code>auto-clean</code> alias since 1.1)</p>
<dl>
<dd>Like clean, autoclean clears out the local repository of retrieved package files. The difference is that it only removes package files that can no longer be downloaded, and are largely useless. This allows a cache to be maintained over a long period without it growing out of control. The configuration option APT::Clean-Installed will prevent installed packages from being erased if it is set to off.</dl>
<p> <code>autoremove</code> (and the <code>auto-remove</code> alias since 1.1)</p>
<dl>
<dd>autoremove is used to remove packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed.</dl>
<p> <code>changelog</code></p>
<dl>
<dd>changelog tries to download the changelog of a package and displays it through <code>sensible-pager</code>. By default it displays the changelog for the version that is installed. However, you can specify the same options as for the <code>install</code> command.</dl>
<p> <code>indextargets</code></p>
<dl>
<dd>Displays by default a deb822 formatted listing of information about all data files (aka index targets) <code>apt-get update</code> would download. Supports a <code>&#8211;format</code> option to modify the output format as well as accepts lines of the default output to filter the records by. The command is mainly used as an interface for external tools working with APT to get information as well as filenames for downloaded files so they can use them as well instead of downloading them again on their own. Detailed documentation is omitted here and can instead be found in the file /usr/share/doc/apt/acquire-additional-files.md.gz shipped by the apt-doc package.</dl>
<h2>Options</h2>
<p>All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>&#8211;no-install-recommends</code></p>
<dl>
<dd>Do not consider recommended packages as a dependency for installing. Configuration Item: APT::Install-Recommends.</dl>
<p> <code>&#8211;install-suggests</code></p>
<dl>
<dd>Consider suggested packages as a dependency for installing. Configuration Item: APT::Install-Suggests.</dl>
<p> <code>-d</code>, <code>&#8211;download-only</code></p>
<dl>
<dd>Download only; package files are only retrieved, not unpacked or installed. Configuration Item: APT::Get::Download-Only.</dl>
<p> <code>-f</code>, <code>&#8211;fix-broken</code></p>
<dl>
<dd>Fix; attempt to correct a system with broken dependencies in place. This option, when used with install/remove, can omit any packages to permit APT to deduce a likely solution. If packages are specified, these have to completely correct the problem. The option is sometimes necessary when running APT for the first time; APT itself does not allow broken package dependencies to exist on a system. It is possible that a system&#8217;s dependency structure can be so corrupt as to require manual intervention (which usually means using <code>dpkg &#8211;remove</code> to eliminate some of the offending packages). Use of this option together with <code>-m</code> may produce an error in some situations. Configuration Item: APT::Get::Fix-Broken.</dl>
<p> <code>-m</code>, <code>&#8211;ignore-missing</code>, <code>&#8211;fix-missing</code></p>
<dl>
<dd>Ignore missing packages; if packages cannot be retrieved or fail the integrity check after retrieval (corrupted package files), hold back those packages and handle the result. Use of this option together with <code>-f</code> may produce an error in some situations. If a package is selected for installation (particularly if it is mentioned on the command line) and it could not be downloaded then it will be silently held back. Configuration Item: APT::Get::Fix-Missing.</dl>
<p> <code>&#8211;no-download</code></p>
<dl>
<dd>Disables downloading of packages. This is best used with <code>&#8211;ignore-missing</code> to force APT to use only the .debs it has already downloaded. Configuration Item: APT::Get::Download.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Quiet; produces output suitable for logging, omitting progress indicators. More q&#8217;s will produce more quiet up to a maximum of 2. You can also use <code>-q=#</code> to set the quiet level, overriding the configuration file. Note that quiet level 2 implies <code>-y</code>; you should never use -qq without a no-action modifier such as -d, &#8211;print-uris or -s as APT may decide to do something you did not expect. Configuration Item: quiet.</dl>
<p> <code>-s</code>, <code>&#8211;simulate</code>, <code>&#8211;just-print</code>, <code>&#8211;dry-run</code>, <code>&#8211;recon</code>, <code>&#8211;no-act</code></p>
<dl>
<dd>No action; perform a simulation of events that would occur based on the current system state but do not actually change the system. Locking will be disabled (<code>Debug::NoLocking</code>) so the system state could change while <code>apt-get</code> is running. Simulations can also be executed by non-root users which might not have read access to all apt configuration distorting the simulation. A notice expressing this warning is also shown by default for non-root users (<code>APT::Get::Show-User-Simulation-Note</code>). Configuration Item: APT::Get::Simulate. </p>
<p> Simulated runs print out a series of lines, each representing a <code>dpkg</code> operation: configure (Conf), remove (Remv) or unpack (Inst). Square brackets indicate broken packages, and empty square brackets indicate breaks that are of no consequence (rare).</dl>
<p> <code>-y</code>, <code>&#8211;yes</code>, <code>&#8211;assume-yes</code></p>
<dl>
<dd>Automatic yes to prompts; assume &quot;yes&quot; as answer to all prompts and run non-interactively. If an undesirable situation, such as changing a held package, trying to install an unauthenticated package or removing an essential package occurs then apt-get will abort. Configuration Item: APT::Get::Assume-Yes.</dl>
<p> <code>&#8211;assume-no</code></p>
<dl>
<dd>Automatic &quot;no&quot; to all prompts. Configuration Item: APT::Get::Assume-No.</dl>
<p> <code>&#8211;no-show-upgraded</code></p>
<dl>
<dd>Do not show a list of all packages that are to be upgraded. Configuration Item: APT::Get::Show-Upgraded.</dl>
<p> <code>-V</code>, <code>&#8211;verbose-versions</code></p>
<dl>
<dd>Show full versions for upgraded and installed packages. Configuration Item: APT::Get::Show-Versions.</dl>
<p> <code>-a</code>, <code>&#8211;host-architecture</code></p>
<dl>
<dd>This option controls the architecture packages are built for by <code>apt-get source &#8211;compile</code> and how cross-builddependencies are satisfied. By default is it not set which means that the host architecture is the same as the build architecture (which is defined by APT::Architecture). Configuration Item: APT::Get::Host-Architecture.</dl>
<p> <code>-P</code>, <code>&#8211;build-profiles</code></p>
<dl>
<dd>This option controls the activated build profiles for which a source package is built by <code>apt-get source &#8211;compile</code> and how build dependencies are satisfied. By default no build profile is active. More than one build profile can be activated at a time by concatenating them with a comma. Configuration Item: APT::Build-Profiles.</dl>
<p> <code>-b</code>, <code>&#8211;compile</code>, <code>&#8211;build</code></p>
<dl>
<dd>Compile source packages after downloading them. Configuration Item: APT::Get::Compile.</dl>
<p> <code>&#8211;ignore-hold</code></p>
<dl>
<dd>Ignore package holds; this causes <code>apt-get</code> to ignore a hold placed on a package. This may be useful in conjunction with dist-upgrade to override a large number of undesired holds. Configuration Item: APT::Ignore-Hold.</dl>
<p> <code>&#8211;with-new-pkgs</code></p>
<dl>
<dd>Allow installing new packages when used in conjunction with upgrade. This is useful if the update of an installed package requires new dependencies to be installed. Instead of holding the package back upgrade will upgrade the package and install the new dependencies. Note that upgrade with this option will never remove packages, only allow adding new ones. Configuration Item: APT::Get::Upgrade-Allow-New.</dl>
<p> <code>&#8211;no-upgrade</code></p>
<dl>
<dd>Do not upgrade packages; when used in conjunction with install, no-upgrade will prevent packages on the command line from being upgraded if they are already installed. Configuration Item: APT::Get::Upgrade.</dl>
<p> <code>&#8211;only-upgrade</code></p>
<dl>
<dd>Do not install new packages; when used in conjunction with install, only-upgrade will install upgrades for already installed packages only and ignore requests to install new packages. Configuration Item: APT::Get::Only-Upgrade.</dl>
<p> <code>&#8211;allow-downgrades</code></p>
<dl>
<dd>This is a dangerous option that will cause apt to continue without prompting if it is doing downgrades. It should not be used except in very special situations. Using it can potentially destroy your system! Configuration Item: APT::Get::allow-downgrades. Introduced in APT 1.1.</dl>
<p> <code>&#8211;allow-remove-essential</code></p>
<dl>
<dd>Force yes; this is a dangerous option that will cause apt to continue without prompting if it is removing essentials. It should not be used except in very special situations. Using it can potentially destroy your system! Configuration Item: APT::Get::allow-remove-essential. Introduced in APT 1.1.</dl>
<p> <code>&#8211;allow-change-held-packages</code></p>
<dl>
<dd>Force yes; this is a dangerous option that will cause apt to continue without prompting if it is changing held packages. It should not be used except in very special situations. Using it can potentially destroy your system! Configuration Item: APT::Get::allow-change-held-packages. Introduced in APT 1.1.</dl>
<p> <code>&#8211;force-yes</code></p>
<dl>
<dd>Force yes; this is a dangerous option that will cause apt to continue without prompting if it is doing something potentially harmful. It should not be used except in very special situations. Using force-yes can potentially destroy your system! Configuration Item: APT::Get::force-yes. This is deprecated and replaced by <code>&#8211;allow-unauthenticated</code> , <code>&#8211;allow-downgrades</code> , <code>&#8211;allow-remove-essential</code> , <code>&#8211;allow-change-held-packages</code> in 1.1.</dl>
<p> <code>&#8211;print-uris</code></p>
<dl>
<dd>Instead of fetching the files to install their URIs are printed. Each URI will have the path, the destination file name, the size and the expected MD5 hash. Note that the file name to write to will not always match the file name on the remote site! This also works with the source and update commands. When used with the update command the MD5 and size are not included, and it is up to the user to decompress any compressed files. Configuration Item: APT::Get::Print-URIs.</dl>
<p> <code>&#8211;purge</code></p>
<dl>
<dd>Use purge instead of remove for anything that would be removed. An asterisk (&quot;*&quot;) will be displayed next to packages which are scheduled to be purged. <code>remove &#8211;purge</code> is equivalent to the <code>purge</code> command. Configuration Item: APT::Get::Purge.</dl>
<p> <code>&#8211;reinstall</code></p>
<dl>
<dd>Re-install packages that are already installed and at the newest version. Configuration Item: APT::Get::ReInstall.</dl>
<p> <code>&#8211;list-cleanup</code></p>
<dl>
<dd>This option is on by default; use &#8211;no-list-cleanup to turn it off. When it is on, <code>apt-get</code> will automatically manage the contents of /var/lib/apt/lists to ensure that obsolete files are erased. The only reason to turn it off is if you frequently change your sources list. Configuration Item: APT::Get::List-Cleanup.</dl>
<p> <code>-t</code>, <code>&#8211;target-release</code>, <code>&#8211;default-release</code></p>
<dl>
<dd>This option controls the default input to the policy engine; it creates a default pin at priority 990 using the specified release string. This overrides the general settings in /etc/apt/preferences. Specifically pinned packages are not affected by the value of this option. In short, this option lets you have simple control over which distribution packages will be retrieved from. Some common examples might be <code>-t &#8216;2.1*&#8217;</code>, <code>-t unstable</code> or <code>-t sid</code>. Configuration Item: APT::Default-Release; see also the <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5) manual page.</dl>
<p> <code>&#8211;trivial-only</code></p>
<dl>
<dd>Only perform operations that are &#8216;trivial&#8217;. Logically this can be considered related to <code>&#8211;assume-yes</code>; where <code>&#8211;assume-yes</code> will answer yes to any prompt, <code>&#8211;trivial-only</code> will answer no. Configuration Item: APT::Get::Trivial-Only.</dl>
<p> <code>&#8211;mark-auto</code></p>
<dl>
<dd>After successful installation, mark all freshly installed packages as automatically installed, which will cause each of the packages to be removed when no more manually installed packages depend on this package. This is equally to running <code>apt-mark auto</code> for all installed packages. Configuration Item: APT::Get::Mark-Auto.</dl>
<p> <code>&#8211;no-remove</code></p>
<dl>
<dd>If any packages are to be removed apt-get immediately aborts without prompting. Configuration Item: APT::Get::Remove.</dl>
<p> <code>&#8211;auto-remove</code>, <code>&#8211;autoremove</code></p>
<dl>
<dd>If the command is either install or remove, then this option acts like running the autoremove command, removing unused dependency packages. Configuration Item: APT::Get::AutomaticRemove.</dl>
<p> <code>&#8211;only-source</code></p>
<dl>
<dd>Only has meaning for the source and build-dep commands. Indicates that the given source names are not to be mapped through the binary table. This means that if this option is specified, these commands will only accept source package names as arguments, rather than accepting binary package names and looking up the corresponding source package. Configuration Item: APT::Get::Only-Source.</dl>
<p> <code>&#8211;diff-only</code>, <code>&#8211;dsc-only</code>, <code>&#8211;tar-only</code></p>
<dl>
<dd>Download only the diff, dsc, or tar file of a source archive. Configuration Item: APT::Get::Diff-Only, APT::Get::Dsc-Only, and APT::Get::Tar-Only.</dl>
<p> <code>&#8211;arch-only</code></p>
<dl>
<dd>Only process architecture-dependent build-dependencies. Configuration Item: APT::Get::Arch-Only.</dl>
<p> <code>&#8211;indep-only</code></p>
<dl>
<dd>Only process architecture-independent build-dependencies. Configuration Item: APT::Get::Indep-Only.</dl>
<p> <code>&#8211;allow-unauthenticated</code></p>
<dl>
<dd>Ignore if packages can&#8217;t be authenticated and don&#8217;t prompt about it. This can be useful while working with local repositories, but is a huge security risk if data authenticity isn&#8217;t ensured in another way by the user itself. The usage of the <code>Trusted</code> option for <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entries should usually be preferred over this global override. Configuration Item: APT::Get::AllowUnauthenticated.</dl>
<p> <code>&#8211;no-allow-insecure-repositories</code></p>
<dl>
<dd>Forbid the update command to acquire unverifiable data from configured sources. APT will fail at the update command for repositories without valid cryptographically signatures. See also <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) for details on the concept and the implications. Configuration Item: Acquire::AllowInsecureRepositories.</dl>
<p> <code>&#8211;allow-releaseinfo-change</code></p>
<dl>
<dd>Allow the update command to continue downloading data from a repository which changed its information of the release contained in the repository indicating e.g a new major release. APT will fail at the update command for such repositories until the change is confirmed to ensure the user is prepared for the change. See also <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) for details on the concept and configuration. </p>
<p> Specialist options (&#8211;allow-releaseinfo-change-<i>field</i>) exist to allow changes only for certain fields like origin, label, codename, suite, version and defaultpin. See also <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5). Configuration Item: Acquire::AllowReleaseInfoChange.</dl>
<p> <code>&#8211;show-progress</code></p>
<dl>
<dd>Show user friendly progress information in the terminal window when packages are installed, upgraded or removed. For a machine parsable version of this data see README.progress-reporting in the apt doc directory. Configuration Items: Dpkg::Progress and Dpkg::Progress-Fancy.</dl>
<p> <code>&#8211;with-source</code> <i>filename</i></p>
<dl>
<dd>Adds the given file as a source for metadata. Can be repeated to add multiple files. See <code>&#8211;with-source</code> description in <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8) for further details.</dl>
<p> <code>-e</code><i>any</i>, <code>&#8211;error-on=</code><i>any</i></p>
<dl>
<dd>Fail the update command if any error occured, even a transient one.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Show a short usage summary.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Show the program version.</dl>
<p> <code>-c</code>, <code>&#8211;config-file</code></p>
<dl>
<dd>Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file. If configuration settings need to be set before the default configuration files are parsed specify a file with the <code>APT_CONFIG</code> environment variable. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for syntax information.</dl>
<p> <code>-o</code>, <code>&#8211;option</code></p>
<dl>
<dd>Set a Configuration Option; This will set an arbitrary configuration option. The syntax is <code>-o Foo::Bar=bar</code>. <code>-o</code> and <code>&#8211;option</code> can be used multiple times to set different options.</dl>
<h2>Files</h2>
<p>/etc/apt/sources.list</p>
<dl>
<dd>Locations to fetch packages from. Configuration Item: Dir::Etc::SourceList.</dl>
<p> /etc/apt/sources.list.d/</p>
<dl>
<dd>File fragments for locations to fetch packages from. Configuration Item: Dir::Etc::SourceParts.</dl>
<p> /etc/apt/apt.conf</p>
<dl>
<dd>APT configuration file. Configuration Item: Dir::Etc::Main.</dl>
<p> /etc/apt/apt.conf.d/</p>
<dl>
<dd>APT configuration file fragments. Configuration Item: Dir::Etc::Parts.</dl>
<p> /etc/apt/preferences</p>
<dl>
<dd>Version preferences file. This is where you would specify &quot;pinning&quot;, i.e. a preference to get certain packages from a separate source or from a different version of a distribution. Configuration Item: Dir::Etc::Preferences.</dl>
<p> /etc/apt/preferences.d/</p>
<dl>
<dd>File fragments for the version preferences. Configuration Item: Dir::Etc::PreferencesParts.</dl>
<p> /var/cache/apt/archives/</p>
<dl>
<dd>Storage area for retrieved package files. Configuration Item: Dir::Cache::Archives.</dl>
<p> /var/cache/apt/archives/partial/</p>
<dl>
<dd>Storage area for package files in transit. Configuration Item: Dir::Cache::Archives (partial will be implicitly appended)</dl>
<p> /var/lib/apt/lists/</p>
<dl>
<dd>Storage area for state information for each package resource specified in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) Configuration Item: Dir::State::Lists.</dl>
<p> /var/lib/apt/lists/partial/</p>
<dl>
<dd>Storage area for state information in transit. Configuration Item: Dir::State::Lists (partial will be implicitly appended)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8), <code><a href="/docs/linux/man/8-apt-cdrom/">apt-cdrom</a></code>(8), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5), <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5), <code><a href="/docs/linux/man/8-apt-config/">apt-config</a></code>(8), <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8), The APT User&#8217;s guide in /usr/share/doc/apt-doc/, <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5), the APT Howto.</p>
<h2>Diagnostics</h2>
<p><code>apt-get</code> returns zero on normal operation, decimal 100 on error.</p>
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
