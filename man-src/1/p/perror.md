---
title: "perror(1)"
name: "perror"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perror/"
description: "perror – display MySQL error message information"
---

<h2 class="name">NAME</h2>
<p> perror &#8211; display MySQL error message information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>perror [</code><i>options</i><code>] </code><i>errorcode</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>perror</code></p>
<dd>displays the error message for MySQL or operating system error codes. Invoke <code>perror</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>perror [</code><i>options</i><code>] </code><i>errorcode</i><code> ...</code>
</pre>
</dl>
<p> <code>perror</code> attempts to be flexible in understanding its arguments. For example, for the ER_WRONG_VALUE_FOR_VAR error, <code>perror</code> understands any of these arguments: <code>1231</code>, 001231, MY-1231, or MY-001231, or ER_WRONG_VALUE_FOR_VAR. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>perror 1231</code>
MySQL error code MY-001231 (ER_WRONG_VALUE_FOR_VAR): Variable '%-.64s'
can't be set to the value of '%-.200s'
</pre>
</dl>
<p> If an error number is in the range where MySQL and operating system errors overlap, <code>perror</code> displays both error messages: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>perror 1 13</code>
OS error code   1:  Operation not permitted
MySQL error code MY-000001: Can't create/write to file '%s' (OS errno %d - %s)
OS error code  13:  Permission denied
MySQL error code MY-000013: Can't get stat of '%s' (OS errno %d - %s)
</pre>
</dl>
<p> To obtain the error message for a MySQL Cluster error code, use the <code>ndb_perror</code> utility. </p>
<p> The meaning of system error messages may be dependent on your operating system. A given error code may mean different things on different operating systems. </p>
<p> <code>perror</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>&#8211;info</code>, <code>-I</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ndb</code> </p>
<p> Print the error message for a MySQL Cluster error code. </p>
<p> This option was removed in MySQL 8.0.13. Use the <code>ndb_perror</code> utility instead.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Silent mode. Print only the error message.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print error code and message. This is the default behavior.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
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
