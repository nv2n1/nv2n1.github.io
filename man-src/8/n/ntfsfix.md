---
title: "ntfsfix(8)"
name: "ntfsfix"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsfix/"
description: "ntfsfix – fix common errors and force Windows to check NTFS"
---

<p>ntfsfix &#8211; fix common errors and force Windows to check NTFS</p>
<h2>Synopsis</h2>
<p><code>ntfsfix</code> [<i>options</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfsfix</code> is a utility that fixes some common NTFS problems. <code>ntfsfix</code> is <code>NOT</code> a Linux version of chkdsk. It only repairs some fundamental NTFS inconsistencies, resets the NTFS journal file and schedules an NTFS consistency check for the first boot into Windows. </p>
<p> You may run <code>ntfsfix</code> on an NTFS volume if you think it was damaged by Windows or some other way and it cannot be mounted.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsfix</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;clear-bad-sectors</code></p>
<dd>Clear the list of bad sectors. This is useful after cloning an old disk with bad sectors to a new disk.</p>
<dt><code>-d</code>, <code>&#8211;clear-dirty</code></p>
<dd>Clear the volume dirty flag if the volume can be fixed and mounted. If the option is not present or the volume cannot be fixed, the dirty volume flag is set to request a volume checking at next mount.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Do not write anything, just show what would have been done.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license</dl>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfsfix</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfsfix</code> was written by Anton Altaparmakov, with contributions from Szabolcs Szakacsits. It was ported to ntfs-3g by Erik Larsson and Jean-Pierre Andre.</p>
<h2>Availability</h2>
<p><code>ntfsfix</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkntfs/">mkntfs</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
