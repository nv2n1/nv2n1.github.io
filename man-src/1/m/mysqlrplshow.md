---
title: "mysqlrplshow(1)"
name: "mysqlrplshow"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlrplshow/"
description: "mysqlrplshow – Show Slaves for Master Server"
---

<h2 class="name">NAME</h2>
<p> mysqlrplshow &#8211; Show Slaves for Master Server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlrplshow [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility shows the replication slaves for a master. It prints a graph of the master and its slaves labeling each with the host name and port number. </p>
<p> You must specify the <code>&#8211;discover-slaves-login </code> option to provide the user name and password to discover any slaves in the topology. </p>
<p> To explore the slaves for each client, use the <code>&#8211;recurse</code> option. This causes the utility to connect to each slave found and attempt to determine whether it has any slaves. If slaves are found, the process continues until the slave is found in the list of servers serving as masters (a circular topology). The graph displays the topology with successive indents. A notation is made for circular topologies. </p>
<p> If you use the <code>&#8211;recurse</code> option, the utility attempts to connect to the slaves using the user name and password provided for the master. By default, if the connection attempt fails, the utility throws an error and stops. To change this behavior, use the <code>&#8211;prompt</code> option, which permits the utility to prompt for the user name and password for each slave that fails to connect. You can also use the <code>&#8211;num-retries=n</code> option to reattempt a failed connection &#8216;n&#8217; times before the utility fails. </p>
<p> An example graph for a typical topology with relay slaves is shown here: </p>
<dl>
<dt>
<dd>
<pre>
# Replication Topology Graph::
localhost:3311 (MASTER)
   |
   +--- localhost:3310 - (SLAVE)
   |
   +--- localhost:3312 - (SLAVE + MASTER)
       |
       +--- localhost:3313 - (SLAVE)
</pre>
</dl>
<p> MASTER, SLAVE, and SLAVE+MASTER indicate that a server is a master only, slave only, and both slave and master, respectively. </p>
<p> A circular replication topology is shown like this, where &lt;&#8211;&gt; indicates circularity: </p>
<dl>
<dt>
<dd>
<pre><code>
#Replication Topology Graph
localhost : 3311(MASTER) |
    +-- -localhost : 3312 - (SLAVE + MASTER) |
    +-- -localhost : 3313 - (SLAVE + MASTER) |
    +-- -localhost : 3311 &lt; -- &gt; (SLAVE)
</code></pre>
</dl>
<p> To produce a column list in addition to the graph, specify the <code>&#8211;show-list</code> option. In this case, to specify how to display the list, use one of the following values with the <code>&#8211;format</code> option: </p>
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
<p> The utility uses of the <code>SHOW SLAVE HOSTS</code> statement to determine which slaves the master has. If you want to use the <code>&#8211;recurse</code> option, slaves should have been started with the &#8211;report-host and &#8211;report-port options set to their actual host name and port number or the utility may not be able to connect to the slaves to determine their own slaves.<br />
OPTIONS </p>
<p> <code>mysqlrplshow</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;discover-slaves-login=&lt;slave-login&gt; </p>
<p> Supply the user and password in the form &lt;user&gt;[:&lt;passwd&gt;] or &lt;login-path&gt; for discovering slaves and relay slaves in the topology. For example, &#8211;discover=joe:secret will use &#8216;joe&#8217; as the user and &#8216;secret&#8217; as the password for each discovered slave.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </p>
<p> Specify the display format for column list output. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>. This option applies only if <code>&#8211;show-list</code> is given.</dl>
<dl>
<dt>
<dd> &bull; &#8211;master=&lt;source&gt; </p>
<p> Connection information for the master server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;max-depth=&lt;N&gt; </p>
<p> The maximum recursion depth. This option is valid only if <code>&#8211;recurse</code> is given.</dl>
<dl>
<dt>
<dd> &bull; &#8211;num-retries=&lt;num_retries&gt;, -n&lt;num_retries&gt; </p>
<p> The number of retries permitted for failed slave login attempts. This option is valid only if <code>&#8211;prompt</code> is given.</dl>
<dl>
<dt>
<dd> &bull; &#8211;prompt, -p </p>
<p> Prompt for the slave user and password if different from the master user and password. </p>
<p> If you give this option, the utility sets <code>&#8211;num-retries</code> to 1 if that option is not set explicitly. This ensures at least one attempt to retry and prompt for the user name and password should a connection fail.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Turn off all messages for quiet execution. This option does not suppress errors or warnings.</dl>
<dl>
<dt>
<dd> &bull; &#8211;recurse, -r </p>
<p> Traverse the list of slaves to find additional master/slave connections. User this option to map a replication topology.</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-list, -l </p>
<p> Display a column list of the topology.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. If this option is used, the IO thread status of each slave is also displayed. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug. If you use -vvv, the output will contain the state of the IO and SQL threads for each slave.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> The login user must have the <code>REPLICATE SLAVE</code> and <code>REPLICATE CLIENT</code> privileges to successfully execute this utility. Specifically, the login user must have appropriate permissions to execute <code>SHOW SLAVE STATUS</code>, <code>SHOW MASTER STATUS</code>, and <code>SHOW SLAVE HOSTS</code>. </p>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> Mixing IP and hostnames is not recommended. The replication-specific utilities will attempt to compare hostnames and IP addresses as aliases for checking slave connectivity to the master. However, if your installation does not support reverse name lookup, the comparison could fail. Without the ability to do a reverse name lookup, the replication utilities could report a false negative that the slave is (not) connected to the master. </p>
<p> For example, if you setup replication using MASTER_HOST=ubuntu.net on the slave and later connect to the slave with mysqlrplcheck and have the master specified as &#8211;master=192.168.0.6 using the valid IP address for ubuntu.net, you must have the ability to do a reverse name lookup to compare the IP (192.168.0.6) and the hostname (ubuntu.net) to determine if they are the same machine. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To show the slaves for a master running on port 3311 on the local host, use the following command: </p>
<dl>
<dt>
<dd>
$ mysqlrplshow&#8211; master = root[at] localhost : 3311 &#8211;discover &#8211; slaves &#8211; login = root<br />
#master on localhost : &#8230; connected.<br />
#Finding slaves for master : localhost : 3311<br />
#Replication Topology Graph<br />
                                                                                      localhost : 3311(MASTER) |<br />
                                                                                  +&#8211; -localhost : 3310 &#8211; (SLAVE) |<br />
                                                                                  +&#8211; -localhost : 3312 &#8211; (SLAVE)
