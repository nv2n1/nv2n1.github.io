---
title: "asciidoc(1)"
name: "asciidoc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asciidoc/"
description: "asciidoc – converts an AsciiDoc text file to HTML or DocBook"
---

<h2 class="name">NAME</h2>
<p> asciidoc &#8211; converts an AsciiDoc text file to HTML or DocBook </p>
<h2>SYNOPSIS</h2>
<p> <code>asciidoc</code> [<i>OPTIONS</i>] <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-asciidoc/">asciidoc</a>(1) command translates the AsciiDoc text file <i>FILE</i> to DocBook or HTML. If <i>FILE</i> is <i>&#8211;</i> then the standard input is used.</p>
<h2>OPTIONS</h2>
<p> <code>-a, &#8211;attribute</code>=<i>ATTRIBUTE</i></p>
<dl>
<dt>
<dd> Define or delete document attribute. <i>ATTRIBUTE</i> is formatted like <i>NAME=VALUE</i>. Command-line attributes take precedence over document and configuration file attributes. Alternate acceptable forms are <i>NAME</i> (the <i>VALUE</i> defaults to an empty string); <i>NAME!</i> (delete the <i>NAME</i> attribute); <i>NAME=VALUE@</i> (do not override document or configuration file attributes). Values containing spaces should be enclosed in double-quote characters. This option may be specified more than once. A special attribute named <i>trace</i> controls the output of diagnostic information.</dl>
<p> <code>-b, &#8211;backend</code>=<i>BACKEND</i></p>
<dl>
<dt>
<dd> Backend output file format: <i>docbook45</i>, <i>xhtml11</i>, <i>html4</i>, <i>html5</i>, <i>slidy</i>, <i>wordpress</i> or <i>latex</i> (the <i>latex</i> backend is experimental). You can also use the backend alias names <i>html</i> (aliased to <i>xhtml11</i>) or <i>docbook</i> (aliased to <i>docbook45</i>). Defaults to <i>html</i>. The <code>&#8211;backend</code> option is also used to manage backend plugins (see <code>PLUGIN COMMANDS</code>).</dl>
<p> <code>-f, &#8211;conf-file</code>=<i>CONF_FILE</i></p>
<dl>
<dt>
<dd> Use configuration file <i>CONF_FILE</i>.Configuration files processed in command-line order (after implicit configuration files). This option may be specified more than once.</dl>
<p> <code>&#8211;doctest</code></p>
<dl>
<dt>
<dd> Run Python doctests in <i>asciidoc</i> module.</dl>
<p> <code>-d, &#8211;doctype</code>=<i>DOCTYPE</i></p>
<dl>
<dt>
<dd> Document type: <i>article</i>, <i>manpage</i> or <i>book</i>. The <i>book</i> document type is only supported by the <i>docbook</i> backend. Default document type is <i>article</i>.</dl>
<p> <code>-c, &#8211;dump-conf</code></p>
<dl>
<dt>
<dd> Dump configuration to stdout.</dl>
<p> <code>&#8211;filter</code>=<i>FILTER</i></p>
<dl>
<dt>
<dd> Specify the name of a filter to be loaded (used to load filters that are not auto-loaded). This option may be specified more than once. The <code>&#8211;filter</code> option is also used to manage filter plugins (see <code>PLUGIN COMMANDS</code>).</dl>
<p> <code>-h, &#8211;help</code> [<i>TOPIC</i>]</p>
<dl>
<dt>
<dd> Print help TOPIC. <code>&#8211;help</code> <i>topics</i> will print a list of help topics, <code>&#8211;help</code> <i>syntax</i> summarizes AsciiDoc syntax, <code>&#8211;help</code> <i>manpage</i> prints the AsciiDoc manpage.</dl>
<p> <code>-e, &#8211;no-conf</code></p>
<dl>
<dt>
<dd> Exclude implicitly loaded configuration files except for those named like the input file (<i>infile.conf</i> and <i>infile-backend.conf</i>).</dl>
<p> <code>-s, &#8211;no-header-footer</code></p>
<dl>
<dt>
<dd> Suppress document header and footer output.</dl>
<p> <code>-o, &#8211;out-file</code>=<i>OUT_FILE</i></p>
<dl>
<dt>
<dd> Write output to file <i>OUT_FILE</i>. Defaults to the base name of input file with <i>backend</i> extension. If the input is stdin then the outfile defaults to stdout. If <i>OUT_FILE</i> is <i>&#8211;</i> then the standard output is used.</dl>
<p> <code>-n, &#8211;section-numbers</code></p>
<dl>
<dt>
<dd> Auto-number HTML article section titles. Synonym for <code>&#8211;attribute numbered</code>.</dl>
<p> <code>&#8211;safe</code></p>
<dl>
<dt>
<dd> Enable safe mode. Safe mode is disabled by default. AsciiDoc <i>safe mode</i> skips potentially dangerous scripted sections in AsciiDoc source files.</dl>
<p> <code>&#8211;theme</code>=<i>THEME</i></p>
<dl>
<dt>
<dd> Specify a theme name. Synonym for <code>&#8211;attribute theme</code>=<i>THEME</i>. The <code>&#8211;theme</code> option is also used to manage theme plugins (see <code>PLUGIN COMMANDS</code>).</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbosely print processing information and configuration file checks to stderr.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print program version number.</dl>
<h2>PLUGIN COMMANDS</h2>
<p> The <a href="/docs/linux/man/1-asciidoc/">asciidoc</a>(1) <code>&#8211;filter</code>, <code>&#8211;backend</code> and <code>&#8211;theme</code> options are used to install, remove and list AsciiDoc filter, backend and theme plugins. Syntax: </p>
<dl>
<dt>
<dd>
<pre><code>
asciidoc OPTION install ZIP_FILE[PLUGINS_DIR] asciidoc OPTION remove PLUGIN_NAME[PLUGINS_DIR] asciidoc OPTION list
    asciidoc OPTION build ZIP_FILE PLUGIN_SOURCE
