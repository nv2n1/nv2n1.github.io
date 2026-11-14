---
title: "ngnutmeg(1)"
name: "ngnutmeg"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ngnutmeg/"
description: "ngnutmeg – ngspice post-processor"
---

<h2 class="name">NAME</h2>
<p> ngnutmeg &#8211; ngspice post-processor </p>
<h2>SYNOPSIS</h2>
<p> <code>ngnutmeg</code> [<i>options</i>] [<i>datafile</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This man page is just a small overview. The primary documentation of ngspice is in the ngspice] User&#8217;s Manual, which is available as a pdf file.<br />
 <code>ngnutmeg</code> is a post processor for ngspice] &#8211; it takes the raw output file created by <code>ngspice -r</code> and plots the data on a graphics terminal or a workstation display. Note that the raw output file is different from the data that ngspice] writes to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd>
 Don&#8217;t try to load the default data file (&quot;rawspice&quot;) if no other files are given.</p>
<dt><code>-n</code> or <code>&#8211;no-spiceinit</code></p>
<dd> Don&#8217;t try to source the file &quot;.spiceinit&quot; upon startup. Normally <code>ngnutmeg</code> tries to find the file in the current directory, and if it is not found then in the user&#8217;s home directory.</p>
<dt><code>-q</code> or <code>&#8211;completion</code></p>
<dd> Enable command completion. (defect)</p>
<dt><code>-t</code> <i>term</i> or <code>&#8211;term=</code><i>term</i></p>
<dd> The program is being run on a terminal with <code>mfb</code> name <i>term</i>.</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Display a verbose help on the arguments available to the program.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd> Display a version number and copyright information of the program.</dl>
<p> Further arguments are taken to be data files in binary or ascii format (see <code><a href="/docs/linux/man/1-sconvert/">sconvert</a></code>(1)) which are loaded into ngnutmeg. If the file is in binary format, it may be only partially completed (useful for examining ngspice] ouput before the simulation is finished). One file may contain any number of data sets from different analyses.</p>
<h2>ENVIRONMENT</h2>
<p> See <a href="/docs/linux/man/1-ngspice/">ngspice</a>(1)</p>
<h2>FILES</h2>
<p> See <a href="/docs/linux/man/1-ngspice/">ngspice</a>(1)</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sconvert/">sconvert</a>(1), <a href="/docs/linux/man/1-ngspice/">ngspice</a>(1), <a href="/docs/linux/man/3-mfb/">mfb</a>(3), <a href="/docs/linux/man/3-writedata/">writedata</a>(3), and<br />
 ngspice] User&#8217;s Manual at <code><a rel="nofollow" href="http://ngspice.sourceforge.net/docs.html">http://ngspice.sourceforge.net/docs.html</a></code></p>
<h2>BUGS</h2>
<p> Please report bugs to the ngspice project via<br />
 <code><a rel="nofollow" href="http://ngspice.sourceforge.net/bugrep.html">http://ngspice.sourceforge.net/bugrep.html</a></code></p>
<h2>AUTHOR</h2>
<p> Wayne Christopher (faustus [at] cad.berkeley.edu)<br />
 <code>ngspice</code>: various authors (see <code><a rel="nofollow" href="http://sourceforge.net/projects/ngspice/">http://sourceforge.net/projects/ngspice/</a></code>) </p>
<h2>Index</h2>
