---
title: "apt-key(8)"
name: "apt-key"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-key/"
description: "apt-key – Deprecated APT key management utility"
---

<p>apt-key &#8211; Deprecated APT key management utility</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>apt-key</code> [<code>&#8211;keyring&nbsp;</code><i>filename</i>] {add&nbsp;<i>filename</i> | del&nbsp;<i>keyid</i> | export&nbsp;<i>keyid</i> | exportall | list | finger | adv | update | net-update | {-v | &#8211;version} | {-h | &#8211;help}}</dl>
<h2>Description</h2>
<p><code>apt-key</code></p>
<dd>is used to manage the list of keys used by apt to authenticate packages. Packages which have been authenticated using these keys will be considered trusted. </p>
<p> Use of <code>apt-key</code> is deprecated, except for the use of <code>apt-key del</code> in maintainer scripts to remove existing keys from the main keyring. If such usage of <code>apt-key</code> is desired the additional installation of the GNU Privacy Guard suite (packaged in gnupg) is required. </p>
<p> <a href="/docs/linux/man/8-apt-key/">apt-key</a>(8) will last be available in Debian 11 and Ubuntu 22.04.</p>
<h2>Supported Keyring Files</h2>
<p>apt-key supports only the binary OpenPGP format (also known as &quot;GPG key public ring&quot;) in files with the &quot;gpg&quot; extension, not the keybox database format introduced in newer <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) versions as default for keyring files. Binary keyring files intended to be used with any apt version should therefore always be created with <code>gpg &#8211;export</code>. </p>
<p> Alternatively, if all systems which should be using the created keyring have at least apt version &gt;= 1.4 installed, you can use the ASCII armored format with the &quot;asc&quot; extension instead which can be created with <code>gpg &#8211;armor &#8211;export</code>.</p>
<h2>Commands</h2>
<p><code>add</code> <i>filename</i> (deprecated)</p>
<dl>
<dd>Add a new key to the list of trusted keys. The key is read from the filename given with the parameter <i>filename</i> or if the filename is &#8211; from standard input. </p>
<p> It is critical that keys added manually via <code>apt-key</code> are verified to belong to the owner of the repositories they claim to be for otherwise the <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) infrastructure is completely undermined. </p>
<p> <i>Note</i>: Instead of using this command a keyring should be placed directly in the /etc/apt/trusted.gpg.d/ directory with a descriptive name and either &quot;gpg&quot; or &quot;asc&quot; as file extension.</dl>
<p> <code>del</code> <i>keyid</i> (mostly deprecated)</p>
<dl>
<dd>Remove a key from the list of trusted keys.</dl>
<p> <code>export</code> <i>keyid</i> (deprecated)</p>
<dl>
<dd>Output the key <i>keyid</i> to standard output.</dl>
<p> <code>exportall</code> (deprecated)</p>
<dl>
<dd>Output all trusted keys to standard output.</dl>
<p> <code>list</code>, <code>finger</code> (deprecated)</p>
<dl>
<dd>List trusted keys with fingerprints.</dl>
<p> <code>adv</code> (deprecated)</p>
<dl>
<dd>Pass advanced options to gpg. With <code>adv &#8211;recv-key</code> you can e.g. download key from keyservers directly into the trusted set of keys. Note that there are <i>no</i> checks performed, so it is easy to completely undermine the <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) infrastructure if used without care.</dl>
<p> <code>update</code> (deprecated)</p>
<dl>
<dd>Update the local keyring with the archive keyring and remove from the local keyring the archive keys which are no longer valid. The archive keyring is shipped in the archive-keyring package of your distribution, e.g. the ubuntu-keyring package in Ubuntu. </p>
<p> Note that a distribution does not need to and in fact should not use this command any longer and instead ship keyring files in the /etc/apt/trusted.gpg.d/ directory directly as this avoids a dependency on gnupg and it is easier to manage keys by simply adding and removing files for maintainers and users alike.</dl>
<p> <code>net-update</code> (deprecated)</p>
<dl>
<dd>Perform an update working similarly to the <code>update</code> command above, but get the archive keyring from a URI instead and validate it against a master key. This requires an installed <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) and an APT build configured to have a server to fetch from and a master keyring to validate. APT in Debian does not support this command, relying on <code>update</code> instead, but Ubuntu&#8217;s APT does.</dl>
<h2>Options</h2>
<p>Note that options need to be defined before the commands described in the previous section. </p>
<p> <code>&#8211;keyring</code> <i>filename</i> (deprecated)</p>
<dl>
<dd>With this option it is possible to specify a particular keyring file the command should operate on. The default is that a command is executed on the trusted.gpg file as well as on all parts in the trusted.gpg.d directory, though trusted.gpg is the primary keyring which means that e.g. new keys are added to this one.</dl>
<h2>Deprecation</h2>
<p>Except for using <code>apt-key del</code> in maintainer scripts, the use of <code>apt-key</code> is deprecated. This section shows how to replace existing use of <code>apt-key</code>. </p>
<p> If your existing use of <code>apt-key add</code> looks like this: </p>
<p> wget -qO- <a rel="nofollow" href="https://myrepo.example/myrepo.asc">https://myrepo.example/myrepo.asc</a> | sudo apt-key add &#8211; </p>
<p> Then you can directly replace this with (though note the recommendation below): </p>
<p> wget -qO- <a rel="nofollow" href="https://myrepo.example/myrepo.asc">https://myrepo.example/myrepo.asc</a> | sudo tee /etc/apt/trusted.gpg.d/myrepo.asc </p>
<p> Make sure to use the &quot;asc&quot; extension for ASCII armored keys and the &quot;gpg&quot; extension for the binary OpenPGP format (also known as &quot;GPG key public ring&quot;). The binary OpenPGP format works for all apt versions, while the ASCII armored format works for apt version &gt;= 1.4. </p>
<p> <i>Recommended:</i> Instead of placing keys into the /etc/apt/trusted.gpg.d directory, you can place them anywhere on your filesystem by using the Signed-By option in your sources.list and pointing to the filename of the key. See <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) for details. Since APT 2.4, /etc/apt/keyrings is provided as the recommended location for keys not managed by packages. When using a deb822-style sources.list, and with apt version &gt;= 2.4, the Signed-By option can also be used to include the full ASCII armored keyring directly in the sources.list without an additional file.</p>
<h2>Files</h2>
<p>/etc/apt/trusted.gpg</p>
<dl>
<dd>Keyring of local trusted keys, new keys will be added here. Configuration Item: Dir::Etc::Trusted.</dl>
<p> /etc/apt/trusted.gpg.d/</p>
<dl>
<dd>File fragments for the trusted keys, additional keyrings can be stored here (by other packages or the administrator). Configuration Item Dir::Etc::TrustedParts.</dl>
<p> /etc/apt/keyrings/</p>
<dl>
<dd>Place to store additional keyrings to be used with Signed-By.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8)</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p>APT was written by the APT team &lt;apt [at] packages.debian.org&gt;.</p>
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
