---
title: "named-journalprint(8)"
name: "named-journalprint"
section: "8"
letter: "n"
url: "/docs/linux/man/8-named-journalprint/"
description: "named-journalprint – print zone journal in human-readable form"
---

<p>named-journalprint &#8211; print zone journal in human-readable form</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>named-journalprint</code> {<i>journal</i>}</dl>
<h2>Description</h2>
<p><code>named-journalprint</code></p>
<dd>prints the contents of a zone journal file in a human-readable form. </p>
<p> Journal files are automatically created by <code>named</code> when changes are made to dynamic zones (e.g., by <code>nsupdate</code>). They record each addition or deletion of a resource record, in binary format, allowing the changes to be re-applied to the zone when the server is restarted after a shutdown or crash. By default, the name of the journal file is formed by appending the extension <i>.jnl</i> to the name of the corresponding zone file. </p>
<p> <code>named-journalprint</code> converts the contents of a given journal file into a human-readable text format. Each line begins with &quot;add&quot; or &quot;del&quot;, to indicate whether the record was added or deleted, and continues with the resource record in master-file format.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code><a href="/docs/linux/man/8-nsupdate/">nsupdate</a></code>(8), BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
