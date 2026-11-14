---
title: "glib-compile-schemas(1)"
name: "glib-compile-schemas"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glib-compile-schemas/"
description: "glib-compile-schemas – GSettings schema compiler"
---

<h2 class="name">NAME</h2>
<p> glib-compile-schemas &#8211; GSettings schema compiler </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>glib-compile-schemas</code> [OPTION&#8230;] {DIRECTORY}</dl>
<h2>DESCRIPTION</h2>
<p> <code>glib-compile-schemas</code></p>
<dd>compiles all the GSettings XML schema files in <i>DIRECTORY</i> into a binary file with the name gschemas.compiled that can be used by <code>GSettings</code>. The XML schema files must have the filename extension .gschema.xml. For a detailed description of the XML file format, see the <code>GSettings</code> documentation. </p>
<p> At runtime, GSettings looks for schemas in the glib-2.0/schemas subdirectories of all directories specified in the <code>XDG_DATA_DIRS</code> environment variable. The usual location to install schema files is /usr/share/glib-2.0/schemas. </p>
<p> In addition to schema files, glib-compile-schemas reads &#8216;vendor override&#8217; files, which are key files that can override default values for keys in the schemas. The group names in the key files are the schema id, and the values are written in serialized GVariant form. Vendor override files must have the filename extension .gschema.override. </p>
<p> By convention, vendor override files begin with nn_ where nn is a number from 00 to 99. Higher numbered files have higher priority (eg: if the same override is made in a file numbered 10 and then again in a file numbered 20, the override from 20 will take precedence).</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print program version and exit</dl>
<p> <code>&#8211;targetdir=</code><i>TARGET</i></p>
<dl>
<dt>
<dd> Store gschemas.compiled in the <i>TARGET</i> directory instead of <i>DIRECTORY</i>.</dl>
<p> <code>&#8211;strict</code></p>
<dl>
<dt>
<dd> Abort on any errors in schemas. Without this option, faulty schema files are simply omitted from the resulting compiled schema.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Don&#8217;t write gschemas.compiled. This option can be used to check .gschema.xml sources for errors.</dl>
<p> <code>&#8211;allow-any-name</code></p>
<dl>
<dt>
<dd> Do not enforce restrictions on key names. Note that this option is purely to facility the transition from GConf, and will be removed at some time in the future.</dl>
<h2>Index</h2>
