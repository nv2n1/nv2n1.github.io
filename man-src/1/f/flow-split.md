---
title: "flow-split(1)"
name: "flow-split"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-split/"
description: "flow-split – Split flow files into smaller files."
---

<h2>NAME</h2>
<p> flow-split &#8211; Split flow files into smaller files.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-split</code> [ <code>-gGhn</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-N</code><i> nflows</i> ] [ <code>-o</code><i> outfile_basename</i> ] [ <code>-T</code><i> nseconds</i> ] [ <code>-z</code><i> z_level</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-split</code> utility will split a flow file into smaller files based on the the number of flows or the ammount of time that has passed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></dt>
<dd> Byte order of output.</dd>
<dt><code>-C</code><i> Comment</i></dt>
<dd> Add a comment.</dd>
<dt><code>-d</code><i> debug_level</i></dt>
<dd> Enable debugging.</dd>
<dt><code>-g</code></dt>
<dd> Split on source tag.</dd>
<dt><code>-G</code></dt>
<dd> Split on destination tag.</dd>
<dt><code>-h</code></dt>
<dd> Display help.</dd>
<dt><code>-n</code></dt>
<dd> Use symbols for tag field in filename.</dd>
<dt><code>-N</code><i> nflows</i></dt>
<dd> Split after processing <i>nflows</i>.</dd>
<dt><code>-o</code><i> outfile_basename</i></dt>
<dd> The basename of the resulting files.</dd>
<dt><code>-T</code><i> nsecond</i></dt>
<dd> Split after processing an interval of <i>nseconds</i> flows.</dd>
<dt><code>-z</code><i> z_level</i></dt>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dd></dl>
<h2>EXAMPLES</h2>
<p> Create 1 minute flow files from the flow archive in <i>/flows/krc4</i>. Store the results in <i>/flows/krc4.split</i> </p>
<p> <code>flow-cat /flows/krc4 | flow-split -T60 -o /flows/krc4.split/1min</code>.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
