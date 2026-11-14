---
title: "myisam_ftdump(1)"
name: "myisam_ftdump"
section: "1"
letter: "m"
url: "/docs/linux/man/1-myisam_ftdump/"
description: "myisam_ftdump – display full-text index information"
---

<h2 class="name">NAME</h2>
<p> myisam_ftdump &#8211; display full-text index information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>myisam_ftdump [</code><i>options</i><code>] </code><i>tbl_name</i><i>index_num</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>myisam_ftdump</code></p>
<dd>displays information about FULLTEXT indexes in MyISAM tables. It reads the MyISAM index file directly, so it must be run on the server host where the table is located. Before using <code>myisam_ftdump</code>, be sure to issue a FLUSH TABLES statement first if the server is running. </p>
<p> <code>myisam_ftdump</code> scans and dumps the entire index, which is not particularly fast. On the other hand, the distribution of words changes infrequently, so it need not be run often. </p>
<p> Invoke <code>myisam_ftdump</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisam_ftdump [</code><i>options</i><code>] </code><i>tbl_name</i><i>index_num</i>
</pre>
</dl>
<p> The <i>tbl_name</i> argument should be the name of a MyISAM table. You can also specify a table by naming its index file (the file with the .MYI suffix). If you do not invoke <code>myisam_ftdump</code> in the directory where the table files are located, the table or index file name must be preceded by the path name to the table&#8217;s database directory. Index numbers begin with 0. </p>
<p> Example: Suppose that the test database contains a table named mytexttable that has the following definition: </p>
<dl>
<dt>
<dd>
<pre>
CREATE TABLE mytexttable
(
  id   INT NOT NULL,
  txt  TEXT NOT NULL,
  PRIMARY KEY (id),
  FULLTEXT (txt)
) ENGINE=MyISAM;
</pre>
</dl>
<p> The index on id is index 0 and the FULLTEXT index on txt is index 1. If your working directory is the test database directory, invoke <code>myisam_ftdump</code> as follows: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisam_ftdump mytexttable 1</code>
</pre>
</dl>
<p> If the path name to the test database directory is /usr/local/mysql/data/test, you can also specify the table name argument using that path name. This is useful if you do not invoke <code>myisam_ftdump</code> in the database directory: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisam_ftdump /usr/local/mysql/data/test/mytexttable 1</code>
</pre>
</dl>
<p> You can use <code>myisam_ftdump</code> to generate a list of index entries in order of frequency of occurrence like this on Unix-like systems: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisam_ftdump -c mytexttable 1 | sort -r</code>
</pre>
</dl>
<p> On Windows, use: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisam_ftdump -c mytexttable 1 | sort /R</code>
</pre>
</dl>
<p> <code>myisam_ftdump</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-h</code> <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;count</code>, <code>-c</code> </p>
<p> Calculate per-word statistics (counts and global weights).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;dump</code>, <code>-d</code> </p>
<p> Dump the index, including data offsets and word weights.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;length</code>, <code>-l</code> </p>
<p> Report the length distribution.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;stats</code>, <code>-s</code> </p>
<p> Report global index statistics. This is the default operation if no other operation is specified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more output about what the program does.</dl>
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
