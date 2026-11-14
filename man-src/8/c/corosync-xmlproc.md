---
title: "corosync-xmlproc(8)"
name: "corosync-xmlproc"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-xmlproc/"
description: "corosync-xmlproc – Converts corosync.xml to the Corosync configuration file."
---

<p>corosync-xmlproc &#8211; Converts corosync.xml to the Corosync configuration file.</p>
<h2>Synopsis</h2>
<p><code>corosync-xmlproc input_xml [output_file]</code></p>
<h2>Description</h2>
<p><code>corosync-xmlproc</code> Converts valid corosync.xml file to the Corosync configuration file format. Command internally uses <code>xsltproc</code> for XML conversion.</p>
<h2>Options</h2>
<dl>
<dt><code>input_xml</code></p>
<dd>Valid XML file to convert.</p>
<dt><code>output_file</code></p>
<dd>Destination file name. If parameter is &#8211; or omitted, output is written to standard output.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-corosync-xml/">corosync.xml</a></code>(5)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
