---
title: "rabbitmqctl(1)"
name: "rabbitmqctl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rabbitmqctl/"
description: "rabbitmqctl – command line tool for managing a RabbitMQ broker"
---

<h2 class="name">NAME</h2>
<p> rabbitmqctl &#8211; command line tool for managing a RabbitMQ broker </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>rabbitmqctl</code> [-n&nbsp;<wbr><i>node</i>] [-t&nbsp;<wbr><i>timeout</i>] [-q] {<i>command</i>} [<i>command options</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>RabbitMQ is an implementation of AMQP, the emerging standard for high performance enterprise messaging. The RabbitMQ server is a robust and scalable implementation of an AMQP broker. </p>
<p> <code>rabbitmqctl</code> is a command line tool for managing a RabbitMQ broker. It performs all actions by connecting to one of the broker&#8217;s nodes. </p>
<p> Diagnostic information is displayed if the broker was not running, could not be reached, or rejected the connection due to mismatching Erlang cookies.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Default node is &quot;rabbit [at] server&quot;, where server is the local host. On a host named &quot;server.example.com&quot;, the node name of the RabbitMQ Erlang node will usually be rabbit [at] server (unless RABBITMQ_NODENAME has been set to some non-default value at broker startup time). The output of <code>hostname -s</code> is usually the correct suffix to use after the &quot;@&quot; sign. See <a href="/docs/linux/man/1-rabbitmq-server/">rabbitmq-server</a>(1) for details of configuring the RabbitMQ broker.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Quiet output mode is selected with the &quot;-q&quot; flag. Informational messages are suppressed when quiet mode is in effect.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Operation timeout in seconds. Only applicable to &quot;list&quot; commands. Default is &quot;infinity&quot;.</dl>
</dl>
<h2>COMMANDS</h2>
<h3>Application and Cluster Management</h3>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Stops the Erlang node on which RabbitMQ is running. To restart the node follow the instructions for Running the Server in the m[blue]<code>installation guide</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If a <code>pid_file</code> is specified, also waits for the process specified there to terminate. See the description of the <code>wait</code> command below for details on this file. </p>
<p> For example: </p>
<pre>
rabbitmqctl stop
</pre>
<p> This command instructs the RabbitMQ node to terminate.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Stops the RabbitMQ application, leaving the Erlang node running. </p>
<p> This command is typically run prior to performing other management actions that require the RabbitMQ application to be stopped, e.g. <code>reset</code>. </p>
<p> For example: </p>
<pre>
rabbitmqctl stop_app
</pre>
<p> This command instructs the RabbitMQ node to stop the RabbitMQ application.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Starts the RabbitMQ application. </p>
<p> This command is typically run after performing other management actions that required the RabbitMQ application to be stopped, e.g. <code>reset</code>. </p>
<p> For example: </p>
<pre>
rabbitmqctl start_app
</pre>
<p> This command instructs the RabbitMQ node to start the RabbitMQ application.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Wait for the RabbitMQ application to start. </p>
<p> This command will wait for the RabbitMQ application to start at the node. It will wait for the pid file to be created, then for a process with a pid specified in the pid file to start, and then for the RabbitMQ application to start in that process. It will fail if the process terminates without starting the RabbitMQ application. </p>
<p> A suitable pid file is created by the <code>rabbitmq-server</code> script. By default this is located in the Mnesia directory. Modify the <code>RABBITMQ_PID_FILE</code> environment variable to change the location. </p>
<p> For example: </p>
<pre>
rabbitmqctl wait /var/run/rabbitmq/pid
</pre>
<p> This command will return when the RabbitMQ node has started up.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Return a RabbitMQ node to its virgin state. </p>
<p> Removes the node from any cluster it belongs to, removes all data from the management database, such as configured users and vhosts, and deletes all persistent messages. </p>
<p> For <code>reset</code> and <code>force_reset</code> to succeed the RabbitMQ application must have been stopped, e.g. with <code>stop_app</code>. </p>
<p> For example: </p>
<pre>
rabbitmqctl reset
</pre>
<p> This command resets the RabbitMQ node.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Forcefully return a RabbitMQ node to its virgin state. </p>
<p> The <code>force_reset</code> command differs from <code>reset</code> in that it resets the node unconditionally, regardless of the current management database state and cluster configuration. It should only be used as a last resort if the database or cluster configuration has been corrupted. </p>
<p> For <code>reset</code> and <code>force_reset</code> to succeed the RabbitMQ application must have been stopped, e.g. with <code>stop_app</code>. </p>
<p> For example: </p>
<pre>
rabbitmqctl force_reset
</pre>
<p> This command resets the RabbitMQ node.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Instruct the RabbitMQ node to rotate the log files. </p>
<p> The RabbitMQ broker appends the contents of its log files to files with names composed of the original name and the suffix, and then resumes logging to freshly created files at the original location. I.e. effectively the current log contents are moved to the end of the suffixed files. </p>
<p> When the target files do not exist they are created. When no <code>suffix</code> is specified, no rotation takes place &#8211; log files are just re-opened. </p>
<p> For example: </p>
<pre>
rabbitmqctl rotate_logs .1
</pre>
<p> This command instructs the RabbitMQ node to append the contents of the log files to files with names consisting of the original logs&#8217; names and &quot;.1&quot; suffix, e.g. rabbit [at] mymachine.log.1 and rabbit [at] mymachine-sasl.log.1. Finally, logging resumes to fresh files at the old locations.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Performs HiPE-compilation and caches resulting .beam-files in the given directory. </p>
<p> Parent directories are created if necessary. Any existing <code>.beam</code> files from the directory are automatically deleted prior to compilation. </p>
<p> To use this precompiled files, you should set <code>RABBITMQ_SERVER_CODE_PATH</code> environment variable to directory specified in <code>hipe_compile</code> invokation. </p>
<p> For example: </p>
<pre>
rabbitmqctl hipe_compile /tmp/rabbit-hipe/ebin
</pre>
<p> HiPE-compiles modules and stores them to /tmp/rabbit-hipe/ebin directory.</dl>
</dl>
<h3>Cluster management</h3>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>clusternode</p>
<dl>
<dt>
<dd> Node to cluster with.</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>If provided, the node will join the cluster as a RAM node.</dl>
<p> Instruct the node to become a member of the cluster that the specified node is in. Before clustering, the node is reset, so be careful when using this command. For this command to succeed the RabbitMQ application must have been stopped, e.g. with <code>stop_app</code>. </p>
<p> Cluster nodes can be of two types: disc or RAM. Disc nodes replicate data in RAM and on disc, thus providing redundancy in the event of node failure and recovery from global events such as power failure across all nodes. RAM nodes replicate data in RAM only (with the exception of queue contents, which can reside on disc if the queue is persistent or too big to fit in memory) and are mainly used for scalability. RAM nodes are more performant only when managing resources (e.g. adding/removing queues, exchanges, or bindings). A cluster must always have at least one disc node, and usually should have more than one. </p>
<p> The node will be a disc node by default. If you wish to create a RAM node, provide the <code>&#8211;ram</code> flag. </p>
<p> After executing the <code>cluster</code> command, whenever the RabbitMQ application is started on the current node it will attempt to connect to the nodes that were in the cluster when the node went down. </p>
<p> To leave a cluster, <code>reset</code> the node. You can also remove nodes remotely with the <code>forget_cluster_node</code> command. </p>
<p> For more details see the m[blue]<code>clustering guide</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> For example: </p>
<pre>
rabbitmqctl join_cluster hare [at] elena --ram
</pre>
<p> This command instructs the RabbitMQ node to join the cluster that <code>hare [at] elena</code> is part of, as a ram node.</dl>
</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Displays all the nodes in the cluster grouped by node type, together with the currently running nodes. </p>
<p> For example: </p>
<pre>
rabbitmqctl cluster_status
</pre>
<p> This command displays the nodes in the cluster.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Changes the type of the cluster node. The node must be stopped for this operation to succeed, and when turning a node into a RAM node the node must not be the only disc node in the cluster. </p>
<p> For example: </p>
<pre>
rabbitmqctl change_cluster_node_type disc
</pre>
<p> This command will turn a RAM node into a disc node.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Enables node removal from an offline node. This is only useful in the situation where all the nodes are offline and the last node to go down cannot be brought online, thus preventing the whole cluster from starting. It should not be used in any other circumstances since it can lead to inconsistencies.</dl>
<p> Removes a cluster node remotely. The node that is being removed must be offline, while the node we are removing from must be online, except when using the <code>&#8211;offline</code> flag. </p>
<p> When using the <code>&#8211;offline</code> flag rabbitmqctl will not attempt to connect to a node as normal; instead it will temporarily become the node in order to make the change. This is useful if the node cannot be started normally. In this case the node will become the canonical source for cluster metadata (e.g. which queues exist), even if it was not before. Therefore you should use this command on the latest node to shut down if at all possible. </p>
<p> For example: </p>
<pre><code>
rabbitmqctl - n hare[at] mcnulty forget_cluster_node rabbit[at] stringer
</code></pre>
<p> This command will remove the node <code>rabbit [at] stringer</code> from the node <code>hare [at] mcnulty</code>.</dl>
</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Supports renaming of cluster nodes in the local database. </p>
<p> This subcommand causes rabbitmqctl to temporarily become the node in order to make the change. The local cluster node must therefore be completely stopped; other nodes can be online or offline. </p>
<p> This subcommand takes an even number of arguments, in pairs representing the old and new names for nodes. You must specify the old and new names for this node and for any other nodes that are stopped and being renamed at the same time. </p>
<p> It is possible to stop all nodes and rename them all simultaneously (in which case old and new names for all nodes must be given to every node) or stop and rename nodes one at a time (in which case each node only needs to be told how its own name is changing). </p>
<p> For example: </p>
<pre><code>
rabbitmqctl rename_cluster_node rabbit[at] misshelpful rabbit[at] cordelia
</code></pre>
<p> This command will rename the node <code>rabbit [at] misshelpful</code> to the node <code>rabbit [at] cordelia</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>clusternode</p>
<dl>
<dt>
<dd> The node to consult for up to date information.</dl>
<p> Instructs an already clustered node to contact <code>clusternode</code> to cluster when waking up. This is different from <code>join_cluster</code> since it does not join any cluster &#8211; it checks that the node is already in a cluster with <code>clusternode</code>. </p>
<p> The need for this command is motivated by the fact that clusters can change while a node is offline. Consider the situation in which node A and B are clustered. A goes down, C clusters with B, and then B leaves the cluster. When A wakes up, it&#8217;ll try to contact B, but this will fail since B is not in the cluster anymore. <code>update_cluster_nodes -n A C</code> will solve this situation.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Ensure that the node will start next time, even if it was not the last to shut down. </p>
<p> Normally when you shut down a RabbitMQ cluster altogether, the first node you restart should be the last one to go down, since it may have seen things happen that other nodes did not. But sometimes that&#8217;s not possible: for instance if the entire cluster loses power then all nodes may think they were not the last to shut down. </p>
<p> In such a case you can invoke <code>rabbitmqctl force_boot</code> while the node is down. This will tell the node to unconditionally start next time you ask it to. If any changes happened to the cluster after this node shut down, they will be lost. </p>
<p> If the last node to go down is permanently lost then you should use <code>rabbitmqctl forget_cluster_node &#8211;offline</code> in preference to this command, as it will ensure that mirrored queues which were mastered on the lost node get promoted. </p>
<p> For example: </p>
<pre>
rabbitmqctl force_boot
</pre>
<p> This will force the node not to wait for other nodes next time it is started.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>queue</p>
<dl>
<dt>
<dd> The name of the queue to synchronise.</dl>
<p> Instructs a mirrored queue with unsynchronised slaves to synchronise itself. The queue will block while synchronisation takes place (all publishers to and consumers from the queue will block). The queue must be mirrored for this command to succeed. </p>
<p> Note that unsynchronised queues from which messages are being drained will become synchronised eventually. This command is primarily useful for queues which are not being drained.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>queue</p>
<dl>
<dt>
<dd> The name of the queue to cancel synchronisation for.</dl>
<p> Instructs a synchronising mirrored queue to stop synchronising itself.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>queue</p>
<dl>
<dt>
<dd> The name of the queue to purge.</dl>
<p> Purges a queue (removes all messages in it).</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Sets the cluster name. The cluster name is announced to clients on connection, and used by the federation and shovel plugins to record where a message has been. The cluster name is by default derived from the hostname of the first node in the cluster, but can be changed. </p>
<p> For example: </p>
<pre>
rabbitmqctl set_cluster_name london
</pre>
<p> This sets the cluster name to &quot;london&quot;.</dl>
</dl>
<h3>User management</h3>
<p> Note that <code>rabbitmqctl</code> manages the RabbitMQ internal user database. Users from any alternative authentication backend will not be visible to <code>rabbitmqctl</code>. </p>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user to create.</dl>
<p> password</p>
<dl>
<dt>
<dd> The password the created user will use to log in to the broker.</dl>
<p> For example: </p>
<pre>
rabbitmqctl add_user tonyg changeit
</pre>
<p> This command instructs the RabbitMQ broker to create a (non-administrative) user named <code>tonyg</code> with (initial) password <code>changeit</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user to delete.</dl>
<p> For example: </p>
<pre>
rabbitmqctl delete_user tonyg
</pre>
<p> This command instructs the RabbitMQ broker to delete the user named <code>tonyg</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user whose password is to be changed.</dl>
<p> newpassword</p>
<dl>
<dt>
<dd> The new password for the user.</dl>
<p> For example: </p>
<pre>
rabbitmqctl change_password tonyg newpass
</pre>
<p> This command instructs the RabbitMQ broker to change the password for the user named <code>tonyg</code> to <code>newpass</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user whose password is to be cleared.</dl>
<p> For example: </p>
<pre>
rabbitmqctl clear_password tonyg
</pre>
<p> This command instructs the RabbitMQ broker to clear the password for the user named <code>tonyg</code>. This user now cannot log in with a password (but may be able to through e.g. SASL EXTERNAL if configured).</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user.</dl>
<p> password</p>
<dl>
<dt>
<dd> The password of the user.</dl>
<p> For example: </p>
<pre>
rabbitmqctl authenticate_user tonyg verifyit
</pre>
<p> This command instructs the RabbitMQ broker to authenticate the user named <code>tonyg</code> with password <code>verifyit</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user whose tags are to be set.</dl>
<p> tag</p>
<dl>
<dt>
<dd> Zero, one or more tags to set. Any existing tags will be removed.</dl>
<p> For example: </p>
<pre>
rabbitmqctl set_user_tags tonyg administrator
</pre>
<p> This command instructs the RabbitMQ broker to ensure the user named <code>tonyg</code> is an administrator. This has no effect when the user logs in via AMQP, but can be used to permit the user to manage users, virtual hosts and permissions when the user logs in via some other means (for example with the management plugin). </p>
<pre>
rabbitmqctl set_user_tags tonyg
</pre>
<p> This command instructs the RabbitMQ broker to remove any tags from the user named <code>tonyg</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Lists users. Each result row will contain the user name followed by a list of the tags set for that user. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_users
</pre>
<p> This command instructs the RabbitMQ broker to list all users.</dl>
</dl>
<h3>Access control</h3>
<p> Note that <code>rabbitmqctl</code> manages the RabbitMQ internal user database. Permissions for users from any alternative authorisation backend will not be visible to <code>rabbitmqctl</code>. </p>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host entry to create.</dl>
<p> Creates a virtual host. </p>
<p> For example: </p>
<pre>
rabbitmqctl add_vhost test
</pre>
<p> This command instructs the RabbitMQ broker to create a new virtual host called <code>test</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host entry to delete.</dl>
<p> Deletes a virtual host. </p>
<p> Deleting a virtual host deletes all its exchanges, queues, bindings, user permissions, parameters and policies. </p>
<p> For example: </p>
<pre>
rabbitmqctl delete_vhost test
</pre>
<p> This command instructs the RabbitMQ broker to delete the virtual host called <code>test</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Lists virtual hosts. </p>
<p> The <code>vhostinfoitem</code> parameter is used to indicate which virtual host information items to include in the results. The column order in the results will match the order of the parameters. <code>vhostinfoitem</code> can take any value from the list that follows: </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the virtual host with non-ASCII characters escaped as in C.</dl>
<p> tracing</p>
<dl>
<dt>
<dd> Whether tracing is enabled for this virtual host.</dl>
<p> If no <code>vhostinfoitem</code>s are specified then the vhost name is displayed. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_vhosts name tracing
</pre>
<p> This command instructs the RabbitMQ broker to list all virtual hosts.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host to which to grant the user access, defaulting to <code>/</code>.</dl>
<p> user</p>
<dl>
<dt>
<dd> The name of the user to grant access to the specified virtual host.</dl>
<p> conf</p>
<dl>
<dt>
<dd> A regular expression matching resource names for which the user is granted configure permissions.</dl>
<p> write</p>
<dl>
<dt>
<dd> A regular expression matching resource names for which the user is granted write permissions.</dl>
<p> read</p>
<dl>
<dt>
<dd> A regular expression matching resource names for which the user is granted read permissions.</dl>
<p> Sets user permissions. </p>
<p> For example: </p>
<pre>
rabbitmqctl set_permissions -p /myvhost tonyg &quot;^tonyg-.*&quot; &quot;.*&quot; &quot;.*&quot;
</pre>
<p> This command instructs the RabbitMQ broker to grant the user named <code>tonyg</code> access to the virtual host called <code>/myvhost</code>, with configure permissions on all resources whose names starts with &quot;tonyg-&quot;, and write and read permissions on all resources.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host to which to deny the user access, defaulting to <code>/</code>.</dl>
<p> username</p>
<dl>
<dt>
<dd> The name of the user to deny access to the specified virtual host.</dl>
<p> Sets user permissions. </p>
<p> For example: </p>
<pre>
rabbitmqctl clear_permissions -p /myvhost tonyg
</pre>
<p> This command instructs the RabbitMQ broker to deny the user named <code>tonyg</code> access to the virtual host called <code>/myvhost</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host for which to list the users that have been granted access to it, and their permissions. Defaults to <code>/</code>.</dl>
<p> Lists permissions in a virtual host. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_permissions -p /myvhost
</pre>
<p> This command instructs the RabbitMQ broker to list all the users which have been granted access to the virtual host called <code>/myvhost</code>, and the permissions they have for operations on resources in that virtual host. Note that an empty string means no permissions granted.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>username</p>
<dl>
<dt>
<dd> The name of the user for which to list the permissions.</dl>
<p> Lists user permissions. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_user_permissions tonyg
</pre>
<p> This command instructs the RabbitMQ broker to list all the virtual hosts to which the user named <code>tonyg</code> has been granted access, and the permissions the user has for operations on resources in these virtual hosts.</dl>
</dl>
<h3>Parameter Management</h3>
<p> Certain features of RabbitMQ (such as the federation plugin) are controlled by dynamic, cluster-wide <i>parameters</i>. Each parameter consists of a component name, a name and a value, and is associated with a virtual host. The component name and name are strings, and the value is an Erlang term. Parameters can be set, cleared and listed. In general you should refer to the documentation for the feature in question to see how to set parameters. </p>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Sets a parameter. </p>
<p> component_name</p>
<dl>
<dt>
<dd> The name of the component for which the parameter is being set.</dl>
<p> name</p>
<dl>
<dt>
<dd> The name of the parameter being set.</dl>
<p> value</p>
<dl>
<dt>
<dd> The value for the parameter, as a JSON term. In most shells you are very likely to need to quote this.</dl>
<p> For example: </p>
<pre>
rabbitmqctl set_parameter federation local_username '&quot;guest&quot;'
</pre>
<p> This command sets the parameter <code>local_username</code> for the <code>federation</code> component in the default virtual host to the JSON term <code>&quot;guest&quot;</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Clears a parameter. </p>
<p> component_name</p>
<dl>
<dt>
<dd> The name of the component for which the parameter is being cleared.</dl>
<p> name</p>
<dl>
<dt>
<dd> The name of the parameter being cleared.</dl>
<p> For example: </p>
<pre>
rabbitmqctl clear_parameter federation local_username
</pre>
<p> This command clears the parameter <code>local_username</code> for the <code>federation</code> component in the default virtual host.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Lists all parameters for a virtual host. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_parameters
</pre>
<p> This command lists all parameters in the default virtual host.</dl>
</dl>
<h3>Policy Management</h3>
<p> Policies are used to control and modify the behaviour of queues and exchanges on a cluster-wide basis. Policies apply within a given vhost, and consist of a name, pattern, definition and an optional priority. Policies can be set, cleared and listed. </p>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Sets a policy. </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the policy.</dl>
<p> pattern</p>
<dl>
<dt>
<dd> The regular expression, which when matches on a given resources causes the policy to apply.</dl>
<p> definition</p>
<dl>
<dt>
<dd> The definition of the policy, as a JSON term. In most shells you are very likely to need to quote this.</dl>
<p> priority</p>
<dl>
<dt>
<dd> The priority of the policy as an integer. Higher numbers indicate greater precedence. The default is 0.</dl>
<p> apply-to</p>
<dl>
<dt>
<dd> Which types of object this policy should apply to &#8211; &quot;queues&quot;, &quot;exchanges&quot; or &quot;all&quot;. The default is &quot;all&quot;.</dl>
<p> For example: </p>
<pre>
rabbitmqctl set_policy federate-me &quot;^amq.&quot; '{&quot;federation-upstream-set&quot;:&quot;all&quot;}'
</pre>
<p> This command sets the policy <code>federate-me</code> in the default virtual host so that built-in exchanges are federated.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Clears a policy. </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the policy being cleared.</dl>
<p> For example: </p>
<pre>
rabbitmqctl clear_policy federate-me
</pre>
<p> This command clears the <code>federate-me</code> policy in the default virtual host.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Lists all policies for a virtual host. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_policies
</pre>
<p> This command lists all policies in the default virtual host.</dl>
</dl>
<h3>Server Status</h3>
<p> The server status queries interrogate the server and return a list of results with tab-delimited columns. Some queries (<code>list_queues</code>, <code>list_exchanges</code>, <code>list_bindings</code>, and <code>list_consumers</code>) accept an optional <code>vhost</code> parameter. This parameter, if present, must be specified immediately after the query. </p>
<p> The list_queues, list_exchanges and list_bindings commands accept an optional virtual host parameter for which to display results. The default value is &quot;/&quot;. </p>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Returns queue details. Queue details of the <code>/</code> virtual host are returned if the &quot;-p&quot; flag is absent. The &quot;-p&quot; flag can be used to override this default. </p>
<p> The <code>queueinfoitem</code> parameter is used to indicate which queue information items to include in the results. The column order in the results will match the order of the parameters. <code>queueinfoitem</code> can take any value from the list that follows: </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the queue with non-ASCII characters escaped as in C.</dl>
<p> durable</p>
<dl>
<dt>
<dd> Whether or not the queue survives server restarts.</dl>
<p> auto_delete</p>
<dl>
<dt>
<dd> Whether the queue will be deleted automatically when no longer used.</dl>
<p> arguments</p>
<dl>
<dt>
<dd> Queue arguments.</dl>
<p> policy</p>
<dl>
<dt>
<dd> Policy name applying to the queue.</dl>
<p> pid</p>
<dl>
<dt>
<dd> Id of the Erlang process associated with the queue.</dl>
<p> owner_pid</p>
<dl>
<dt>
<dd> Id of the Erlang process representing the connection which is the exclusive owner of the queue. Empty if the queue is non-exclusive.</dl>
<p> exclusive</p>
<dl>
<dt>
<dd> True if queue is exclusive (i.e. has owner_pid), false otherwise</dl>
<p> exclusive_consumer_pid</p>
<dl>
<dt>
<dd> Id of the Erlang process representing the channel of the exclusive consumer subscribed to this queue. Empty if there is no exclusive consumer.</dl>
<p> exclusive_consumer_tag</p>
<dl>
<dt>
<dd> Consumer tag of the exclusive consumer subscribed to this queue. Empty if there is no exclusive consumer.</dl>
<p> messages_ready</p>
<dl>
<dt>
<dd> Number of messages ready to be delivered to clients.</dl>
<p> messages_unacknowledged</p>
<dl>
<dt>
<dd> Number of messages delivered to clients but not yet acknowledged.</dl>
<p> messages</p>
<dl>
<dt>
<dd> Sum of ready and unacknowledged messages (queue depth).</dl>
<p> messages_ready_ram</p>
<dl>
<dt>
<dd> Number of messages from messages_ready which are resident in ram.</dl>
<p> messages_unacknowledged_ram</p>
<dl>
<dt>
<dd> Number of messages from messages_unacknowledged which are resident in ram.</dl>
<p> messages_ram</p>
<dl>
<dt>
<dd> Total number of messages which are resident in ram.</dl>
<p> messages_persistent</p>
<dl>
<dt>
<dd> Total number of persistent messages in the queue (will always be 0 for transient queues).</dl>
<p> message_bytes</p>
<dl>
<dt>
<dd> Sum of the size of all message bodies in the queue. This does not include the message properties (including headers) or any overhead.</dl>
<p> message_bytes_ready</p>
<dl>
<dt>
<dd> Like <code>message_bytes</code> but counting only those messages ready to be delivered to clients.</dl>
<p> message_bytes_unacknowledged</p>
<dl>
<dt>
<dd> Like <code>message_bytes</code> but counting only those messages delivered to clients but not yet acknowledged.</dl>
<p> message_bytes_ram</p>
<dl>
<dt>
<dd> Like <code>message_bytes</code> but counting only those messages which are in RAM.</dl>
<p> message_bytes_persistent</p>
<dl>
<dt>
<dd> Like <code>message_bytes</code> but counting only those messages which are persistent.</dl>
<p> head_message_timestamp</p>
<dl>
<dt>
<dd> The timestamp property of the first message in the queue, if present. Timestamps of messages only appear when they are in the paged-in state.</dl>
<p> disk_reads</p>
<dl>
<dt>
<dd> Total number of times messages have been read from disk by this queue since it started.</dl>
<p> disk_writes</p>
<dl>
<dt>
<dd> Total number of times messages have been written to disk by this queue since it started.</dl>
<p> consumers</p>
<dl>
<dt>
<dd> Number of consumers.</dl>
<p> consumer_utilisation</p>
<dl>
<dt>
<dd> Fraction of the time (between 0.0 and 1.0) that the queue is able to immediately deliver messages to consumers. This can be less than 1.0 if consumers are limited by network congestion or prefetch count.</dl>
<p> memory</p>
<dl>
<dt>
<dd> Bytes of memory consumed by the Erlang process associated with the queue, including stack, heap and internal structures.</dl>
<p> slave_pids</p>
<dl>
<dt>
<dd> If the queue is mirrored, this gives the IDs of the current slaves.</dl>
<p> synchronised_slave_pids</p>
<dl>
<dt>
<dd> If the queue is mirrored, this gives the IDs of the current slaves which are synchronised with the master &#8211; i.e. those which could take over from the master without message loss.</dl>
<p> state</p>
<dl>
<dt>
<dd> The state of the queue. Normally &#8216;running&#8217;, but may be &quot;{syncing, MsgCount}&quot; if the queue is synchronising. Queues which are located on cluster nodes that are currently down will be shown with a status of &#8216;down&#8217; (and most other <code>queueinfoitem</code>s will be unavailable).</dl>
<p> If no <code>queueinfoitem</code>s are specified then queue name and depth are displayed. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_queues -p /myvhost messages consumers
</pre>
<p> This command displays the depth and number of consumers for each queue of the virtual host named <code>/myvhost</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Returns exchange details. Exchange details of the <code>/</code> virtual host are returned if the &quot;-p&quot; flag is absent. The &quot;-p&quot; flag can be used to override this default. </p>
<p> The <code>exchangeinfoitem</code> parameter is used to indicate which exchange information items to include in the results. The column order in the results will match the order of the parameters. <code>exchangeinfoitem</code> can take any value from the list that follows: </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the exchange with non-ASCII characters escaped as in C.</dl>
<p> type</p>
<dl>
<dt>
<dd> The exchange type (such as [<code>direct</code>, <code>topic</code>, <code>headers</code>, <code>fanout</code>]).</dl>
<p> durable</p>
<dl>
<dt>
<dd> Whether or not the exchange survives server restarts.</dl>
<p> auto_delete</p>
<dl>
<dt>
<dd> Whether the exchange will be deleted automatically when no longer used.</dl>
<p> internal</p>
<dl>
<dt>
<dd> Whether the exchange is internal, i.e. cannot be directly published to by a client.</dl>
<p> arguments</p>
<dl>
<dt>
<dd> Exchange arguments.</dl>
<p> policy</p>
<dl>
<dt>
<dd> Policy name for applying to the exchange.</dl>
<p> If no <code>exchangeinfoitem</code>s are specified then exchange name and type are displayed. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_exchanges -p /myvhost name type
</pre>
<p> This command displays the name and type for each exchange of the virtual host named <code>/myvhost</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Returns binding details. By default the bindings for the <code>/</code> virtual host are returned. The &quot;-p&quot; flag can be used to override this default. </p>
<p> The <code>bindinginfoitem</code> parameter is used to indicate which binding information items to include in the results. The column order in the results will match the order of the parameters. <code>bindinginfoitem</code> can take any value from the list that follows: </p>
<p> source_name</p>
<dl>
<dt>
<dd> The name of the source of messages to which the binding is attached. With non-ASCII characters escaped as in C.</dl>
<p> source_kind</p>
<dl>
<dt>
<dd> The kind of the source of messages to which the binding is attached. Currently always exchange. With non-ASCII characters escaped as in C.</dl>
<p> destination_name</p>
<dl>
<dt>
<dd> The name of the destination of messages to which the binding is attached. With non-ASCII characters escaped as in C.</dl>
<p> destination_kind</p>
<dl>
<dt>
<dd> The kind of the destination of messages to which the binding is attached. With non-ASCII characters escaped as in C.</dl>
<p> routing_key</p>
<dl>
<dt>
<dd> The binding&#8217;s routing key, with non-ASCII characters escaped as in C.</dl>
<p> arguments</p>
<dl>
<dt>
<dd> The binding&#8217;s arguments.</dl>
<p> If no <code>bindinginfoitem</code>s are specified then all above items are displayed. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_bindings -p /myvhost exchange_name queue_name
</pre>
<p> This command displays the exchange name and queue name of the bindings in the virtual host named <code>/myvhost</code>.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Returns TCP/IP connection statistics. </p>
<p> The <code>connectioninfoitem</code> parameter is used to indicate which connection information items to include in the results. The column order in the results will match the order of the parameters. <code>connectioninfoitem</code> can take any value from the list that follows: </p>
<p> pid</p>
<dl>
<dt>
<dd> Id of the Erlang process associated with the connection.</dl>
<p> name</p>
<dl>
<dt>
<dd> Readable name for the connection.</dl>
<p> port</p>
<dl>
<dt>
<dd> Server port.</dl>
<p> host</p>
<dl>
<dt>
<dd> Server hostname obtained via reverse DNS, or its IP address if reverse DNS failed or was not enabled.</dl>
<p> peer_port</p>
<dl>
<dt>
<dd> Peer port.</dl>
<p> peer_host</p>
<dl>
<dt>
<dd> Peer hostname obtained via reverse DNS, or its IP address if reverse DNS failed or was not enabled.</dl>
<p> ssl</p>
<dl>
<dt>
<dd> Boolean indicating whether the connection is secured with SSL.</dl>
<p> ssl_protocol</p>
<dl>
<dt>
<dd> SSL protocol (e.g. tlsv1)</dl>
<p> ssl_key_exchange</p>
<dl>
<dt>
<dd> SSL key exchange algorithm (e.g. rsa)</dl>
<p> ssl_cipher</p>
<dl>
<dt>
<dd> SSL cipher algorithm (e.g. aes_256_cbc)</dl>
<p> ssl_hash</p>
<dl>
<dt>
<dd> SSL hash function (e.g. sha)</dl>
<p> peer_cert_subject</p>
<dl>
<dt>
<dd> The subject of the peer&#8217;s SSL certificate, in RFC4514 form.</dl>
<p> peer_cert_issuer</p>
<dl>
<dt>
<dd> The issuer of the peer&#8217;s SSL certificate, in RFC4514 form.</dl>
<p> peer_cert_validity</p>
<dl>
<dt>
<dd> The period for which the peer&#8217;s SSL certificate is valid.</dl>
<p> state</p>
<dl>
<dt>
<dd> Connection state (one of [<code>starting</code>, <code>tuning</code>, <code>opening</code>, <code>running</code>, <code>flow</code>, <code>blocking</code>, <code>blocked</code>, <code>closing</code>, <code>closed</code>]).</dl>
<p> channels</p>
<dl>
<dt>
<dd> Number of channels using the connection.</dl>
<p> protocol</p>
<dl>
<dt>
<dd> Version of the AMQP protocol in use (currently one of <code>{0,9,1}</code> or <code>{0,8,0}</code>). Note that if a client requests an AMQP 0-9 connection, we treat it as AMQP 0-9-1.</dl>
<p> auth_mechanism</p>
<dl>
<dt>
<dd> SASL authentication mechanism used, such as <code>PLAIN</code>.</dl>
<p> user</p>
<dl>
<dt>
<dd> Username associated with the connection.</dl>
<p> vhost</p>
<dl>
<dt>
<dd> Virtual host name with non-ASCII characters escaped as in C.</dl>
<p> timeout</p>
<dl>
<dt>
<dd> Connection timeout / negotiated heartbeat interval, in seconds.</dl>
<p> frame_max</p>
<dl>
<dt>
<dd> Maximum frame size (bytes).</dl>
<p> channel_max</p>
<dl>
<dt>
<dd> Maximum number of channels on this connection.</dl>
<p> client_properties</p>
<dl>
<dt>
<dd> Informational properties transmitted by the client during connection establishment.</dl>
<p> recv_oct</p>
<dl>
<dt>
<dd> Octets received.</dl>
<p> recv_cnt</p>
<dl>
<dt>
<dd> Packets received.</dl>
<p> send_oct</p>
<dl>
<dt>
<dd> Octets send.</dl>
<p> send_cnt</p>
<dl>
<dt>
<dd> Packets sent.</dl>
<p> send_pend</p>
<dl>
<dt>
<dd> Send queue size.</dl>
<p> connected_at</p>
<dl>
<dt>
<dd> Date and time this connection was established, as timestamp.</dl>
<p> If no <code>connectioninfoitem</code>s are specified then user, peer host, peer port, time since flow control and memory block state are displayed. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_connections send_pend port
</pre>
<p> This command displays the send queue size and server port for each connection.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Returns information on all current channels, the logical containers executing most AMQP commands. This includes channels that are part of ordinary AMQP connections, and channels created by various plug-ins and other extensions. </p>
<p> The <code>channelinfoitem</code> parameter is used to indicate which channel information items to include in the results. The column order in the results will match the order of the parameters. <code>channelinfoitem</code> can take any value from the list that follows: </p>
<p> pid</p>
<dl>
<dt>
<dd> Id of the Erlang process associated with the connection.</dl>
<p> connection</p>
<dl>
<dt>
<dd> Id of the Erlang process associated with the connection to which the channel belongs.</dl>
<p> name</p>
<dl>
<dt>
<dd> Readable name for the channel.</dl>
<p> number</p>
<dl>
<dt>
<dd> The number of the channel, which uniquely identifies it within a connection.</dl>
<p> user</p>
<dl>
<dt>
<dd> Username associated with the channel.</dl>
<p> vhost</p>
<dl>
<dt>
<dd> Virtual host in which the channel operates.</dl>
<p> transactional</p>
<dl>
<dt>
<dd> True if the channel is in transactional mode, false otherwise.</dl>
<p> confirm</p>
<dl>
<dt>
<dd> True if the channel is in confirm mode, false otherwise.</dl>
<p> consumer_count</p>
<dl>
<dt>
<dd> Number of logical AMQP consumers retrieving messages via the channel.</dl>
<p> messages_unacknowledged</p>
<dl>
<dt>
<dd> Number of messages delivered via this channel but not yet acknowledged.</dl>
<p> messages_uncommitted</p>
<dl>
<dt>
<dd> Number of messages received in an as yet uncommitted transaction.</dl>
<p> acks_uncommitted</p>
<dl>
<dt>
<dd> Number of acknowledgements received in an as yet uncommitted transaction.</dl>
<p> messages_unconfirmed</p>
<dl>
<dt>
<dd> Number of published messages not yet confirmed. On channels not in confirm mode, this remains 0.</dl>
<p> prefetch_count</p>
<dl>
<dt>
<dd> QoS prefetch limit for new consumers, 0 if unlimited.</dl>
<p> global_prefetch_count</p>
<dl>
<dt>
<dd> QoS prefetch limit for the entire channel, 0 if unlimited.</dl>
<p> If no <code>channelinfoitem</code>s are specified then pid, user, consumer_count, and messages_unacknowledged are assumed. </p>
<p> For example: </p>
<pre>
rabbitmqctl list_channels connection messages_unacknowledged
</pre>
<p> This command displays the connection process and count of unacknowledged messages for each channel.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>List consumers, i.e. subscriptions to a queue&#8217;s message stream. Each line printed shows, separated by tab characters, the name of the queue subscribed to, the id of the channel process via which the subscription was created and is managed, the consumer tag which uniquely identifies the subscription within a channel, a boolean indicating whether acknowledgements are expected for messages delivered to this consumer, an integer indicating the prefetch limit (with 0 meaning &#8216;none&#8217;), and any arguments for this consumer.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Displays broker status information such as the running applications on the current Erlang node, RabbitMQ and Erlang versions, OS name, memory and file descriptor statistics. (See the <code>cluster_status</code> command to find out which nodes are clustered and running.) </p>
<p> For example: </p>
<pre>
rabbitmqctl status
</pre>
<p> This command displays information about the RabbitMQ broker.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Health check of the RabbitMQ node. Verifies the rabbit application is running, list_queues and list_channels return, and alarms are not set. </p>
<p> For example: </p>
<pre>
rabbitmqctl node_health_check -n rabbit [at] stringer
</pre>
<p> This command performs a health check on the RabbitMQ node.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Display the name and value of each variable in the application environment for each running application.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Generate a server status report containing a concatenation of all server status information for support purposes. The output should be redirected to a file when accompanying a support request. </p>
<p> For example: </p>
<pre>
rabbitmqctl report &gt; server_report.txt
</pre>
<p> This command creates a server report which may be attached to a support request email.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>Evaluate an arbitrary Erlang expression. </p>
<p> For example: </p>
<pre>
rabbitmqctl eval 'node().'
</pre>
<p> This command returns the name of the node to which rabbitmqctl has connected.</dl>
</dl>
<h3>Miscellaneous</h3>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>connectionpid</p>
<dl>
<dt>
<dd> Id of the Erlang process associated with the connection to close.</dl>
<p> explanation</p>
<dl>
<dt>
<dd> Explanation string.</dl>
<p> Instruct the broker to close the connection associated with the Erlang process id <code>connectionpid</code> (see also the <code>list_connections</code> command), passing the <code>explanation</code> string to the connected client as part of the AMQP connection shutdown protocol. </p>
<p> For example: </p>
<pre>
rabbitmqctl close_connection &quot;&lt;rabbit [at] tanto.4262.0&gt;&quot; &quot;go away&quot;
</pre>
<p> This command instructs the RabbitMQ broker to close the connection associated with the Erlang process id <code>&lt;rabbit [at] tanto.4262.0&gt;</code>, passing the explanation <code>go away</code> to the connected client.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host for which to start tracing.</dl>
<p> Starts tracing. Note that the trace state is not persistent; it will revert to being off if the server is restarted.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>vhost</p>
<dl>
<dt>
<dd> The name of the virtual host for which to stop tracing.</dl>
<p> Stops tracing.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>fraction</p>
<dl>
<dt>
<dd> The new memory threshold fraction at which flow control is triggered, as a floating point number greater than or equal to 0.</dl>
</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>memory_limit</p>
<dl>
<dt>
<dd> The new memory limit at which flow control is triggered, expressed in bytes as an integer number greater than or equal to 0 or as a string with memory units (e.g. 512M or 1G). Available units are: k, kiB: kibibytes (2^10 bytes) M, MiB: mebibytes (2^20) G, GiB: gibibytes (2^30) kB: kilobytes (10^3) MB: megabytes (10^6) GB: gigabytes (10^9)</dl>
</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>disk_limit</p>
<dl>
<dt>
<dd> Lower bound limit as an integer in bytes or a string with memory units (see vm_memory_high_watermark), e.g. 512M or 1G. Once free disk space reaches the limit, a disk alarm will be set.</dl>
</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>fraction</p>
<dl>
<dt>
<dd> Limit relative to the total amount available RAM as a non-negative floating point number. Values lower than 1.0 can be dangerous and should be used carefully.</dl>
</dl>
</dl>
<h2>AUTHOR</h2>
<p> <code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> installation guide</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.rabbitmq.com/install.html">http://www.rabbitmq.com/install.html</a></dl>
<dt> 2.</p>
<dd> clustering guide</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.rabbitmq.com/clustering.html">http://www.rabbitmq.com/clustering.html</a></dl>
</dl>
<h2>Index</h2>
