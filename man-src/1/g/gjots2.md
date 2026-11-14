---
title: "gjots2(1)"
name: "gjots2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjots2/"
description: "gjots2 – A gnome-2/X11 jotter"
---

<h2>NAME</h2>
<p> gjots2 &#8211; A gnome-2/X11 jotter</p>
<h2>SYNOPSIS</h2>
<p> <code>gjots2</code> [<code>options</code>] <i>gjotsfile </i></p>
<h2>DESCRIPTION</h2>
<p> <code>gjots2</code> is a fairly simple jotter application for your desktop. It displays your data organised in a tree with each leaf being your text. Getting data into <code>gjots2</code> is fairly easy &#8211; you can type it in, cut and paste text or use an editor to convert other text files to the simple <code>gjots2</code> format (see below for details). You can also convert an existing DOCBOOK file into <code>gjots2</code> format with <code><a href="/docs/linux/man/1-docbook2gjots/">docbook2gjots</a></code>(1). <code>gjots2</code> files can be simply converted into HTML using <code><a href="/docs/linux/man/1-gjots2html/">gjots2html</a></code>(1) or into DOCBOOK with <code><a href="/docs/linux/man/1-gjots2docbook/">gjots2docbook</a></code>(1) Sensitive data can be encrypted by <code><a href="/docs/linux/man/1-ccrypt/">ccrypt</a></code>(1), <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1) or <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) simply by saving with an appropriate file suffix and providing a password:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ccrypt</code></p>
<dd>
&nbsp;<wbr>.cpt</p>
<dt><code>openssl</code></p>
<dd>
&nbsp;<wbr>.ssl</p>
<dt><code>gpg</code></p>
<dd>
&nbsp;<wbr>.gpg</dl>
</dl>
<p> Don&#8217;t forget your passwords. Obviously, the appropriate encryption utility must have been installed. Simple text formatting is provided with the usual cut &amp; paste operations and paragraph formatting (line wrapping) according to the line length set in <i>Settings-&gt;Preferences.</i> Lines are formatted by pressing the <i>Wrap</i> button or ^L. This requires the <code><a href="/docs/linux/man/1-fmt/">fmt</a></code>(1) command which is in the <i>sys-apps/textutils</i> pacakge (on <code>Gentoo</code>). An external editor (configured in <i>Settings-&gt;Preferences</i>) can be invoked by pressing the <code>Ext.Ed</code> button. <code>gjots2</code> is suspended while the editing is carried on. File locking is implemented by a lockfile (<i>.#filename</i>) in the same directory as the file being edited. Multiple users can open the file readonly but only one user can open the file for writing. Since the locking is done with a lockfile even NFS-mounted files can be protected.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Prints help.</p>
<dt><code>-g</code>, <code>&#8211;geometry</code> <i>WIDTHxHEIGHT</i>[<i>+X+Y</i>]</p>
<dd> Initial window geometry for <code>gjots2.</code> Note that the X and Y components are presently ignored.</p>
<dt><code>-p</code>, <code>&#8211;purge-password</code></p>
<dd> When opening an encrypted file, <code>gjots</code> now remembers the password for subsequent writes. To restore the old behaviour where <code>gjots</code> purged the password, use this option.</p>
<dt><code>-r</code>, <code>&#8211;readonly</code></p>
<dd> Opens the gjotsfile in readonly mode (with no locking and no ability to write)</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Produces a trace of program execution possiby useful in debugging</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version and quit</dl>
<h2>FILES</h2>
<p> <code>$HOME/.gjotsfile</code> The default data file</p>
<dl>
<dt>`<code>dirname </code><i>filename</i>`<i>/.#</i>`<code>basename</code> <i>filename</i>`</p>
<dd> The lock file for the file called <i>filename</i>.</dl>
<h2>FILE FORMAT</h2>
<p> <code>gjots2</code> uses a simple text file format with the addition of a hierarchy of items introduced by keywords. The keywords need to be at the start of line to be recognised. Only 3 keywords are presently used:</p>
<dl>
<dt><code>\NewEntry</code></p>
<dd> Starts a new entry</p>
<dt><code>\NewFolder</code></p>
<dd> Promotes the current item to a folder</p>
<dt><code>\EndFolder</code></p>
<dd> Ends a folder The first line in every entry is used as the &#8216;title&#8217; for the tree. In a future release the <code>\Option</code> keyword may be added.</dl>
<h2>EXAMPLE</h2>
<pre>
\NewEntry 
title1
this is the stuff that goes into title1
\NewFolder
\NewEntry 
title3
title 3's stuff
\EndFolder
</pre>
<h2>AUTHOR</h2>
<p> Written by Bob Hepple &lt;bhepple [at] freeshell.org&gt; <a rel="nofollow" href="http://bhepple.freeshell.org/gjots">http://bhepple.freeshell.org/gjots</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002 Robert Hepple<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gjots2html/">gjots2html</a></code>(1), <code><a href="/docs/linux/man/1-gjots2docbook/">gjots2docbook</a></code>(1), <code><a href="/docs/linux/man/1-docbook2gjots/">docbook2gjots</a></code>(1). Also, see the <code><a href="/docs/linux/man/1-gjots2/">gjots2</a></code>(1) README, probably as something like:</p>
<dl>
<dt>
<dd>
<pre>
gjots /usr/share/doc/gjots-0.8/gjots2.gjots
</dl>
or
<dl><dt><dd>netscape /usr/share/doc/gjots-0.8/gjots2.html
</pre>
</dl>
<h2>Index</h2>
