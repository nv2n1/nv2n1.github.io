---
title: "pilot-read-notepad(1)"
name: "pilot-read-notepad"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-read-notepad/"
description: "pilot-read-notepad – List the record information found in the Palm Notepad"
---

<h2>NAME</h2>
<p> pilot-read-notepad &#8211; List the record information found in the Palm Notepad</p>
<h2>SECTION</h2>
<p> pilot-link: Userland conduits </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr><i>pilot-read-notepad</i>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;port</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>-q</code>|<code>&#8211;quiet</code>]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>-?</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;usage</code>]&nbsp;<wbr>[<code>-l</code>|<code>&#8211;list</code>]&nbsp;<wbr>[<code>-t</code>|<code>&#8211;type</code>&nbsp;<wbr>&nbsp;<wbr><code>ppm|png</code>] </p>
<h2>DESCRIPTION</h2>
<p> Connect to the Palm handheld and list the record information found in the Palm Notepad application (found on OS4 and newer devices). If <code>&#8211;type</code> is specified, each record&#8217;s image will be converted to files, using Portable Network Graphic (.png) or Portable Pixmap (.ppm) format. </p>
<p>&nbsp;<wbr><i>pilot-read-notepad</i>&nbsp;<wbr>allows a user running PalmOS 4.0 or later to read the data stored in the Palm Notepad application and extract the data into images and convert them to Portable Network Graphics&nbsp;<wbr>(.png)&nbsp;<wbr>or Portable Pixmap&nbsp;<wbr>(.ppm)&nbsp;<wbr>files. </p>
<h2>OPTIONS</h2>
<h3>pilot-read-notepad options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-l</code>,&nbsp;<wbr><code>&#8211;list</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> List picture information found on the device instead of converting them to image files. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-t</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;type</code>&nbsp;<wbr><code>type</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Specify the output picture type. Can be either &quot;png&quot; or &quot;ppm&quot;. </p>
<h3>Conduit Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>,&nbsp;<wbr><code>&#8211;port</code>&nbsp;<wbr><i>port</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Use device file &lt;<i>port</i>&gt; to communicate with the Palm handheld. If this is not specified, <i>pilot-read-notepad</i> will look for the <i> $PILOTPORT </i> environment variable. If neither are found or supplied, <i>pilot-read-notepad</i> will print the usage information. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-q</code>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;quiet</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Suppress &#8216;Hit HotSync button&#8217; message </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-v</code>,&nbsp;<wbr><code>&#8211;version</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display version of <i>pilot-read-notepad</i> and exit without connecting. </p>
<h3>Help Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display the help synopsis for <i>pilot-read-notepad</i> and exit without connecting. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;usage</code>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display a brief usage message and exit without connecting. </p>
<h2>USAGE</h2>
<p> The program will connect to the target Palm handheld, and list or convert the records and images found in the Palm Notepad application to Portable Network Graphic (.png) or Portable Pixmap (.ppm) files. </p>
<h2>AUTHOR</h2>
<p>&nbsp;<wbr><i>pilot-read-notepad</i>&nbsp;<wbr>was originally written by Angus Ainslie&nbsp;<wbr>&lt;angusa [at] deltatee.com&gt;. </p>
<p> This manual page was converted to XML by Neil Williams &lt;linux [at] codehelp.co.uk&gt; </p>
<h2>REPORTING BUGS</h2>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7) </p>
<h2>Index</h2>
