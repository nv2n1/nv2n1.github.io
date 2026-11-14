---
title: "getsebool(8)"
name: "getsebool"
section: "8"
letter: "g"
url: "/docs/linux/man/8-getsebool/"
description: "getsebool – get SELinux boolean value(s)"
---

<p>getsebool &#8211; get SELinux boolean value(s)</p>
<h2>Synopsis</h2>
<p><code>getsebool</code> [<code>-a</code>] [<i>boolean</i>]</p>
<h2>Description</h2>
<p><code>getsebool </code> reports where a particular SELinux boolean or all SELinux booleans are on or off In certain situations a boolean can be in one state with a pending change to the other state. getsebool will report this as a pending change. The pending value indicates the value that will be applied upon the next boolean commit. </p>
<p> The setting of boolean values occurs in two stages; first the pending value is changed, then the booleans are committed, causing their active values to become their pending values. This allows a group of booleans to be changed in a single transaction, by setting all of their pending values as desired and then committing once.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Show all SELinux booleans.</dl>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The program was written by Tresys Technology.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-setsebool/">setsebool</a></code>(8), <code><a href="/docs/linux/man/8-booleans/">booleans</a></code>(8) </p>
