---
title: "mysql_config_editor(1)"
name: "mysql_config_editor"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_config_editor/"
description: "mysql_config_editor – configure authentication information for connecting to MySQL server"
---

<h2 class="name">NAME</h2>
<p> mysql_config_editor &#8211; configure authentication information for connecting to MySQL server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_config_editor </code><i>options command</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mysql_config_editor</code> utility enables you to store authentication credentials in an obfuscated login path file named .mylogin.cnf. The file location is the %APPDATA%\MySQL directory on Windows and the current user&#8217;s home directory on non-Windows systems. The file can be read later by MySQL client programs to obtain authentication credentials for connecting to MySQL Server. </p>
<p> The unobfuscated format of the .mylogin.cnf login path file consists of option groups, similar to other option files. Each option group in .mylogin.cnf is called a &#8220;login path,&#8221; which is a group that permits only certain options: <code>host</code>, <code>user</code>, <code>password</code>, <code>port</code> and <code>socket</code>. Think of a login path option group as a set of options that specify which MySQL server to connect to and which account to authenticate as. Here is an unobfuscated example: </p>
<dl>
<dt>
<dd>
<pre><code>
[client] user = mydefaultname
    password = mydefaultpass
        host = 127.0.0.1
            [mypath] user = myothername
                password = myotherpass
                    host = localhost
</code></pre>
</dl>
<p> When you invoke a client program to connect to the server, the client uses .mylogin.cnf in conjunction with other option files. Its precedence is higher than other option files, but less than options specified explicitly on the client command line. For information about the order in which option files are used, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<p> To specify an alternate login path file name, set the MYSQL_TEST_LOGIN_FILE environment variable. This variable is recognized by <code>mysql_config_editor</code>, by standard MySQL clients (<code>mysql</code>, <code>mysqladmin</code>, and so forth), and by the <code>mysql-test-run.pl</code> testing utility. </p>
<p> Programs use groups in the login path file as follows: </p>
<dl>
<dt>
<dd> &bull; <code>mysql_config_editor</code> operates on the client login path by default if you specify no <code>&#8211;login-path=</code><i>name</i> option to indicate explicitly which login path to use.</dl>
<dl>
<dt>
<dd> &bull; Without a <code>&#8211;login-path</code> option, client programs read the same option groups from the login path file that they read from other option files. Consider this command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql</code>
</pre>
</dl>
<p> By default, the <code>mysql</code> client reads the [client] and [mysql] groups from other option files, so it reads them from the login path file as well.</dl>
<dl>
<dt>
<dd> &bull; With a <code>&#8211;login-path</code> option, client programs additionally read the named login path from the login path file. The option groups read from other option files remain the same. Consider this command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql --login-path=mypath</code>
</pre>
</dl>
<p> The <code>mysql</code> client reads [client] and [mysql] from other option files, and [client], [mysql], and [mypath] from the login path file.</dl>
<dl>
<dt>
<dd> &bull; Client programs read the login path file even when the <code>&#8211;no-defaults</code> option is used. This permits passwords to be specified in a safer way than on the command line even if <code>&#8211;no-defaults</code> is present.</dl>
<p> <code>mysql_config_editor</code> obfuscates the .mylogin.cnf file so it cannot be read as cleartext, and its contents when unobfuscated by client programs are used only in memory. In this way, passwords can be stored in a file in non-cleartext format and used later without ever needing to be exposed on the command line or in an environment variable. <code>mysql_config_editor</code> provides a print command for displaying the login path file contents, but even in this case, password values are masked so as never to appear in a way that other users can see them. </p>
<p> The obfuscation used by <code>mysql_config_editor</code> prevents passwords from appearing in .mylogin.cnf as cleartext and provides a measure of security by preventing inadvertent password exposure. For example, if you display a regular unobfuscated my.cnf option file on the screen, any passwords it contains are visible for anyone to see. With .mylogin.cnf, that is not true. But the obfuscation used will not deter a determined attacker and you should not consider it unbreakable. A user who can gain system administration privileges on your machine to access your files could unobfuscate the .mylogin.cnf file with some effort. </p>
<p> The login path file must be readable and writable to the current user, and inaccessible to other users. Otherwise, <code>mysql_config_editor</code> ignores it, and client programs do not use it, either. </p>
<p> Invoke <code>mysql_config_editor</code> like this: </p>
<dl>
<dt>
<dd>
shell &gt; mysql_config_editor[program_options] command[command_options]
</dl>
<p> If the login path file does not exist, <code>mysql_config_editor</code> creates it. </p>
<p> Command arguments are given as follows: </p>
<dl>
<dt>
<dd> &bull; <i>program_options</i> consists of general <code>mysql_config_editor</code> options.</dl>
<dl>
<dt>
<dd> &bull; command indicates what action to perform on the .mylogin.cnf login path file. For example, set writes a login path to the file, remove removes a login path, and print displays login path contents.</dl>
<dl>
<dt>
<dd> &bull; <i>command_options</i> indicates any additional options specific to the command, such as the login path name and the values to use in the login path.</dl>
<p> The position of the command name within the set of program arguments is significant. For example, these command lines have the same arguments, but produce different results: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_config_editor --help set</code>
shell&gt; <code>mysql_config_editor set --help</code>
</pre>
</dl>
<p> The first command line displays a general <code>mysql_config_editor</code> help message, and ignores the set command. The second command line displays a help message specific to the set command. </p>
<p> Suppose that you want to establish a client login path that defines your default connection parameters, and an additional login path named remote for connecting to the MySQL server the host remote.example.com. You want to log in as follows: </p>
<dl>
<dt>
<dd> &bull; By default, to the local server with a user name and password of localuser and localpass</dl>
<dl>
<dt>
<dd> &bull; To the remote server with a user name and password of remoteuser and remotepass</dl>
<p> To set up the login paths in the .mylogin.cnf file, use the following set commands. Enter each command on a single line, and enter the appropriate passwords when prompted: </p>
<dl>
<dt>
<dd>
shell &gt; mysql_config_editor set&#8211; login &#8211; path = client&#8211; host = localhost&#8211; user = localuser&#8211; password<br />
                                                                                        Enter password : enter password &#8220;localpass&#8221; here<br />
                                                                                                             shell &gt; mysql_config_editor set&#8211; login &#8211; path = remote&#8211; host = remote.example.com&#8211; user = remoteuser&#8211; password<br />
                                                                                        Enter password : enter password &#8220;remotepass&#8221; here
