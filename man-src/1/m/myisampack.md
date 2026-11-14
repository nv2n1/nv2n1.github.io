---
title: "myisampack(1)"
name: "myisampack"
section: "1"
letter: "m"
url: "/docs/linux/man/1-myisampack/"
description: "myisampack – generate compressed, read-only MyISAM tables"
---

<h2 class="name">NAME</h2>
<p> myisampack &#8211; generate compressed, read-only MyISAM tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>myisampack [</code><i>options</i><code>] </code><i>file_name</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>myisampack</code> utility compresses MyISAM tables. <code>myisampack</code> works by compressing each column in the table separately. Usually, <code>myisampack</code> packs the data file 40% to 70%. </p>
<p> When the table is used later, the server reads into memory the information needed to decompress columns. This results in much better performance when accessing individual rows, because you only have to uncompress exactly one row. </p>
<p> MySQL uses mmap() when possible to perform memory mapping on compressed tables. If mmap() does not work, MySQL falls back to normal read/write file operations. </p>
<p> Please note the following: </p>
<dl>
<dt>
<dd> &bull; If the <code>mysqld</code> server was invoked with external locking disabled, it is not a good idea to invoke <code>myisampack</code> if the table might be updated by the server during the packing process. It is safest to compress tables with the server stopped.</dl>
<dl>
<dt>
<dd> &bull; After packing a table, it becomes read only. This is generally intended (such as when accessing packed tables on a CD).</dl>
<dl>
<dt>
<dd> &bull; <code>myisampack</code> does not support partitioned tables.</dl>
<p> Invoke <code>myisampack</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisampack [</code><i>options</i><code>] </code><i>file_name</i><code> ...</code>
</pre>
</dl>
<p> Each file name argument should be the name of an index (.MYI) file. If you are not in the database directory, you should specify the path name to the file. It is permissible to omit the .MYI extension. </p>
<p> After you compress a table with <code>myisampack</code>, use <code>myisamchk -rq</code> to rebuild its indexes. <code><a href="/docs/linux/man/1-myisamchk/">myisamchk</a></code>(1). </p>
<p> <code>myisampack</code> supports the following options. It also reads option files and supports the options for processing them described at Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;backup</code>, <code>-b</code> </p>
<p> Make a backup of each table&#8217;s data file using the name <i>tbl_name</i>.OLD.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>dir_name</i> </p>
<p> The directory where character sets are installed. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code>, <code>-f</code> </p>
<p> Produce a packed table even if it becomes larger than the original or if the intermediate file from an earlier invocation of <code>myisampack</code> exists. (<code>myisampack</code> creates an intermediate file named <i>tbl_name</i>.TMD in the database directory while it compresses the table. If you kill <code>myisampack</code>, the .TMD file might not be deleted.) Normally, <code>myisampack</code> exits with an error if it finds that <i>tbl_name</i>.TMD exists. With <code>&#8211;force</code>, <code>myisampack</code> packs the table anyway.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;join=</code><i>big_tbl_name</i>, <code>-j </code><i>big_tbl_name</i> </p>
<p> Join all tables named on the command line into a single packed table <i>big_tbl_name</i>. All tables that are to be combined <i>must</i> have identical structure (same column names and types, same indexes, and so forth). </p>
<p> <i>big_tbl_name</i> must not exist prior to the join operation. All source tables named on the command line to be merged into <i>big_tbl_name</i> must exist. The source tables are read for the join operation but not modified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Silent mode. Write output only when errors occur.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;test</code>, <code>-t</code> </p>
<p> Do not actually pack the table, just test packing it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tmpdir=</code><i>dir_name</i>, <code>-T </code><i>dir_name</i> </p>
<p> Use the named directory as the location where <code>myisampack</code> creates temporary files.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Write information about the progress of the packing operation and its result.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;wait</code>, <code>-w</code> </p>
<p> Wait and retry if the table is in use. If the <code>mysqld</code> server was invoked with external locking disabled, it is not a good idea to invoke <code>myisampack</code> if the table might be updated by the server during the packing process.</dl>
<p> The following sequence of commands illustrates a typical table compression session: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; ls - l station.*-rw - rw - r-- 1 jones my 994128 Apr 17 19 : 00 station.MYD - rw - rw - r-- 1 jones my 53248 Apr 17 19 : 00 station.MYI shell &gt; myisamchk - dvv station MyISAM file : station Isam - version : 2 Creation time : 1996 - 03 - 13 10 : 08 : 58 Recover time : 1997 - 02 - 02 3 : 06 : 43 Data records : 1192 Deleted blocks : 0 Datafile parts : 1192 Deleted data : 0 Datafile pointer(bytes) : 2 Keyfile pointer(bytes) : 2 Max datafile length : 54657023 Max keyfile length : 33554431 Recordlength : 834 Record format : Fixed length table description : Key Start Len Index Type Root Blocksize Rec / key 1 2 4 unique unsigned long 1024 1024 1 2 32 30 multip.text 10240 1024 1 Field Start Length Type 1 1 1 2 2 4 3 6 4 4 10 1 5 11 20 6 31 1 7 32 30 8 62 35 9 97 35 10 132 35 11 167 4 12 171 16 13 187 35 14 222 4 15 226 16 16 242 20 17 262 20 18 282 20 19 302 30 20 332 4 21 336 4 22 340 1 23 341 8 24 349 8 25 357 8 26 365 2 27 367 2 28 369 4 29 373 4 30 377 1 31 378 2 32 380 8 33 388 4 34 392 4 35 396 4 36 400 4 37 404 1 38 405 4 39 409 4 40 413 4 41 417 4 42 421 4 43 425 4 44 429 20 45 449 30 46 479 1 47 480 1 48 481 79 49 560 79 50 639 79 51 718 79 52 797 8 53 805 1 54 806 1 55 807 20 56 827 4 57 831 4 shell &gt; myisampack station.MYI
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Compressing station.MYI : (1192 records) -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Calculating statistics
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  normal : 20 empty
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  - space : 16 empty - zero : 12 empty - fill : 11 pre - space : 0 end - space : 12 table - lookups : 5 zero : 7 Original trees : 57 After join : 17 - Compressing file 87.14 % Remember to run myisamchk - rq on compressed tables shell
    &gt; myisamchk - rq station
          - check record delete - chain
          - recovering(with sort) MyISAM - table 'station' Data records : 1192 - Fixing index 1 - Fixing index 2 shell
    &gt; mysqladmin - uroot flush - tables shell &gt; ls - l station.*-rw - rw - r-- 1 jones my 127874 Apr 17 19 : 00 station.MYD
                                                    - rw - rw - r-- 1 jones my 55296 Apr 17 19 : 04 station.MYI shell
    &gt; myisamchk - dvv station MyISAM file : station Isam - version : 2 Creation time : 1996 - 03 - 13 10 : 08 : 58 Recover time : 1997 - 04 - 17 19 : 04 : 26 Data records : 1192 Deleted blocks : 0 Datafile parts : 1192 Deleted data : 0 Datafile pointer(bytes) : 3 Keyfile pointer(bytes) : 1 Max datafile length : 16777215 Max keyfile length : 131071 Recordlength : 834 Record format : Compressed table description : Key Start Len Index Type Root Blocksize Rec / key 1 2 4 unique unsigned long 10240 1024 1 2 32 30 multip.text 54272 1024 1 Field Start Length Type Huff tree Bits 1 1 1 constant 1 0 2 2 4 zerofill(1) 2 9 3 6 4 no zeros,
    zerofill(1) 2 9 4 10 1 3 9 5 11 20 table - lookup 4 0 6 31 1 3 9 7 32 30 no endspace, not_always 5 9 8 62 35 no endspace, not_always, no empty 6 9 9 97 35 no empty 7 9 10 132 35 no endspace, not_always, no empty 6 9 11 167 4 zerofill(1) 2 9 12 171 16 no endspace, not_always, no empty 5 9 13 187 35 no endspace, not_always, no empty 6 9 14 222 4 zerofill(1) 2 9 15 226 16 no endspace, not_always, no empty 5 9 16 242 20 no endspace, not_always 8 9 17 262 20 no endspace, no empty 8 9 18 282 20 no endspace, no empty 5 9 19 302 30 no endspace, no empty 6 9 20 332 4 always zero 2 9 21 336 4 always zero 2 9 22 340 1 3 9 23 341 8 table - lookup 9 0 24 349 8 table - lookup 10 0 25 357 8 always zero 2 9 26 365 2 2 9 27 367 2 no zeros, zerofill(1) 2 9 28 369 4 no zeros, zerofill(1) 2 9 29 373 4 table - lookup 11 0 30 377 1 3 9 31 378 2 no zeros, zerofill(1) 2 9 32 380 8 no zeros 2 9 33 388 4 always zero 2 9 34 392 4 table - lookup 12 0 35 396 4 no zeros, zerofill(1) 13 9 36 400 4 no zeros, zerofill(1) 2 9 37 404 1 2 9 38 405 4 no zeros 2 9 39 409 4 always zero 2 9 40 413 4 no zeros 2 9 41 417 4 always zero 2 9 42 421 4 no zeros 2 9 43 425 4 always zero 2 9 44 429 20 no empty 3 9 45 449 30 no empty 3 9 46 479 1 14 4 47 480 1 14 4 48 481 79 no endspace, no empty 15 9 49 560 79 no empty 2 9 50 639 79 no empty 2 9 51 718 79 no endspace 16 9 52 797 8 no empty 2 9 53 805 1 17 1 54 806 1 3 9 55 807 20 no empty 3 9 56 827 4 no zeros, zerofill(2) 2 9 57 831 4 no zeros, zerofill(1) 2 9
