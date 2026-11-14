---
title: "mysqluc(1)"
name: "mysqluc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqluc/"
description: "mysqluc – Command line client for running MySQL Utilities"
---

<h2 class="name">NAME</h2>
<p> mysqluc &#8211; Command line client for running MySQL Utilities </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqluc [&#8211;help | &#8211;version | [ | &#8211;verbose | &#8211;quiet |] &#8211;width=&lt;num&gt; | &#8211;utildir=&lt;path&gt; | &#8211;execute &lt;command list&gt; &lt;variable&gt;=&lt;value&gt;]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility provides a command line environment for running MySQL Utilities. </p>
<p> The mysqluc utility, hence console, allows users to execute any of the currently installed MySQL Utilities command. The option <code>&#8211;utildir</code> is used to provide a path to the MySQL Utilities if the location is different from when the utility is executed. </p>
<p> The console has a list of console or base commands. These allow the user to interact with the features of the console itself. The list of base commands is shown below along with a brief description.: </p>
<dl>
<dt>
<dd>
<pre><code>
Command                 Description
----------------------  ---------------------------------------------------
help utilities          Display list of all utilities supported.
help &lt;utility&gt;          Display help for a specific utility.
help | help commands    Show this list.
exit | quit             Exit the console.
set &lt;variable&gt;=&lt;value&gt;  Store a variable for recall in commands.
show options            Display list of options specified by the user on
                        launch.
show variables          Display list of variables.
&lt;ENTER&gt;                 Press ENTER to execute command.
&lt;ESCAPE&gt;                Press ESCAPE to clear the command entry.
&lt;DOWN&gt;                  Press DOWN to retrieve the previous command.
&lt;UP&gt;                    Press UP to retrieve the next command in history.
&lt;TAB&gt;                   Press TAB for type completion of utility, option,
                        or variable names.
&lt;TAB&gt;&lt;TAB&gt;              Press TAB twice for list of matching type
                        completion (context sensitive).
