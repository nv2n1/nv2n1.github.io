---
title: "apt-cache(8)"
name: "apt-cache"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-cache/"
description: "apt-cache – query the APT cache"
---

<p>apt-cache &#8211; query the APT cache</p>
<h2>Synopsis</h2>
<pre><code>apt-cache [-agipns] [-o=config_string] [-c=config_file] {gencaches | showpkg pkg...  | showsrc pkg...  | stats | dump | dumpavail | unmet | search regex...  | show pkg [{=pkg_version_number | /target_release}]...  | depends pkg [{=pkg_version_number | /target_release}]...  | rdepends pkg [{=pkg_version_number | /target_release}]...  | pkgnames [prefix]  | dotty pkg [{=pkg_version_number | /target_release}]...  | xvcg pkg [{=pkg_version_number | /target_release}]...  | policy [pkg...]  | madison pkg...  | {-v | --version} | {-h | --help}}</code></pre>
<h2>Description</h2>
<p><code>apt-cache</code></p>
<dd>performs a variety of operations on APT&#8217;s package cache. <code>apt-cache</code> does not manipulate the state of the system but does provide operations to search and generate interesting output from the package metadata. The metadata is acquired and updated via the &#8216;update&#8217; command of e.g. <code>apt-get</code>, so that it can be outdated if the last update is too long ago, but in exchange <code>apt-cache</code> works independently of the availability of the configured sources (e.g. offline). Unless the <code>-h</code>, or <code>&#8211;help</code> option is given, one of the commands below must be present. <code>gencaches</code></p>
<dl>
<dd>gencaches creates APT&#8217;s package cache. This is done implicitly by all commands needing this cache if it is missing or outdated.</dl>
<p> <code>showpkg</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>showpkg displays information about the packages listed on the command line. Remaining arguments are package names. The available versions and reverse dependencies of each package listed are listed, as well as forward dependencies for each version. Forward (normal) dependencies are those packages upon which the package in question depends; reverse dependencies are those packages that depend upon the package in question. Thus, forward dependencies must be satisfied for a package, but reverse dependencies need not be. For instance, <code>apt-cache showpkg libreadline2</code> would produce output similar to the following:</p>
<dl>
<dd>
<pre>Package: libreadline2
Versions: 2.1-12(/var/state/apt/lists/foo_Packages),
Reverse Depends: 
 libreadlineg2,libreadline2
 libreadline2-altdev,libreadline2
