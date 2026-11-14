---
title: "ndb_select_all(1)"
name: "ndb_select_all"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_select_all/"
description: "ndb_select_all – print rows from an NDB table"
---

<h2 class="name">NAME</h2>
<p> ndb_select_all &#8211; print rows from an NDB table </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_select_all -c </code><i>connect_string</i><i>tbl_name</i><code> -d </code><i>db_name</i><code> [&gt; </code><i>file_name</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_select_all</code></p>
<dd>prints all rows from an NDB table to stdout. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_select_all -c <i>connect_string</i> <i>tbl_name</i> -d <i>db_name</i> [&gt; <i>file_name</i>]
</pre>
</dl>
<p> <code>Additional Options</code>: </p>
<dl>
<dt>
<dd> * <code>&#8211;lock=</code><i>lock_type</i>, <code>-l </code><i>lock_type</i> </p>
<p> Employs a lock when reading the table. Possible values for <i>lock_type</i> are: </p>
<dl>
<dt>
<dd> * 0: Read lock</dl>
<dl>
<dt>
<dd> * 1: Read lock with hold</dl>
<dl>
<dt>
<dd> * 2: Exclusive read lock</dl>
<dl>
<dt>
<dd> There is no default value for this option.</dl>
<dl>
<dt>
<dd> * <code>&#8211;order=</code><i>index_name</i>, <code>-o </code><i>index_name</i> </p>
<p> Orders the output according to the index named <i>index_name</i>. Note that this is the name of an index, not of a column, and that the index must have been explicitly named when created.</dl>
<dl>
<dt>
<dd> * <code>&#8211;descending</code>, <code>-z</code> </p>
<p> Sorts the output in descending order. This option can be used only in conjunction with the <code>-o</code> (<code>&#8211;order</code>) option.</dl>
<dl>
<dt>
<dd> * <code>&#8211;header=FALSE</code> </p>
<p> Excludes column headers from the output.</dl>
<dl>
<dt>
<dd> * <code>&#8211;useHexFormat</code> <code>-x</code> </p>
<p> Causes all numeric values to be displayed in hexadecimal format. This does not affect the output of numerals contained in strings or datetime values.</dl>
<dl>
<dt>
<dd> * <code>&#8211;delimiter=</code><i>character</i>, <code>-D </code><i>character</i> </p>
<p> Causes the <i>character</i> to be used as a column delimiter. Only table data columns are separated by this delimiter. </p>
<p> The default delimiter is the tab character.</dl>
<dl>
<dt>
<dd> * <code>&#8211;disk</code> </p>
<p> Adds a disk reference column to the output. The column is nonempty only for Disk Data tables having nonindexed columns.</dl>
<dl>
<dt>
<dd> * <code>&#8211;rowid</code> </p>
<p> Adds a ROWID column providing information about the fragments in which rows are stored.</dl>
<dl>
<dt>
<dd> * <code>&#8211;gci</code> </p>
<p> Adds a column to the output showing the global checkpoint at which each row was last updated. See Section 17.1, lqMySQL Cluster Overviewrq, and Section 17.5.4.2, lqMySQL Cluster Log Eventsrq, for more information about checkpoints.</dl>
<dl>
<dt>
<dd> * <code>&#8211;tupscan</code>, <code>-t</code> </p>
<p> Scan the table in the order of the tuples.</dl>
<dl>
<dt>
<dd> * <code>&#8211;nodata</code> </p>
<p> Causes any table data to be omitted.</dl>
<p> <code>Sample Output</code>: </p>
<p> Output from a MySQL SELECT statement: </p>
<dl>
<dt>
<dd>
<pre><code>
mysql &gt; SELECT *FROM ctest1.fish;
+ -- --+-- -- -- -- -- -+ | id | name |
    +-- --+-- -- -- -- -- -+ | 3 | shark |
    | 6 | puffer |
    | 2 | tuna |
    | 4 | manta ray |
    | 5 | grouper |
    | 1 | guppy |
    +-- --+-- -- -- -- -- -+6 rows in set(0.04 sec)
</code></pre>
</dl>
<p> Output from the equivalent invocation of <code>ndb_select_all</code>: </p>
<dl>
<dt>
<dd>
shell &gt;./ ndb_select_all &#8211; c localhost fish &#8211; d ctest1 id name 3 [shark] 6 [puffer] 2 [tuna] 4 [manta ray] 5 [grouper] 1 [guppy] 6 rows returned NDBT_ProgramExit : 0 &#8211; OK
</dl>
<p> Note that all string values are enclosed by square brackets (lq[&#8230;]rq) in the output of <code>ndb_select_all</code>. For a further example, consider the table created and populated as shown here: </p>
<dl>
<dt>
<dd>
CREATE TABLE dogs(<br />
    id INT(11) NOT NULL AUTO_INCREMENT,<br />
    name VARCHAR(25) NOT NULL,<br />
    breed VARCHAR(50) NOT NULL,<br />
    PRIMARY KEY pk(id),<br />
    KEY ix(name))<br />
    TABLESPACE ts STORAGE DISK<br />
    ENGINE = NDBCLUSTER;<br />
INSERT INTO dogs VALUES(&#8221;, &#8216;Lassie&#8217;, &#8216;collie&#8217;),<br />
    (&#8221;, &#8216;Scooby-Doo&#8217;, &#8216;Great Dane&#8217;),<br />
    (&#8221;, &#8216;Rin-Tin-Tin&#8217;, &#8216;Alsatian&#8217;),<br />
    (&#8221;, &#8216;Rosscoe&#8217;, &#8216;Mutt&#8217;);
</dl>
<p> This demonstrates the use of several additional <code>ndb_select_all</code> options: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt;./ ndb_select_all - d ctest1 dogs - o ix - z-- gci-- disk GCI id name breed DISK_REF 834461 2 [Scooby - Doo][Great Dane] [m_file_no:0 m_page:98 m_page_idx:0] 834878 4 [Rosscoe][Mutt] [m_file_no:0 m_page:98 m_page_idx:16] 834463 3 [Rin - Tin - Tin][Alsatian] [m_file_no:0 m_page:34 m_page_idx:0] 835657 1 [Lassie][Collie] [m_file_no:0 m_page:66 m_page_idx:0] 4 rows returned NDBT_ProgramExit : 0 - OK
</code></pre>
</dl>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
