---
title: "cryptdisks_stop(8)"
name: "cryptdisks_stop"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cryptdisks_stop/"
description: "cryptdisks_stop – wrapper around cryptsetup that parses /etc/crypttab."
---

<p>cryptdisks_stop &#8211; wrapper around cryptsetup that parses /etc/crypttab.</p>
<h2>Synopsis</h2>
<p><code>cryptdisks_stop</code> <i>&lt;name&gt;</i></p>
<h2>Description</h2>
<p><code>cryptdisks_stop</code> is a wrapper around <code>cryptsetup</code> that parses <code>/etc/crypttab</code> just like the initscript /etc/init.d/cryptdisks does and stops the dm-crypt mapping that corresponds to <i>&lt;name&gt;</i>.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-cryptdisks_start/">cryptdisks_start</a></i>(8), <i><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></i>(8), <i><a href="/docs/linux/man/5-crypttab/">crypttab</a></i>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Jonas Meurer &lt;mejo [at] debian.org&gt; in January 2008.</p>
