---
title: "bakefile_gen(1)"
name: "bakefile_gen"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bakefile_gen/"
description: "bakefile_gen – batch bakefile generation"
---

<h2 class="name">NAME</h2>
<p> bakefile_gen &#8211; batch bakefile generation </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bakefile_gen</code> [<code>-d</code><i>DESCFILE</i>&#8230;] [<code>-F</code><i>FORMATS</i>&#8230;] [<code>-D</code><i>VAR</i>=<i>VALUE</i>&#8230;] [<code>-I</code><i>PATH</i>&#8230;] [<code>-c</code>] [<code>&#8211;list-files</code>] [<code>-j</code>] [<code>-p</code>] [<code>&#8211;dry-run</code>] [<code>-k</code>] [<code>-n</code>] [<code>-v</code>] [<code>-V</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>Calls <code>bakefile</code> with flags listed in description file (Bakefiles.bkgen or file specified using the &#8211;desc option).</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> <code>&#8211;desc</code>=<i>DESCFILE</i></p>
<dl>
<dt>
<dd> Uses given description file instead of Bakefiles.bkgen.</dl>
<p> <code>&#8211;formats</code>=<i>FORMATS</i></p>
<dl>
<dt>
<dd> Calls Bakefile to generate only makefiles for specified formats. <i>FORMATS</i> is comma-separed list of format names. Formats not included in the list are ignored even if they are listed in &lt;add-formats&gt; tags in the description file.</dl>
<p> <code>&#8211;bakefiles</code>=<i>BAKEFILES</i></p>
<dl>
<dt>
<dd> Calls Bakefile to generate makefiles only from bakefiles that match any wildcard in comma-separed list of wildcards in <i>BAKEFILES</i>. Input files specified using the &lt;input&gt; tag in the description file that don&#8217;t match any of the wildcards are not processed.</dl>
<p> <code>-D</code><i>VAR</i>=<i>VALUE</i></p>
<dl>
<dt>
<dd> Pass variable definition to Bakefile, overriding any definition in description file or the input bakefile.</dl>
<p> <code>-I</code><i>PATH</i></p>
<dl>
<dt>
<dd> Add path to the list of directories where Bakefile looks for rules and output templates.</dl>
<p> <code>-c</code>, <code>&#8211;clean</code></p>
<dl>
<dt>
<dd> Removes all output files instead of generating them.</dl>
<p> <code>&#8211;list-files</code></p>
<dl>
<dt>
<dd> Prints the list of output files that would be generated instead of creating them. This command respects the constraints specified using the <code>&#8211;format</code> and <code>&#8211;bakefile</code> options. It can be used for example to create the list of all makefiles for given format.</dl>
<p> <code>-j</code>, <code>&#8211;jobs</code></p>
<dl>
<dt>
<dd> Number of jobs to run simultaneously. Default is the number of CPUs.</dl>
<p> <code>-p</code>, <code>&#8211;pretend</code></p>
<dl>
<dt>
<dd> Don&#8217;t do anything, only display actions that would be performed.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Process the bakefile normally, but instead of creating or modifying files, just print which files would be changed without actually modifying them.</dl>
<p> <code>-k</code>, <code>&#8211;keep-going</code></p>
<dl>
<dt>
<dd> Do not stop when a target fails.</dl>
<p> <code>-B</code>, <code>&#8211;always-make</code></p>
<dl>
<dt>
<dd> Pretend that all makefiles are out of date and regenerate all of them. <code>-f</code> and <code>-b</code> options are respected.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Display detailed information.</dl>
<p> <code>-V</code>, <code>&#8211;very-verbose</code></p>
<dl>
<dt>
<dd> Display even more detailed information.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display usage information for <code>bakefile_gen</code></dl>
<h2>Index</h2>
