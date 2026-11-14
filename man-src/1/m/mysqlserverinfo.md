---
title: "mysqlserverinfo(1)"
name: "mysqlserverinfo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlserverinfo/"
description: "mysqlserverinfo – Display Common Diagnostic Information from a Server"
---

<h2 class="name">NAME</h2>
<p> mysqlserverinfo &#8211; Display Common Diagnostic Information from a Server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlserverinfo [</code><i>options</i><code>] </code><i>db1</i><code> [</code><i>:db2</i><code>] &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility displays critical information about a server for use in diagnosing problems. The information displayed includes the following: </p>
<dl>
<dt>
<dd> &bull; Server connection information</dl>
<dl>
<dt>
<dd> &bull; Server version number</dl>
<dl>
<dt>
<dd> &bull; Data directory path name</dl>
<dl>
<dt>
<dd> &bull; Base directory path name</dl>
<dl>
<dt>
<dd> &bull; Plugin directory path name</dl>
<dl>
<dt>
<dd> &bull; Configuration file location and name</dl>
<dl>
<dt>
<dd> &bull; Current binary log coordinates (file name and position)</dl>
<dl>
<dt>
<dd> &bull; Current relay log coordinates (file name and position)</dl>
<p> This utility can be used to see the diagnostic information for servers that are running or offline. If you want to see information about an offline server, the utility starts the server in read-only mode. In this case, you must specify the <code>&#8211;basedir</code>, <code>&#8211;datadir</code>, and <code>&#8211;start</code> options to prevent the utility from starting an offline server accidentally. Note: Be sure to consider the ramifications of starting an offline server on the error and similar logs. It is best to save this information prior to running this utility. </p>
<p> To specify how to display output, use one of the following values with the <code>&#8211;format</code> option: </p>
<dl>
<dt>
<dd> &bull; <code>grid</code> (default) </p>
<p> Display output in grid or table format like that of the <code>mysql</code> monitor.</dl>
<dl>
<dt>
<dd> &bull; <code>csv</code> </p>
<p> Display output in comma-separated values format.</dl>
<dl>
<dt>
<dd> &bull; <code>tab</code> </p>
<p> Display output in tab-separated format.</dl>
<dl>
<dt>
<dd> &bull; <code>vertical</code> </p>
<p> Display output in single-column format like that of the \G command for the <code>mysql</code> monitor.</dl>
<p> To turn off the headers for <code>csv</code> or <code>tab</code> display format, specify the <code>&#8211;no-headers</code> option. </p>
<p> To see the common default settings for the local server&#8217;s configuration file, use the <code>&#8211;show-defaults</code> option. This option reads the configuration file on the machine where the utility is run, not the machine for the host that the <code>&#8211;server</code> option specifies. </p>
<p> To run the utility against several servers, specify the <code>&#8211;server</code> option multiple times. In this case, the utility attempts to connect to each server and read the information. </p>
<p> To see the MySQL servers running on the local machine, use the <code>&#8211;show-servers</code> option. This shows all the servers with their process ID and data directory. On Windows, the utility shows only the process ID and port.<br />
OPTIONS </p>
<p> <code>mysqlserverinfo</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;basedir=&lt;basedir&gt; </p>
<p> The base directory for the server. This option is required for starting an offline server. </p>
<p> Is also used to access server tools, such as my_print_defaults that is required to read the login-path values from the login configuration file (.mylogin.cnf).</dl>
<dl>
<dt>
<dd> &bull; &#8211;datadir=&lt;datadir&gt; </p>
<p> The data directory for the server. This option is required for starting an offline server.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </p>
<p> Specify the output display format. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;no-headers, -h </p>
<p> Do not display column headers. This option applies only for <code>csv</code> and <code>tab</code> output.</dl>
<dl>
<dt>
<dd> &bull; &#8211;port-range=&lt;start:end&gt; </p>
<p> The port range to check for finding running servers. This option applies only to Windows and is ignored unless <code>&#8211;show-servers</code> is given. The default range is 3306:3333.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server=&lt;server&gt; </p>
<p> Connection information for a server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]. Use this option multiple times to see information for multiple servers.</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-defaults, -d </p>
<p> Display default settings for <code>mysqld</code> from the local configuration file. It uses <code>my_print_defaults</code> to obtain the options.</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-servers </p>
<p> Display information about servers running on the local host. The utility examines the host process list to determine which servers are running.</dl>
<dl>
<dt>
<dd> &bull; &#8211;start, -s </p>
<p> Start the server in read-only mode if it is offline. With this option, you must also give the <code>&#8211;basedir</code> and <code>&#8211;datadir</code> options.</dl>
<dl>
<dt>
<dd> &bull; &#8211;start-timeout </p>
<p> Number of seconds to wait for the server to be online when started in read-only mode using the <code>&#8211;start</code> option. The default value is 10 seconds. </p>
<p> The &#8211;start-timeout option is available as of MySQL Utilities 1.2.4 / 1.3.3.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To display the server information for the local server and the settings for <code>mysqld</code> in the configuration file with the output in a vertical list, use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlserverinfo --server=root:pass [at] localhost -d --format=vertical
#Source on localhost : ... connected.
*************************       1. row *************************
         server: localhost:3306
        version: 5.1.50-log
        datadir: /usr/local/mysql/data/
        basedir: /usr/local/mysql-5.1.50-osx10.6-x86_64/
     plugin_dir: /usr/local/mysql-5.1.50-osx10.6-x86_64/lib/plugin
    config_file: /etc/my.cnf
     binary_log: my_log.000068
 binary_log_pos: 212383
      relay_log: None
  relay_log_pos: None
1 rows.
Defaults for server localhost:3306
  --port=3306
  --basedir=/usr/local/mysql
  --datadir=/usr/local/mysql/data
  --server_id=5
  --log-bin=my_log
  --general_log
  --slow_query_log
  --innodb_data_file_path=ibdata1:778M;
ibdata2 : 50M : autoextend
#... done.
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
