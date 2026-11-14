---
title: "bf_copy(1)"
name: "bf_copy"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bf_copy/"
description: "bf_copy – shell script to copy a bogofilter working directory"
---

<h2 class="name">NAME</h2>
<p> bf_copy &#8211; shell script to copy a bogofilter working directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bf_copy</code> [-c] <i>source_dir</i> <i>destination_dir</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>bf_copy</code></p>
<dd>copies a bogofilter working directory to another directory. Currently it copies the database files (*.db), related files (log.*), and DB_CONFIG (if present).</p>
<h2>OPTIONS</h2>
<p> The <code>-c</code> option causes only active log files to be copied, not all. The default is to copy all log files.</p>
<h2>EXIT STATUS</h2>
<p> The script exits with status code 0 if everything went well, and nonzero if it encountered trouble.</p>
<h2>BUGS</h2>
<p> This script assumes all *.db files in the source directory are relevant and copies them. This may not match your actual configuration.</p>
<h2>NOTES</h2>
<p> This script is meant for use with Berkeley DB and SQLite based bogofilter versions. </p>
<p> This script expects a SUSv2 compliant shell. Solaris systems should have the SUNWxcu4 package installed (when bogofilter is configured) so that /usr/xpg4/bin/sh can be used.</p>
<h2>AUTHORS</h2>
<p> Matthias Andree </p>
<h2>Index</h2>
