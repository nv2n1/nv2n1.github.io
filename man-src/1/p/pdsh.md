---
title: "pdsh(1)"
name: "pdsh"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdsh/"
description: "pdsh – issue commands to groups of hosts in parallel"
---

<h2 class="name">NAME</h2>
<p> pdsh &#8211; issue commands to groups of hosts in parallel</p>
<h2>SYNOPSIS</h2>
<p> <code>pdsh</code> [<i>options</i>]&#8230; command </p>
<h2>DESCRIPTION</h2>
<p> <code>pdsh</code> is a variant of the <a href="/docs/linux/man/1-rsh/">rsh</a>(1) command. Unlike <a href="/docs/linux/man/1-rsh/">rsh</a>(1), which runs commands on a single remote host, <code>pdsh</code> can run multiple remote commands in parallel. <code>pdsh</code> uses a &quot;sliding window&quot; (or <i>fanout</i>) of threads to conserve resources on the initiating host while allowing some connections to time out. </p>
<p> When <code>pdsh</code> receives SIGINT (ctrl-C), it lists the status of current threads. A second SIGINT within one second terminates the program. Pending threads may be canceled by issuing ctrl-Z within one second of ctrl-C. Pending threads are those that have not yet been initiated, or are still in the process of connecting to the remote host. </p>
<p> If a remote command is not specified on the command line, <code>pdsh</code> runs interactively, prompting for commands and executing them when terminated with a carriage return. In interactive mode, target nodes that time out on the first command are not contacted for subsequent commands, and commands prefixed with an exclamation point will be executed on the local system. </p>
<p> The core functionality of <code>pdsh</code> may be supplemented by dynamically loadable modules. The modules may provide a new connection protocol (replacing the standard <a href="/docs/linux/man/3-rcmd/">rcmd</a>(3) protocol used by <a href="/docs/linux/man/1-rsh/">rsh</a>(1)), filtering options (e.g. removing hosts that are &quot;down&quot; from the target list), and/or host selection options (e.g., <i>-a</i> selects all hosts from a configuration file.). By default, <code>pdsh</code> must have at least one &quot;rcmd&quot; module loaded. See the <code>RCMD MODULES</code> section for more information. </p>
<h2>RCMD MODULES</h2>
<p> The method by which <code>pdsh</code> runs commands on remote hosts may be selected at runtime using the <i>-R</i> option (See <i>OPTIONS</i> below). This functionality is ultimately implemented via dynamically loadable modules, and so the list of available options may be different from installation to installation. A list of currently available rcmd modules is printed when using any of the <i>-h</i>, <i>-V</i>, or <i>-L</i> options. The default rcmd module will also be displayed with the <i>-h</i> and <i>-V</i> options. </p>
<p> A list of <i>rcmd</i> modules currently distributed with <code>pdsh</code> follows.</p>
<dl>
<dt>rsh</p>
<dd> Uses an internal, thread-safe implementation of BSD <a href="/docs/linux/man/3-rcmd/">rcmd</a>(3) to run commands using the standard <a href="/docs/linux/man/1-rsh/">rsh</a>(1) protocol.</p>
<dt>exec</p>
<dd> Executes an arbitrary command for each target host. The first of the <code>pdsh</code> remote arguments is the local command to execute, followed by any further arguments. Some simple parameters are substitued on the command line, including <i>%h</i> for the target hostname, <i>%u</i> for the remote username, and <i>%n</i> for the remote rank [0-n] (To get a literal <i>%</i> use <i>%%</i>). For example, the following would duplicate using the <code>ssh</code> module to run <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1) across the hosts foo[0-10]: </p>
<pre>
   pdsh -R exec -w foo[0-10] ssh -x -l %u %h hostname
</pre>
<p> and this command line would run <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) in parallel across the files console.foo[0-10]: </p>
<pre>
   pdsh -R exec -w foo[0-10] grep BUG console.%h
