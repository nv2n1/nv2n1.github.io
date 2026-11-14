---
title: "ibd2sdi(1)"
name: "ibd2sdi"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibd2sdi/"
description: "ibd2sdi – InnoDB utility for extracting serialized dictionary information (SDI) from an InnoDB tablespace"
---

<h2 class="name">NAME</h2>
<p> ibd2sdi &#8211; InnoDB utility for extracting serialized dictionary information (SDI) from an InnoDB tablespace </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ibd2sdi [</code><i>options</i><code>] </code><i>file_name1</i><code> [</code><i>file_name2 file_name3 &#8230;]</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ibd2sdi</code></p>
<dd>is a utility for extracting serialized dictionary information (SDI) from InnoDB tablespace files. SDI data is present all persistent InnoDB tablespace files. </p>
<p> <code>ibd2sdi</code> can be run on file-per-table tablespace files (*.ibd files), general tablespace files (*.ibd files), system tablespace files (ibdata* files), and the data dictionary tablespace (mysql.ibd). It is not supported for use with temporary tablespaces or undo tablespaces. </p>
<p> <code>ibd2sdi</code> can be used at runtime or while the server is offline. During DDL operations, ROLLBACK operations, and undo log purge operations related to SDI, there may be a short interval of time when <code>ibd2sdi</code> fails to read SDI data stored in the tablespace. </p>
<p> <code>ibd2sdi</code> performs an uncommitted read of SDI from the specified tablespace. Redo logs and undo logs are not accessed. </p>
<p> Invoke the <code>ibd2sdi</code> utility like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; ibd2sdi[options] file_name1[file_name2 file_name3...]
</code></pre>
</dl>
<p> <code>ibd2sdi</code> supports multi-file tablespaces like the InnoDB system tablespace, but it cannot be run on more than one tablespace at a time. For multi-file tablespaces, specify each file: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi ibdata1 ibdata2</code>
</pre>
</dl>
<p> The files of a multi-file tablespace must be specified in order of the ascending page number. If two successive files have the same space ID, the later file must start with the last page number of the previous file + 1. </p>
<p> <code>ibd2sdi</code> outputs SDI (containing id, type, and data fields) in JSON format. ibd2sdi Options </p>
<p> <code>ibd2sdi</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-h</code> </p>
<p> Displays command-line help. </p>
<dl>
<dt>
<dd>
shell &gt; ibd2sdi&#8211; help<br />
                Usage :./<br />
            ibd2sdi[-v][-c&lt;strict &#8211; check&gt;][-d&lt;dump file name&gt;][-n] filename1[filenames] See http : // dev.mysql.com/doc/refman/8.0/en/ibd2sdi.html for usage hints.<br />
                                                                                                    -h,<br />
    &#8211;help Display this help and exit.- v, &#8211;version Display version information and exit.- #, &#8211;debug[= name] Output debug log.See http : // dev.mysql.com/doc/refman/8.0/en/dbug-package.html<br />
                                                                                                                                           -d,<br />
    &#8211;dump &#8211; file = name<br />
                        Dump the tablespace SDI into the file passed by user.Without the filename,<br />
             it will default to stdout &#8211; s, &#8211;skip &#8211; data Skip retrieving data from SDI records.Retrieve only id and type.- i, &#8211;id = #Retrieve the SDI record matching the id passed by user.- t, &#8211;type = #Retrieve the SDI records matching the type passed by user.- c, &#8211;strict &#8211; check = name Specify the strict checksum algorithm by the user.Allowed values are innodb, crc32, none.- n, &#8211;no &#8211; check Ignore the checksum verification.- p, &#8211;pretty Pretty format the SDI output.If false, SDI would be not human readable but it will be of less size(Defaults to on; use&#8211; skip &#8211; pretty to disable.) Variables(&#8211;variable &#8211; name = value) and boolean options{FALSE | TRUE} Value(after reading options)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;debug(No default value) dump &#8211; file(No default value) skip &#8211; data FALSE id 0 type 0 strict &#8211; check crc32 no &#8211; check FALSE pretty TRUE
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-v</code> </p>
<p> Displays MySQL version information. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi --version</code>
ibd2sdi  Ver 8.0.3-dmr for Linux on x86_64 (Source distribution)
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Prints a debug log. For debug options, refer to Section 29.5.4, &#8220;The DBUG Package&#8221;. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi --debug=d:t /tmp/ibd2sdi.trace</code>
</pre>
</dl>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;dump-file=</code>, <code>-d</code> </p>
<p> Dumps serialized dictionary information (SDI) into the specified dump file. If a dump file is not specified, the tablespace SDI is dumped to stdout. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi --dump-file=</code><i>file_name</i><code> ../data/test/t1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-data</code>, <code>-s</code> </p>
<p> Skips retrieval of data field values from the serialized dictionary information (SDI) and only retrieves the id and type field values, which are primary keys for SDI records. </p>
<dl>
<dt>
<dd>
shell &gt; ibd2sdi&#8211; skip &#8211; data../ data / test / t1.ibd[&#8220;ibd2sdi&#8221;, {<br />
    &#8220;type&#8221; : 1,<br />
    &#8220;id&#8221; : 330<br />
},<br />
                                                      {<br />
                                                          &#8220;type&#8221; : 2,<br />
                                                          &#8220;id&#8221; : 7<br />
                                                      }]
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;id=</code><i>#</i>, <code>-i </code><i>#</i> </p>
<p> Retrieves serialized dictionary information (SDI) matching the specified table or tablespace object id. An object id is unique to the object type. Table and tablespace object IDs are also found in the id column of the mysql.tables and mysql.tablespace data dictionary tables. For information about data dictionary tables, see Section 14.1, &#8220;Data Dictionary Schema&#8221;. </p>
<dl>
<dt>
<dd>
shell &gt; ibd2sdi&#8211; id = 7../ data / test / t1.ibd[&#8220;ibd2sdi&#8221;, {<br />
    &#8220;type&#8221; : 2,<br />
    &#8220;id&#8221; : 7,<br />
    &#8220;object&#8221; :<br />
        {<br />
            &#8220;mysqld_version_id&#8221; : 80003,<br />
            &#8220;dd_version&#8221; : 80003,<br />
            &#8220;sdi_version&#8221; : 1,<br />
            &#8220;dd_object_type&#8221; : &#8220;Tablespace&#8221;,<br />
            &#8220;dd_object&#8221; : {<br />
                &#8220;name&#8221; : &#8220;test/t1&#8221;,<br />
                &#8220;comment&#8221; : &#8220;&#8221;,<br />
                &#8220;options&#8221; : &#8220;&#8221;,<br />
                &#8220;se_private_data&#8221; : &#8220;flags=16417;id=2;server_version=80003;space_version=1;&#8221;,<br />
                &#8220;engine&#8221; : &#8220;InnoDB&#8221;,<br />
                &#8220;files&#8221; : [<br />
                    {<br />
                        &#8220;ordinal_position&#8221; : 1,<br />
                        &#8220;filename&#8221; : &#8220;./test/t1.ibd&#8221;,<br />
                        &#8220;se_private_data&#8221; : &#8220;id=2;&#8221;<br />
                    }<br />
                ]<br />
            }<br />
        }<br />
}]
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;type=</code><i>#</i>, <code>-t </code><i>#</i> </p>
<p> Retrieves serialized dictionary information (SDI) matching the specified object type. SDI is provided for table (type=1) and tablespace (type=2) objects. </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; ibd2sdi-- type = 2../ data / test / t1.ibd["ibd2sdi", {
    "type" : 2,
    "id" : 7,
    "object" :
        {
            "mysqld_version_id" : 80003,
            "dd_version" : 80003,
            "sdi_version" : 1,
            "dd_object_type" : "Tablespace",
            "dd_object" : {
                "name" : "test/t1",
                "comment" : "",
                "options" : "",
                "se_private_data" : "flags=16417;id=2;server_version=80003;space_version=1;",
                "engine" : "InnoDB",
                "files" : [
                    {
                        "ordinal_position" : 1,
                        "filename" : "./test/t1.ibd",
                        "se_private_data" : "id=2;"
                    }
                ]
            }
        }
}]
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;strict-check</code>, <code>-c</code> </p>
<p> Specifies a strict checksum algorithm for validating the checksum of pages that are read. Options include innodb, crc32, and none. </p>
<p> In this example, the strict version of the innodb checksum algorithm is specified: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi --strict-check=innodb ../data/test/t1.ibd</code>
</pre>
</dl>
<p> In this example, the strict version of crc32 checksum algorithm is specified: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi -c crc32 ../data/test/t1.ibd</code>
</pre>
</dl>
<p> If you do not specify the <code>&#8211;strict-check</code> option, validation is performed against non-strict innodb, crc32 and none checksums.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-check</code>, <code>-n</code> </p>
<p> Skips checksum validation for pages that are read. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi --no-check ../data/test/t1.ibd</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pretty</code>, <code>-p</code> </p>
<p> Outputs SDI data in JSON pretty print format. Enabled by default. If disabled, SDI is not human readable but is smaller in size. Use &#8211;skip-pretty to disable. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ibd2sdi --skip-pretty ../data/test/t1.ibd</code>
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
