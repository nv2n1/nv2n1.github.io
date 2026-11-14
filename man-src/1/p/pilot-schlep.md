---
title: "pilot-schlep(1)"
name: "pilot-schlep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-schlep/"
description: "pilot-schlep – Pack an arbitrary file and install it on your Palm or unpack a file from your Palm."
---

<h2>NAME</h2>
<p> pilot-schlep &#8211; Pack an arbitrary file and install it on your Palm or unpack a file from your Palm.</p>
<h2>SECTION</h2>
<p> pilot-link: Userland conduits </p>
<h2>SYNOPSIS</h2>
<p> <i>pilot-schlep</i> [<code>-p</code>|<code>&#8211;port</code>&lt;<code>port</code>&gt;] [<code>&#8211;version</code>] [<code>-?</code>|<code>&#8211;help</code>] [<code>&#8211;usage</code>] [<code>-q</code>|<code>&#8211;quiet</code>] [<code>-i</code>|<code>&#8211;install</code> <i>file</i>] [<code>-f</code>|<code>&#8211;fetch</code> <i>file</i>] [<code>-d</code>|<code>&#8211;delete</code>] </p>
<h2>DESCRIPTION</h2>
<p> Currently the stored name and file type is not queried so you can potentially install a PDF file, and retrieve it as a ZIP file. </p>
<p> You must take care to remember what type of file you are installing and fetching. This will be updated in a later release to handle this type of capability, as well as handle multiple &#8216;Schlep&#8217; files. </p>
<h2>OPTIONS</h2>
<h3>pilot-schlep options</h3>
<p> <code>-i</code>, <code>&#8211;install</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>file</i> </p>
<p> Pack and install <i>file</i> to your Palm <code>-f</code>, <code>&#8211;fetch</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>file</i> </p>
<p> Unpack the file from your Palm device <code>-d</code>, <code>&#8211;delete</code> </p>
<p> Delete the packaged file from your Palm device </p>
<h3>Conduit Options</h3>
<p> <code>-p</code>, <code>&#8211;port</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>port</i> </p>
<p> Use device file <i>port</i> to communicate with the Palm handheld. If this is not specified, <i>pilot-schlep</i> will look for the <i>$PILOTPORT</i> environment variable. If neither are found or supplied, <i> pilot-schlep </i> will print the usage information. <code>-q</code>, <code>&#8211;quiet</code> </p>
<p> Suppress &#8216;Hit HotSync button&#8217; message <code>-v</code>, <code>&#8211;version</code> </p>
<p> Display version of <i>pilot-schlep</i>. </p>
<h3>Help Options</h3>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<p> Display the help synopsis for <i>pilot-schlep</i>. <code>&#8211;usage</code> </p>
<p> Display a brief usage message and exit without connecting. </p>
<h2>EXAMPLES</h2>
<p> To package up and store a file for later retrieval on your Palm: </p>
<pre>
<code>pilot-schlep</code> -p /dev/pilot -i InstallThis.zip        
</pre>
<p> To unpack a file that has been stored on your Palm with pilot-schlep: </p>
<pre>
<code>pilot-schlep</code> -p /dev/pilot -f RetrieveThis.pdfc        
</pre>
<p> Please notice that you must use redirection to Install or Fetch files using pilot-schlep. </p>
<p> Currently the stored name and file type is not queried so you can potentially Install a PDF file, and retrieve it as a ZIP file. </p>
<p> You must take care to remember what type of file you are installing and fetching. This will be updated in a later release to handle this type of capability, as well as handle multiple &#8216;Schlep&#8217; files. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Neil Williams &lt;linux [at] codehelp.co.uk&gt; </p>
<h2>REPORTING BUGS</h2>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7) </p>
<h2>Index</h2>
