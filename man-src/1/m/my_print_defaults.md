---
title: "my_print_defaults(1)"
name: "my_print_defaults"
section: "1"
letter: "m"
url: "/docs/linux/man/1-my_print_defaults/"
description: "my_print_defaults – display options from option files"
---

<h2 class="name">NAME</h2>
<p> my_print_defaults &#8211; display options from option files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>my_print_defaults [</code><i>options</i><code>] </code><i>option_group</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>my_print_defaults</code></p>
<dd>displays the options that are present in option groups of option files. The output indicates what options will be used by programs that read the specified option groups. For example, the <code>mysqlcheck</code> program reads the [mysqlcheck] and [client] option groups. To see what options are present in those groups in the standard option files, invoke <code>my_print_defaults</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>my_print_defaults mysqlcheck client</code>
--user=myusername
--password=<i>password</i>
--host=localhost
</pre>
</dl>
<p> The output consists of options, one per line, in the form that they would be specified on the command line. </p>
<p> <code>my_print_defaults</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;config-file=</code><i>file_name</i>, <code>&#8211;defaults-file=</code><i>file_name</i>, <code>-c </code><i>file_name</i> </p>
<p> Read only the given option file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug=</code><i>debug_options</i>, <code>-# </code><i>debug_options</i> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/my_print_defaults.trace.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-extra-file=</code><i>file_name</i>, <code>&#8211;extra-file=</code><i>file_name</i>, <code>-e </code><i>file_name</i> </p>
<p> Read this option file after the global option file but (on Unix) before the user option file. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-group-suffix=</code><i>suffix</i>, <code>-g </code><i>suffix</i> </p>
<p> In addition to the groups named on the command line, read groups that have the given suffix. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i>, <code>-l </code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code>, <code>-n</code> </p>
<p> Return an empty string. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;show</code>, <code>-s</code> </p>
<p> <code>my_print_defaults</code> masks passwords by default. Use this option to display passwords as cleartext.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
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
