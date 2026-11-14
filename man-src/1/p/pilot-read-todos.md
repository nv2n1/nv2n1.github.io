---
title: "pilot-read-todos(1)"
name: "pilot-read-todos"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-read-todos/"
description: "pilot-read-todos – Syncronize your Palm ToDo application’s database with your desktop machine."
---

<h2>NAME</h2>
<p> pilot-read-todos &#8211; Syncronize your Palm ToDo application&#8217;s database with your desktop machine.</p>
<h2>SECTION</h2>
<p> pilot-link: Userland conduits </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;port</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>-q</code>|<code>&#8211;quiet</code>]&nbsp;<wbr>[<code>-A</code>|<code>&#8211;archived</code>]&nbsp;<wbr>[<code>-w</code>|<code>&#8211;write</code>] </p>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>[<code>-f</code>|<code>&#8211;file</code>&nbsp;<wbr>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-A</code>|<code>&#8211;archived</code>]&nbsp;<wbr>[<code>-w</code>|<code>&#8211;write</code>] </p>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>-?</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;usage</code>] </p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>will read the ToDo database on the Palm handheld, or read the ToDoDB.pdb file directly from disk on your desktop machine, and print the contents to STDOUT&nbsp;<wbr>(generally the screen). </p>
<p> Use only one of <code>&#8211;port</code> or <code>&#8211;file</code>. </p>
<h2>OPTIONS</h2>
<h3>pilot-read-todos option</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-f</code>,&nbsp;<wbr><code>&#8211;file</code>&nbsp;<wbr><i>file</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Read a local todo database file from disk for printing. Excludes &#8211;port. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-A</code>,&nbsp;<wbr><code>&#8211;archived</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Write archived entries only, in human-readable format </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-w</code>,&nbsp;<wbr><code>&#8211;write</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Write output &#8211; every operation must include a write command. </p>
<h3>Conduit Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>,&nbsp;<wbr><code>&#8211;port</code>&nbsp;<wbr><i>port</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Use device file &lt;<i>port</i>&gt; to communicate with the Palm handheld device. If this is not specified, <i>pilot-read-todos</i> will look for the <i> $PILOTPORT </i> environment variable. If neither are found or supplied, <i>pilot-read-todos</i> will print the usage information. </p>
<p> Excludes &#8211;file. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-q</code>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;quiet</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Suppress &#8216;Hit HotSync button&#8217; message </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-v</code>,&nbsp;<wbr><code>&#8211;version</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display version of <i>pilot-read-todos</i> and exit without connecting. </p>
<h3>Help Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display the help synopsis for <i>pilot-read-todos</i> and exit without connecting. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;usage</code>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display a brief usage message and exit without connecting. </p>
<h2>USAGE</h2>
<p> Connect to a target Palm handheld and read the ToDo database, or read the ToDoDB.pdb file from disk and print the entries found to STDOUT. </p>
<h2>EXAMPLES</h2>
<p> Read the on-Palm ToDo database, and dump to STDOUT. </p>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>&nbsp;<wbr>&nbsp;<wbr><i>/dev/pilot</i>&nbsp;<wbr> </p>
<p> Read the ToDoDB.pdb file on disk, and dump to STDOUT </p>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&nbsp;<wbr><code>-f</code>&nbsp;<wbr>&nbsp;<wbr><i>ToDoDB.pdb</i>&nbsp;<wbr> </p>
<h2>AUTHOR</h2>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>was originally written by Kenneth Albanowski </p>
<h2>BUGS</h2>
<h3>Known Bugs</h3>
<p>&nbsp;<wbr><i>pilot-read-todos</i>&nbsp;<wbr>does not support Notes attached to ToDo items at this time. </p>
<h3>Reporting Bugs</h3>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><i>install-todo</i>&nbsp;<wbr>(1),&nbsp;<wbr><i>install-todos</i>&nbsp;<wbr>(1),&nbsp;<wbr><i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7) </p>
<h2>Index</h2>
