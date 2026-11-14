---
title: "ndb_desc(1)"
name: "ndb_desc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_desc/"
description: "ndb_desc – describe NDB tables"
---

<h2 class="name">NAME</h2>
<p> ndb_desc &#8211; describe NDB tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_desc </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_desc</code></p>
<dd>provides a detailed description of one or more NDB tables. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_desc -c <i>connect_string</i> <i>tbl_name</i> -d <i>db_name</i> [-p]
</pre>
</dl>
<p> <code>Sample Output</code>: </p>
<p> MySQL table creation and population statements: </p>
<dl>
<dt>
<dd>
<pre><code>
USE test;
CREATE TABLE fish(
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    length_mm INT(11) NOT NULL,
    weight_gm INT(11) NOT NULL,
    PRIMARY KEY pk(id),
    UNIQUE KEY uk(name)) ENGINE = NDB;
INSERT INTO fish VALUES('', 'guppy', 35, 2), ('', 'tuna', 2500, 150000),
    ('', 'shark', 3000, 110000), ('', 'manta ray', 1500, 50000),
    ('', 'grouper', 900, 125000), ('', 'puffer', 250, 2500);
</code></pre>
</dl>
<p> Output from <code>ndb_desc</code>: </p>
<dl>
<dt>
<dd>
shell &gt;./ ndb_desc &#8211; c localhost fish &#8211; d test &#8211; p&#8211; fish&#8211; Version : 2 Fragment type : 9 K Value : 6 Min load factor : 78 Max load factor : 80 Temporary table : no Number of attributes : 4 Number of primary keys : 1 Length of frm data : 311 Row Checksum : 1 Row GCI : 1 SingleUserMode : 0 ForceVarPart : 1 FragmentCount : 2 TableStatus : Retrieved&#8211; Attributes&#8211; id Int PRIMARY KEY DISTRIBUTION KEY AT = FIXED ST = MEMORY AUTO_INCR<br />
    name Varchar(20; latin1_swedish_ci) NOT NULL AT = SHORT_VAR ST = MEMORY<br />
        length_mm Int NOT NULL AT = FIXED ST = MEMORY<br />
            weight_gm Int NOT NULL AT = FIXED ST = MEMORY&#8211; Indexes&#8211; PRIMARY KEY(id) &#8211; UniqueHashIndex PRIMARY(id) &#8211; OrderedIndex uk$unique(name) &#8211; UniqueHashIndex uk(name) &#8211; OrderedIndex&#8211; Per partition info&#8211; Partition Row count Commit count Frag fixed memory Frag varsized memory Extent_space Free extent_space 0 2 2 32768 32768 0 0 1 4 4 32768 32768 0 0 NDBT_ProgramExit : 0 &#8211; OK
</dl>
<p> Information about multiple tables can be obtained in a single invocation of <code>ndb_desc</code> by using their names, separated by spaces. All of the tables must be in the same database. </p>
<p> The Extent_space and Free extent_space columns were added in MySQL Cluster NDB 6.3.27 and MySQL Cluster NDB 7.0.8. They are applicable only to NDB tables having columns on disk; for tables having only in-memory columns, these columns always contain the value 0. </p>
<p> To illustrate their use, we modify the previous example. First, we must create the necessary Disk Data objects, as shown here: </p>
<dl>
<dt>
<dd>
CREATE LOGFILE GROUP lg_1<br />
    ADD UNDOFILE &#8216;undo_1.log&#8217; INITIAL_SIZE 16M UNDO_BUFFER_SIZE 2M ENGINE NDB;<br />
ALTER LOGFILE GROUP lg_1<br />
    ADD UNDOFILE &#8216;undo_2.log&#8217; INITIAL_SIZE 12M ENGINE NDB;<br />
CREATE TABLESPACE ts_1<br />
    ADD DATAFILE &#8216;data_1.dat&#8217; USE LOGFILE GROUP lg_1<br />
        INITIAL_SIZE 32M ENGINE NDB;<br />
ALTER TABLESPACE ts_1<br />
    ADD DATAFILE &#8216;data_2.dat&#8217; INITIAL_SIZE 48M ENGINE NDB;
