---
title: "mysqld_multi(1)"
name: "mysqld_multi"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqld_multi/"
description: "mysqld_multi – manage multiple MySQL servers"
---

<h2 class="name">NAME</h2>
<p> mysqld_multi &#8211; manage multiple MySQL servers </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqld_multi [</code><i>options</i><code>] {start|stop|report} [</code><i>GNR</i><code>[,</code><i>GNR</i><code>] &#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysqld_multi</code></p>
<dd>is designed to manage several <code>mysqld</code> processes that listen for connections on different Unix socket files and TCP/IP ports. It can start or stop servers, or report their current status. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> For some Linux platforms, MySQL installation from RPM or Debian packages includes systemd support for managing MySQL server startup and shutdown. On these platforms, <code>mysqld_multi</code> is not installed because it is unnecessary. For information about using systemd to handle multiple MySQL instances, see Section 2.5.9, &#8220;Managing MySQL Server with systemd&#8221;. </p>
</dl>
<p> <code>mysqld_multi</code> searches for groups named [mysqld<i>N</i>] in my.cnf (or in the file named by the <code>&#8211;defaults-file</code> option). <i>N</i> can be any positive integer. This number is referred to in the following discussion as the option group number, or <i>GNR</i>. Group numbers distinguish option groups from one another and are used as arguments to <code>mysqld_multi</code> to specify which servers you want to start, stop, or obtain a status report for. Options listed in these groups are the same that you would use in the [mysqld] group used for starting <code>mysqld</code>. (See, for example, Section 2.10.5, &#8220;Starting and Stopping MySQL Automatically&#8221;.) However, when using multiple servers, it is necessary that each one use its own value for options such as the Unix socket file and TCP/IP port number. For more information on which options must be unique per server in a multiple-server environment, see Section 5.8, &#8220;Running Multiple MySQL Instances on One Machine&#8221;. </p>
<p> To invoke <code>mysqld_multi</code>, use the following syntax: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqld_multi[options]{start | stop | reload | report}[GNR[, GNR]...]
</code></pre>
</dl>
<p> start, stop, reload (stop and restart), and report indicate which operation to perform. You can perform the designated operation for a single server or multiple servers, depending on the <i>GNR</i> list that follows the option name. If there is no list, <code>mysqld_multi</code> performs the operation for all servers in the option file. </p>
<p> Each <i>GNR</i> value represents an option group number or range of group numbers. The value should be the number at the end of the group name in the option file. For example, the <i>GNR</i> for a group named [mysqld17] is 17. To specify a range of numbers, separate the first and last numbers by a dash. The <i>GNR</i> value 10-13 represents groups [mysqld10] through [mysqld13]. Multiple groups or group ranges can be specified on the command line, separated by commas. There must be no whitespace characters (spaces or tabs) in the <i>GNR</i> list; anything after a whitespace character is ignored. </p>
<p> This command starts a single server using option group [mysqld17]: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqld_multi start 17</code>
</pre>
</dl>
<p> This command stops several servers, using option groups [mysqld8] and [mysqld10] through [mysqld13]: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqld_multi stop 8,10-13</code>
</pre>
</dl>
<p> For an example of how you might set up an option file, use this command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqld_multi --example</code>
</pre>
</dl>
<p> <code>mysqld_multi</code> searches for option files as follows: </p>
<dl>
<dt>
<dd> &bull; With <code>&#8211;no-defaults</code>, no option files are read.</dl>
<dl>
<dt>
<dd> &bull; With <code>&#8211;defaults-file=</code><i>file_name</i>, only the named file is read.</dl>
<dl>
<dt>
<dd> &bull; Otherwise, option files in the standard list of locations are read, including any file named by the <code>&#8211;defaults-extra-file=</code><i>file_name</i> option, if one is given. (If the option is given multiple times, the last value is used.)</dl>
<p> For additional information about these and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;. </p>
<p> Option files read are searched for [mysqld_multi] and [mysqld<i>N</i>] option groups. The [mysqld_multi] group can be used for options to <code>mysqld_multi</code> itself. [mysqld<i>N</i>] groups can be used for options passed to specific <code>mysqld</code> instances. </p>
<p> The [mysqld] or [mysqld_safe] groups can be used for common options read by all instances of <code>mysqld</code> or <code>mysqld_safe</code>. You can specify a <code>&#8211;defaults-file=</code><i>file_name</i> option to use a different configuration file for that instance, in which case the [mysqld] or [mysqld_safe] groups from that file will be used for that instance. </p>
<p> <code>mysqld_multi</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;example</code> </p>
<p> Display a sample option file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;log=</code><i>file_name</i> </p>
<p> Specify the name of the log file. If the file exists, log output is appended to it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqladmin=</code><i>prog_name</i> </p>
<p> The <code>mysqladmin</code> binary to be used to stop servers.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqld=</code><i>prog_name</i> </p>
<p> The <code>mysqld</code> binary to be used. Note that you can specify <code>mysqld_safe</code> as the value for this option also. If you use <code>mysqld_safe</code> to start the server, you can include the mysqld or ledir options in the corresponding [mysqld<i>N</i>] option group. These options indicate the name of the server that <code>mysqld_safe</code> should start and the path name of the directory where the server is located. (See the descriptions for these options in <code><a href="/docs/linux/man/1-mysqld_safe/">mysqld_safe</a></code>(1).) Example: </p>
<dl>
<dt>
<dd>
<pre>
[mysqld38]
mysqld = mysqld-debug
ledir  = /opt/local/mysql/libexec
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-log</code> </p>
<p> Print log information to stdout rather than to the log file. By default, output goes to the log file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password=</code><i>password</i> </p>
<p> The password of the MySQL account to use when invoking <code>mysqladmin</code>. Note that the password value is not optional for this option, unlike for other MySQL programs.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code> </p>
<p> Silent mode; disable warnings.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tcp-ip</code> </p>
<p> Connect to each MySQL server through the TCP/IP port instead of the Unix socket file. (If a socket file is missing, the server might still be running, but accessible only through the TCP/IP port.) By default, connections are made using the Unix socket file. This option affects stop and report operations.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i> </p>
<p> The user name of the MySQL account to use when invoking <code>mysqladmin</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code> </p>
<p> Be more verbose.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code> </p>
<p> Display version information and exit.</dl>
<p> Some notes about <code>mysqld_multi</code>: </p>
<dl>
<dt>
<dd> &bull; <code>Most important</code>: Before using <code>mysqld_multi</code> be sure that you understand the meanings of the options that are passed to the <code>mysqld</code> servers and <i>why</i> you would want to have separate <code>mysqld</code> processes. Beware of the dangers of using multiple <code>mysqld</code> servers with the same data directory. Use separate data directories, unless you <i>know</i> what you are doing. Starting multiple servers with the same data directory does <i>not</i> give you extra performance in a threaded system. See Section 5.8, &#8220;Running Multiple MySQL Instances on One Machine&#8221;. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font><br />
 Make sure that the data directory for each server is fully accessible to the Unix account that the specific <code>mysqld</code> process is started as. <i>Do not</i> use the Unix <i>root</i> account for this, unless you <i>know</i> what you are doing. See Section 6.1.5, &#8220;How to Run MySQL as a Normal User&#8221;. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Make sure that the MySQL account used for stopping the <code>mysqld</code> servers (with the <code>mysqladmin</code> program) has the same user name and password for each server. Also, make sure that the account has the SHUTDOWN privilege. If the servers that you want to manage have different user names or passwords for the administrative accounts, you might want to create an account on each server that has the same user name and password. For example, you might set up a common multi_admin account by executing the following commands for each server: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql -u root -S /tmp/mysql.sock -p</code>
Enter password:
mysql&gt; <code>CREATE USER 'multi_admin'@'localhost' IDENTIFIED BY 'multipass';</code>
mysql&gt; <code>GRANT SHUTDOWN ON *.* TO 'multi_admin'@'localhost';</code>
</pre>
</dl>
<p> See Section 6.2, &#8220;Access Control and Account Management&#8221;. You have to do this for each <code>mysqld</code> server. Change the connection parameters appropriately when connecting to each one. Note that the host name part of the account name must permit you to connect as multi_admin from the host where you want to run <code>mysqld_multi</code>.</dl>
<dl>
<dt>
<dd> &bull; The Unix socket file and the TCP/IP port number must be different for every <code>mysqld</code>. (Alternatively, if the host has multiple network addresses, you can set the bind_address system variable to cause different servers to listen to different interfaces.)</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;pid-file</code> option is very important if you are using <code>mysqld_safe</code> to start <code>mysqld</code> (for example, <code>&#8211;mysqld=mysqld_safe</code>) Every <code>mysqld</code> should have its own process ID file. The advantage of using <code>mysqld_safe</code> instead of <code>mysqld</code> is that <code>mysqld_safe</code> monitors its <code>mysqld</code> process and restarts it if the process terminates due to a signal sent using kill -9 or for other reasons, such as a segmentation fault.</dl>
<dl>
<dt>
<dd> &bull; You might want to use the <code>&#8211;user</code> option for <code>mysqld</code>, but to do this you need to run the <code>mysqld_multi</code> script as the Unix superuser (root). Having the option in the option file doesn&#8217;t matter; you just get a warning if you are not the superuser and the <code>mysqld</code> processes are started under your own Unix account.</dl>
<p> The following example shows how you might set up an option file for use with <code>mysqld_multi</code>. The order in which the <code>mysqld</code> programs are started or stopped depends on the order in which they appear in the option file. Group numbers need not form an unbroken sequence. The first and fifth [mysqld<i>N</i>] groups were intentionally omitted from the example to illustrate that you can have &#8220;gaps&#8221; in the option file. This gives you more flexibility. </p>
<dl>
<dt>
<dd>
<pre><code>
#This is an example of a my.cnf file for mysqld_multi.
#Usually this file is located in home dir ~ /.my.cnf or / etc / my.cnf
[mysqld_multi] mysqld = / usr / local / mysql / bin / mysqld_safe mysqladmin = / usr / local / mysql / bin / mysqladmin user = multi_admin
                                                                                   password = my_password
                                                                                       [mysqld2] socket = / tmp / mysql.sock2 port = 3307 pid - file = / usr / local / mysql / data2 / hostname.pid2 datadir = / usr / local / mysql / data2 language = / usr / local / mysql / share / mysql / english user = unix_user1
                                                                                                                                                                                                                                                            [mysqld3] mysqld = / path / to / mysqld_safe ledir = / path / to / mysqld - binary /
                                                                                                                                                                                                                                                                                                                                            mysqladmin = / path / to / mysqladmin socket = / tmp / mysql.sock3 port = 3308 pid - file = / usr / local / mysql / data3 / hostname.pid3 datadir = / usr / local / mysql / data3 language = / usr / local / mysql / share / mysql / swedish user = unix_user2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             [mysqld4] socket = / tmp / mysql.sock4 port = 3309 pid - file = / usr / local / mysql / data4 / hostname.pid4 datadir = / usr / local / mysql / data4 language = / usr / local / mysql / share / mysql / estonia user = unix_user3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  [mysqld6] socket = / tmp / mysql.sock6 port = 3311 pid - file = / usr / local / mysql / data6 / hostname.pid6 datadir = / usr / local / mysql / data6 language = / usr / local / mysql / share / mysql / japanese user = unix_user4
</code></pre>
</dl>
<p> See Section 4.2.2.2, &#8220;Using Option Files&#8221;.</p>
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
