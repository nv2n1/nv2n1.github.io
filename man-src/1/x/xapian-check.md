---
title: "xapian-check(1)"
name: "xapian-check"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xapian-check/"
description: "xapian-check – Check the consistency of a database or table"
---

<h2>NAME</h2>
<p> xapian-check &#8211; Check the consistency of a database or table</p>
<h2>SYNOPSIS</h2>
<p> <code>xapian-check</code> <i>&lt;database directory&gt;|&lt;path to btree and prefix&gt; </i>[[<i>t</i>][<i>f</i>][<i>b</i>][<i>v</i>][<i>+</i>]]</p>
<h2>DESCRIPTION</h2>
<p> xapian-check &#8211; Check the consistency of a database or table </p>
<p> If a whole database is checked, then additional cross-checks between the tables are performed.</p>
<h3>The btree(s) is/are always checked &#8211; control the output verbosity with:</h3>
<dl>
<dt>
<dd> t = short tree printing f = full tree printing b = show bitmap v = show stats about B-tree (default) + = same as tbv e.g. xapian-check /var/lib/xapian/data/default</p>
<dt>
<dd> xapian-check /var/lib/xapian/data/default/postlist fbv </p>
</dl>
<h2>Index</h2>
