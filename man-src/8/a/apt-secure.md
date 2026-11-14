---
title: "apt-secure(8)"
name: "apt-secure"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-secure/"
description: "apt-secure – Archive authentication support for APT"
---

<p>apt-secure &#8211; Archive authentication support for APT</p>
<h2>Description</h2>
<p>Starting with version 0.6, <code>APT</code> contains code that does signature checking of the Release file for all repositories. This ensures that data like packages in the archive can&#8217;t be modified by people who have no access to the Release file signing key. Starting with version 1.1 <code>APT</code> requires repositories to provide recent authentication information for unimpeded usage of the repository. Since version 1.5 changes in the information contained in the Release file about the repository need to be confirmed before APT continues to apply updates from this repository. </p>
<p> Note: All APT-based package management front-ends like <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/8-aptitude/">aptitude</a></code>(8) and <code><a href="/docs/linux/man/8-synaptic/">synaptic</a></code>(8) support this authentication feature, so this manpage uses APT to refer to them all for simplicity only.</p>
<h2>Unsigned Repositories</h2>
<p>If an archive has an unsigned Release file or no Release file at all current APT versions will refuse to download data from them by default in <code>update</code> operations and even if forced to download front-ends like <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) will require explicit confirmation if an installation request includes a package from such an unauthenticated archive. </p>
<p> You can force all APT clients to raise only warnings by setting the configuration option <code>Acquire::AllowInsecureRepositories</code> to true. Individual repositories can also be allowed to be insecure via the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) option allow-insecure=yes. Note that insecure repositories are strongly discouraged and all options to force apt to continue supporting them will eventually be removed. Users also have the <code>Trusted</code> option available to disable even the warnings, but be sure to understand the implications as detailed in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5). </p>
<p> A repository which previously was authenticated but would loose this state in an <code>update</code> operation raises an error in all APT clients irrespective of the option to allow or forbid usage of insecure repositories. The error can be overcome by additionally setting <code>Acquire::AllowDowngradeToInsecureRepositories</code> to true or for Individual repositories with the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) option allow-downgrade-to-insecure=yes.</p>
<h2>Signed Repositories</h2>
<p>The chain of trust from an APT archive to the end user is made up of several steps. <code>apt-secure</code> is the last step in this chain; trusting an archive does not mean that you trust its packages not to contain malicious code, but means that you trust the archive maintainer. It&#8217;s the archive maintainer&#8217;s responsibility to ensure that the archive&#8217;s integrity is preserved. </p>
<p> apt-secure does not review signatures at a package level. If you require tools to do this you should look at <code>debsig-verify</code> and <code>debsign</code> (provided in the debsig-verify and devscripts packages respectively). </p>
<p> The chain of trust in Debian starts (e.g.) when a maintainer uploads a new package or a new version of a package to the Debian archive. In order to become effective, this upload needs to be signed by a key contained in one of the Debian package maintainer keyrings (available in the debian-keyring package). Maintainers&#8217; keys are signed by other maintainers following pre-established procedures to ensure the identity of the key holder. Similar procedures exist in all Debian-based distributions. </p>
<p> Once the uploaded package is verified and included in the archive, the maintainer signature is stripped off, and checksums of the package are computed and put in the Packages file. The checksums of all of the Packages files are then computed and put into the Release file. The Release file is then signed by the archive key for this Ubuntu release, and distributed alongside the packages and the Packages files on Ubuntu mirrors. The keys are in the Ubuntu archive keyring available in the ubuntu-keyring package. </p>
<p> End users can check the signature of the Release file, extract a checksum of a package from it and compare it with the checksum of the package they downloaded by hand &#8211; or rely on APT doing this automatically. </p>
<p> Notice that this is distinct from checking signatures on a per package basis. It is designed to prevent two possible attacks: </p>
<dl>
<dd>&bull; Network &quot;man in the middle&quot; attacks. Without signature checking, malicious agents can introduce themselves into the package download process and provide malicious software either by controlling a network element (router, switch, etc.) or by redirecting traffic to a rogue server (through ARP or DNS spoofing attacks).</dl>
<dl>
<dd>&bull; Mirror network compromise. Without signature checking, a malicious agent can compromise a mirror host and modify the files in it to propagate malicious software to all users downloading packages from that host.</dl>
<p> However, it does not defend against a compromise of the master server itself (which signs the packages) or against a compromise of the key used to sign the Release files. In any case, this mechanism can complement a per-package signature.</p>
<h2>Information Changes</h2>
<p>A Release file contains beside the checksums for the files in the repository also general information about the repository like the origin, codename or version number of the release. </p>
<p> This information is shown in various places so a repository owner should always ensure correctness. Further more user configuration like <code><a href="/docs/linux/man/5-apt_preferences/">apt_preferences</a></code>(5) can depend and make use of this information. Since version 1.5 the user must therefore explicitly confirm changes to signal that the user is sufficiently prepared e.g. for the new major release of the distribution shipped in the repository (as e.g. indicated by the codename).</p>
<h2>User Configuration</h2>
<p><code>apt-key</code> is the program that manages the list of keys used by APT to trust repositories. It can be used to add or remove keys as well as list the trusted keys. Limiting which key(s) are able to sign which archive is possible via the <code>Signed-By</code> in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5). </p>
<p> Note that a default installation already contains all keys to securely acquire packages from the default repositories, so fiddling with <code>apt-key</code> is only needed if third-party repositories are added. </p>
<p> In order to add a new key you need to first download it (you should make sure you are using a trusted communication channel when retrieving it), add it with <code>apt-key</code> and then run <code>apt-get update</code> so that apt can download and verify the InRelease or Release.gpg files from the archives you have configured.</p>
<h2>Repository Configuration</h2>
<p>If you want to provide archive signatures in an archive under your maintenance you have to: </p>
<dl>
<dd>&bull; <i>Create a toplevel Release file</i>, if it does not exist already. You can do this by running <code>apt-ftparchive release</code> (provided in apt-utils).</dl>
<dl>
<dd>&bull; <i>Sign it</i>. You can do this by running <code>gpg &#8211;clearsign -o InRelease Release</code> and <code>gpg -abs -o Release.gpg Release</code>.</dl>
<dl>
<dd>&bull; <i>Publish the key fingerprint</i>, so that your users will know what key they need to import in order to authenticate the files in the archive. It is best to ship your key in its own keyring package like Ubuntu does with ubuntu-keyring to be able to distribute updates and key transitions automatically later.</dl>
<dl>
<dd>&bull; <i>Provide instructions on how to add your archive and key</i>. If your users can&#8217;t acquire your key securely the chain of trust described above is broken. How you can help users add your key depends on your archive and target audience ranging from having your keyring package included in another archive users already have configured (like the default repositories of their distribution) to leveraging the web of trust.</dl>
<p> Whenever the contents of the archive change (new packages are added or removed) the archive maintainer has to follow the first two steps outlined above.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5), <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5), <code><a href="/docs/linux/man/8-apt-key/">apt-key</a></code>(8), <code><a href="/docs/linux/man/1-apt-ftparchive/">apt-ftparchive</a></code>(1), <code><a href="/docs/linux/man/1-debsign/">debsign</a></code>(1), <code><a href="/docs/linux/man/1-debsig-verify/">debsig-verify</a></code>(1), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<p> For more background information you might want to review the m[blue]<code>Debian Security Infrastructure</code>m[]<font SIZE="-2">[1]</font> chapter of the Securing Debian Manual (also available in the harden-doc package) and the m[blue]<code>Strong Distribution HOWTO</code>m[]<font SIZE="-2">[2]</font> by V. Alex Brennen.</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[3]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p>APT was written by the APT team &lt;apt [at] packages.debian.org&gt;.</p>
<h2>Manpage Authors</h2>
<p>This man-page is based on the work of Javier Fernández-Sanguino Peña, Isaac Jones, Colin Walters, Florian Weimer and Michael Vogt.</p>
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
<dd>Debian Security Infrastructure</p>
<dl>
<dd><a rel="nofollow" href="https://www.debian.org/doc/manuals/securing-debian-howto/ch7">https://www.debian.org/doc/manuals/securing-debian-howto/ch7</a></dl>
<dt> 2.</p>
<dd>Strong Distribution HOWTO</p>
<dl>
<dd><a rel="nofollow" href="http://www.cryptnet.net/fdp/crypto/strong_distro.html">http://www.cryptnet.net/fdp/crypto/strong_distro.html</a></dl>
<dt> 3.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