Dependencies:
2.1-12 - libc5 (2 5.4.0-0) ncurses3.0 (0 (null))
Provides:
2.1-12 - 
Reverse Provides: </pre>
</dl>
<p> Thus it may be seen that libreadline2, version 2.1-12, depends on libc5 and ncurses3.0 which must be installed for libreadline2 to work. In turn, libreadlineg2 and libreadline2-altdev depend on libreadline2. If libreadline2 is installed, libc5 and ncurses3.0 (and ldso) must also be installed; libreadlineg2 and libreadline2-altdev do not have to be installed. For the specific meaning of the remainder of the output it is best to consult the apt source code.</dl>
<p> <code>stats</code></p>
<dl>
<dd>stats displays some statistics about the cache. No further arguments are expected. Statistics reported are:</p>
<dl>
<dd>&bull; Total package names is the number of package names found in the cache.</dl>
<dl>
<dd>&bull; Normal packages is the number of regular, ordinary package names; these are packages that bear a one-to-one correspondence between their names and the names used by other packages for them in dependencies. The majority of packages fall into this category.</dl>
<dl>
<dd>&bull; Pure virtual packages is the number of packages that exist only as a virtual package name; that is, packages only &quot;provide&quot; the virtual package name, and no package actually uses the name. For instance, &quot;mail-transport-agent&quot; in the Debian system is a pure virtual package; several packages provide &quot;mail-transport-agent&quot;, but there is no package named &quot;mail-transport-agent&quot;.</dl>
<dl>
<dd>&bull; Single virtual packages is the number of packages with only one package providing a particular virtual package. For example, in the Debian system, &quot;X11-text-viewer&quot; is a virtual package, but only one package, xless, provides &quot;X11-text-viewer&quot;.</dl>
<dl>
<dd>&bull; Mixed virtual packages is the number of packages that either provide a particular virtual package or have the virtual package name as the package name. For instance, in the Debian system, &quot;debconf&quot; is both an actual package, and provided by the debconf-tiny package.</dl>
<dl>
<dd>&bull; Missing is the number of package names that were referenced in a dependency but were not provided by any package. Missing packages may be an evidence if a full distribution is not accessed, or if a package (real or virtual) has been dropped from the distribution. Usually they are referenced from Conflicts or Breaks statements.</dl>
<dl>
<dd>&bull; Total distinct versions is the number of package versions found in the cache. If more than one distribution is being accessed (for instance, &quot;stable&quot; and &quot;unstable&quot;), this value can be considerably larger than the number of total package names.</dl>
<dl>
<dd>&bull; Total dependencies is the number of dependency relationships claimed by all of the packages in the cache.</dl>
<p>  <code>showsrc</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>showsrc displays all the source package records that match the given package names. All versions are shown, as well as all records that declare the name to be a binary package. Use <code>&#8211;only-source</code> to display only source package names.</dl>
<p> <code>dump</code></p>
<dl>
<dd>dump shows a short listing of every package in the cache. It is primarily for debugging.</dl>
<p> <code>dumpavail</code></p>
<dl>
<dd>dumpavail prints out an available list to stdout. This is suitable for use with <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) and is used by the <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1) method.</dl>
<p> <code>unmet</code></p>
<dl>
<dd>unmet displays a summary of all unmet dependencies in the package cache.</dl>
<p> <code>show</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>show performs a function similar to <code>dpkg &#8211;print-avail</code>; it displays the package records for the named packages.</dl>
<p> <code>search</code> <i>regex</i><code>&#8230;</code></p>
<dl>
<dd>search performs a full text search on all available package lists for the POSIX regex pattern given, see <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7). It searches the package names and the descriptions for an occurrence of the regular expression and prints out the package name and the short description, including virtual package names. If <code>&#8211;full</code> is given then output identical to show is produced for each matched package, and if <code>&#8211;names-only</code> is given then the long description is not searched, only the package name and provided packages are. Separate arguments can be used to specify multiple search patterns that are and&#8217;ed together.</dl>
<p> <code>depends</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>depends shows a listing of each dependency a package has and all the possible other packages that can fulfill that dependency.</dl>
<p> <code>rdepends</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>rdepends shows a listing of each reverse dependency a package has.</dl>
<p> <code>pkgnames</code> [<i>prefix</i>]</p>
<dl>
<dd>This command prints the name of each package APT knows. The optional argument is a prefix match to filter the name list. The output is suitable for use in a shell tab complete function and the output is generated extremely quickly. This command is best used with the <code>&#8211;generate</code> option. Note that a package which APT knows of is not necessarily available to download, installable or installed, e.g. virtual packages are also listed in the generated list.</dl>
<p> <code>dotty</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>dotty takes a list of packages on the command line and generates output suitable for use by dotty from the m[blue]<code>GraphViz</code>m[]<font SIZE="-2">[1]</font> package. The result will be a set of nodes and edges representing the relationships between the packages. By default the given packages will trace out all dependent packages; this can produce a very large graph. To limit the output to only the packages listed on the command line, set the APT::Cache::GivenOnly option. The resulting nodes will have several shapes; normal packages are boxes, pure virtual packages are triangles, mixed virtual packages are diamonds, missing packages are hexagons. Orange boxes mean recursion was stopped (leaf packages), blue lines are pre-depends, green lines are conflicts. Caution, dotty cannot graph larger sets of packages.</dl>
<p> <code>xvcg</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>The same as dotty, only for xvcg from the m[blue]<code>VCG tool</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> <code>policy</code> [<i>pkg</i>&#8230;]</p>
<dl>
<dd>policy is meant to help debug issues relating to the preferences file. With no arguments it will print out the priorities of each source. Otherwise it prints out detailed information about the priority selection of the named package.</dl>
<p> <code>madison</code> <i>pkg</i><code>&#8230;</code></p>
<dl>
<dd>apt-cache&#8217;s madison command attempts to mimic the output format and a subset of the functionality of the Debian archive management tool, madison. It displays available versions of a package in a tabular format. Unlike the original madison, it can only display information for the architecture for which APT has retrieved package lists (APT::Architecture).</dl>
<h2>Options</h2>
<p>All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>-p</code>, <code>&#8211;pkg-cache</code></p>
<dl>
<dd>Select the file to store the package cache. The package cache is the primary cache used by all operations. Configuration Item: Dir::Cache::pkgcache.</dl>
<p> <code>-s</code>, <code>&#8211;src-cache</code></p>
<dl>
<dd>Select the file to store the source cache. The source is used only by gencaches and it stores a parsed version of the package information from remote sources. When building the package cache the source cache is used to avoid reparsing all of the package files. Configuration Item: Dir::Cache::srcpkgcache.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Quiet; produces output suitable for logging, omitting progress indicators. More q&#8217;s will produce more quietness up to a maximum of 2. You can also use <code>-q=#</code> to set the quietness level, overriding the configuration file. Configuration Item: quiet.</dl>
<p> <code>-i</code>, <code>&#8211;important</code></p>
<dl>
<dd>Print only important dependencies; for use with unmet and depends. Causes only Depends and Pre-Depends relations to be printed. Configuration Item: APT::Cache::Important.</dl>
<p> <code>&#8211;no-pre-depends</code>, <code>&#8211;no-depends</code>, <code>&#8211;no-recommends</code>, <code>&#8211;no-suggests</code>, <code>&#8211;no-conflicts</code>, <code>&#8211;no-breaks</code>, <code>&#8211;no-replaces</code>, <code>&#8211;no-enhances</code></p>
<dl>
<dd>Per default the <code>depends</code> and <code>rdepends</code> print all dependencies. This can be tweaked with these flags which will omit the specified dependency type. Configuration Item: APT::Cache::Show<i>DependencyType</i> e.g. APT::Cache::ShowRecommends.</dl>
<p> <code>&#8211;implicit</code></p>
<dl>
<dd>Per default <code>depends</code> and <code>rdepends</code> print only dependencies explicitly expressed in the metadata. With this flag it will also show dependencies implicitly added based on the encountered data. A Conflicts: foo e.g. expresses implicitly that this package also conflicts with the package foo from any other architecture. Configuration Item: APT::Cache::ShowImplicit.</dl>
<p> <code>-f</code>, <code>&#8211;full</code></p>
<dl>
<dd>Print full package records when searching. Configuration Item: APT::Cache::ShowFull.</dl>
<p> <code>-a</code>, <code>&#8211;all-versions</code></p>
<dl>
<dd>Print full records for all available versions. This is the default; to turn it off, use <code>&#8211;no-all-versions</code>. If <code>&#8211;no-all-versions</code> is specified, only the candidate version will be displayed (the one which would be selected for installation). This option is only applicable to the show command. Configuration Item: APT::Cache::AllVersions.</dl>
<p> <code>-g</code>, <code>&#8211;generate</code></p>
<dl>
<dd>Perform automatic package cache regeneration, rather than use the cache as it is. This is the default; to turn it off, use <code>&#8211;no-generate</code>. Configuration Item: APT::Cache::Generate.</dl>
<p> <code>&#8211;names-only</code>, <code>-n</code></p>
<dl>
<dd>Only search on the package and provided package names, not the long descriptions. Configuration Item: APT::Cache::NamesOnly.</dl>
<p> <code>&#8211;all-names</code></p>
<dl>
<dd>Make pkgnames print all names, including virtual packages and missing dependencies. Configuration Item: APT::Cache::AllNames.</dl>
<p> <code>&#8211;recurse</code></p>
<dl>
<dd>Make depends and rdepends recursive so that all packages mentioned are printed once. Configuration Item: APT::Cache::RecurseDepends.</dl>
<p> <code>&#8211;installed</code></p>
<dl>
<dd>Limit the output of depends and rdepends to packages which are currently installed. Configuration Item: APT::Cache::Installed.</dl>
<p> <code>&#8211;with-source</code> <i>filename</i></p>
<dl>
<dd>Adds the given file as a source for metadata. Can be repeated to add multiple files. Supported are currently *.deb, *.dsc, *.changes, Sources and Packages files as well as source package directories. Files are matched based on their name only, not their content! </p>
<p> Sources and Packages can be compressed in any format apt supports as long as they have the correct extension. If you need to store multiple of these files in one directory you can prefix a name of your choice with the last character being an underscore (&quot;_&quot;). Example: my.example_Packages.xz </p>
<p> Note that these sources are treated as trusted (see <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8)). Configuration Item: APT::Sources::With.</dl>
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
<p> /var/lib/apt/lists/</p>
<dl>
<dd>Storage area for state information for each package resource specified in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) Configuration Item: Dir::State::Lists.</dl>
<p> /var/lib/apt/lists/partial/</p>
<dl>
<dd>Storage area for state information in transit. Configuration Item: Dir::State::Lists (partial will be implicitly appended)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5), <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5), <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8)</p>
<h2>Diagnostics</h2>
<p><code>apt-cache</code> returns zero on normal operation, decimal 100 on error.</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[3]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
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
<dd>GraphViz</p>
<dl>
<dd><a rel="nofollow" href="http://www.research.att.com/sw/tools/graphviz/">http://www.research.att.com/sw/tools/graphviz/</a></dl>
<dt> 2.</p>
<dd>VCG tool</p>
<dl>
<dd><a rel="nofollow" href="http://rw4.cs.uni-sb.de/users/sander/html/gsvcg1.html">http://rw4.cs.uni-sb.de/users/sander/html/gsvcg1.html</a></dl>
<dt> 3.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
