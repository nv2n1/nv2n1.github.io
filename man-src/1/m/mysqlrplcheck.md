---
title: "mysqlrplcheck(1)"
name: "mysqlrplcheck"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlrplcheck/"
description: "mysqlrplcheck – Check Replication Prerequisitiess"
---

<h2 class="name">NAME</h2>
<p> mysqlrplcheck &#8211; Check Replication Prerequisitiess </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlrplcheck [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility checks the prerequisites for replication between a master and a slave. These checks (called tests) are designed to ensure a healthy replication setup. The utility performs the following tests: </p>
<dl>
<dt>
<dd> 1. Is the binary log enabled on the master?</dl>
<dl>
<dt>
<dd> 2. Are there binary logging exceptions (such as *_do_db or *_ignore_db settings)? If so, display them.</dl>
<dl>
<dt>
<dd> 3. Does the replication user exist on the master with the correct privileges?</dl>
<dl>
<dt>
<dd> 4. Are there server_id conflicts?</dl>
<dl>
<dt>
<dd> 5. Is the slave connected to this master? If not, display the master host and port.</dl>
<dl>
<dt>
<dd> 6. Are there conflicts between the master.info file on the slave and the values shown in <code>SHOW SLAVE STATUS</code> on the master?</dl>
<dl>
<dt>
<dd> 7. Are the InnoDB configurations compatible (plugin vs. native)?</dl>
<dl>
<dt>
<dd> 8. Are the storage engines compatible (have same on slave as master)?</dl>
<dl>
<dt>
<dd> 9. Are the lower_case_tables_names settings compatible? Warn if there are settings for lowercase/uppercase table names that can cause problems. See Bug #59240.</dl>
<dl>
<dt>
<dd> 10. Is the slave behind the master?</dl>
<p> The utility runs each test in turn unless there is a fatal error preventing further testing, such as a loss of connection to the servers. </p>
<p> Each test can complete with one of the following states: pass (the prerequisites are met), fail (the prerequisites were met but one or more errors occurred or there are exceptions to consider), or warn (the test found some unusual settings that should be examined further but may not be in error). </p>
<p> Use the <code>&#8211;verbose</code> option to see additional information such as server IDs, lower_case_table_name settings, and the contents of the master information file on the slave. </p>
<p> To see the values from the <code>SHOW SLAVE STATUS</code> statement, use the <code>&#8211;show-slave-status</code> option.<br />
OPTIONS </p>
<p> <code>mysqlrplcheck</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;master=&lt;source&gt; </p>
<p> Connection information for the master server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;master-info-file=&lt;file&gt; </p>
<p> The name of the master information file on the slave. The default is master.info read from the data directory. Note: This option requires that you run the utility on the slave and that you have appropriate read access for the file.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Turn off all messages for quiet execution. Note: Errors and warnings are not suppressed.</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-slave-status, -s </p>
<p> Display the values from <code>SHOW SLAVE STATUS</code> on the master.</dl>
<dl>
<dt>
<dd> &bull; &#8211;slave=&lt;source&gt; </p>
<p> Connection information for the slave server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;suppress </p>
<p> Suppress warning messages.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;width=&lt;number&gt; </p>
<p> Change the display width of the test report. The default is 75 characters.</dl>
<p>NOTES </p>
<p> The login user must have the appropriate permissions to execute <code>SHOW SLAVE STATUS</code>, <code>SHOW MASTER STATUS</code>, and <code>SHOW VARIABLES</code> on the appropriate servers. </p>
<p> Mixing IP and hostnames is not recommended. The replication-specific utilities will attempt to compare hostnames and IP addresses as aliases for checking slave connectivity to the master. However, if your installation does not support reverse name lookup, the comparison could fail. Without the ability to do a reverse name lookup, the replication utilities could report a false negative that the slave is (not) connected to the master. </p>
<p> For example, if you setup replication using MASTER_HOST=ubuntu.net on the slave and later connect to the slave with mysqlrplcheck and have the master specified as &#8211;master=192.168.0.6 using the valid IP address for ubuntu.net, you must have the ability to do a reverse name lookup to compare the IP (192.168.0.6) and the hostname (ubuntu.net) to determine if they are the same machine. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To check the prerequisites of a master and slave that currently are actively performing replication, use the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlrplcheck --master=root [at] host1:3310 --slave=root [at] host2:3311
#master on host1 : ... connected.
#slave on host2 : ... connected.
Test Description                                                  Status
------------------------------------------------------------------------
Checking for binary logging on master                             [pass]
Are there binlog exceptions?                                      [pass]
Replication user exists?                                          [pass]
Checking server_id values                                         [pass]
Is slave connected to master?                                     [pass]
Check master information file                                     [pass]
Checking InnoDB compatibility                                     [pass]
Checking storage engines compatibility                            [pass]
Checking lower_case_table_names settings                          [pass]
Checking slave delay (seconds behind master)                      [pass]
#... done.
</code></pre>
</dl>
<p> As shown in the example, you must provide valid login information for both the master and the slave. </p>
<p> To perform the same command but also display the contents of the master information file on the slave and the values of <code>SHOW SLAVE STATUS</code> as well as additional details, use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlrplcheck --master=root [at] host1:3310 --slave=root [at] host2:3311 \
  --show-slave-status -vv
