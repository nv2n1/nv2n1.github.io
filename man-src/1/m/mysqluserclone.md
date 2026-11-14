---
title: "mysqluserclone(1)"
name: "mysqluserclone"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqluserclone/"
description: "mysqluserclone – Clone Existing User to Create New User"
---

<h2 class="name">NAME</h2>
<p> mysqluserclone &#8211; Clone Existing User to Create New User </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqluserclone [</code><i>options</i><code>] </code><i>base_user</i><i>new_user</i><code>[</code><i>:password</i><code>][</code><i>@host_name</i><code>] &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility uses an existing MySQL user account on one server as a template, and clones it to create one or more new user accounts with the same privileges as the original user. The new users can be created on the original server or a different server. </p>
<p> To list users for a server, specify the <code>&#8211;list</code> option. This prints a list of the users on the source (no destination is needed). To control how to display list output, use one of the following values with the <code>&#8211;format</code> option: </p>
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
<p>OPTIONS </p>
<p> <code>mysqluserclone</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;destination=&lt;destination&gt; </p>
<p> Connection information for the destination server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;dump, -d </p>
<p> Display the <code>GRANT</code> statements to create the account rather than executing them. In this case, the utility does not connect to the destination server and no <code>&#8211;destination</code> option is needed.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;list_format&gt;, -f&lt;list_format&gt; </p>
<p> Specify the user display format. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>. This option is valid only if <code>&#8211;list</code> is given.</dl>
<dl>
<dt>
<dd> &bull; &#8211;force </p>
<p> Drop the new user account if it exists before creating the new account. Without this option, it is an error to try to create an account that already exists.</dl>
<dl>
<dt>
<dd> &bull; &#8211;include-global-privileges </p>
<p> Include privileges that match base_user@% as well as base_user [at] host.</dl>
<dl>
<dt>
<dd> &bull; &#8211;list </p>
<p> List all users on the source server. With this option, a destination server need not be specified.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Turn off all messages for quiet execution.</dl>
<dl>
<dt>
<dd> &bull; &#8211;source=&lt;source&gt; </p>
<p> Connection information for the source server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> You must provide connection parameters (user, host, password, and so forth) for an account that has the appropriate privileges to access all objects in the operation. </p>
<p> The account used to connect to the source server must have privileges to read the <code>mysql</code> database. </p>
<p> The account used to connect to the destination server must have privileges to execute <code>CREATE USER</code> (and <code>DROP USER</code> if the <code>&#8211;force</code> option is given), and privileges to execute <code>GRANT</code> for all privileges to be granted to the new accounts. </p>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To clone joe as sam and sally with passwords and logging in as root on the local machine, use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqluserclone-- source = root[at] localhost-- destination = root[at] localhost
    joe[at] localhost sam : secret1[at] localhost sally : secret2[at] localhost
#Source on localhost : ... connected.
#Destination on localhost : ... connected.
#Cloning 2 users...
#Cloning joe[at] localhost to user sam : secret1[at] localhost
#Cloning joe[at] localhost to user sally : secret2[at] localhost
#... done.
</code></pre>
</dl>
<p> The following command shows all users on the local server in the most verbose output in CSV format: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqluserclone-- source = root[at] localhost-- list-- format = csv - vvv
#Source on localhost : ... connected.
                                                                           user,
                   host, database joe, localhost, util_test rpl, localhost,
                   sally, localhost, util_test sam, localhost, util_test joe, user, util_test
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
