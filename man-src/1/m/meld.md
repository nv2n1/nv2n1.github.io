---
title: "meld(1)"
name: "meld"
section: "1"
letter: "m"
url: "/docs/linux/man/1-meld/"
description: "meld – Visual diff and merge tool for the GNOME Desktop"
---

<h2 class="name">NAME</h2>
<p> <code>meld</code> &#8211; Visual diff and merge tool for the GNOME Desktop </p>
<h2>SYNOPSIS</h2>
<p> <code>meld</code> [options]<br />
 <code>meld</code> [options] FILE1<br />
 <code>meld</code> [options] DIR1<br />
 <code>meld</code> [options] FILE1 FILE2 [FILE3]<br />
 <code>meld</code> [options] DIR1 DIR2 [DIR3]</p>
<h2>DESCRIPTION</h2>
<p> <code>Meld</code> is a graphical diff viewer and merge application for the GNOME desktop. It supports 2 and 3-file diffs, recursive directory diffs, diffing of directories under version control (Bazaar, CVS, Darcs, Fossil, Git, Mercurial, Monotone), as well as the ability to manually and automatically merge file differences.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;auto-compare, -a</code></p>
<dd>
 Automatically compare all differing files on startup.</p>
<dt><code>&#8211;auto-merge</code></p>
<dd>
 Automatically merge files</p>
<dt><code>&#8211;comparison-file=&lt;file&gt;</code></p>
<dd>
 Load a saved comparison from a Meld comparison file</p>
<dt><code>&#8211;diff FILE1|DIR1 FILE2|DIR2 [FILE3|DIR3]</code></p>
<dd>
 Create a diff tab for the given files or directories. Note that &quot;<code>meld</code> &#8211;diff FILE1 FILE2&quot; is functionally equivalent to &quot;<code>meld</code> FILE1 FILE2&quot;. However, the <code>&#8211;diff</code> argument can be given multiple times for one invocation of <code>meld</code> which allows the user to automatically initiate multiple diffs when <code>meld</code> starts. See examples below.</p>
<dt><code>&#8211;help, -h</code></p>
<dd>
 Print application help and usage.</p>
<dt><code>&#8211;label=&lt;label&gt;, -L &lt;label&gt;</code></p>
<dd>
 Set application window title to &lt;label&gt;.</p>
<dt><code>&#8211;newtab, -n</code></p>
<dd>
 Open the comparison as a new tab in an already-running instance.</p>
<dt><code>&#8211;output, -o</code></p>
<dd>
 Sets the save path for the middle buffer in a three-pane merge view. This is useful for loading the middle buffer from one file and saving it to another, for example in use as a version control merge helper.</p>
<dt><code>&#8211;unified, -u</code></p>
<dd>
 Ignored for compatibility</p>
<dt><code>&#8211;version</code></p>
<dd>
 Print application version and exit.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>meld</code></p>
<dd>
 Run <code>meld</code> without initiating a diff.</p>
<dt><code>meld</code> FILE1</p>
<dd>
 Initiate a diff between FILE1 and the version-controlled copy of FILE1.</p>
<dt><code>meld</code> DIR1</p>
<dd>
 Initiate a recursive diff between DIR1 and the version-controlled copy of DIR1.</p>
<dt><code>meld</code> FILE1 FILE2</p>
<dd>
 Initiate a diff between FILE1 and FILE2.</p>
<dt><code>meld</code> FILE1 FILE2 FILE3</p>
<dd>
 Initiate a 3-way diff between FILE1, FILE2, and FILE3.</p>
<dt><code>meld</code> DIR1 DIR2</p>
<dd>
 Initiate a recursive diff between directory DIR1 and DIR2.</p>
<dt><code>meld</code> DIR1 DIR2 DIR3</p>
<dd>
 Initiate a recursive 3-way diff between directory DIR1, DIR2, and DIR3.</p>
<dt><code>meld</code> &#8211;diff FILE1 FILE2 &#8211;diff FILE3 FILE4</p>
<dd>
 Initiate a diff between FILE1 and FILE2, and a separate diff between FILE3 and FILE4.</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://gitlab.gnome.org/GNOME/meld/issues">https://gitlab.gnome.org/GNOME/meld/issues</a> or mail a description of the issue to meld-list [at] gnome.org.</p>
<h2>AUTHORS</h2>
<p> See the AUTHORS text file in <code>meld&#8217;s</code> source code (<a rel="nofollow" href="http://git.gnome.org/browse/meld/tree/AUTHORS">http://git.gnome.org/browse/meld/tree/AUTHORS</a>). </p>
<h2>Index</h2>
