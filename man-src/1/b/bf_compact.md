---
title: "bf_compact(1)"
name: "bf_compact"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bf_compact/"
description: "bf_compact – shell script to compact a bogofilter directory"
---

<h2 class="name">NAME</h2>
<p> bf_compact &#8211; shell script to compact a bogofilter directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bf_compact</code> <i>bogofilter_directory</i> [<i>wordlist_name</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>bf_compact</code></p>
<dd>creates a more compact bogofilter working directory with a dump/load cycle and renames the previous <i>bogofilter_directory</i> to <i>bogofilter_directory</i>.old. </p>
<p> Note: <code>bf_compact</code> cannot be used to process the current working directory, &quot;.&quot;, because that cannot be renamed. </p>
<p> If no <i>wordlist_file</i> arguments are given, then <code>bf_compact</code> will use the configured set of wordlists, if the given <i>bogofilter_directory</i> is the same as the configured, or use all *.db files if it is a different directory.</p>
<h2>EXIT STATUS</h2>
<p> The script exits with status code 0 if everything went well, and nonzero if it encountered trouble.</p>
<h2>NOTES</h2>
<p> This script will delete <i>bogofilter_directory</i>.old and all of its contents! </p>
<p> This script expects a SUSv2 compliant shell. Solaris systems should have the SUNWxcu4 package installed (when bogofilter is configured) so that /usr/xpg4/bin/sh can be used.</p>
<h2>AUTHORS</h2>
<p> Matthias Andree </p>
<h2>Index</h2>
