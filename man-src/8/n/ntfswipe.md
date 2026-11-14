---
title: "ntfswipe(8)"
name: "ntfswipe"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfswipe/"
description: "ntfswipe – overwrite unused space on an NTFS volume"
---

<p>ntfswipe &#8211; overwrite unused space on an NTFS volume</p>
<h2>Synopsis</h2>
<p><code>ntfswipe</code> [<i>options</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfswipe</code> clears all or part of unused space on an NTFS volume by overwriting with zeroes or random bytes.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfswipe</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>Wipe all unused space. This may take significant time. If the option &#8211;unused-fast (or -U) is also present, the faster wiping method is used.</p>
<dt><code>-b</code>, <code>&#8211;bytes</code> BYTE-LIST</p>
<dd>Define the allowed replacement bytes which are drawn randomly to overwrite the unused space. BYTE-LIST is a comma-separated list of values in range 0-255 expressed in octal, decimal or hexadecimal base.</p>
<dt><code>-c</code>, <code>&#8211;count</code> NUM</p>
<dd>Define the number of times the unused space is to be overwritten. If both options <code>&#8211;bytes</code> and <code>&#8211;count</code> are set, the space is repeatedly overwritten this number of times by each of the values in the list.</p>
<dt><code>-d</code>, <code>&#8211;directory</code></p>
<dd>Wipe all the directory indexes, which may contain names of deleted files.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not using a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd>Display details about unused space, without wiping anything.</p>
<dt><code>-l</code>, <code>&#8211;logfile</code></p>
<dd>Overwrite the logfile (update journal).</p>
<dt><code>-m</code>, <code>&#8211;mft</code></p>
<dd>Overwrite the unused space in the MFT (main file table, which contains the file names, and the contents of short files).</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Executes the wiping process without writing to device.</p>
<dt><code>-p</code>, <code>&#8211;pagefile</code></p>
<dd>Overwrite the Windows swap space.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-s</code>, <code>&#8211;undel</code></p>
<dd>Overwrite the space which had been allocated to a file which has been deleted recently and is still undeletable. This option is not compatible with <code>&#8211;bytes</code> and the replacement bytes are random ones or taken from a standard list.</p>
<dt><code>-t</code>, <code>&#8211;tails</code></p>
<dd>Overwrite the space at the end of files which is unused, but allocated because the allocations are always done by full clusters.</p>
<dt><code>-u</code>, <code>&#8211;unused</code></p>
<dd>Overwrite the space which is currently not allocated to any file (but may have been used in the past).</p>
<dt><code>-U</code>, <code>&#8211;unused-fast</code></p>
<dd>Overwrite the space which is currently not allocated to any file, trying not to overwrite the space not written to since the previous wiping.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages. This option may be used twice to display even more messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license of <code>ntfswipe</code>.</dl>
<h2>Examples</h2>
<p>Wipe out all unused space in an NTFS volume.</p>
<dl>
<dd><code>ntfswipe -a /dev/sda1</code></dl>
<p> Wipe out all deleted file names from an NTFS volume.</p>
<dl>
<dd><code>ntfswipe -dms /dev/sda1</code> </p>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfswipe</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfswipe</code> was written by Richard Russon, Anton Altaparmakov and Yura Pakhuchiy. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Availability</h2>
<p><code>ntfswipe</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8), <code><a href="/docs/linux/man/8-ntfsls/">ntfsls</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
