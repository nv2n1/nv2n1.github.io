---
title: "ntfscluster(8)"
name: "ntfscluster"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfscluster/"
description: "ntfscluster – identify files in a specified region of an NTFS volume."
---

<p>ntfscluster &#8211; identify files in a specified region of an NTFS volume.</p>
<h2>Synopsis</h2>
<p><code>ntfscluster</code> [<i>options</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfscluster</code> has three modes of operation: <i>info</i>, <i>sector</i> and <i>cluster</i>.</p>
<h3>Info</h3>
<p>The default mode, <i>info</i> is currently not implemented. It will display general information about the NTFS volume when it is working.</p>
<h3>Sector</h3>
<p>The <i>sector</i> mode will display a list of files that have data in the specified range of sectors.</p>
<h3>Cluster</h3>
<p>The <i>cluster</i> mode will display a list of files that have data in the specified range of clusters. When the cluster size is one sector, this will be equivalent to the <i>sector</i> mode of operation.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfscluster</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;cluster</code> RANGE</p>
<dd>Any files whose data is in this range of clusters will be displayed.</p>
<dt><code>-F</code>, <code>&#8211;filename</code> NAME</p>
<dd>Show information about this file.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not working with a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-I</code>, <code>&#8211;inode</code> NUM</p>
<dd>Show information about this inode.</p>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd>This option is not yet implemented.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Reduce the amount of output to a minimum. Naturally, it doesn&#8217;t make sense to combine this option with <code>&#8211;verbose</code></p>
<dt><code>-s</code>, <code>&#8211;sector</code> RANGE</p>
<dd>Any files whose data is in this range of sectors will be displayed.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase the amount of output that <code>ntfscluster</code> prints.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license for <code>ntfscluster</code>.</dl>
<h2>Examples</h2>
<p>Get some information about the volume /dev/hda1.</p>
<dl>
<dd><code>ntfscluster /dev/hda1</code></dl>
<p> Look for files in the first 500 clusters of /dev/hda1.</p>
<dl>
<dd><code>ntfscluster -c 0-500 /dev/hda1</code> </p>
<h2>Bugs</h2>
<p>The <i>info</i> mode isn&#8217;t implemented yet. <code>ntfscluster</code> is quite limited, but it has no known bugs. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfscluster</code> was written by Richard Russon, with contributions from Anton Altaparmakov. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Availability</h2>
<p><code>ntfscluster</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsinfo/">ntfsinfo</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
