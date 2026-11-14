---
title: "rscript(1)"
name: "rscript"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rscript/"
description: "Rscript – front end for scripting with R"
---

<p>Rscript &#8211; front end for scripting with R </p>
<h2>Synopsis</h2>
<p><code>Rscript</code> [<i>&#8211;options</i>] [<i>-e expr</i>] <i>file </i>[<i>args</i>]</p>
<h2>Description</h2>
<p>A binary front-end to R, for use in scripting applications.</p>
<dl>
<dt><code>expr</code></p>
<dd>An optional expression to be evaluated, used in place of <code>file</code>.</p>
<dt><code>file</code></p>
<dd>Input file of R expressions</p>
<dt><code>args</code></p>
<dd>Optional further arguments to be processed by <i>commandArgs</i> in the R interpreter.</dl>
<h2>Options</h2>
<p><code>&#8211;options</code> accepted are</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print usage and exit</p>
<dt><code>&#8211;version</code></p>
<dd>Print version and exit</p>
<dt><code>&#8211;verbose</code></p>
<dd>Print information on progress</p>
<dt><code>&#8211;default-packages</code>=<i>list</i></p>
<dd>Where &#8216;list&#8217; is a comma-separated set of package names, or &#8216;NULL&#8217;</dl>
<p> and also options to R (in addition to <code>&#8211;no-echo</code> <code>&#8211;no-restore</code>), such as</p>
<dl>
<dt><code>&#8211;save</code></p>
<dd>Do save workspace at the end of the session</p>
<dt><code>&#8211;no-environ</code></p>
<dd>Don&#8217;t read the site and user environment files</p>
<dt><code>&#8211;no-site-file</code></p>
<dd>Don&#8217;t read the site-wide Rprofile</p>
<dt><code>&#8211;no-init-file</code></p>
<dd>Don&#8217;t read the user R profile</p>
<dt><code>&#8211;restore</code></p>
<dd>Do restore previously saved objects at startup</p>
<dt><code>&#8211;vanilla</code></p>
<dd>Combine <code>&#8211;no-save</code>, <code>&#8211;no-restore</code>, <code>&#8211;no-site-file</code> <code>&#8211;no-init-file</code> and <code>&#8211;no-environ</code></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-r/">R</a>(1)</code></p>
