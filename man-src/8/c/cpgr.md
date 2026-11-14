---
title: "cpgr(8)"
name: "cpgr"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cpgr/"
description: "cppw, cpgr – copy with locking the given file to the password or group file"
---

<p>cppw, cpgr &#8211; copy with locking the given file to the password or group file</p>
<h2>Synopsis</h2>
<p><code>cppw</code> [<code>-h</code>] [<code>-s</code>] password_file<br />
 <code>cpgr</code> [<code>-h</code>] [<code>-s</code>] group_file </p>
<h2>Description</h2>
<p><code>cppw</code> and <code>cpgr</code> will copy, with locking, the given file to <i>/etc/passwd</i> and <i>/etc/group</i>, respectively. With the <code>-s</code> flag, they will copy the shadow versions of those files, <i>/etc/shadow</i> and <i>/etc/gshadow</i>, respectively. </p>
<p> With the <code>-h</code> flag, the commands display a short help message and exit silently.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-vipw/">vipw</a></code>(8), <code><a href="/docs/linux/man/8-vigr/">vigr</a></code>(8), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5)</p>
<h2>Author</h2>
<p><code>cppw</code> and <code>cpgr</code> were written by Stephen Frost, based on <code>vipw</code> and <code>vigr</code> written by Guy Maor.</p>
