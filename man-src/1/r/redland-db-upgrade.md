---
title: "redland-db-upgrade(1)"
name: "redland-db-upgrade"
section: "1"
letter: "r"
url: "/docs/linux/man/1-redland-db-upgrade/"
description: "redland-db-upgrade – upgrade older Redland databases to 0.9.12 format"
---

<h2 class="name">NAME</h2>
<p> redland-db-upgrade &#8211; upgrade older Redland databases to 0.9.12 format </p>
<h2>SYNOPSIS</h2>
<p> <code>redland-db-upgrade</code> <i>old BDB Name</i> <i>new BDB name</i></p>
<h2>DESCRIPTION</h2>
<p> <i>redland-db-upgrade</i> converts Redland databases from the format in 0.9.11 and earlier into the new format. It must be run on each Redland database. For example if database <i>a</i> created files <i>a-sp2o.db</i>, <i>a-so2p.db</i> and <i>a-po2s.db</i> it could be converted to a new database <i>b</i> with:</p>
<dl>
<dt>
<dd> redland-db-upgrade a b</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-redland/">redland</a></code>(3),</p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://purl.org/net/dajobe/">http://purl.org/net/dajobe/</a> </p>
<h2>Index</h2>
