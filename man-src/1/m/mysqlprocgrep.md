---
title: "mysqlprocgrep(1)"
name: "mysqlprocgrep"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlprocgrep/"
description: "mysqlprocgrep – Search Server Process Lists"
---

<h2 class="name">NAME</h2>
<p> mysqlprocgrep &#8211; Search Server Process Lists </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlprocgrep [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility scans the process lists for the servers specified using instances of the <code>&#8211;server</code> option and selects those that match the conditions specified using the <code>&#8211;age</code> and &#8211;match-xxx options. For a process to match, all conditions given must match. The utility then either prints the selected processes (the default) or executes certain actions on them. </p>
<p> If no <code>&#8211;age</code> or &#8211;match-xxx options are given, the utility selects all processes. </p>
<p> The &#8211;match-xxx options correspond to the columns in the <code>INFORMATION_SCHEMA.PROCESSLIST</code> table. For example, <code>&#8211;match-command</code> specifies a matching condition for <code>PROCESSLIST.COMMAND</code> column values. There is no &#8211;match-time option. To specify a condition based on process time, use <code>&#8211;age</code>. </p>
<p> Processes that can be seen and killed are subject to whether the account used to connect to the server has the <code>PROCESS</code> and <code>SUPER</code> privileges. Without <code>PROCESS</code>, the account cannot see processes belonging to other accounts Without <code>SUPER</code>, the account cannot kill processes belonging to other accounts </p>
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
<p>Options </p>
<p> <code>mysqlprocgrep</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;age=&lt;time&gt; </p>
<p> Select only processes that have been in the current state more than a given time. The time value can be specified in two formats: either using the hh:mm:ss format, with hours and minutes optional, or as a sequence of numbers with a suffix giving the period size. </p>
<p> The permitted suffixes are <code>s</code> (second), <code>m</code> (minute), <code>h</code> (hour), <code>d</code> (day), and <code>w</code> (week). For example, <code>4h15m</code> mean 4 hours and 15 minutes. </p>
<p> For both formats, the specification can optionally be preceded by + or -, where + means older than the given time, and &#8211; means younger than the given time.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </p>
<p> Specify the output display format. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;kill-connection </p>
<p> Kill the connection for all matching processes (like the <code>KILL CONNECTION</code> statement).</dl>
<dl>
<dt>
<dd> &bull; &#8211;kill-query </p>
<p> Kill the query for all matching processes (like the <code>KILL QUERY</code> statement).</dl>
<dl>
<dt>
<dd> &bull; &#8211;match-command=&lt;pattern&gt; </p>
<p> Match all processes where the <code>Command</code> field matches the pattern.</dl>
<dl>
<dt>
<dd> &bull; &#8211;match-db=&lt;pattern&gt; </p>
<p> Match all processes where the <code>Db</code> field matches the pattern.</dl>
<dl>
<dt>
<dd> &bull; &#8211;match-host=&lt;pattern&gt; </p>
<p> Match all processes where the <code>Host</code> field matches the pattern.</dl>
<dl>
<dt>
<dd> &bull; &#8211;match-info=&lt;pattern&gt; </p>
<p> Match all processes where the <code>Info</code> field matches the pattern.</dl>
<dl>
<dt>
<dd> &bull; &#8211;match-state=&lt;pattern&gt; </p>
<p> Match all processes where the <code>State</code> field matches the pattern.</dl>
<dl>
<dt>
<dd> &bull; &#8211;match-user=&lt;pattern&gt; </p>
<p> Match all processes where the <code>User</code> field matches the pattern.</dl>
<dl>
<dt>
<dd> &bull; &#8211;print </p>
<p> Print information about the matching processes. This is the default if no <code>&#8211;kill-connection</code> or <code>&#8211;kill-query</code> option is given. If a kill option is given, <code>&#8211;print</code> prints information about the processes before killing them.</dl>
<dl>
<dt>
<dd> &bull; &#8211;regexp, &#8211;basic-regexp, -G </p>
<p> Perform pattern matches using the <code>REGEXP</code> operator. The default is to use <code>LIKE</code> for matching. This affects the &#8211;match-xxx options.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server=&lt;source&gt; </p>
<p> Connection information for a server to search in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]. Use this option multiple times to search multiple servers.</dl>
<dl>
<dt>
<dd> &bull; &#8211;sql, &#8211;print-sql, -Q </p>
<p> Instead of displaying the selected processes, emit the <code>SELECT</code> statement that retrieves information about them. If the <code>&#8211;kill-connection</code> or <code>&#8211;kill-query</code> option is given, the utility generates a stored procedure named kill_processes() for killing the queries rather than a <code>SELECT</code> statement.</dl>
<dl>
<dt>
<dd> &bull; &#8211;sql-body </p>
<p> Like <code>&#8211;sql</code>, but produces the output as the body of a stored procedure without the <code>CREATE PROCEDURE</code> part of the definition. This could be used, for example, to generate an event for the server Event Manager. </p>
<p> When used with a kill option, code for killing the matching queries is generated. Note that it is not possible to execute the emitted code unless it is put in a stored routine, event, or trigger. For example, the following code could be generated to kill all idle connections for user www-data: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlprocgrep-- kill - connection-- sql - body &gt; --match - user = www - data-- match - state = sleep
                                                                        DECLARE kill_done INT;
DECLARE kill_cursor CURSOR FOR
    SELECT
        Id,
    User, Host, Db, Command, Time, State, Info FROM INFORMATION_SCHEMA.PROCESSLIST WHERE user LIKE 'www-data' AND State LIKE 'sleep' OPEN kill_cursor;
BEGIN
DECLARE id BIGINT;
DECLARE EXIT HANDLER FOR NOT FOUND SET kill_done = 1;
kill_loop : LOOP
                FETCH kill_cursor INTO id;
KILL CONNECTION id;
END LOOP kill_loop;
END;
CLOSE kill_cursor;
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> For each example, assume that the root user on localhost has sufficient privileges to kill queries and connections. </p>
<p> Kill all queries created by user mats that are younger than 1 minute: </p>
<dl>
<dt>
<dd>
mysqlprocgrep&#8211; server = root[at] localhost&#8211; match &#8211; user = mats&#8211; age = -1m &#8211;kill &#8211; query
</dl>
<p> Kill all connections that have been idle for more than 1 hour: </p>
<dl>
<dt>
<dd>
<pre><code>
mysqlprocgrep-- server = root[at] localhost-- match - command = sleep-- age = 1h --kill - connection
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
