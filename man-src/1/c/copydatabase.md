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
<p> <code>copydatabase</code> <i>SOURCE_DATABASE</i>&#8230; <i>DESTINATION_DATABASE</i></p>
<p> copydatabase &#8211; Perform a document-by-document copy of one or more Xapian databases</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-renumber</code></dt>
<dd> Preserve the numbering of document ids (useful if you have external references to them, or have set them to match unique ids from an external source). If multiple source databases are specified and the same docid occurs in more one, the last occurrence will be the one which ends up in the destination database.</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