</code></pre>
</dl>
<p> One of the most helpful base commands is the ability to see the options for a given utility by typing &#8216;help &lt;utility&gt;&#8217;. When the user types this command and presses ENTER, the console will display a list of all of the options for the utility. </p>
<p> The console provides tab completion for all commands, options for utilities, and user-defined variables. Tab completion for commands allows users to specify the starting N characters of a command and press TAB to complete the command. If there are more than one command that matches the prefix, and the user presses TAB twice, a list of all possible matches is displayed. </p>
<p> Tab completion for options is similar. The user must first type a valid MySQL Utility command then types the first N characters of a command and presses TAB, for example &#8211;verb&lt;TAB&gt;. In this case, the console will complete the option. For the cases where an option requires a value, the console will complete the option name and append the &#8216;=&#8217; character. Tab completion for options works for both the full name and the alias (if available). If the user presses TAB twice, the console will display a list of matching options. Pressing TAB twice immediately after typing the name of a MySQL Utility will display a list of all options for that utility. </p>
<p> Tab completion for variables works the same as that for options. In this case, the user must first type the &#8216;$&#8217; character then press TAB. For example, if a variable $SERVER1 exists, when the user types &#8211;server=$SER&lt;TAB&gt;, the console will complete the $SERVER variable name. For cases where there are multiple variables, pressing TAB twice will display a list of all matches to the first $+N characters. Pressing TAB twice after typing only the $ character will display a list of all variables. </p>
<p> Note: the console does not require typing the &#8216;mysql&#8217; prefix for the utility. For example, if the user types &#8216;disku&lt;TAB&gt;&#8217; the console will complete the command with &#8216;diskusage &#8216;. </p>
<p> Executing utilities is accomplished by typing the complete command and pressing ENTER. The user does not have to type &#8216;python&#8217; or provide the &#8216;.py&#8217; file extension. The console will add these if needed. </p>
<p> The user can also run commands using the option <code>&#8211;execute</code>. The value for this option is a semi-colon separated list of commands to execute. These can be base commands or MySQL Utility commands. The console will execute each command and display the output. All commands to be run by the console must appear inside a quoted string and separated by semi-colons. Commands outside of the quoted string will be treated as arguments for the mysqluc utility itself and thus ignored for execution. </p>
<p> Note: if there is an error in the console or related code, the console will stop executing commands at the point of failure. Commands may also be piped into the console using a mechanism like &#8216;echo &#8220;&lt;commands&gt;&#8221; | mysqluc&#8221;. </p>
<p> The console also allows users to set user-defined variables for commonly used values in options. The syntax is simply &#8216;set VARNAME=VALUE&#8217;. The user can see a list of all variables by entering the &#8216;show variables&#8217; command. To use the values of these variables in utility commands, the user must prefix the value with a &#8216;$&#8217;. For example, &#8211;server=$SERVER1 will substitute the value of the SERVER1 user-defined variable when the utility is executed. </p>
<p> Note: user-defined variables have a session lifetime. They are not saved from one execution to another of the users console. </p>
<p> User-defined variables may also be set by passing them as arguments to the mysqluc command. For example, to set the SERVER1 variable and launch the console, the user can launch the console using this command.: </p>
<dl>
<dt>
<dd>
<pre>
$ mysqluc SERVER1=root [at] localhost
</pre>
</dl>
<p> The user can provide any number of user-defined variables but they must contain a value and no spaces around the &#8216;=&#8217; character. Once the console is launched, the user can see all variables using the &#8216;show variables&#8217; command.<br />
OPTIONS </p>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> show program&#8217;s version number and exit</dl>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> show the program&#8217;s help page</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> control how much information is displayed. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet </p>
<p> suppress all informational messages</dl>
<dl>
<dt>
<dd> &bull; &#8211;execute &lt;commands&gt;, -e &lt;commands&gt; </p>
<p> Execute commands and exit. Multiple commands are separated with semi-colons. Note: some platforms may require double quotes around command list.</dl>
<dl>
<dt>
<dd> &bull; &#8211;utildir &lt;path&gt; </p>
<p> location of utilities</dl>
<dl>
<dt>
<dd> &bull; &#8211;width &lt;number&gt; </p>
<p> Display width</dl>
<p>NOTES </p>
<p> Using the <code>&#8211;execute</code> option or piping commands to the console may require quotes or double quotes (for example, on Windows).<br />
EXAMPLES </p>
<p> To launch the console, use this command: </p>
<dl>
<dt>
<dd>
<pre>
$ mysqluc
</pre>
</dl>
<p> The following demonstrates launching the console and running the console command &#8216;help utilities&#8217; to see a list of all utilities supported. The console will execute the command then exit.: </p>
<dl>
<dt>
<dd>
$ mysqluc -e &#8220;help utilities&#8221;<br />
Utility           Description<br />
&#8212;&#8212;&#8212;&#8212;&#8212;-  &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
mysqlindexcheck   check for duplicate or redundant indexes<br />
mysqlrplcheck     check replication<br />
mysqluserclone    clone a MySQL user account to one or more new users<br />
mysqldbcompare    compare databases for consistency<br />
mysqldiff         compare object definitions among objects where the<br />
                  difference is how db1.obj1 differs from db2.obj2<br />
mysqldbcopy       copy databases from one server to another<br />
mysqlreplicate    establish replication with a master<br />
mysqldbexport     export metadata and data from databases<br />
mysqldbimport     import metadata and data from files<br />
mysqlmetagrep     search metadata<br />
mysqlprocgrep     search process information<br />
mysqldiskusage    show disk usage for databases<br />
mysqlserverinfo   show server information<br />
mysqlserverclone  start another instance of a running server
</dl>
<p> The following demonstrates launching the console to run several commands using the &#8211;execute option to including setting a variable for a server connection and executing a utility using variable substitution. Note: it may be necessary to escape the &#8216;$&#8217; on some platforms (for example, Linux). Output below is an excerpt and is representational only.: </p>
<dl>
<dt>
<dd>
$ mysqluc &#8211; e &#8220;set SERVER=root [at] host123; mysqldiskusage &#8211;server=\$SERVER&#8221;<br />
#Source on host123 : &#8230; connected.<br />
            NOTICE : Your user account does not have read access to the datadir.Data sizes will be calculated and actual file sizes may be omitted.Some features may be unavailable.<br />
#Database totals:<br />
        + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ |<br />
    db_name | total |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8230; | world | 0 |<br />
    &#8230; + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+Total database disk usage = 1,<br />
                                                                                 072, 359, 052 bytes or 1022.00 MB<br />
#&#8230; done.
</dl>
<p> The following demonstrates launching the console using the commands shown above but piped into the console on the command line. The results are the same as above.: </p>
<dl>
<dt>
<dd>
$ echo &#8220;set SERVER=root [at] host123; mysqldiskusage &#8211;server=\$SERVER&#8221; | mysqluc
</dl>
<p> The following demonstrates launching the console and setting variables via the command line.: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqluc SERVER = root[at] host123 VAR_A = 57 - e "show variables" Variable Value-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -SERVER root[at] host123
                                                     VAR_A 57
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
