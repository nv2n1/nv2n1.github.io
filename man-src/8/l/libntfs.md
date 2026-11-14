---
title: "libntfs(8)"
name: "libntfs"
section: "8"
letter: "l"
url: "/docs/linux/man/8-libntfs/"
description: "libntfs – library for accessing and managing NTFS volumes"
---

<p>libntfs &#8211; library for accessing and managing NTFS volumes</p>
<h2>Overview</h2>
<p><code>libntfs</code> is GPL licensed library for accessing and managing NTFS volumes. It is used by<code> ntfsprogs</code> and some other projects.</p>
<h2>Accessing Encrypted Files</h2>
<p>Programs that uses<code> libntfs</code> can transparently access encrypted files on NTFS volumes if<code> libntfs</code> was compiled with <code>&#8211;enable-crypto</code> option (it depends on<code> libgcrypt</code>,<code> GNU TLS</code> and <code>libconfig</code>) and user wrote configuration file. Configuration file should be placed in <code>/etc/libntfs/config</code> or <code>$(HOME)/.libntfs/config</code> and contain list of .PFX key files (see ntfsprogs-&lt;version&gt;/libntfs/config in ntfsprogs source tarball for sample configuration file). Key files can be created/exported using<code> cipher</code> tool under windows.</p>
<h2>Authors</h2>
<p><code>libntfs</code> was written by Anton Altaparmakov, Richard Russon, Szabolcs Szakacsits, Yuval Fledel and Yura Pakhuchiy.</p>
<h2>Availability</h2>
<p>The <code>ntfsprogs</code> can be downloaded from:<br />
 <a rel="nofollow" href="http://www.linux-ntfs.org/content/view/19/37">http://www.linux-ntfs.org/content/view/19/37</a> </p>
<p> These manual pages can be viewed online at:<br />
 <a rel="nofollow" href="http://man.linux-ntfs.org/">http://man.linux-ntfs.org/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8), <code><a href="/docs/linux/man/8-libntfs-gnomevfs/">libntfs-gnomevfs</a></code>(8) </p>