</code></pre>
</dl>
<p> <code>myisampack</code> displays the following kinds of information: </p>
<dl>
<dt>
<dd> &bull; normal </p>
<p> The number of columns for which no extra packing is used.</dl>
<dl>
<dt>
<dd> &bull; empty-space </p>
<p> The number of columns containing values that are only spaces. These occupy one bit.</dl>
<dl>
<dt>
<dd> &bull; empty-zero </p>
<p> The number of columns containing values that are only binary zeros. These occupy one bit.</dl>
<dl>
<dt>
<dd> &bull; empty-fill </p>
<p> The number of integer columns that do not occupy the full byte range of their type. These are changed to a smaller type. For example, a BIGINT column (eight bytes) can be stored as a TINYINT column (one byte) if all its values are in the range from -128 to 127.</dl>
<dl>
<dt>
<dd> &bull; pre-space </p>
<p> The number of decimal columns that are stored with leading spaces. In this case, each value contains a count for the number of leading spaces.</dl>
<dl>
<dt>
<dd> &bull; end-space </p>
<p> The number of columns that have a lot of trailing spaces. In this case, each value contains a count for the number of trailing spaces.</dl>
<dl>
<dt>
<dd> &bull; table-lookup </p>
<p> The column had only a small number of different values, which were converted to an ENUM before Huffman compression.</dl>
<dl>
<dt>
<dd> &bull; zero </p>
<p> The number of columns for which all values are zero.</dl>
<dl>
<dt>
<dd> &bull; Original trees </p>
<p> The initial number of Huffman trees.</dl>
<dl>
<dt>
<dd> &bull; After join </p>
<p> The number of distinct Huffman trees left after joining trees to save some header space.</dl>
<p> After a table has been compressed, the Field lines displayed by <code>myisamchk -dvv</code> include additional information about each column: </p>
<dl>
<dt>
<dd> &bull; Type </p>
<p> The data type. The value may contain any of the following descriptors: </p>
<dl>
<dt>
<dd> &bull; constant </p>
<p> All rows have the same value.</dl>
<dl>
<dt>
<dd> &bull; no endspace </p>
<p> Do not store endspace.</dl>
<dl>
<dt>
<dd> &bull; no endspace, not_always </p>
<p> Do not store endspace and do not do endspace compression for all values.</dl>
<dl>
<dt>
<dd> &bull; no endspace, no empty </p>
<p> Do not store endspace. Do not store empty values.</dl>
<dl>
<dt>
<dd> &bull; table-lookup </p>
<p> The column was converted to an ENUM.</dl>
<dl>
<dt>
<dd> &bull; zerofill(<i>N</i>) </p>
<p> The most significant <i>N</i> bytes in the value are always 0 and are not stored.</dl>
<dl>
<dt>
<dd> &bull; no zeros </p>
<p> Do not store zeros.</dl>
<dl>
<dt>
<dd> &bull; always zero </p>
<p> Zero values are stored using one bit.</dl>
</dl>
<dl>
<dt>
<dd> &bull; Huff tree </p>
<p> The number of the Huffman tree associated with the column.</dl>
<dl>
<dt>
<dd> &bull; Bits </p>
<p> The number of bits used in the Huffman tree.</dl>
<p> After you run <code>myisampack</code>, use <code>myisamchk</code> to re-create any indexes. At this time, you can also sort the index blocks and create statistics needed for the MySQL optimizer to work more efficiently: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk -rq --sort-index --analyze </code><i>tbl_name</i><code>.MYI</code>
</pre>
</dl>
<p> After you have installed the packed table into the MySQL database directory, you should execute <code>mysqladmin flush-tables</code> to force <code>mysqld</code> to start using the new table. </p>
<p> To unpack a packed table, use the <code>&#8211;unpack</code> option to <code>myisamchk</code>.</p>
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
