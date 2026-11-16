---
title: "ezstream-file-sh(1)"
name: "ezstream-file-sh"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ezstream-file-sh/"
description: "ezstream-file.sh – script to stream files from the command line"
---

<p><code>ezstream-file.sh</code> &#8211; script to stream files from the command line </p>
<h2>Synopsis</h2>
<p>-words [-<code>hmnqVv </code>[-<code>T </code><i>cfg_template</i> ] ] [<i>file &#8230;</i> ]</p>
<h2>Description</h2>
<p>The script uses an <code>ezstream</code> configuration file template to stream a list of files given on the command line, or via standard input. In other words, filenames are written to a temporary playlist, and a template-based configuration is generated to stream them. </p>
<p> The path to a configuration template must be provided, either by using the &#8211;<code>T</code> command line argument, or the <code>EZSTREAM_TEMPLATE</code> environment variable. </p>
<p> The configuration template must be a valid playlist configuration, and contain the follwing configuration statement: </p>
<blockquote>
<pre>&lt;filename&gt;%FILENAME%&lt;/filename&gt;</pre>
</blockquote>
<p> If no input files are specified, the list of files to be streamed are read from standard input. </p>
<p> Lastly, the <code>EZSTREAM</code> environment variable allows to specify an alternate <code>ezstream</code> binary.</p>
<h3>Command line parameters</h3>
<dl>
<dt><code>-h</code></dt>
<dd>Print a summary of available command line parameters with short descriptions and exit.</dd>
<dt><code>-m</code></dt>
<dd>Po Passed to <code>ezstream</code> Pc Disable all metadata updates and keep existing metadata in streams untouched.</dd>
<dt><code>-n</code></dt>
<dd>Po Passed to <code>ezstream</code> Pc Normalize metadata strings by removing excess whitespaces.</dd>
<dt><code>-q</code></dt>
<dd>Po Passed to <code>ezstream</code> Pc Be more quiet. Suppress the output that external programs send to standard error.</dd>
<dt><code>-T </code><i>cfg_template</i></dt>
<dd>Use the configuration in <i>cfg_template</i> overriding the default set in the <code>EZSTREAM_TEMPLATE</code> environment variable.</dd>
<dt><code>-V</code></dt>
<dd>Print the version number and exit.</dd>
<dt><code>-v</code></dt>
<dd>Po Passed to <code>ezstream</code> Pc Produce more verbose output from <code>ezstream</code> Use twice for even more verbose output.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/usr/share/examples/ezstream </code></dt>
<dd>Directory containing example configuration files for various uses of <code>ezstream</code> as well as example playlist and metadata scripts.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ezstream/">ezstream</a>(1)</p>
<h2>Authors</h2>
<p>An -nosplit The script and this manual were written by An Moritz Grimm .</p>