</dl>
<p> <code>mysql_config_editor</code> uses the client login path by default, so the <code>&#8211;login-path=client</code> option can be omitted from the first command without changing its effect. </p>
<p> To see what <code>mysql_config_editor</code> writes to the .mylogin.cnf file, use the print command: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysql_config_editor print-- all
            [client] user = localuser
    password = *****host = localhost
        [remote] user = remoteuser
            password = *****host = remote.example.com
</code></pre>
</dl>
<p> The print command displays each login path as a set of lines beginning with a group header indicating the login path name in square brackets, followed by the option values for the login path. Password values are masked and do not appear as cleartext. </p>
<p> If you do not specify <code>&#8211;all</code> to display all login paths or <code>&#8211;login-path=</code><i>name</i> to display a named login path, the print command displays the client login path by default, if there is one. </p>
<p> As shown by the preceding example, the login path file can contain multiple login paths. In this way, <code>mysql_config_editor</code> makes it easy to set up multiple &#8220;personalities&#8221; for connecting to different MySQL servers, or for connecting to a given server using different accounts. Any of these can be selected by name later using the <code>&#8211;login-path</code> option when you invoke a client program. For example, to connect to the remote server, use this command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql --login-path=remote</code>
</pre>
</dl>
<p> Here, <code>mysql</code> reads the [client] and [mysql] option groups from other option files, and the [client], [mysql], and [remote] groups from the login path file. </p>
<p> To connect to the local server, use this command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql --login-path=client</code>
</pre>
</dl>
<p> Because <code>mysql</code> reads the client and mysql login paths by default, the <code>&#8211;login-path</code> option does not add anything in this case. That command is equivalent to this one: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql</code>
</pre>
</dl>
<p> Options read from the login path file take precedence over options read from other option files. Options read from login path groups appearing later in the login path file take precedence over options read from groups appearing earlier in the file. </p>
<p> <code>mysql_config_editor</code> adds login paths to the login path file in the order you create them, so you should create more general login paths first and more specific paths later. If you need to move a login path within the file, you can remove it, then recreate it to add it to the end. For example, a client login path is more general because it is read by all client programs, whereas a mysqldump login path is read only by <code>mysqldump</code>. Options specified later override options specified earlier, so putting the login paths in the order client, mysqldump enables <code>mysqldump</code>-specific options to override client options. </p>
<p> When you use the set command with <code>mysql_config_editor</code> to create a login path, you need not specify all possible option values (host name, user name, password, port, socket). Only those values given are written to the path. Any missing values required later can be specified when you invoke a client path to connect to the MySQL server, either in other option files or on the command line. Any options specified on the command line override those specified in the login path file or other option files. For example, if the credentials in the remote login path also apply for the host remote2.example.com, connect to the server on that host like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql --login-path=remote --host=remote2.example.com</code>
</pre>
</dl>
<p> mysql_config_editor General Options </p>
<p> <code>mysql_config_editor</code> supports the following general options, which may be used preceding any command named on the command line. For descriptions of command-specific options, see mysql_config_editor Commands and Command-Specific Options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a general help message and exit. </p>
<p> To see a command-specific help message, invoke <code>mysql_config_editor</code> as follows, where <i>command</i> is a command other than help: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_config_editor </code><i>command</i><code> --help</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# </code><i>debug_options</i> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/mysql_config_editor.trace. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does. This option may be helpful in diagnosing problems if an operation does not have the effect you expect.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<p> mysql_config_editor Commands and Command-Specific Options </p>
<p> This section describes the permitted <code>mysql_config_editor</code> commands, and, for each one, the command-specific options permitted following the command name on the command line. </p>
<p> In addition, <code>mysql_config_editor</code> supports general options that can be used preceding any command. For descriptions of these options, see mysql_config_editor General Options. </p>
<p> <code>mysql_config_editor</code> supports these commands: </p>
<dl>
<dt>
<dd> &bull; help </p>
<p> Display a general help message and exit. This command takes no following options. </p>
<p> To see a command-specific help message, invoke <code>mysql_config_editor</code> as follows, where <i>command</i> is a command other than help: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_config_editor </code><i>command</i><code> --help</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; print [<i>options</i>] </p>
<p> Print the contents of the login path file in unobfuscated form, with the exception that passwords are displayed as *****. </p>
<p> The default login path name is client if no login path is named. If both <code>&#8211;all</code> and <code>&#8211;login-path</code> are given, <code>&#8211;all</code> takes precedence. </p>
<p> The print command permits these options following the command name: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message for the print command and exit. </p>
<p> To see a general help message, use <code>mysql_config_editor &#8211;help</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;all</code> </p>
<p> Print the contents of all login paths in the login path file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i>, <code>-G </code><i>name</i> </p>
<p> Print the contents of the named login path.</dl>
</dl>
<dl>
<dt>
<dd> &bull; remove [<i>options</i>] </p>
<p> Remove a login path from the login path file, or modify a login path by removing options from it. </p>
<p> This command removes from the login path only such options as are specified with the <code>&#8211;host</code>, <code>&#8211;password</code>, <code>&#8211;port</code>, <code>&#8211;socket</code>, and <code>&#8211;user</code> options. If none of those options are given, remove removes the entire login path. For example, this command removes only the <code>user</code> option from the mypath login path rather than the entire mypath login path: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_config_editor remove --login-path=mypath --user</code>
</pre>
</dl>
<p> This command removes the entire mypath login path: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_config_editor remove --login-path=mypath</code>
</pre>
</dl>
<p> The remove command permits these options following the command name: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message for the remove command and exit. </p>
<p> To see a general help message, use <code>mysql_config_editor &#8211;help</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host</code>, <code>-h</code> </p>
<p> Remove the host name from the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i>, <code>-G </code><i>name</i> </p>
<p> The login path to remove or modify. The default login path name is client if this option is not given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password</code>, <code>-p</code> </p>
<p> Remove the password from the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port</code>, <code>-P</code> </p>
<p> Remove the TCP/IP port number from the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket</code>, <code>-S</code> </p>
<p> Remove the Unix socket file name from the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user</code>, <code>-u</code> </p>
<p> Remove the user name from the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;warn</code>, <code>-w</code> </p>
<p> Warn and prompt the user for confirmation if the command attempts to remove the default login path (client) and <code>&#8211;login-path=client</code> was not specified. This option is enabled by default; use <code>&#8211;skip-warn</code> to disable it.</dl>
</dl>
<dl>
<dt>
<dd> &bull; reset [<i>options</i>] </p>
<p> Empty the contents of the login path file. </p>
<p> The reset command permits these options following the command name: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message for the reset command and exit. </p>
<p> To see a general help message, use <code>mysql_config_editor &#8211;help</code>.</dl>
</dl>
<dl>
<dt>
<dd> &bull; set [<i>options</i>] </p>
<p> Write a login path to the login path file. </p>
<p> This command writes to the login path only such options as are specified with the <code>&#8211;host</code>, <code>&#8211;password</code>, <code>&#8211;port</code>, <code>&#8211;socket</code>, and <code>&#8211;user</code> options. If none of those options are given, <code>mysql_config_editor</code> writes the login path as an empty group. </p>
<p> The set command permits these options following the command name: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message for the set command and exit. </p>
<p> To see a general help message, use <code>mysql_config_editor &#8211;help</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> The host name to write to the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i>, <code>-G </code><i>name</i> </p>
<p> The login path to create. The default login path name is client if this option is not given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password</code>, <code>-p</code> </p>
<p> Prompt for a password to write to the login path. After <code>mysql_config_editor</code> displays the prompt, type the password and press Enter. To prevent other users from seeing the password, <code>mysql_config_editor</code> does not echo it. </p>
<p> To specify an empty password, press Enter at the password prompt. The resulting login path written to the login path file will include a line like this: </p>
<dl>
<dt>
<dd>
<pre>
password =
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> The TCP/IP port number to write to the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>file_name</i>, <code>-S </code><i>file_name</i> </p>
<p> The Unix socket file name to write to the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name to write to the login path.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;warn</code>, <code>-w</code> </p>
<p> Warn and prompt the user for confirmation if the command attempts to overwrite an existing login path. This option is enabled by default; use <code>&#8211;skip-warn</code> to disable it.</dl>
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
