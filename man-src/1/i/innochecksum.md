---
title: "innochecksum(1)"
name: "innochecksum"
section: "1"
letter: "i"
url: "/docs/linux/man/1-innochecksum/"
description: "innochecksum – offline InnoDB file checksum utility"
---

<h2 class="name">NAME</h2>
<p> innochecksum &#8211; offline InnoDB file checksum utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>innochecksum [</code><i>options</i><code>] </code><i>file_name</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>innochecksum</code></p>
<dd>prints checksums for InnoDB files. This tool reads an InnoDB tablespace file, calculates the checksum for each page, compares the calculated checksum to the stored checksum, and reports mismatches, which indicate damaged pages. It was originally developed to speed up verifying the integrity of tablespace files after power outages but can also be used after file copies. Because checksum mismatches cause InnoDB to deliberately shut down a running server, it may be preferable to use this tool rather than waiting for an in-production server to encounter the damaged pages. </p>
<p> <code>innochecksum</code> cannot be used on tablespace files that the server already has open. For such files, you should use CHECK TABLE to check tables within the tablespace. Attempting to run <code>innochecksum</code> on a tablespace that the server already has open will result in an &#8220;Unable to lock file&#8221; error. </p>
<p> If checksum mismatches are found, you would normally restore the tablespace from backup or start the server and attempt to use <code>mysqldump</code> to make a backup of the tables within the tablespace. </p>
<p> Invoke <code>innochecksum</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum [</code><i>options</i><code>] </code><i>file_name</i>
</pre>
</dl>
<p> innochecksum Options </p>
<p> <code>innochecksum</code> supports the following options. For options that refer to page numbers, the numbers are zero-based. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Displays command line help. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --help</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;info</code>, <code>-I</code> </p>
<p> Synonym for <code>&#8211;help</code>. Displays command line help. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --info</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Displays version information. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --version</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode; prints a progress indicator to the log file every five seconds. In order for the progress indicator to be printed, the log file must be specified using the &#8211;log option. To turn on verbose mode, run: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --verbose</code>
</pre>
</dl>
<p> To turn off verbose mode, run: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --verbose=FALSE</code>
</pre>
</dl>
<p> The &#8211;verbose option and &#8211;log option can be specified at the same time. For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --verbose --log=/var/lib/mysql/test/logtest.txt</code>
</pre>
</dl>
<p> To locate the progress indicator information in the log file, you can perform the following search: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>cat ./logtest.txt | grep -i &quot;okay&quot;</code>
</pre>
</dl>
<p> The progress indicator information in the log file appears similar to the following: </p>
<dl>
<dt>
<dd>
<pre>
page 1663 okay: 2.863% done
page 8447 okay: 14.537% done
page 13695 okay: 23.568% done
page 18815 okay: 32.379% done
page 23039 okay: 39.648% done
page 28351 okay: 48.789% done
page 33023 okay: 56.828% done
page 37951 okay: 65.308% done
page 44095 okay: 75.881% done
page 49407 okay: 85.022% done
page 54463 okay: 93.722% done
...
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;count</code>, <code>-c</code> </p>
<p> Print a count of the number of pages in the file and exit. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --count ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;start-page=</code><i>num</i>, <code>-s </code><i>num</i> </p>
<p> Start at this page number. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --start-page=600 ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> or: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum -s 600 ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;end-page=</code><i>num</i>, <code>-e </code><i>num</i> </p>
<p> End at this page number. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --end-page=700 ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> or: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --p 700 ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;page=</code><i>num</i>, <code>-p </code><i>num</i> </p>
<p> Check only this page number. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --page=701 ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;strict-check</code>, <code>-C</code> </p>
<p> Specify a strict checksum algorithm. Options include innodb, crc32, and none. </p>
<p> In this example, the innodb checksum algorithm is specified: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --strict-check=innodb ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> In this example, the crc32 checksum algorithm is specified: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum -C crc32 ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> The following conditions apply: </p>
<dl>
<dt>
<dd> &bull; If you do not specify the <code>&#8211;strict-check</code> option, <code>innochecksum</code> validates against innodb, crc32 and none.</dl>
<dl>
<dt>
<dd> &bull; If you specify the none option, only checksums generated by none are allowed.</dl>
<dl>
<dt>
<dd> &bull; If you specify the innodb option, only checksums generated by innodb are allowed.</dl>
<dl>
<dt>
<dd> &bull; If you specify the crc32 option, only checksums generated by crc32 are allowed.</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-check</code>, <code>-n</code> </p>
<p> Ignore the checksum verification when rewriting a checksum. This option may only be used with the <code>innochecksum</code> <code>&#8211;write</code> option. If the <code>&#8211;write</code> option is not specified, <code>innochecksum</code> will terminate. </p>
<p> In this example, an innodb checksum is rewritten to replace an invalid checksum: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --no-check --write innodb ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;allow-mismatches</code>, <code>-a</code> </p>
<p> The maximum number of checksum mismatches allowed before <code>innochecksum</code> terminates. The default setting is 0. If &#8211;allow-mismatches=<i>N</i>, where <i>N</i>&gt;=0, <i>N</i> mismatches are permitted and <code>innochecksum</code> terminates at <i>N</i>+1. When &#8211;allow-mismatches is set to 0, <code>innochecksum</code> terminates on the first checksum mismatch. </p>
<p> In this example, an existing innodb checksum is rewritten to set &#8211;allow-mismatches to 1. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --allow-mismatches=1 --write innodb ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> With &#8211;allow-mismatches set to 1, if there is a mismatch at page 600 and another at page 700 on a file with 1000 pages, the checksum is updated for pages 0-599 and 601-699. Because &#8211;allow-mismatches is set to 1, the checksum tolerates the first mismatch and terminates on the second mismatch, leaving page 600 and pages 700-999 unchanged.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;write=</code><i>name</i>, <code>-w </code><i>num</i> </p>
<p> Rewrite a checksum. When rewriting an invalid checksum, the <code>&#8211;no-check</code> option must be used together with the <code>&#8211;write</code> option. The <code>&#8211;no-check</code> option tells <code>innochecksum</code> to ignore verification of the invalid checksum. You do not have to specify the <code>&#8211;no-check</code> option if the current checksum is valid. </p>
<p> An algorithm must be specified when using the <code>&#8211;write</code> option. Possible values for the <code>&#8211;write</code> option are: </p>
<dl>
<dt>
<dd> &bull; innodb: A checksum calculated in software, using the original algorithm from InnoDB.</dl>
<dl>
<dt>
<dd> &bull; crc32: A checksum calculated using the crc32 algorithm, possibly done with a hardware assist.</dl>
<dl>
<dt>
<dd> &bull; none: A constant number.</dl>
<p> The <code>&#8211;write</code> option rewrites entire pages to disk. If the new checksum is identical to the existing checksum, the new checksum is not written to disk in order to minimize I/O. </p>
<p> <code>innochecksum</code> obtains an exclusive lock when the <code>&#8211;write</code> option is used. </p>
<p> In this example, a crc32 checksum is written for tab1.ibd: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum -w crc32 ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> In this example, a crc32 checksum is rewritten to replace an invalid crc32 checksum: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --no-check --write crc32 ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;page-type-summary</code>, <code>-S</code> </p>
<p> Display a count of each page type in a tablespace. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --page-type-summary ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> Sample output for &#8211;page-type-summary: </p>
<dl>
<dt>
<dd>
<pre><code>
File::../ data / test / tab1.ibd == == == == == == == == PAGE TYPE SUMMARY == == == == == == ==
#PAGE_COUNT PAGE_TYPE
    == == == == == == == == == == == == == == == == == == == == == == ==
    =
        2 Index page 0 Undo log page 1 Inode page 0 Insert buffer free list page 2 Freshly allocated page 1 Insert buffer bitmap 0 System page 0 Transaction system page 1 File Space Header 0 Extent descriptor page 0 BLOB page 0 Compressed BLOB page 0 Other type of page == == == == == == == == == == == == == == == == == == == == == == == =
                                                                                                                                                                                                                                                                                                                                                       Additional information : Undo page type : 0 insert,
                                                                                                                                                                                                                                                                                                                                                0 update, 0 other Undo page state : 0 active, 0 cached, 0 to_free, 0 to_purge, 0 prepared, 0 other
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;page-type-dump</code>, <code>-D</code> </p>
<p> Dump the page type information for each page in a tablespace to stderr or stdout. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --page-type-dump=/tmp/a.txt ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;log</code>, <code>-l</code> </p>
<p> Log output for the <code>innochecksum</code> tool. A log file name must be provided. Log output contains checksum values for each tablespace page. For uncompressed tables, LSN values are also provided. The <code>&#8211;log</code> replaces the &#8211;debug option, which was available in earlier releases. Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum --log=/tmp/log.txt ../data/test/tab1.ibd</code>
</pre>
</dl>
<p> or: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>innochecksum -l /tmp/log.txt ../data/test/tab1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; &#8211; option. </p>
<p> Specify the &#8211; option to read from standard input. If the &#8211; option is missing when &#8220;read from standard in&#8221; is expected, <code>innochecksum</code> will output <code>innochecksum</code> usage information indicating that the &#8220;-&#8221; option was omitted. Example usages: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>cat t1.ibd | innochecksum -</code>
</pre>
</dl>
<p> In this example, <code>innochecksum</code> writes the crc32 checksum algorithm to a.ibd without changing the original t1.ibd file. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>cat t1.ibd | innochecksum --write=crc32 - &gt; a.ibd</code>
</pre>
</dl>
</dl>
<p> Running innochecksum on Multiple User-defined Tablespace Files </p>
<p> The following examples demonstrate how to run <code>innochecksum</code> on multiple user-defined tablespace files (.ibd files). </p>
<p> Run <code>innochecksum</code> for all tablespace (.ibd) files in the &#8220;test&#8221; database: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; innochecksum ./data/test/*.ibd
</pre>
</dl>
<p> Run <code>innochecksum</code> for all tablespace files (.ibd files) that have a file name starting with &#8220;t&#8221;: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; innochecksum ./data/test/t*.ibd
</pre>
</dl>
<p> Run <code>innochecksum</code> for all tablespace files (.ibd files) in the data directory: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; innochecksum ./data/*/*.ibd
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Running <code>innochecksum</code> on multiple user-defined tablespace files is not supported on Windows operating systems, as Windows shells such as <code>cmd.exe</code> do not support glob pattern expansion. On Windows systems, <code>innochecksum</code> must be run separately for each user-defined tablespace file. For example: </p>
<dl>
<dt>
<dd>
<pre>
cmd&gt; innochecksum.exe t1.ibd
cmd&gt; innochecksum.exe t2.ibd
cmd&gt; innochecksum.exe t3.ibd
</pre>
</dl>
</dl>
<p> Running innochecksum on Multiple System Tablespace Files </p>
<p> By default, there is only one InnoDB system tablespace file (ibdata1) but multiple files for the system tablespace can be defined using the innodb_data_file_path option. In the following example, three files for the system tablespace are defined using the innodb_data_file_path option: ibdata1, ibdata2, and ibdata3. </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt;./ bin / mysqld-- no - defaults-- innodb - data - file - path = "ibdata1:10M;ibdata2:10M;ibdata3:10M:autoextend"
</code></pre>
</dl>
<p> The three files (ibdata1, ibdata2, and ibdata3) form one logical system tablespace. To run <code>innochecksum</code> on multiple files that form one logical system tablespace, <code>innochecksum</code> requires the &#8211; option to read tablespace files in from standard input, which is equivalent to concatenating multiple files to create one single file. For the example provided above, the following <code>innochecksum</code> command would be used: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; cat ibdata* | innochecksum -
</pre>
</dl>
<p> Refer to the <code>innochecksum</code> options information for more information about the &#8220;-&#8221; option. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Running <code>innochecksum</code> on multiple files in the same tablespace is not supported on Windows operating systems, as Windows shells such as <code>cmd.exe</code> do not support glob pattern expansion. On Windows systems, <code>innochecksum</code> must be run separately for each system tablespace file. For example: </p>
<dl>
<dt>
<dd>
<pre>
cmd&gt; innochecksum.exe ibdata1
cmd&gt; innochecksum.exe ibdata2
cmd&gt; innochecksum.exe ibdata3
</pre>
</dl>
</dl>
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
