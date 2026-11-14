---
title: "fwbuilder(1)"
name: "fwbuilder"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fwbuilder/"
description: "fwbuilder – Multiplatform firewall configuration tool"
---

<h2>NAME</h2>
<p> fwbuilder &#8211; Multiplatform firewall configuration tool</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/fwbuilder</code> [-f<code>file.fwb]</code> [-d] [-h] [-o<code>file]</code> [-P<code>object_name]</code> [-r] [-v]<br />
&nbsp;<wbr> </p>
<h2>DESCRIPTION</h2>
<p> <code>fwbuilder</code> is the Graphic User Interface (GUI) component of Firewall Builder. </p>
<p> Firewall Builder consists of a GUI and set of policy compilers for various firewall platforms. It helps users maintain a database of objects and allows policy editing using simple drag-and-drop operations. GUI generates firewall description in the form of XML file, which compilers then interpret and generate platform-specific code. Several algorithms are provided for automated network objects discovery and bulk import of data. The GUI and policy compilers are completely independent, this provides for a consistent abstract model and the same GUI for different firewall platforms. </p>
<p> Firewall Builder supports firewalls based on iptables (Linux kernel 2.4.x and 2.6.x, see <a href="/docs/linux/man/1-fwb_ipt/">fwb_ipt</a>(1)), ipfilter (variety of platforms including *BSD, Solaris and others, see <a href="/docs/linux/man/1-fwb_ipf/">fwb_ipf</a>(1)), pf (OpenBSD and FreeBSD, see <a href="/docs/linux/man/1-fwb_pf/">fwb_pf</a>(1)), ipfw (FreeBSD and others), Cisco PIX (v6.x and 7.x) and Cisco IOS extended access lists. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-f FILE</p>
<dd> Specify the name of the file to be loaded when program starts. </p>
<dt>-r</p>
<dd> When this command line option is given in combination with -f file, the program automatically opens RCS head revision of the file if file is in RCS. If file is not in RCS, this option does nothing and the file is opened as usual. </p>
<dt>-d</p>
<dd> Turns on debug mode. Note that in this mode the program generates lots of output on standard error. This is used for debugging. </p>
<dt>-h</p>
<dd> Prints brief help message </p>
<dt>-o file</p>
<dd> Specify the name of the file for the print output, see option &quot;-P&quot;. </p>
<dt>-P object_name</p>
<dd> Print rules and objects for the firewall object &quot;object_name&quot; and immediately exit. The program does not go into interactive mode and does not need X11. Print output will be placed in the file specified with &quot;-o&quot; option. If file name is not given with option &quot;-o&quot;, print output is stored in the file &quot;print.pdf&quot; in the current directory. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.qt/firewallbuilder2rc</p>
<dd> Fwbuilder v2.1 stores user preferences in this file. </p>
<dt>$HOME/.config/netcitadel.com/Firewall Builder.conf</p>
<dd> Fwbuilder v3.0 stores user preferences in this file. </p>
</dl>
<h2>URL</h2>
<p> Firewall Builder home page is located at the following URL: <code><a rel="nofollow" href="http://www.fwbuilder.org/">http://www.fwbuilder.org/</a></code> </p>
<h2>BUGS</h2>
<p> Please report bugs using bug tracking system on SourceForge: </p>
<p> <code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=5314">http://sourceforge.net/tracker/?group_id=5314</a>&amp;atid=105314</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fwblookup/">fwblookup</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_ipt/">fwb_ipt</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_ipf/">fwb_ipf</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_pf/">fwb_pf</a>(1)</code> </p>
<h2>Index</h2>
