---
title: "lintian-lab-tool(1)"
name: "lintian-lab-tool"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lintian-lab-tool/"
description: "lintian-lab-tool – perform common operations on/involving laboratories"
---

<h2 class="name">NAME</h2>
<p> lintian-lab-tool &#8211; perform common operations on/involving laboratories </p>
<h2>SYNOPSIS</h2>
<p> <code>lintian-lab-tool</code> &lt;cmd&gt; &lt;lab&gt; [&#8230;] </p>
<p> <code>lintian-lab-tool</code> help</p>
<h2>DESCRIPTION</h2>
<p> The <code>lintian-lab-tool</code> &#8230;</p>
<h2>OPERATIONS</h2>
<dl>
<dt><code>create-lab</code> <i>laboratory-dir</i></p>
<dd> Creates a new permanent Lintian laboratory in the directory denoted by <code>laboratory-dir</code>.</p>
<dt><code>help</code> [<i>cmd</i>]</p>
<dd> Display the synopsis of this tool or one of its operations.</p>
<dt><code>remove-lab</code> <i>laboratory-dir</i></p>
<dd> Removes a permanent Lintian laboratory in the directory denoted by <code>laboratory-dir</code>.</p>
<dt><code>remove-pkgs</code> <i>laboratory-dir</i> <i>query</i> [&#8230; <i>query</i>]</p>
<dd> Removes all packages matching the given <i>queries</i> from the permanent Lintian laboratory denoted by <code>laboratory-dir</code>.</p>
<dt><code>scrub-lab</code> <i>laboratory-dir</i></p>
<dd> Attempt to fix common metadata issues in an existing laboratory. </p>
<p> This command can correct <i>some</i> corruptions caused by programs that failed to synchronize the laboratory metadata with the actual contents. Almost all corrections involve discarding corrupted entries. </p>
<p> These issues usually occur because:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Two processes update the laboratory concurrently.</p>
<dt>&bull;</p>
<dd> A process updated the laboratory but was killed / crashed before it properly close the laboratory.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note that Lintian tools will fix these issues automatically as the tools happen to run into the issues.</dl>
</dl>
<h2>CAVEAT</h2>
<p> Laboratories are not designed to have multiple processes working on them concurrently.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lintian/">lintian</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> Niels Thykier &lt;niels [at] thykier.net&gt; </p>
<p> Richard Braakman &lt;dark [at] xs4all.nl&gt; </p>
<p> Christian Schwarz &lt;schwarz [at] monet.m.isar.de&gt; </p>
<h2>Index</h2>
