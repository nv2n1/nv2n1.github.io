---
title: "copydatabase(1)"
name: "copydatabase"
section: "1"
letter: "c"
url: "/docs/linux/man/1-copydatabase/"
description: "copydatabase – Perform a document-by-document copy of one or more Xapian databases"
---

<h2>NAME</h2>
<p> copydatabase &#8211; Perform a document-by-document copy of one or more Xapian databases</p>
<h2>SYNOPSIS</h2>
<p> <code>copydatabase</code> <i>SOURCE_DATABASE</i>&#8230; <i>DESTINATION_DATABASE</i></p>
<h2>DESCRIPTION</h2>
<p> copydatabase &#8211; Perform a document-by-document copy of one or more Xapian databases</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-renumber</code></p>
<dd> Preserve the numbering of document ids (useful if you have external references to them, or have set them to match unique ids from an external source). If multiple source databases are specified and the same docid occurs in more one, the last occurrence will be the one which ends up in the destination database.</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>Index</h2>