</dl>
<p> (For more information on the statements just shown and the objects created by them, see Section 17.5.10.1, lqMySQL Cluster Disk Data Objectsrq, as well as Section 12.1.14, lqCREATE LOGFILE GROUP Syntaxrq, and Section 12.1.18, lqCREATE TABLESPACE Syntaxrq.) </p>
<p> Now we can create and populate a version of the fish table that stores 2 of its columns on disk (deleting the previous version of the table first, if it already exists): </p>
<dl>
<dt>
<dd>
CREATE TABLE fish(<br />
    id INT(11) NOT NULL AUTO_INCREMENT,<br />
    name VARCHAR(20) NOT NULL,<br />
    length_mm INT(11) NOT NULL,<br />
    weight_gm INT(11) NOT NULL,<br />
    PRIMARY KEY pk(id),<br />
    UNIQUE KEY uk(name)) TABLESPACE ts_1 STORAGE DISK<br />
    ENGINE = NDB;<br />
INSERT INTO fish VALUES(&#8221;, &#8216;guppy&#8217;, 35, 2), (&#8221;, &#8216;tuna&#8217;, 2500, 150000),<br />
    (&#8221;, &#8216;shark&#8217;, 3000, 110000), (&#8221;, &#8216;manta ray&#8217;, 1500, 50000),<br />
    (&#8221;, &#8216;grouper&#8217;, 900, 125000), (&#8221;, &#8216;puffer&#8217;, 250, 2500);
</dl>
<p> When run against this version of the table, <code>ndb_desc</code> displays the following output: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt;./ ndb_desc - c localhost fish - d test - p-- fish-- Version : 3 Fragment type : 9 K Value : 6 Min load factor : 78 Max load factor : 80 Temporary table : no Number of attributes : 4 Number of primary keys : 1 Length of frm data : 321 Row Checksum : 1 Row GCI : 1 SingleUserMode : 0 ForceVarPart : 1 FragmentCount : 2 TableStatus : Retrieved-- Attributes-- id Int PRIMARY KEY DISTRIBUTION KEY AT = FIXED ST = MEMORY AUTO_INCR
    name Varchar(20; latin1_swedish_ci) NOT NULL AT = SHORT_VAR ST = MEMORY
        length_mm Int NOT NULL AT = FIXED ST = DISK
            weight_gm Int NOT NULL AT = FIXED ST = DISK-- Indexes-- PRIMARY KEY(id) - UniqueHashIndex PRIMARY(id) - OrderedIndex uk$unique(name) - UniqueHashIndex uk(name) - OrderedIndex-- Per partition info-- Partition Row count Commit count Frag fixed memory Frag varsized memory Extent_space Free extent_space 0 2 2 32768 32768 1048576 1044440 1 4 4 32768 32768 1048576 1044400 NDBT_ProgramExit : 0 - OK
</code></pre>
</dl>
<p> This means that 1048576 bytes are allocated from the tablespace for this table on each partition, of which 1044440 bytes remain free for additional storage. In other words, 1048576 &#8211; 1044440 = 4136 bytes per partition is currently being used to store the data from this table&#8217;s disk-based columns. The number of bytes shown as Free extent_space is available for storing on-disk column data from the fish table only; for this reason, it is not visible when selecting from the INFORMATION_SCHEMA.FILES table. </p>
<p> <code>Additional Options</code>: </p>
<dl>
<dt>
<dd> * <code>&#8211;extra-partition-info</code>, <code>-p</code> </p>
<p> Print additional information about the table&#8217;s partitions.</dl>
<dl>
<dt>
<dd> * <code>&#8211;blob-info</code>, <code>-b</code> </p>
<p> Include information about subordinate BLOB and TEXT columns. </p>
<p> Use of this option also requires the use of the <code>&#8211;extra-partition-info</code> (<code>-p</code>) option. </p>
<p> This option was added in MySQL Cluster NDB 6.3.32, MySQL Cluster NDB 7.0.13, and MySQL Cluster NDB 7.1.2.</dl>
<dl>
<dt>
<dd> * <code>&#8211;extra-node-info</code>, <code>-n</code> </p>
<p> Include information about the mappings between table partitions and the data nodes upon which they reside. This information can be useful for verifying distribution awareness mechanisms and supporting more efficient application access to the data stored in MySQL Cluster. </p>
<p> Use of this option also requires the use of the <code>&#8211;extra-partition-info</code> (<code>-p</code>) option. </p>
<p> This option was added in MySQL Cluster NDB 6.2.19, MySQL Cluster NDB 6.3.33, MySQL Cluster NDB 7.0.14, and MySQL Cluster NDB 7.1.2.</dl>
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
