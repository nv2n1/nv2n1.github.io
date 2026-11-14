---
title: "togglesebool(8)"
name: "togglesebool"
section: "8"
letter: "t"
url: "/docs/linux/man/8-togglesebool/"
description: "togglesebool – flip the current value of a SELinux boolean"
---

<p>togglesebool &#8211; flip the current value of a SELinux boolean</p>
<h2>Synopsis</h2>
<p><code>togglesebool boolean&#8230;</code> </p>
<h2>Description</h2>
<p><code>togglesebool</code> flips the current value of a list of booleans. If the value is currently a 1, then it will be changed to a 0 and vice versa. Only the &quot;in memory&quot; values are changed; the boot-time settings are unaffected.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This man page was written by Steve Grubb &lt;sgrubb [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-booleans/">booleans</a>(8), <a href="/docs/linux/man/8-getsebool/">getsebool</a>(8), <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