</code></pre>
</dl>
<p> Where: </p>
<p> <code>OPTION</code></p>
<dl>
<dt>
<dd> <a href="/docs/linux/man/1-asciidoc/">asciidoc</a>(1) <code>&#8211;filter</code>, <code>&#8211;backend</code> or <code>&#8211;theme</code> option specifying the type of plugin.</dl>
<p> <code>PLUGIN_NAME</code></p>
<dl>
<dt>
<dd> A unique plugin name containing only alphanumeric or underscore characters.</dl>
<p> <code>ZIP_FILE</code></p>
<dl>
<dt>
<dd> A Zip file containing plugin resources, the name must start with the plugin name e.g. my_filter-1.0.zip packages filter my_filter.</dl>
<p> <code>PLUGINS_DIR</code></p>
<dl>
<dt>
<dd> The directory containing installed plugins. Each plugin is contained in its own separate subdirectory which has the same name as the plugin. <code>PLUGINS_DIR</code> defaults to the $HOME/.asciidoc/filters (for filter plugins) or $HOME/.asciidoc/backends (for backend plugins) or $HOME/.asciidoc/themes (for theme plugins).</dl>
<p> <code>PLUGIN_SOURCE</code></p>
<dl>
<dt>
<dd> The name of a directory containing the plugin source files or the name of a single source file.</dl>
<p> The plugin commands perform as follows: </p>
<p> <code>install</code></p>
<dl>
<dt>
<dd> Create a subdirectory in <code>PLUGINS_DIR</code> with the same name as the plugin then extract the <code>ZIP_FILE</code> into it.</dl>
<p> <code>remove</code></p>
<dl>
<dt>
<dd> Delete the <code>PLUGIN_NAME</code> plugin subdirectory and all its contents from the <code>PLUGINS_DIR</code>.</dl>
<p> <code>list</code></p>
<dl>
<dt>
<dd> List the names and locations of all installed filter or theme plugins (including standard plugins installed in the global configuration directory).</dl>
<p> <code>build</code></p>
<dl>
<dt>
<dd> Create a plugin file named <code>ZIP_FILE</code> containing the files and subdirectories specified by <code>PLUGIN_SOURCE</code>. File and directory names starting with a period are skipped.</dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failure (syntax or usage error; configuration error; document processing failure; unexpected error).</dl>
<h2>BUGS</h2>
<p> See the AsciiDoc distribution BUGS file.</p>
<h2>AUTHOR</h2>
<p> AsciiDoc was originally written by Stuart Rackham. Many people have contributed to it.</p>
<h2>RESOURCES</h2>
<p> SourceForge: <a rel="nofollow" href="http://sourceforge.net/projects/asciidoc/">http://sourceforge.net/projects/asciidoc/</a> </p>
<p> Main web site: <a rel="nofollow" href="http://www.methods.co.nz/asciidoc/">http://www.methods.co.nz/asciidoc/</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2002-2011 Stuart Rackham. Free use of this software is granted under the terms of the GNU General Public License (GPL). </p>
<h2>Index</h2>
