---
title: "apt-mark(8)"
name: "apt-mark"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-mark/"
description: "apt-mark – show, set and unset various settings for a package"
---

<p>apt-mark &#8211; show, set and unset various settings for a package</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>apt-mark</code> {<code>-f=</code><i>filename</i> | {auto | manual}&nbsp;<i>pkg</i>&#8230; | {showauto | showmanual}&nbsp;[<i>pkg</i>&#8230;] } | {-v | &#8211;version} | {-h | &#8211;help}</p>
<dt> <code>apt-mark</code> {hold | unhold | install | remove | purge}&nbsp;<i>pkg</i>&#8230; | {showhold | showinstall | showremove | showpurge}&nbsp;[<i>pkg</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>apt-mark</code></p>
<dd>can be used as a unified front-end to set various settings for a package, such as marking a package as being automatically/manually installed or changing <code>dpkg</code> selections such as hold, install, deinstall and purge which are respected e.g. by <code>apt-get dselect-upgrade</code> or <code>aptitude</code>.</p>
<h2>Automatically And Manually Installed Packages</h2>
<p>When you request that a package is installed, and as a result other packages are installed to satisfy its dependencies, the dependencies are marked as being automatically installed, while the package you installed explicitly is marked as manually installed. Once an automatically installed package is no longer depended on by any manually installed package it is considered no longer needed and e.g. <code>apt-get</code> or <code>aptitude</code> will at least suggest removing them. </p>
<p> <code>auto</code></p>
<dl>
<dd>auto is used to mark a package as being automatically installed, which will cause the package to be removed when no more manually installed packages depend on this package.</dl>
<p> <code>manual</code></p>
<dl>
<dd>manual is used to mark a package as being manually installed, which will prevent the package from being automatically removed if no other packages depend on it.</dl>
<p> <code>minimize-manual</code></p>
<dl>
<dd>minimize-manual is used to mark (transitive) dependencies of metapackages as automatically installed. This can be used after an installation for example, to minimize the number of manually installed packages; or continuously on systems managed by system configuration metapackages.</dl>
<p> <code>showauto</code></p>
<dl>
<dd>showauto is used to print a list of automatically installed packages with each package on a new line. All automatically installed packages will be listed if no package is given. If packages are given only those which are automatically installed will be shown.</dl>
<p> <code>showmanual</code></p>
<dl>
<dd>showmanual can be used in the same way as showauto except that it will print a list of manually installed packages instead.</dl>
<h3>Options</h3>
<p><code>-f=</code><i>filename</i>, <code>&#8211;file=</code><i>filename</i></p>
<dl>
<dd>Read/Write package stats from the filename given with the parameter <i>filename</i> instead of from the default location, which is extended_states in the directory defined by the Configuration Item: Dir::State.</dl>
<h2>Prevent Changes For A Package</h2>
<p><code>hold</code></p>
<dl>
<dd>hold is used to mark a package as held back, which will prevent the package from being automatically installed, upgraded or removed.</dl>
<p> <code>unhold</code></p>
<dl>
<dd>unhold is used to cancel a previously set hold on a package to allow all actions again.</dl>
<p> <code>showhold</code></p>
<dl>
<dd>showhold is used to print a list of packages on hold in the same way as for the other show commands.</dl>
<h2>Schedule Packages For Install, Remove And Purge</h2>
<p>Some front-ends like <code>apt-get dselect-upgrade</code> can be used to apply previously scheduled changes to the install state of packages. Such changes can be scheduled with the <code>install</code>, <code>remove</code> (also known as <code>deinstall</code>) and <code>purge</code> commands. Packages with a specific selection can be displayed with <code>showinstall</code>, <code>showremove</code> and <code>showpurge</code> respectively. More information about these so called dpkg selections can be found in <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1).</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code></p>
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
<p>/var/lib/apt/extended_states</p>
<dl>
<dd>Status list of auto-installed packages. Configuration Item: Dir::State::extended_states.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8),<code><a href="/docs/linux/man/8-aptitude/">aptitude</a></code>(8),<code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5)</p>
<h2>Diagnostics</h2>
<p><code>apt-mark</code> returns zero on normal operation, non-zero on error.</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Authors</h2>
<p><code>Mike O&#8217;Connor</code></p>
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
