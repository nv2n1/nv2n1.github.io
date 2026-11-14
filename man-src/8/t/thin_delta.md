---
title: "thin_delta(8)"
name: "thin_delta"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_delta/"
description: "thin_delta – Print the differences in the mappings between two thin devices."
---

<p><code>thin_delta </code>&#8211; Print the differences in the mappings between two thin devices.</p>
<h2>Synopsis</h2>
<pre><code>thin_delta</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>thin_delta</code> allows you to compare the mappings in two thin volumes (snapshots allow common blocks between thin volumes). </p>
<p> This tool cannot be run on live metadata unless the <code>&#8211;metadata-snap</code> option is used.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;thin1</code>, <code>&#8211;snap1</code> {natural}</p>
<dd>The numeric identifier for the first thin volume to diff.</p>
<dt><code>&#8211;thin2</code>, <code>&#8211;snap2</code> {natural}</p>
<dd>The numeric identifier for the second thin volume to diff.</p>
<dt><code>&#8211;metadata-snap</code> [block nr]</p>
<dd>Use a metadata snapshot.</dl>
<pre> If you want to get information out of a live pool then you will need to
 take a metadata snapshot and use this switch. In order for the information
 to be meaningful, you need to ensure the thin volumes you're examining are
 not changing (ie, do not activate those thins).</pre>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd>Provide extra information on the mappings.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output version information and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;heinzm [at] redhat.com&gt;</p>
