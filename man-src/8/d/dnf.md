---
title: "dnf(8)"
name: "dnf"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf/"
description: "dnf – DNF Command Reference"
---

<p>dnf &#8211; DNF Command Reference</p>
<h2>Synopsis</h2>
<p><code>dnf [options] &lt;command&gt; [&lt;args&gt;&#8230;]</code></p>
<h2>Description</h2>
<p><i>DNF</i> is the next upcoming major version of <i>Yum</i>, a package manager for RPM-based Linux distributions. It roughly maintains CLI compatibility with Yum and defines strict API for extensions and plugins. Plugins can modify or extend features of DNF or provide additional CLI commands on top of those mentioned below. </p>
<p> Available commands are:</p>
<dl>
<dt>&bull;</p>
<dd>autoremove</p>
<dt>&bull;</p>
<dd>check-update</p>
<dt>&bull;</p>
<dd>clean</p>
<dt>&bull;</p>
<dd>distro-sync</p>
<dt>&bull;</p>
<dd>downgrade</p>
<dt>&bull;</p>
<dd>group</p>
<dt>&bull;</p>
<dd>help</p>
<dt>&bull;</p>
<dd>history</p>
<dt>&bull;</p>
<dd>info</p>
<dt>&bull;</p>
<dd>install</p>
<dt>&bull;</p>
<dd>list</p>
<dt>&bull;</p>
<dd>makecache</p>
<dt>&bull;</p>
<dd>provides</p>
<dt>&bull;</p>
<dd>reinstall</p>
<dt>&bull;</p>
<dd>remove</p>
<dt>&bull;</p>
<dd>repolist</p>
<dt>&bull;</p>
<dd>repository-packages</p>
<dt>&bull;</p>
<dd>search</p>
<dt>&bull;</p>
<dd>updateinfo</p>
<dt>&bull;</p>
<dd>upgrade</p>
<dt>&bull;</p>
<dd>upgrade-to </p>
<p> See the reference for each command below.</dl>
<h2>Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>Resolve to IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd>Resolve to IPv6 addresses only.</p>
<dt><code>&#8211;allowerasing</code></p>
<dd>Allow erasing of installed packages to resolve dependencies. This option could be used as an alternative to <code>yum swap</code> command where packages to remove are not explicitly defined.</p>
<dt><code>&#8211;assumeno</code></p>
<dd>answer no for all questions</p>
<dt><code>&#8211;best</code></p>
<dd>Try the best available package versions in transactions. Specifically during <code>dnf upgrade</code>, which by default skips over updates that can not be installed for dependency reasons, the switch forces DNF to only consider the latest packages and possibly fail giving a reason why the latest version can not be installed.</p>
<dt><code>-C, &#8211;cacheonly</code></p>
<dd>Run entirely from system cache, don&#8217;t update the cache and use it even in case it is expired. </p>
<p> DNF uses a separate cache for each user under which it executes. The cache for the root user is called the system cache. This switch allows a regular user read-only access to the system cache which usually is more fresh then the user&#8217;s and thus he does not have to wait for metadata sync.</p>
<dt><code>-c &lt;config file&gt;, &#8211;config=&lt;config file&gt;</code></p>
<dd>config file location</p>
<dt><code>-d &lt;debug level&gt;, &#8211;debuglevel=&lt;debug level&gt;</code></p>
<dd>Debugging output level. This is an integer value between 0 (no additional information strings) and 10 (shows all debugging information, even that not understandable to the user), default is 2. Deprecated, use <code>-v</code> instead.</p>
<dt><code>&#8211;debugsolver</code></p>
<dd>Dump data aiding in dependency solver debugging into <code>./debugdata</code>. </p>
<p> <code>&#8211;disableexcludes=[all|main|&lt;repoid&gt;]</code> Disable the config file excludes. Takes one of three options:</p>
<dt>&bull;</p>
<dd><code>all</code>, disables all config file excludes</p>
<dt>&bull;</p>
<dd><code>main</code>, disables excludes defined in the <code>[main]</code> section</p>
<dt>&bull;</p>
<dd><code>repoid</code>, disables excludes defined for the given repo</p>
<dt><code>&#8211;disableplugin=&lt;plugin names&gt;</code></p>
<dd>Disable the listed plugins specified by names or globs.</p>
<dt><code>&#8211;disablerepo=&lt;repoid&gt;</code></p>
<dd>Disable specific repositories by an id or a glob.</p>
<dt><code>-e &lt;error level&gt;, &#8211;errorlevel=&lt;error level&gt;</code></p>
<dd>Error output level. This is an integer value between 0 (no error output) and 10 (shows all error messages), default is 2. Deprecated, use <code>-v</code> instead.</p>
<dt><code>&#8211;enablerepo=&lt;repoid&gt;</code></p>
<dd>Enable specific repositories by an id or a glob.</p>
<dt><code>-x &lt;package-spec&gt;, &#8211;exclude=&lt;package-spec&gt;</code></p>
<dd>Exclude packages specified by <code>&lt;package-spec&gt;</code> from the operation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show the help.</p>
<dt><code>&#8211;installroot=&lt;path&gt;</code></p>
<dd>set install root</p>
<dt><code>&#8211;refresh</code></p>
<dd>set metadata as expired before running the command</p>
<dt><code>&#8211;nogpgcheck</code></p>
<dd>skip checking GPG signatures on packages</p>
<dt><code>&#8211;noplugins</code></p>
<dd>Disable all plugins.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>quiet operation</p>
<dt><code>-R &lt;minutes&gt;, &#8211;randomwait=&lt;minutes&gt;</code></p>
<dd>maximum command wait time</p>
<dt><code>&#8211;releasever=&lt;release&gt;</code></p>
<dd>configure DNF as if the distribution release was <code>&lt;release&gt;</code>. This can affect cache paths, values in configuration files and mirrorlist URLs. Using &#8216;/&#8217; for this value makes DNF detect the release number from the running system.</p>
<dt><code>&#8211;rpmverbosity=&lt;debug level name&gt;</code></p>
<dd>debugging output level for rpm</p>
<dt><code>&#8211;setopt=&lt;option&gt;=&lt;value&gt;</code></p>
<dd>override a config option from the config file. To override config options from repo files, use <code>repoid.option</code> for the <code>&lt;option&gt;</code>.</p>
<dt><code>&#8211;showduplicates</code></p>
<dd>show duplicates, in repos, in list/search commands</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>verbose operation, show debug messages.</p>
<dt><code>&#8211;version</code></p>
<dd>show DNF version and exit</p>
<dt><code>-y, &#8211;assumeyes</code></p>
<dd>answer yes for all questions </p>
<p> List options are comma separated. Command-line options override respective settings from configuration files.</dl>
<h2>Commands</h2>
<p>For an explanation of <code>&lt;package-spec&gt;</code> and <code>&lt;package-name-spec&gt;</code> see <i>Specifying Packages</i>. </p>
<p> For an explanation of <code>&lt;package-nevr-spec&gt;</code> see <i>Specifying Exact Versions of Packages</i>. </p>
<p> For an explanation of <code>&lt;provide-spec&gt;</code> see <i>Specifying Provides</i>. </p>
<p> For an explanation of <code>&lt;group-spec&gt;</code> see <i>Specifying Groups</i>. </p>
<p> For an explanation of <code>&lt;transaction-spec&gt;</code> see <i>Specifying Transactions</i>.</p>
<h3>Auto Remove Command</h3>
<p><code>dnf [options] autoremove</code> Removes all &quot;leaf&quot; packages from the system that were originally installed as dependencies of user-installed packages but which are no longer required by any such package. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</p>
<h3>Check Update Command</h3>
<p><code>dnf [options] check-update [&lt;package-specs&gt;&#8230;]</code> Non-interactively checks if updates of the specified packages are available. If no <code>&lt;package-specs&gt;</code> are given checks whether any updates at all are available for your system. DNF exit code will be 100 when there are updates available and a list of the updates will be printed, 0 if not and 1 if an error occurs. </p>
<p> Please note that having a specific newer version available for an installed package (and reported by <code>check-update</code>) does not imply that subsequent <code>dnf upgrade</code> will install it. The difference is that <code>dnf upgrade</code> must also ensure the satisfiability of all dependencies and other restrictions.</p>
<h3>Clean Command</h3>
<p>Performs cleanup of temporary files for the currently enabled repositories.</p>
<dl>
<dt><code>dnf clean dbcache</code></p>
<dd>Removes cache files generated from the repository metadata. This forces DNF to regenerate the cache files the next time it is run.</p>
<dt><code>dnf clean expire-cache</code></p>
<dd>Removes local cookie files saying when the metadata and mirrorlists were downloaded for each repo. DNF will re-validate the cache for each repo the next time it is used.</p>
<dt><code>dnf clean metadata</code></p>
<dd>Removes repository metadata. Those are the files which DNF uses to determine the remote availability of packages. Using this option will make DNF download all the metadata the next time it is run.</p>
<dt><code>dnf clean packages</code></p>
<dd>Removes any cached packages from the system.</p>
<dt><code>dnf clean plugins</code></p>
<dd>Tells all enabled plugins to eliminate their cached data.</p>
<dt><code>dnf clean all</code></p>
<dd>Does all of the above.</dl>
<h3>Distro-sync command</h3>
<dl>
<dt><code>dnf distro-sync [&lt;package-spec&gt;&#8230;]</code></p>
<dd>As necessary upgrades, downgrades or keeps selected installed packages to match the latest version available from any enabled repository. If no package is given, all installed packages are considered.</dl>
<h3>Distribution-synchronization command</h3>
<dl>
<dt><code>dnf distribution-synchronization</code></p>
<dd>Deprecated alias for the <i>Distro-sync command</i>.</dl>
<h3>Downgrade Command</h3>
<dl>
<dt><code>dnf [options] downgrade &lt;package-specs&gt;&#8230;</code></p>
<dd>Downgrades the specified packages to the highest of all known lower versions.</dl>
<h3>Erase Command</h3>
<dl>
<dt><code>dnf [options] erase &lt;spec&gt;&#8230;</code></p>
<dd>Deprecated alias for the <i>Remove Command</i>.</dl>
<h3>Group Command</h3>
<p>Groups are virtual collections of packages. DNF keeps track of groups that the user selected (&quot;marked&quot;) installed and can manipulate the comprising packages with simple commands.</p>
<dl>
<dt><code>dnf [options] group [summary] &lt;group-spec&gt;</code></p>
<dd>Display overview of how many groups are installed and available. With a spec, limit the output to the matching groups. <code>summary</code> is the default groups subcommand.</p>
<dt><code>dnf [options] group info &lt;group-spec&gt;</code></p>
<dd>Display package lists of a group. Shows which packages are installed or available from a repo when <code>-v</code> is used.</p>
<dt><code>dnf [options] group install [with-optional] &lt;group-spec&gt;&#8230;</code></p>
<dd>Mark the specified group installed and install packages it contains. Also include optional packages of the group if <code>with-optional</code> is specified.</p>
<dt><code>dnf [options] group list &lt;group-spec&gt;&#8230;</code></p>
<dd>List all matching groups, either among installed or available groups. If nothing is specified list all known groups. Records are ordered by <i>display_order</i> tag defined in comps.xml file.</p>
<dt><code>dnf [options] group remove &lt;group-spec&gt;&#8230;</code></p>
<dd>Mark the group removed and remove those packages in the group from the system which are neither comprising another installed group and were not installed explicitly by the user.</p>
<dt><code>dnf [options] group upgrade &lt;group-spec&gt;&#8230;</code></p>
<dd>Upgrades the packages from the group and upgrades the group itself. The latter comprises of installing pacakges that were added to the group by the distribution and removing packages that got removed from the group as far as they were not installed explicitly by the user. </p>
<p> Groups can be also be marked installed or removed without physically manipualting any packages:</p>
<dt><code>dnf [options] group mark install &lt;group-spec&gt;&#8230;</code></p>
<dd>Mark the specified group installed. No packages will be installed by this command but the group is then considered installed.</p>
<dt><code>dnf [options] group mark remove &lt;group-spec&gt;&#8230;</code></p>
<dd>Mark the specified group removed. No packages will be removed by this command.</dl>
<h3>Help Command</h3>
<dl>
<dt><code>dnf help [&lt;command&gt;]</code></p>
<dd>Displays the help text for all commands. If given a command name then only displays the help for that particular command.</dl>
<h3>History Command</h3>
<p>The history command allows the user to view what has happened in past transactions and act according to this information (assuming the <code>history_record</code> configuration option is set).</p>
<dl>
<dt><code>dnf history [list]</code></p>
<dd>The default history action is listing all known transaction information in a table.</p>
<dt><code>dnf history info [&lt;spec&gt;&#8230;]</code></p>
<dd>Describe the given transactions. Each <code>&lt;spec&gt;</code> can be either a <code>&lt;transaction-spec&gt;</code>, which specifies a transaction directly, or a <code>&lt;package-name-spec&gt;</code>, which specifies a transaction by a package which it manipulated. When no transaction is specified describe what happened during the latest transaction.</p>
<dt><code>dnf history redo &lt;transaction-spec&gt;</code></p>
<dd>Repeat the specified transaction. If it is not possible to redo any operation due to the current state of RPMDB, do not redo any operation.</p>
<dt><code>dnf history rollback &lt;transaction-spec&gt;</code></p>
<dd>Undo all transactions performed after the specified transaction. If it is not possible to undo any transaction due to the current state of RPMDB, do not undo any transaction.</p>
<dt><code>dnf history undo &lt;transaction-spec&gt;</code></p>
<dd>Perform the opposite operation to all operations performed in the specified transaction. If it is not possible to undo any operation due to the current state of RPMDB, do not undo any operation.</p>
<dt><code>dnf history userinstalled</code></p>
<dd>List names of all packages installed by a user. The output can be used as the %packages section in a <i>kickstart</i> file. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</dl>
<h3>Info Command</h3>
<dl>
<dt><code>dnf [options] info [&lt;package-spec&gt;&#8230;]</code></p>
<dd>Is used to list description and summary information about available packages. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</dl>
<h3>Install Command</h3>
<dl>
<dt><code>dnf [options] install &lt;spec&gt;&#8230;</code></p>
<dd>Make sure that the given packages and their dependencies are installed on the system. Each <code>&lt;spec&gt;</code> can be either a <code>&lt;package-spec&gt;</code>, which specifies a package directly, or a path to the local rpm package, or an URL to a remote rpm package, or a <code>@&lt;group-spec&gt;</code>, which specifies an (environment) group which contains it. If a given package cannot be (and is not already) installed, the exit code will be non-zero. </p>
<p> Please make sure that you understand which package will be selected in case of multiple matches (see <i>Specifying Packages</i>).</dl>
<h3>List Command</h3>
<p>Dumps lists of packages depending on the packages&#8217; relation to the system. Generally packages are available (it is present in a repository we know about) or installed (present in the RPMDB). The list command can also limit the displayed packages according to other criteria, e.g. to only those that update an installed package. </p>
<p> All the forms take a <code>[&lt;package-specs&gt;&#8230;]</code> parameter to further limit the result to only those packages matching it.</p>
<dl>
<dt><code>dnf [options] list [all] [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>Lists all packages known to us, present in the RPMDB, in a repo or in both.</p>
<dt><code>dnf [options] list installed [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>Lists installed packages.</p>
<dt><code>dnf [options] list available [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>Lists available packages.</p>
<dt><code>dnf [options] list extras [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>Lists extras, that is packages installed on the system that are not available in any known repository.</p>
<dt><code>dnf [options] list obsoletes [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>List the packages installed on the system that are obsoleted by packages in any known repository.</p>
<dt><code>dnf [options] list recent [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>List packages recently added into the repositories.</p>
<dt><code>dnf [options] list upgrades [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>List upgrades available for the installed packages. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</dl>
<h3>Makecache Command</h3>
<dl>
<dt><code>dnf [options] makecache</code></p>
<dd>Downloads and caches in binary format metadata for all known repos. Tries to avoid downloading whenever possible (e.g. when the local metadata hasn&#8217;t expired yet or when the metadata timestamp hasn&#8217;t changed).</p>
<dt><code>dnf [options] makecache timer</code></p>
<dd>Like plain <code>makecache</code> but instructs DNF to be more resource-aware, meaning will not do anything if running on battery power and will terminate immediately if it&#8217;s too soon after the last successful <code>makecache</code> run (see <i><a href="/docs/linux/man/8-dnf-conf/">dnf.conf</a>(8)</i>, <i>metadata_timer_sync</i>).</dl>
<h3>Provides Command</h3>
<dl>
<dt><code>dnf [options] provides &lt;provide-spec&gt;</code></p>
<dd>Finds the packages providing the given <code>&lt;provide-spec&gt;</code>. This is useful when one knows a filename and wants to find what package (installed or not) provides this file. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</dl>
<h3>Reinstall Command</h3>
<dl>
<dt><code>dnf [options] reinstall &lt;package-specs&gt;&#8230;</code></p>
<dd>Installs the specified packages, fails if some of the packages are either not installed or not available (i.e. there is no repository where to download the same RPM).</dl>
<h3>Remove Command</h3>
<dl>
<dt><code>dnf [options] remove &lt;package-specs&gt;&#8230;</code></p>
<dd>Removes the specified packages from the system along with any packages depending on the packages being removed. Each <code>&lt;spec&gt;</code> can be either a <code>&lt;package-spec&gt;</code>, which specifies a package directly, or a <code>@&lt;group-spec&gt;</code>, which specifies an (environment) group which contains it. If <code>clean_requirements_on_remove</code> is enabled (the default) also removes any dependencies that are no longer needed.</dl>
<h3>Repolist Command</h3>
<dl>
<dt><code>dnf [options] repolist [enabled|disabled|all]</code></p>
<dd>Depending on the exact command, lists enabled, disabled or all known repositories. Lists all enabled repositories by default. Provides more detailed information when <code>-v</code> option is used. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</dl>
<h3>Repository-Packages Command</h3>
<p>The repository-packages command allows the user to run commands on top of all packages in the repository named <code>&lt;repoid&gt;</code>. However, any dependency resolution takes into account packages from all enabled repositories. Specifications <code>&lt;package-name-spec&gt;</code> and <code>&lt;package-spec&gt;</code> further limit the candidates to only those packages matching at least one of them. </p>
<p> <code>info</code> subcommand lists description and summary information about packages depending on the packages&#8217; relation to the repository. <code>list</code> subcommand just dumps lists of that packages.</p>
<dl>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; check-update [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Non-interactively checks if updates of the specified packages in the repository are available. DNF exit code will be 100 when there are updates available and a list of the updates will be printed.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info [all] [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List all related packages.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info installed [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages installed from the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info available [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages available in the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info extras [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>List packages installed from the repository that are not available in any repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info obsoletes [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages in the repository that obsolete packages installed on the system.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info recent [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages recently added into the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; info upgrades [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages in the repository that upgrade packages installed on the system.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; install [&lt;package-spec&gt;&#8230;]</code></p>
<dd>Install all packages in the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list [all] [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List all related packages.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list installed [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages installed from the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list available [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages available in the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list extras [&lt;package-name-specs&gt;&#8230;]</code></p>
<dd>List packages installed from the repository that are not available in any repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list obsoletes [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages in the repository that obsolete packages installed on the system.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list recent [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages recently added into the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; list upgrades [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>List packages in the repository that upgrade packages installed on the system.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; move-to [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Reinstall all those packages that are available in the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; reinstall [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Run <code>reinstall-old</code> subcommand. If it fails, run <code>move-to</code> subcommand.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; reinstall-old [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Reinstall all those packages that were installed from the repository and simultaneously are available in the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; remove [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Remove all packages installed from the repository along with any packages depending on the packages being removed. If <code>clean_requirements_on_remove</code> is enabled (the default) also removes any dependencies that are no longer needed.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; remove-or-distro-sync [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Select all packages installed from the repository. Upgrade, downgrade or keep those of them that are available in another repositories to match the latest version available there and remove the others along with any packages depending on the packages being removed. If <code>clean_requirements_on_remove</code> is enabled (the default) also removes any dependencies that are no longer needed.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; remove-or-reinstall [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Select all packages installed from the repository. Reinstall those of them that are available in another repositories and remove the others along with any packages depending on the packages being removed. If <code>clean_requirements_on_remove</code> is enabled (the default) also removes any dependencies that are no longer needed.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; upgrade [&lt;package-name-spec&gt;&#8230;]</code></p>
<dd>Update all packages to the highest resolvable version available in the repository.</p>
<dt><code>dnf [options] repository-packages &lt;repoid&gt; upgrade-to &lt;package-nevr-specs&gt;&#8230;</code></p>
<dd>Update packages to the specified versions that are available in the repository.</dl>
<h3>Search Command</h3>
<dl>
<dt><code>dnf [options] search [all] &lt;keywords&gt;&#8230;</code></p>
<dd>Search package metadata for the keywords. Keywords are matched as case-insensitive substrings, globbing is supported. By default the command will only look at package names and summaries, failing that (or whenever <code>all</code> was given as an argument) it will match against package descriptions and URLs. The result is sorted from the most relevant results to the least. </p>
<p> This command by default does not force a sync of expired metadata. See also <i>Metadata Synchronization</i>.</dl>
<h3>Update Command</h3>
<dl>
<dt><code>dnf [options] update</code></p>
<dd>Deprecated alias for the <i>Upgrade Command</i>.</dl>
<h3>Updateinfo Command</h3>
<dl>
<dt><code>dnf [options] updateinfo [&lt;output&gt;] [&lt;availability&gt;] [&lt;spec&gt;&#8230;]</code></p>
<dd>Display information about update advisories. </p>
<p> Depending on <code>&lt;output&gt;</code>, DNF displays just counts of advisory types (omitted or <code>summary</code>), list of advisories (<code>list</code>) or detailed information (<code>info</code>). When <code>info</code> with <code>-v</code> option is used, the information is even more detailed. </p>
<p> <code>&lt;availability&gt;</code> specifies whether advisories about newer versions of installed packages (omitted or <code>available</code>), advisories about equal and older versions of installed packages (<code>installed</code>), advisories about newer versions of those installed packages for which a newer version is available (<code>updates</code>) or advisories about any versions of installed packages (<code>all</code>) are taken into account. Most of the time, <code>available</code> and <code>updates</code> displays the same output. The outputs differ only in the cases when an advisory refers to a newer version but there is no enabled repository which contains any newer version. </p>
<p> If given and if neither ID, type (<code>bugfix</code>, <code>enhancement</code>, <code>security</code>/<code>sec</code>) nor a package name of an advisory does match <code>&lt;spec&gt;</code>, the advisory is not taken into account. The matching is case-sensitive and in the case of advisory IDs and package names, globbing is supported.</dl>
<h3>Upgrade Command</h3>
<dl>
<dt><code>dnf [options] upgrade</code></p>
<dd>Updates each package to a highest version that is both available and resolvable.</p>
<dt><code>dnf [options] upgrade &lt;package-specs&gt;&#8230;</code></p>
<dd>Updates each specified package to the latest available version. Updates dependencies as necessary.</dl>
<h3>Update-To Command</h3>
<dl>
<dt><code>dnf [options] update-to &lt;package-nevr-specs&gt;&#8230;</code></p>
<dd>Deprecated alias for the <i>Upgrade-To Command</i>.</dl>
<h3>Upgrade-To Command</h3>
<dl>
<dt><code>dnf [options] upgrade-to &lt;package-nevr-specs&gt;&#8230;</code></p>
<dd>Upgrades packages to the specified versions.</dl>
<h2>Specifying Packages</h2>
<p>Many commands take a <code>&lt;package-spec&gt;</code> parameter that selects a package for the operation. DNF looks for interpretations of the parameter from the most commonly used meanings to the least, that is it tries to see if the given spec fits one of the following patterns (in decreasing order of priority):</p>
<dl>
<dt>&bull;</p>
<dd><code>name.arch</code></p>
<dt>&bull;</p>
<dd><code>name</code></p>
<dt>&bull;</p>
<dd><code>name-[epoch:]version-release.arch</code></p>
<dt>&bull;</p>
<dd><code>name-[epoch:]version-release</code></p>
<dt>&bull;</p>
<dd><code>name-[epoch:]version</code> </p>
<p> Note that <code>name</code> can in general contain dashes (e.g. <code>package-subpackage</code>). </p>
<p> Failing to match the input argument to an existing package name based on the patterns above, DNF tries to see if the argument matches an existing provide. </p>
<p> By default, if multiple versions of the selected package exist in the repo, the most recent version suitable for the given operation is used. If the selected package exists for multiple architectures, the packages which best match the system&#8217;s architecture will be preferred. The name specification is case-sensitive, globbing characters &quot;<code>?</code>, <code>*</code> and <code>[</code> are allowed and trigger shell-like glob matching. If globbing character is present in <code>name</code>, DNF expands given <code>name</code> first and consequently selects all packages matching expanded <code>&lt;package-spec&gt;</code>. </p>
<p> <code>&lt;package-name-spec&gt;</code> is similar to <code>&lt;package-spec&gt;</code> except the provides matching is never attempted there.</dl>
<h2>Specifying Exact Versions Of Packages</h2>
<p>Commands accepting the <code>&lt;package-nevr-spec&gt;</code> parameter need not only the name of the package, but also its version, release and optionally the architecture. Further, the version part can be preceded by an epoch when it is relevant (i.e. the epoch is non-zero).</p>
<h2>Specifying Provides</h2>
<p><code>&lt;provide-spec&gt;</code> in command descriptions means the command operates on packages providing the given spec. This can either be an explicit provide, an implicit provide (i.e. name of the package) or a file provide. The selection is case-sensitive and globbing is supported.</p>
<h2>Specifying Groups</h2>
<p><code>&lt;group-spec&gt;</code> allows one to select (environment) groups a particular operation should work on. It is a case insensitive string (supporting globbing characters) that is matched against a group&#8217;s ID, canonical name and name translated into the current LC_MESSAGES locale (if possible).</p>
<h2>Specifying Transactions</h2>
<p><code>&lt;transaction-spec&gt;</code> can be in one of several forms. If it is an integer, it specifies a transaction ID. Specifying <code>last</code> is the same as specifying the ID of the most recent transaction. The last form is <code>last-&lt;offset&gt;</code>, where <code>&lt;offset&gt;</code> is a positive integer. It specifies offset-th transaction preceding the most recent transaction.</p>
<h2>Metadata Synchronization</h2>
<p>Correct operation of DNF depends on having access to up-to-date data from all enabled repositories but contacting remote mirrors on every operation considerably slows it down and costs bandwidth for both the client and the repository provider. The <i>metadata_expire</i> (see <i><a href="/docs/linux/man/8-dnf-conf/">dnf.conf</a>(8)</i>) repo config option is used by DNF to determine whether particular local copy of repository data is due to be re-synced. It is crucial that the repository providers set the option well, namely to a value where it is guaranteed that if particular metadata was available in time <code>T</code> on the server, then all packages it references will still be available for download from the server in time <code>T + metadata_expire</code>. </p>
<p> To further reduce the bandwidth load, some of the commands where having up-to-date metadata is not critical (e.g. the <code>list</code> command) do not look at whether a repository is expired and whenever any version of it is locally available, it will be used. Note that in all situations the user can force synchronization of all enabled repositories with the <code>&#8211;refresh</code> switch.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><i><a href="/docs/linux/man/8-dnf-conf/">dnf.conf</a>(8)</i>, <i>DNF Configuration Reference</i></p>
<dt>&bull;</p>
<dd><i>dnf.plugin.*(8)</i>, assorted DNF plugins that might be installed on the system.</p>
<dt>&bull;</p>
<dd><i>DNF</i> project homepage (<i><a rel="nofollow" href="https://github.com/rpm-software-management/dnf/">https://github.com/rpm-software-management/dnf/</a></i>)</p>
<dt>&bull;</p>
<dd><i>Yum</i> project homepage (<i><a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a></i>)</dl>
<h2>Author</h2>
<p>See AUTHORS in DNF source distribution.</p>
<h2>Copyright</h2>
<p>2012-2014, Red Hat, Licensed under GPLv2+</p>
