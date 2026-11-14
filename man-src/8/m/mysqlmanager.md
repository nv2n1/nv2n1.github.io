---
title: "mysqlmanager(8)"
name: "mysqlmanager"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mysqlmanager/"
description: "mysqlmanager – the MySQL Instance Manager"
---

<p>mysqlmanager &#8211; the MySQL Instance Manager</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mysqlmanager [</code><i>options</i><code>]</code></dl>
<h2>Description</h2>
<dl>
<dd>
<dd><font SIZE="+1"> <code>Important</code> </font></p>
<dd>
<dd>MySQL Instance Manager has been deprecated and is removed in MySQL 5.5.  <code>mysqlmanager</code> is the MySQL Instance Manager (IM). This program monitors and manages MySQL Database Server instances. MySQL Instance Manager is available for Unix-like operating systems, as well as Windows. It runs as a daemon that listens on a TCP/IP port. On Unix, it also listens on a Unix socket file. MySQL Instance Manager can be used in place of the mysqld_safe script to start and stop one or more instances of MySQL Server. Because Instance Manager can manage multiple server instances, it can also be used in place of the <code>mysqld_multi</code> script. Instance Manager offers these capabilities:</p>
<dl>
<dd>* Instance Manager can start and stop instances, and report on the status of instances.</dl>
<dl>
<dd>* Server instances can be treated as guarded or unguarded:</p>
<dl>
<dd>* When Instance Manager starts, it starts each guarded instance. If the instance crashes, Instance Manager detects this and restarts it. When Instance Manager stops, it stops the instance.</dl>
<dl>
<dd>* A nonguarded instance is not started when Instance Manager starts or monitored by it. If the instance crashes after being started, Instance Manager does not restart it. When Instance Manager exits, it does not stop the instance if it is running.</dl>
<dl>
<dd>Instances are guarded by default. An instance can be designated as nonguarded by including the <code>nonguarded</code> option in the configuration file.</dl>
<dl>
<dd>* Instance Manager provides an interactive interface for configuring instances, so that the need to edit the configuration file manually is reduced or eliminated.</dl>
<dl>
<dd>* Instance Manager provides remote instance management. That is, it runs on the host where you want to control MySQL Server instances, but you can connect to it from a remote host to perform instance-management operations.</dl>
<p> The following sections describe MySQL Instance Manager operation in more detail.</dl>
<h2>Mysql Instance Manager Command Options</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> The MySQL Instance Manager supports a number of command options. For a brief listing, invoke <code>mysqlmanager</code> with the <code>&#8211;help</code> option. Options may be given on the command line or in the Instance Manager configuration file. On Windows, the standard configuration file is my.ini in the directory where Instance Manager is installed. On Unix, the standard file is /etc/my.cnf. To specify a different configuration file, start Instance Manager with the <code>&#8211;defaults-file</code> option. </p>
<p> <code>mysqlmanager</code> supports the following options. The options for managing entries in the password file are described further in the section called lqINSTANCE MANAGER USER AND PASSWORD MANAGEMENTrq. </p>
<dl>
<dd>* <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dd>* <code>&#8211;add-user</code> </p>
<p> Add a new user (specified with the <code>&#8211;username</code> option) to the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;angel-pid-file=</code><i>file_name</i> </p>
<p> The file in which the angel process records its process ID when <code>mysqlmanager</code> runs in daemon mode (that is, when the <code>&#8211;run-as-service</code> option is given). The default file name is mysqlmanager.angel.pid. </p>
<p> If the <code>&#8211;angel-pid-file</code> option is not given, the default angel PID file has the same name as the PID file except that any PID file extension is replaced with an extension of .angel.pid. (For example, mysqlmanager.pid becomes mysqlmanager.angel.pid.) </p>
<p> This option was added in MySQL 5.1.11.</dl>
<dl>
<dd>* <code>&#8211;bind-address=</code><i>IP</i> </p>
<p> The IP address to bind to.</dl>
<dl>
<dd>* <code>&#8211;check-password-file</code> </p>
<p> Check the validity and consistency of the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;clean-password-file</code> </p>
<p> Drop all users from the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;debug=</code><i>debug_options</i>, <code>-# </code><i>debug_options</i> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is &#8216;d:t:o,<i>file_name</i>&#8216;. This option was added in MySQL 5.1.10.</dl>
<dl>
<dd>* <code>&#8211;default-mysqld-path=</code><i>path</i> </p>
<p> The path name of the MySQL Server binary. This path name is used for all server instance sections in the configuration file for which no <code>mysqld-path</code> option is present. The default value of this option is the compiled-in path name, which depends on how the MySQL distribution was configured. Example: <code>&#8211;default-mysqld-path=/usr/sbin/mysqld</code></dl>
<dl>
<dd>* <code>&#8211;defaults-file=</code><i>file_name</i> </p>
<p> Read Instance Manager and MySQL Server settings from the given file. All configuration changes made by the Instance Manager will be written to this file. This must be the first option on the command line if it is used, and the file must exist. </p>
<p> If this option is not given, Instance Manager uses its standard configuration file. On Windows, the standard file is my.ini in the directory where Instance Manager is installed. On Unix, the standard file is /etc/my.cnf.</dl>
<dl>
<dd>* <code>&#8211;drop-user</code> </p>
<p> Drop a user (specified with the <code>&#8211;username</code> option) from the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;edit-user</code> </p>
<p> Change an entry for an existing user (specified with the <code>&#8211;username</code> option) in the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;install</code> </p>
<p> On Windows, install Instance Manager as a Windows service. The service name is MySQL Manager.</dl>
<dl>
<dd>* <code>&#8211;list-users</code> </p>
<p> List the users in the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;log=</code><i>file_name</i> </p>
<p> The path to the Instance Manager log file. This option has no effect unless the <code>&#8211;run-as-service</code> option is also given. If the file name specified for the option is a relative name, the log file is created under the directory from which Instance Manager is started. To ensure that the file is created in a specific directory, specify it as a full path name. </p>
<p> If <code>&#8211;run-as-service</code> is given without <code>&#8211;log</code>, the log file is mysqlmanager.log in the data directory. </p>
<p> If <code>&#8211;run-as-service</code> is not given, log messages go to the standard output. To capture log output, you can redirect Instance Manager output to a file: </p>
<dl>
<dd>
<pre>mysqlmanager &gt; im.log</pre>
</dl>
</dl>
<dl>
<dd>* <code>&#8211;monitoring-interval=</code><i>seconds</i> </p>
<p> The interval in seconds for monitoring server instances. The default value is 20 seconds. Instance Manager tries to connect to each monitored (guarded) instance using the nonexisting MySQL_Instance_Manager user account to check whether it is alive/not hanging. If the result of the connection attempt indicates that the instance is unavailable, Instance Manager performs several attempts to restart the instance. </p>
<p> Normally, the MySQL_Instance_Manager account does not exist, so the connection attempts by Instance Manager cause the monitored instance to produce messages in its general query log similar to the following: </p>
<dl>
<dd>
<pre>Access denied for user 'MySQL_Instance_M'@'localhost' Fc
 (using password: YES)</pre>
</dl>
<p> The nonguarded option in the appropriate server instance section disables monitoring for a particular instance. If the instance dies after being started, Instance Manager will not restart it. Instance Manager tries to connect to a nonguarded instance only when you request the instance&#8217;s status (for example, with the SHOW INSTANCES status. </p>
<p> See the section called lqMYSQL SERVER INSTANCE STATUS MONITORINGrq, for more information.</dl>
<dl>
<dd>* <code>&#8211;mysqld-safe-compatible</code> </p>
<p> Run in a <code>mysqld_safe</code>-compatible manner. For details, see the section called lqSTARTING THE MYSQL SERVER WITH MYSQL INSTANCE MANAGERrq. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;password=</code><i>password</i>, <code>-p </code><i>password</i> </p>
<p> Specify the password for an entry to be added to or modified in the password file. Unlike the <code>&#8211;password</code>/<code>-P</code> option for most MySQL programs, the password value is required, not optional. See also the section called lqINSTANCE MANAGER USER AND PASSWORD MANAGEMENTrq. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;password-file=</code><i>file_name</i> </p>
<p> The name of the file where the Instance Manager looks for users and passwords. On Windows, the default is mysqlmanager.passwd in the directory where Instance Manager is installed. On Unix, the default file is /etc/mysqlmanager.passwd. See also the section called lqINSTANCE MANAGER USER AND PASSWORD MANAGEMENTrq.</dl>
<dl>
<dd>* <code>&#8211;pid-file=</code><i>file_name</i> </p>
<p> The process ID file to use. On Windows, the default file is mysqlmanager.pid in the directory where Instance Manager is installed. On Unix, the default is mysqlmanager.pid in the data directory.</dl>
<dl>
<dd>* <code>&#8211;port=</code><i>port_num</i> </p>
<p> The port number to use when listening for TCP/IP connections from clients. The default port number (assigned by IANA) is 2273.</dl>
<dl>
<dd>* <code>&#8211;print-defaults</code> </p>
<p> Print the current defaults and exit. This must be the first option on the command line if it is used.</dl>
<dl>
<dd>* <code>&#8211;print-password-line</code> </p>
<p> Prepare an entry for the password file, print it to the standard output, and exit. You can redirect the output from Instance Manager to a file to save the entry in the file. </p>
<p> Prior to MySQL 5.1.12, this option was named <code>&#8211;passwd</code>.</dl>
<dl>
<dd>* <code>&#8211;remove</code> </p>
<p> On Windows, removes Instance Manager as a Windows service. This assumes that Instance Manager has been run with <code>&#8211;install</code> previously.</dl>
<dl>
<dd>* <code>&#8211;run-as-service</code> </p>
<p> On Unix, daemonize and start an angel process. The angel process monitors Instance Manager and restarts it if it crashes. (The angel process itself is simple and unlikely to crash.)</dl>
<dl>
<dd>* <code>&#8211;socket=</code><i>path</i> </p>
<p> On Unix, the socket file to use for incoming connections. The default file is named /tmp/mysqlmanager.sock. This option has no meaning on Windows.</dl>
<dl>
<dd>* <code>&#8211;standalone</code> </p>
<p> This option is used on Windows to run Instance Manager in standalone mode. You should specify it when you start Instance Manager from the command line.</dl>
<dl>
<dd>* <code>&#8211;user=</code><i>user_name</i> </p>
<p> On Unix, the user name of the system account to use for starting and running <code>mysqlmanager</code>. This option generates a warning and has no effect unless you start <code>mysqlmanager</code> as root (so that it can change its effective user ID), or as the named user. It is recommended that you configure <code>mysqlmanager</code> to run using the same account used to run the <code>mysqld</code> server. (lqUserrq in this context refers to a system login account, not a MySQL user listed in the grant tables.)</dl>
<dl>
<dd>* <code>&#8211;username=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> Specify the user name for an entry to be added to or modified in the password file. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dd>* <code>&#8211;wait-timeout=</code><i>N</i> </p>
<p> The number of seconds to wait for activity on an incoming connection before closing it. The default is 28800 seconds (8 hours). </p>
<p> This option was added in MySQL 5.1.7. Before that, the timeout is 30 seconds and cannot be changed.</dl>
<h2>Mysql Instance Manager Configuration Files</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> Instance Manager uses its standard configuration file unless it is started with a <code>&#8211;defaults-file</code> option that specifies a different file. On Windows, the standard file is my.ini in the directory where Instance Manager is installed. On Unix, the standard file is /etc/my.cnf. </p>
<p> Instance Manager reads options for itself from the [manager] section of the configuration file, and options for server instances from [mysqld] or [mysqld<i>N</i>] sections. The [manager] section contains any of the options listed in the section called lqMYSQL INSTANCE MANAGER COMMAND OPTIONSrq, except for those specified as having to be given as the first option on the command line. Here is a sample [manager] section: </p>
<dl>
<dd>
<pre># MySQL Instance Manager options section
[manager]
default-mysqld-path = /usr/local/mysql/libexec/mysqld
socket=/tmp/manager.sock
pid-file=/tmp/manager.pid
password-file = /home/cps/.mysqlmanager.passwd
monitoring-interval = 2
port = 1999
bind-address = 192.168.1.5</pre>
</dl>
<p> Each [mysqld] or [mysqld<i>N</i>] instance section specifies options given by Instance Manager to a server instance at startup. These are mainly common MySQL Server options (see Section 5.1.2, lqServer Command Optionsrq). In addition, a [mysqld<i>N</i>] section can contain the options in the following list, which are specific to Instance Manager. These options are interpreted by Instance Manager itself; it does not pass them to the server when it attempts to start that server. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> The Instance Manager-specific options must not be used in a [mysqld] section. If a server is started without using Instance Manager, it will not recognize these options and will fail to start properly. </p>
</dl>
<dl>
<dd>* mysqld-path = <i>path</i> </p>
<p> The path name of the <code>mysqld</code> server binary to use for the server instance.</dl>
<dl>
<dd>* nonguarded </p>
<p> This option disables Instance Manager monitoring functionality for the server instance. By default, an instance is guarded: At Instance Manager start time, it starts the instance. It also monitors the instance status and attempts to restart it if it fails. At Instance Manager exit time, it stops the instance. None of these things happen for nonguarded instances.</dl>
<dl>
<dd>* shutdown-delay = <i>seconds</i> </p>
<p> The number of seconds Instance Manager should wait for the server instance to shut down. The default value is 35 seconds. After the delay expires, Instance Manager assumes that the instance is hanging and attempts to terminate it. If you use InnoDB with large tables, you should increase this value.</dl>
<p> Here are some sample instance sections: </p>
<dl>
<dd>
<pre>[mysqld1]
mysqld-path=/usr/local/mysql/libexec/mysqld
socket=/tmp/mysql.sock
port=3307
server_id=1
skip-stack-trace
core-file
log-bin
log-error
log=mylog
log-slow-queries
[mysqld2]
nonguarded
port=3308
server_id=2
mysqld-path= /home/cps/mysql/trees/mysql-5.1/sql/mysqld
socket = /tmp/mysql.sock5
pid-file = /tmp/hostname.pid5
datadir= /home/cps/mysql_data/data_dir1
language=/home/cps/mysql/trees/mysql-5.1/sql/share/english
log-bin
log=/tmp/fordel.log</pre>
</dl>
<h2>Starting The Mysql Server With Mysql Instance Manager</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> This section discusses how Instance Manager starts server instances when it starts. However, before you start Instance Manager, you should set up a password file for it. Otherwise, you will not be able to connect to Instance Manager to control it after it starts. For details about creating Instance Manager accounts, see the section called lqINSTANCE MANAGER USER AND PASSWORD MANAGEMENTrq. </p>
<p> On Unix, the <code>mysqld</code> MySQL database server normally is started with the <code>mysql.server</code> script, which usually resides in the /etc/init.d/ folder. That script invokes the <code>mysqld_safe</code> script by default. However, you can use Instance Manager instead if you modify the /etc/my.cnf configuration file by adding use-manager to the [mysql.server] section: </p>
<dl>
<dd>
<pre>[mysql.server]
use-manager</pre>
</dl>
<p> Before MySQL 5.1.12, Instance Manager always tries to start at least one server instance: When it starts, it reads its configuration file if it exists to find server instance sections and prepare a list of instances. Instance sections have names of the form [mysqld] or [mysqld<i>N</i>], where <i>N</i> is an unsigned integer (for example, [mysqld1], [mysqld2], and so forth). </p>
<p> After preparing the list of instances, Instance Manager starts the guarded instances in the list. If there are no instances, Instance Manager creates an instance named mysqld and attempts to start it with default (compiled-in) configuration values. This means that the Instance Manager cannot find the <code>mysqld</code> program if it is not installed in the default location. (Section 2.1.5, lqInstallation Layoutsrq, describes default locations for components of MySQL distributions.) If you have installed the MySQL server in a nonstandard location, you should create the Instance Manager configuration file. </p>
<p> The startup behavior just described is similar to that of <code>mysqld_safe</code>, which always attempts to start a server. However, it lacks the flexibility required for some operations because it is not possible to run Instance Manager in such a way that it refrains from starting any server instances. For example, you cannot invoke Instance Manager for the purpose of configuring an instance without also starting it (a task that a MySQL installer application might want to perform). Consequently, MySQL 5.1.12 introduces the following changes: </p>
<dl>
<dd>* A new option, <code>&#8211;mysqld-safe-compatible</code>, may be used to cause Instance Manager to run with startup behavior similar to that used before MySQL 5.1.12: If Instance Manager finds a [mysqld] instance section in the configuration file, it will start it. If Instance Manager finds no [mysqld] section, it creates one using default configuration values, writes a [mysqld] section to the configuration file if it is accessible, and starts the mysqld instance. Instance Manager also starts any other guarded instances listed in the configuration file.</dl>
<dl>
<dd>* Without <code>&#8211;mysqld-safe-compatible</code>, Instance Manager reads its configuration file if it exists and starts instances for any guarded instance sections that it finds. If there are none, it starts no instances.</dl>
<p> Instance Manager also stops all guarded server instances when it shuts down. </p>
<p> The allowable options for [mysqld<i>N</i>] server instance sections are described in the section called lqMYSQL INSTANCE MANAGER CONFIGURATION FILESrq. In these sections, you can use a special <code>mysqld-path=</code><i>path-to-mysqld-binary</i> option that is recognized only by Instance Manager. Use this option to let Instance Manager know where the <code>mysqld</code> binary resides. If there are multiple instances, it may also be necessary to set other options such as <code>datadir</code> and <code>port</code>, to ensure that each instance has a different data directory and TCP/IP port number. Section 5.6, lqRunning Multiple MySQL Servers on the Same Machinerq, discusses the configuration values that must differ for each instance when you run multiple instance on the same machine. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> The [mysqld] instance section, if it exists, must not contain any Instance Manager-specific options. </p>
</dl>
<p> The typical Unix startup/shutdown cycle for a MySQL server with the MySQL Instance Manager enabled is as follows: </p>
<dl>
<dd>1. The <code>/etc/init.d/mysql</code> script starts MySQL Instance Manager.</dl>
<dl>
<dd>2. Instance Manager starts the guarded server instances and monitors them.</dl>
<dl>
<dd>3. If a server instance fails, Instance Manager restarts it.</dl>
<dl>
<dd>4. If Instance Manager is shut down (for example, with the <code>/etc/init.d/mysql stop</code> command), it shuts down all server instances.</dl>
<h2>Instance Manager User And Password Management</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> The Instance Manager stores its user information in a password file. On Windows, the default is mysqlmanager.passwd in the directory where Instance Manager is installed. On Unix, the default file is /etc/mysqlmanager.passwd. To specify a different location for the password file, use the <code>&#8211;password-file</code> option. </p>
<p> If the password file does not exist or contains no password entries, you cannot connect to the Instance Manager. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Any Instance Manager process that is running to monitor server instances does not notice changes to the password file. You must stop it and restart it after making password entry changes. </p>
</dl>
<p> Entries in the password file have the following format, where the two fields are the account user name and encrypted password, separated by a colon: </p>
<dl>
<dd>
<pre>petr:*35110DC9B4D8140F5DE667E28C72DD2597B5C848</pre>
</dl>
<p> Instance Manager password encryption is the same as that used by MySQL Server. It is a one-way operation; no means are provided for decrypting encrypted passwords. </p>
<p> Instance Manager accounts differ somewhat from MySQL Server accounts: </p>
<dl>
<dd>* MySQL Server accounts are associated with a host name, user name, and password (see Section 5.5.1, lqUser Names and Passwordsrq).</dl>
<dl>
<dd>* Instance Manager accounts are associated with a user name and password only.</dl>
<p> This means that a client can connect to Instance Manager with a given user name from any host. To limit connections so that clients can connect only from the local host, start Instance Manager with the <code>&#8211;bind-address=127.0.0.1</code> option so that it listens only to the local network interface. Remote clients will not be able to connect. Local clients can connect like this: </p>
<dl>
<dd>
<pre>shell&gt; <code>mysql -h 127.0.0.1 -P 2273</code></pre>
</dl>
<p> Before MySQL 5.1.12, the only option for creating password file entries is <code>&#8211;passwd</code>, which causes Instance Manager to prompt for user name and password values and display the resulting entry. You can save the output in the /etc/mysqlmanager.passwd password file to store it. Here is an example: </p>
<dl>
<dd>
<pre>shell&gt; <code>mysqlmanager --passwd &gt;&gt; /etc/mysqlmanager.passwd</code>
Creating record for new user.
Enter user name: <code>mike</code>
Enter password: <code>mikepass</code>
Re-type password: <code>mikepass</code></pre>
</dl>
<p> At the prompts, enter the user name and password for the new Instance Manager user. You must enter the password twice. It does not echo to the screen, so double entry guards against entering a different password than you intend (if the two passwords do not match, no entry is generated). </p>
<p> The preceding command causes the following line to be added to /etc/mysqlmanager.passwd: </p>
<dl>
<dd>
<pre>mike:*BBF1F551DD9DD96A01E66EC7DDC073911BAD17BA</pre>
</dl>
<p> Use of the <code>&#8211;password</code> option fails if <code>mysqlmanager</code> is invoked directly from an IBM 5250 terminal. To work around this, use a command like the following from the command line to generate the password entry: </p>
<dl>
<dd>
<pre>shell&gt; <code>mysql -B --skip-column-name \</code>
 <code>-e 'SELECT CONCAT(&quot;</code><i>user_name</i><code>&quot;,&quot;:&quot;,PASSWORD(&quot;</code><i>pass_val</i><code>&quot;));'</code></pre>
</dl>
<p> The output from the command can be used an entry in the /etc/mysqlmanager.passwd file. </p>
<p> Beginning with MySQL 5.1.12, the <code>&#8211;passwd</code> option is renamed to <code>&#8211;print-password-line</code> and there are several other options for managing user accounts from the command line. For example, the <code>&#8211;username</code> and <code>&#8211;password</code> options are available on the command line for specifying the user name and password for an account entry. You can use them to generate an entry with no prompting like this (type the command on a single line): </p>
<dl>
<dd>
<pre>shell&gt; <code>mysqlmanager --print-password-line</code>
 <code>--username=mike --password=mikepass &gt;&gt; /etc/mysqlmanager.passwd</code></pre>
</dl>
<p> If you omit the <code>&#8211;username</code> or <code>&#8211;password</code> option, Instance Manager prompts for the required value. </p>
<p> <code>&#8211;print-password-line</code> causes Instance Manager to send the resulting account entry to its output, which you can append to the password file. The following list describes other account-management options that cause Instance Manager to operate directly on the password file. (These options make Instance Manager scriptable for account-management purposes.) For operations on the password file to succeed, the file must exist and it must be accessible by Instance Manager. (The exception is <code>&#8211;clean-password-file</code>, which creates the file if it does not exist. Alternatively, if there is no password file, manually create it as an empty file and ensure that its ownership and access modes allow it to be read and written by Instance Manager.) The default password file is used unless you specify a <code>&#8211;password-file</code> option. </p>
<p> To ensure consistent treatment of the password file, it should be owned by the system account that you use for running Instance Manager to manage server instances, and you should invoke it from that account when you use it to manage accounts in the password file. </p>
<dl>
<dd>* Create a new user: </p>
<dl>
<dd>
<pre>mysqlmanager --add-user --username=<i>user_name</i> [--password=<i>password</i>]</pre>
</dl>
<p> This command adds a new entry with the given user name and password to the password file. The <code>&#8211;username</code> (or <code>-u</code>) option is required. <code>mysqlmanager</code> prompts for the password if it is not given on the command line with the <code>&#8211;password</code> (or <code>-p</code>) option. The command fails if the user already exists.</dl>
<dl>
<dd>* Drop an existing user: </p>
<dl>
<dd>
<pre>mysqlmanager --drop-user --username=<i>user_name</i></pre>
</dl>
<p> This command removes the entry with the given user name from the password file. The user name is required. The command fails if the user does not exist.</dl>
<dl>
<dd>* Change the password for an existing user: </p>
<dl>
<dd>
<pre>mysqlmanager --edit-user --username=<i>user_name</i> [--password=<i>password</i>]</pre>
</dl>
<p> This command changes the given user&#8217;s password in the password file. The user name is required. <code>mysqlmanager</code> prompts for the password it is not given on the command line. The command fails if the user does not exist.</dl>
<dl>
<dd>* List existing users: </p>
<dl>
<dd>
<pre>mysqlmanager --list-users</pre>
</dl>
<p> This command lists the user names of the accounts in the password file.</dl>
<dl>
<dd>* Check the password file: </p>
<dl>
<dd>
<pre>mysqlmanager --check-password-file</pre>
</dl>
<p> This command performs a consistency and validity check of the password file. The command fails if there is something wrong with the file.</dl>
<dl>
<dd>* Empty the password file: </p>
<dl>
<dd>
<pre>mysqlmanager --clean-password-file</pre>
</dl>
<p> This command empties the password file, which has the effect of dropping all users listed in it. The option creates the password file if it does not exist, so it can be used to initialize a new password file to be used for other account-management operations. Take care not to use this option to reinitialize a file containing accounts that you do not want to drop.</dl>
<h2>Mysql Server Instance Status Monitoring</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> To monitor the status of each guarded server instance, the MySQL Instance Manager attempts to connect to the instance at regular intervals using the MySQL_Instance_Manager [at] localhost user account with a password of check_connection. </p>
<p> You are <i>not</i> required to create this account for MySQL Server; in fact, it is expected that it will not exist. Instance Manager can tell that a server is operational if the server accepts the connection attempt but refuses access for the account by returning a login error. However, these failed connection attempts are logged by the server to its general query log (see Section 5.2.3, lqThe General Query Logrq). </p>
<p> Instance Manager also attempts a connection to nonguarded server instances when you use the SHOW INSTANCES or SHOW INSTANCE STATUS command. This is the only status monitoring done for nonguarded instances. </p>
<p> Instance Manager knows if a server instance fails at startup because it receives a status from the attempt. For an instance that starts but later crashes, Instance Manager receives a signal because it is the parent process of the instance. </p>
<p> Beginning with MySQL 5.1.12, Instance Manager tracks instance states so that it can determine which commands are allowed for each instance. For example, commands that modify an instance&#8217;s configuration are allowed only while the instance is offline. </p>
<p> Each instance is in one of the states described in the following table. Guarded instances can be in any of the states. Nonguarded instances can only be offline or online. Instance state information is displayed in the status column of the SHOW INSTANCES and SHOW INSTANCE STATUS commands. </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>State</code> </td>
<td> <code>Meaning</code>
</td>
</tr>
<tr VALIGN=top>
<td> offline </td>
<td> The instance has not been started and is not running.
</td>
</tr>
<tr VALIGN=top>
<td> starting </td>
<td> The instance is starting (initializing). Nonguarded instances cannot be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in this state. A nonguarded instance goes directly from<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>offline to online.
</td>
</tr>
<tr VALIGN=top>
<td> stopping </td>
<td> The instance is stopping. Nonguarded instances cannot be in this state.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A nonguarded instance goes directly from online to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>offline, or stays offline if startup fails.
</td>
</tr>
<tr VALIGN=top>
<td> online </td>
<td> The instance has started and is running.
</td>
</tr>
<tr VALIGN=top>
<td> failed </td>
<td> The instance was online but it crashed and is being restarted by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Instance Manager, or else the instance failed to start<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>at all and Instance Manager is again attempting to start<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>it. Nonguarded instances cannot be in this state.
</td>
</tr>
<tr VALIGN=top>
<td> crashed </td>
<td> Instance Manager failed to start the instance after several attempts.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Instance Manager will try again later.)&nbsp;<wbr>Nonguarded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instances cannot be in this state.
</td>
</tr>
<tr VALIGN=top>
<td> abandoned </td>
<td> Instance Manager was not able to start the instance, has given up, and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>will make no further attempts until instructed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>otherwise. To tell Instance Manager to try again, you<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>must first use STOP INSTANCE to put<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the instance in offline state, and then use<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>START INSTANCE to start the instance.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>If it is necessary to make configuration changes for the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instance, you must do so after putting the instance<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>offline and before starting it.&nbsp;<wbr>(Instance Manager<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>accepts configuration-changing commands only for offline<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instances.)&nbsp;<wbr>Nonguarded instances cannot be in this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>state.
</td>
</tr>
</table>
<h2>Connecting To Mysql Instance Manager</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> After you set up a password file for the MySQL Instance Manager and Instance Manager is running, you can connect to it. The MySQL client-server protocol is used to communicate with the Instance Manager. For example, you can connect to it using the standard <code>mysql</code> client program: </p>
<dl>
<dd>
<pre>shell&gt; <code>mysql --port=2273 --host=im.example.org --user=mysql --password</code></pre>
</dl>
<p> Instance Manager supports the version of the MySQL client-server protocol used by the client tools and libraries distributed with MySQL 4.1 or later, so other programs that use the MySQL C API also can connect to it.</p>
<h2>Mysql Instance Manager Commands</h2>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font> </p>
<p> MySQL Instance Manager has been deprecated and is removed in MySQL 5.5. </p>
</dl>
<p> After you connect to MySQL Instance Manager, you can issue commands. The following general principles apply to Instance Manager command execution: </p>
<dl>
<dd>* Commands that take an instance name fail if the name is not a valid instance name.</dl>
<dl>
<dd>* Commands that take an instance name (other than CREATE INSTANCE) fail if the instance does not exist.</dl>
<dl>
<dd>* As of MySQL 5.1.12, commands for an instance require that the instance be in an appropriate state. You cannot configure or start an instance that is not offline. You cannot start an instance that is online.</dl>
<dl>
<dd>* Instance Manager maintains information about instance configuration in an internal (in-memory) cache. Initially, this information comes from the configuration file if it exists, but some commands change the configuration of an instance. Commands that modify the configuration file fail if the file does not exist or is not accessible to Instance Manager. </p>
<p> As of MySQL 5.1.12, configuration-changing commands modify both the in-memory cache and the server instance section recorded in the configuration file to maintain consistency between them. For this to occur, the instance must be offline and the configuration file must be accessible and not malformed. If the configuration file cannot be updated, the command fails and the cache remains unchanged.</dl>
<dl>
<dd>* On Windows, the standard file is my.ini in the directory where Instance Manager is installed. On Unix, the standard configuration file is /etc/my.cnf. To specify a different configuration file, start Instance Manager with the <code>&#8211;defaults-file</code> option.</dl>
<dl>
<dd>* If a [mysqld] instance section exists in the configuration file, it must not contain any Instance Manager-specific options (see the section called lqMYSQL INSTANCE MANAGER CONFIGURATION FILESrq). Therefore, you must not add any of these options if you change the configuration for an instance named mysqld.</dl>
<p> The following list describes the commands that Instance Manager accepts, with examples. </p>
<dl>
<dd>* CREATE INSTANCE <i>instance_name</i> [<i>option_name</i>[=<i>option_value</i>], &#8230;] </p>
<p> This command configures a new instance by creating an [<i>instance_name</i>] section in the configuration file. The command fails if <i>instance_name</i> is not a valid instance name or the instance already exists. </p>
<p> The created section instance is empty if no options are given. Otherwise, the options are added to the section. Options should be given in the same format used when you write options in option files. (See Section 4.2.3.3, lqUsing Option Filesrq for a description of the allowable syntax.) If you specify multiple options, separate them by commas. </p>
<p> For example, to create an instance section named [mysqld98], you might write something like this were you to modify the configuration file directly: </p>
<dl>
<dd>
<pre>[mysqld98]
basedir=/var/mysql98</pre>
</dl>
<p> To achieve the same effect via CREATE INSTANCE, issue this command to Instance Manager: </p>
<dl>
<dd>
<pre>mysql&gt; <code>CREATE INSTANCE mysqld98 basedir=&quot;/var/mysql98&quot;;</code>
Query OK, 0 rows affected (0,00 sec)</pre>
</dl>
<p> CREATE INSTANCE creates the instance but does not start it. </p>
<p> If the instance name is the (deprecated) name mysqld, the option list cannot include any options that are specific to Instance Manager, such as nonguarded (see the section called lqMYSQL INSTANCE MANAGER CONFIGURATION FILESrq). </p>
<p> This command was added in MySQL 5.1.12.</dl>
<dl>
<dd>* DROP INSTANCE <i>instance_name</i> </p>
<p> This command removes the configuration for <i>instance_name</i> from the configuration file. </p>
<dl>
<dd>
<pre>mysql&gt; <code>DROP INSTANCE mysqld98;</code>
Query OK, 0 rows affected (0,00 sec)</pre>
</dl>
<p> The command fails if <i>instance_name</i> is not a valid instance name, the instance does not exist, or is not offline. </p>
<p> This command was added in MySQL 5.1.12.</dl>
<dl>
<dd>* START INSTANCE <i>instance_name</i> </p>
<p> This command attempts to start an offline instance. The command is asynchronous; it does not wait for the instance to start. </p>
<dl>
<dd>
<pre>mysql&gt; <code>START INSTANCE mysqld4;</code>
Query OK, 0 rows affected (0,00 sec)</pre>
</dl>
</dl>
<dl>
<dd>* STOP INSTANCE <i>instance_name</i> </p>
<p> This command attempts to stop an instance. The command is synchronous; it waits for the instance to stop. </p>
<dl>
<dd>
<pre>mysql&gt; <code>STOP INSTANCE mysqld4;</code>
Query OK, 0 rows affected (0,00 sec)</pre>
</dl>
</dl>
<dl>
<dd>* SHOW INSTANCES </p>
<p> Shows the names and status of all loaded instances. </p>
<dl>
<dd>
<pre>mysql&gt; <code>SHOW INSTANCES;</code>
+---------------+---------+
| instance_name | status |
+---------------+---------+
| mysqld3 | offline |
| mysqld4 | online |
| mysqld2 | offline |
+---------------+---------+</pre>
</dl>
</dl>
<dl>
<dd>* SHOW INSTANCE STATUS <i>instance_name</i> </p>
<p> Shows status and version information for an instance. </p>
<dl>
<dd>
<pre>mysql&gt; <code>SHOW INSTANCE STATUS mysqld3;</code>
+---------------+--------+---------+
| instance_name | status | version |
+---------------+--------+---------+
| mysqld3 | online | unknown |
+---------------+--------+---------+</pre>
</dl>
</dl>
<dl>
<dd>* SHOW INSTANCE OPTIONS <i>instance_name</i> </p>
<p> Shows the options used by an instance. </p>
<dl>
<dd>
<pre>mysql&gt; <code>SHOW INSTANCE OPTIONS mysqld3;</code>
+---------------+---------------------------------------------------+
| option_name | value |
+---------------+---------------------------------------------------+
| instance_name | mysqld3 |
| mysqld-path | /home/cps/mysql/trees/mysql-4.1/sql/mysqld |
| port | 3309 |
| socket | /tmp/mysql.sock3 |
| pid-file | hostname.pid3 |
| datadir | /home/cps/mysql_data/data_dir1/ |
| language | /home/cps/mysql/trees/mysql-4.1/sql/share/english |
+---------------+---------------------------------------------------+</pre>
</dl>
</dl>
<dl>
<dd>* SHOW <i>instance_name</i> LOG FILES </p>
<p> The command lists all log files used by the instance. The result set contains the path to the log file and the log file size. If no log file path is specified in the instance section of the configuration file (for example, log=/var/mysql.log), the Instance Manager tries to guess its placement. If Instance Manager is unable to guess the log file placement you should specify the log file location explicitly by using a log option in the appropriate instance section of the configuration file. </p>
<dl>
<dd>
<pre>mysql&gt; <code>SHOW mysqld LOG FILES;</code>
+-------------+------------------------------------+----------+
| Logfile | Path | Filesize |
+-------------+------------------------------------+----------+
| ERROR LOG | /home/cps/var/mysql/owlet.err | 9186 |
| GENERAL LOG | /home/cps/var/mysql/owlet.log | 471503 |
| SLOW LOG | /home/cps/var/mysql/owlet-slow.log | 4463 |
+-------------+------------------------------------+----------+</pre>
</dl>
<p> SHOW &#8230; LOG FILES displays information only about log files. If a server instance uses log tables (see Section 5.2.1, lqSelecting General Query and Slow Query Log Output Destinationsrq), no information about those tables is shown. </p>
<p> Log options are described in Section 5.1.2, lqServer Command Optionsrq.</dl>
<dl>
<dd>* SHOW <i>instance_name</i> LOG {ERROR | SLOW | GENERAL} <i>size</i>[,<i>offset_from_end</i>] </p>
<p> This command retrieves a portion of the specified log file. Because most users are interested in the latest log messages, the <i>size</i> parameter defines the number of bytes to retrieve from the end of the log. To retrieve data from the middle of the log file, specify the optional <i>offset_from_end</i> parameter. The following example retrieves 21 bytes of data, starting 23 bytes before the end of the log file and ending 2 bytes before the end: </p>
<dl>
<dd>
<pre>mysql&gt; <code>SHOW mysqld LOG GENERAL 21, 2;</code>
+---------------------+
| Log |
+---------------------+
| using password: YES |
+---------------------+</pre>
</dl>
</dl>
<dl>
<dd>* SET <i>instance_name</i>.<i>option_name</i>[=<i>option_value</i>] </p>
<p> This command edits the specified instance&#8217;s configuration section to change or add instance options. The option is added to the section is it is not already present. Otherwise, the new setting replaces the existing one. </p>
<dl>
<dd>
<pre>mysql&gt; <code>SET mysqld2.port=3322;</code>
Query OK, 0 rows affected (0.00 sec)</pre>
</dl>
<p> As of MySQL 5.1.12, you can specify multiple options (separated by commas), and SET can be used only for offline instances. Each option must indicate the instance name: </p>
<dl>
<dd>
<pre>mysql&gt; <code>SET mysqld2.port=3322, mysqld3.nonguarded;</code>
Query OK, 0 rows affected (0.00 sec)</pre>
</dl>
<p> Before MySQL 5.1.12, only a single option can be specified. Also, changes made to the configuration file do not take effect until the MySQL server is restarted. In addition, these changes are not stored in the instance manager&#8217;s local cache of instance settings until a FLUSH INSTANCES command is executed.</dl>
<dl>
<dd>* UNSET <i>instance_name</i>.<i>option_name</i> </p>
<p> This command removes an option from an instance&#8217;s configuration section. </p>
<dl>
<dd>
<pre>mysql&gt; <code>UNSET mysqld2.port;</code>
Query OK, 0 rows affected (0.00 sec)</pre>
</dl>
<p> As of MySQL 5.1.12, you can specify multiple options (separated by commas), and UNSET can be used only for offline instances. Each option must indicate the instance name: </p>
<dl>
<dd>
<pre>mysql&gt; <code>UNSET mysqld2.port, mysqld4.nonguarded;</code>
Query OK, 0 rows affected (0.00 sec)</pre>
</dl>
<p> Before MySQL 5.1.12, only a single option can be specified. Also, changes made to the configuration file do not take effect until the MySQL server is restarted. In addition, these changes are not stored in the instance manager&#8217;s local cache of instance settings until a FLUSH INSTANCES command is executed.</dl>
<dl>
<dd>* FLUSH INSTANCES </p>
<p> As of MySQL 5.1.12, FLUSH INSTANCES cannot be used unless all instances are offline. The command causes Instance Manager to reread the configuration file, update its in-memory configuration cache, and start any guarded instances. </p>
<p> Before MySQL 5.1.12, this command forces Instance Manager reread the configuration file and to refresh internal structures. This command should be performed after editing the configuration file. The command does not restart instances. </p>
<dl>
<dd>
<pre>mysql&gt; <code>FLUSH INSTANCES;</code>
Query OK, 0 rows affected (0.04 sec)</pre>
</dl>
</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
<h2>See Also</h2>
<p>For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>Author</h2>
<p>Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).</p>
