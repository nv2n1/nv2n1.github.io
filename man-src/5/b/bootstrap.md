---
title: "bootstrap(5)"
name: "bootstrap"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bootstrap/"
description: "bootstrap – xxQS_NAMExx bootstrap file"
---

<p>bootstrap &#8211; xxQS_NAMExx bootstrap file</p>
<h2>Description</h2>
<p><i>bootstrap</i> contains parameters that are needed for the startup of xxQS_NAMExx components. It is created during the xxqs_name_sxx_qmaster installation. Modifying <i>bootstrap</i> in a running system is not supported. </p>
<h2>Format</h2>
<p>The paragraphs that follow provide brief descriptions of the individual parameters that comprise the bootstrap configuration for a xxQS_NAMExx cluster:</p>
<h3><code>admin_user</code></h3>
<p>Administrative user account used by xxQS_NAMExx for all internal file handling (status spooling, message logging, etc.). Can be used in cases where the root account does not have the corresponding file access permissions (e.g. on a shared file system without global root read/write access). </p>
<p> As a parameter set at installation time, changing <code>admin_user</code> in a running system is not supported. Changing it manually on a shut-down cluster is possible, but if access to the xxQS_NAMExx spooling area is interrupted, this will result in unpredictable behavior. </p>
<p> The <code>admin_user</code> parameter has no default value, but instead it is defined during the master installation procedure.</p>
<h3><code>default_domain</code></h3>
<p>Only needed if your xxQS_NAMExx cluster covers hosts belonging to more than a single DNS domain. In this case it can be used if your hostname resolving yields both qualified and unqualified hostnames for the hosts in one of the DNS domains. The value of <code>default_domain</code> is appended to the unqualified hostname to define a fully qualified hostname. The <code>default_domain</code> parameter will have no effect if <code>ignore_fqdn</code> is set to &quot;true&quot;. </p>
<p> As a parameter set at installation time, changing <code>default_domain</code> in a running system is not supported. The default for <code>default_domain</code> is &quot;none&quot;, in which case it will not be used.</p>
<h3><code>ignore_fqdn</code></h3>
<p>Ignore fully qualified domain name component of hostnames. Should be set if all hosts belonging to a xxQS_NAMExx cluster are part of a single DNS domain. It is switched on if set to either &quot;true&quot; or &quot;1&quot;. Switching it on may solve problems with load reports due to different hostname resolutions across the cluster. </p>
<p> As a parameter set at installation time, changing <code>ignore_fqdn</code> in a running system is not supported. The default for <code>ignore_fqdn</code> is &quot;true&quot;.</p>
<h3><code>spooling_method</code></h3>
<p>Defines how writes its configuration and the status information of a running cluster. </p>
<p> The available spooling methods are <i>berkeleydb</i> and <i>classic</i>.</p>
<h3><code>spooling_lib</code></h3>
<p>The name of a shared library containing the <code>spooling_method</code> to be loaded at initialization time. The extension characterizing a shared library (.so, .sl, .dylib etc.) is not contained in <code>spooling_lib</code>. </p>
<p> If <code>spooling_method</code> was set to <i>berkeleydb</i> during installation, <code>spooling_lib</code> is set to <i>libspoolb</i>, and if <i>classic</i> was chosen as <code>spooling_method</code>, <code>spooling_lib</code> is set to <i>libspoolc</i>. </p>
<p> Not all operating systems allow the dynamic loading of libraries. On these platforms a certain spooling method (default: berkeleydb) is compiled into the binaries and the parameter <code>spooling_lib</code> will be ignored.</p>
<h3><code>spooling_params</code></h3>
<p>Defines parameters of the chosen spooling method that are needed to initialize the spooling framework, e.g. to open database files. </p>
<p> The spooling parameters value for spooling method <i>berkeleydb</i> is </p>
<p>&nbsp;<wbr>&nbsp;[<i>rpc_server</i><code>:</code>]<i>database directory</i>[<code>;</code><i>options</i>]<br />
 e.g. &quot;/opt/sge/default/spool/qmaster/spooldb&quot; for spooling to a local filesystem, or &quot;myhost:sge&quot; for spooling over a Berkeley DB RPC server. </p>