#master on host1 : ... connected.
#slave on host2 : ... connected.
Test Description                                                  Status
------------------------------------------------------------------------
Checking for binary logging on master                              [pass]
Are there binlog exceptions?                                       [pass]
Replication user exists?                                           [pass]
Checking server_id values                                          [pass]
 master id = 10
  slave id = 11
Is slave connected to master?                                      [pass]
Check master information file                                      [pass]
#
#Master information file:
#
               Master_Log_File : clone-bin.000001
           Read_Master_Log_Pos : 482
                   Master_Host : host1
                   Master_User : rpl
               Master_Password : XXXX
                   Master_Port : 3310
                 Connect_Retry : 60
            Master_SSL_Allowed : 0
            Master_SSL_CA_File :
            Master_SSL_CA_Path :
               Master_SSL_Cert :
             Master_SSL_Cipher :
                Master_SSL_Key :
 Master_SSL_Verify_Server_Cert : 0
Checking InnoDB compatibility                                      [pass]
Checking storage engines compatibility                             [pass]
Checking lower_case_table_names settings                           [pass]
  Master lower_case_table_names: 2
   Slave lower_case_table_names: 2
Checking slave delay (seconds behind master)                       [pass]
#
#Slave status:
#
                Slave_IO_State : Waiting for master to send event
                   Master_Host : host1
                   Master_User : rpl
                   Master_Port : 3310
                 Connect_Retry : 60
               Master_Log_File : clone-bin.000001
           Read_Master_Log_Pos : 482
                Relay_Log_File : clone-relay-bin.000006
                 Relay_Log_Pos : 251
         Relay_Master_Log_File : clone-bin.000001
              Slave_IO_Running : Yes
             Slave_SQL_Running : Yes
               Replicate_Do_DB :
           Replicate_Ignore_DB :
            Replicate_Do_Table :
        Replicate_Ignore_Table :
       Replicate_Wild_Do_Table :
   Replicate_Wild_Ignore_Table :
                    Last_Errno : 0
                    Last_Error :
                  Skip_Counter : 0
           Exec_Master_Log_Pos : 482
               Relay_Log_Space : 551
               Until_Condition : None
                Until_Log_File :
                 Until_Log_Pos : 0
            Master_SSL_Allowed : No
            Master_SSL_CA_File :
            Master_SSL_CA_Path :
               Master_SSL_Cert :
             Master_SSL_Cipher :
                Master_SSL_Key :
         Seconds_Behind_Master : 0
 Master_SSL_Verify_Server_Cert : No
                 Last_IO_Errno : 0
                 Last_IO_Error :
                Last_SQL_Errno : 0
                Last_SQL_Error :
#... done.
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
