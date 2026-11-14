---
title: "bochs(1)"
name: "bochs"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bochs/"
description: "bochs – Portable x86 Emulator."
---

<h2 class="name">NAME</h2>
<p> bochs &#8211; Portable x86 Emulator. </p>
<h2>SYNOPSIS</h2>
<p> <code>bochs</code> [<i>bochs_options</i>] [<i>bochsrc_options</i>]</p>
<h2>DESCRIPTION</h2>
<p> Bochs is a portable Intel Architecture 32 (x86) emulator that runs on most popular operating systems. Inside the emulator, it can run many operating systems including Linux and Microsoft(R) Windows(R).</p>
<h2>OPTIONS</h2>
<p> When you run bochs without one of the following options, it will search for a configuration file called .bochsrc in the current directory and your home directory and display the start menu.</p>
<dl>
<dt><code>-q</code></p>
<dd> With this option the start menu will be skipped after loading the configuration file.</p>
<dt><code>-f configfile</code></p>
<dd> This option specifies the name of the configuration file.</p>
<dt><code>-qf configfile</code></p>
<dd> When you run bochs with this option, it will skip the start menu and use the specified configuration file.</p>
<dt><code>-n</code></p>
<dd> With this option bochs doesn&#8217;t load a configuration file. In that case the setup for the emulation must be done with bochsrc options on the command line or in the start menu.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a summary of the command line options for bochs and exit.</dl>
<p> You can override the settings from the configuration file with command line arguments, using the same syntax as the bochsrc file. If you have any spaces in your command line arguments, they should be enclosed in single quotes. For information on Bochs command line and configuration file arguments, see the man page <code><a href="/docs/linux/man/5-bochsrc/">bochsrc</a>(5).</code> </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>bochs -q&nbsp;<wbr>&#8216;boot:a&#8217;&nbsp;<wbr>&#8216;floppya: 1_44=a.img, status=inserted&#8217; </p>
<h2>LICENSE</h2>
<p> This program is distributed under the terms of the GNU Lesser General Public License as published by the Free Software Foundation. See the COPYING file located in /usr/share/doc/bochs-2.3.8/ for details on the license and the lack of warranty.</p>
<h2>AVAILABILITY</h2>
<p> The latest version of this program can be found at: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://bochs.sourceforge.net/getcurrent.html">http://bochs.sourceforge.net/getcurrent.html</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-bochsrc/">bochsrc</a>(5), <a href="/docs/linux/man/1-bochs-dlx/">bochs-dlx</a>(1), <a href="/docs/linux/man/1-bximage/">bximage</a>(1), <a href="/docs/linux/man/1-bxcommit/">bxcommit</a>(1) </p>
<pre>
The Bochs IA-32 Emulator site on the World Wide Web:
        <a rel="nofollow" href="http://bochs.sourceforge.net">http://bochs.sourceforge.net</a>
Online Bochs Documentation
        <a rel="nofollow" href="http://bochs.sourceforge.net/doc/docbook">http://bochs.sourceforge.net/doc/docbook</a>
</pre>
<h2>AUTHORS</h2>
<p> The Bochs emulator was created by Kevin Lawton (kevin [at] mandrakesoft.com), and is currently maintained by the members of the Bochs x86 Emulator Project. You can see a current roster of members at: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://bochs.sourceforge.net/getinvolved.html">http://bochs.sourceforge.net/getinvolved.html</a></p>
<h2>BUGS</h2>
<p> Please report all bugs to the bug tracker on our web site. Just go to <a rel="nofollow" href="http://bochs.sourceforge.net,">http://bochs.sourceforge.net,</a> and click &quot;Bug Reports&quot; on the sidebar under &quot;Feedback&quot;. </p>
<p> Provide a detailed description of the bug, the version of the program you are running, the operating system you are running the program on and the operating system you are running in the emulator. </p>
<h2>Index</h2>