</pre>
<dt>ssh</p>
<dd> Uses a variant of <a href="/docs/linux/man/3-popen/">popen</a>(3) to run multiple copies of the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command.</p>
<dt>mrsh</p>
<dd> This module uses the <a href="/docs/linux/man/1-mrsh/">mrsh</a>(1) protocol to execute jobs on remote hosts. The mrsh protocol uses a credential based authentication, forgoing the need to allocate reserved ports. In other aspects, it acts just like rsh. Remote nodes must be running <a href="/docs/linux/man/8-mrshd/">mrshd</a>(8) in order for the mrsh module to work.</p>
<dt>qsh</p>
<dd> Allows <code>pdsh</code> to execute MPI jobs over QsNet. Qshell propagates the current working directory, pdsh environment, and Elan capabilities to the remote process. The following environment variable are also appended to the environment: RMS_RANK, RMS_NODEID, RMS_PROCID, RMS_NNODES, and RMS_NPROCS. Since <code>pdsh</code> needs to run setuid root for qshell support, qshell does not directly support propagation of LD_LIBRARY_PATH and LD_PREOPEN. Instead the QSHELL_REMOTE_LD_LIBRARY_PATH and QSHELL_REMOTE_LD_PREOPEN environment variables will may be used and will be remapped to LD_LIBRARY_PATH and LD_PREOPEN by the qshell daemon if set.</p>
<dt>mqsh</p>
<dd> Similar to qshell, but uses the mrsh protocol instead of the rsh protocol.</p>
<dt>krb4</p>
<dd> The krb4 module allows users to execute remote commands after authenticating with kerberos. Of course, the remote rshd daemons must be kerberized.</p>
<dt>xcpu</p>
<dd> The xcpu module uses the xcpu service to execute remote commands. </p>
</dl>
<h2>OPTIONS</h2>
<p> The list of available options is determined at runtime by supplementing the list of standard <code>pdsh</code> options with any options provided by loaded <i>rcmd</i> and <i>misc</i> modules. In some cases, options provided by modules may conflict with each other. In these cases, the modules are incompatible and the first module loaded wins. </p>
<h2>Standard target nodelist options</h2>
<dl>
<dt><code>-w</code> <i>TARGETS,&#8230;</i></p>
<dd> Target and or filter the specified list of hosts. Do not use with any other node selection options (e.g. <i>-a</i>, <i>-g</i>, if they are available). No spaces are allowed in the comma-separated list. Arguments in the <i>TARGETS</i> list may include normal host names, a range of hosts in hostlist format (See <code>HOSTLIST EXPRESSIONS</code>), or a single `-&#8216; character to read the list of hosts on stdin. </p>
<p> If a host or hostlist is preceded by a `-&#8216; character, this causes those hosts to be explicitly excluded. If the argument is preceded by a single `^&#8217; character, it is taken to be the path to file containing a list of hosts, one per line. If the item begins with a `/&#8217; character, it is taken as a regular expression on which to filter the list of hosts (a regex argument may also be optionally trailed by another &#8216;/&#8217;, e.g. /node.*/). A regex or file name argument may also be preceeded by a minus `-&#8216; to exclude instead of include thoses hosts. </p>
<p> A list of hosts may also be preceded by &quot;user@&quot; to specify a remote username other than the default, or &quot;rcmd_type:&quot; to specify an alternate rcmd connection type for these hosts. When used together, the rcmd type must be specified first, e.g. &quot;ssh:user1 [at] host0&quot; would use ssh to connect to host0 as user &quot;user1.&quot; </p>
<dt><i></i><code>-x</code> <i>host,host,&#8230;</i></p>
<dd> Exclude the specified hosts. May be specified in conjunction with other target node list options such as <i>-a</i> and <i>-g</i> (when available). Hostlists may also be specified to the <i>-x</i> option (see the <code>HOSTLIST EXPRESSIONS</code> section below). Arguments to <i>-x</i> may also be preceeded by the filename (`^&#8217;) and regex (&#8216;/&#8217;) characters as described above, in which case the resulting hosts are excluded as if they had been given to <code>-w</code> and preceeded with the minus `-&#8216; character. </p>
</dl>
<h2>Standard pdsh options</h2>
<dl>
<dt><i>-S</i></p>
<dd> Return the largest of the remote command return values.</p>
<dt><i>-h</i></p>
<dd> Output usage menu and quit. A list of available rcmd modules will also be printed at the end of the usage message.</p>
<dt><i>-s</i></p>
<dd> Only on AIX, separate remote command stderr and stdout into two sockets.</p>
<dt><i>-q</i></p>
<dd> List option values and the target nodelist and exit without action.</p>
<dt><i>-b</i></p>
<dd> Disable ctrl-C status feature so that a single ctrl-C kills parallel job. (Batch Mode)</p>
<dt><i>-l user</i></p>
<dd> This option may be used to run remote commands as another user, subject to authorization. For BSD rcmd, this means the invoking user and system must be listed in the user&#8217;s .rhosts file (even for root).</p>
<dt><i>-t seconds</i></p>
<dd> Set the connect timeout. Default is 10 seconds.</p>
<dt><i>-u seconds</i></p>
<dd> Set a limit on the amount of time a remote command is allowed to execute. Default is no limit. See note in LIMITATIONS if using <i>-u</i> with ssh.</p>
<dt><i>-f number</i></p>
<dd> Set the maximum number of simultaneous remote commands to <i>number</i>. The default is 32.</p>
<dt><i>-R name</i></p>
<dd> Set rcmd module to <i>name</i>. This option may also be set via the PDSH_RCMD_TYPE environment variable. A list of available rcmd modules may be obtained via the <i>-h</i>, <i>-V</i>, or <i>-L</i> options. The default will be listed with <i>-h</i> or <i>-V.</p>
<dt>-M name,&#8230;</i></p>
<dd> When multiple <code>misc</code> modules provide the same options to <code>pdsh</code>, the first module initialized &quot;wins&quot; and subsequent modules are not loaded. The <i>-M</i> option allows a list of modules to be specified that will be force-initialized before all others, in-effect ensuring that they load without conflict (unless they conflict with eachother). This option may also be set via the PDSH_MISC_MODULES environment variable.</p>
<dt><i>-L</i></p>
<dd> List info on all loaded <code>pdsh</code> modules and quit.</p>
<dt><i>-N</i></p>
<dd> Disable hostname: prefix on lines of output.</p>
<dt><i>-d</i></p>
<dd> Include more complete thread status when SIGINT is received, and display connect and command time statistics on stderr when done.</p>
<dt><i>-V</i></p>
<dd> Output <code>pdsh</code> version information, along with list of currently loaded modules, and exit. </p>
</dl>
<h2>qsh/mqsh module options</h2>
<dl>
<dt><i>-n tasks_per_node</i></p>
<dd> Set the number of tasks spawned per node. Default is 1.</p>
<dt><i>-m block | cyclic</i></p>
<dd> Set block versus cyclic allocation of processes to nodes. Default is block.</p>
<dt><i>-r railmask</i></p>
<dd> Set the rail bitmask for a job on a multirail system. The default railmask is 1, which corresponds to rail 0 only. Each bit set in the argument to <i>-r</i> corresponds to a rail on the system, so a value of 2 would correspond to rail 1 only, and 3 would indicate to use both rail 1 and rail 0. </p>
</dl>
<h2>machines module options</h2>
<dl>
<dt><i>-a</i></p>
<dd> Target all nodes from machines file. </p>
</dl>
<h2>genders module options</h2>
<p> In addition to the genders options presented below, the genders attribute pdsh_rcmd_type may also be used in the genders database to specify an alternate rcmd connect type than the pdsh default for hosts with this attribute. For example, the following line in the genders file </p>
<pre>
  host0 pdsh_rcmd_type=ssh
</pre>
<p> would cause <code>pdsh</code> to use ssh to connect to host0, even if rsh were the default. This can be overridden on the commandline with the &quot;rcmd_type:host0&quot; syntax. </p>
<dl>
<dt><i>-A</i></p>
<dd> Target all nodes in genders database. The <i>-A</i> option will target every host listed in genders &#8212; if you want to omit some hosts by default, see the <i>-a</i> option below.</p>
<dt><i>-a</i></p>
<dd> Target all nodes in genders database except those with the &quot;pdsh_all_skip&quot; attribute. This is shorthand for running &quot;pdsh -A -X pdsh_all_skip &#8230;&quot;</p>
<dt><i>-g attr[=val][,attr[=val],&#8230;]</i></p>
<dd> Target nodes that match any of the specified genders attributes (with optional values). Conflicts with the <i>-a</i> option. If used in combination with other node selection options like <i>-w</i>, the <i>-g</i> option will select from the supplied node list, instead of from the genders file as a whole. Otherwise, This option targets the alternate hostnames in the genders database by default. The <i>-i</i> option provided by the genders module may be used to translate these to the canonical genders hostnames. If the installed version of genders supports it, attributes supplied to <i>-g</i> may also take the form of genders <code>queries</code>. Genders <code>queries</code> will query the genders database for the union, intersection, difference, or complement of genders attributes and values. The set operation union is represented by two pipe symbols (&#8216;||&#8217;), intersection by two ampersand symbols (&#8216;&amp;&amp;&#8217;), difference by two minus symbols (&#8216;&#8211;&#8216;), and complement by a tilde (&#8216;~&#8217;). Parentheses may be used to change the order of operations. See the <a href="/docs/linux/man/1-nodeattr/">nodeattr</a>(1) manpage for examples of genders <code>queries</code>.</p>
<dt><i>-X attr[=val][,attr[=val],&#8230;]</i></p>
<dd> Exclude nodes that match any of the specified genders attributes (optionally with values). This option may be used in combination with any other of the node selection options (e.g. <i>-w</i>, <i>-g</i>, <i>-a</i>, <i>-X</i> may also take the form of genders <code>queries</code>. Please see documentation for the genders <i>-g</i> option for more information about genders <code>queries</code>.</p>
<dt><i>-i</i></p>
<dd> Request translation between canonical and alternate hostnames.</p>
<dt><i>-F filename</i></p>
<dd> Read genders information from <i>filename</i> instead of the system default genders file. If <i>filename</i> doesn&#8217;t specify an absolute path then it is taken to be relative to the directory specified by the <i>PDSH_GENDERS_DIR</i> environment variable (/etc by default). An alternate genders file may also be specified via the <i>PDSH_GENDERS_FILE</i> environment variable. </p>
</dl>
<h2>nodeupdown module options</h2>
<dl>
<dt><i>-v</i></p>
<dd> Eliminate target nodes that are considered &quot;down&quot; by libnodeupdown. </p>
</dl>
<h2>slurm module options</h2>
<p> The <code>slurm</code><i> module allows </i><code>pdsh</code> to target nodes based on currently running SLURM jobs. The <code>slurm</code> module is typically called after all other node selection options have been processed, and if no nodes have been selected, the module will attempt to read a running jobid from the SLURM_JOBID environment variable (which is set when running under a SLURM allocation). If SLURM_JOBID references an invalid job, it will be silently ignored.</p>
<dl>
<dt><i>-j jobid[,jobid,&#8230;]</i></p>
<dd> Target list of nodes allocated to the SLURM job <i>jobid</i>. This option may be used multiple times to target multiple SLURM jobs. The special argument &quot;all&quot; can be used to target all nodes running SLURM jobs, e.g. <i>-j all</i>.</p>
<dt><i>-P partition[,partition,&#8230;]</i></p>
<dd> Target list of nodes containing in the SLURM partition <i>partition</i>. This option may be used multiple times to target multiple SLURM partitions and/or partitions may be given in a comma-delimited list. </p>
</dl>
<h2>torque module options</h2>
<p> The <code>torque</code><i> module allows </i><code>pdsh</code> to target nodes based on currently running Torque/PBS jobs. Similar to the slurm module, the <code>torque</code> module is typically called after all other node selection options have been processed, and if no nodes have been selected, the module will attempt to read a running jobid from the PBS_JOBID environment variable (which is set when running under a Torque allocation).</p>
<dl>
<dt><i>-j jobid[,jobid,&#8230;]</i></p>
<dd> Target list of nodes allocated to the Torque job <i>jobid</i>. This option may be used multiple times to target multiple Torque jobs. </p>
</dl>
<h2>rms module options</h2>
<p> The <code>rms</code> module allows pdsh to target nodes based on an RMS resource. The <code>rms</code> module is typically called after all other node selection options, and if no nodes have been selected, the module will examine the RMS_RESOURCEID environment variable and attempt to set the target list of hosts to the nodes in the RMS resource. If an invalid resource is denoted, the variable is silently ignored. </p>
<h2>SDR module options</h2>
<p> The SDR module supports targeting hosts via the System Data Repository on IBM SPs.</p>
<dl>
<dt><i>-a</i></p>
<dd> Target all nodes in the SDR. The list is generated from the &quot;reliable hostname&quot; in the SDR by default.</p>
<dt><i>-i</i></p>
<dd> Translate hostnames between reliable and initial in the SDR, when applicable. If the a target hostname matches either the initial or reliable hostname in the SDR, the alternate name will be substitued. Thus a list composed of initial hostnames will instead be replaced with a list of reliable hostnames. For example, when used with <i>-a</i> above, all initial hostnames in the SDR are targeted.</p>
<dt><i>-v</i></p>
<dd> Do not target nodes that are marked as not responding in the SDR on the targeted interface. (If a hostname does not appear in the SDR, then that name will remain in the target hostlist.)</p>
<dt><i>-G</i></p>
<dd> In combination with <i>-a</i>, include all partitions. </p>
</dl>
<h2>nodeattr module options</h2>
<p> The <code>nodeattr</code> module supports access to the genders database via the <a href="/docs/linux/man/1-nodeattr/">nodeattr</a>(1) command. See the <code>genders</code> section above for a list of support options with this module. The option usage with the <code>nodeattr</code> module is the same as <code>genders</code>, above, with the exception that the <i>-i</i> option may only be used with <i>-a</i> or <i>-g</i>. <code>NOTE</code>: This module will only work with very old releases of genders where the <code><a href="/docs/linux/man/1-nodeattr/">nodeattr</a></code>(1) command supports the <i>-r</i> option, and before the libgenders API was available. Users running newer versions of genders will need to use the <code>genders</code> module instead. </p>
<h2>dshgroup module options</h2>
<p> The dshgroup module allows pdsh to use dsh (or Dancer&#8217;s shell) style group files from /etc/dsh/group/ or ~/.dsh/group/. The default search path may be overridden with the DSHGROUP_PATH environment variable, a colon-separated list of directories to search. The default value for DSHGROUP_PATH is /etc/dsh/group.</p>
<dl>
<dt><i>-g groupname,&#8230;</i></p>
<dd> Target nodes in dsh group file &quot;groupname&quot; found in either ~/.dsh/group/groupname or /etc/dsh/group/groupname.</p>
<dt><i>-X groupname,&#8230;</i></p>
<dd> Exclude nodes in dsh group file &quot;groupname.&quot;</dl>
<p> As an enhancement in <code>pdsh</code>, dshgroup files may optionally include other dshgroup files via a special <i>#include STRING</i> syntax. The argument to <i>#include</i> may be either a file path, or a group name, in which case the path used to search for the group file is the same as if the group had been specified to <i>-g</i>. </p>
<h2>netgroup module options</h2>
<p> The netgroup module allows pdsh to use standard netgroup entries to build lists of target hosts. (/etc/netgroup or NIS)</p>
<dl>
<dt><i>-g groupname,&#8230;</i></p>
<dd> Target nodes in netgroup &quot;groupname.&quot;</p>
<dt><i>-X groupname,&#8230;</i></p>
<dd> Exclude nodes in netgroup &quot;groupname.&quot; </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>PDSH_RCMD_TYPE</p>
<dd> Equivalent to the <i>-R</i> option, the value of this environment variable will be used to set the default rcmd module for pdsh to use (e.g. ssh, rsh).</p>
<dt>PDSH_SSH_ARGS</p>
<dd> Override the standard arguments that <code>pdsh</code> passes to the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command (&quot;-2 -a -x -l%u %h&quot;). The use of the parameters <code>%u</code>, <code>%h</code>, and <code>%n</code> (as documented in the <code>rcmd/exec</code> section above) is optional. If these parameters are missing, <code>pdsh</code> will append them to the ssh commandline because it is assumed they are mandatory.</p>
<dt>PDSH_SSH_ARGS_APPEND</p>
<dd> Append additional options to the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command invoked by <code>pdsh</code>. For example, PDSH_SSH_ARGS_APPEND=&quot;-q&quot; would run ssh in quiet mode, or &quot;-v&quot; would increase the verbosity of ssh. (Note: these arguments are actually prepended to the ssh commandline to ensure they appear before any target hostname argument to ssh.)</p>
<dt>WCOLL</p>
<dd> If no other node selection option is used, the WCOLL environment variable may be set to a filename from which a list of target hosts will be read. The file should contain a list of hosts, one per line (though each line may contain a hostlist expression. See <i>HOSTLIST EXPRESSIONS</i> section below).</p>
<dt>DSHPATH</p>
<dd> If set, the path in DSHPATH will be used as the PATH for the remote processes.</p>
<dt>FANOUT</p>
<dd> Set the <code>pdsh</code> fanout (See description of <i>-f</i> above). </p>
</dl>
<h2>HOSTLIST EXPRESSIONS</h2>
<p> As noted in sections above <code>pdsh</code> accepts lists of hosts the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc., as an alternative to explicit lists of hosts. This form should not be confused with regular expression character classes (also denoted by &#8220;[]&#8221;). For example, foo[19] does not represent an expression matching foo1 or foo9, but rather represents the degenerate hostlist: foo19. </p>
<p> The hostlist syntax is meant only as a convenience on clusters with a &quot;prefixNNN&quot; naming convention and specification of ranges should not be considered necessary &#8212; this foo1,foo9 could be specified as such, or by the hostlist foo[1,9]. </p>
<p> Some examples of usage follow: </p>
<pre><code>
Run command on foo01, foo02, ..., foo05 pdsh - w foo[01 - 05] command Run command on foo7, foo9, foo10 pdsh - w foo[7, 9 - 10] command Run command on foo0, foo4, foo5 pdsh - w foo[0 - 5] - x foo[1 - 3] command
</code></pre>
<p> A suffix on the hostname is also supported: </p>
<pre>
Run command on foo0-eth0,foo1-eth0,foo2-eth0,foo3-eth0
   pdsh -w foo[0-3]-eth0 command
</pre>
<p> As a reminder to the reader, some shells will interpret brackets (&#8216;[&#8216; and &#8216;]&#8217;) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. For example, in tcsh, the first example above should be executed as: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pdsh -w &quot;foo[01-05]&quot; command</p>
<h2>ORIGIN</h2>
<p> Originally a rewrite of IBM <a href="/docs/linux/man/1-dsh/">dsh</a>(1) by Jim Garlick &lt;garlick [at] llnl.gov&gt; on LLNL&#8217;s ASCI Blue-Pacific IBM SP system. It is now used on Linux clusters at LLNL. </p>
<h2>LIMITATIONS</h2>
<p> When using <code>ssh</code> for remote execution, expect the stderr of ssh to be folded in with that of the remote command. When invoked by <code>pdsh</code>, it is not possible for <code>ssh</code> to prompt for passwords if RSA/DSA keys are configured properly, etc.. For <code>ssh</code> implementations that suppport a connect timeout option, <code>pdsh</code> attempts to use that option to enforce the timeout (e.g. -oConnectTimeout=T for OpenSSH), otherwise connect timeouts are not supported when using <code>ssh</code>. Finally, there is no reliable way for <code>pdsh</code> to ensure that remote commands are actually terminated when using a command timeout. Thus if <i>-u</i> is used with <code>ssh</code> commands may be left running on remote hosts even after timeout has killed local <code>ssh</code> processes. </p>
<p> Output from multiple processes per node may be interspersed when using qshell or mqshell rcmd modules. </p>
<p> The number of nodes that <code>pdsh</code> can simultaneously execute remote jobs on is limited by the maximum number of threads that can be created concurrently, as well as the availability of reserved ports in the rsh and qshell rcmd modules. On systems that implement Posix threads, the limit is typically defined by the constant PTHREADS_THREADS_MAX. </p>
<h2>FILES</h2>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rsh/">rsh</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), <a href="/docs/linux/man/1-dshbak/">dshbak</a>(1), <a href="/docs/linux/man/1-pdcp/">pdcp</a>(1) </p>
<h2>Index</h2>
