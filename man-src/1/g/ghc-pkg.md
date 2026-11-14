---
title: "ghc-pkg(1)"
name: "ghc-pkg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ghc-pkg/"
description: "ghc-pkg – GHC Haskell Cabal package manager"
---

<h2 class="name">NAME</h2>
<p> ghc-pkg &#8211; GHC Haskell Cabal package manager </p>
<h2>SYNOPSIS</h2>
<p> <code>ghc-pkg</code> <i>action</i> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> A package is a library of Haskell modules known to the compiler. The <code>ghc-pkg</code> tool allows adding or removing them from a package database. By default, the system-wide package database is modified, but alternatively the user&#8217;s local package database or another specified file can be used. </p>
<p> To make a package available for <code>ghc</code>, <code>ghc-pkg</code> can be used to register it. Unregistering it removes it from the database. Also, packages can be hidden, to make <code>ghc</code> ignore the package by default, without uninstalling it. Exposing a package makes a hidden package available. Additionally, <code>ghc-pkg</code> has various commands to query the package database. </p>
<p> Where a package name is required, the package can be named in full including the version number (e.g. <code>network-1.0</code>), or without the version number. Naming a package without the version number matches all versions of the package; the specified action will be applied to all the matching packages. A package specifier that matches all version of the package can also be written <code>pkg-*</code>, to make it clearer that multiple packages are being matched.</p>
<h2>ACTIONS</h2>
<dl>
<dt><code>register</code> <i>filename</i>|<code>&#8211;</code></p>
<dd> Register the package using the specified installed package description.</p>
<dt><code>update</code> <i>filename</i>|<code>&#8211;</code></p>
<dd> Register the package, overwriting any other package with the same name.</p>
<dt><code>unregister</code> <i>pkg-id</i></p>
<dd> Unregister the specified package.</p>
<dt><code>expose</code> <i>pkg-id</i></p>
<dd> Expose the specified package.</p>
<dt><code>hide</code> <i>pkg-id</i></p>
<dd> Hide the specified package</p>
<dt><code>list</code> [<i>pkg</i>]&#8230;</p>
<dd> List registered packages in the global database, and also the user database if <code>&#8211;user</code> is given. If a package name is given all the registered versions will be listed in ascending order. Accepts the <code>&#8211;simple-output</code> flag.</p>
<dt><code>dot</code></p>
<dd> Generate a graph of the package dependencies in a form suitable for input for the graphviz tools. For example, to generate a PDF of the dependency graph:<br />
 <code> dot tred dot -Tpdf &gt;pkgs.pdf</code></p>
