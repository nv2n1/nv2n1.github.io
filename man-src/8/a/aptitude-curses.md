---
title: "aptitude-curses(8)"
name: "aptitude-curses"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aptitude-curses/"
description: "aptitude – high-level interface to the package manager"
---

<p>aptitude &#8211; high-level interface to the package manager</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>aptitude</code> [&lt;<i>options</i>&gt;&#8230;] {autoclean | clean | forget-new | keep-all | update}</p>
<dt> <code>aptitude</code> [&lt;<i>options</i>&gt;&#8230;] {full-upgrade | safe-upgrade} [&lt;<i>packages</i>&gt;&#8230;]</p>
<dt> <code>aptitude</code> [&lt;<i>options</i>&gt;&#8230;] {build-dep | build-depends | changelog | download | forbid-version | hold | install | markauto | purge | reinstall | remove | show | unhold | unmarkauto | versions} &lt;<i>packages</i>&gt;&#8230;</p>
<dt> <code>aptitude</code> extract-cache-subset &lt;<i>output-directory</i>&gt; &lt;<i>packages</i>&gt;&#8230;</p>
<dt> <code>aptitude</code> [&lt;<i>options</i>&gt;&#8230;] search &lt;<i>patterns</i>&gt;&#8230;</p>
<dt> <code>aptitude</code> [&lt;<i>options</i>&gt;&#8230;] {add-user-tag | remove-user-tag} &lt;<i>tag</i>&gt; &lt;<i>packages</i>&gt;&#8230;</p>
<dt> <code>aptitude</code> [&lt;<i>options</i>&gt;&#8230;] {why | why-not} [&lt;<i>patterns</i>&gt;&#8230;] &lt;<i>package</i>&gt;</p>
<dt> <code>aptitude</code> [-S&nbsp;<wbr>&lt;<i>fname</i>&gt;] [&#8211;autoclean-on-startup | &#8211;clean-on-startup | -i | -u]</p>
<dt> <code>aptitude</code> help</dl>
<h2>Description</h2>
<p><code>aptitude</code></p>
<dd>is a text-based interface to the Debian GNU/Linux package system. </p>
<p> It allows the user to view the list of packages and to perform package management tasks such as installing, upgrading, and removing packages. Actions may be performed from a visual interface or from the command-line.</p>
<h2>Command-Line Actions</h2>
<p>The first argument which does not begin with a hyphen (&#8220;<code>&#8211;</code>&#8220;) is considered to be an action that the program should perform. If an action is not specified on the command-line, <code>aptitude</code> will start up in visual mode. </p>
<p> The following actions are available: </p>
<p> <code>install</code></p>
<dl>
<dd>Install one or more packages. The packages should be listed after the &#8220;install&#8221; command; if a package name contains a tilde character (&#8220;<code>~</code>&#8220;) or a question mark (&#8220;<code>?</code>&#8220;), it will be treated as a search pattern and every package matching the pattern will be installed (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). </p>
<p> To select a particular version of the package, append &#8220;<code>=</code><code>&lt;</code><i>version</i>&gt;&#8221; to the package name: for instance, &#8220;<code>aptitude install apt=0.3.1</code>&#8220;. Similarly, to select a package from a particular archive, append &#8220;<code>/</code><code>&lt;</code><i>archive</i>&gt;&#8221; to the package name: for instance, &#8220;<code>aptitude install apt/experimental</code>&#8220;. You cannot specify both an archive and a version for a package. </p>
<p> Not every package listed on the command line has to be installed; you can tell <code>aptitude</code> to do something different with a package by appending an &#8220;override specifier&#8221; to the name of the package. For example, <code>aptitude remove wesnoth+</code> will install <code>wesnoth</code>, not remove it. The following override specifiers are available: </p>
<p> &lt;<i>package</i>&gt;<code>+</code></p>
<dl>
<dd>Install &lt;<i>package</i>&gt;.</dl>
<p> &lt;<i>package</i>&gt;<code>+M</code></p>
<dl>
<dd>Install &lt;<i>package</i>&gt; and immediately mark it as automatically installed (note that if nothing depends on &lt;<i>package</i>&gt;, this will cause it to be immediately removed).</dl>
<p> &lt;<i>package</i>&gt;<code>&#8211;</code></p>
<dl>
<dd>Remove &lt;<i>package</i>&gt;.</dl>
<p> &lt;<i>package</i>&gt;<code>_</code></p>
<dl>
<dd>Purge &lt;<i>package</i>&gt;: remove it and all its associated configuration and data files.</dl>
<p> &lt;<i>package</i>&gt;<code>=</code></p>
<dl>
<dd>Place &lt;<i>package</i>&gt; on hold: cancel any active installation, upgrade, or removal, and prevent this package from being automatically upgraded in the future.</dl>
<p> &lt;<i>package</i>&gt;<code>:</code></p>
<dl>
<dd>Keep &lt;<i>package</i>&gt; at its current version: cancel any installation, removal, or upgrade. Unlike &#8220;hold&#8221; (above) this does not prevent automatic upgrades in the future.</dl>
<p> &lt;<i>package</i>&gt;<code>&amp;M</code></p>
<dl>
<dd>Mark &lt;<i>package</i>&gt; as having been automatically installed.</dl>
<p> &lt;<i>package</i>&gt;<code>&amp;m</code></p>
<dl>
<dd>Mark &lt;<i>package</i>&gt; as having been manually installed.</dl>
<p> As a special case, &#8220;<code>install</code>&#8221; with no arguments will act on any stored/pending actions. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Once you enter <code>Y</code> at the final confirmation prompt, the &#8220;<code>install</code>&#8221; command will modify <code>aptitude</code>&#8216;s stored information about what actions to perform. Therefore, if you issue (e.g.) the command &#8220;<code>aptitude install foo bar</code>&#8221; and then abort the installation once <code>aptitude</code> has started downloading and installing packages, you will need to run &#8220;<code>aptitude remove foo bar</code>&#8221; to cancel that order. </p>
</dl>
</dl>
<p> <code>remove</code>, <code>purge</code>, <code>hold</code>, <code>unhold</code>, <code>keep</code>, <code>reinstall</code></p>
<dl>
<dd>These commands are the same as &#8220;<code>install</code>&#8220;, but apply the named action to all packages given on the command line for which it is not overridden. The difference between <code>hold</code> and <code>keep</code> is that <code>hold</code> will cause a package to be ignored by future <code>safe-upgrade</code> or <code>full-upgrade</code> commands, while <code>keep</code> merely cancels any scheduled actions on the package. <code>unhold</code> will allow a package to be upgraded by future <code>safe-upgrade</code> or <code>full-upgrade</code> commands, without otherwise altering its state. </p>
<p> For instance, &#8220;<code>aptitude remove &#8216;~ndeity&#8217;</code>&#8221; will remove all packages whose name contains &#8220;<code>deity</code>&#8220;.</dl>
<p> <code>markauto</code>, <code>unmarkauto</code></p>
<dl>
<dd>Mark packages as automatically installed or manually installed, respectively. Packages are specified in exactly the same way as for the &#8220;<code>install</code>&#8221; command. For instance, &#8220;<code>aptitude markauto &#8216;~slibs&#8217;</code>&#8221; will mark all packages in the &#8220;<code>libs</code>&#8221; section as having been automatically installed. </p>
<p> For more information on automatically installed packages, see the section &#8220;Managing Automatically Installed Packages&#8221; in the <code>aptitude</code> reference manual.</dl>
<p> <code>build-depends</code>, <code>build-dep</code></p>
<dl>
<dd>Satisfy the build-dependencies of a package. Each package name may be a source package, in which case the build dependencies of that source package are installed; otherwise, binary packages are found in the same way as for the &#8220;<code>install</code>&#8221; command, and the build-dependencies of the source packages that build those binary packages are satisfied. </p>
<p> If the command-line parameter <code>&#8211;arch-only</code> is present, only architecture-dependent build dependencies (i.e., not <code>Build-Depends-Indep</code> or <code>Build-Conflicts-Indep</code>) will be obeyed.</dl>
<p> <code>forbid-version</code></p>
<dl>
<dd>Forbid a package from being upgraded to a particular version. This will prevent <code>aptitude</code> from automatically upgrading to this version, but will allow automatic upgrades to future versions. By default, <code>aptitude</code> will select the version to which the package would normally be upgraded; you may override this selection by appending &#8220;<code>=</code><code>&lt;</code><i>version</i>&gt;&#8221; to the package name: for instance, &#8220;<code>aptitude forbid-version vim=1.2.3.broken-4</code>&#8220;. </p>
<p> This command is useful for avoiding broken versions of packages without having to set and clear manual holds. If you decide you really want the forbidden version after all, &#8220;<code>aptitude install </code><code>&lt;</code><i>package</i>&gt;&#8221; will remove the ban.</dl>
<p> <code>update</code></p>
<dl>
<dd>Updates the list of available packages from the apt sources (this is equivalent to &#8220;<code>apt-get update</code>&#8220;)</dl>
<p> <code>safe-upgrade</code></p>
<dl>
<dd>Upgrades installed packages to their most recent version. Installed packages will not be removed unless they are unused (see the section &#8220;Managing Automatically Installed Packages&#8221; in the <code>aptitude</code> reference manual). Packages which are not currently installed may be installed to resolve dependencies unless the <code>&#8211;no-new-installs</code> command-line option is supplied. </p>
<p> If no &lt;<i>package</i>&gt;s are listed on the command line, <code>aptitude</code> will attempt to upgrade every package that can be upgraded. Otherwise, <code>aptitude</code> will attempt to upgrade only the packages which it is instructed to upgrade. The &lt;<i>package</i>&gt;s can be extended with suffixes in the same manner as arguments to <code>aptitude install</code>, so you can also give additional instructions to <code>aptitude</code> here; for instance, <code>aptitude safe-upgrade bash dash-</code> will attempt to upgrade the bash package and remove the dash package. </p>
<p> It is sometimes necessary to remove one package in order to upgrade another; this command is not able to upgrade packages in such situations. Use the <code>full-upgrade</code> command to upgrade as many packages as possible.</dl>
<p> <code>full-upgrade</code></p>
<dl>
<dd>Upgrades installed packages to their most recent version, removing or installing packages as necessary. This command is less conservative than <code>safe-upgrade</code> and thus more likely to perform unwanted actions. However, it is capable of upgrading packages that <code>safe-upgrade</code> cannot upgrade. </p>
<p> If no &lt;<i>package</i>&gt;s are listed on the command line, <code>aptitude</code> will attempt to upgrade every package that can be upgraded. Otherwise, <code>aptitude</code> will attempt to upgrade only the packages which it is instructed to upgrade. The &lt;<i>package</i>&gt;s can be extended with suffixes in the same manner as arguments to <code>aptitude install</code>, so you can also give additional instructions to <code>aptitude</code> here; for instance, <code>aptitude full-upgrade bash dash-</code> will attempt to upgrade the bash package and remove the dash package. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This command was originally named <code>dist-upgrade</code> for historical reasons, and <code>aptitude</code> still recognizes <code>dist-upgrade</code> as a synonym for <code>full-upgrade</code>. </p>
</dl>
</dl>
<p> <code>keep-all</code></p>
<dl>
<dd>Cancels all scheduled actions on all packages; any packages whose sticky state indicates an installation, removal, or upgrade will have this sticky state cleared.</dl>
<p> <code>forget-new</code></p>
<dl>
<dd>Forgets all internal information about what packages are &#8220;new&#8221; (equivalent to pressing &#8220;f&#8221; when in visual mode).</dl>
<p> <code>search</code></p>
<dl>
<dd>Searches for packages matching one of the patterns supplied on the command line. All packages which match any of the given patterns will be displayed; for instance, &#8220;<code>aptitude search &#8216;~N&#8217; edit</code>&#8221; will list all &#8220;new&#8221; packages and all packages whose name contains &#8220;edit&#8221;. For more information on search patterns, see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 In the example above, &#8220;<code>aptitude search &#8216;~N&#8217; edit</code>&#8221; has two arguments after <code>search</code> and thus is searching for <i>two</i> patterns: &#8220;<code>~N</code>&#8221; and &#8220;<code>edit</code>&#8220;. As described in the search pattern reference, a <i>single</i> pattern composed of two sub-patterns separated by a space (such as &#8220;<code>~N edit</code>&#8220;) matches only if <i>both</i> patterns match. Thus, the command &#8220;<code>aptitude search &#8216;~N edit&#8217;</code>&#8221; will only show &#8220;new&#8221; packages whose name contains &#8220;edit&#8221;. </p>
</dl>
<p> Unless you pass the <code>-F</code> option, the output of <code>aptitude search</code> will look something like this: </p>
<dl>
<dd>
<pre>i apt - Advanced front-end for dpkg
pi apt-build - frontend to apt to build, optimize and in
cp apt-file - APT package searching utility -- command-
ihA raptor-utils - Raptor RDF Parser utilities</pre>
</dl>
<p> Each search result is listed on a separate line. The first character of each line indicates the current state of the package: the most common states are <code>p</code>, meaning that no trace of the package exists on the system, <code>c</code>, meaning that the package was deleted but its configuration files remain on the system, <code>i</code>, meaning that the package is installed, and <code>v</code>, meaning that the package is virtual. The second character indicates the stored action (if any; otherwise a blank space is displayed) to be performed on the package, with the most common actions being <code>i</code>, meaning that the package will be installed, <code>d</code>, meaning that the package will be deleted, and <code>p</code>, meaning that the package and its configuration files will be removed. If the third character is <code>A</code>, the package was automatically installed. </p>
<p> For a complete list of the possible state and action flags, see the section &#8220;Accessing Package Information&#8221; in the <code>aptitude</code> reference guide. To customize the output of <code>search</code>, see the command-line options <code>-F</code> and <code>&#8211;sort</code>.</dl>
<p> <code>show</code></p>
<dl>
<dd>Displays detailed information about one or more packages, listed following the search command. If a package name contains a tilde character (&#8220;<code>~</code>&#8220;) or a question mark (&#8220;<code>?</code>&#8220;), it will be treated as a search pattern and all matching packages will be displayed (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). </p>
<p> If the verbosity level is 1 or greater (i.e., at least one <code>-v</code> is present on the command-line), information about all versions of the package is displayed. Otherwise, information about the &#8220;candidate version&#8221; (the version that &#8220;<code>aptitude install</code>&#8221; would download) is displayed. </p>
<p> You can display information about a different version of the package by appending <code>=</code><code>&lt;</code><i>version</i>&gt; to the package name; you can display the version from a particular archive or release by appending <code>/</code><code>&lt;</code><i>archive</i>&gt; or <code>/</code><code>&lt;</code><i>release</i>&gt; to the package name: for instance, <code>/unstable</code> or <code>/sid</code>. If either of these is present, then only the version you request will be displayed, regardless of the verbosity level. </p>
<p> If the verbosity level is 1 or greater, the package&#8217;s architecture, compressed size, filename, and md5sum fields will be displayed. If the verbosity level is 2 or greater, the select version or versions will be displayed once for each archive in which they are found.</dl>
<p> <code>versions</code></p>
<dl>
<dd>Displays the versions of the packages listed on the command-line. </p>
<dl>
<dd>
<pre>$ aptitude versions wesnoth
p 1:1.4.5-1 100
p 1:1.6.5-1 unstable 500
p 1:1.7.14-1 experimental 1</pre>
</dl>
<p> Each version is listed on a separate line. The leftmost three characters indicate the current state, planned state (if any), and whether the package was automatically installed; for more information on their meanings, see the documentation of <code>aptitude search</code>. To the right of the version number you can find the releases from which the version is available, and the pin priority of the version. </p>
<p> If a package name contains a tilde character (&#8220;<code>~</code>&#8220;) or a question mark (&#8220;<code>?</code>&#8220;), it will be treated as a search pattern and all matching <i>versions</i> will be displayed (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). This means that, for instance, <code>aptitude versions &#8216;~i&#8217;</code> will display all the versions that are currently installed on the system and nothing else, not even other versions of the same packages. </p>
<dl>
<dd>
<pre>$ aptitude versions '~nexim4-daemon-light'
Package exim4-daemon-light:
i 4.71-3 100
p 4.71-4 unstable 500
Package exim4-daemon-light-dbg:
p 4.71-4 unstable 500</pre>
</dl>
<p> If the input is a search pattern, or if more than one package&#8217;s versions are to be displayed, <code>aptitude</code> will automatically group the output by package, as shown above. You can disable this via <code>&#8211;group-by</code><code>=none</code>, in which case <code>aptitude</code> will display a single list of all the versions that were found and automatically include the package name in each output line: </p>
<dl>
<dd>
<pre>$ aptitude versions --group-by=none '~nexim4-daemon-light'
i exim4-daemon-light 4.71-3 100
p exim4-daemon-light 4.71-4 unstable 500
p exim4-daemon-light-dbg 4.71-4 unstable 500</pre>
</dl>
<p> To disable the package name, pass <code>&#8211;show-package-names</code><code>=never</code>: </p>
<dl>
<dd>
<pre>$ aptitude versions --show-package-names=never --group-by=none '~nexim4-daemon-light'
i 4.71-3 100
p 4.71-4 unstable 500
p 4.71-4 unstable 500</pre>
</dl>
<p> In addition to the above options, the information printed for each version can be controlled by the command-line option <code>-F</code>. The order in which versions are displayed can be controlled by the command-line option <code>&#8211;sort</code>. To prevent <code>aptitude</code> from formatting the output into columns, use <code>&#8211;disable-columns</code>.</dl>
<p> <code>add-user-tag</code>, <code>remove-user-tag</code></p>
<dl>
<dd>Adds a user tag to or removes a user tag from the selected group of packages. If a package name contains a tilde (&#8220;<code>~</code>&#8220;) or question mark (&#8220;<code>?</code>&#8220;), it is treated as a search pattern and the tag is added to or removed from all the packages that match the pattern (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). </p>
<p> User tags are arbitrary strings associated with a package. They can be used with the <code>?user-tag(</code><code>&lt;</code><i>tag</i>&gt;<code>)</code> search term, which will select all the packages that have a user tag matching &lt;<i>tag</i>&gt;.</dl>
<p> <code>why</code>, <code>why-not</code></p>
<dl>
<dd>Explains the reason that a particular package should or cannot be installed on the system. </p>
<p> This command searches for packages that require or conflict with the given package. It displays a sequence of dependencies leading to the target package, along with a note indicating the installed state of each package in the dependency chain: </p>
<dl>
<dd>
<pre>$ aptitude why kdepim
i nautilus-data Recommends nautilus
i A nautilus Recommends desktop-base (&gt;= 0.2)
i A desktop-base Suggests gnome | kde | xfce4 | wmaker
p kde Depends kdepim (&gt;= 4:3.4.3)</pre>
</dl>
<p> The command <code>why</code> finds a dependency chain that installs the package named on the command line, as above. Note that the dependency that <code>aptitude</code> produced in this case is only a suggestion. This is because no package currently installed on this computer depends on or recommends the kdepim package; if a stronger dependency were available, <code>aptitude</code> would have displayed it. </p>
<p> In contrast, <code>why-not</code> finds a dependency chain leading to a conflict with the target package: </p>
<dl>
<dd>
<pre>$ aptitude why-not textopo
i ocaml-core Depends ocamlweb
i A ocamlweb Depends tetex-extra | texlive-latex-extra
i A texlive-latex-extra Conflicts textopo</pre>
</dl>
<p> If one or more &lt;<i>pattern</i>&gt;s are present, then <code>aptitude</code> will begin its search at these patterns; that is, the first package in the chain it prints will be a package matching the pattern in question. The patterns are considered to be package names unless they contain a tilde character (&#8220;<code>~</code>&#8220;) or a question mark (&#8220;<code>?</code>&#8220;), in which case they are treated as search patterns (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). </p>
<p> If no patterns are present, then <code>aptitude</code> will search for dependency chains beginning at manually installed packages. This effectively shows the packages that have caused or would cause a given package to be installed. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <code>aptitude why</code> does not perform full dependency resolution; it only displays direct relationships between packages. For instance, if A requires B, C requires D, and B and C conflict, &#8220;<code>aptitude why-not D</code>&#8221; will not produce the answer &#8220;A depends on B, B conflicts with C, and D depends on C&#8221;. </p>
</dl>
<p> By default <code>aptitude</code> outputs only the &#8220;most installed, strongest, tightest, shortest&#8221; dependency chain. That is, it looks for a chain that only contains packages which are installed or will be installed; it looks for the strongest possible dependencies under that restriction; it looks for chains that avoid ORed dependencies and Provides; and it looks for the shortest dependency chain meeting those criteria. These rules are progressively weakened until a match is found. </p>
<p> If the verbosity level is 1 or more, then <i>all</i> the explanations <code>aptitude</code> can find will be displayed, in inverse order of relevance. If the verbosity level is 2 or more, a truly excessive amount of debugging information will be printed to standard output. </p>
<p> This command returns 0 if successful, 1 if no explanation could be constructed, and -1 if an error occurred.</dl>
<p> <code>clean</code></p>
<dl>
<dd>Removes all previously downloaded <code>.deb</code> files from the package cache directory (usually /var/cache/apt/archives).</dl>
<p> <code>autoclean</code></p>
<dl>
<dd>Removes any cached packages which can no longer be downloaded. This allows you to prevent a cache from growing out of control over time without completely emptying it.</dl>
<p> <code>changelog</code></p>
<dl>
<dd>Downloads and displays the Debian changelog for each of the given source or binary packages. </p>
<p> By default, the changelog for the version which would be installed with &#8220;<code>aptitude install</code>&#8221; is downloaded. You can select a particular version of a package by appending <code>=</code><code>&lt;</code><i>version</i>&gt; to the package name; you can select the version from a particular archive or release by appending <code>/</code><code>&lt;</code><i>archive</i>&gt; or <code>/</code><code>&lt;</code><i>release</i>&gt; to the package name (for instance, <code>/unstable</code> or <code>/sid</code>).</dl>
<p> <code>download</code></p>
<dl>
<dd>Downloads the <code>.deb</code> file for the given package to the current directory. If a package name contains a tilde character (&#8220;<code>~</code>&#8220;) or a question mark (&#8220;<code>?</code>&#8220;), it will be treated as a search pattern and all the matching packages will be downloaded (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). </p>
<p> By default, the version which would be installed with &#8220;<code>aptitude install</code>&#8221; is downloaded. You can select a particular version of a package by appending <code>=</code><code>&lt;</code><i>version</i>&gt; to the package name; you can select the version from a particular archive or release by appending <code>/</code><code>&lt;</code><i>archive</i>&gt; or <code>/</code><code>&lt;</code><i>release</i>&gt; to the package name (for instance: <code>/unstable</code> or <code>/sid</code>).</dl>
<p> <code>extract-cache-subset</code></p>
<dl>
<dd>Copy the apt configuration directory (<code>/etc/apt</code>) and a subset of the package database to the specified directory. If no packages are listed, the entire package database is copied; otherwise only the entries corresponding to the named packages are copied. Each package name may be a search pattern, and all the packages matching that pattern will be selected (see the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual). Any existing package database files in the output directory will be overwritten. </p>
<p> Dependencies in binary package stanzas will be rewritten to remove references to packages not in the selected set.</dl>
<p> <code>help</code></p>
<dl>
<dd>Displays a brief summary of the available commands and options.</dl>
<h2>Options</h2>
<p>The following options may be used to modify the behavior of the actions described above. Note that while all options will be accepted for all commands, some options don&#8217;t apply to particular commands and will be ignored by those commands. </p>
<p> <code>&#8211;add-user-tag </code><code>&lt;</code><i>tag</i>&gt;</p>
<dl>
<dd>For <code>full-upgrade</code>, <code>safe-upgrade</code>, <code>forbid-version</code>, <code>hold</code>, <code>install</code>, <code>keep-all</code>, <code>markauto</code>, <code>unmarkauto</code>, <code>purge</code>, <code>reinstall</code>, <code>remove</code>, <code>unhold</code>, and <code>unmarkauto</code>: add the user tag &lt;<i>tag</i>&gt; to all packages that are installed, removed, or upgraded by this command as if with the <code>add-user-tag</code> command.</dl>
<p> <code>&#8211;add-user-tag-to </code><code>&lt;</code><i>tag</i>&gt;<code>,</code><code>&lt;</code><i>pattern</i>&gt;</p>
<dl>
<dd>For <code>full-upgrade</code>, <code>safe-upgrade</code><code>forbid-version</code>, <code>hold</code>, <code>install</code>, <code>keep-all</code>, <code>markauto</code>, <code>unmarkauto</code>, <code>purge</code>, <code>reinstall</code>, <code>remove</code>, <code>unhold</code>, and <code>unmarkauto</code>: add the user tag &lt;<i>tag</i>&gt; to all packages that match &lt;<i>pattern</i>&gt; as if with the <code>add-user-tag</code> command. The pattern is a search pattern as described in the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual. </p>
<p> For instance, <code>aptitude safe-upgrade &#8211;add-user-tag-to &quot;new-installs,?action(install)&quot;</code> will add the tag <code>new-installs</code> to all the packages installed by the <code>safe-upgrade</code> command.</dl>
<p> <code>&#8211;allow-new-upgrades</code></p>
<dl>
<dd>When the safe resolver is being used (i.e., <code>&#8211;safe-resolver</code> was passed, the action is <code>safe-upgrade</code>, or <code>Aptitude::Always-Use-Safe-Resolver</code> is set to <code>true</code>), allow the dependency resolver to install upgrades for packages regardless of the value of <code>Aptitude::Safe-Resolver::No-New-Upgrades</code>.</dl>
<p> <code>&#8211;allow-new-installs</code></p>
<dl>
<dd>Allow the <code>safe-upgrade</code> command to install new packages; when the safe resolver is being used (i.e., <code>&#8211;safe-resolver</code> was passed, the action is <code>safe-upgrade</code>, or <code>Aptitude::Always-Use-Safe-Resolver</code> is set to <code>true</code>), allow the dependency resolver to install new packages. This option takes effect regardless of the value of <code>Aptitude::Safe-Resolver::No-New-Installs</code>.</dl>
<p> <code>&#8211;allow-untrusted</code></p>
<dl>
<dd>Install packages from untrusted sources without prompting. You should only use this if you know what you are doing, as it could easily compromise your system&#8217;s security.</dl>
<p> <code>&#8211;disable-columns</code></p>
<dl>
<dd>This option causes <code>aptitude search</code> and <code>aptitude versions</code> to output their results without any special formatting. In particular: normally <code>aptitude</code> will add whitespace or truncate search results in an attempt to fit its results into vertical &#8220;columns&#8221;. With this flag, each line will be formed by replacing any format escapes in the format string with the corresponding text; column widths will be ignored. </p>
<p> For instance, the first few lines of output from &#8220;<code>aptitude search -F &#8216;%p %V&#8217; &#8211;disable-columns libedataserver</code>&#8221; might be: </p>
<dl>
<dd>
<pre>disksearch 1.2.1-3
hp-search-mac 0.1.3
libbsearch-ruby 1.5-5
libbsearch-ruby1.8 1.5-5
libclass-dbi-abstractsearch-perl 0.07-2
libdbix-fulltextsearch-perl 0.73-10</pre>
</dl>
<p> As in the above example, <code>&#8211;disable-columns</code> is often useful in combination with a custom display format set using the command-line option <code>-F</code>. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Disable-Columns</code>.</dl>
<p> <code>-D</code>, <code>&#8211;show-deps</code></p>
<dl>
<dd>For commands that will install or remove packages (<code>install</code>, <code>full-upgrade</code>, etc), show brief explanations of automatic installations and removals. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Show-Deps</code>.</dl>
<p> <code>-d</code>, <code>&#8211;download-only</code></p>
<dl>
<dd>Download packages to the package cache as necessary, but do not install or remove anything. By default, the package cache is stored in /var/cache/apt/archives. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Download-Only</code>.</dl>
<p> <code>-F</code> &lt;<i>format</i>&gt;, <code>&#8211;display-format</code> &lt;<i>format</i>&gt;</p>
<dl>
<dd>Specify the format which should be used to display output from the <code>search</code> and <code>versions</code> commands. For instance, passing &#8220;<code>%p %V %v</code>&#8221; for &lt;<i>format</i>&gt; will display a package&#8217;s name, followed by its currently installed version and its available version (see the section &#8220;Customizing how packages are displayed&#8221; in the <code>aptitude</code> reference manual for more information). </p>
<p> The command-line option <code>&#8211;disable-columns</code> is often useful in combination with <code>-F</code>. </p>
<p> For <code>search</code>, this corresponds to the configuration option <code>Aptitude::CmdLine::Package-Display-Format</code>; for <code>versions</code>, this corresponds to the configuration option <code>Aptitude::CmdLine::Version-Display-Format</code>.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Try hard to fix the dependencies of broken packages, even if it means ignoring the actions requested on the command line. </p>
<p> This corresponds to the configuration item <code>Aptitude::CmdLine::Fix-Broken</code>.</dl>
<p> <code>&#8211;full-resolver</code></p>
<dl>
<dd>When package dependency problems are encountered, use the default &#8220;full&#8221; resolver to solve them. Unlike the &#8220;safe&#8221; resolver activated by <code>&#8211;safe-resolver</code>, the full resolver will happily remove packages to fulfill dependencies. It can resolve more situations than the safe algorithm, but its solutions are more likely to be undesirable. </p>
<p> This option can be used to force the use of the full resolver even when <code>Aptitude::Always-Use-Safe-Resolver</code> is true. The <code>safe-upgrade</code> command never uses the full resolver and does not accept the <code>&#8211;full-resolver</code> option.</dl>
<p> <code>&#8211;group-by</code> &lt;<i>grouping-mode</i>&gt;</p>
<dl>
<dd>Control how the <code>versions</code> command groups its output. The following values are recognized: </p>
<dl>
<dd>&bull; <code>archive</code> to group packages by the archive they occur in (&#8220;<code>stable</code>&#8220;, &#8220;<code>unstable</code>&#8220;, etc). If a package occurs in several archives, it will be displayed in each of them.</dl>
<dl>
<dd>&bull; <code>auto</code> to group versions by their package unless there is exactly one argument and it is not a search pattern.</dl>
<dl>
<dd>&bull; <code>none</code> to display all the versions in a single list without any grouping.</dl>
<dl>
<dd>&bull; <code>package</code> to group versions by their package.</dl>
<dl>
<dd>&bull; <code>source-package</code> to group versions by their source package.</dl>
<dl>
<dd>&bull; <code>source-version</code> to group versions by their source package and source version.</dl>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Versions-Group-By</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display a brief help message. Identical to the <code>help</code> action.</dl>
<p> <code>&#8211;log-file=</code><code>&lt;</code><i>file</i>&gt;</p>
<dl>
<dd>If &lt;<i>file</i>&gt; is a nonempty string, log messages will be written to it, except that if &lt;<i>file</i>&gt; is &#8220;<code>&#8211;</code>&#8220;, the messages will be written to standard output instead. If this option appears multiple times, the last occurrence is the one that will take effect. </p>
<p> This does not affect the log of installations that <code>aptitude</code> has performed (/var/log/aptitude); the log messages written using this configuration include internal program events, errors, and debugging messages. See the command-line option <code>&#8211;log-level</code> to get more control over what gets logged. </p>
<p> This corresponds to the configuration option <code>Aptitude::Logging::File</code>.</dl>
<p> <code>&#8211;log-level=</code><code>&lt;</code><i>level</i>&gt;, <code>&#8211;log-level=</code><code>&lt;</code><i>category</i>&gt;<code>:</code><code>&lt;</code><i>level</i>&gt;</p>
<dl>
<dd><code>&#8211;log-level=</code><code>&lt;</code><i>level</i>&gt; causes <code>aptitude</code> to only log messages whose level is &lt;<i>level</i>&gt; or higher. For instance, setting the log level to <code>error</code> will cause only messages at the log levels <code>error</code> and <code>fatal</code> to be displayed; all others will be hidden. Valid log levels (in descending order) are <code>off</code>, <code>fatal</code>, <code>error</code>, <code>warn</code>, <code>info</code>, <code>debug</code>, and <code>trace</code>. The default log level is <code>warn</code>. </p>
<p> <code>&#8211;log-level=</code><code>&lt;</code><i>category</i>&gt;<code>:</code><code>&lt;</code><i>level</i>&gt; causes messages in &lt;<i>category</i>&gt; to only be logged if their level is &lt;<i>level</i>&gt; or higher. </p>
<p> <code>&#8211;log-level</code> may appear multiple times on the command line; the most specific setting is the one that takes effect, so if you pass <code>&#8211;log-level=aptitude.resolver:fatal</code> and <code>&#8211;log-level=aptitude.resolver.hints.match:trace</code>, then messages in <code>aptitude.resolver.hints.parse</code> will only be printed if their level is <code>fatal</code>, but all messages in <code>aptitude.resolver.hints.match</code> will be printed. If you set the level of the same category two or more times, the last setting is the one that will take effect. </p>
<p> This does not affect the log of installations that <code>aptitude</code> has performed (/var/log/aptitude); the log messages written using this configuration include internal program events, errors, and debugging messages. See the command-line option <code>&#8211;log-file</code> to change where log messages go. </p>
<p> This corresponds to the configuration group <code>Aptitude::Logging::Levels</code>.</dl>
<p> <code>&#8211;log-resolver</code></p>
<dl>
<dd>Set some standard log levels related to the resolver, to produce logging output suitable for processing with automated tools. This is equivalent to the command-line options <code>&#8211;log-level=aptitude.resolver.search:trace &#8211;log-level=aptitude.resolver.search.tiers:info</code>.</dl>
<p> <code>&#8211;no-new-installs</code></p>
<dl>
<dd>Prevent <code>safe-upgrade</code> from installing any new packages; when the safe resolver is being used (i.e., <code>&#8211;safe-resolver</code> was passed or <code>Aptitude::Always-Use-Safe-Resolver</code> is set to <code>true</code>), forbid the dependency resolver from installing new packages. This option takes effect regardless of the value of <code>Aptitude::Safe-Resolver::No-New-Installs</code>. </p>
<p> This mimics the historical behavior of <code>apt-get upgrade</code>.</dl>
<p> <code>&#8211;no-new-upgrades</code></p>
<dl>
<dd>When the safe resolver is being used (i.e., <code>&#8211;safe-resolver</code> was passed or <code>Aptitude::Always-Use-Safe-Resolver</code> is set to <code>true</code>), forbid the dependency resolver from installing upgrades for packages regardless of the value of <code>Aptitude::Safe-Resolver::No-New-Upgrades</code>.</dl>
<p> <code>&#8211;no-show-resolver-actions</code></p>
<dl>
<dd>Do not display the actions performed by the &#8220;safe&#8221; resolver, overriding any configuration option or earlier <code>&#8211;show-resolver-actions</code>.</dl>
<p> <code>-O</code> &lt;<i>order</i>&gt;, <code>&#8211;sort</code> &lt;<i>order</i>&gt;</p>
<dl>
<dd>Specify the order in which output from the <code>search</code> and <code>versions</code> commands should be displayed. For instance, passing &#8220;<code>installsize</code>&#8221; for &lt;<i>order</i>&gt; will list packages in order according to their size when installed (see the section &#8220;Customizing how packages are sorted&#8221; in the <code>aptitude</code> reference manual for more information). </p>
<p> The default sort order is <code>name,version</code>.</dl>
<p> <code>-o</code> &lt;<i>key</i>&gt;<code>=</code>&lt;<i>value</i>&gt;</p>
<dl>
<dd>Set a configuration file option directly; for instance, use <code>-o Aptitude::Log=/tmp/my-log</code> to log <code>aptitude</code>&#8216;s actions to /tmp/my-log. For more information on configuration file options, see the section &#8220;Configuration file reference&#8221; in the <code>aptitude</code> reference manual.</dl>
<p> <code>-P</code>, <code>&#8211;prompt</code></p>
<dl>
<dd>Always display a prompt before downloading, installing or removing packages, even when no actions other than those explicitly requested will be performed. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Always-Prompt</code>.</dl>
<p> <code>&#8211;purge-unused</code></p>
<dl>
<dd>If <code>Aptitude::Delete-Unused</code> is set to &#8220;<code>true</code>&#8221; (its default), then in addition to removing each package that is no longer required by any installed package, <code>aptitude</code> will also purge them, removing their configuration files and perhaps other important data. For more information about which packages are considered to be &#8220;unused&#8221;, see the section &#8220;Managing Automatically Installed Packages&#8221; in the <code>aptitude</code> reference manual. <i>THIS OPTION CAN CAUSE DATA LOSS! DO NOT USE IT UNLESS YOU KNOW WHAT YOU ARE DOING!</i> </p>
<p> This corresponds to the configuration option <code>Aptitude::Purge-Unused</code>.</dl>
<p> <code>-q</code><code>[=&lt;</code><i>n</i>&gt;], <code>&#8211;quiet</code><code>[=&lt;</code><i>n</i>&gt;]</p>
<dl>
<dd>Suppress all incremental progress indicators, thus making the output loggable. This may be supplied multiple times to make the program quieter, but unlike <code>apt-get</code>, <code>aptitude</code> does not enable <code>-y</code> when <code>-q</code> is supplied more than once. </p>
<p> The optional <code>=</code><code>&lt;</code><i>n</i>&gt; may be used to directly set the amount of quietness (for instance, to override a setting in /etc/apt/apt.conf); it causes the program to behave as if <code>-q</code> had been passed exactly &lt;<i>n</i>&gt; times.</dl>
<p> <code>-R</code>, <code>&#8211;without-recommends</code></p>
<dl>
<dd>Do <i>not</i> treat recommendations as dependencies when installing new packages (this overrides settings in /etc/apt/apt.conf and ~/.aptitude/config). Packages previously installed due to recommendations will not be removed. </p>
<p> This corresponds to the pair of configuration options <code>Apt::Install-Recommends</code> and <code>Apt::AutoRemove::InstallRecommends</code>.</dl>
<p> <code>-r</code>, <code>&#8211;with-recommends</code></p>
<dl>
<dd>Treat recommendations as dependencies when installing new packages (this overrides settings in /etc/apt/apt.conf and ~/.aptitude/config). </p>
<p> This corresponds to the configuration option <code>Apt::Install-Recommends</code></dl>
<p> <code>&#8211;remove-user-tag </code><code>&lt;</code><i>tag</i>&gt;</p>
<dl>
<dd>For <code>full-upgrade</code>, <code>safe-upgrade</code><code>forbid-version</code>, <code>hold</code>, <code>install</code>, <code>keep-all</code>, <code>markauto</code>, <code>unmarkauto</code>, <code>purge</code>, <code>reinstall</code>, <code>remove</code>, <code>unhold</code>, and <code>unmarkauto</code>: remove the user tag &lt;<i>tag</i>&gt; from all packages that are installed, removed, or upgraded by this command as if with the <code>add-user-tag</code> command.</dl>
<p> <code>&#8211;remove-user-tag-from </code><code>&lt;</code><i>tag</i>&gt;<code>,</code><code>&lt;</code><i>pattern</i>&gt;</p>
<dl>
<dd>For <code>full-upgrade</code>, <code>safe-upgrade</code><code>forbid-version</code>, <code>hold</code>, <code>install</code>, <code>keep-all</code>, <code>markauto</code>, <code>unmarkauto</code>, <code>purge</code>, <code>reinstall</code>, <code>remove</code>, <code>unhold</code>, and <code>unmarkauto</code>: remove the user tag &lt;<i>tag</i>&gt; from all packages that match &lt;<i>pattern</i>&gt; as if with the <code>remove-user-tag</code> command. The pattern is a search pattern as described in the section &#8220;Search Patterns&#8221; in the <code>aptitude</code> reference manual. </p>
<p> For instance, <code>aptitude safe-upgrade &#8211;remove-user-tag-from &quot;not-upgraded,?action(upgrade)&quot;</code> will remove the <code>not-upgraded</code> tag from all packages that the <code>safe-upgrade</code> command is able to upgrade.</dl>
<p> <code>-s</code>, <code>&#8211;simulate</code></p>
<dl>
<dd>In command-line mode, print the actions that would normally be performed, but don&#8217;t actually perform them. This does not require root privileges. In the visual interface, always open the cache in read-only mode regardless of whether you are root. </p>
<p> This corresponds to the configuration option <code>Aptitude::Simulate</code>.</dl>
<p> <code>&#8211;safe-resolver</code></p>
<dl>
<dd>When package dependency problems are encountered, use a &#8220;safe&#8221; algorithm to solve them. This resolver attempts to preserve as many of your choices as possible; it will never remove a package or install a version of a package other than the package&#8217;s default candidate version. It is the same algorithm used in <code>safe-upgrade</code>; indeed, <code>aptitude &#8211;safe-resolver full-upgrade</code> is equivalent to <code>aptitude safe-upgrade</code>. Because <code>safe-upgrade</code> always uses the safe resolver, it does not accept the <code>&#8211;safe-resolver</code> flag. </p>
<p> This option is equivalent to setting the configuration variable <code>Aptitude::Always-Use-Safe-Resolver</code> to <code>true</code>.</dl>
<p> <code>&#8211;schedule-only</code></p>
<dl>
<dd>For commands that modify package states, schedule operations to be performed in the future, but don&#8217;t perform them. You can execute scheduled actions by running <code>aptitude install</code> with no arguments. This is equivalent to making the corresponding selections in visual mode, then exiting the program normally. </p>
<p> For instance, <code>aptitude &#8211;schedule-only install evolution</code> will schedule the <code>evolution</code> package for later installation.</dl>
<p> <code>&#8211;show-package-names</code> &lt;<i>when</i>&gt;</p>
<dl>
<dd>Controls when the <code>versions</code> command shows package names. The following settings are allowed: </p>
<dl>
<dd>&bull; <code>always</code>: display package names every time that <code>aptitude versions</code> runs.</dl>
<dl>
<dd>&bull; <code>auto</code>: display package names when <code>aptitude versions</code> runs if the output is not grouped by package, and either there is a pattern-matching argument or there is more than one argument.</dl>
<dl>
<dd>&bull; <code>never</code>: never display package names in the output of <code>aptitude versions</code>.</dl>
<p> This option corresponds to the configuration item <code>Aptitude::CmdLine::Versions-Show-Package-Names</code>.</dl>
<p> <code>&#8211;show-resolver-actions</code></p>
<dl>
<dd>Display the actions performed by the &#8220;safe&#8221; resolver and by <code>safe-upgrade</code>. </p>
<p> When executing the command <code>safe-upgrade</code> or when the option &#8211;safe-resolver is present, <code>aptitude</code> will display a summary of the actions performed by the resolver before printing the installation preview. This is equivalent to the configuration option <code>Aptitude::Safe-Resolver::Show-Resolver-Actions</code>.</dl>
<p> <code>&#8211;show-summary</code><code>[=&lt;</code><i>MODE</i>&gt;]</p>
<dl>
<dd>Changes the behavior of &#8220;<code>aptitude why</code>&#8221; to summarize each dependency chain that it outputs, rather than displaying it in long form. If this option is present and &lt;<i>MODE</i>&gt; is not &#8220;<code>no-summary</code>&#8220;, chains that contain Suggests dependencies will not be displayed: combine <code>&#8211;show-summary</code> with <code>-v</code> to see a summary of all the reasons for the target package to be installed. </p>
<p> &lt;<i>MODE</i>&gt; can be any one of the following: </p>
<dl>
<dd>1. <code>no-summary</code>: don&#8217;t show a summary (the default behavior if <code>&#8211;show-summary</code> is not present).</dl>
<dl>
<dd>2. <code>first-package</code>: display the first package in each chain. This is the default value of &lt;<i>MODE</i>&gt; if it is not present.</dl>
<dl>
<dd>3. <code>first-package-and-type</code>: display the first package in each chain, along with the strength of the weakest dependency in the chain.</dl>
<dl>
<dd>4. <code>all-packages</code>: briefly display each chain of dependencies leading to the target package.</dl>
<dl>
<dd>5. <code>all-packages-with-dep-versions</code>: briefly display each chain of dependencies leading to the target package, including the target version of each dependency.</dl>
<p> This option corresponds to the configuration item <code>Aptitude::CmdLine::Show-Summary</code>; if <code>&#8211;show-summary</code> is present on the command-line, it will override <code>Aptitude::CmdLine::Show-Summary</code>. </p>
<p> <code>Example 10. Usage of &#8211;show-summary</code> <code>&#8211;show-summary</code> used with <code>-v</code> to display all the reasons a package is installed: </p>
<dl>
<dd>
<pre>$ aptitude -v --show-summary why foomatic-db
Packages requiring foomatic-db:
 cupsys-driver-gutenprint
 foomatic-db-engine
 foomatic-db-gutenprint
 foomatic-db-hpijs
 foomatic-filters-ppds
 foomatic-gui
 kde
 printconf
 wine
$ aptitude -v --show-summary=first-package-and-type why foomatic-db
Packages requiring foomatic-db:
 [Depends] cupsys-driver-gutenprint
 [Depends] foomatic-db-engine
 [Depends] foomatic-db-gutenprint
 [Depends] foomatic-db-hpijs
 [Depends] foomatic-filters-ppds
 [Depends] foomatic-gui
 [Depends] kde
 [Depends] printconf
 [Depends] wine
$ aptitude -v --show-summary=all-packages why foomatic-db
Packages requiring foomatic-db:
 cupsys-driver-gutenprint D: cups-driver-gutenprint D: cups R: foomatic-filters R: foomatic-db-engine D: foomatic-db
 foomatic-filters-ppds D: foomatic-filters R: foomatic-db-engine D: foomatic-db
 kde D: kdeadmin R: system-config-printer-kde D: system-config-printer R: hal-cups-utils D: cups R: foomatic-filters R: foomatic-db-engine D: foomatic-db
 wine D: libwine-print D: cups-bsd R: cups R: foomatic-filters R: foomatic-db-engine D: foomatic-db
 foomatic-db-engine D: foomatic-db
 foomatic-db-gutenprint D: foomatic-db
 foomatic-db-hpijs D: foomatic-db
 foomatic-gui D: python-foomatic D: foomatic-db-engine D: foomatic-db
 printconf D: foomatic-db
$ aptitude -v --show-summary=all-packages-with-dep-versions why foomatic-db
Packages requiring foomatic-db:
 cupsys-driver-gutenprint D: cups-driver-gutenprint (&gt;= 5.0.2-4) D: cups (&gt;= 1.3.0) R: foomatic-filters (&gt;= 4.0) R: foomatic-db-engine (&gt;= 4.0) D: foomatic-db (&gt;= 20090301)
 foomatic-filters-ppds D: foomatic-filters R: foomatic-db-engine (&gt;= 4.0) D: foomatic-db (&gt;= 20090301)
 kde D: kdeadmin (&gt;= 4:3.5.5) R: system-config-printer-kde (&gt;= 4:4.2.2-1) D: system-config-printer (&gt;= 1.0.0) R: hal-cups-utils D: cups R: foomatic-filters (&gt;= 4.0) R: foomatic-db-engine (&gt;= 4.0) D: foomatic-db (&gt;= 20090301)
 wine D: libwine-print (= 1.1.15-1) D: cups-bsd R: cups R: foomatic-filters (&gt;= 4.0) R: foomatic-db-engine (&gt;= 4.0) D: foomatic-db (&gt;= 20090301)
 foomatic-db-engine D: foomatic-db
 foomatic-db-gutenprint D: foomatic-db
 foomatic-db-hpijs D: foomatic-db
 foomatic-gui D: python-foomatic (&gt;= 0.7.9.2) D: foomatic-db-engine D: foomatic-db (&gt;= 20090301)
 printconf D: foomatic-db</pre>
</dl>
<p> <code>&#8211;show-summary</code> used to list a chain on one line: </p>
<dl>
<dd>
<pre>$ aptitude --show-summary=all-packages why aptitude-gtk libglib2.0-data
Packages requiring libglib2.0-data:
 aptitude-gtk D: libglib2.0-0 R: libglib2.0-data</pre>
</dl>
</dl>
<p> <code>-t</code> &lt;<i>release</i>&gt;, <code>&#8211;target-release</code> &lt;<i>release</i>&gt;</p>
<dl>
<dd>Set the release from which packages should be installed. For instance, &#8220;<code>aptitude -t experimental &#8230;</code>&#8221; will install packages from the experimental distribution unless you specify otherwise. For the command-line actions &#8220;changelog&#8221;, &#8220;download&#8221;, and &#8220;show&#8221;, this is equivalent to appending <code>/</code><code>&lt;</code><i>release</i>&gt; to each package named on the command-line; for other commands, this will affect the default candidate version of packages according to the rules described in <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5). </p>
<p> This corresponds to the configuration item <code>APT::Default-Release</code>.</dl>
<p> <code>-V</code>, <code>&#8211;show-versions</code></p>
<dl>
<dd>Show which versions of packages will be installed. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Show-Versions</code>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Causes some commands (for instance, <code>show</code>) to display extra information. This may be supplied multiple times to get more and more information. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Verbose</code>.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Display the version of <code>aptitude</code> and some information about how it was compiled.</dl>
<p> <code>&#8211;visual-preview</code></p>
<dl>
<dd>When installing or removing packages from the command line, instead of displaying the usual prompt, start up the visual interface and display its preview screen.</dl>
<p> <code>-W</code>, <code>&#8211;show-why</code></p>
<dl>
<dd>In the preview displayed before packages are installed or removed, show which manually installed package requires each automatically installed package. For instance: </p>
<dl>
<dd>
<pre>$ aptitude --show-why install mediawiki
...
The following NEW packages will be installed:
 libapache2-mod-php5{a} (for mediawiki) mediawiki php5{a} (for mediawiki)
 php5-cli{a} (for mediawiki) php5-common{a} (for mediawiki)
 php5-mysql{a} (for mediawiki)</pre>
</dl>
<p> When combined with <code>-v</code> or a non-zero value for <code>Aptitude::CmdLine::Verbose</code>, this displays the entire chain of dependencies that lead each package to be installed. For instance: </p>
<dl>
<dd>
<pre>$ aptitude -v --show-why install libdb4.2-dev
The following NEW packages will be installed:
 libdb4.2{a} (libdb4.2-dev D: libdb4.2) libdb4.2-dev
The following packages will be REMOVED:
 libdb4.4-dev{a} (libdb4.2-dev C: libdb-dev P&lt;- libdb-dev)</pre>
</dl>
<p> This option will also describe why packages are being removed, as shown above. In this example, libdb4.2-dev conflicts with libdb-dev, which is provided by libdb-dev. </p>
<p> This argument corresponds to the configuration option <code>Aptitude::CmdLine::Show-Why</code> and displays the same information that is computed by <code>aptitude why</code> and <code>aptitude why-not</code>.</dl>
<p> <code>-w</code> &lt;<i>width</i>&gt;, <code>&#8211;width</code> &lt;<i>width</i>&gt;</p>
<dl>
<dd>Specify the display width which should be used for output from the <code>search</code> command (by default, the terminal width is used). </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Package-Display-Width</code></dl>
<p> <code>-y</code>, <code>&#8211;assume-yes</code></p>
<dl>
<dd>When a yes/no prompt would be presented, assume that the user entered &#8220;yes&#8221;. In particular, suppresses the prompt that appears when installing, upgrading, or removing packages. Prompts for &#8220;dangerous&#8221; actions, such as removing essential packages, will still be displayed. This option overrides <code>-P</code>. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Assume-Yes</code>.</dl>
<p> <code>-Z</code></p>
<dl>
<dd>Show how much disk space will be used or freed by the individual packages being installed, upgraded, or removed. </p>
<p> This corresponds to the configuration option <code>Aptitude::CmdLine::Show-Size-Changes</code>.</dl>
<p> The following options apply to the visual mode of the program, but are primarily for internal use; you generally won&#8217;t need to use them yourself. </p>
<p> <code>&#8211;autoclean-on-startup</code></p>
<dl>
<dd>Deletes old downloaded files when the program starts (equivalent to starting the program and immediately selecting Actions &rarr; Clean obsolete files). You cannot use this option and &#8220;<code>&#8211;autoclean-on-startup</code>&#8220;, &#8220;<code>-i</code>&#8220;, or &#8220;<code>-u</code>&#8221; at the same time.</dl>
<p> <code>&#8211;clean-on-startup</code></p>
<dl>
<dd>Cleans the package cache when the program starts (equivalent to starting the program and immediately selecting Actions &rarr; Clean package cache). You cannot use this option and &#8220;<code>&#8211;autoclean-on-startup</code>&#8220;, &#8220;<code>-i</code>&#8220;, or &#8220;<code>-u</code>&#8221; at the same time.</dl>
<p> <code>-i</code></p>
<dl>
<dd>Displays a download preview when the program starts (equivalent to starting the program and immediately pressing &#8220;g&#8221;). You cannot use this option and &#8220;<code>&#8211;autoclean-on-startup</code>&#8220;, &#8220;<code>&#8211;clean-on-startup</code>&#8220;, or &#8220;<code>-u</code>&#8221; at the same time.</dl>
<p> <code>-S</code> &lt;<i>fname</i>&gt;</p>
<dl>
<dd>Loads the extended state information from &lt;<i>fname</i>&gt; instead of the standard state file.</dl>
<p> <code>-u</code></p>
<dl>
<dd>Begins updating the package lists as soon as the program starts. You cannot use this option and &#8220;<code>&#8211;autoclean-on-startup</code>&#8220;, &#8220;<code>&#8211;clean-on-startup</code>&#8220;, or &#8220;<code>-i</code>&#8221; at the same time.</dl>
<h2>Environment</h2>
<p><code>HOME</code></p>
<dl>
<dd>If $HOME/.aptitude exists, <code>aptitude</code> will store its configuration file in $HOME/.aptitude/config. Otherwise, it will look up the current user&#8217;s home directory using <code><a href="/docs/linux/man/2-getpwuid/">getpwuid</a></code>(2) and place its configuration file there.</dl>
<p> <code>PAGER</code></p>
<dl>
<dd>If this environment variable is set, <code>aptitude</code> will use it to display changelogs when &#8220;<code>aptitude changelog</code>&#8221; is invoked. If not set, it defaults to <code>more</code>.</dl>
<p> <code>TMP</code></p>
<dl>
<dd>If <code>TMPDIR</code> is unset, <code>aptitude</code> will store its temporary files in <code>TMP</code> if that variable is set. Otherwise, it will store them in /tmp.</dl>
<p> <code>TMPDIR</code></p>
<dl>
<dd><code>aptitude</code> will store its temporary files in the directory indicated by this environment variable. If <code>TMPDIR</code> is not set, then <code>TMP</code> will be used; if <code>TMP</code> is also unset, then <code>aptitude</code> will use /tmp.</dl>
<h2>Files</h2>
<p>/var/lib/aptitude/pkgstates</p>
<dl>
<dd>The file in which stored package states and some package flags are stored.</dl>
<p> /etc/apt/apt.conf, /etc/apt/apt.conf.d/*, ~/.aptitude/config</p>
<dl>
<dd>The configuration files for <code>aptitude</code>. ~/.aptitude/config overrides /etc/apt/apt.conf. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for documentation of the format and contents of these files.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8), /usr/share/doc/aptitude/html/&lt;<i>lang</i>&gt;/index.html from the package aptitude-doc-&lt;<i>lang</i>&gt;</p>
<h2>Author</h2>
<p><code>Daniel Burrows</code> &lt;dburrows [at] debian.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright 2004-2011 Daniel Burrows. </p>
<p> This manual page is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This manual page is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</p>