<p> <i>rpc_server</i> is obsolete since recent BDB versions don&#8217;t support RPC and support has been removed from xxQS_NAMExx; it must be replaced if it occurs in an old configuration before an upgrade. <i>database directory</i> is the directory containing the spool files, and <i>options</i> is a list of options for the database. Currently the only valid value for <i>options</i> is <code>private</code>, which means to open the database with the DB_PRIVATE flag to specify that it is only accessed by a single process. This allows the <i>database directory</i> to be on an NFSv3 filesystem (as opposed to an NFSv4 one, which is otherwise necessary), but it is unsafe to access it with any other program. In particular, this means that the backup script (inst_sge -bup), similar scripts using the DB utilities, <i>spooledit</i> etc., must not be used while qmaster is running with berkeleydb spooling. </p>
<p> For spooling method <i>classic</i> the spooling parameters take the form <i>common_dir</i><code>;</code><i>qmaster spool dir</i>, e.g. /sge/default/common;/sge/default/spool/qmaster.</p>
<h3><code>binary_path</code></h3>
<p>The directory path where the xxQS_NAMExx binaries reside. It is used within xxQS_NAMExx components to locate and startup other xxQS_NAMExx programs. </p>
<p> The path name given here is searched for binaries as well as any directory below with a directory name equal to the current operating system architecture. Therefore, /usr/xxQS_NAME_Sxx/bin will work for all architectures, if the corresponding binaries are located in subdirectories named aix51, lx-amd64, lx-x86, hp11, hp11-64, sol-amd64, sol-sparc etc. </p>
<p> The default location for the binary path is &lt;xxqs_name_sxx_root&gt;/bin</p>
<h3><code>qmaster_spool_dir</code></h3>
<p>The location where the master spool directory resides. Only the and need to have access to this directory. The master spool directory &#8211; in particular the job_scripts directory and the messages log file &#8211; may become quite large, depending on the size of the cluster and the number of jobs. Be sure to allocate enough disk space and regularly clean off the log files, e.g. via a <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8) job. </p>
<p> As a parameter set at installation time, changing <code>qmaster_spool_dir</code> in a running system is not supported. </p>
<p> The default location for the master spool directory is &lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/spool/qmaster.</p>
<h3><code>security_mode</code></h3>
<p>The security mode defines the set of security features the installed cluster is using, as a comma-separated list. </p>
<p> Possible security mode settings are &quot;none&quot;, &quot;afs&quot;, &quot;dce&quot;, &quot;kerberos&quot;, &quot;csp&quot;, &quot;munge&quot; (no additional security, AFS, DCE/GSSAPI, Kerberos/GSSAPI, X.509 certificate-based security, and MUNGE authentication &lt;URL: <a rel="nofollow" href="http://dun.github.io/munge/">http://dun.github.io/munge/</a> &gt;). Their availability depends on how xxQS_NAMExx was built/installed. </p>
<p> The &quot;dce&quot; and &quot;kerberos&quot; methods are nearly equivalent, calling the GSSAPI security modules in the same way, whether they were built for Kerberos/GSSAPI or DCE/GSSAPI, except that &quot;dce&quot; runs the program <i>$SGE_ROOT/utilbin/$ARCH/starter_cred</i> as a wrapper for the shepherd unless <code>NO_SECURITY</code> is specified in <code>execd_params</code> in </p>
<p> Only the CSP and MUNGE methods are currently properly functional and safe (from the point of view of not exposing credentials generally). Both provide user authentication, preventing impersonation of other users. CSP requires certificates to be generated for each user and available on each host which the user can access; it is appropriate for a loosely coupled system, e.g. including desktop systems, particularly as it protects the communication stream as well as providing authentication. MUNGE is appropriate in the security domain of a tightly coupled system, such as a normal cluster, and allows operation with <code>enforce_user=auto</code> (see it requires the <i>munged</i> daemon to be running on each host, with a shared secret and doesn&#8217;t encrypt the communication. </p>
<p> <code>NB.</code> Do not use AFS security without some means of user authentication, otherwise it is possible to submit jobs as another user and steal their credential from a job running on the same node.</p>
<h3><code>listener_threads</code></h3>
<p>The number of listener threads (defaults set by installation). Increasing this and/or <code>worker_threads</code> (below) to use additional cores/hardware threads on the master host may improve performance in demanding cases.</p>
<h3><code>worker_threads</code></h3>
<p>The number of qmaster worker threads (defaults set by installation).</p>
<h3><code>scheduler_threads</code></h3>
<p>The number of qmaster scheduler threads (allowed: 0-1, default set by installation: 1, off: 0; see -kt/-at option).</p>
<h3><code>jvm_threads</code></h3>
<p>The number of JVM threads (allowed: 0-1, default set by installation, off: 0).</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
