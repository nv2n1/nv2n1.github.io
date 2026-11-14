---
title: "vapigen-0-26(1)"
name: "vapigen-0-26"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vapigen-0-26/"
description: "vapigen – generate a Vala API"
---

<p>vapigen &#8211; generate a Vala API </p>
<h2>Synopsis</h2>
<p><code>vapigen </code><i>SOURCE</i> <i>PKGBASE</i> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>Description</h2>
<p><code>vapigen</code> is a utility which generates Vala API (VAPI) files from GI files, which may be generated using the <a href="/docs/linux/man/1-vala-gen-introspect/">vala-gen-introspect</a>(1) utility. </p>
<h2>Examples</h2>
<dl COMPACT>
<dt>After compilation, the following command generates a GI for pango:</p>
<dd><code>vala-gen-introspect pango packages/pango</code></p>
<dt>This can then be converted to a Vala API as follows:</p>
<dd><code>vapigen &#8211;pkg cairo &#8211;vapidir . &#8211;library pango packages/pango/pango.gi</code> </p>
</dl>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-?, &#8211;help</code></p>
<dd>Show help option</p>
<dt><code>&#8211;vapidir=</code><i>DIRECTORY</i></p>
<dd>Look for package bindings in <i>DIRECTORY</i>.</p>
<dt><code>&#8211;girdir=</code><i>DIRECTORY</i></p>
<dd>Look for GIR bindings in <i>DIRECTORY</i>.</p>
<dt><code>&#8211;metadatadir=</code><i>DIRECTORY</i></p>
<dd>Look for GIR .metadata files in <i>DIRECTORY</i>.</p>
<dt><code>&#8211;pkg=</code><i>PACKAGE</i></p>
<dd>Include binding for <i>PACKAGE</i></p>
<dt><code>&#8211;library=</code><i>NAME</i></p>
<dd>Specify library name as <i>NAME</i></p>
<dt><code>-d, &#8211;directory=</code><i>DIRECTORY</i></p>
<dd>Specify output directory as <i>DIRECTORY</i></p>
<dt><code>&#8211;version</code></p>
<dd>Display version number and exit.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Do not print messages to the console </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vala-gen-introspect/">vala-gen-introspect</a></code>(1) </p>
<h2>Homepage And Bug Report</h2>
<p><a rel="nofollow" href="http://www.vala-project.org/">http://www.vala-project.org/</a> </p>
<h2>Author</h2>
<p>vapigen for Vala was written by Jürg Billeter &lt;j@bitron.ch&gt; and Raffaele Sandrini &lt;rasa [at] gmx.ch&gt;. </p>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others).</p>
