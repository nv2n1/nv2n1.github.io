---
title: "mysql_plugin(1)"
name: "mysql_plugin"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_plugin/"
description: "mysql_plugin – configure MySQL server plugins"
---

<h2 class="name">NAME</h2>
<p> mysql_plugin &#8211; configure MySQL server plugins </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_plugin [</code><i>options</i><code>] </code><i>plugin</i><code> {ENABLE|DISABLE}</code></dl>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd>
<dd> <font SIZE="+1"> <code>Note</code> </font></p>
<dd>
<p> <code>mysql_plugin</code></p>
<dd>is deprecated as of MySQL 5.7.11 and removed in MySQL 8.0. Alternatives include loading plugins at server startup using the <code>&#8211;plugin-load</code> or <code>&#8211;plugin-load-add</code> option, or at runtime using the INSTALL PLUGIN statement. </p>
</dl>
<p> The <code>mysql_plugin</code> utility enables MySQL administrators to manage which plugins a MySQL server loads. It provides an alternative to manually specifying the <code>&#8211;plugin-load</code> option at server startup or using the INSTALL PLUGIN and UNINSTALL PLUGIN statements at runtime. </p>
<p> Depending on whether <code>mysql_plugin</code> is invoked to enable or disable plugins, it inserts or deletes rows in the mysql.plugin table that serves as a plugin registry. (To perform this operation, <code>mysql_plugin</code> invokes the MySQL server in bootstrap mode. This means that the server must not already be running.) For normal server startups, the server loads and enables plugins listed in mysql.plugin automatically. For additional control over plugin activation, use <code>&#8212;</code><i>plugin_name</i> options named for specific plugins, as described in Section 5.5.1, &#8220;Installing and Uninstalling Plugins&#8221;. </p>
<p> Each invocation of <code>mysql_plugin</code> reads a configuration file to determine how to configure the plugins contained in a single plugin library file. To invoke <code>mysql_plugin</code>, use this syntax: </p>
<dl>
<dt>
<dd>
<pre><code>
mysql_plugin[options] plugin
{
    ENABLE | DISABLE
}
</code></pre>
</dl>
<p> <i>plugin</i> is the name of the plugin to configure. ENABLE or DISABLE (not case-sensitive) specify whether to enable or disable components of the plugin library named in the configuration file. The order of the <i>plugin</i> and ENABLE or DISABLE arguments does not matter. </p>
<p> For example, to configure components of a plugin library file named myplugins.so on Linux or myplugins.dll on Windows, specify a <i>plugin</i> value of myplugins. Suppose that this plugin library contains three plugins, plugin1, plugin2, and plugin3, all of which should be configured under <code>mysql_plugin</code> control. By convention, configuration files have a suffix of .ini and the same base name as the plugin library, so the default configuration file name for this plugin library is myplugins.ini. The configuration file contents look like this: </p>
<dl>
<dt>
<dd>
<pre>
myplugins
plugin1
plugin2
plugin3
</pre>
</dl>
<p> The first line in the myplugins.ini file is the name of the library file, without any extension such as .so or .dll. The remaining lines are the names of the components to be enabled or disabled. Each value in the file should be on a separate line. Lines on which the first character is &#8216;#&#8217; are taken as comments and ignored. </p>
<p> To enable the plugins listed in the configuration file, invoke <code>mysql_plugin</code> this way: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_plugin myplugins ENABLE</code>
</pre>
</dl>
<p> To disable the plugins, use DISABLE rather than ENABLE. </p>
<p> An error occurs if <code>mysql_plugin</code> cannot find the configuration file or plugin library file, or if <code>mysql_plugin</code> cannot start the MySQL server. </p>
<p> <code>mysql_plugin</code> supports the following options, which can be specified on the command line or in the [mysqld] group of any option file. For options specified in a [mysqld] group, <code>mysql_plugin</code> recognizes the <code>&#8211;basedir</code>, <code>&#8211;datadir</code>, and <code>&#8211;plugin-dir</code> options and ignores others. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;basedir=</code><i>dir_name</i>, <code>-b </code><i>dir_name</i> </p>
<p> The server base directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;datadir=</code><i>dir_name</i>, <code>-d </code><i>dir_name</i> </p>
<p> The server data directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;my-print-defaults=</code><i>file_name</i>, <code>-b </code><i>file_name</i> </p>
<p> The path to the <code>my_print_defaults</code> program.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqld=</code><i>file_name</i>, <code>-b </code><i>file_name</i> </p>
<p> The path to the <code>mysqld</code> server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code>, <code>-p</code> </p>
<p> Do not read values from the configuration file. This option enables an administrator to skip reading defaults from the configuration file. </p>
<p> With <code>mysql_plugin</code>, this option need not be given first on the command line, unlike most other MySQL programs that support <code>&#8211;no-defaults</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i>, <code>-p </code><i>dir_name</i> </p>
<p> The server plugin directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-ini=</code><i>file_name</i>, <code>-i </code><i>file_name</i> </p>
<p> The <code>mysql_plugin</code> configuration file. Relative path names are interpreted relative to the current directory. If this option is not given, the default is <i>plugin</i>.ini in the plugin directory, where <i>plugin</i> is the <i>plugin</i> argument on the command line.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-defaults</code>, <code>-P</code> </p>
<p> Display the default values from the configuration file. This option causes <code>mysql_plugin</code> to print the defaults for <code>&#8211;basedir</code>, <code>&#8211;datadir</code>, and <code>&#8211;plugin-dir</code> if they are found in the configuration file. If no value for a variable is found, nothing is shown. </p>
<p> With <code>mysql_plugin</code>, this option need not be given first on the command line, unlike most other MySQL programs that support <code>&#8211;print-defaults</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does. This option can be used multiple times to increase the amount of information.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2019, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
