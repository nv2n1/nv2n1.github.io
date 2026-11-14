---
title: "mysql_config(1)"
name: "mysql_config"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_config/"
description: "mysql_config – get compile options for compiling clients"
---

<h2 class="name">NAME</h2>
<p> mysql_config &#8211; get compile options for compiling clients </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_config </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql_config</code></p>
<dd>provides you with useful information for compiling your MariaDB client and connecting it to MariaDB. </p>
<p> <code>mysql_config</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;cflags</code> </p>
<p> Compiler flags to find include files and critical compiler flags and defines used when compiling the libmysqlclient library. The options returned are tied to the specific compiler that was used when the library was created and might clash with the settings for your own compiler. Use <code>&#8211;include</code> for more portable options that contain only include paths.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include</code> </p>
<p> Compiler options to find MariaDB include files.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;libmysqld-libs</code>, <code>&#8211;embedded</code> </p>
<p> Libraries and options required to link with the MariaDB embedded server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;libs</code> </p>
<p> Libraries and options required to link with the MariaDB client library.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;libs_r</code> </p>
<p> Libraries and options required to link with the thread-safe MariaDB client library.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugindir</code> </p>
<p> The default plugin directory path name, defined when configuring MariaDB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port</code> </p>
<p> The default TCP/IP port number, defined when configuring MariaDB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket</code> </p>
<p> The default Unix socket file, defined when configuring MariaDB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;variable=VAR</code> </p>
<p> Path to MariaDB include, library and plugin directories. <code>VAR</code> is one of `pkgincludedir`, `pkglibdir` and `plugindir`, respectively.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code> </p>
<p> Version number for the MariaDB distribution.</dl>
<p> If you invoke <code>mysql_config</code> with no options, it displays a list of all options that it supports, and their values: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysql_config
                    Usage : /
                            usr / local / mysql / bin / mysql_config[options] Options : --cflags[-I / usr / local / mysql / include / mysql - mcpu = pentiumpro]-- include[-I / usr / local / mysql / include / mysql]-- libs[-L / usr / local / mysql / lib / mysql - lmysqlclient - lz - lcrypt - lnsl - lm - L / usr / lib - lssl - lcrypto]-- libs_r[-L / usr / local / mysql / lib / mysql - lmysqlclient_r - lpthread - lz - lcrypt - lnsl - lm - lpthread]-- socket[/ tmp / mysql.sock]-- port[3306]-- version[4.0.16]-- libmysqld -
            libs[-L / usr / local / mysql / lib / mysql - lmysqld - lpthread - lz - lcrypt - lnsl - lm - lpthread - lrt]
</code></pre>
</dl>
<p> You can use <code>mysql_config</code> within a command line to include the value that it displays for a particular option. For example, to compile a MariaDB client program, use <code>mysql_config</code> as follows: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>CFG=/usr/local/mysql/bin/mysql_config</code>
shell&gt; <code>sh -c &quot;gcc -o progname `$CFG --include` progname.c `$CFG --libs`&quot;</code>
</pre>
</dl>
<p> When you use <code>mysql_config</code> this way, be sure to invoke it within backtick (&#8220;`&#8221;) characters. That tells the shell to execute it and substitute its output into the surrounding command.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2008 MySQL AB, 2008-2010 Sun Microsystems, Inc., 2010-2015 MariaDB Foundation </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a></p>
<h2>AUTHOR</h2>
<p> MariaDB Foundation (<a rel="nofollow" href="http://www.mariadb.org/">http://www.mariadb.org/</a>). </p>
<h2>Index</h2>
