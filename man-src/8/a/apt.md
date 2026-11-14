---
title: "apt(8)"
name: "apt"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt/"
description: "apt – command-line interface"
---

<p>apt &#8211; command-line interface</p>
<h2>Synopsis</h2>
<pre><code>apt [-h] [-o=config_string] [-c=config_file] [-t=target_release] [-a=architecture] {list | search | show | update | install pkg [{=pkg_version_number | /target_release}]...  | remove pkg...  | upgrade | full-upgrade | edit-sources | {-v | --version} | {-h | --help}}</code></pre>
<h2>Description</h2>
<p><code>apt</code></p>
<dd>provides a high-level commandline interface for the package management system. It is intended as an end user interface and enables some options better suited for interactive usage by default compared to more specialized APT tools like <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) and <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8). </p>
<p> Much like <code>apt</code> itself, its manpage is intended as an end user interface and as such only mentions the most used commands and options partly to not duplicate information in multiple places and partly to avoid overwhelming readers with a cornucopia of options and details. </p>
<p> <code>update</code> (<code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8))</p>
<dl>
<dd><code>update</code> is used to download package information from all configured sources. Other commands operate on this data to e.g. perform package upgrades or search in and display details about all packages available for installation.</dl>
<p> <code>upgrade</code> (<code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8))</p>
<dl>
<dd><code>upgrade</code> is used to install available upgrades of all packages currently installed on the system from the sources configured via <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5). New packages will be installed if required to satisfy dependencies, but existing packages will never be removed. If an upgrade for a package requires the removal of an installed package the upgrade for this package isn&#8217;t performed.</dl>
<p> <code>full-upgrade</code> (<code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8))</p>
<dl>
<dd>full-upgrade performs the function of upgrade but will remove currently installed packages if this is needed to upgrade the system as a whole.</dl>
<p> <code>install</code>, <code>reinstall</code>, <code>remove</code>, <code>purge</code> (<code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8))</p>
<dl>
<dd>Performs the requested action on one or more packages specified via <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) or exact match. The requested action can be overridden for specific packages by appending a plus (+) to the package name to install this package or a minus (-) to remove it. </p>
<p> A specific version of a package can be selected for installation by following the package name with an equals (=) and the version of the package to select. Alternatively the version from a specific release can be selected by following the package name with a forward slash (/) and codename (bullseye, bookworm, sid &#8230;) or suite name (stable, testing, unstable). This will also select versions from this release for dependencies of this package if needed to satisfy the request. </p>
<p> Removing a package removes all packaged data, but leaves usually small (modified) user configuration files behind, in case the remove was an accident. Just issuing an installation request for the accidentally removed package will restore its function as before in that case. On the other hand you can get rid of these leftovers by calling <code>purge</code> even on already removed packages. Note that this does not affect any data or configuration stored in your home directory.</dl>
<p> <code>autoremove</code> (<code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8))</p>
<dl>
<dd>autoremove is used to remove packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed as dependencies changed or the package(s) needing them were removed in the meantime. </p>
<p> You should check that the list does not include applications you have grown to like even though they were once installed just as a dependency of another package. You can mark such a package as manually installed by using <code><a href="/docs/linux/man/8-apt-mark/">apt-mark</a></code>(8). Packages which you have installed explicitly via <code>install</code> are also never proposed for automatic removal.</dl>
<p> <code>satisfy</code> (<code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8))</p>
<dl>
<dd><code>satisfy</code> satisfies dependency strings, as used in Build-Depends. It also handles conflicts, by prefixing an argument with &quot;Conflicts: &quot;. </p>
<p> Example: apt satisfy &quot;foo, bar (&gt;= 1.0)&quot; &quot;Conflicts: baz, fuzz&quot;</dl>
<p> <code>search</code> (<code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8))</p>
<dl>
<dd><code>search</code> can be used to search for the given <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) term(s) in the list of available packages and display matches. This can e.g. be useful if you are looking for packages having a specific feature. If you are looking for a package including a specific file try <code><a href="/docs/linux/man/1-apt-file/">apt-file</a></code>(1).</dl>
<p> <code>show</code> (<code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8))</p>
<dl>
<dd>Show information about the given package(s) including its dependencies, installation and download size, sources the package is available from, the description of the packages content and much more. It can e.g. be helpful to look at this information before allowing <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) to remove a package or while searching for new packages to install.</dl>
<p> <code>list</code></p>
<dl>
<dd><code>list</code> is somewhat similar to <code>dpkg-query &#8211;list</code> in that it can display a list of packages satisfying certain criteria. It supports <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) patterns for matching package names as well as options to list installed (<code>&#8211;installed</code>), upgradeable (<code>&#8211;upgradeable</code>) or all available (<code>&#8211;all-versions</code>) versions.</dl>
<p> <code>edit-sources</code> (work-in-progress)</p>
<dl>
<dd>edit-sources lets you edit your <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) files in your preferred text editor while also providing basic sanity checks.</dl>
<h2>Script Usage And Differences From Other Apt Tools</h2>
<p>The <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) commandline is designed as an end-user tool and it may change behavior between versions. While it tries not to break backward compatibility this is not guaranteed either if a change seems beneficial for interactive use. </p>
<p> All features of <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) are available in dedicated APT tools like <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) and <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8) as well. <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) just changes the default value of some options (see <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) and specifically the Binary scope). So you should prefer using these commands (potentially with some additional options enabled) in your scripts as they keep backward compatibility as much as possible.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8), <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5), <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5), <code><a href="/docs/linux/man/8-apt-config/">apt-config</a></code>(8), The APT User&#8217;s guide in /usr/share/doc/apt-doc/, <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5), the APT Howto.</p>
<h2>Diagnostics</h2>
<p><code>apt</code> returns zero on normal operation, decimal 100 on error.</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p><code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
