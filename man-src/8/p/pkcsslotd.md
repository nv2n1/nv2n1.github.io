---
title: "pkcsslotd(8)"
name: "pkcsslotd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkcsslotd/"
description: "pkcsslotd – shared memory manager for opencryptoki"
---

<p>pkcsslotd &#8211; shared memory manager for opencryptoki </p>
<h2>Description</h2>
<p>The <code>pkcsslotd</code> daemon manages PKCS#11 objects between PKCS#11-enabled applications. When 2 or more processes are accessing the same cryptographic token, the daemon is notified and updates each application when the token&#8217;s objects change. </p>
<h2>Notes</h2>
<p>Only one instance of the pkcsslotd daemon should be running on any given host. If a prior instance of pkcsslotd did not shut down cleanly, then it may leave an allocated shared memory segment on the system. The allocated memory segment can be identified by its key and can be safely removed once the daemon is stopped with the ipcrm command, such as: <i>ipcrm -M 0x6202AB38</i> The daemon creates the shared memory segment with group ownership by the <i>pkcs11</i> group. All non-root users that should be able to use openCryptoki need to be members of the group. Only trusted users should be assigned to the group, see the &quot;SECURITY NOTE&quot; in the <code><a href="/docs/linux/man/7-opencryptoki/">opencryptoki</a></code>(7) manual page for details. </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-opencryptoki/">opencryptoki</a></code>(7),</p>
<dd>
<dt><code><a href="/docs/linux/man/5-opencryptoki-conf/">opencryptoki.conf</a></code>(5),</p>
<dd>
<dt><code><a href="/docs/linux/man/1-pkcsconf/">pkcsconf</a></code>(1),</p>
<dd>
