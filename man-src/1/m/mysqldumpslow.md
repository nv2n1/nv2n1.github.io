---
title: "mysqldumpslow(1)"
name: "mysqldumpslow"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldumpslow/"
description: "mysqldumpslow – Summarize slow query log files"
---

<h2 class="name">NAME</h2>
<p> mysqldumpslow &#8211; Summarize slow query log files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldumpslow [</code><code>options</code><code>] [</code><i>log_file</i><code> &#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<dd>The MySQL slow query log contains information about queries that take a long time to execute (see Section 5.4.5, &#8220;The Slow Query Log&#8221;). <code>mysqldumpslow</code> parses MySQL slow query log files and summarizes their contents. </p>
<p> Normally, <code>mysqldumpslow</code> groups queries that are similar except for the particular values of number and string data values. It &#8220;abstracts&#8221; these values to N and &#8216;S&#8217; when displaying summary output. To modify value abstracting behavior, use the <code>-a</code> and <code>-n</code> options. </p>
<p> Invoke <code>mysqldumpslow</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqldumpslow[options][log_file...]
</code></pre>
</dl>
<p> Example of usage: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqldumpslow
                    Reading mysql slow query log from /
                usr / local / mysql / data / mysqld80 -
            slow.log
                Count : 1 Time = 4.32s(4s)Lock = 0.00s(0s)Rows = 0.0(0),
                          root[root] @localhost
                              insert into t2 select *from t1
                                  Count : 3 Time = 2.53s(7s)Lock = 0.00s(0s)Rows = 0.0(0),
                          root[root] @localhost
                              insert into t2 select *from t1 limit N
                                  Count : 3 Time = 2.13s(6s)Lock = 0.00s(0s)Rows = 0.0(0),
                          root[root] @localhost
                              insert into t1 select *from t1
</code></pre>
</dl>
<p> <code>mysqldumpslow</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>-a</code> </p>
<p> Do not abstract all numbers to N and strings to &#8216;S&#8217;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug</code>, <code>-d</code> </p>
<p> Run in debug mode. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>-g </code><i>pattern</i> </p>
<p> Consider only queries that match the (<code>grep</code>-style) pattern.</dl>
<dl>
<dt>
<dd> &bull; <code>-h </code><i>host_name</i> </p>
<p> Host name of MySQL server for *-slow.log file name. The value can contain a wildcard. The default is * (match all).</dl>
<dl>
<dt>
<dd> &bull; <code>-i </code><i>name</i> </p>
<p> Name of server instance (if using <code>mysql.server</code> startup script).</dl>
<dl>
<dt>
<dd> &bull; <code>-l</code> </p>
<p> Do not subtract lock time from total time.</dl>
<dl>
<dt>
<dd> &bull; <code>-n </code><i>N</i> </p>
<p> Abstract numbers with at least <i>N</i> digits within names.</dl>
<dl>
<dt>
<dd> &bull; <code>-r</code> </p>
<p> Reverse the sort order.</dl>
<dl>
<dt>
<dd> &bull; <code>-s </code><i>sort_type</i> </p>
<p> How to sort the output. The value of <i>sort_type</i> should be chosen from the following list: </p>
<dl>
<dt>
<dd> &bull; t, at: Sort by query time or average query time</dl>
<dl>
<dt>
<dd> &bull; l, al: Sort by lock time or average lock time</dl>
<dl>
<dt>
<dd> &bull; r, ar: Sort by rows sent or average rows sent</dl>
<dl>
<dt>
<dd> &bull; c: Sort by count</dl>
<p> By default, <code>mysqldumpslow</code> sorts by average query time (equivalent to <code>-s at</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>-t </code><i>N</i> </p>
<p> Display only the first <i>N</i> queries in the output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
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
