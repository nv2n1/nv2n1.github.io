---
title: "debootstrap(8)"
name: "debootstrap"
section: "8"
letter: "d"
url: "/docs/linux/man/8-debootstrap/"
description: "debootstrap – Bootstrap a basic Debian system"
---

<p>debootstrap &#8211; Bootstrap a basic Debian system</p>
<h2>Synopsis</h2>
<p><code>debootstrap</code> [<code>OPTION&#8230;</code>] <i>SUITE TARGET</i> [<i>MIRROR</i> [<i>SCRIPT</i>]] </p>
<p> <code>debootstrap</code> [<code>OPTION&#8230;</code>] &#8211;second-stage</p>
<h2>Description</h2>
<p><code>debootstrap</code> bootstraps a basic Debian system of <i>SUITE</i> into <i>TARGET</i> from <i>MIRROR</i> by running <i>SCRIPT</i>. <i>MIRROR</i> can be an http:// or https:// URL, a file:/// URL, or an <a href="ssh:///">ssh:///</a> URL. </p>
<p> The <i>SUITE</i> may be a release code name (eg, sid, stretch, jessie) or a symbolic name (eg, unstable, testing, stable, oldstable) </p>
<p> Notice that file:/ URLs are translated to file:/// (correct scheme as described in RFC1738 for local filenames), and file:// will <code>not</code> work. <a href="ssh://USER@HOST/PATH">ssh://USER@HOST/PATH</a> URLs are retrieved using <code>scp</code>; use of <code>ssh-agent</code> or similar is strongly recommended. </p>
<p> <code>Debootstrap</code> can be used to install Debian in a system without using an installation disk but can also be used to run a different Debian flavor in a <code>chroot</code> environment. This way you can create a full (minimal) Debian installation which can be used for testing purposes (see the <code>EXAMPLES</code> section). If you are looking for a chroot system to build packages please take a look at <code>pbuilder</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;arch=ARCH</code></p>
<dd>Set the target architecture (use if dpkg isn&#8217;t installed). See also &#8211;foreign.</p>
<dd>
<dt><code>&#8211;include=alpha,beta</code></p>
<dd>Comma separated list of packages which will be added to download and extract lists.</p>
<dd>
<dt><code>&#8211;exclude=alpha,beta</code></p>
<dd>Comma separated list of packages which will be removed from download and extract lists. WARNING: you can and probably will exclude essential packages, be careful using this option.</p>
<dd>
<dt><code>&#8211;extra-suites=alpha,beta</code></p>
<dd>Also use packages from the listed suites of the archive.</p>
<dd>
<dt><code>&#8211;components=alpha,beta</code></p>
<dd>Use packages from the listed components of the archive.</p>
<dd>
<dt><code>&#8211;no-resolve-deps</code></p>
<dd>By default, debootstrap will attempt to automatically resolve any missing dependencies, warning if any are found. Note that this is not a complete dependency resolve in the sense of dpkg or apt, and that it is far better to specify the entire base system than rely on this option. With this option set, this behaviour is disabled.</p>
<dd>
<dt><code>&#8211;log-extra-deps</code></p>
<dd>If you want to record additional dependencies when resolving package dependencies, set this option to track them through debootstrap.log.</p>
<dd>
<dt><code>&#8211;variant=minbase|buildd|fakechroot</code></p>
<dd>Name of the bootstrap script variant to use. Currently, the variants supported are minbase, which only includes <i>required</i> packages and apt; buildd, which installs the build-essential packages and fakechroot, which installs the packages without root privileges. The default, with no <code>&#8211;variant=X</code> argument, is to create a base Debian installation with all packages of priority <i>required</i> and <i>important</i>, including apt.</p>
<dd>
<dt><code>&#8211;merged-usr</code></p>
<dd>Create /{bin,sbin,lib}/ symlinks pointing to their counterparts in /usr/. (Default for most variants.)</p>
<dd>
<dt><code>&#8211;no-merged-usr</code></p>
<dd>Do not create /{bin,sbin,lib}/ symlinks pointing to their counterparts in /usr/. (Default for the buildd variant.)</p>
<dd>
<dt><code>&#8211;keyring=KEYRING</code></p>
<dd>Override the default keyring for the distribution being bootstrapped, and use <i>KEYRING</i> to check signatures of retrieved Release files.</p>
<dd>
<dt><code>&#8211;no-check-gpg</code></p>
<dd>Disables checking gpg signatures of retrieved Release files.</p>
<dd>
<dt><code>&#8211;force-check-gpg</code></p>
<dd>Forces checking Release file signatures, disabling automatic fallback to HTTPS in case of a missing keyring. Incompatible with the previous option.</p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Produce more info about downloading.</p>
<dd>
<dt><code>&#8211;print-debs</code></p>
<dd>Print the packages to be installed, and exit. Note that an empty or non-existing TARGET directory must be specified so that debootstrap can download Packages files to determine which packages should be installed, and to resolve dependencies. The TARGET directory will be deleted unless &#8211;keep-debootstrap-dir is specified.</p>
<dd>
<dt><code>&#8211;download-only</code></p>
<dd>Download packages, but don&#8217;t perform installation.</p>
<dd>
<dt><code>&#8211;foreign</code></p>
<dd>Do the initial unpack phase of bootstrapping only, for example if the target architecture does not match the host architecture. A copy of debootstrap sufficient for completing the bootstrap process will be installed as /debootstrap/debootstrap in the target filesystem. You can run it with the <code>&#8211;second-stage</code> option to complete the bootstrapping process.</p>
<dd>
<dt><code>&#8211;second-stage</code></p>
<dd>Complete the bootstrapping process. Other arguments are generally not needed.</p>
<dd>
<dt><code>&#8211;second-stage-target=DIR</code></p>
<dd>Run second stage in a subdirectory instead of root. (can be used to create a foreign chroot) (requires &#8211;second-stage)</p>
<dd>
<dt><code>&#8211;keep-debootstrap-dir</code></p>
<dd>Don&#8217;t delete the /debootstrap directory in the target after completing the installation.</p>
<dd>
<dt><code>&#8211;cache-dir=DIR</code></p>
<dd>Cache .deb files under directory. It should be an absolute path.</p>
<dd>
<dt><code>&#8211;unpack-tarball=FILE</code></p>
<dd>Acquire .debs from gzipped tarball FILE (specified with absolute path) instead of downloading via HTTP(S).</p>
<dd>
<dt><code>&#8211;make-tarball=FILE</code></p>
<dd>Instead of bootstrapping, make a gzipped tarball (written to FILE) of the downloaded packages. The resulting tarball may be passed to a later <code>&#8211;unpack-tarball</code>. Note that an empty or non-existing TARGET directory must be specified so that debootstrap can download packages to prepare the tarball. The TARGET directory will be deleted unless &#8211;keep-debootstrap-dir is specified.</p>
<dd>
<dt><code>&#8211;debian-installer</code></p>
<dd>Used for internal purposes by the debian-installer</p>
<dd>
<dt><code>&#8211;extractor=TYPE</code></p>
<dd>Override automatic .deb extractor selection to <i>TYPE</i>. Supported extractors are: dpkg-deb and ar.</p>
<dd>
<dt><code>&#8211;no-check-certificate</code></p>
<dd>Do not check certificate against certificate authorities</p>
<dd>
<dt><code>&#8211;certificate=FILE</code></p>
<dd>Use the client certificate stored in file (PEM)</p>
<dd>
<dt><code>&#8211;private-key=FILE</code></p>
<dd>Read the private key from file </p>
</dl>
<h2>Examples</h2>
<p>To setup a <i>stretch</i> system: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;debootstrap stretch ./stretch-chroot&nbsp;<a rel="nofollow" href="http://deb.debian.org/debian">http://deb.debian.org/debian</a> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;debootstrap stretch ./stretch-chroot file:///LOCAL_MIRROR/debian </p>
<p> Full process to create a complete Debian installation of <i>sid</i> (unstable) in a chroot: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;debootstrap sid sid-root&nbsp;<a rel="nofollow" href="http://deb.debian.org/debian/">http://deb.debian.org/debian/</a><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;&#8230; watch it download the whole system&nbsp;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;echo&nbsp;&quot;proc sid-root/proc proc defaults 0 0&quot;&nbsp;&gt;&gt;&nbsp;/etc/fstab<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;mount proc sid-root/proc -t proc<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;echo&nbsp;&quot;sysfs sid-root/sys sysfs defaults 0 0&quot;&nbsp;&gt;&gt;&nbsp;/etc/fstab<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;mount sysfs sid-root/sys -t sysfs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;cp&nbsp;/etc/hosts sid-root/etc/hosts<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main&nbsp;#&nbsp;chroot sid-root&nbsp;/bin/bash</p>
<h2>Author</h2>
<p><code>debootstrap</code> was written by Anthony Towns &lt;ajt [at] debian.org&gt;. This manpage was written by Matt Kraai &lt;kraai [at] debian.org&gt;.</p>
