---
title: "cnid_index(1)"
name: "cnid_index"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cnid_index/"
description: "cnid_index – check and repair Netatalk CNID database indexes"
---

<h2 class="name">NAME</h2>
<p> cnid_index &#8211; check and repair Netatalk CNID database indexes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cnid_index</code> <i>dbdir</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>cnid_index</code></p>
<dd>is a utility to check CNID databases for consistency. If needed, the indexes are repaired. It works for databases created by the cdb and dbd backends. </p>
<p> Volumes usind the dbd CNID scheme can also be checked automatically, for further information please see the <code><a href="/docs/linux/man/8-cnid_dbd/">cnid_dbd</a></code>(8) man page. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font> </p>
<p> When using <code>cnid_index</code> on cdb handled databases, <code>cnid_index</code> cannot check if another process (afpd) accesses the CNID databases. In this case, you have to manually ensure no other process accesses the database when running <code>cnid_index</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cnid_dbd/">cnid_dbd</a></code>(8), <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
<h2>Index</h2>