<dt><code>find-module</code> <i>module</i></p>
<dd> List registered packages exposing module <i>module</i> in the global database, and also the user database if <code>&#8211;user</code> is given. All the registered versions will be listed in ascending order. Accepts the <code>&#8211;simple-output</code> flag.</p>
<dt><code>latest</code> <i>pkg-id</i></p>
<dd> Prints the highest registered version of a package.</p>
<dt><code>check</code></p>
<dd> Check the consistency of package dependencies and list broken packages. Accepts the <code>&#8211;simple-output</code> flag.</p>
<dt><code>describe</code> <i>pkg</i></p>
<dd> Give the registered description for the specified package. The description is returned in precisely the syntax required by ghc-pkg register.</p>
<dt><code>field</code> <i>pkg field</i></p>
<dd> Extract the specified field of the package description for the specified package. Accepts comma-separated multiple fields.</p>
<dt><code>dump</code></p>
<dd> Dump the registered description for every package. This is like <code>ghc-pkg describe&nbsp;<wbr>&#8216;*&#8217;</code>, expect that it is intended to be used by tools that parse the results, rather than humans.</p>
<dt><code>recache</code></p>
<dd> Regenerate the package database cache. This command should only be necessary if you added a package to the database by dropping a file into the database directory manyally. By default, the global DB is recached; to recache a different DB use <code>&#8211;user</code> or <code>&#8211;package-conf</code> as appropriate.</dl>
<h2>OPTIONS</h2>
<p> When asked to modify a database (<code>register</code>,&nbsp;<wbr><code>unregister</code>,&nbsp;<wbr><code>update</code>,&nbsp;<wbr><code>hide</code>,&nbsp;<wbr><code>expose</code>, and also&nbsp;<wbr><code>check</code>), <code>ghc-pkg</code> modifies the global database by default. Specifying <code>&#8211;user</code> causes it to act on the user database, or <code>&#8211;package-conf</code> can be used to act on another database entirely. When multiple of these options are given, the rightmost one is used as the database to act upon. </p>
<p> Commands that query the package database (<code>list</code>,&nbsp;<wbr><code>latest</code>,&nbsp;<wbr><code>describe</code>,&nbsp;<wbr><code>field</code>) operate on the list of databases specified by the flags <code>&#8211;user</code>,&nbsp;<wbr><code>&#8211;global</code>, and <code>&#8211;package-conf</code>. If none of these flags are given, the default is <code>&#8211;global &#8211;user</code>.</p>
<dl>
<dt><code>&#8211;user</code></p>
<dd> Use the current user&#8217;s package database.</p>
<dt><code>&#8211;global</code></p>
<dd> Use the global package database.</p>
<dt><code>-f</code> <i>FILE</i>, <code>&#8211;package-conf=</code><i>FILE</i></p>
<dd> Use the specified package config file.</p>
<dt><code>&#8211;global-conf=</code><i>FILE</i></p>
<dd> Location of the global package config.</p>
<dt><code>&#8211;force</code></p>
<dd> Ignore missing dependencies, directories, and libraries.</p>
<dt><code>&#8211;force-files</code></p>
<dd> Ignore missing directories and libraries only.</p>
<dt><code>-g</code>,&nbsp;<wbr><code>&#8211;auto-ghc-libs</code></p>
<dd> Automatically build libs for GHCi (with register).</p>
<dt><code>-?</code>,&nbsp;<wbr><code>&#8211;help</code></p>
<dd> Display a help message and exit.</p>
<dt><code>-V</code>,&nbsp;<wbr><code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>&#8211;simple-output</code></p>
<dd> Print output in easy-to-parse format for some commands.</p>
<dt><code>&#8211;names-only</code></p>
<dd> Only print package names, not versions; can only be used with <code>list &#8211;simple-output</code>.</p>
<dt><code>&#8211;ignore-case</code></p>
<dd> Ignore case for substring matching.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>GHC_PACKAGE_PATH</code></p>
<dd> The <code>GHC_PACKAGE_PATH</code> environment variable may be set to a <code>:</code>-separated list of files containing package databases. This list of package databases is used by <code>ghc</code> and <code>ghc-pkg</code>, with earlier databases in the list overriding later ones. This order was chosen to match the behaviour of the <code>PATH</code> environment variable; think of it as a list of package databases that are searched left-to-right for packages. </p>
<p> If <code>GHC_PACKAGE_PATH</code> ends in a separator, then the default user and system package databases are appended, in that order. e.g. to augment the usual set of packages with a database of your own, you could say: </p>
<p> <code> export GHC_PACKAGE_PATH=$HOME/.my-ghc-packages.conf:</code> </p>
<p> To check whether your <code>GHC_PACKAGE_PATH</code> setting is doing the right thing, <code>ghc-pkg list</code> will list all the databases in use, in the reverse order they are searched.</dl>
<h2>FILES</h2>
<p> Both of these locations are changed for Debian. Upstream still keeps these under <i>/usr</i>. Some programs may refer to that, but look in <i>/var</i> instead.</p>
<dl>
<dt><i>/var/lib/ghc/package.conf</i></p>
<dd> Global package.conf file.</p>
<dt><i>/var/lib/ghc/package.conf.d/</i></p>
<dd> Directory for library specific package.conf files. These are added to the global registry.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ghc/">ghc</a></code>(1), <code><a href="/docs/linux/man/1-runghc/">runghc</a></code>(1), <code><a href="/docs/linux/man/1-hugs/">hugs</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Kari Pahula &lt;kaol [at] debian.org&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>
