---
title: "mpirun-openmpi(1)"
name: "mpirun-openmpi"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpirun-openmpi/"
description: "orterun, mpirun, mpiexec – Execute serial and parallel jobs in Open MPI. oshrun, shmemrun – Execute serial and parallel jobs in Open SHMEM."
---

<p>orterun, mpirun, mpiexec &#8211; Execute serial and parallel jobs in Open MPI. oshrun, shmemrun &#8211; Execute serial and parallel jobs in Open SHMEM. </p>
<p> <code>Note:</code> <i>mpirun</i>, <i>mpiexec</i>, and <i>orterun</i> are all synonyms for each other as well as <i>oshrun</i>, <i>shmemrun</i> in case Open SHMEM is installed. Using any of the names will produce the same behavior. </p>
<h2>Synopsis</h2>
<p>Single Process Multiple Data (SPMD) Model: </p>
<p> <code>mpirun</code> [ options ] <code>&lt;program&gt;</code> [ &lt;args&gt; ] </p>
<p> Multiple Instruction Multiple Data (MIMD) Model: </p>
<p> <code>mpirun</code> [ global_options ]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;local_options1&nbsp;] <code>&lt;program1&gt;</code> [ &lt;args1&gt; ] :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;local_options2&nbsp;] <code>&lt;program2&gt;</code> [ &lt;args2&gt; ] :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;local_optionsN&nbsp;] <code>&lt;programN&gt;</code> [ &lt;argsN&gt; ] </p>
<p> Note that in both models, invoking <i>mpirun</i> via an absolute path name is equivalent to specifying the <i>&#8211;prefix</i> option with a <i>&lt;dir&gt;</i> value equivalent to the directory where <i>mpirun</i> resides, minus its last subdirectory. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;/usr/local/bin/mpirun &#8230; </p>
<p> is equivalent to </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;mpirun &#8211;prefix&nbsp;/usr/local </p>
<h2>Quick Summary</h2>
<p>If you are simply looking for how to run an MPI application, you probably want to use a command line of the following form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;mpirun&nbsp;[&nbsp;-np X&nbsp;]&nbsp;[&nbsp;&#8211;hostfile&nbsp;&lt;filename&gt;&nbsp;]&nbsp;<wbr>&nbsp;&lt;program&gt; </p>
<p> This will run X copies of <i>&lt;program&gt;</i> in your current run-time environment (if running under a supported resource manager, Open MPI&#8217;s <i>mpirun</i> will usually automatically use the corresponding resource manager process starter, as opposed to, for example, <i>rsh</i> or <i>ssh</i>, which require the use of a hostfile, or will default to running all X copies on the localhost), scheduling (by default) in a round-robin fashion by CPU slot. See the rest of this page for more details. </p>
<p> Please note that mpirun automatically binds processes as of the start of the v1.8 series. Three binding patterns are used in the absence of any further directives:</p>
<dl COMPACT>
<dt><code>Bind to core:</code></p>
<dd>when the number of processes is &lt;= 2</p>
<dt><code>Bind to socket:</code></p>
<dd>when the number of processes is &gt; 2</p>
<dt><code>Bind to none:</code></p>
<dd>when oversubscribed</dl>
<p> If your application uses threads, then you probably want to ensure that you are either not bound at all (by specifying &#8211;bind-to none), or bound to multiple cores using an appropriate binding level or specific number of processing elements per application process.</p>
<h2>Options</h2>
<p><i>mpirun</i> will send the name of the directory where it was invoked on the local node to each of the remote nodes, and attempt to change to that directory. See the &quot;Current Working Directory&quot; section below for further details.</p>
<dl COMPACT>
<dt><code>&lt;program&gt;</code></p>
<dd>The program executable. This is identified as the first non-recognized argument to mpirun.</p>
<dt><code>&lt;args&gt;</code></p>
<dd>Pass these run-time arguments to every new process. These must always be the last arguments to <i>mpirun</i>. If an app context file is used, <i>&lt;args&gt;</i> will be ignored.</p>
<dt><code>-h</code>, &#8211;help</p>
<dd>Display help for this command</p>
<dt><code>-q</code>, &#8211;quiet</p>
<dd>Suppress informative messages from orterun during application execution.</p>
<dt><code>-v</code>, &#8211;verbose</p>
<dd>Be verbose</p>
<dt><code>-V</code>, &#8211;version</p>
<dd>Print version number. If no other arguments are given, this will also cause orterun to exit.</p>
<dt><code>-N </code>&lt;num&gt;</p>
<dd>Launch num processes per node on all allocated nodes (synonym for npernode).</p>
<dt><code>-display-map</code>, &#8211;display-map</p>
<dd>Display a table showing the mapped location of each process prior to launch.</p>
<dt><code>-display-allocation</code>, &#8211;display-allocation</p>
<dd>Display the detected resource allocation.</p>
<dt><code>-output-proctable</code>, &#8211;output-proctable</p>
<dd>Output the debugger proctable after launch.</p>
<dt><code>-dvm</code>, &#8211;dvm</p>
<dd>Create a persistent distributed virtual machine (DVM).</p>
<dt><code>-max-vm-size</code>, &#8211;max-vm-size &lt;size&gt;</p>
<dd>Number of processes to run.</p>
<dt><code>-novm</code>, &#8211;novm</p>
<dd>Execute without creating an allocation-spanning virtual machine (only start daemons on nodes hosting application procs).</p>
<dt><code>-hnp</code>, &#8211;hnp &lt;arg0&gt;</p>
<dd>Specify the URI of the Head Node Process (HNP), or the name of the file (specified as file:filename) that contains that info.</dl>
<p> Use one of the following options to specify which hosts (nodes) of the cluster to run on. Note that as of the start of the v1.8 release, mpirun will launch a daemon onto each host in the allocation (as modified by the following options) at the very beginning of execution, regardless of whether or not application processes will eventually be mapped to execute there. This is done to allow collection of hardware topology information from the remote nodes, thus allowing us to map processes against known topology. However, it is a change from the behavior in prior releases where daemons were only launched after mapping was complete, and thus only occurred on nodes where application processes would actually be executing.</p>
<dl COMPACT>
<dt><code>-H</code>, -host, &#8211;host &lt;host1,host2,&#8230;,hostN&gt;</p>
<dd>List of hosts on which to invoke processes.</p>
<dt><code>-hostfile</code>, &#8211;hostfile &lt;hostfile&gt;</p>
<dd>Provide a hostfile to use.</p>
<dt><code>-default-hostfile</code>, &#8211;default-hostfile &lt;hostfile&gt;</p>
<dd>Provide a default hostfile.</p>
<dt><code>-machinefile</code>, &#8211;machinefile &lt;machinefile&gt;</p>
<dd>Synonym for <i>-hostfile</i>.</p>
<dt><code>-cpu-set</code>, &#8211;cpu-set &lt;list&gt;</p>
<dd>Restrict launched processes to the specified logical cpus on each node (comma-separated list). Note that the binding options will still apply within the specified envelope &#8211; e.g., you can elect to bind each process to only one cpu within the specified cpu set.</dl>
<p> The following options specify the number of processes to launch. Note that none of the options imply a particular binding policy &#8211; e.g., requesting N processes for each socket does not imply that the processes will be bound to the socket.</p>
<dl COMPACT>
<dt><code>-c</code>, -n, &#8211;n, -np &lt;#&gt;</p>
<dd>Run this many copies of the program on the given nodes. This option indicates that the specified file is an executable program and not an application context. If no value is provided for the number of copies to execute (i.e., neither the &quot;-np&quot; nor its synonyms are provided on the command line), Open MPI will automatically execute a copy of the program on each process slot (see below for description of a &quot;process slot&quot;). This feature, however, can only be used in the SPMD model and will return an error (without beginning execution of the application) otherwise.</p>
<dt><code>—map-by ppr:N:&lt;object&gt;</code></p>
<dd>Launch N times the number of objects of the specified type on each node.</p>
<dt><code>-npersocket</code>, &#8211;npersocket &lt;#persocket&gt;</p>
<dd>On each node, launch this many processes times the number of processor sockets on the node. The <i>-npersocket</i> option also turns on the <i>-bind-to-socket</i> option. (deprecated in favor of &#8211;map-by ppr:n:socket)</p>
<dt><code>-npernode</code>, &#8211;npernode &lt;#pernode&gt;</p>
<dd>On each node, launch this many processes. (deprecated in favor of &#8211;map-by ppr:n:node)</p>
<dt><code>-pernode</code>, &#8211;pernode</p>
<dd>On each node, launch one process &#8212; equivalent to <i>-npernode</i> 1. (deprecated in favor of &#8211;map-by ppr:1:node)</dl>
<p> To map processes:</p>
<dl COMPACT>
<dt><code>&#8211;map-by </code>&lt;foo&gt;</p>
<dd>Map to the specified object, defaults to <i>socket</i>. Supported options include slot, hwthread, core, L1cache, L2cache, L3cache, socket, numa, board, node, sequential, distance, and ppr. Any object can include modifiers by adding a : and any combination of PE=n (bind n processing elements to each proc), SPAN (load balance the processes across the allocation), OVERSUBSCRIBE (allow more processes on a node than processing elements), and NOOVERSUBSCRIBE. This includes PPR, where the pattern would be terminated by another colon to separate it from the modifiers.</p>
<dt><code>-bycore</code>, &#8211;bycore</p>
<dd>Map processes by core (deprecated in favor of &#8211;map-by core)</p>
<dt><code>-byslot</code>, &#8211;byslot</p>
<dd>Map and rank processes round-robin by slot.</p>
<dt><code>-nolocal</code>, &#8211;nolocal</p>
<dd>Do not run any copies of the launched application on the same node as orterun is running. This option will override listing the localhost with <code>&#8211;host</code> or any other host-specifying mechanism.</p>
<dt><code>-nooversubscribe</code>, &#8211;nooversubscribe</p>
<dd>Do not oversubscribe any nodes; error (without starting any processes) if the requested number of processes would cause oversubscription. This option implicitly sets &quot;max_slots&quot; equal to the &quot;slots&quot; value for each node. (Enabled by default).</p>
<dt><code>-oversubscribe</code>, &#8211;oversubscribe</p>
<dd>Nodes are allowed to be oversubscribed, even on a managed system, and overloading of processing elements.</p>
<dt><code>-bynode</code>, &#8211;bynode</p>
<dd>Launch processes one per node, cycling by node in a round-robin fashion. This spreads processes evenly among nodes and assigns MPI_COMM_WORLD ranks in a round-robin, &quot;by node&quot; manner.</p>
<dt><code>-cpu-list</code>, &#8211;cpu-list &lt;cpus&gt;</p>
<dd>Comma-delimited list of processor IDs to which to bind processes [default=NULL]. Processor IDs are interpreted as hwloc logical core IDs. Run the hwloc <i><a href="/docs/linux/man/1-lstopo/">lstopo</a>(1)</i> command to see a list of available cores and their logical IDs.</dl>
<p> To order processes&#8217; ranks in MPI_COMM_WORLD:</p>
<dl COMPACT>
<dt><code>&#8211;rank-by </code>&lt;foo&gt;</p>
<dd>Rank in round-robin fashion according to the specified object, defaults to <i>slot</i>. Supported options include slot, hwthread, core, L1cache, L2cache, L3cache, socket, numa, board, and node.</dl>
<p> For process binding:</p>
<dl COMPACT>
<dt><code>&#8211;bind-to </code>&lt;foo&gt;</p>
<dd>Bind processes to the specified object, defaults to <i>core</i>. Supported options include slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none.</p>
<dt><code>-cpus-per-proc</code>, &#8211;cpus-per-proc &lt;#perproc&gt;</p>
<dd>Bind each process to the specified number of cpus. (deprecated in favor of &#8211;map-by &lt;obj&gt;:PE=n)</p>
<dt><code>-cpus-per-rank</code>, &#8211;cpus-per-rank &lt;#perrank&gt;</p>
<dd>Alias for <i>-cpus-per-proc</i>. (deprecated in favor of &#8211;map-by &lt;obj&gt;:PE=n)</p>
<dt><code>-bind-to-core</code>, &#8211;bind-to-core</p>
<dd>Bind processes to cores (deprecated in favor of &#8211;bind-to core)</p>
<dt><code>-bind-to-socket</code>, &#8211;bind-to-socket</p>
<dd>Bind processes to processor sockets (deprecated in favor of &#8211;bind-to socket)</p>
<dt><code>-report-bindings</code>, &#8211;report-bindings</p>
<dd>Report any bindings for launched processes.</dl>
<p> For rankfiles:</p>
<dl COMPACT>
<dt><code>-rf</code>, &#8211;rankfile &lt;rankfile&gt;</p>
<dd>Provide a rankfile file.</dl>
<p> To manage standard I/O:</p>
<dl COMPACT>
<dt><code>-output-filename</code>, &#8211;output-filename &lt;filename&gt;</p>
<dd>Redirect the stdout, stderr, and stddiag of all processes to a process-unique version of the specified filename. Any directories in the filename will automatically be created. Each output file will consist of filename.id, where the id will be the processes&#8217; rank in MPI_COMM_WORLD, left-filled with zero&#8217;s for correct ordering in listings. A relative path value will be converted to an absolute path based on the cwd where mpirun is executed. Note that this <i>will not</i> work on environments where the file system on compute nodes differs from that where mpirun is executed.</p>
<dt><code>-stdin</code>, &#8211;stdin &lt;rank&gt;</p>
<dd>The MPI_COMM_WORLD rank of the process that is to receive stdin. The default is to forward stdin to MPI_COMM_WORLD rank 0, but this option can be used to forward stdin to any process. It is also acceptable to specify <i>none</i>, indicating that no processes are to receive stdin.</p>
<dt><code>-merge-stderr-to-stdout</code>, &#8211;merge-stderr-to-stdout</p>
<dd>Merge stderr to stdout for each process.</p>
<dt><code>-tag-output</code>, &#8211;tag-output</p>
<dd>Tag each line of output to stdout, stderr, and stddiag with <code>[jobid, MCW_rank]&lt;stdxxx&gt;</code> indicating the process jobid and MPI_COMM_WORLD rank of the process that generated the output, and the channel which generated it.</p>
<dt><code>-timestamp-output</code>, &#8211;timestamp-output</p>
<dd>Timestamp each line of output to stdout, stderr, and stddiag.</p>
<dt><code>-xml</code>, &#8211;xml</p>
<dd>Provide all output to stdout, stderr, and stddiag in an xml format.</p>
<dt><code>-xml-file</code>, &#8211;xml-file &lt;filename&gt;</p>
<dd>Provide all output in XML format to the specified file.</p>
<dt><code>-xterm</code>, &#8211;xterm &lt;ranks&gt;</p>
<dd>Display the output from the processes identified by their MPI_COMM_WORLD ranks in separate xterm windows. The ranks are specified as a comma-separated list of ranges, with a -1 indicating all. A separate window will be created for each specified process. <code>Note:</code> xterm will normally terminate the window upon termination of the process running within it. However, by adding a &quot;!&quot; to the end of the list of specified ranks, the proper options will be provided to ensure that xterm keeps the window open <i>after</i> the process terminates, thus allowing you to see the process&#8217; output. Each xterm window will subsequently need to be manually closed. <code>Note:</code> In some environments, xterm may require that the executable be in the user&#8217;s path, or be specified in absolute or relative terms. Thus, it may be necessary to specify a local executable as &quot;./foo&quot; instead of just &quot;foo&quot;. If xterm fails to find the executable, mpirun will hang, but still respond correctly to a ctrl-c. If this happens, please check that the executable is being specified correctly and try again.</dl>
<p> To manage files and runtime environment:</p>
<dl COMPACT>
<dt><code>-path</code>, &#8211;path &lt;path&gt;</p>
<dd>&lt;path&gt; that will be used when attempting to locate the requested executables. This is used prior to using the local PATH setting.</p>
<dt><code>&#8211;prefix </code>&lt;dir&gt;</p>
<dd>Prefix directory that will be used to set the <i>PATH</i> and <i>LD_LIBRARY_PATH</i> on the remote node before invoking Open MPI or the target process. See the &quot;Remote Execution&quot; section, below.</p>
<dt><code>&#8211;noprefix</code></p>
<dd>Disable the automatic &#8211;prefix behavior</p>
<dt><code>-s</code>, &#8211;preload-binary</p>
<dd>Copy the specified executable(s) to remote machines prior to starting remote processes. The executables will be copied to the Open MPI session directory and will be deleted upon completion of the job.</p>
<dt><code>&#8211;preload-files </code>&lt;files&gt;</p>
<dd>Preload the comma separated list of files to the current working directory of the remote machines where processes will be launched prior to starting those processes.</p>
<dt><code>-set-cwd-to-session-dir</code>, &#8211;set-cwd-to-session-dir</p>
<dd>Set the working directory of the started processes to their session directory.</p>
<dt><code>-wd </code>&lt;dir&gt;</p>
<dd>Synonym for <i>-wdir</i>.</p>
<dt><code>-wdir </code>&lt;dir&gt;</p>
<dd>Change to the directory &lt;dir&gt; before the user&#8217;s program executes. See the &quot;Current Working Directory&quot; section for notes on relative paths. <code>Note:</code> If the <i>-wdir</i> option appears both on the command line and in an application context, the context will take precedence over the command line. Thus, if the path to the desired wdir is different on the backend nodes, then it must be specified as an absolute path that is correct for the backend node.</p>
<dt><code>-x </code>&lt;env&gt;</p>
<dd>Export the specified environment variables to the remote nodes before executing the program. Only one environment variable can be specified per <i>-x</i> option. Existing environment variables can be specified or new variable names specified with corresponding values. For example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;mpirun -x DISPLAY -x OFILE=/tmp/out &#8230; </p>
<p> The parser for the <i>-x</i> option is not very sophisticated; it does not even understand quoted values. Users are advised to set variables in the environment, and then use <i>-x</i> to export (not define) them.</dl>
<p> Setting MCA parameters:</p>
<dl COMPACT>
<dt><code>-gmca</code>, &#8211;gmca &lt;key&gt; &lt;value&gt;</p>
<dd>Pass global MCA parameters that are applicable to all contexts. <i>&lt;key&gt;</i> is the parameter name; <i>&lt;value&gt;</i> is the parameter value.</p>
<dt><code>-mca</code>, &#8211;mca &lt;key&gt; &lt;value&gt;</p>
<dd>Send arguments to various MCA modules. See the &quot;MCA&quot; section, below.</p>
<dt><code>-am </code>&lt;arg0&gt;</p>
<dd>Aggregate MCA parameter set file list.</p>
<dt><code>-tune</code>, &#8211;tune &lt;tune_file&gt;</p>
<dd>Specify a tune file to set arguments for various MCA modules and environment variables. See the &quot;Setting MCA parameters and environment variables from file&quot; section, below.</dl>
<p> For debugging:</p>
<dl COMPACT>
<dt><code>-debug</code>, &#8211;debug</p>
<dd>Invoke the user-level debugger indicated by the <i>orte_base_user_debugger</i> MCA parameter.</p>
<dt><code>&#8211;get-stack-traces</code></p>
<dd>When paired with the <code>&#8211;timeout</code> option, <i>mpirun</i> will obtain and print out stack traces from all launched processes that are still alive when the timeout expires. Note that obtaining stack traces can take a little time and produce a lot of output, especially for large process-count jobs.</p>
<dt><code>-debugger</code>, &#8211;debugger &lt;args&gt;</p>
<dd>Sequence of debuggers to search for when <i>&#8211;debug</i> is used (i.e. a synonym for <i>orte_base_user_debugger</i> MCA parameter).</p>
<dt><code>&#8211;timeout </code>&lt;seconds&gt;</p>
<dd>The maximum number of seconds that <i>mpirun</i> (also known as <i>mpiexec</i>,<i> oshrun</i>,<i> orterun</i>,<i></i> etc.) will run. After this many seconds, <i>mpirun</i> will abort the launched job and exit with a non-zero exit status. Using <code>&#8211;timeout</code> can be also useful when combined with the <code>&#8211;get-stack-traces</code> option.</p>
<dt><code>-tv</code>, &#8211;tv</p>
<dd>Launch processes under the TotalView debugger. Deprecated backwards compatibility flag. Synonym for <i>&#8211;debug</i>.</dl>
<p> There are also other options:</p>
<dl COMPACT>
<dt><code>&#8211;allow-run-as-root</code></p>
<dd>Allow <i>mpirun</i> to run when executed by the root user (<i>mpirun</i> defaults to aborting when launched as the root user). Be sure to see the <i>Running as root</i> section, below, for more detail.</p>
<dt><code>&#8211;app </code>&lt;appfile&gt;</p>
<dd>Provide an appfile, ignoring all other command line options.</p>
<dt><code>-cf</code>, &#8211;cartofile &lt;cartofile&gt;</p>
<dd>Provide a cartography file.</p>
<dt><code>-continuous</code>, &#8211;continuous</p>
<dd>Job is to run until explicitly terminated.</p>
<dt><code>-disable-recovery</code>, &#8211;disable-recovery</p>
<dd>Disable recovery (resets all recovery options to off).</p>
<dt><code>-do-not-launch</code>, &#8211;do-not-launch</p>
<dd>Perform all necessary operations to prepare to launch the application, but do not actually launch it.</p>
<dt><code>-do-not-resolve</code>, &#8211;do-not-resolve</p>
<dd>Do not attempt to resolve interfaces.</p>
<dt><code>-enable-recovery</code>, &#8211;enable-recovery</p>
<dd>Enable recovery from process failure [Default = disabled].</p>
<dt><code>-index-argv-by-rank</code>, &#8211;index-argv-by-rank</p>
<dd>Uniquely index argv[0] for each process using its rank.</p>
<dt><code>-leave-session-attached</code>, &#8211;leave-session-attached</p>
<dd>Do not detach OmpiRTE daemons used by this application. This allows error messages from the daemons as well as the underlying environment (e.g., when failing to launch a daemon) to be output.</p>
<dt><code>-max-restarts</code>, &#8211;max-restarts &lt;num&gt;</p>
<dd>Max number of times to restart a failed process.</p>
<dt><code>-ompi-server</code>, &#8211;ompi-server &lt;uri or file&gt;</p>
<dd>Specify the URI of the Open MPI server (or the mpirun to be used as the server), the name of the file (specified as file:filename) that contains that info, or the PID (specified as pid:#) of the mpirun to be used as the server. The Open MPI server is used to support multi-application data exchange via the MPI-2 MPI_Publish_name and MPI_Lookup_name functions.</p>
<dt><code>-personality</code>, &#8211;personality &lt;list&gt;</p>
<dd>Comma-separated list of programming model, languages, and containers being used (default=&quot;ompi&quot;).</p>
<dt><code>&#8211;ppr </code>&lt;list&gt;</p>
<dd>Comma-separated list of number of processes on a given resource type [default: none].</p>
<dt><code>-report-child-jobs-separately</code>, &#8211;report-child-jobs-separately</p>
<dd>Return the exit status of the primary job only.</p>
<dt><code>-report-events</code>, &#8211;report-events &lt;URI&gt;</p>
<dd>Report events to a tool listening at the specified URI.</p>
<dt><code>-report-pid</code>, &#8211;report-pid &lt;channel&gt;</p>
<dd>Print out mpirun&#8217;s PID during startup. The channel must be either a &#8216;-&#8216; to indicate that the pid is to be output to stdout, a &#8216;+&#8217; to indicate that the pid is to be output to stderr, or a filename to which the pid is to be written.</p>
<dt><code>-report-uri</code>, &#8211;report-uri &lt;channel&gt;</p>
<dd>Print out mpirun&#8217;s URI during startup. The channel must be either a &#8216;-&#8216; to indicate that the URI is to be output to stdout, a &#8216;+&#8217; to indicate that the URI is to be output to stderr, or a filename to which the URI is to be written.</p>
<dt><code>-show-progress</code>, &#8211;show-progress</p>
<dd>Output a brief periodic report on launch progress.</p>
<dt><code>-terminate</code>, &#8211;terminate</p>
<dd>Terminate the DVM.</p>
<dt><code>-use-hwthread-cpus</code>, &#8211;use-hwthread-cpus</p>
<dd>Use hardware threads as independent cpus.</p>
<dt><code>-use-regexp</code>, &#8211;use-regexp</p>
<dd>Use regular expressions for launch.</dl>
<p> The following options are useful for developers; they are not generally useful to most ORTE and/or MPI users:</p>
<dl COMPACT>
<dt><code>-d</code>, &#8211;debug-devel</p>
<dd>Enable debugging of the OmpiRTE (the run-time layer in Open MPI). This is not generally useful for most users.</p>
<dt><code>&#8211;debug-daemons</code></p>
<dd>Enable debugging of any OmpiRTE daemons used by this application.</p>
<dt><code>&#8211;debug-daemons-file</code></p>
<dd>Enable debugging of any OmpiRTE daemons used by this application, storing output in files.</p>
<dt><code>-display-devel-allocation</code>, &#8211;display-devel-allocation</p>
<dd>Display a detailed list of the allocation being used by this job.</p>
<dt><code>-display-devel-map</code>, &#8211;display-devel-map</p>
<dd>Display a more detailed table showing the mapped location of each process prior to launch.</p>
<dt><code>-display-diffable-map</code>, &#8211;display-diffable-map</p>
<dd>Display a diffable process map just before launch.</p>
<dt><code>-display-topo</code>, &#8211;display-topo</p>
<dd>Display the topology as part of the process map just before launch.</p>
<dt><code>-launch-agent</code>, &#8211;launch-agent</p>
<dd>Name of the executable that is to be used to start processes on the remote nodes. The default is &quot;orted&quot;. This option can be used to test new daemon concepts, or to pass options back to the daemons without having mpirun itself see them. For example, specifying a launch agent of orted -mca odls_base_verbose 5 allows the developer to ask the orted for debugging output without clutter from mpirun itself.</p>
<dt><code>&#8211;report-state-on-timeout</code></p>
<dd>When paired with the <code>&#8211;timeout</code> command line option, report the run-time subsystem state of each process when the timeout expires.</dl>
<p> There may be other options listed with <i>mpirun &#8211;help</i>.</p>
<h3>Environment Variables</h3>
<dl COMPACT>
<dt><code>MPIEXEC_TIMEOUT</code></p>
<dd>Synonym for the <code>&#8211;timeout</code> command line option.</dl>
<h2>Description</h2>
<p>One invocation of <i>mpirun</i> starts an MPI application running under Open MPI. If the application is single process multiple data (SPMD), the application can be specified on the <i>mpirun</i> command line. </p>
<p> If the application is multiple instruction multiple data (MIMD), comprising of multiple programs, the set of programs and argument can be specified in one of two ways: Extended Command Line Arguments, and Application Context. </p>
<p> An application context describes the MIMD program set including all arguments in a separate file. This file essentially contains multiple <i>mpirun</i> command lines, less the command name itself. The ability to specify different options for different instantiations of a program is another reason to use an application context. </p>
<p> Extended command line arguments allow for the description of the application layout on the command line using colons (<i>:</i>) to separate the specification of programs and arguments. Some options are globally set across all specified programs (e.g. &#8211;hostfile), while others are specific to a single program (e.g. -np).</p>
<h3>Specifying Host Nodes</h3>
<p>Host nodes can be identified on the <i>mpirun</i> command line with the <i>-host</i> option or in a hostfile. </p>
<p> For example,</p>
<dl COMPACT>
<dt>mpirun -H aa,aa,bb ./a.out</p>
<dd>launches two processes on node aa and one on bb.</dl>
<p> Or, consider the hostfile </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;cat myhostfile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;aa slots=2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;bb slots=2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;cc slots=2 </p>
<p> Here, we list both the host names (aa, bb, and cc) but also how many &quot;slots&quot; there are for each. Slots indicate how many processes can potentially execute on a node. For best performance, the number of slots may be chosen to be the number of cores on the node or the number of processor sockets. If the hostfile does not provide slots information, Open MPI will attempt to discover the number of cores (or hwthreads, if the use-hwthreads-as-cpus option is set) and set the number of slots to that value. This default behavior also occurs when specifying the <i>-host</i> option with a single hostname. Thus, the command</p>
<dl COMPACT>
<dt>mpirun -H aa ./a.out</p>
<dd>launches a number of processes equal to the number of cores on node aa.</dl>
<dl COMPACT>
<dt>mpirun -hostfile myhostfile ./a.out</p>
<dd>will launch two processes on each of the three nodes.</p>
<dt>mpirun -hostfile myhostfile -host aa ./a.out</p>
<dd>will launch two processes, both on node aa.</p>
<dt>mpirun -hostfile myhostfile -host dd ./a.out</p>
<dd>will find no hosts to run on and abort with an error. That is, the specified host dd is not in the specified hostfile.</dl>
<p> When running under resource managers (e.g., SLURM, Torque, etc.), Open MPI will obtain both the hostnames and the number of slots directly from the resource manger.</p>
<h3>Specifying Number of Processes</h3>
<p>As we have just seen, the number of processes to run can be set using the hostfile. Other mechanisms exist. </p>
<p> The number of processes launched can be specified as a multiple of the number of nodes or processor sockets available. For example,</p>
<dl COMPACT>
<dt>mpirun -H aa,bb -npersocket 2 ./a.out</p>
<dd>launches processes 0-3 on node aa and process 4-7 on node bb, where aa and bb are both dual-socket nodes. The <i>-npersocket</i> option also turns on the <i>-bind-to-socket</i> option, which is discussed in a later section.</p>
<dt>mpirun -H aa,bb -npernode 2 ./a.out</p>
<dd>launches processes 0-1 on node aa and processes 2-3 on node bb.</p>
<dt>mpirun -H aa,bb -npernode 1 ./a.out</p>
<dd>launches one process per host node.</p>
<dt>mpirun -H aa,bb -pernode ./a.out</p>
<dd>is the same as <i>-npernode</i> 1.</dl>
<p> Another alternative is to specify the number of processes with the <i>-np</i> option. Consider now the hostfile </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;cat myhostfile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;aa slots=4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;bb slots=4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;cc slots=4 </p>
<p> Now,</p>
<dl COMPACT>
<dt>mpirun -hostfile myhostfile -np 6 ./a.out</p>
<dd>will launch processes 0-3 on node aa and processes 4-5 on node bb. The remaining slots in the hostfile will not be used since the <i>-np</i> option indicated that only 6 processes should be launched.</dl>
<h3>Mapping Processes to Nodes: Using Policies</h3>
<p>The examples above illustrate the default mapping of process processes to nodes. This mapping can also be controlled with various <i>mpirun</i> options that describe mapping policies. </p>
<p> Consider the same hostfile as above, again with <i>-np</i> 6: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;node aa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;node bb&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;node cc </p>
<p>&nbsp;<wbr>&nbsp;mpirun&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 1 2 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 5 </p>
<p>&nbsp;<wbr>&nbsp;mpirun &#8211;map-by node&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 5 </p>
<p>&nbsp;<wbr>&nbsp;mpirun -nolocal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 1 2 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 5 </p>
<p> The <i>&#8211;map-by node</i> option will load balance the processes across the available nodes, numbering each process in a round-robin fashion. </p>
<p> The <i>-nolocal</i> option prevents any processes from being mapped onto the local host (in this case node aa). While <i>mpirun</i> typically consumes few system resources, <i>-nolocal</i> can be helpful for launching very large jobs where <i>mpirun</i> may actually need to use noticeable amounts of memory and/or processing time. </p>
<p> Just as <i>-np</i> can specify fewer processes than there are slots, it can also oversubscribe the slots. For example, with the same hostfile:</p>
<dl COMPACT>
<dt>mpirun -hostfile myhostfile -np 14 ./a.out</p>
<dd>will launch processes 0-3 on node aa, 4-7 on bb, and 8-11 on cc. It will then add the remaining two processes to whichever nodes it chooses.</dl>
<p> One can also specify limits to oversubscription. For example, with the same hostfile:</p>
<dl COMPACT>
<dt>mpirun -hostfile myhostfile -np 14 -nooversubscribe ./a.out</p>
<dd>will produce an error since <i>-nooversubscribe</i> prevents oversubscription.</dl>
<p> Limits to oversubscription can also be specified in the hostfile itself:<br />
&nbsp;%&nbsp;cat myhostfile<br />
&nbsp;aa slots=4 max_slots=4<br />
&nbsp;bb&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_slots=4<br />
&nbsp;cc slots=4 </p>
<p> The <i>max_slots</i> field specifies such a limit. When it does, the <i>slots</i> value defaults to the limit. Now:</p>
<dl COMPACT>
<dt>mpirun -hostfile myhostfile -np 14 ./a.out</p>
<dd>causes the first 12 processes to be launched as before, but the remaining two processes will be forced onto node cc. The other two nodes are protected by the hostfile against oversubscription by this job.</dl>
<p> Using the <i>&#8211;nooversubscribe</i> option can be helpful since Open MPI currently does not get &quot;max_slots&quot; values from the resource manager. </p>
<p> Of course, <i>-np</i> can also be used with the <i>-H</i> or <i>-host</i> option. For example,</p>
<dl COMPACT>
<dt>mpirun -H aa,bb -np 8 ./a.out</p>
<dd>launches 8 processes. Since only two hosts are specified, after the first two processes are mapped, one to aa and one to bb, the remaining processes oversubscribe the specified hosts.</dl>
<p> And here is a MIMD example:</p>
<dl COMPACT>
<dt>mpirun -H aa -np 1 hostname : -H bb,cc -np 2 uptime</p>
<dd>will launch process 0 running <i>hostname</i> on node aa and processes 1 and 2 each running <i>uptime</i> on nodes bb and cc, respectively.</dl>
<h3>Mapping, Ranking, and Binding: Oh My!</h3>
<p>Open MPI employs a three-phase procedure for assigning process locations and ranks:</p>
<dl COMPACT>
<dt><code>mapping</code></p>
<dd>Assigns a default location to each process</p>
<dt><code>ranking</code></p>
<dd>Assigns an MPI_COMM_WORLD rank value to each process</p>
<dt><code>binding</code></p>
<dd>Constrains each process to run on specific processors</dl>
<p> The <i>mapping</i> step is used to assign a default location to each process based on the mapper being employed. Mapping by slot, node, and sequentially results in the assignment of the processes to the node level. In contrast, mapping by object, allows the mapper to assign the process to an actual object on each node. </p>
<p> <code>Note:</code> the location assigned to the process is independent of where it will be bound &#8211; the assignment is used solely as input to the binding algorithm. </p>
<p> The mapping of process processes to nodes can be defined not just with general policies but also, if necessary, using arbitrary mappings that cannot be described by a simple policy. One can use the &quot;sequential mapper,&quot; which reads the hostfile line by line, assigning processes to nodes in whatever order the hostfile specifies. Use the <i>-mca rmaps seq</i> option. For example, using the same hostfile as before: </p>
<p> mpirun -hostfile myhostfile -mca rmaps seq ./a.out </p>
<p> will launch three processes, one on each of nodes aa, bb, and cc, respectively. The slot counts don&#8217;t matter; one process is launched per line on whatever node is listed on the line. </p>
<p> Another way to specify arbitrary mappings is with a rankfile, which gives you detailed control over process binding as well. Rankfiles are discussed below. </p>
<p> The second phase focuses on the <i>ranking</i> of the process within the job&#8217;s MPI_COMM_WORLD. Open MPI separates this from the mapping procedure to allow more flexibility in the relative placement of MPI processes. This is best illustrated by considering the following two cases where we used the —map-by ppr:2:socket option: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;node aa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;node bb </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank-by core&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 1&nbsp;!&nbsp;2 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 5&nbsp;!&nbsp;6 7 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank-by socket&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 2&nbsp;!&nbsp;1 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 6&nbsp;!&nbsp;5 7 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank-by socket:span&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 4&nbsp;!&nbsp;1 5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 6&nbsp;!&nbsp;3 7 </p>
<p> Ranking by core and by slot provide the identical result &#8211; a simple progression of MPI_COMM_WORLD ranks across each node. Ranking by socket does a round-robin ranking within each node until all processes have been assigned an MCW rank, and then progresses to the next node. Adding the <i>span</i> modifier to the ranking directive causes the ranking algorithm to treat the entire allocation as a single entity &#8211; thus, the MCW ranks are assigned across all sockets before circling back around to the beginning. </p>
<p> The <i>binding</i> phase actually binds each process to a given set of processors. This can improve performance if the operating system is placing processes suboptimally. For example, it might oversubscribe some multi-core processor sockets, leaving other sockets idle; this can lead processes to contend unnecessarily for common resources. Or, it might spread processes out too widely; this can be suboptimal if application performance is sensitive to interprocess communication costs. Binding can also keep the operating system from migrating processes excessively, regardless of how optimally those processes were placed to begin with. </p>
<p> The processors to be used for binding can be identified in terms of topological groupings &#8211; e.g., binding to an l3cache will bind each process to all processors within the scope of a single L3 cache within their assigned location. Thus, if a process is assigned by the mapper to a certain socket, then a <i>—bind-to l3cache</i> directive will cause the process to be bound to the processors that share a single L3 cache within that socket. </p>
<p> Alternatively, processes can be assigned to processors based on their local rank on a node using the <i>&#8211;bind-to cpu-list:ordered</i> option with an associated <i>&#8211;cpu-list &quot;0,2,5&quot;</i>. In this example, the first process on a node will be bound to cpu 0, the second process on the node will be bound to cpu 2, and the third process on the node will be bound to cpu 5. <i>&#8211;bind-to</i> will also accept <i>cpulist:ortered</i> as a synonym to <i>cpu-list:ordered</i>. Note that an error will result if more processes are assigned to a node than cpus are provided. </p>
<p> To help balance loads, the binding directive uses a round-robin method when binding to levels lower than used in the mapper. For example, consider the case where a job is mapped to the socket level, and then bound to core. Each socket will have multiple cores, so if multiple processes are mapped to a given socket, the binding algorithm will assign each process located to a socket to a unique core in a round-robin manner. </p>
<p> Alternatively, processes mapped by l2cache and then bound to socket will simply be bound to all the processors in the socket where they are located. In this manner, users can exert detailed control over relative MCW rank location and binding. </p>
<p> Finally, <i>&#8211;report-bindings</i> can be used to report bindings. </p>
<p> As an example, consider a node with two processor sockets, each comprising four cores. We run <i>mpirun</i> with <i>-np 4 &#8211;report-bindings</i> and the following additional options: </p>
<p>&nbsp;%&nbsp;mpirun &#8230; &#8211;map-by core &#8211;bind-to core<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,0]&nbsp;to cpus 0001<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,1]&nbsp;to cpus 0002<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,2]&nbsp;to cpus 0004<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,3]&nbsp;to cpus 0008 </p>
<p>&nbsp;%&nbsp;mpirun &#8230; &#8211;map-by socket &#8211;bind-to socket<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,0]&nbsp;to socket 0 cpus 000f<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,1]&nbsp;to socket 1 cpus 00f0<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,2]&nbsp;to socket 0 cpus 000f<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,3]&nbsp;to socket 1 cpus 00f0 </p>
<p>&nbsp;%&nbsp;mpirun &#8230; &#8211;map-by core:PE=2 &#8211;bind-to core<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,0]&nbsp;to cpus 0003<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,1]&nbsp;to cpus 000c<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,2]&nbsp;to cpus 0030<br />
&nbsp;[&#8230;]&nbsp;&#8230; binding child&nbsp;[&#8230;,3]&nbsp;to cpus 00c0 </p>
<p>&nbsp;%&nbsp;mpirun &#8230; &#8211;bind-to none </p>
<p> Here, <i>&#8211;report-bindings</i> shows the binding of each process as a mask. In the first case, the processes bind to successive cores as indicated by the masks 0001, 0002, 0004, and 0008. In the second case, processes bind to all cores on successive sockets as indicated by the masks 000f and 00f0. The processes cycle through the processor sockets in a round-robin fashion as many times as are needed. In the third case, the masks show us that 2 cores have been bound per process. In the fourth case, binding is turned off and no bindings are reported. </p>
<p> Open MPI&#8217;s support for process binding depends on the underlying operating system. Therefore, certain process binding options may not be available on every system. </p>
<p> Process binding can also be set with MCA parameters. Their usage is less convenient than that of <i>mpirun</i> options. On the other hand, MCA parameters can be set not only on the <i>mpirun</i> command line, but alternatively in a system or user mca-params.conf file or as environment variables, as described in the MCA section below. Some examples include: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mpirun option&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MCA parameter key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value </p>
<p>&nbsp;<wbr>&nbsp;&#8211;map-by core&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rmaps_base_mapping_policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;core<br />
&nbsp;<wbr>&nbsp;&#8211;map-by socket&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rmaps_base_mapping_policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;socket<br />
&nbsp;<wbr>&nbsp;&#8211;rank-by core&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rmaps_base_ranking_policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;core<br />
&nbsp;<wbr>&nbsp;&#8211;bind-to core&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hwloc_base_binding_policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;core<br />
&nbsp;<wbr>&nbsp;&#8211;bind-to socket&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hwloc_base_binding_policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;socket<br />
&nbsp;<wbr>&nbsp;&#8211;bind-to none&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hwloc_base_binding_policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;none</p>
<h3>Rankfiles</h3>
<p>Rankfiles are text files that specify detailed information about how individual processes should be mapped to nodes, and to which processor(s) they should be bound. Each line of a rankfile specifies the location of one process (for MPI jobs, the process&#8217; &quot;rank&quot; refers to its rank in MPI_COMM_WORLD). The general form of each line in the rankfile is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank&nbsp;&lt;N&gt;=&lt;hostname&gt;&nbsp;slot=&lt;slot list&gt; </p>
<p> For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;cat myrankfile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 0=aa slot=1:0-2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 1=bb slot=0:0,1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 2=cc slot=1-2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;mpirun -H aa,bb,cc,dd -rf myrankfile ./a.out </p>
<p> Means that </p>
<p>&nbsp;<wbr>&nbsp;Rank 0 runs on node aa, bound to logical socket 1, cores 0-2.<br />
&nbsp;<wbr>&nbsp;Rank 1 runs on node bb, bound to logical socket 0, cores 0 and 1.<br />
&nbsp;<wbr>&nbsp;Rank 2 runs on node cc, bound to logical cores 1 and 2. </p>
<p> Rankfiles can alternatively be used to specify <i>physical</i> processor locations. In this case, the syntax is somewhat different. Sockets are no longer recognized, and the slot number given must be the number of the physical PU as most OS&#8217;s do not assign a unique physical identifier to each core in the node. Thus, a proper physical rankfile looks something like the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;cat myphysicalrankfile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 0=aa slot=1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 1=bb slot=8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 2=cc slot=6 </p>
<p> This means that </p>
<p>&nbsp;<wbr>&nbsp;Rank 0 will run on node aa, bound to the core that contains physical PU 1<br />
&nbsp;<wbr>&nbsp;Rank 1 will run on node bb, bound to the core that contains physical PU 8<br />
&nbsp;<wbr>&nbsp;Rank 2 will run on node cc, bound to the core that contains physical PU 6 </p>
<p> Rankfiles are treated as <i>logical</i> by default, and the MCA parameter rmaps_rank_file_physical must be set to 1 to indicate that the rankfile is to be considered as <i>physical</i>. </p>
<p> The hostnames listed above are &quot;absolute,&quot; meaning that actual resolveable hostnames are specified. However, hostnames can also be specified as &quot;relative,&quot; meaning that they are specified in relation to an externally-specified list of hostnames (e.g., by mpirun&#8217;s &#8211;host argument, a hostfile, or a job scheduler). </p>
<p> The &quot;relative&quot; specification is of the form &quot;+n&lt;X&gt;&quot;, where X is an integer specifying the Xth hostname in the set of all available hostnames, indexed from 0. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;cat myrankfile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 0=+n0 slot=1:0-2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 1=+n1 slot=0:0,1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rank 2=+n2 slot=1-2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;mpirun -H aa,bb,cc,dd -rf myrankfile ./a.out </p>
<p> Starting with Open MPI v1.7, all socket/core slot locations are be specified as <i>logical</i> indexes (the Open MPI v1.6 series used <i>physical</i> indexes). You can use tools such as HWLOC&#8217;s &quot;lstopo&quot; to find the logical indexes of socket and cores.</p>
<h3>Application Context or Executable Program?</h3>
<p>To distinguish the two different forms, <i>mpirun</i> looks on the command line for <i>&#8211;app</i> option. If it is specified, then the file named on the command line is assumed to be an application context. If it is not specified, then the file is assumed to be an executable program.</p>
<h3>Locating Files</h3>
<p>If no relative or absolute path is specified for a file, Open MPI will first look for files by searching the directories specified by the <i>&#8211;path</i> option. If there is no <i>&#8211;path</i> option set or if the file is not found at the <i>&#8211;path</i> location, then Open MPI will search the user&#8217;s PATH environment variable as defined on the source node(s). </p>
<p> If a relative directory is specified, it must be relative to the initial working directory determined by the specific starter used. For example when using the rsh or ssh starters, the initial directory is $HOME by default. Other starters may set the initial directory to the current working directory from the invocation of <i>mpirun</i>.</p>
<h3>Current Working Directory</h3>
<p>The <i>-wdir</i> mpirun option (and its synonym, <i>-wd</i>) allows the user to change to an arbitrary directory before the program is invoked. It can also be used in application context files to specify working directories on specific nodes and/or for specific applications. </p>
<p> If the <i>-wdir</i> option appears both in a context file and on the command line, the context file directory will override the command line value. </p>
<p> If the <i>-wdir</i> option is specified, Open MPI will attempt to change to the specified directory on all of the remote nodes. If this fails, <i>mpirun</i> will abort. </p>
<p> If the <i>-wdir</i> option is <code>not</code> specified, Open MPI will send the directory name where <i>mpirun</i> was invoked to each of the remote nodes. The remote nodes will try to change to that directory. If they are unable (e.g., if the directory does not exist on that node), then Open MPI will use the default directory determined by the starter. </p>
<p> All directory changing occurs before the user&#8217;s program is invoked; it does not wait until <i>MPI_INIT</i> is called.</p>
<h3>Standard I/O</h3>
<p>Open MPI directs UNIX standard input to /dev/null on all processes except the MPI_COMM_WORLD rank 0 process. The MPI_COMM_WORLD rank 0 process inherits standard input from <i>mpirun</i>. <code>Note:</code> The node that invoked <i>mpirun</i> need not be the same as the node where the MPI_COMM_WORLD rank 0 process resides. Open MPI handles the redirection of <i>mpirun</i>&#8216;s standard input to the rank 0 process. </p>
<p> Open MPI directs UNIX standard output and error from remote nodes to the node that invoked <i>mpirun</i> and prints it on the standard output/error of <i>mpirun</i>. Local processes inherit the standard output/error of <i>mpirun</i> and transfer to it directly. </p>
<p> Thus it is possible to redirect standard I/O for Open MPI applications by using the typical shell redirection procedure on <i>mpirun</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;mpirun -np 2 my_app&nbsp;&lt;&nbsp;my_input&nbsp;&gt;&nbsp;my_output </p>
<p> Note that in this example <i>only</i> the MPI_COMM_WORLD rank 0 process will receive the stream from <i>my_input</i> on stdin. The stdin on all the other nodes will be tied to /dev/null. However, the stdout from all nodes will be collected into the <i>my_output</i> file.</p>
<h3>Signal Propagation</h3>
<p>When orterun receives a SIGTERM and SIGINT, it will attempt to kill the entire job by sending all processes in the job a SIGTERM, waiting a small number of seconds, then sending all processes in the job a SIGKILL. </p>
<p> SIGUSR1 and SIGUSR2 signals received by orterun are propagated to all processes in the job. </p>
<p> A SIGTSTOP signal to mpirun will cause a SIGSTOP signal to be sent to all of the programs started by mpirun and likewise a SIGCONT signal to mpirun will cause a SIGCONT sent. </p>
<p> Other signals are not currently propagated by orterun.</p>
<h3>Process Termination / Signal Handling</h3>
<p>During the run of an MPI application, if any process dies abnormally (either exiting before invoking <i>MPI_FINALIZE</i>, or dying as the result of a signal), <i>mpirun</i> will print out an error message and kill the rest of the MPI application. </p>
<p> User signal handlers should probably avoid trying to cleanup MPI state (Open MPI is currently not async-signal-safe; see <a href="/docs/linux/man/3-mpi_init_thread/">MPI_Init_thread</a>(3) for details about <i>MPI_THREAD_MULTIPLE</i> and thread safety). For example, if a segmentation fault occurs in <i>MPI_SEND</i> (perhaps because a bad buffer was passed in) and a user signal handler is invoked, if this user handler attempts to invoke <i>MPI_FINALIZE</i>, Bad Things could happen since Open MPI was already &quot;in&quot; MPI when the error occurred. Since <i>mpirun</i> will notice that the process died due to a signal, it is probably not necessary (and safest) for the user to only clean up non-MPI state.</p>
<h3>Process Environment</h3>
<p>Processes in the MPI application inherit their environment from the Open RTE daemon upon the node on which they are running. The environment is typically inherited from the user&#8217;s shell. On remote nodes, the exact environment is determined by the boot MCA module used. The <i>rsh</i> launch module, for example, uses either <i>rsh</i>/<i>ssh</i> to launch the Open RTE daemon on remote nodes, and typically executes one or more of the user&#8217;s shell-setup files before launching the Open RTE daemon. When running dynamically linked applications which require the <i>LD_LIBRARY_PATH</i> environment variable to be set, care must be taken to ensure that it is correctly set when booting Open MPI. </p>
<p> See the &quot;Remote Execution&quot; section for more details.</p>
<h3>Remote Execution</h3>
<p>Open MPI requires that the <i>PATH</i> environment variable be set to find executables on remote nodes (this is typically only necessary in <i>rsh</i>&#8211; or <i>ssh</i>-based environments &#8212; batch/scheduled environments typically copy the current environment to the execution of remote jobs, so if the current environment has <i>PATH</i> and/or <i>LD_LIBRARY_PATH</i> set properly, the remote nodes will also have it set properly). If Open MPI was compiled with shared library support, it may also be necessary to have the <i>LD_LIBRARY_PATH</i> environment variable set on remote nodes as well (especially to find the shared libraries required to run user MPI applications). </p>
<p> However, it is not always desirable or possible to edit shell startup files to set <i>PATH</i> and/or <i>LD_LIBRARY_PATH</i>. The <i>&#8211;prefix</i> option is provided for some simple configurations where this is not possible. </p>
<p> The <i>&#8211;prefix</i> option takes a single argument: the base directory on the remote node where Open MPI is installed. Open MPI will use this directory to set the remote <i>PATH</i> and <i>LD_LIBRARY_PATH</i> before executing any Open MPI or user applications. This allows running Open MPI jobs without having pre-configured the <i>PATH</i> and <i>LD_LIBRARY_PATH</i> on the remote nodes. </p>
<p> Open MPI adds the basename of the current node&#8217;s &quot;bindir&quot; (the directory where Open MPI&#8217;s executables are installed) to the prefix and uses that to set the <i>PATH</i> on the remote node. Similarly, Open MPI adds the basename of the current node&#8217;s &quot;libdir&quot; (the directory where Open MPI&#8217;s libraries are installed) to the prefix and uses that to set the <i>LD_LIBRARY_PATH</i> on the remote node. For example:</p>
<dl COMPACT>
<dt>Local bindir:</p>
<dd>/local/node/directory/bin</p>
<dt>Local libdir:</p>
<dd>/local/node/directory/lib64</dl>
<p> If the following command line is used: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;mpirun &#8211;prefix&nbsp;/remote/node/directory </p>
<p> Open MPI will add &quot;/remote/node/directory/bin&quot; to the <i>PATH</i> and &quot;/remote/node/directory/lib64&quot; to the <i>LD_LIBRARY_PATH</i> on the remote node before attempting to execute anything. </p>
<p> The <i>&#8211;prefix</i> option is not sufficient if the installation paths on the remote node are different than the local node (e.g., if &quot;/lib&quot; is used on the local node, but &quot;/lib64&quot; is used on the remote node), or if the installation paths are something other than a subdirectory under a common prefix. </p>
<p> Note that executing <i>mpirun</i> via an absolute pathname is equivalent to specifying <i>&#8211;prefix</i> without the last subdirectory in the absolute pathname to <i>mpirun</i>. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;/usr/local/bin/mpirun &#8230; </p>
<p> is equivalent to </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;mpirun &#8211;prefix&nbsp;/usr/local</p>
<h3>Exported Environment Variables</h3>
<p>All environment variables that are named in the form OMPI_* will automatically be exported to new processes on the local and remote nodes. Environmental parameters can also be set/forwarded to the new processes using the MCA parameter <i>mca_base_env_list</i>. The <i>-x</i> option to <i>mpirun</i> has been deprecated, but the syntax of the MCA param follows that prior example. While the syntax of the <i>-x</i> option and MCA param allows the definition of new variables, note that the parser for these options are currently not very sophisticated &#8211; it does not even understand quoted values. Users are advised to set variables in the environment and use the option to export them; not to define them.</p>
<h3>Setting MCA Parameters</h3>
<p>The <i>-mca</i> switch allows the passing of parameters to various MCA (Modular Component Architecture) modules. MCA modules have direct impact on MPI programs because they allow tunable parameters to be set at run time (such as which BTL communication device driver to use, what parameters to pass to that BTL, etc.). </p>
<p> The <i>-mca</i> switch takes two arguments: <i>&lt;key&gt;</i> and <i>&lt;value&gt;</i>. The <i>&lt;key&gt;</i> argument generally specifies which MCA module will receive the value. For example, the <i>&lt;key&gt;</i> &quot;btl&quot; is used to select which BTL to be used for transporting MPI messages. The <i>&lt;value&gt;</i> argument is the value that is passed. For example:</p>
<dl COMPACT>
<dt>mpirun -mca btl tcp,self -np 1 foo</p>
<dd>Tells Open MPI to use the &quot;tcp&quot; and &quot;self&quot; BTLs, and to run a single copy of &quot;foo&quot; an allocated node.</p>
<dt>mpirun -mca btl self -np 1 foo</p>
<dd>Tells Open MPI to use the &quot;self&quot; BTL, and to run a single copy of &quot;foo&quot; an allocated node.</dl>
<p> The <i>-mca</i> switch can be used multiple times to specify different <i>&lt;key&gt;</i> and/or <i>&lt;value&gt;</i> arguments. If the same <i>&lt;key&gt;</i> is specified more than once, the <i>&lt;value&gt;</i>s are concatenated with a comma (&quot;,&quot;) separating them. </p>
<p> Note that the <i>-mca</i> switch is simply a shortcut for setting environment variables. The same effect may be accomplished by setting corresponding environment variables before running <i>mpirun</i>. The form of the environment variables that Open MPI sets is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OMPI_MCA_&lt;key&gt;=&lt;value&gt; </p>
<p> Thus, the <i>-mca</i> switch overrides any previously set environment variables. The <i>-mca</i> settings similarly override MCA parameters set in the $OPAL_PREFIX/etc/openmpi-mca-params.conf or $HOME/.openmpi/mca-params.conf file. </p>
<p> Unknown <i>&lt;key&gt;</i> arguments are still set as environment variable &#8212; they are not checked (by <i>mpirun</i>) for correctness. Illegal or incorrect <i>&lt;value&gt;</i> arguments may or may not be reported &#8212; it depends on the specific MCA module. </p>
<p> To find the available component types under the MCA architecture, or to find the available parameters for a specific component, use the <i>ompi_info</i> command. See the <i><a href="/docs/linux/man/1-ompi_info/">ompi_info</a>(1)</i> man page for detailed information on the command.</p>
<h3>Setting MCA parameters and environment variables from file.</h3>
<p>The <i>-tune</i> command line option and its synonym <i>-mca mca_base_envar_file_prefix</i> allows a user to set mca parameters and environment variables with the syntax described below. This option requires a single file or list of files separated by &quot;,&quot; to follow. </p>
<p> A valid line in the file may contain zero or many &quot;-x&quot;, &quot;-mca&quot;, or “&#8211;mca” arguments. The following patterns are supported: -mca var val -mca var &quot;val&quot; -x var=val -x var. If any argument is duplicated in the file, the last value read will be used. </p>
<p> MCA parameters and environment specified on the command line have higher precedence than variables specified in the file.</p>
<h3>Running as root</h3>
<p>The Open MPI team strongly advises against executing <i>mpirun</i> as the root user. MPI applications should be run as regular (non-root) users. </p>
<p> Reflecting this advice, mpirun will refuse to run as root by default. To override this default, you can add the <i>&#8211;allow-run-as-root</i> option to the <i>mpirun</i> command line, or you can set the environmental parameters <i>OMPI_ALLOW_RUN_AS_ROOT=1</i> and <i>OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1</i>. Note that it takes setting <i>two</i> environment variables to effect the same behavior as <i>&#8211;allow-run-as-root</i> in order to stress the Open MPI team&#8217;s strong advice against running as the root user. After extended discussions with communities who use containers (where running as the root user is the default), there was a persistent desire to be able to enable root execution of <i>mpirun</i> via an environmental control (vs. the existing <i>&#8211;allow-run-as-root</i> command line parameter). The compromise of using <i>two</i> environment variables was reached: it allows root execution via an environmental control, but it conveys the Open MPI team&#8217;s strong recomendation against this behavior.</p>
<h3>Exit status</h3>
<p>There is no standard definition for what <i>mpirun</i> should return as an exit status. After considerable discussion, we settled on the following method for assigning the <i>mpirun</i> exit status (note: in the following description, the &quot;primary&quot; job is the initial application started by mpirun &#8211; all jobs that are spawned by that job are designated &quot;secondary&quot; jobs):</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>if all processes in the primary job normally terminate with exit status 0, we return 0</p>
<dt>&bull;</p>
<dd>if one or more processes in the primary job normally terminate with non-zero exit status, we return the exit status of the process with the lowest MPI_COMM_WORLD rank to have a non-zero status</p>
<dt>&bull;</p>
<dd>if all processes in the primary job normally terminate with exit status 0, and one or more processes in a secondary job normally terminate with non-zero exit status, we (a) return the exit status of the process with the lowest MPI_COMM_WORLD rank in the lowest jobid to have a non-zero status, and (b) output a message summarizing the exit status of the primary and all secondary jobs.</p>
<dt>&bull;</p>
<dd>if the cmd line option &#8211;report-child-jobs-separately is set, we will return -only- the exit status of the primary job. Any non-zero exit status in secondary jobs will be reported solely in a summary print statement.</dl>
<p> By default, OMPI records and notes that MPI processes exited with non-zero termination status. This is generally not considered an &quot;abnormal termination&quot; &#8211; i.e., OMPI will not abort an MPI job if one or more processes return a non-zero status. Instead, the default behavior simply reports the number of processes terminating with non-zero status upon completion of the job. </p>
<p> However, in some cases it can be desirable to have the job abort when any process terminates with non-zero status. For example, a non-MPI job might detect a bad result from a calculation and want to abort, but doesn&#8217;t want to generate a core file. Or an MPI job might continue past a call to MPI_Finalize, but indicate that all processes should abort due to some post-MPI result. </p>
<p> It is not anticipated that this situation will occur frequently. However, in the interest of serving the broader community, OMPI now has a means for allowing users to direct that jobs be aborted upon any process exiting with non-zero status. Setting the MCA parameter &quot;orte_abort_on_non_zero_status&quot; to 1 will cause OMPI to abort all processes once any process<br />
&nbsp;exits with non-zero status. </p>
<p> Terminations caused in this manner will be reported on the console as an &quot;abnormal termination&quot;, with the first process to so exit identified along with its exit status. </p>
<h2>Examples</h2>
<p>Be sure also to see the examples throughout the sections above.</p>
<dl COMPACT>
<dt>mpirun -np 4 -mca btl ib,tcp,self prog1</p>
<dd>Run 4 copies of prog1 using the &quot;ib&quot;, &quot;tcp&quot;, and &quot;self&quot; BTL&#8217;s for the transport of MPI messages.</p>
<dt>mpirun -np 4 -mca btl tcp,sm,self</p>
<dd>&#8211;mca btl_tcp_if_include eth0 prog1<br />
 Run 4 copies of prog1 using the &quot;tcp&quot;, &quot;sm&quot; and &quot;self&quot; BTLs for the transport of MPI messages, with TCP using only the eth0 interface to communicate. Note that other BTLs have similar if_include MCA parameters.</dl>
<h2>Return Value</h2>
<p><i>mpirun</i> returns 0 if all processes started by <i>mpirun</i> exit after calling MPI_FINALIZE. A non-zero value is returned if an internal error occurred in mpirun, or one or more processes exited before calling MPI_FINALIZE. If an internal error occurred in mpirun, the corresponding error code is returned. In the event that one or more processes exit before calling MPI_FINALIZE, the return value of the MPI_COMM_WORLD rank of the process that <i>mpirun</i> first notices died before calling MPI_FINALIZE will be returned. Note that, in general, this will be the first process that died but is not guaranteed to be so. </p>
<p> If the <code>&#8211;timeout</code> command line option is used and the timeout expires before the job completes (thereby forcing <i>mpirun</i> to kill the job) <i>mpirun</i> will return an exit status equivalent to the value of <code>ETIMEDOUT</code> (which is typically 110 on Linux and OS X systems). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-mpi_init_thread/">MPI_Init_thread</a>(3)</p>
