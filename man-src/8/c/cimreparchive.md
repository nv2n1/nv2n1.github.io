---
title: "cimreparchive(8)"
name: "cimreparchive"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimreparchive/"
description: "cimreparchive – create an archive copy of the CIM Server repository"
---

<p>cimreparchive &#8211; create an archive copy of the CIM Server repository</p>
<h2>Synopsis</h2>
<p><code>cimreparchive </code>archive_file </p>
<p> <code>cimreparchive &#8211;help </p>
<p> cimreparchive &#8211;version </code></p>
<h2>Description</h2>
<p>The <code>cimreparchive </code> command creates an archive copy of the CIM Server repository in the specified archive_file. The archive copy is assured to contain a consistent repository state even if it is created while the CIM Server is running. </p>
<p> The archive_file is created using the <a href="/docs/linux/man/1-tar/">tar</a>(1) command. To restore the repository from the archive_file, stop the cimserver, move the active repository files to a different location, use <a href="/docs/linux/man/2-tar/">tar</a>(2) to extract the archived repository files, and restart the cimserver. (Note that the repository location is printed when an archive file is created.)</p>
<h3>Options</h3>
<p><code>cimreparchive </code> recognizes the following options:</p>
<dl>
<dd>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Displays the command help message.</p>
<dt><code>&#8211;version</code></p>
<dd>Displays the CIM Server version number.</dl>
</dl>
<h2>Exit Status</h2>
<p>When an error occurs, an error message is written to the standard error stream and a non-zero exit status value is returned. The following exit status values are defined:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Success</p>
<dt><code>1</code></p>
<dd>General error</p>
<dt><code>2</code></p>
<dd>Failed to initiate archive operation</p>
<dt><code>3</code></p>
<dd>Archive operation failed</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cimserver/">cimserver</a>(8), <a href="/docs/linux/man/1-tar/">tar</a>(1). </p>
