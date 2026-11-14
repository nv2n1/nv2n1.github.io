---
title: "vala-gen-introspect-0-26(1)"
name: "vala-gen-introspect-0-26"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vala-gen-introspect-0-26/"
description: "vala-gen-introspect – generate a GI file for GObject and glib based packages"
---

<p>vala-gen-introspect &#8211; generate a GI file for GObject and glib based packages </p>
<h2>Synopsis</h2>
<p><code>vala-gen-introspect </code><i>PKGNAME</i> <i>PKGBASE</i> </p>
<h2>Description</h2>
<p><code>vala-gen-introspect</code> is a utility which generates GI files from GObject and glib based packages. It can be used in combination with <a href="/docs/linux/man/1-vapigen/">vapigen</a>(1) to generate an API for Vala, and allow it&#8217;s usage in Vala for compiling to native code. <i>PKGNAME</i> is the pkg-config name of the library and <i>PKGBASE</i> specifies the base directory for that package. </p>
<h2>Examples</h2>
<dl COMPACT>
<dt>After compilation, the following command generates a GI for pango:</p>
<dd><code>vala-gen-introspect pango packages/pango</code> </p>
</dl>
<h2>Options</h2>
<dl COMPACT>
<dt>This command currently takes no command line options.</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vapigen/">vapigen</a></code>(1) </p>
<h2>Author</h2>
<p>vala-gen-introspect for Vala was written by Juerg Billeter &lt;j@bitron.ch&gt; and Raffaele Sandrini &lt;rasa [at] gmx.ch&gt;. </p>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others).</p>
