---
title: "mysql-server(1)"
name: "mysql-server"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql-server/"
description: "mysql.server – MariaDB server startup script"
---

<p>mysql.server &#8211; MariaDB server startup script </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>mysql {start|stop}</code></dl>
<h2>Description</h2>
<dd>MariaDB distributions on Unix include a script named <code>mysql.server</code>. It can be used on systems such as Linux and Solaris that use System V-style run directories to start and stop system services. It is also used by the Mac OS X Startup Item for MariaDB. </p>
<p> <code>mysql.server</code> can be found in the support-files directory under your MariaDB installation directory or in a MariaDB source distribution. </p>
<p> If you use the Linux server RPM package (MySQL-server-<i>VERSION</i>.rpm), the <code>mysql.server</code> script will be installed in the /etc/init.d directory with the name mysql. You need not install it manually. </p>
<p> Some vendors provide RPM packages that install a startup script under a different name such as <code>mysqld</code>. </p>
<p> If you install MariaDB from a source distribution or using a binary distribution format that does not install <code>mysql.server</code> automatically, you can install it manually. </p>
<p> <code>mysql.server</code> reads options from the [mysql.server] and [mysqld] sections of option files. For backward compatibility, it also reads [mysql_server] sections, although you should rename such sections to [mysql.server]&amp;. </p>
<p> <code>mysql.server</code> supports the following options. </p>
<dl COMPACT>
<dd>&bull; <code>&#8211;basedir=</code><i>path</i> </p>
<p> The path to the MariaDB installation directory.</dl>
<dl COMPACT>
<dd>&bull; <code>&#8211;datadir=</code><i>path</i> </p>
<p> The path to the MariaDB data directory.</dl>
<dl COMPACT>
<dd>&bull; <code>&#8211;pid-file=</code><i>file_name</i> </p>
<p> The path name of the file in which the server should write its process ID. If not provided, the default, &quot;host_name.pid&quot; is used.</dl>
<dl COMPACT>
<dd>&bull; <code>&#8211;service-startup-timeout=</code><i>file_name</i> </p>
<p> How long in seconds to wait for confirmation of server startup. If the server does not start within this time, <code>mysql.server</code> exits with an error. The default value is 900. A value of 0 means not to wait at all for startup. Negative values mean to wait forever (no timeout).</dl>
<dl COMPACT>
<dd>&bull; <code>&#8211;use-mysqld_safe</code> </p>
<p> Use <code>mysqld_safe</code> to start the server. This is the default.</dl>
<dl COMPACT>
<dd>&bull; <code>&#8211;use-manager</code> </p>
<p> Use Instance Manager to start the server.</dl>
<dl COMPACT>
<dd>&bull; <code>&#8211;user=</code><i>user_name</i> </p>
<p> The login user name to use for running <code>mysqld</code>.</dl>
<h2>Copyright</h2>
<p>Copyright 2007-2008 MySQL AB, 2008-2010 Sun Microsystems, Inc., 2010-2015 MariaDB Foundation </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>See Also</h2>
<p>For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a></p>
<h2>Author</h2>
<p>MariaDB Foundation (<a rel="nofollow" href="http://www.mariadb.org/">http://www.mariadb.org/</a>).</p>
