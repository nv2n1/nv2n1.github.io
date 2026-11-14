---
title: "pango-querymodules-64(1)"
name: "pango-querymodules-64"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pango-querymodules-64/"
description: "pango-querymodules – Module registration utility"
---

<h2 class="name">NAME</h2>
<p> pango-querymodules &#8211; Module registration utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pango-querymodules</code> [OPTION&#8230;] [MODULE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pango-querymodules</code></p>
<dd>collects information about loadable modules for Pango and writes it to stdout. </p>
<p> If called without MODULE arguments, it looks for modules in the Pango module path, which is specified by the key Pango/ModulesPath in the Pango configuration database. </p>
<p> If called with MODULE arguments, it looks for the specified modules. The arguments may be absolute or relative paths. </p>
<p> At runtime, Pango looks for the loadable module information (i.e. the output of pango-querymodules) in <i>libdir</i>/pango/1.8.0/modules.cache.</p>
<h2>OPTIONS</h2>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints version information.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Do not load user-specific configuration.</dl>
<p> <code>&#8211;update-cache</code></p>
<dl>
<dt>
<dd> Update the Pango module cache file directly, instead of writing the information to stdout.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PANGO_RC_FILE</code></p>
<dl>
<dt>
<dd> Specifies an additional rc file for the Pango configuration database, in addition to the system-wide and per-user files.</dl>
<h2>FILES</h2>
<p> <i>sysconfdir</i>/pango/pangorc</p>
<dl>
<dt>
<dd> System-wide Pango configuration file.</dl>
<p> <code>$XDG_CONFIG_HOME</code>/pango/pangorc</p>
<dl>
<dt>
<dd> User-specific Pango configuration file.</dl>
<p> <i>libdir</i>/pango/1.8.0/modules.cache</p>
<dl>
<dt>
<dd> Location of the module cache file read by Pango.</dl>
<h2>BUGS</h2>
<p> None known yet.</p>
<h2>AUTHORS</h2>
<p> <code>Owen Taylor</code></p>
<dl>
<dt>
<dd> Developer</dl>
<p> <code>Behdad Esfahbod</code></p>
<dl>
<dt>
<dd> Developer</dl>
<h2>Index</h2>
