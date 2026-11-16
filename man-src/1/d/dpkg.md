---
title: "dpkg(1)"
name: "dpkg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg/"
description: "dpkg – package manager for Debian"
---

<h2 class="name">NAME</h2>
<p> dpkg &#8211; package manager for Debian </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg</code> [<i>option</i>&#8230;] <i>action</i></p>
<h2>WARNING</h2>
<p> This manual is intended for users wishing to understand <code>dpkg</code>&#8216;s command line options and package states in more detail than that provided by <code>dpkg &#8211;help</code>. </p>
<p> It should <i>not</i> be used by package maintainers wishing to understand how <code>dpkg</code> will install their packages. The descriptions of what <code>dpkg</code> does when installing and removing packages are particularly inadequate.</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg</code> is a medium-level tool to install, build, remove and manage Debian packages. The primary and more user-friendly front-end for <code>dpkg</code> as a <font SIZE="-1">CLI</font> (command-line interface) is <code>apt</code>(8&gt; and as a <font SIZE="-1">TUI</font> (terminal user interface) is <code>aptitude</code>(8). <code>dpkg</code> itself is controlled entirely via command line parameters, which consist of exactly one action and zero or more options. The action-parameter tells <code>dpkg</code> what to do and options control the behavior of the action in some way. </p>
<p> <code>dpkg</code> can also be used as a front-end to <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1) and <code><a href="/docs/linux/man/1-dpkg-query/">dpkg-query</a></code>(1). The list of supported actions can be found later on in the <font SIZE="-1"><code>ACTIONS</code></font> section. If any such action is encountered <code>dpkg</code> just runs <code>dpkg-deb</code> or <code>dpkg-query</code> with the parameters given to it, but no specific options are currently passed to them, to use any such option the back-ends need to be called directly.</p>
<h2>INFORMATION ABOUT PACKAGES</h2>
<p> <code>dpkg</code> maintains some usable information about available packages. The information is divided in three classes: <code>states</code>, <code>selection states</code> and <code>flags</code>. These values are intended to be changed mainly with <code>dselect</code>.</p>
<h3>Package states</h3>
<dl>
<dt><code>not-installed</code></dt>
<dd> The package is not installed on your system.</dd>
<dt><code>config-files</code></dt>
<dd> Only the configuration files or the <code>postrm</code> script and the data it needs to remove of the package exist on the system.</dd>
<dt><code>half-installed</code></dt>
<dd> The installation of the package has been started, but not completed for some reason.</dd>
<dt><code>unpacked</code></dt>
<dd> The package is unpacked, but not configured.</dd>
<dt><code>half-configured</code></dt>
<dd> The package is unpacked and configuration has been started, but not yet completed for some reason.</dd>
<dt><code>triggers-awaited</code></dt>
<dd> The package awaits trigger processing by another package.</dd>
<dt><code>triggers-pending</code></dt>
<dd> The package has been triggered.</dd>
<dt><code>installed</code></dt>
<dd> The package is correctly unpacked and configured.</dd></dl>
<h3>Package selection states</h3>
<dl>
<dt><code>install</code></dt>
<dd> The package is selected for installation.</dd>
<dt><code>hold</code></dt>
<dd> A package marked to be on <code>hold</code> is kept on the same version, that is, no automatic new installs, upgrades or removals will be performed on them, unless these actions are requested explicitly, or are permitted to be done automatically with the <code>&#8211;force-hold</code> option.</dd>
<dt><code>deinstall</code></dt>
<dd> The package is selected for deinstallation (i.e. we want to remove all files, except configuration files).</dd>
<dt><code>purge</code></dt>
<dd> The package is selected to be purged (i.e. we want to remove everything from system directories, even configuration files).</dd>
<dt><code>unknown</code></dt>
<dd> The package selection is unknown. A package that is also in a <code>not-installed</code> state, and with an <code>ok</code> flag will be forgotten in the next database store.</dd></dl>
<h3>Package flags</h3>
<dl>
<dt><code>ok</code></dt>
<dd> A package marked <code>ok</code> is in a known state, but might need further processing.</dd>
<dt><code>reinstreq</code></dt>
<dd> A package marked <code>reinstreq</code> is broken and requires reinstallation. These packages cannot be removed, unless forced with option <code>&#8211;force-remove-reinstreq</code>.</dd></dl>
<h2>ACTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;install</code> <i>package-file</i>&#8230;</dt>
<dd> Install the package. If <code>&#8211;recursive</code> or <code>-R</code> option is specified, <i>package-file</i> must refer to a directory instead. </dd>
<p> Installation consists of the following steps: </p>
<p> <code>1.</code> Extract the control files of the new package. </p>
<p> <code>2.</code> If another version of the same package was installed before the new installation, execute <i>prerm</i> script of the old package. </p>
<p> <code>3.</code> Run <i>preinst</i> script, if provided by the package. </p>
<p> <code>4.</code> Unpack the new files, and at the same time back up the old files, so that if something goes wrong, they can be restored. </p>
<p> <code>5.</code> If another version of the same package was installed before the new installation, execute the <i>postrm</i> script of the old package. Note that this script is executed after the <i>preinst</i> script of the new package, because new files are written at the same time old files are removed. </p>
<p> <code>6.</code> Configure the package. See <code>&#8211;configure</code> for detailed information about how this is done.</p>
<dt><code>&#8211;unpack</code> <i>package-file</i>&#8230;</dt>
<dd> Unpack the package, but don&#8217;t configure it. If <code>&#8211;recursive</code> or <code>-R</code> option is specified, <i>package-file</i> must refer to a directory instead.</dd>
<dt><code>&#8211;configure</code> <i>package</i>&#8230;|<code>-a</code>|<code>&#8211;pending</code></dt>
<dd> Configure a package which has been unpacked but not yet configured. If <code>-a</code> or <code>&#8211;pending</code> is given instead of <i>package</i>, all unpacked but unconfigured packages are configured. </dd>
<p> To reconfigure a package which has already been configured, try the <code><a href="/docs/linux/man/8-dpkg-reconfigure/">dpkg-reconfigure</a></code>(8) command instead. </p>
<p> Configuring consists of the following steps: </p>
<p> <code>1.</code> Unpack the conffiles, and at the same time back up the old conffiles, so that they can be restored if something goes wrong. </p>
<p> <code>2.</code> Run <i>postinst</i> script, if provided by the package.</p>
<dt><code>&#8211;triggers-only</code> <i>package</i>&#8230;|<code>-a</code>|<code>&#8211;pending</code></dt>
<dd> Processes only triggers (since dpkg 1.14.17). All pending triggers will be processed. If package names are supplied only those packages&#8217; triggers will be processed, exactly once each where necessary. Use of this option may leave packages in the improper <code>triggers-awaited</code> and <code>triggers-pending</code> states. This can be fixed later by running: <code>dpkg &#8211;configure &#8211;pending</code>.</dd>
<dt><code>-r</code>, <code>&#8211;remove</code> <i>package</i>&#8230;|<code>-a</code>|<code>&#8211;pending</code></dt>
<dd> Remove an installed package. This removes everything except conffiles and other data cleaned up by the <i>postrm</i> script, which may avoid having to reconfigure the package if it is reinstalled later (conffiles are configuration files that are listed in the <i>DEBIAN/conffiles</i> control file). If there is no <i>DEBIAN/conffiles</i> control file nor <i>DEBIAN/postrm</i> script, this command is equivalent to calling <code>&#8211;purge</code>. If <code>-a</code> or <code>&#8211;pending</code> is given instead of a package name, then all packages unpacked, but marked to be removed in file <i>/var/lib/dpkg/status</i>, are removed. </dd>
<p> Removing of a package consists of the following steps: </p>
<p> <code>1.</code> Run <i>prerm</i> script </p>
<p> <code>2.</code> Remove the installed files </p>
<p> <code>3.</code> Run <i>postrm</i> script</p>
<dt><code>-P</code>, <code>&#8211;purge</code> <i>package</i>&#8230;|<code>-a</code>|<code>&#8211;pending</code></dt>
<dd> Purge an installed or already removed package. This removes everything, including conffiles, and anything else cleaned up from <i>postrm</i>. If <code>-a</code> or <code>&#8211;pending</code> is given instead of a package name, then all packages unpacked or removed, but marked to be purged in file <i>/var/lib/dpkg/status</i>, are purged. </dd>
<p> <code>Note:</code> Some configuration files might be unknown to <code>dpkg</code> because they are created and handled separately through the configuration scripts. In that case, <code>dpkg</code> won&#8217;t remove them by itself, but the package&#8217;s <i>postrm</i> script (which is called by <code>dpkg</code>), has to take care of their removal during purge. Of course, this only applies to files in system directories, not configuration files written to individual users&#8217; home directories. </p>
<p> Purging of a package consists of the following steps: </p>
<p> <code>1.</code> Remove the package, if not already removed. See <code>&#8211;remove</code> for detailed information about how this is done. </p>
<p> <code>2.</code> Run <i>postrm</i> script.</p>
<dt><code>-V</code>, <code>&#8211;verify</code> [<i>package-name</i>&#8230;]</dt>
<dd> Verifies the integrity of <i>package-name</i> or all packages if omitted, by comparing information from the files installed by a package with the files metadata information stored in the <code>dpkg</code> database (since dpkg 1.17.2). The origin of the files metadata information in the database is the binary packages themselves. That metadata gets collected at package unpack time during the installation process. </dd>
<p> Currently the only functional check performed is an md5sum verification of the file contents against the stored value in the files database. It will only get checked if the database contains the file md5sum. To check for any missing metadata in the database, the <code>&#8211;audit</code> command can be used. </p>
<p> The output format is selectable with the <code>&#8211;verify-format</code> option, which by default uses the <code>rpm</code> format, but that might change in the future, and as such, programs parsing this command output should be explicit about the format they expect.</p>
<dt><code>-C</code>, <code>&#8211;audit</code> [<i>package-name</i>&#8230;]</dt>
<dd> Performs database sanity and consistency checks for <i>package-name</i> or all packages if omitted (per package checks since dpkg 1.17.10). For example, searches for packages that have been installed only partially on your system or that have missing, wrong or obsolete control data or files. <code>dpkg</code> will suggest what to do with them to get them fixed.</dd>
<dt><code>&#8211;update-avail</code> [<i>Packages-file</i>]</dt>
<dd>
</dd><dt><code>&#8211;merge-avail</code> [<i>Packages-file</i>]</dt>
<dd> Update <code>dpkg</code>&#8216;s and <code>dselect</code>&#8216;s idea of which packages are available. With action <code>&#8211;merge-avail</code>, old information is combined with information from <i>Packages-file</i>. With action <code>&#8211;update-avail</code>, old information is replaced with the information in the <i>Packages-file</i>. The <i>Packages-file</i> distributed with Debian is simply named &laquo;<i>Packages</i>&raquo;. If the <i>Packages-file</i> argument is missing or named &laquo;<code>&#8211;</code>&raquo; then it will be read from standard input (since dpkg 1.17.7). <code>dpkg</code> keeps its record of available packages in <i>/var/lib/dpkg/available</i>. </dd>
<p> A simpler one-shot command to retrieve and update the <i>available</i> file is <code>dselect update</code>. Note that this file is mostly useless if you don&#8217;t use <code>dselect</code> but an APT-based frontend: <font SIZE="-1">APT</font> has its own system to keep track of available packages.</p>
<dt><code>-A</code>, <code>&#8211;record-avail</code> <i>package-file</i>&#8230;</dt>
<dd> Update <code>dpkg</code> and <code>dselect</code>&#8216;s idea of which packages are available with information from the package <i>package-file</i>. If <code>&#8211;recursive</code> or <code>-R</code> option is specified, <i>package-file</i> must refer to a directory instead.</dd>
<dt><code>&#8211;forget-old-unavail</code></dt>
<dd> Now <code>obsolete</code> and a no-op as <code>dpkg</code> will automatically forget uninstalled unavailable packages (since dpkg 1.15.4), but only those that do not contain user information such as package selections.</dd>
<dt><code>&#8211;clear-avail</code></dt>
<dd> Erase the existing information about what packages are available.</dd>
<dt><code>&#8211;get-selections</code> [<i>package-name-pattern</i>&#8230;]</dt>
<dd> Get list of package selections, and write it to stdout. Without a pattern, non-installed packages (i.e. those which have been previously purged) will not be shown.</dd>
<dt><code>&#8211;set-selections</code></dt>
<dd> Set package selections using file read from stdin. This file should be in the format &#8220;<i>package</i> <i>state</i>&#8220;, where state is one of <code>install</code>, <code>hold</code>, <code>deinstall</code> or <code>purge</code>. Blank lines and comment lines beginning with &#8216;<code>#</code>&#8216; are also permitted. </dd>
<p> The <i>available</i> file needs to be up-to-date for this command to be useful, otherwise unknown packages will be ignored with a warning. See the <code>&#8211;update-avail</code> and <code>&#8211;merge-avail</code> commands for more information.</p>
<dt><code>&#8211;clear-selections</code></dt>
<dd> Set the requested state of every non-essential package to deinstall (since dpkg 1.13.18). This is intended to be used immediately before <code>&#8211;set-selections</code>, to deinstall any packages not in list given to <code>&#8211;set-selections</code>.</dd>
<dt><code>&#8211;yet-to-unpack</code></dt>
<dd> Searches for packages selected for installation, but which for some reason still haven&#8217;t been installed. </dd>
<p> <code>Note:</code> This command makes use of both the available file and the package selections.</p>
<dt><code>&#8211;predep-package</code></dt>
<dd> Print a single package which is the target of one or more relevant pre-dependencies and has itself no unsatisfied pre-dependencies. </dd>
<p> If such a package is present, output it as a Packages file entry, which can be massaged as appropriate. </p>
<p> <code>Note:</code> This command makes use of both the available file and the package selections. </p>
<p> Returns 0 when a package is printed, 1 when no suitable package is available and 2 on error.</p>
<dt><code>&#8211;add-architecture</code> <i>architecture</i></dt>
<dd> Add <i>architecture</i> to the list of architectures for which packages can be installed without using <code>&#8211;force-architecture</code> (since dpkg 1.16.2). The architecture <code>dpkg</code> is built for (i.e. the output of <code>&#8211;print-architecture</code>) is always part of that list.</dd>
<dt><code>&#8211;remove-architecture</code> <i>architecture</i></dt>
<dd> Remove <i>architecture</i> from the list of architectures for which packages can be installed without using <code>&#8211;force-architecture</code> (since dpkg 1.16.2). If the architecture is currently in use in the database then the operation will be refused, except if <code>&#8211;force-architecture</code> is specified. The architecture <code>dpkg</code> is built for (i.e. the output of <code>&#8211;print-architecture</code>) can never be removed from that list.</dd>
<dt><code>&#8211;print-architecture</code></dt>
<dd> Print architecture of packages <code>dpkg</code> installs (for example, &#8220;i386&#8221;).</dd>
<dt><code>&#8211;print-foreign-architectures</code></dt>
<dd> Print a newline-separated list of the extra architectures <code>dpkg</code> is configured to allow packages to be installed for (since dpkg 1.16.2).</dd>
<dt><code>&#8211;assert-help</code></dt>
<dd> Give help about the <code>&#8211;assert-</code><i>feature</i> options (since dpkg 1.21.0).</dd>
<dt><code>&#8211;assert-</code><i>feature</i></dt>
<dd> Asserts that <code>dpkg</code> supports the requested feature. Returns 0 if the feature is fully supported, 1 if the feature is known but <code>dpkg</code> cannot provide support for it yet, and 2 if the feature is unknown. The current list of assertable features is:</dd>
<dl>
<dl>
<dt><code>support-predepends</code></dt>
<dd> Supports the <code>Pre-Depends</code> field (since dpkg 1.1.0).</dd>
<dt><code>working-epoch</code></dt>
<dd> Supports epochs in version strings (since dpkg 1.4.0.7).</dd>
<dt><code>long-filenames</code></dt>
<dd> Supports long filenames in <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5) archives (since dpkg 1.4.1.17).</dd>
<dt><code>multi-conrep</code></dt>
<dd> Supports multiple <code>Conflicts</code> and <code>Replaces</code> (since dpkg 1.4.1.19).</dd>
<dt><code>multi-arch</code></dt>
<dd> Supports multi-arch fields and semantics (since dpkg 1.16.2).</dd>
<dt><code>versioned-provides</code></dt>
<dd> Supports versioned <code>Provides</code> (since dpkg 1.17.11).</dd>
<dt><code>protected-field</code></dt>
<dd> Supports the <code>Protected</code> field (since dpkg 1.20.1).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;validate-</code><i>thing string</i></dt>
<dd> Validate that the <i>thing</i> <i>string</i> has a correct syntax (since dpkg 1.18.16). Returns 0 if the <i>string</i> is valid, 1 if the <i>string</i> is invalid but might be accepted in lax contexts, and 2 if the <i>string</i> is invalid. The current list of validatable <i>thing</i>s is:</dd>
<dl>
<dl>
<dt><code>pkgname</code></dt>
<dd> Validates the given package name (since dpkg 1.18.16).</dd>
<dt><code>trigname</code></dt>
<dd> Validates the given trigger name (since dpkg 1.18.16).</dd>
<dt><code>archname</code></dt>
<dd> Validates the given architecture name (since dpkg 1.18.16).</dd>
<dt><code>version</code></dt>
<dd> Validates the given version (since dpkg 1.18.16).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;compare-versions</code> <i>ver1</i> <i>op</i> <i>ver2</i></dt>
<dd> Compare version numbers, where <i>op</i> is a binary operator. <code>dpkg</code> returns true (<code>0</code>) if the specified condition is satisfied, and false (<code>1</code>) otherwise. There are two groups of operators, which differ in how they treat an empty <i>ver1</i> or <i>ver2</i>. These treat an empty version as earlier than any version: <code>lt le eq ne ge gt</code>. These treat an empty version as later than any version: <code>lt-nl le-nl ge-nl gt-nl</code>. These are provided only for compatibility with control file syntax: <code>&lt; &lt;&lt; &lt;= = &gt;= &gt;&gt; &gt;</code>. The <code>&lt;</code> and <code>&gt;</code> operators are obsolete and should <code>not</code> be used, due to confusing semantics. To illustrate: <code>0.1 &lt; 0.1</code> evaluates to true.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display a brief help message.</dd>
<dt><code>&#8211;force-help</code></dt>
<dd> Give help about the <code>&#8211;force-</code><i>thing</i> options.</dd>
<dt><code>-Dh</code>, <code>&#8211;debug=help</code></dt>
<dd> Give help about debugging options.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display <code>dpkg</code> version information. </dd>
<p> When used with <code>&#8211;robot</code>, the output will be the program version number in a dotted numerical format, with no newline.</p>
<dt><code>dpkg-deb actions</code></dt>
<dd> See <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1) for more information about the following actions, and other actions and options not exposed by the <code>dpkg</code> front-end.</dd>
<dl>
<dl>
<dt><code>-b</code>, <code>&#8211;build</code> <i>directory</i> [<i>archive</i>|<i>directory</i>]</dt>
<dd> Build a deb package.</dd>
<dt><code>-c</code>, <code>&#8211;contents</code> <i>archive</i></dt>
<dd> List contents of a deb package.</dd>
<dt><code>-e</code>, <code>&#8211;control</code> <i>archive</i> [<i>directory</i>]</dt>
<dd> Extract control-information from a package.</dd>
<dt><code>-x</code>, <code>&#8211;extract</code> <i>archive directory</i></dt>
<dd> Extract the files contained by package.</dd>
<dt><code>-X</code>, <code>&#8211;vextract</code> <i>archive directory</i></dt>
<dd> Extract and display the filenames contained by a package.</dd>
<dt><code>-f</code>, <code>&#8211;field</code> <i>archive</i> [<i>control-field</i>&#8230;]</dt>
<dd> Display control field(s) of a package.</dd>
<dt><code>&#8211;ctrl-tarfile</code> <i>archive</i></dt>
<dd> Output the control tar-file contained in a Debian package.</dd>
<dt><code>&#8211;fsys-tarfile</code> <i>archive</i></dt>
<dd> Output the filesystem tar-file contained by a Debian package.</dd>
<dt><code>-I</code>, <code>&#8211;info</code> <i>archive</i> [<i>control-file</i>&#8230;]</dt>
<dd> Show information about a package.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>dpkg-query actions</code></dt>
<dd> See <code><a href="/docs/linux/man/1-dpkg-query/">dpkg-query</a></code>(1) for more information about the following actions, and other actions and options not exposed by the <code>dpkg</code> front-end.</dd>
<dl>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code> <i>package-name-pattern</i>&#8230;</dt>
<dd> List packages matching given pattern.</dd>
<dt><code>-s</code>, <code>&#8211;status</code> <i>package-name</i>&#8230;</dt>
<dd> Report status of specified package.</dd>
<dt><code>-L</code>, <code>&#8211;listfiles</code> <i>package-name</i>&#8230;</dt>
<dd> List files installed to your system from <i>package-name</i>.</dd>
<dt><code>-S</code>, <code>&#8211;search</code> <i>filename-search-pattern</i>&#8230;</dt>
<dd> Search for a filename from installed packages.</dd>
<dt><code>-p</code>, <code>&#8211;print-avail</code> <i>package-name</i>&#8230;</dt>
<dd> Display details about <i>package-name</i>, as found in <i>/var/lib/dpkg/available</i>. Users of APT-based frontends should use <code>apt show</code> <i>package-name</i> instead.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>OPTIONS</h2>
<p> All options can be specified both on the command line and in the <code>dpkg</code> configuration file <i>/etc/dpkg/dpkg.cfg</i> or fragment files (with names matching this shell pattern &#8216;[0-9a-zA-Z_-]*&#8217;) on the configuration directory <i>/etc/dpkg/dpkg.cfg.d/</i>. Each line in the configuration file is either an option (exactly the same as the command line option but without leading hyphens) or a comment (if it starts with a &#8216;<code>#</code>&#8216;).</p>
<dl>
<dt><code>&#8211;abort-after=</code><i>number</i></dt>
<dd> Change after how many errors <code>dpkg</code> will abort. The default is 50.</dd>
<dt><code>-B</code>, <code>&#8211;auto-deconfigure</code></dt>
<dd> When a package is removed, there is a possibility that another installed package depended on the removed package. Specifying this option will cause automatic deconfiguration of the package which depended on the removed package.</dd>
<dt><code>-D</code><i>octal</i>, <code>&#8211;debug=</code><i>octal</i></dt>
<dd> Switch debugging on. <i>octal</i> is formed by bitwise-ORing desired values together from the list below (note that these values may change in future releases). <code>-Dh</code> or <code>&#8211;debug=help</code> display these debugging values. </dd>
<pre><code>
    Number   Description
         1   Generally helpful progress information
         2   Invocation and status of maintainer scripts
        10   Output for each file processed
       100   Lots of output for each file processed
        20   Output for each configuration file
       200   Lots of output for each configuration file
        40   Dependencies and conflicts
       400   Lots of dependencies/conflicts output
     10000   Trigger activation and processing
     20000   Lots of output regarding triggers
     40000   Silly amounts of output regarding triggers
      1000   Lots of drivel about e.g. the dpkg/info dir
      2000   Insane amounts of drivel
</code></pre>
<dt><code>&#8211;force-</code><i>things</i></dt>
<dd>
</dd><dt><code>&#8211;no-force-</code><i>things</i>, <code>&#8211;refuse-</code><i>things</i></dt>
<dd> Force or refuse (<code>no-force</code> and <code>refuse</code> mean the same thing) to do some things. <i>things</i> is a comma separated list of things specified below. <code>&#8211;force-help</code> displays a message describing them. Things marked with (*) are forced by default. </dd>
<p> <i>Warning: These options are mostly intended to be used by experts only. Using them without fully understanding their effects may break your whole system.</i> </p>
<p> <code>all</code>: Turns on (or off) all force options. </p>
<p> <code>downgrade</code>(*): Install a package, even if newer version of it is already installed. </p>
<p> <i>Warning: At present</i> <code>dpkg</code> <i>does not do any dependency checking on downgrades and therefore will not warn you if the downgrade breaks the dependency of some other package. This can have serious side effects, downgrading essential system components can even make your whole system unusable. Use with care.</i> </p>
<p> <code>configure-any</code>: Configure also any unpacked but unconfigured packages on which the current package depends. </p>
<p> <code>hold</code>: Allow automatic installs, upgrades or removals of packages even when marked to be on &#8220;hold&#8221;. <code>Note:</code> This does not prevent these actions when requested explicitly. </p>
<p> <code>remove-reinstreq</code>: Remove a package, even if it&#8217;s broken and marked to require reinstallation. This may, for example, cause parts of the package to remain on the system, which will then be forgotten by <code>dpkg</code>. </p>
<p> <code>remove-protected</code>: Remove, even if the package is considered protected (since dpkg 1.20.1). Protected packages contain mostly important system boot infrastructure. Removing them might cause the whole system to be unable to boot, so use with caution. </p>
<p> <code>remove-essential</code>: Remove, even if the package is considered essential. Essential packages contain mostly very basic Unix commands. Removing them might cause the whole system to stop working, so use with caution. </p>
<p> <code>depends</code>: Turn all dependency problems into warnings. This affects the <code>Pre-Depends</code> and <code>Depends</code> fields. </p>
<p> <code>depends-version</code>: Don&#8217;t care about versions when checking dependencies. This affects the <code>Pre-Depends</code> and <code>Depends</code> fields. </p>
<p> <code>breaks</code>: Install, even if this would break another package (since dpkg 1.14.6). This affects the <code>Breaks</code> field. </p>
<p> <code>conflicts</code>: Install, even if it conflicts with another package. This is dangerous, for it will usually cause overwriting of some files. This affects the <code>Conflicts</code> field. </p>
<p> <code>confmiss</code>: Always install the missing conffile without prompting. This is dangerous, since it means not preserving a change (removing) made to the file. </p>
<p> <code>confnew</code>: If a conffile has been modified and the version in the package did change, always install the new version without prompting, unless the <code>&#8211;force-confdef</code> is also specified, in which case the default action is preferred. </p>
<p> <code>confold</code>: If a conffile has been modified and the version in the package did change, always keep the old version without prompting, unless the <code>&#8211;force-confdef</code> is also specified, in which case the default action is preferred. </p>
<p> <code>confdef</code>: If a conffile has been modified and the version in the package did change, always choose the default action without prompting. If there is no default action it will stop to ask the user unless <code>&#8211;force-confnew</code> or <code>&#8211;force-confold</code> is also been given, in which case it will use that to decide the final action. </p>
<p> <code>confask</code>: If a conffile has been modified always offer to replace it with the version in the package, even if the version in the package did not change (since dpkg 1.15.8). If any of <code>&#8211;force-confnew</code>, <code>&#8211;force-confold</code>, or <code>&#8211;force-confdef</code> is also given, it will be used to decide the final action. </p>
<p> <code>overwrite</code>: Overwrite one package&#8217;s file with another&#8217;s file. </p>
<p> <code>overwrite-dir</code>: Overwrite one package&#8217;s directory with another&#8217;s file. </p>
<p> <code>overwrite-diverted</code>: Overwrite a diverted file with an undiverted version. </p>
<p> <code>statoverride-add</code>: Overwrite an existing stat override when adding it (since dpkg 1.19.5). </p>
<p> <code>statoverride-remove</code>: Ignore a missing stat override when removing it (since dpkg 1.19.5). </p>
<p> <code>security-mac</code>(*): Use platform-specific Mandatory Access Controls (<font SIZE="-1">MAC</font>) based security when installing files into the filesystem (since dpkg 1.19.5). On Linux systems the implementation uses SELinux. </p>
<p> <code>unsafe-io</code>: Do not perform safe I/O operations when unpacking (since dpkg 1.15.8.6). Currently this implies not performing file system syncs before file renames, which is known to cause substantial performance degradation on some file systems, unfortunately the ones that require the safe I/O on the first place due to their unreliable behaviour causing zero-length files on abrupt system crashes. </p>
<p> <i>Note</i>: For ext4, the main offender, consider using instead the mount option <code>nodelalloc</code>, which will fix both the performance degradation and the data safety issues, the latter by making the file system not produce zero-length files on abrupt system crashes with any software not doing syncs before atomic renames. </p>
<p> <i>Warning: Using this option might improve performance at the cost of losing data, use with care.</i> </p>
<p> <code>script-chrootless</code>: Run maintainer scripts without <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2)ing into <code>instdir</code> even if the package does not support this mode of operation (since dpkg 1.18.5). </p>
<p> <i>Warning: This can destroy your host system, use with extreme care.</i> </p>
<p> <code>architecture</code>: Process even packages with wrong or no architecture. </p>
<p> <code>bad-version</code>: Process even packages with wrong versions (since dpkg 1.16.1). </p>
<p> <code>bad-path</code>: <font SIZE="-1"><code>PATH</code></font> is missing important programs, so problems are likely. </p>
<p> <code>not-root</code>: Try to (de)install things even when not root. </p>
<p> <code>bad-verify</code>: Install a package even if it fails authenticity check.</p>
<dt><code>&#8211;ignore-depends</code>=<i>package</i>,&#8230;</dt>
<dd> Ignore dependency-checking for specified packages (actually, checking is performed, but only warnings about conflicts are given, nothing else). This affects the <code>Pre-Depends</code>, <code>Depends</code> and <code>Breaks</code> fields.</dd>
<dt><code>&#8211;no-act</code>, <code>&#8211;dry-run</code>, <code>&#8211;simulate</code></dt>
<dd> Do everything which is supposed to be done, but don&#8217;t write any changes. This is used to see what would happen with the specified action, without actually modifying anything. </dd>
<p> Be sure to give <code>&#8211;no-act</code> before the action-parameter, or you might end up with undesirable results. (e.g. <code>dpkg &#8211;purge foo &#8211;no-act</code> will first purge package &#8220;foo&#8221; and then try to purge package &#8220;&#8211;no-act&#8221;, even though you probably expected it to actually do nothing).</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></dt>
<dd> Recursively handle all regular files matching pattern <code>*.deb</code> found at specified directories and all of its subdirectories. This can be used with <code>-i</code>, <code>-A</code>, <code>&#8211;install</code>, <code>&#8211;unpack</code> and <code>&#8211;record-avail</code> actions.</dd>
<dt><code>-G</code></dt>
<dd> Don&#8217;t install a package if a newer version of the same package is already installed. This is an alias of <code>&#8211;refuse-downgrade</code>.</dd>
<dt><code>&#8211;admindir=</code><i>dir</i></dt>
<dd> Set the administrative directory to <i>directory</i>. This directory contains many files that give information about status of installed or uninstalled packages, etc. Defaults to &laquo;<i>/var/lib/dpkg</i>&raquo;.</dd>
<dt><code>&#8211;instdir=</code><i>dir</i></dt>
<dd> Set the installation directory, which refers to the directory where packages are to be installed. <code>instdir</code> is also the directory passed to <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) before running package&#8217;s installation scripts, which means that the scripts see <code>instdir</code> as a root directory. Defaults to &laquo;<i>/</i>&raquo;.</dd>
<dt><code>&#8211;root=</code><i>dir</i></dt>
<dd> Set the root directory to <code>directory</code>, which sets the installation directory to &laquo;<i>dir</i>&raquo; and the administrative directory to &laquo;<i>dir</i><code>/var/lib/dpkg</code>&raquo;.</dd>
<dt><code>-O</code>, <code>&#8211;selected-only</code></dt>
<dd> Only process the packages that are selected for installation. The actual marking is done with <code>dselect</code> or by <code>dpkg</code>, when it handles packages. For example, when a package is removed, it will be marked selected for deinstallation.</dd>
<dt><code>-E</code>, <code>&#8211;skip-same-version</code></dt>
<dd> Don&#8217;t install the package if the same version of the package is already installed.</dd>
<dt><code>&#8211;pre-invoke=</code><i>command</i></dt>
<dd>
</dd><dt><code>&#8211;post-invoke=</code><i>command</i></dt>
<dd> Set an invoke hook <i>command</i> to be run via &#8220;sh -c&#8221; before or after the <code>dpkg</code> run for the <i>unpack</i>, <i>configure</i>, <i>install</i>, <i>triggers-only</i>, <i>remove</i>, <i>purge</i>, <i>add-architecture</i> and <i>remove-architecture</i> <code>dpkg</code> actions (since dpkg 1.15.4; <i>add-architecture</i> and <i>remove-architecture</i> actions since dpkg 1.17.19). This option can be specified multiple times. The order the options are specified is preserved, with the ones from the configuration files taking precedence. The environment variable <font SIZE="-1"><code>DPKG_HOOK_ACTION</code></font> is set for the hooks to the current <code>dpkg</code> action. </dd>
<p> <code>Note:</code> Front-ends might call <code>dpkg</code> several times per invocation, which might run the hooks more times than expected.</p>
<dt><code>&#8211;path-exclude=</code><i>glob-pattern</i></dt>
<dd>
</dd><dt><code>&#8211;path-include=</code><i>glob-pattern</i></dt>
<dd> Set <i>glob-pattern</i> as a path filter, either by excluding or re-including previously excluded paths matching the specified patterns during install (since dpkg 1.15.8). </dd>
<p> <i>Warning: Take into account that depending on the excluded paths you might completely break your system, use with caution.</i> </p>
<p> The glob patterns use the same wildcards used in the shell, were &#8216;*&#8217; matches any sequence of characters, including the empty string and also &#8216;/&#8217;. For example, &laquo;<i>/usr/*/READ*</i>&raquo; matches &laquo;<i>/usr/share/doc/package/README</i>&raquo;. As usual, &#8216;?&#8217; matches any single character (again, including &#8216;/&#8217;). And &#8216;[&#8216; starts a character class, which can contain a list of characters, ranges and complementations. See <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) for detailed information about globbing. <code>Note:</code> The current implementation might re-include more directories and symlinks than needed, in particular when there is a more specific re-inclusion, to be on the safe side and avoid possible unpack failures; future work might fix this. </p>
<p> This can be used to remove all paths except some particular ones; a typical case is: </p>
<pre>
 --path-exclude=/usr/share/doc/*
 --path-include=/usr/share/doc/*/copyright
