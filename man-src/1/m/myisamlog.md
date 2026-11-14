---
title: "myisamlog(1)"
name: "myisamlog"
section: "1"
letter: "m"
url: "/docs/linux/man/1-myisamlog/"
description: "myisamlog – display MyISAM log file contents"
---

<h2 class="name">NAME</h2>
<p> myisamlog &#8211; display MyISAM log file contents </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>myisamlog [</code><i>options</i><code>] [</code><i>log_file</i><code> [</code><i>tbl_name</i><code>] &#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>myisamlog</code></p>
<dd>processes the contents of a MyISAM log file. To create such a file, start the server with a <code>&#8211;log-isam=</code><code>log_file</code> option. </p>
<p> Invoke <code>myisamlog</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; myisamlog[options][file_name[tbl_name]...]
</code></pre>
</dl>
<p> The default operation is update (<code>-u</code>). If a recovery is done (<code>-r</code>), all writes and possibly updates and deletes are done and errors are only counted. The default log file name is myisam.log if no <i>log_file</i> argument is given. If tables are named on the command line, only those tables are updated. </p>
<p> <code>myisamlog</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>-?</code>, <code>-I</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>-c </code><i>N</i> </p>
<p> Execute only <i>N</i> commands.</dl>
<dl>
<dt>
<dd> &bull; <code>-f </code><i>N</i> </p>
<p> Specify the maximum number of open files.</dl>
<dl>
<dt>
<dd> &bull; <code>-F </code><i>filepath/</i> </p>
<p> Specify the file path with a trailing slash.</dl>
<dl>
<dt>
<dd> &bull; <code>-i</code> </p>
<p> Display extra information before exiting.</dl>
<dl>
<dt>
<dd> &bull; <code>-o </code><i>offset</i> </p>
<p> Specify the starting offset.</dl>
<dl>
<dt>
<dd> &bull; <code>-p </code><i>N</i> </p>
<p> Remove <i>N</i> components from path.</dl>
<dl>
<dt>
<dd> &bull; <code>-r</code> </p>
<p> Perform a recovery operation.</dl>
<dl>
<dt>
<dd> &bull; <code>-R </code><i>record_pos_file record_pos</i> </p>
<p> Specify record position file and record position.</dl>
<dl>
<dt>
<dd> &bull; <code>-u</code> </p>
<p> Perform an update operation.</dl>
<dl>
<dt>
<dd> &bull; <code>-v</code> </p>
<p> Verbose mode. Print more output about what the program does. This option can be given multiple times to produce more and more output.</dl>
<dl>
<dt>
<dd> &bull; <code>-w </code><i>write_file</i> </p>
<p> Specify the write file.</dl>
<dl>
<dt>
<dd> &bull; <code>-V</code> </p>
<p> Display version information.</dl>
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
