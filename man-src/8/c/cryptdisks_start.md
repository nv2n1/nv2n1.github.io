---
title: "cryptdisks_start(8)"
name: "cryptdisks_start"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cryptdisks_start/"
description: "cryptdisks_start – wrapper around cryptsetup that parses /etc/crypttab."
---

<p>cryptdisks_start &#8211; wrapper around cryptsetup that parses /etc/crypttab.</p>
<h2>Synopsis</h2>
<p><code>cryptdisks_start</code> <i>&lt;name&gt;</i></p>
<h2>Description</h2>
<p><code>cryptdisks_start</code> is a wrapper around <code>cryptsetup</code> that parses <code>/etc/crypttab</code> just like the initscript /etc/init.d/cryptdisks does and starts the dm-crypt mapping that corresponds to <i>&lt;name&gt;</i>. </p>
<p> Note that this wrapper passes <code>&#8211;key-file=-</code> to <code>cryptsetup</code>, so the passphrase in any referenced key file must not be followed by a newline character.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-cryptdisks_stop/">cryptdisks_stop</a></i>(8), <i><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></i>(8), <i><a href="/docs/linux/man/5-crypttab/">crypttab</a></i>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Jonas Meurer &lt;mejo [at] debian.org&gt; in December 2007.</p>