</pre>
<p> to remove all documentation files except the copyright files. </p>
<p> These two options can be specified multiple times, and interleaved with each other. Both are processed in the given order, with the last rule that matches a file name making the decision. </p>
<p> The filters are applied when unpacking the binary packages, and as such only have knowledge of the type of object currently being filtered (e.g. a normal file or a directory) and have not visibility of what objects will come next. Because these filters have side effects (in contrast to <code><a href="/docs/linux/man/1-find/">find</a></code>(1) filters), excluding an exact pathname that happens to be a directory object like <i>/usr/share/doc</i> will not have the desired result, and only that pathname will be excluded (which could be automatically reincluded if the code sees the need). Any subsequent files contained within that directory will fail to unpack. </p>
<p> Hint: make sure the globs are not expanded by your shell.</p>
<dt><code>&#8211;verify-format</code> <i>format-name</i></dt>
<dd> Sets the output format for the <code>&#8211;verify</code> command (since dpkg 1.17.2). </dd>
<p> The only currently supported output format is <code>rpm</code>, which consists of a line for every path that failed any check. These lines have the following format: </p>
<p>&nbsp;<code>missing&nbsp;<wbr>&nbsp;</code>&nbsp;[<code>c</code>]&nbsp;<i>pathname</i>&nbsp;[<code>(</code><i>error-message</i><code>)</code>]<br />
&nbsp;<code>??5??????</code>&nbsp;[<code>c</code>]&nbsp;<i>pathname</i> </p>
<p> The first 9 characters are used to report the checks result, either a literal <code>missing</code> when the file is not present or its metadata cannot be fetched, or one of the following special characters that report the result for each check:</p>
<dl>
<dl>
<dt>&#8216;<code>?</code>&#8216;</dt>
<dd> Implies the check could not be done (lack of support, file permissions, etc).</dd>
<dt>&#8216;<code>.</code>&#8216;</dt>
<dd> Implies the check passed.</dd>
<dt>&#8216;<i>A-Za-z0-9</i>&#8216;</dt>
<dd> Implies a specific check failed. The following positions and alphanumeric characters are currently supported:</dd>
<dl>
<dl>
<dt>1 &#8216;<code>?</code>&#8216;</dt>
<dd> These checks are currently not supported, will always be &#8216;<code>?</code>&#8216;.</dd>
<dt>2 &#8216;<code>M</code>&#8216;</dt>
<dd> The file mode check failed (since dpkg 1.21.0). Because pathname metadata is currently not tracked, this check can only be partially emulated via a very simple heuristic for pathnames that have a known digest, which implies they should be regular files, where the check will fail if the pathname is not a regular file on the filesystem. This check will currently never succeed as it does not have enough information available.</dd>
<dt>3 &#8216;<code>5</code>&#8216;</dt>
<dd> The digest check failed, which means the file contents have changed.</dd>
<dt>4-9 &#8216;<code>?</code>&#8216;</dt>
<dd> These checks are currently not supported, will always be &#8216;<code>?</code>&#8216;.</dd></dl>
</dl>
<dl>
</dl>
</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The line is followed by a space and an attribute character. The following attribute character is supported:</p>
</dd><dl>
<dt>&#8216;<code>c</code>&#8216;</dt>
<dd> The pathname is a conffile.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Finally followed by another space and the pathname. </p>
<p> In case the entry was of the <code>missing</code> type, and the file was not actually present on the filesystem, then the line is followed by a space and the error message enclosed within parenthesis.</dd></dl>
<dt><code>&#8211;status-fd</code> <i>n</i></dt>
<dd> Send machine-readable package status and progress information to file descriptor <i>n</i>. This option can be specified multiple times. The information is generally one record per line, in one of the following forms:</dd>
<dl>
<dl>
<dt><code>status:</code> <i>package</i><code>:</code> <i>status</i></dt>
<dd> Package status changed; <i>status</i> is as in the status file.</dd>
<dt><code>status:</code> <i>package</i> <code>: error :</code> <i>extended-error-message</i></dt>
<dd> An error occurred. Any possible newlines in <i>extended-error-message</i> will be converted to spaces before output.</dd>
<dt><code>status:</code> <i>file</i> <code>: conffile-prompt : &#8216;</code><i>real-old</i><code>&#8216; &#8216;</code><i>real-new</i><code>&#8216;</code> <i>useredited</i> <i>distedited</i></dt>
<dd> User is being asked a conffile question.</dd>
<dt><code>processing:</code> <i>stage</i><code>:</code> <i>package</i></dt>
<dd> Sent just before a processing stage starts. <i>stage</i> is one of <code>upgrade</code>, <code>install</code> (both sent before unpacking), <code>configure</code>, <code>trigproc</code>, <code>disappear</code>, <code>remove</code>, <code>purge</code>.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;status-logger</code>=<i>command</i></dt>
<dd> Send machine-readable package status and progress information to the shell <i>command</i>&#8216;s standard input, to be run via &#8220;sh -c&#8221; (since dpkg 1.16.0). This option can be specified multiple times. The output format used is the same as in <code>&#8211;status-fd</code>.</dd>
<dt><code>&#8211;log=</code><i>filename</i></dt>
<dd> Log status change updates and actions to <i>filename</i>, instead of the default <i>/var/log/dpkg.log</i>. If this option is given multiple times, the last filename is used. Log messages are of the form:</dd>
<dl>
<dl>
<dt>YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font> <code>startup</code> <i>type</i> <i>command</i></dt>
<dd> For each dpkg invocation where <i>type</i> is <code>archives</code> (with a <i>command</i> of <code>unpack</code> or <code>install</code>) or <code>packages</code> (with a <i>command</i> of <code>configure</code>, <code>triggers-only</code>, <code>remove</code> or <code>purge</code>).</dd>
<dt>YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font> <code>status</code> <i>state</i> <i>pkg</i> <i>installed-version</i></dt>
<dd> For status change updates.</dd>
<dt>YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font> <i>action</i> <i>pkg</i> <i>installed-version</i> <i>available-version</i></dt>
<dd> For actions where <i>action</i> is one of <code>install</code>, <code>upgrade</code>, <code>configure</code>, <code>trigproc</code>, <code>disappear</code>, <code>remove</code> or <code>purge</code>.</dd>
<dt>YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font> <code>conffile</code> <i>filename</i> <i>decision</i></dt>
<dd> For conffile changes where <i>decision</i> is either <code>install</code> or <code>keep</code>.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;robot</code></dt>
<dd> Use a machine-readable output format. This provides an interface for programs that need to parse the output of some of the commands that do not otherwise emit a machine-readable output format. No localization will be used, and the output will be modified to make it easier to parse. </dd>
<p> The only currently supported command is <code>&#8211;version</code>.</p>
<dt><code>&#8211;no-pager</code></dt>
<dd> Disables the use of any pager when showing information (since dpkg 1.19.2).</dd>
<dt><code>&#8211;no-debsig</code></dt>
<dd> Do not try to verify package signatures.</dd>
<dt><code>&#8211;no-triggers</code></dt>
<dd> Do not run any triggers in this run (since dpkg 1.14.17), but activations will still be recorded. If used with <code>&#8211;configure</code> <i>package</i> or <code>&#8211;triggers-only</code> <i>package</i> then the named package postinst will still be run even if only a triggers run is needed. Use of this option may leave packages in the improper <code>triggers-awaited</code> and <code>triggers-pending</code> states. This can be fixed later by running: <code>dpkg &#8211;configure &#8211;pending</code>.</dd>
<dt><code>&#8211;triggers</code></dt>
<dd> Cancels a previous <code>&#8211;no-triggers</code> (since dpkg 1.14.17).</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> The requested action was successfully performed. Or a check or assertion command returned true.</dd>
<dt><code>1</code></dt>
<dd> A check or assertion command returned false.</dd>
<dt><code>2</code></dt>
<dd> Fatal or unrecoverable error due to invalid command-line usage, or interactions with the system, such as accesses to the database, memory allocations, etc.</dd></dl>
<h2>ENVIRONMENT</h2>
<h3>External environment</h3>
<dl>
<dt><font SIZE="-1"><code>PATH</code></font></dt>
<dd> This variable is expected to be defined in the environment and point to the system paths where several required programs are to be found. If it&#8217;s not set or the programs are not found, <code>dpkg</code> will abort.</dd>
<dt><font SIZE="-1"><code>HOME</code></font></dt>
<dd> If set, <code>dpkg</code> will use it as the directory from which to read the user specific configuration file.</dd>
<dt><font SIZE="-1"><code>TMPDIR</code></font></dt>
<dd> If set, <code>dpkg</code> will use it as the directory in which to create temporary files and directories.</dd>
<dt><font SIZE="-1"><code>SHELL</code></font></dt>
<dd> The program <code>dpkg</code> will execute when starting a new interactive shell, or when spawning a command via a shell.</dd>
<dt><font SIZE="-1"><code>PAGER</code></font></dt>
<dd>
</dd><dt><font SIZE="-1"><code>DPKG_PAGER</code></font></dt>
<dd> The program <code>dpkg</code> will execute when running a pager, which will be executed with &laquo;$SHELL<code> -c</code>&raquo;, for example when displaying the conffile differences. If <font SIZE="-1"><code>SHELL</code></font> is not set, &laquo;<code>sh</code>&raquo; will be used instead. The <font SIZE="-1"><code>DPKG_PAGER</code></font> overrides the <font SIZE="-1"><code>PAGER</code></font> environment variable (since dpkg 1.19.2).</dd>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></dt>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dd>
<dt><font SIZE="-1"><code>DPKG_FORCE</code></font></dt>
<dd> Sets the force flags (since dpkg 1.19.5). When this variable is present, no built-in force defaults will be applied. If the variable is present but empty, all force flags will be disabled.</dd>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></dt>
<dd> If set and the <code>&#8211;admindir</code> or <code>&#8211;root</code> options have not been specified, it will be used as the <code>dpkg</code> administrative directory (since dpkg 1.20.0).</dd>
<dt><font SIZE="-1"><code>DPKG_FRONTEND_LOCKED</code></font></dt>
<dd> Set by a package manager frontend to notify dpkg that it should not acquire the frontend lock (since dpkg 1.19.1).</dd></dl>
<h3>Internal environment</h3>
<dl>
<dt><font SIZE="-1"><code>LESS</code></font></dt>
<dd> Defined by <code>dpkg</code> to &#8220;<code>-FRSXMQ</code>&#8220;, if not already set, when spawning a pager (since dpkg 1.19.2). To change the default behavior, this variable can be preset to some other value including an empty string, or the <font SIZE="-1"><code>PAGER</code></font> or <font SIZE="-1"><code>DPKG_PAGER</code></font> variables can be set to disable specific options with &laquo;<code>-+</code>&raquo;, for example <code>DPKG_PAGER=&#8220;less -+F&#8221;</code>.</dd>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to indicate which installation to act on (since dpkg 1.18.5). The value is intended to be prepended to any path maintainer scripts operate on. During normal operation, this variable is empty. When installing packages into a different <code>instdir</code>, <code>dpkg</code> normally invokes maintainer scripts using <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) and leaves this variable empty, but if <code>&#8211;force-script-chrootless</code> is specified then the <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) call is skipped and <code>instdir</code> is non-empty.</dd>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to indicate the <code>dpkg</code> administrative directory to use (since dpkg 1.16.0). This variable is always set to the current <code>&#8211;admindir</code> value.</dd>
<dt><font SIZE="-1"><code>DPKG_FORCE</code></font></dt>
<dd> Defined by <code>dpkg</code> on the subprocesses environment to all the currently enabled force option names separated by commas (since dpkg 1.19.5).</dd>
<dt><font SIZE="-1"><code>DPKG_SHELL_REASON</code></font></dt>
<dd> Defined by <code>dpkg</code> on the shell spawned on the conffile prompt to examine the situation (since dpkg 1.15.6). Current valid value: <code>conffile-prompt</code>.</dd>
<dt><font SIZE="-1"><code>DPKG_CONFFILE_OLD</code></font></dt>
<dd> Defined by <code>dpkg</code> on the shell spawned on the conffile prompt to examine the situation (since dpkg 1.15.6). Contains the path to the old conffile.</dd>
<dt><font SIZE="-1"><code>DPKG_CONFFILE_NEW</code></font></dt>
<dd> Defined by <code>dpkg</code> on the shell spawned on the conffile prompt to examine the situation (since dpkg 1.15.6). Contains the path to the new conffile.</dd>
<dt><font SIZE="-1"><code>DPKG_HOOK_ACTION</code></font></dt>
<dd> Defined by <code>dpkg</code> on the shell spawned when executing a hook action (since dpkg 1.15.4). Contains the current <code>dpkg</code> action.</dd>
<dt><font SIZE="-1"><code>DPKG_RUNNING_VERSION</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to the version of the currently running <code>dpkg</code> instance (since dpkg 1.14.17).</dd>
<dt><font SIZE="-1"><code>DPKG_MAINTSCRIPT_PACKAGE</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to the (non-arch-qualified) package name being handled (since dpkg 1.14.17).</dd>
<dt><font SIZE="-1"><code>DPKG_MAINTSCRIPT_PACKAGE_REFCOUNT</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to the package reference count, i.e. the number of package instances with a state greater than <code>not-installed</code> (since dpkg 1.17.2).</dd>
<dt><font SIZE="-1"><code>DPKG_MAINTSCRIPT_ARCH</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to the architecture the package got built for (since dpkg 1.15.4).</dd>
<dt><font SIZE="-1"><code>DPKG_MAINTSCRIPT_NAME</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to the name of the script running, one of <code>preinst</code>, <code>postinst</code>, <code>prerm</code> or <code>postrm</code> (since dpkg 1.15.7).</dd>
<dt><font SIZE="-1"><code>DPKG_MAINTSCRIPT_DEBUG</code></font></dt>
<dd> Defined by <code>dpkg</code> on the maintainer script environment to a value (&#8216;<code>0</code>&#8216; or &#8216;<code>1</code>&#8216;) noting whether debugging has been requested (with the <code>&#8211;debug</code> option) for the maintainer scripts (since dpkg 1.18.4).</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dpkg/dpkg.cfg.d/[0-9a-zA-Z_-]*</i></dt>
<dd> Configuration fragment files (since dpkg 1.15.4).</dd>
<dt><i>/etc/dpkg/dpkg.cfg</i></dt>
<dd> Configuration file with default options.</dd>
<dt><i>/var/log/dpkg.log</i></dt>
<dd> Default log file (see <i>/etc/dpkg/dpkg.cfg</i> and option <code>&#8211;log</code>).</dd></dl>
<p> The other files listed below are in their default directories, see option <code>&#8211;admindir</code> to see how to change locations of these files.</p>
<dl>
<dt><i>/var/lib/dpkg/available</i></dt>
<dd> List of available packages.</dd>
<dt><i>/var/lib/dpkg/status</i></dt>
<dd> Statuses of available packages. This file contains information about whether a package is marked for removing or not, whether it is installed or not, etc. See section <font SIZE="-1"><code>INFORMATION ABOUT PACKAGES</code></font> for more info. </dd>
<p> The status file is backed up daily in <i>/var/backups</i>. It can be useful if it&#8217;s lost or corrupted due to filesystems troubles.</dl>
<p> The format and contents of a binary package are described in <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5).</p>
<h2>BUGS</h2>
<p> <code>&#8211;no-act</code> usually gives less information than might be helpful.</p>
<h2>EXAMPLES</h2>
<p> To list installed packages related to the editor <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) (note that <code>dpkg-query</code> does not load the <i>available</i> file anymore by default, and the <code>dpkg-query</code> <code>&#8211;load-avail</code> option should be used instead for that): </p>
<pre>
 dpkg -l '*vi*'
</pre>
<p> To see the entries in <i>/var/lib/dpkg/available</i> of two packages: </p>
<pre>
 dpkg --print-avail elvis vim | less
</pre>
<p> To search the listing of packages yourself: </p>
<pre>
 less /var/lib/dpkg/available
</pre>
<p> To remove an installed elvis package: </p>
<pre>
 dpkg -r elvis
</pre>
<p> To install a package, you first need to find it in an archive or <font SIZE="-1">CDROM.</font> The <i>available</i> file shows that the vim package is in section <code>editors</code>: </p>
<pre>
 cd /media/cdrom/pool/main/v/vim
 dpkg -i vim_4.5-3.deb
</pre>
<p> To make a local copy of the package selection states: </p>
<pre>
 dpkg --get-selections&gt; myselections
</pre>
<p> You might transfer this file to another computer, and after having updated the <i>available</i> file there with your package manager frontend of choice (see &lt;<a rel="nofollow" href="https://wiki.debian.org/Teams/Dpkg/FAQ">https://wiki.debian.org/Teams/Dpkg/FAQ</a>&gt; for more details), for example: </p>
<pre>
 apt-cache dumpavail | dpkg --merge-avail
</pre>
<p> or with dpkg 1.17.6 and earlier: </p>
<pre>
 avail=$(mktemp)
 apt-cache dumpavail&gt; &quot;$avail&quot;
 dpkg --merge-avail &quot;$avail&quot;
 rm &quot;$avail&quot;
</pre>
<p> you can install it with: </p>
<pre>
 dpkg --clear-selections
 dpkg --set-selections &lt;myselections
</pre>
<p> Note that this will not actually install or remove anything, but just set the selection state on the requested packages. You will need some other application to actually download and install the requested packages. For example, run <code>apt-get dselect-upgrade</code>. </p>
<p> Ordinarily, you will find that <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1) provides a more convenient way to modify the package selection states.</p>
<h2>ADDITIONAL FUNCTIONALITY</h2>
<p> Additional functionality can be gained by installing any of the following packages: <code>apt</code>, <code>aptitude</code> and <code>debsums</code>.</p>
<h2>SEE ALSO</h2>
<p> <code>aptitude</code>(8), <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8), <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-query/">dpkg-query</a></code>(1), <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5), <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5), <code><a href="/docs/linux/man/5-dpkg-cfg/">dpkg.cfg</a></code>(5), and <code><a href="/docs/linux/man/8-dpkg-reconfigure/">dpkg-reconfigure</a></code>(8).</p>
<h2>AUTHORS</h2>
<p> See <i>/usr/share/doc/dpkg/THANKS</i> for the list of people who have contributed to <code>dpkg</code>. </p>
<h2>Index</h2>
</p>