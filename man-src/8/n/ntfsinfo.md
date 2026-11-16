---
title: "ntfsinfo(8)"
name: "ntfsinfo"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsinfo/"
description: "ntfsinfo – dump a file’s attributes"
---

<p>ntfsinfo &#8211; dump a file&#8217;s attributes</p>
<h2>Synopsis</h2>
<p><code>ntfsinfo</code> [<i>options</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfsinfo</code> will dump the attributes of inode <i>inode-number</i> or the file <i>path-filename</i> and/or information about the mft ( <i>-m</i> option). Run ntfsinfo without arguments for a full list of options.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsinfo</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-F</code>, <code>&#8211;file</code> FILE</dt>
<dd>Show information about this file</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd>This will override some sensible defaults, such as not overwriting an existing file. Use this option with caution.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Show a list of options with a brief description of each one.</dd>
<dt><code>-i</code>, <code>&#8211;inode</code> NUM</dt>
<dd>Show information about this inode.</dd>
<dt><code>-m</code>, <code>&#8211;mft</code></dt>
<dd>Show information about the volume.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd>Produce less output.</dd>
<dt><code>-t</code>, <code>&#8211;notime</code></dt>
<dd>Do not display timestamps in the output.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>Increase the amount of output that <code>ntfsinfo</code> prints.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Show the version number, copyright and license.</dd></dl>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfsinfo</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfsinfo</code> was written by Matthew J. Fanto, Anton Altaparmakov, Richard Russon, Szabolcs Szakacsits, Yuval Fledel, Yura Pakhuchiy and Cristian Klein. It was ported to ntfs-3g by Erik Larsson and Jean-Pierre Andre.</p>
<h2>Availability</h2>
<p><code>ntfsinfo</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
