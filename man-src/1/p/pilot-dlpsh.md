---
title: "pilot-dlpsh(1)"
name: "pilot-dlpsh"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-dlpsh/"
description: "pilot-dlpsh – An interactive Desktop Link Protocol (DLP) Shell for your Palm device."
---

<h2>NAME</h2>
<p> pilot-dlpsh &#8211; An interactive Desktop Link Protocol (DLP) Shell for your Palm device.</p>
<h2>SECTION</h2>
<p> pilot-link: Tools </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr><i>pilot-dlpsh</i>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;port</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>-c</code>|<code>&#8211;command</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-i</code>|<code>&#8211;interactive</code>]&nbsp;<wbr>[<code>&#8211;version</code>] </p>
<h2>OPTIONS</h2>
<h3>pilot-dlpsh options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-c</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;command STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Execute <code>cmd</code> and exit immediately. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-i</code>,&nbsp;<wbr><code>&#8211;interactive</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Enter interactive mode </p>
<h3>Conduit Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;port</code>&nbsp;<wbr>&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>port</code>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Use device file &lt;<i>port</i>&gt; to communicate with the Palm handheld. If this is not specified, <i>pilot-dlpsh</i> will look for the <i>$PILOTPORT</i> environment variable. If the port is missing and <i>$PILOTPORT</i> is not set, <i>pilot-dlpsh</i> will print the usage information. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;version</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display the copyright information, version number, license details and build details and exit without connecting. </p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr><i>pilot-dlpsh</i>&nbsp;<wbr>allows the user to connect to a Palm handheld and execute arbitrary DLP commands. </p>
<p> pilot-dlpsh can query many different types of information from your Palm device, such as username, memory capacity, set the time, as well as other useful functions. </p>
<p> Once connected, the user may execute most of the built-in <i>DLP</i> commands. (See <i>BUILT-IN COMMANDS </i> below for more detail on currently supported options). </p>
<p> The connection to the Pilot is kept alive by sending a <i>PadTickle</i> packet to the Pilot after a small period of non-activity. (7 seconds by default) </p>
<h2>BUILT-IN COMMANDS</h2>
<p> There are many options available while connected to your Palm handheld via <i>pilot-dlpsh</i>, including the following: </p>
<p>&nbsp;<wbr><code>user, u</code>&nbsp;<wbr> </p>
<p> Print the currently set User information, including Username, UserID, PCid, and ViewerID. You may also set these values from this command as well. To set these values, simply pass the value to the option, such as &#8216;user John Q. Public&#8217; for example. </p>
<p>&nbsp;<wbr><code>ls</code>&nbsp;<wbr> </p>
<p> Used with <code>-l</code> and <code>-r</code> to provide long and RAM and ROM file lists, similar to (but slightly different from) the Unix &#8216;ls&#8217; command. This does not yet allow you to narrow your listing to a certain range of files. It will simply list them all. </p>
<p>&nbsp;<wbr><code>df</code>&nbsp;<wbr> </p>
<p> Display how much RAM and ROM is free on your device, again similar to the Unix &#8216;df&#8217; command. This does not accept arguments at this time. </p>
<p>&nbsp;<wbr><code>ntp, time, dtp</code>&nbsp;<wbr> </p>
<p> Set the time on the Palm from the currently-set desktop time. This does not work on OS version 3.3, due to a bug in PalmOS at that time. </p>
<p>&nbsp;<wbr><code>rm, del</code>&nbsp;<wbr> </p>
<p> Remove a file and delete it entirely from the Palm device. This is an irrevokable process, and you cannot &quot;undelete&quot; a file, once it has been deleted with this command. </p>
<p>&nbsp;<wbr><code>quit, q, exit, bye</code>&nbsp;<wbr> </p>
<p> Exit the DLP Protocol Shell </p>
<h2>OPTIONS</h2>
<p> Passing commandline options to <code>pilot-dlpsh</code> will allow you to interact with it in unattended mode, for example: &#8216;<code>pilot-dlpsh</code> -p usb: -c user&#8217; will connect and display the user information, just as if you had connected interactively and typed &#8216;user&#8217; at the DLP shell prompt. </p>
<h2>USAGE</h2>
<p> The program will connect to your Palm handheld and give the user an interactive prompt (a &quot;shell&quot;) for executing commands across the DLP <i>HotSync</i> protocol. </p>
<h2>AUTHOR</h2>
<p>&nbsp;<wbr><code>pilot-dlpsh</code>&nbsp;<wbr>was originally written by Chris Stevens&nbsp;<wbr>&lt;stevens [at] rpi.edu&gt;&nbsp;<wbr>and Damien Neil&nbsp;<wbr>&lt;neild [at] rpi.edu&gt;&nbsp;<wbr> </p>
<p> This manual page was updated to XML by Neil Williams &lt;linux [at] codehelp.co.uk&gt; </p>
<h2>REPORTING BUGS</h2>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7) </p>
<h2>Index</h2>
