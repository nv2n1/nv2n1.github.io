---
title: "backend-spec(7)"
name: "backend-spec"
section: "7"
letter: "b"
url: "/docs/linux/man/7-backend-spec/"
description: "backend-spec – interface between jw and its backends"
---

<p>backend-spec &#8211; interface between jw and its backends</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/1-jw/">jw</a></code>(1) calls backends like <i>backends/html</i> to do the &quot;real&quot; conversion work. The backend gets all necessary data delivered via environment variables ready to use. </p>
<p> This documentation describes those environment variables. </p>
<p> The backend is run in the directory where the output files are to be created. It should return 0 if there weren&#8217;t any problem, and return a positive value otherwise.</p>
<h2>Variables</h2>
<dl>
<dt><code> SGML_FILE_NAME </code></p>
<dd>The bare name of the source file</dl>
<dl>
<dt><code> SGML_FILE </code></p>
<dd>The full name and path of the source file</dl>
<dl>
<dt><code> SGML_JADE </code></p>
<dd>The name of the parser (usually <code>Jade</code> or <code>OpenJade</code>)</dl>
<dl>
<dt><code> SGML_ARGUMENTS </code></p>
<dd>The full argument-string for <code>Jade</code> or <code>OpenJade</code></dl>
<dl>
<dt><code> SGML_CATALOG_FILES </code></p>
<dd>The list of catalog files needed by <code>Jade</code> or <code>OpenJade</code></dl>
<dl>
<dt><code> SGML_STYLESHEET </code></p>
<dd>The style sheet to use</dl>
<dl>
<dt><code> SGML_BASE_DIR </code></p>
<dd>The base directory of the SGML system (default is <i>/usr/share/sgml</i>)</dl>
<h2>Files</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-frontend-spec/">frontend-spec</a></code>(7)</p>
<h2>Authors</h2>
<p>Jochem Huhmann &lt;joh [at] revier.com&gt;</p>
