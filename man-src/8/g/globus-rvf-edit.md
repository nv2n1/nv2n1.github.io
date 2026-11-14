---
title: "globus-rvf-edit(8)"
name: "globus-rvf-edit"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-rvf-edit/"
description: "globus-rvf-edit – Edit a GRAM5 RSL validation file"
---

<p>globus-rvf-edit &#8211; Edit a GRAM5 RSL validation file</p>
<h2>Synopsis</h2>
<p><code>globus-rvf-edit</code> <i>-h</i></p>
<h2>Description</h2>
<p>The <code>globus-rvf-edit</code> command is a utility which opens the default editor on a specified RSL validation file, and then, when editing completes, runs the command is a utility which opens the default editor on a specified RSL validation file, and then, when editing completes, runs the <code>globus-rvf-check</code> command to verify that the RVF file syntax is correct. If a parse error occurs, the user will be given an option to rerun the editor or discard the modifications. command to verify that the RVF file syntax is correct. If a parse error occurs, the user will be given an option to rerun the editor or discard the modifications. </p>
<p> The full set of command-line options to <code>globus-rvf-edit</code> consists of: consists of: </p>
<p> <i>-h</i></p>
<dl>
<dd>Print command-line option summary and exit</dl>
<p> <i>-s</i></p>
<dl>
<dd>Edit of the site-specific RVF file, which provides override values applicable to all LRMs installed on the system.</dl>
<p> <code>&#8216;-l &#8216;</code></p>
<dl>
<dd>Edit the site-specific LRM overrides for the LRM named by the <i>&#8216;LRM</i>&#8216; parameter to the option.</dl>
<p> <code>&#8216;-f &#8216;</code></p>
<dl>
<dd>Edit the RVF file located at <i>&#8216;PATH</i>&#8216;</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-globus-rvf-check/">globus-rvf-check</a>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
