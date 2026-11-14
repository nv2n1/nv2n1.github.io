---
title: "bximage(1)"
name: "bximage"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bximage/"
description: "bximage – Interactive Disk Image Creator for Bochs"
---

<h2 class="name">NAME</h2>
<p> bximage &#8211; Interactive Disk Image Creator for Bochs </p>
<h2>SYNOPSIS</h2>
<p> <code>bximage</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> Bximage is an easy to use console based tool for creating disk images, particularly for use with Bochs. It is completely interactive if no command line arguments are used. It can be switched to a non-interactive mode if all required parameters are given in the command line.</p>
<h2>OPTIONS</h2>
<p> When you run bximage without one of the following options, it will appear in interactive mode and ask for all required parameters to create an image.</p>
<dl>
<dt><code>-fd</code></p>
<dd> Create a floppy image.</p>
<dt><code>-hd</code></p>
<dd> Create a hard disk image.</p>
<dt><code>-mode=&#8230;</code></p>
<dd> Image mode (for hard disks only &#8211; see the <i>bochsrc</i> sample for supported options).</p>
<dt><code>-size=&#8230;</code></p>
<dd> Image size in megabytes (e.g. 1.44 for floppy image, 10 for hard disk image).</p>
<dt><code>-q</code></p>
<dd> Quiet mode (don&#8217;t prompt for user input). Without this option bximage uses the command line parameters as defaults for the interactive mode. If this option is given and one of the required parameters is missing, bximage will fall back to interactive mode.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the command line options for bximage and exit.</dl>
<p> The <i>filename</i> parameter specifies the name of the image to be created.</p>
<h2>LICENSE</h2>
<p> This program is distributed under the terms of the GNU Lesser General Public License as published by the Free Software Foundation. See the COPYING file located in /usr/share/doc/bochs-2.3.8/ for details on the license and the lack of warranty.</p>
<h2>AVAILABILITY</h2>
<p> The latest version of this program can be found at:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://bochs.sourceforge.net/getcurrent.html">http://bochs.sourceforge.net/getcurrent.html</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bochs/">bochs</a>(1), <a href="/docs/linux/man/5-bochsrc/">bochsrc</a>(5), <a href="/docs/linux/man/1-bochs-dlx/">bochs-dlx</a>(1), <a href="/docs/linux/man/1-bxcommit/">bxcommit</a>(1) </p>
<pre>
The Bochs IA-32 Emulator site on the World Wide Web:
  <a rel="nofollow" href="http://bochs.sourceforge.net">http://bochs.sourceforge.net</a>
Online Bochs Documentation
        <a rel="nofollow" href="http://bochs.sourceforge.net/doc/docbook">http://bochs.sourceforge.net/doc/docbook</a>
</pre>
<h2>AUTHORS</h2>
<p> Bximage was written by Bryce Denney, based on several similar tools from the bochs-developers list.</p>
<h2>BUGS</h2>
<p> Please report all bugs to the bug tracker on our web site. Just go to <a rel="nofollow" href="http://bochs.sourceforge.net,">http://bochs.sourceforge.net,</a> and click &quot;Bug Reports&quot; on the sidebar under &quot;Feedback.&quot; </p>
<p> Provide a detailed description of the bug, the version of the program you are running, the operating system you are running the program on and the operating system you are running in the emulator. </p>
<h2>Index</h2>
