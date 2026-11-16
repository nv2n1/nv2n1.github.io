---
title: "frontend-spec(7)"
name: "frontend-spec"
section: "7"
letter: "f"
url: "/docs/linux/man/7-frontend-spec/"
description: "frontend-spec – interface between jw and its frontends"
---

<p>frontend-spec &#8211; interface between jw and its frontends</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/1-jw/">jw</a></code>(1) calls frontends like <i>frontends/docbook</i> to get the informations specific to a given input format. The frontend knows which information to return from the first command line parameter. It gets all necessary data via environment variables ready to use. </p>
<p> This document describes that command line parameter and those environment variables. </p>
<p> The frontend should return 0 if there weren&#8217;t any problem, and return a positive value otherwise.</p>
<h2>Variables</h2>
<dl>
<dt><code> $1 </code></dt>
<dd>The command line parameter, specifying which information to return. It can take the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>centralized-catalog</code></dt>
<dd>The frontend must return the DTD-specific centralized catalog name. Centralized catalogs normally reside in <i>/etc/sgml</i> and provide the location of all the catalog files useful for handling this input type (the catalog for the DTD, the catalog for the stylesheets, the catalog for the entities,</dd>
<dt><code>style-sheet</code></dt>
<dd>The frontend must return the filename of the style sheet to be used for this document type and with the chosen backend.</dd></dl>
</dl>
</dl>
<dl>
<dt><code> SGML_CATALOGS_DIR </code></dt>
<dd>The directory where the centralized catalogs reside. It is normally <i>/etc/sgml</i>. </dd>
<p> (This variable is valid only while determining the centralized catalog to use.)</dl>
<dl>
<dt><code> SGML_BASE_DIR </code></dt>
<dd>The base directory of the SGML system. It is normally <i>/usr/share/sgml</i>. </dd>
<p> (This variable is valid only while determining the style sheet to use.)</dl>
<dl>
<dt><code> SGML_FILE </code></dt>
<dd>The name of the file to convert. </dd>
<p> (This variable is valid only while determining the centralized catalog to use.)</dl>
<dl>
<dt><code> SGML_TYPE </code></dt>
<dd>The type of the backend to use, whether it produces output files to be displayed online or to be printed out. It can take the value html or print. </dd>
<p> (This variable is valid only while determining the style sheet to use).</dl>
<dl>
<dt><code> SGML_STYLESHEETS </code></dt>
<dd>The desired custom stylesheet type, either none or default. If none, the frontend must return the file name of the style sheet provided by the system beneath the docbook-utils. If default, the frontend must return the custom stylesheet provided by the docbook-utils. </dd>
<p> (This variable is valid only while determining the style sheet to use).</p>
<dt><code> SGML_XML </code></dt>
<dd>The metalanguage of the file to convert, either sgml or xml. </dd>
<p> (This variable is valid only while determining the centralized catalog to use).</dl>
<h2>Files</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-backend-spec/">backend-spec</a></code>(7)</p>
<h2>Authors</h2>
<p>Jochem Huhmann &lt;joh [at] revier.com&gt;</p>
</p>