---
title: "orte-server(1)"
name: "orte-server"
section: "1"
letter: "o"
url: "/docs/linux/man/1-orte-server/"
description: "ompi-server – Server for supporting name publish/lookup operations."
---

<h2 class="name">NAME</h2>
<p> ompi-server &#8211; Server for supporting name publish/lookup operations.</p>
<h2>SYNOPSIS</h2>
<p> <code>ompi-server</code> [ options ]</p>
<h2>Options</h2>
<p> <i>ompi-server</i> acts as a data server for Open MPI jobs to exchange contact information in support of MPI-2&#8217;s Publish_name and Lookup_name functions.</p>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Display help for this command</p>
<dt><code>-d | &#8211;debug</code></p>
<dd> Enable verbose output for debugging</p>
<dt><code>-r | &#8211;report-uri </code>&lt;value&gt;</p>
<dd> Report the Open MPI contact information for the server. This information is required for MPI jobs to use the data server. Three parameter values are supported: (a) &#8216;-&#8216;, indicating that the uri is to be printed to stdout; (b) &#8216;+&#8217;, indicating that the uri is to be printed to stderr; and (c) &quot;file:path-to-file&quot;, indicating that the uri is to be printed to the specified file. The &quot;path-to-file&quot; can be either absolute or relative, but must be in a location where the user has write permissions. Please note that the resulting file must be read-accessible to expected users of the server.</dl>
<h2>DESCRIPTION</h2>
<p> <i>ompi-server</i> acts as a data server for Open MPI jobs to exchange contact information in support of MPI-2&#8217;s Publish_name and Lookup_name functions.</p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
