---
title: "casper-snapshot(1)"
name: "casper-snapshot"
section: "1"
letter: "c"
url: "/docs/linux/man/1-casper-snapshot/"
description: "casper-snapshot – a simple script to ease persistence usage."
---

<h2 class="name">NAME</h2>
<p> casper-snapshot &#8211; a simple script to ease persistence usage.</p>
<h2>SYNOPSIS</h2>
<p> <code>casper-snapshot</code> [<code>-c</code>|<code>&#8211;cow</code> <i>DIRECTORY</i>] [<code>-d</code>|<code>&#8211;device</code> <i>DEVICE</i>] [<code>-e</code>|<code>&#8211;exclude-list</code> <i>FILE</i>] [<code>-o</code>|<code>&#8211;output</code> <i>FILE</i>] [<code>-t</code>|<code>&#8211;type</code> <i>TYPE</i>] </p>
<p> <code>casper-snapshot</code> -r<code>|</code>&#8211;resync-string <i>STRING</i><br />
 <code>casper-snapshot</code> -h<code>|</code>&#8211;help<br />
 <code>casper-snapshot</code> -u<code>|</code>&#8211;usage<br />
 <code>casper-snapshot</code> -v<code>|</code>&#8211;version </p>
<h2>DESCRIPTION</h2>
<p> Casper-snapshot is a script which can be used to build the right types of persistent image files supported by casper. It is also used on exit by the casper init script to resync the boot-found snapshots devices. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c, &#8211;cow</code><i> DIRECTORY</i></p>
<dd> specifies the input directory to be cloned in the image file. Its default value &quot;/cow&quot; should be right for most uses. However it could be handy to specify &quot;/home&quot; and type ext2 for the type to prepare an image file suited to be directly mounted by casper as home.</p>
<dt><code>-d, &#8211;device</code><i> DEVICE</i></p>
<dd> sets the device where the media which the snapshot/persistence file/partition will be put. If it is not specified, a tmpfs will be used and linked to the user&#8217;s desktop to move it where it is needed. If the device has no filesystem, an ext2 fs will be automatically created and labelled according to the values specified after the &quot;&#8211;output&quot; value or with a sane default.</p>
<dt><code>-e, &#8211;exclude-list</code><i> FILE</i></p>
<dd> a file containing a list of filenames/paths that should not be saved. This exclude list will be remebered on the target snapshot media for reuse.</p>
<dt><code>-o, &#8211;output</code><i> FILE</i></p>
<dd> the filename/label used for the output file/partition. If left blank, casper-snapshot will search for a proper file on the device or use the whole partition.</p>
<dt><code>-r, &#8211;resync-string</code><i> STRING</i></p>
<dd> internally used on resyncs.</p>
<dt><code>-t, &#8211;type</code><i> TYPE</i></p>
<dd> Type could be one of &quot;cpio&quot;, &quot;squashfs&quot; or &quot;ext2&quot;. </p>
</dl>
<h2>BUGS</h2>
<p> <code>casper-snapshot</code> Time (and BTS) will tell. </p>
<h2>HOMEPAGE</h2>
<p> Debian Live project &lt;<a rel="nofollow" href="http://live.debian.net/">http://live.debian.net/</a>&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-casper/">casper</a>(7)</code> </p>
<h2>AUTHOR</h2>
<p> casper-snapshot was written Marco Amadori &lt;marco.amadori [at] gmail.com&gt;.</p>
<dl>
<dt>This manual page was written by Marco Amadori &lt;marco.amadori [at] gmail.com&gt;,</p>
<dd> for the Debian project (but may be used by others). </p>
</dl>
<h2>Index</h2>
