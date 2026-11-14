---
title: "aptdcon(1)"
name: "aptdcon"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aptdcon/"
description: "aptdcon – command line client for aptdaemon"
---

<h2 class="name">NAME</h2>
<p> aptdcon &#8211; command line client for aptdaemon </p>
<h2>SYNOPSIS</h2>
<p> <code>aptdcon</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>aptdcon</code> allows to perform package management tasks, e.g. installing or removing software, using aptdaemon. There isn&#8217;t any need to be root to run this programme.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-v, &#8211;version</p>
<dd> Show the version number of the aptdcon.</p>
<dt>-h, &#8211;help</p>
<dd> Show information about the usage of the command.</p>
<dt>-d, &#8211;debug</p>
<dd> Show additional information on the command line.</p>
<dt>-i, &#8211;install PACKAGES</p>
<dd> Install the list of PACKAGES. If you want to install more than one package you have to put the package names into quotation marks.</p>
<dt>&#8211;reinstall PACKAGES</p>
<dd> Reinstall the list of PACKAGES. If you want to reinstall more than one package you have to put the package names into quotation marks.</p>
<dt>-r, &#8211;remove PACKAGES</p>
<dd> Remove the list of PACKAGES. If you want to remove more than one package you have to put the package names into quotation marks.</p>
<dt>-p, &#8211;purge PACKAGES</p>
<dd> Purge the list of PACKAGES. If you want to purge more than one package you have to put the package names into quotation marks.</p>
<dt>-u, &#8211;upgrade PACKAGES</p>
<dd> Upgrade the list of PACKAGES. If you want to upgrade more than one package you have to put the package names into quotation marks.</p>
<dt>&#8211;upgrade-system</p>
<dd> Upgrade the whole system.</p>
<dt>&#8211;fix-install</p>
<dd> Try to complete a previously cancelled installation by calling &quot;dpkg &#8211;configure -a&quot;.</p>
<dt>&#8211;fix-depends</p>
<dd> Try to resolve unsatisified dependencies. Attention: Currently you don&#8217;t get a confirmation of the changes, which makes this method quite dangerous since it could remove a lot of packages.</p>
<dt>&#8211;add-vendor-key PUBLIC_KEY_FILE</p>
<dd> Install the PUBLIC_KEY_FILE to authenticate and trust packages singed by the vendor.</p>
<dt>&#8211;add-vendor-key-from-keyserver PUBLIC_KEY_ID</p>
<dd> Download and install the PUBLIC_KEY_ID to authenticate and trust packages singed by the vendor. Requires the &#8211;keyserver to be set.</p>
<dt>&#8211;key-server KEYSERVER</p>
<dd> Download vendor keys from the given KEYSERVER.</p>
<dt>&#8211;remove-vendor-key FINGERPRINT</p>
<dd> Remove the vendor key of the given FINGERPRINT to no longer trust packages from this vendor.</p>
<dt>&#8211;add-repository &#8216;DEB_LINE&#8217;</p>
<dd> Allow to install software from the repository specified by the given DEB_LINE. You have to put quotation marks around the DEB_LINE since it normally contains spaces: <i>&#8216;deb <a rel="nofollow" href="http://ftp.de.debian.org/debian">http://ftp.de.debian.org/debian</a> unstable main&#8217;</i></p>
<dt>&#8211;sources-file SOURCES_FILE</p>
<dd> Specify an alternative sources file to which the new repository should be written. SOURCES_FILE should be only the basename: <i>backports.list</i></p>
<dt>&#8211;list-trusted-vendors</p>
<dd> Show all trusted software vendors and theirs keys.</p>
<dt>&#8211;hide-terminal</p>
<dd> Do not attach to the interactive terminal of the underlying dpkg call.</p>
<dt>&#8211;allow-unauthenticated</p>
<dd> Allow to install packages which are not from a trusted vendor.</dl>
<h2>EXAMPLES</h2>
<p> The following command will install the package xterm and remove the package eterm in the same run:</p>
<dl>
<dt>
<dd> $ aptdcon &#8211;install &quot;xterm&quot; &#8211;remove &quot;eterm&quot;</dl>
<p> To handle more than one package the names have to be put into quotation marks. The following command will install xterm and eterm:</p>
<dl>
<dt>
<dd> $ aptdcon &#8211;install &quot;xterm eterm&quot;</dl>
<p> The following command will add the backport repository to the sources.list in a separate file <i>/etc/apt/sources.list.d/backports.list</i> :</p>
<dl>
<dt>
<dd> $ aptdcon &#8211;sources-file backports.list \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;add-repostiry&nbsp;&quot;deb&nbsp;<a rel="nofollow" href="http://archive.backports.org/debian">http://archive.backports.org/debian</a>&nbsp;stable main&quot;</dl>
<h2>DIAGNOSTICS</h2>
<p> By default aptdaemon logs to the syslog facility AptDaemon. Furthermore you can use the -d option to get additional information on the command line.</p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="https://launchpad.net/aptdaemon">https://launchpad.net/aptdaemon</a></p>
<h2>BUGS</h2>
<p> You can report bugs at the Launchpad site of aptdaemon: <a rel="nofollow" href="https://bugs.launchpad.net/aptdaemon/+filebug">https://bugs.launchpad.net/aptdaemon/+filebug</a></p>
<h2>AUTHOR</h2>
<p> Sebastian Heinlein &lt;devel at glatzor dot de&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aptd/">aptd</a></code>(1), <code><a href="/docs/linux/man/7-org-debian-apt/">org.debian.apt</a></code>(7), <code><a href="/docs/linux/man/7-org-debian-apt-transaction/">org.debian.apt.transaction</a></code>(7) </p>
<h2>Index</h2>
