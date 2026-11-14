---
title: "twprint(8)"
name: "twprint"
section: "8"
letter: "t"
url: "/docs/linux/man/8-twprint/"
description: "twprint – Tripwire database and report printer"
---

<p>twprint &#8211; Tripwire database and report printer</p>
<h2>Synopsis</h2>
<p><code>twprint</code> { <code>-m r</code> | <code>&#8211;print-report</code> } [ <i>options&#8230;</i> ]<br />
 <code>twprint</code> { <code>-m d</code> | <code>&#8211;print-dbfile</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <i>object1</i> [ <i>object2&#8230;</i> ]]</p>
<h2>Description</h2>
<p>Prints <i>Tripwire</i> database and report files in clear text format.</p>
<h3>Report Printing mode</h3>
<p>In Report Printing mode, <code>twprint</code> verifies and displays the contents of a <i>Tripwire</i> report file (<i>.twr</i>). If no report is specified on the command line, the report specified in the <tt>REPORTFILE</tt> variable in the configuration file will be used. By default, this value includes the date and time to the nearest second. Because this value is constantly changing, <code>twprint</code> may not be able to find the correct report file. For this reason, the (<code>-r</code> or <code>&#8211;twrfile</code>) flag should be used with the desired report name to print a specific report.</p>
<h3>Database Printing mode</h3>
<p>This option is used to print a <i>Tripwire</i> database file in human-readable (clear text) form. In Database Printing mode, <code>twprint</code> verifies and prints the contents of a specified database to <i>stdout</i>. If no database file is specified on the command line, the default database specified by the <tt>DBFILE</tt> variable in the configuration file is used.</p>
<h2>Options</h2>
<h3>Report printing mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m r</code></td>
<td><code>&#8211;print-report</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-h</code></td>
<td><code>&#8211;hexadecimal</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-r <i>report</i></code></td>
<td><code>&#8211;twrfile <i>report</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-t { 0|1|2|3|4 }</code></td>
<td><code>&#8211;report-level { 0|1|2|3|4 }</code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m r</code>, <code>&#8211;print-report</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-h</code>, <code>&#8211;hexadecimal</code></p>
<dd>Display hash values as hexadecimal.</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-r</code><i> report</i>, <code>&#8211;twrfile</code><i> report</i></p>
<dd>Print the specified report file.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Use the specified local key file to perform verification with reports which are signed.</p>
<dt><code>-t</code><i> level</i>, <code>&#8211;report-level</code><i> level</i></p>
<dd>Specifies the detail level of the printed report, overriding the <tt>REPORTLEVEL</tt> variable in the configuration file. <i>level</i> must be a number from 0 to 4.</dl>
<h3>Database printing mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m d</code></td>
<td><code>&#8211;print-dbfile</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-h</code></td>
<td><code>&#8211;hexadecimal</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-d <i>database</i></code></td>
<td><code>&#8211;dbfile <i>database</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
</table>
<p> [ <i>object1</i> [ <i>object2&#8230;</i> ]]</dl>
<dl>
<dt><code>-m d</code>, <code>&#8211;print-dbfile</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-h</code>, <code>&#8211;hexadecimal</code></p>
<dd>Display hash values as hexadecimal.</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-d</code><i> database</i>, <code>&#8211;dbfile</code><i> database</i></p>
<dd>Print the specified database file.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Use the specified local key file to read the database.</p>
<dt>[ <i>object1</i> [ <i>object2&#8230;</i> ]]</p>
<dd>List of filesystem objects in the database to print. If no objects are specified, every object in the database will be printed. The format for a list of objects is: <i>section: objname objname&#8230; section: objname&#8230;</i></dl>
<h2>Version Information</h2>
<p>This man page describes <code>twprint</code> version 2.4.</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) </p>
