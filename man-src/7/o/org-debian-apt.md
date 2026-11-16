---
title: "org-debian-apt(7)"
name: "org-debian-apt"
section: "7"
letter: "o"
url: "/docs/linux/man/7-org-debian-apt/"
description: "org.debian.apt – the main interface of aptdaemon"
---

<p>org.debian.apt &#8211; the main interface of aptdaemon</p>
<h2>Synopsis</h2>
<p>The daemon is accessed through the D-Bus object at <i>/org/debian/apt</i>. Which provides the following interface.</p>
<h2>Description</h2>
<h3>Methods</h3>
<dl>
<dt><code>AddRepository </code></dt>
<dd><code>AddRepository (in &#8216;s&#8217; </code><i>type</i><code>,</code><br />
 <code> in &#8216;s&#8217; </code><i>uri</i><code>,</code><br />
 <code> in &#8216;s&#8217; </code><i>dist</i><code>,</code><br />
 <code> in &#8216;as&#8217; </code><i>comps</i><code>,</code><br />
 <code> in &#8216;s&#8217; </code><i>comment</i><code>,</code><br />
 <code> in &#8216;s&#8217; </code><i>sourcesfile</i><code>)</code></dd>
<dl>
<dd>Add a new repository to the sources list file. The repository has to define the type (e.g. deb or deb-src), uri (e.g. <a rel="nofollow" href="http://archive.debian.org/debian">http://archive.debian.org/debian</a>), the distribution (e.g. stable) and a list of components (e.g. main). </dd>
<p> Optionally a comment and an alternative sources.list file can be specified.</dl>
<dt><code>EnableDistroComponent</code></dt>
<dd><code>EnableDistroComponent (in &#8216;s&#8217; </code><i>comp</i><code>)</code></dd>
<dl>
<dd>Enable a component for all distro repositories, e.g. main or universe.</dd></dl>
<dt><code>GetTrustedVendorKeys</code></dt>
<dd><code>GetTrustedVendorKeys (out &#8216;as&#8217; </code><i>keys</i><code>)</code></dd>
<dl>
<dd>Return the GnuPG keys which are used to authenticate packages.</dd></dl>
<dt><code>GetAtiveTransactions</code></dt>
<dd><code>GetActiveTransactions (out &#8216;as&#8217; </code><i>tids</i><code>)</code></dd>
<dl>
<dd>Return an array of the currently queued transactions.</dd></dl>
<dt><code>Quit</code></dt>
<dd><code>Quit ()</code></dd>
<dl>
<dd>Request the shutdown of the daemon. The daemon will finish a currently running transaction before.</dd></dl>
</dl>
<h3>Transaction Based Methods</h3>
<p>The following methods are handled by transactions. By calling the methods a new transaction will be created for the task. The return value of the method is the D-Bus object path of the corresponding transaction. The transaction can be modified, to use an http proxy or to run in a specific language by setting the corresponding properties on the <code><a href="/docs/linux/man/7-org-debian-apt-transaction/">org.debian.apt.transaction</a></code>(7) interface. Afterwards the transaction has to be queued for processing by calling its Run method on the <code><a href="/docs/linux/man/7-org-debian-apt-transaction/">org.debian.apt.transaction</a></code>(7) interface.</p>
<dl>
<dt><code>UpdateCache</code></dt>
<dd><code>UpdateCache (out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will fetch the latest meta data from the repositories and rebuild the cache of available and installed packages.</dd></dl>
<dt><code>UpdateCachePartially</code></dt>
<dd><code>UpdateCachePartially (in &#8216;s&#8217; </code><i>sources_list</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will fetch the latest meta data from the repositories specified in the given sources.list snippet only and rebuild the cache of available and installed packages.</dd></dl>
<dt><code>InstallPackages</code></dt>
<dd><code>InstallPackages (in &#8216;as&#8217; </code><i>package_names</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will install the packages of the given names. </dd>
<p> Optionally the to be installed version can be specified by appending a &quot;=&quot; and the version to the package name, e.g. &quot;xterm=256-1&quot;.</dl>
<dt><code>InstallFile</code></dt>
<dd><code>InstallFile (in &#8216;s&#8217; </code><i>path</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly create transaction which will install a local *.deb package file at the given <i>path</i>.</dd></dl>
<dt><code>UpgradePackages</code></dt>
<dd><code>UpgradePackages (in &#8216;as&#8217; </code><i>package_names</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will upgrade the packages of the given names to their latest version. </dd>
<p> Optionally the to be installed version can be specified by appending a &quot;=&quot; and the version to the package name, e.g. &quot;xterm=256-1&quot;.</dl>
<dt><code>RemovePackages</code></dt>
<dd><code>RemovePackages (in &#8216;as&#8217; </code><i>package_names</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will remove the packages of the given names. </dd>
<p> Optionally the version of the to be removed packages can be specified by appending a &quot;=&quot; and the version to the package name, e.g. &quot;xterm=256-1&quot;.</dl>
<dt><code>UpgradeSystem</code></dt>
<dd><code>UpgradeSystem (in &#8216;b&#8217; </code><i>safe_mode</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will upgrade the whole system. </dd>
<p> If in safe mode only already installed packages will be updated. Updates which require to remove installed packages or to install additional packages will be skipped.</dl>
<dt><code>CommitPackages</code></dt>
<dd><code>CommitPackages (in &#8216;as&#8217; </code><i>install</i><code>,</code><br />
 <code> in &#8216;as&#8217; </code><i>reinstall,</i><br />
 <code> in &#8216;as&#8217; </code><i>remove,</i><br />
 <code> in &#8216;as&#8217; </code><i>purge,</i><br />
 <code> in &#8216;as&#8217; </code><i>upgrade</i><code>,</code><br />
 <code> in &#8216;as&#8217; </code><i>downgrade</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will perform a complex install/removal task at once. <i>Install</i>, <i>reinstall</i>, <i>remove</i>, <i>purge</i> and <i>upgrade</i> are lists of package names. </dd>
<p> Optionally the version of the to be removed packages or the version of the package which should be installed can be specified by appending a &quot;=&quot; and the version to the package name, e.g. &quot;xterm=256-1&quot;.</dl>
<dt><code>AddVendorKeyFromFile</code></dt>
<dd><code>AddVendorKeyFromFile (in &#8216;s&#8217; </code><i>path</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will install the public GnuPG key at the given <i>path</i> to the list of trusted software vendors. The list will be used to authenticate packages.</dd></dl>
<dt><code>AddVendorKeyFromKeyserver</code></dt>
<dd><code>AddVendorKeyFromKeyserver (in &#8216;s&#8217; </code><i>keyid</i><code>,</code><br />
 <code> in &#8216;s&#8217; </code><i>keyserver,</i><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will download and install the public GnuPG key of the <i>keyid</i> from the given <i>keyserver</i> to the list of trusted software vendors. The list will be used to authenticate packages.</dd></dl>
<dt><code>RemoveVendorKey</code></dt>
<dd><code>RemoveVendorKey (in &#8216;s&#8217; </code><i>fingerprint</i><code>,</code><br />
 <code> out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will remove the public GnuPG key with the given <i>fingerprint</i> from the list of trusted software vendors. The list will be used to authenticate packages.</dd></dl>
<dt><code>FixBrokenDepends</code></dt>
<dd><code>FixBrokenDepends (out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will try to resolve unsatisfied dependencies by installing required packages or removing conflicting ones.</dd></dl>
<dt><code>FixIncompleteInstall</code></dt>
<dd><code>FixIncompleteInstall (out &#8216;s&#8217; </code><i>tid</i><code>)</code></dd>
<dl>
<dd>Return the id of a newly created transaction which will try to complete previously failed installations by calling &quot;dpkg &#8211;configure -a&quot;.</dd></dl>
</dl>
<h3>Signals</h3>
<dl>
<dt><code>ActiveTransactionsChanged</code></dt>
<dd><code>ActiveTransactionsChanged (&#8216;s&#8217; </code><i>active</i><code>,</code><br />
 <code> &#8216;as&#8217; </code><i>queued</i><code>)</code></dd>
<dl>
<dd>The signal is used to report changes of the currently running or queued transactions. If there&#8217;s any active transaction active will be an empty string.</dd></dl>
</dl>
<h2>Homepage</h2>
<p><a rel="nofollow" href="https://launchpad.net/aptdaemon">https://launchpad.net/aptdaemon</a></p>
<h2>Bugs</h2>
<p>You can report bugs at the Launchpad site of aptdaemon: <a rel="nofollow" href="https://bugs.launchpad.net/aptdaemon/+filebug">https://bugs.launchpad.net/aptdaemon/+filebug</a></p>
<h2>Author</h2>
<p>Sebastian Heinlein &lt;devel at glatzor dot de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-org-debian-apt-transaction/">org.debian.apt.transaction</a></code>(7), <code>aptd</code>(2), <code>aptdcon</code>(2) </p>
