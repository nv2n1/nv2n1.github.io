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
<dt><code>expr</code></dt>
<dd>An optional expression to be evaluated, used in place of <code>file</code>.</dd>
<dt><code>file</code></dt>
<dd>Input file of R expressions</dd>
<dt><code>args</code></dt>
<dd>Optional further arguments to be processed by <i>commandArgs</i> in the R interpreter.</dd></dl>
<h2>Options</h2>
<p><code>&#8211;options</code> accepted are</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>Print usage and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd>Print version and exit</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Print information on progress</dd>
<dt><code>&#8211;default-packages</code>=<i>list</i></dt>
<dd>Where &#8216;list&#8217; is a comma-separated set of package names, or &#8216;NULL&#8217;</dd></dl>
<p> and also options to R (in addition to <code>&#8211;no-echo</code> <code>&#8211;no-restore</code>), such as</p>
<dl>
<dt><code>&#8211;save</code></dt>
<dd>Do save workspace at the end of the session</dd>
<dt><code>&#8211;no-environ</code></dt>
<dd>Don&#8217;t read the site and user environment files</dd>
<dt><code>&#8211;no-site-file</code></dt>
<dd>Don&#8217;t read the site-wide Rprofile</dd>
<dt><code>&#8211;no-init-file</code></dt>
<dd>Don&#8217;t read the user R profile</dd>
<dt><code>&#8211;restore</code></dt>
<dd>Do restore previously saved objects at startup</dd>
<dt><code>&#8211;vanilla</code></dt>
<dd>Combine <code>&#8211;no-save</code>, <code>&#8211;no-restore</code>, <code>&#8211;no-site-file</code> <code>&#8211;no-init-file</code> and <code>&#8211;no-environ</code></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-r/">R</a>(1)</code></p>
