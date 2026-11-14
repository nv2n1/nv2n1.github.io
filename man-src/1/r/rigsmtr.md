---
title: "rigsmtr(1)"
name: "rigsmtr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rigsmtr/"
description: "rigsmtr – measure S-Meter vs azimuth using Hamlib"
---

<h2 class="name">NAME</h2>
<p> rigsmtr &#8211; measure S-Meter vs azimuth using Hamlib </p>
<h2>SYNOPSIS</h2>
<p> <code>rigsmtr</code> [<i>OPTION</i>]&#8230; [time_step]</p>
<h2>DESCRIPTION</h2>
<p> <code>rigsmtr</code> uses Hamlib to control a rig to measure S-Meter vs azimuth:<br />
 It rotates the antenna from minimum azimuth to maximum azimuth. Every second or <i>time_step</i> if specified in seconds, it retrieves the signal strength.<br />
 Azimuth in degree and corresponding S-Meter level in dB relative to S9 are then printed on stdout.<br />
 To work correctly, rigsmtr needs a rig that could measure S-Meter and a Hamlib backend that is able to get it, mounted on a Hamlib supported rotator. </p>
<p> Keep in mind that <code>Hamlib</code> is still BETA level software. A lof of stuff hasn&#8217;t been tested thoroughly, and the API may change without publicised notice. Please report bugs and feedback at the e-mail address given in the REPORTING BUGS section.</p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd> Select radio model number. See model list provided by rigctl.</p>
<dt><code>-r, &#8211;rig-file=device</code></p>
<dd> Use <code>device</code> as the file name of the radio to operate on.</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd> Set radio serial speed to <code>baud</code> rate. Uses maximal rig speed as default.</p>
<dt><code>-c, &#8211;civaddr=id</code></p>
<dd> Use <code>id</code> as the CI-V address to communicate with the rig. Only for Icom rigs. NB: the id is in decimal, unless prefixed by <code>0x</code>, in which case it is hexadecimal.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd> Set radio config parameter. See -L option of rigctl for a list.</p>
<dt><code>-M, &#8211;rot-model=id</code></p>
<dd> Select radio model number. See model list provided by rotctl.</p>
<dt><code>-R, &#8211;rot-file=device</code></p>
<dd> Use <code>device</code> as the file name of the rotator to operate on.</p>
<dt><code>-S, &#8211;rot-serial-speed=baud</code></p>
<dd> Set rotator serial speed to <code>baud</code> rate. Uses maximal speed as default.</p>
<dt><code>-N, &#8211;rot-set-conf=parm=val[,parm=val]*</code></p>
<dd> Set rotator config parameter. See -L option of rotctl for a list.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Set verbose mode, cumulative (BUG, ERR, WARN, VERBOSE, TRACE).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program and exit. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> rigsmtr exits with: 0 if all operations went fine; 1 if there was an invalid command line option or arg; 2 if an error was returned by Hamlib; 3 if the rig doesn&#8217;t have the required capabilities. </p>
<h2>EXAMPLE</h2>
<p> rigsmtr -m 209 -r /dev/ttyS1 -M 202 &gt; csmtr </p>
<p> Collect S-Meter readings on a TS850 while an EasycommII rotator makes a full 360&#176;, and record measurements in file csmtr.<br />
 After completion, csmtr file contains for example the following lines : </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0 -47 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>30 -40&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>60 -22 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>90 -3&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>120 10&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>150 1&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>180 -11&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>210 -24&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>240 -35&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>270 -42&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>300 -48&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>330 -51&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>360 -49&nbsp;<wbr> </p>
<dl>
<dt>Result could then be ploted with gnuplot:</p>
<dd>
 gnuplot<br />
 set angles degrees<br />
 set polar<br />
 set grid polar 15.<br />
 unset border<br />
 unset param<br />
 set style data line<br />
 set rrange [-60:60]<br />
 set xrange [-60:60]<br />
 set yrange [-60:60]<br />
 plot &quot;csmtr&quot;</dl>
<h2>AUTHOR</h2>
<p> Man page written by Stephane Fillod.</p>
<h2>BUGS</h2>
<p> Need more testing. Reports are welcome.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;hamlib-developer [at] users.sourceforge.net&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2009 Thierry Leconte &amp; Stephane Fillod<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hamlib/">hamlib</a></code>(3),<code><a href="/docs/linux/man/1-rigctl/">rigctl</a></code>(1),<code><a href="/docs/linux/man/1-rotctl/">rotctl</a></code>(1) </p>
<h2>Index</h2>
