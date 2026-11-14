---
title: "ntfslabel(8)"
name: "ntfslabel"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfslabel/"
description: "ntfslabel – display/change the label on an ntfs file system"
---

<p>ntfslabel &#8211; display/change the label on an ntfs file system</p>
<h2>Synopsis</h2>
<p><code>ntfslabel</code> [<i>options</i>] <i>device </i>[<i>new-label</i>]</p>
<h2>Description</h2>
<p><code>ntfslabel</code> will display or change the file system label on the ntfs file system located on <i>device</i>. It can also change the serial number of the <i>device</i>. </p>
<p> If the optional argument <i>new-label</i> is not present, and no option is present, <code>ntfslabel</code> will simply display the current file system label. </p>
<p> If the optional argument <i>new-label</i> is present, then <code>ntfslabel</code> will set the file system label to be <i>new-label</i>. NTFS file system labels can be at most 128 Unicode characters long; if <i>new-label</i> is longer than 128 Unicode characters, <code>ntfslabel</code> will truncate it and print a warning message. </p>
<p> It is also possible to set the file system label using the <code>-L</code> option of <code><a href="/docs/linux/man/8-mkntfs/">mkntfs</a></code>(8) during creation of the file system.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfslabel</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not working with a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>&#8211;new-serial</code>[<i>=ssssssssssssssss</i>], or</p>
<dd>
<dt><code>&#8211;new-half-serial</code>[<i>=ssssssss</i>]</p>
<dd>Set a new serial number to the device, either the argument value, or a random one if no argument is given. The serial number is a 64 bit number, represented as a sixteen-digit hexadecimal number, used to identify the device during the mounting process. As a consequence, two devices with the same serial number cannot be mounted at the same time on the same computer. This is not the volume UUID used by Windows to locate files which have been moved to another volume. </p>
<p> The option &#8211;new-half-serial only changes the upper part of the serial number, keeping the lower part which is used by Windows unchanged. In this case the optional argument is an eight-digit hexadecimal number. </p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Don&#8217;t actually write to disk.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Reduce the amount of output to a minimum.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase the amount of output that <code>ntfslabel</code> prints. The label and the serial number are displayed.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license for <code>ntfslabel</code>.</dl>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfslabel</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfslabel</code> was written by Matthew J. Fanto, with contributions from Anton Altaparmakov and Richard Russon. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Availability</h2>
<p><code>ntfslabel</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkntfs/">mkntfs</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
