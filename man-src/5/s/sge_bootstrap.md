---
title: "sge_bootstrap(5)"
name: "sge_bootstrap"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_bootstrap/"
description: "bootstrap – Grid Engine bootstrap file"
---

<p>bootstrap &#8211; Grid Engine bootstrap file</p>
<h2>Description</h2>
<p><i>bootstrap</i> contains parameters that are needed for the startup of Grid Engine components. It is created during the ge_qmaster installation. Modifying <i>bootstrap</i> in a running system is not supported. </p>
<h2>Format</h2>
<p>The paragraphs that follow provide brief descriptions of the individual parameters that compose the bootstrap configuration for a Grid Engine cluster:</p>
<h3><code>admin_user</code></h3>
<p>Administrative user account used by Grid Engine for all internal file handling (status spooling, message logging, etc.). Can be used in cases where the root account does not have the corresponding file access permissions (e.g. on a shared file system without global root read/write access). </p>
<p> Being a parameter set at installation time changing <code>admin_user</code> in a running system is not supported. Changing it manually on a shut-down cluster is possible, but if access to the Grid Engine spooling area is interrupted, this will result in unpredictable behavior. </p>
<p> The <code>admin_user</code> parameter has no default value, but instead it is defined during the master installation procedure.</p>
<h3><code>default_domain</code></h3>
<p>Only needed if your Grid Engine cluster covers hosts belonging to more than a single DNS domain. In this case it can be used if your hostname resolving yields both qualified and unqualified hostnames for the hosts in one of the DNS domains. The value of <code>default_domain</code> is appended to the unqualified hostname to define a fully qualified hostname. The <code>default_domain</code> parameter will have no effect if <code>ignore_fqdn</code> is set to &quot;true&quot;. </p>
<p> Being a parameter set at installation time changing <code>default_domain</code> in a running system is not supported. The default for <code>default_domain</code> is &quot;none&quot;, in which case it will not be used.</p>
<h3><code>ignore_fqdn</code></h3>
<p>Ignore fully qualified domain name component of hostnames. Should be set if all hosts belonging to a Grid Engine cluster are part of a single DNS domain. It is switched on if set to either &quot;true&quot; or &quot;1&quot;. Switching it on may solve problems with load reports due to different hostname resolutions across the cluster. </p>
<p> Being a parameter set at installation time changing <code>ignore_fqdn</code> in a running system is not supported. The default for <code>ignore_fqdn</code> is &quot;true&quot;.</p>
<h3><code>spooling_method</code></h3>
<p>Defines how writes its configuration and the status information of a running cluster. </p>
<p> The available spooling methods are <i>berkeleydb</i> and <i>classic</i>.</p>
<h3><code>spooling_lib</code></h3>
<p>The name of a shared library containing the <code>spooling_method</code> to be loaded at initialization time. The extension characterizing a shared library (.so, .sl, .dylib etc.) is not contained in <code>spooling_lib</code>. </p>
<p> If <code>spooling_method</code> was set to <i>berkeleydb</i> during installation, <code>spooling_lib</code> is set to <i>libspoolb</i>, if <i>classic</i> was chosen as <code>spooling_method</code>, <code>spooling_lib</code> is set to <i>libspoolc</i>. </p>
<p> Not all operating systems allow the dynamic loading of libraries. On these platforms a certain spooling method (default: berkeleydb) is compiled into the binaries and the parameter <code>spooling_lib</code> will be ignored.</p>
<h3><code>spooling_params</code></h3>
<p>Defines parameters to the chosen spooling method. </p>
<p> Parameters that are needed to initialize the spooling framework, e.g. to open database files or to connect to a certain database server. </p>
<p> The spooling parameters value for spooling method <i>berkeleydb</i> is [rpc_server:]database directory, e.g. /sge_local/default/spool/qmaster/spooldb for spooling to a local filesystem, or myhost:sge for spooling over a Berkeley DB RPC server. </p>
<p> For spooling method <i>classic</i> the spooling parameters take the form &lt;common_dir&gt;;&lt;qmaster spool dir&gt;, e.g. /sge/default/common;/sge/default/spool/qmaster</p>
<h3><code>binary_path</code></h3>
<p>The directory path where the Grid Engine binaries reside. It is used within Grid Engine components to locate and startup other Grid Engine programs. </p>
<p> The path name given here is searched for binaries as well as any directory below with a directory name equal to the current operating system architecture. Therefore, /usr/GE/bin will work for all architectures, if the corresponding binaries are located in subdirectories named aix43, cray, lx24-x86, hp11, irix65, tru64, sol-sparc, etc. </p>
<p> The default location for the binary path is &lt;ge_root&gt;/bin</p>
<h3><code>qmaster_spool_dir</code></h3>
<p>The location where the master spool directory resides. Only the and need to have access to this directory. The master spool directory &#8211; in particular the job_scripts directory and the messages log file &#8211; may become quite large depending on the size of the cluster and the number of jobs. Be sure to allocate enough disk space and regularly clean off the log files, e.g. via a job. </p>
<p> Being a parameter set at installation time changing <code>qmaster_spool_dir</code> in a running system is not supported. </p>
<p> The default location for the master spool directory is &lt;ge_root&gt;/&lt;cell&gt;/spool/qmaster.</p>
<h3><code>security_mode</code></h3>
<p>The security mode defines the set of security features the installed cluster is using. </p>
<p> Possible security mode settings are none, afs, dce, kerberos, csp. (no additional security, AFS, DCE, KERBEROS, CSP security model).</p>
<h3><code>listener_threads</code></h3>
<p>The number of listener threads (defaults set by installation).</p>
<h3><code>worker_threads</code></h3>
<p>The number of worker threads (defaults set by installation).</p>
<h3><code>scheduler_threads</code></h3>
<p>The number of scheduler threads (allowed: 0-1, default set by installation: 1, off: 0). (see -kt/-at option)</p>
<h3><code>jvm_threads</code></h3>
<p>The number of jvm threads (allowed: 0-1, default set by installation, off: 0).</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
