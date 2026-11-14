---
title: "pilot-addresses(1)"
name: "pilot-addresses"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-addresses/"
description: "pilot-addresses – Read and write address book databases to and from a Palm handheld."
---

<h2>NAME</h2>
<p> pilot-addresses &#8211; Read and write address book databases to and from a Palm handheld.</p>
<h2>SECTION</h2>
<p> pilot-link: Userland conduits </p>
<h2>LOCATION</h2>
<p> ./src </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;port</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>-?</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;usage</code>]&nbsp;<wbr>[<code>-q</code>|<code>&#8211;quiet</code>]&nbsp;<wbr>[<code>&#8211;delete-all</code>]&nbsp;<wbr>[<code>-t</code>|<code>&#8211;delimiter</code>&nbsp;<wbr>&nbsp;<wbr><code>INT</code>]&nbsp;<wbr>[<code>-d</code>|<code>&#8211;delete-category</code>&nbsp;<wbr>&nbsp;<wbr><code>&nbsp;<wbr>category&nbsp;<wbr></code>&nbsp;<wbr>]&nbsp;<wbr>[<code>-c</code>|<code>&#8211;category</code>&nbsp;<wbr>&nbsp;<wbr><code>category</code>]&nbsp;<wbr>[<code>-a</code>|<code>&#8211;augment</code>]&nbsp;<wbr>[<code>-r</code>|<code>&#8211;read</code>&nbsp;<wbr>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-w</code>|<code>&#8211;write</code>&nbsp;<wbr>&nbsp;<wbr><i>&nbsp;<wbr>file&nbsp;<wbr></i>&nbsp;<wbr>]&nbsp;<wbr>[<code>-C</code>|<code>&#8211;human-readable</code>] </p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>allows the user to read all entries from a Palm handheld such as those made by&nbsp;<wbr><i>Palm</i>,&nbsp;<wbr><i>Handspring</i>,&nbsp;<wbr><i>Handera</i>,&nbsp;<wbr><i>TRGPro</i>,&nbsp;<wbr><i>Sony</i>&nbsp;<wbr>or other Palm handheld in the Palm Address Book application, write new entries into the database, and delete a category or delete all entries in the database. </p>
<h2>COMMANDS</h2>
<p> Provide exactly one of &#8211;read or &#8211;write. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-r</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;read</code>=&lt;<i>file</i>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Reads records from &lt;<i>file</i>&gt; and install them to the Palm Address Book application. (Use the <code>-w</code> &lt;<i>file</i>&gt; option to get a sample &quot;template file&quot; for input records to see how the fields are laid out). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-w</code>, &#8211;write=<i>file</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Reads all address book records from the Palm Address Book application and writes them into <i> file </i> </p>
<h2>OPTIONS</h2>
<h3>pilot-addresses options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-a</code>,&nbsp;<wbr><code>&#8211;augment</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Augments fields in address book records with additional information. The augmented information is placed before and separated from the field with a semi-colon, (;). </p>
<p> Augmented information can include any of the following below. </p>
<p>&nbsp;<wbr><code>category</code>&nbsp;<wbr>#&nbsp;<wbr>Placed in front of each record or.. </p>
<p> Placed in front of each phone number field: </p>
<p> [&quot;Work&quot;|&quot;Home&quot;|&quot;Fax&quot;|&quot;Other&quot;|&quot;E-mail&quot;|&quot;Main&quot;|&quot;Pager&quot;|&quot;Mobile&quot;] </p>
<p> Empty fields are not augmented. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-c</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;category</code>=<code>category</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Install records to category <code>category</code> by default. Normally <i>pilot-addresses</i> uses the <i>Unfiled</i> category by default. This option is overridden by the category specified in the record with the <code> -a </code> option. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-d</code>,&nbsp;<wbr><code>&#8211;delete-category</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Delete all records in the specified category <code>category</code> before installing new records. </p>
<p> Note that the long name of this option has changed since 0.11.8 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-D</code>,&nbsp;<wbr><code>&#8211;delete-all</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Delete all address book records in all categories. Obviously, be <i>very</i> careful with this one. </p>
<p> Note that the long name of this option has changed since 0.11.8 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-t</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;delimiter</code>&nbsp;<wbr><code>INT</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Include category in each record, use the delimiter specified to separate all fields of a record. Delimiters are specified as follows: 3=tab, 2=;, 1=,. This overrides the default delimiter of comma between fields and semi-colon between a field&#8217;s augmented information. (Please note that this may generate confusing results when used with the <code>-a</code> option.) </p>
<p> Note that the long name of this option has changed since 0.11.8 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-T</code>,&nbsp;<wbr><code>&#8211;titles</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Obsolete. This option has been removed since 0.11.8 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-C</code>|<code>&#8211;human-readable</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Write generic human-readable output instead of CSV. </p>
<h3>Conduit Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;port</code>&nbsp;<wbr>&lt;<i>port</i>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Use device file &lt;<i>port</i>&gt; to communicate with the Palm handheld. If this is not specified, <i>pilot-addresses</i> will look for the <i> $PILOTPORT </i> environment variable. If neither are found or supplied, <i>pilot-addresses</i> will print the usage information. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-q</code>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;quiet</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Suppress &#8216;Hit HotSync button&#8217; message </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-v</code>,&nbsp;<wbr><code>&#8211;version</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display version of <i>pilot-addresses</i> and exit without connecting. </p>
<h3>Help Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display the help synopsis for <i>pilot-addresses</i> and exit without connecting. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;usage</code>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display a brief usage message and exit without connecting. </p>
<h2>USAGE</h2>
<p> The program will connect to the Palm handheld, and perform the requested read or write operation specified by the user. </p>
<h2>EXAMPLES</h2>
<p> To write all address records in a Palm to the file addrbook.csv: </p>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&nbsp;<wbr><i>addrbook.csv</i>&nbsp;<wbr> </p>
<p> or </p>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>&nbsp;<wbr>&nbsp;<wbr><i>/dev/pilot</i>&nbsp;<wbr>&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&nbsp;<wbr><i>addrbook.csv</i>&nbsp;<wbr> </p>
<p> To read the address book records in the file addrbook.csv and install them onto the Palm: </p>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>&nbsp;<wbr><code>-r</code>&nbsp;<wbr>&nbsp;<wbr><i>addrbook.csv</i>&nbsp;<wbr> </p>
<p> To read the address book records in the file addrbook.csv and place them into the Palm address book database category <i>Special</i> after first deleting all current records in the <i> Special </i> category on the palm: </p>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>&nbsp;<wbr><code>-c</code>&nbsp;<wbr>&nbsp;<wbr><code>Special</code>&nbsp;<wbr>&nbsp;<wbr><code>-d</code>&nbsp;<wbr>&nbsp;<wbr><code>Special</code>&nbsp;<wbr>&nbsp;<wbr><code>-r</code>&nbsp;<wbr>&nbsp;<wbr><i>addrbook.csv</i>&nbsp;<wbr> </p>
<h2>AUTHOR</h2>
<p>&nbsp;<wbr><i>pilot-addresses</i>&nbsp;<wbr>originally written by Kenneth Albanowski, this manual page was originally written by Robert Wittig&nbsp;<wbr>&lt;bob.wittig [at] gt.org&gt;&nbsp;<wbr>and later updated by David A. Desrosiers&nbsp;<wbr>&lt;hacker [at] gnu-designs.com&gt;&nbsp;<wbr>and Neil Williams&nbsp;<wbr>&lt;linux [at] codehelp.co.uk&gt;. </p>
<h2>REPORTING BUGS</h2>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><i><a href="/docs/linux/man/1-addresses/">addresses</a></i>(1)&nbsp;<wbr><i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7) </p>
<h2>Index</h2>
