---
title: "mysql_tzinfo_to_sql(1)"
name: "mysql_tzinfo_to_sql"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_tzinfo_to_sql/"
description: "mysql_tzinfo_to_sql – load the time zone tables"
---

<h2 class="name">NAME</h2>
<p> mysql_tzinfo_to_sql &#8211; load the time zone tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_tzinfo_to_sql </code><i>arguments</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mysql_tzinfo_to_sql</code> program loads the time zone tables in the mysql database. It is used on systems that have a <i>zoneinfo</i> database (the set of files describing time zones). Examples of such systems are Linux, FreeBSD, Solaris, and macOS. One likely location for these files is the /usr/share/zoneinfo directory (/usr/share/lib/zoneinfo on Solaris). If your system does not have a zoneinfo database, you can use the downloadable package described in Section 5.1.13, &#8220;MySQL Server Time Zone Support&#8221;. </p>
<p> <code>mysql_tzinfo_to_sql</code> can be invoked several ways: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_tzinfo_to_sql </code><i>tz_dir</i>
shell&gt; <code>mysql_tzinfo_to_sql </code><i>tz_file tz_name</i>
shell&gt; <code>mysql_tzinfo_to_sql --leap </code><i>tz_file</i>
</pre>
</dl>
<p> For the first invocation syntax, pass the zoneinfo directory path name to <code>mysql_tzinfo_to_sql</code> and send the output into the <code>mysql</code> program. For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql</code>
</pre>
</dl>
<p> <code>mysql_tzinfo_to_sql</code> reads your system&#8217;s time zone files and generates SQL statements from them. <code>mysql</code> processes those statements to load the time zone tables. </p>
<p> The second syntax causes <code>mysql_tzinfo_to_sql</code> to load a single time zone file <i>tz_file</i> that corresponds to a time zone name <i>tz_name</i>: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_tzinfo_to_sql </code><i>tz_file</i><i>tz_name</i><code> | mysql -u root mysql</code>
</pre>
</dl>
<p> If your time zone needs to account for leap seconds, invoke <code>mysql_tzinfo_to_sql</code> using the third syntax, which initializes the leap second information. <i>tz_file</i> is the name of your time zone file: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_tzinfo_to_sql --leap </code><i>tz_file</i><code> | mysql -u root mysql</code>
</pre>
</dl>
<p> After running <code>mysql_tzinfo_to_sql</code>, it is best to restart the server so that it does not continue to use any previously cached time zone data.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
