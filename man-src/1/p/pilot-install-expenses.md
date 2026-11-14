---
title: "pilot-install-expenses(1)"
name: "pilot-install-expenses"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-install-expenses/"
description: "pilot-install-expenses – Install an expense record entries onto your Palm handheld device."
---

<h2>NAME</h2>
<p> pilot-install-expenses &#8211; Install an expense record entries onto your Palm handheld device.</p>
<h2>SECTION</h2>
<p> pilot-link: Userland conduits </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr><i>pilot-install-expenses</i>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;port</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>-q</code>|<code>&#8211;quiet</code>]&nbsp;<wbr>[<code>-?</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;usage</code>]&nbsp;<wbr>[<code>-t</code>|<code>&#8211;ptype</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-e</code>|<code>&#8211;etype</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-a</code>|<code>&#8211;amount</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;vendor</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-i</code>|<code>&#8211;city</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-g</code>|<code>&#8211;guests</code>&nbsp;<wbr>&nbsp;<wbr><code>NUMBER</code>]&nbsp;<wbr>[<code>-n</code>|<code>&#8211;note</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>-c</code>|<code>&#8211;category</code>&nbsp;<wbr>&nbsp;<wbr><code>STRING</code>]&nbsp;<wbr>[<code>&#8211;replace</code>] </p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr><i>pilot-install-expenses</i>&nbsp;<wbr>allows a Palm handheld with the Expense application to have expense records synchronized to it from the commandline. You can pass any of the fields&nbsp;<wbr>(except categories, currently)&nbsp;<wbr>to&nbsp;<wbr><i>pilot-install-expenses</i>&nbsp;<wbr>and create new expense records on your Palm handheld. </p>
<h2>OPTIONS</h2>
<h3>pilot-install-expenses options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-t</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;ptype</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add entries to the &quot;Payment Type&quot; field. These can be in the form of &quot;Cash&quot;, &quot;Cheque&quot; and others. See the Expense application on your Palm device for full details on payment types. </p>
<p> Note that the long name for this option has been renamed since 0.11.8. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-e</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;etype</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add entries to the &quot;Expense Type&quot; field. These can be in the form of Airfare, Meals, and Others. See the Expense application on your Palm device for full details on expense types. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-a</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;amount</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add currency amount entries to the &quot;Amount&quot; field. These can be in the form of 1.00 or &quot;$10.00&quot; and so on. See the Expense application on your Palm device for full details on amount types. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-V</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;vendor</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add entries to the &quot;Vendor&quot; field. These are free-form values, and can be the name of a restaurant, an airline, or any other text value you wish to use. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-g</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;guests</code>&nbsp;<wbr><code>DIGIT</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add the number of attendees to the expense record, identified by <code>DIGIT</code>. If you ate lunch with four (4) additional people, you would put five (5) here, a numeric value. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-i</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;city</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add entries to the &quot;City&quot; field in the expense record. These are free-form values, and can be the name of the location, city, or town that the expense record occurred in. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-n</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;note</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Add a &quot;Note&quot; entry to the expense record. These are free-form values, and can be some notes related to the expense entry. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-c</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;category</code>&nbsp;<wbr><code>STRING</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Install entries into the named category defined here. See the Expense application on your Palm device for full details on using these categories. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;replace</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Replace the entry found in the named category identified by the <code>&#8211;category</code> option </p>
<p> Note that the short name for this option has been removed since 0.11.8 </p>
<h3>Conduit Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-p</code>,&nbsp;<wbr><code>&#8211;port</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;<code>port</code>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Use device file &lt;<i>port</i>&gt; to communicate with the Palm handheld. If this is not specified, <i>pilot-install-expenses</i> will look for the <i> $PILOTPORT </i> environment variable. If neither are found or supplied, <i>pilot-install-expenses</i> will print the usage information. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-q</code>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;quiet</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Suppress &#8216;Hit HotSync button&#8217; message. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;version</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display version information for <i>pilot-install-expenses</i> and exit without connecting. </p>
<h3>Help options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display the help synopsis for <i>pilot-install-expenses</i> and exit without connecting. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;usage</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Display a brief usage message and exit without connecting. </p>
<h2>USAGE</h2>
<p> The program will connect to the Palm handheld, and install entries into the Expense application based on values passed to <i>pilot-install-expenses</i> arguments. </p>
<h2>EXAMPLE</h2>
<p>&nbsp;<wbr><i>pilot-install-expenses</i>&nbsp;<wbr>&nbsp;<wbr><i>-p</i>&nbsp;<wbr>&nbsp;<wbr><i>/dev/pilot</i>&nbsp;<wbr>&nbsp;<wbr><i>-c</i>&nbsp;<wbr>Unfiled&nbsp;<wbr><i>-t</i>&nbsp;<wbr>Cash&nbsp;<wbr><i>-e</i>&nbsp;<wbr>Meals&nbsp;<wbr><i>-a</i>&nbsp;<wbr>10.00&nbsp;<wbr><i>-V</i>&nbsp;<wbr>McDonalds&nbsp;<wbr><i>-g</i>&nbsp;<wbr>21&nbsp;<wbr><i>-l</i>&nbsp;<wbr>&quot;San Francisco&quot;&nbsp;<wbr><i>-N</i>&nbsp;<wbr>&quot;This is a note&quot; </p>
<p> Installs a new expense; you are recording having 21 guests at McDonalds in the city of San Francisco for a meal which cost 10.00 units of your default currency and you added a simple note. The expense will take the default date &#8211; today. </p>
<h2>AUTHOR</h2>
<p>&nbsp;<wbr><i>pilot-install-expenses</i>&nbsp;<wbr>was originally written by community authors, the original author is unknown. </p>
<p> This manual page was converted to XML by Neil Williams &lt;linux [at] codehelp.co.uk&gt; </p>
<h2>REPORTING BUGS</h2>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><i>read-expenses</i>&nbsp;<wbr>(1),&nbsp;<wbr><i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7). </p>
<h2>Index</h2>