</dl>
<p> As shown in the example, you must provide valid login information for the master. </p>
<p> To show additional information about the IO thread status (to confirm if the slaves are really connected to the master) use the option <code>&#8211;verbose</code>: </p>
<dl>
<dt>
<dd>
$ mysqlrplshow&#8211; master = root[at] localhost : 3311 &#8211;discover &#8211; slaves &#8211; login = root&#8211; verbose<br />
#master on localhost : &#8230; connected.<br />
#Finding slaves for master : localhost : 3311<br />
#Replication Topology Graph<br />
                                                                                      localhost : 3311(MASTER) |<br />
                                                                                  +&#8211; -localhost : 3310 [IO:Yes, SQL:Yes] &#8211; (SLAVE) |<br />
                                                                                  +&#8211; -localhost : 3312 [IO:Yes, SQL:Yes] &#8211; (SLAVE)
</dl>
<p> To show the full replication topology of a master running on the local host, use the following command: </p>
<dl>
<dt>
<dd>
$ mysqlrplshow&#8211; master = root[at] localhost : 3311 &#8211;recurse&#8211; discover &#8211; slaves &#8211; login = root<br />
#master on localhost : &#8230; connected.<br />
#Finding slaves for master : localhost : 3311<br />
#Replication Topology Graph<br />
                                                                                                localhost : 3311(MASTER) |<br />
                                                                                            +&#8211; -localhost : 3310 &#8211; (SLAVE) |<br />
                                                                                            +&#8211; -localhost : 3312 &#8211; (SLAVE + MASTER) |<br />
                                                                                            +&#8211; -localhost : 3313 &#8211; (SLAVE)
</dl>
<p> To show the full replication topology of a master running on the local host, prompting for the user name and password for slaves that do not have the same user name and password credentials as the master, use the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlrplshow-- recurse-- prompt-- num - retries = 1 --master = root[at] localhost : 3331 --discover - slaves - login = root
                                                                                                                             Server localhost : 3331 is running on localhost.
#master on localhost : ... connected.
#Finding slaves for master : localhost : 3331
                                                                                                                         Server localhost : 3332 is running on localhost.
#master on localhost : ... FAILED.
                                                                                                                         Connection to localhost : 3332 has failed.Please enter the following information to connect to this server.User name : root
                                                                                                                                                                                                                                                    Password :
#master on localhost : ... connected.
#Finding slaves for master : localhost : 3332
    Server localhost : 3333 is running on localhost.
#master on localhost : ... FAILED.
    Connection to localhost : 3333 has failed.Please enter the following information to connect to this server.User name : root
                                                                                                                               Password :
#master on localhost : ... connected.
#Finding slaves for master : localhost : 3333
    Server localhost : 3334 is running on localhost.
#master on localhost : ... FAILED.
    Connection to localhost : 3334 has failed.Please enter the following information to connect to this server.User name : root
                                                                                                                               Password :
#master on localhost : ... connected.
#Finding slaves for master : localhost : 3334
#Replication Topology Graph
    localhost : 3331(MASTER) |
                                                                                                                         +-- -localhost : 3332 - (SLAVE) |
                                                                                                                         +-- -localhost : 3333 - (SLAVE + MASTER) |
                                                                                                                         +-- -localhost : 3334 - (SLAVE)
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
