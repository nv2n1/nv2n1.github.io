---
title: "svgakeymap(1)"
name: "svgakeymap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-svgakeymap/"
description: "svgakeymap – generates keymaps for svgalib"
---

<h2>NAME</h2>
<p> svgakeymap &#8211; generates keymaps for svgalib </p>
<h2>SYNOPSIS</h2>
<p> <code>svgakeymap [</code><i>physical_table</i><code> [</code><i>program_table</i><code>]] &gt; </code><i>output.keymap</i> </p>
<h2>DESCRIPTION</h2>
<p> Generates a keymap conversion file for <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7) from two keytable definitions. Keytables are searched for in <i>/lib/kbd/keymaps</i> and are automatically filtered through <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) if necessary. </p>
<p> If only one keytable is specified, a keymap is generated that performs no conversion but contains the proper key names for that layout. If no keytables are specified, the standard US QWERTY keyboard is used. </p>
<p> The generated keymap is sent to the standard output and may be redirected or piped in any creative manner you wish. </p>
<h2>FILES</h2>
<p> <i>/lib/kbd/keymaps/*/*/*.map[.gz]</i></p>
<dl>
<dt>
<dd> The system keytable files used by <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1).</dl>
<h2>BUGS</h2>
<p> Can get confused if there is more than one key with a given name or if names do not match properly between keytables. Keymaps may require manual editing. </p>
<h2>AUTHOR</h2>
<p> Brion Vibber &lt;brion [at] pobox.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5) </p>
<p> <i>README.keymap</i> from the svgalib distribution </p>
<h2>Index</h2>
