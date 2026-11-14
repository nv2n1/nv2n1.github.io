---
title: "criu(8)"
name: "criu"
section: "8"
letter: "c"
url: "/docs/linux/man/8-criu/"
description: "criu – checkpoint/restore in userspace"
---

<p>criu &#8211; checkpoint/restore in userspace</p>
<h2>Synopsis</h2>
<p><code>criu</code> <i>&lt;command&gt;</i> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>criu</code> is a tool for checkpointing and restoring running applications. It does this by saving their state as a collection of files (see the <i>dump</i> command) and creating equivalent processes from those files (see the <i>restore</i> command). The restore operation can be performed at a later time, on a different system, or both.</p>
<h2>Options</h2>
<p>The options are depending on the <i>&lt;command&gt;</i> <code>criu</code> run with.</p>
<h3>Common options</h3>
<p>Common options are applied to any <i>&lt;command&gt;</i>. </p>
<p> <code>-v</code>[<i>&lt;num&gt;</i>|<code>v</code>&#8230;]</p>
<dl>
<dd>Set logging level to <i>&lt;num&gt;</i>. The higer the level, the more output is produced. Either numeric values or multiple <code>v</code> can be used. </p>
<p> The following levels are available: </p>
<dl>
<dd>&bull; <code>-v1</code>, <code>-v</code> only messages and errors;</dl>
<dl>
<dd>&bull; <code>-v2</code>, <code>-vv</code> also warnings (default level);</dl>
<dl>
<dd>&bull; <code>-v3</code>, <code>-vvv</code> also information messages and timestamps;</dl>
<dl>
<dd>&bull; <code>-v4</code>, <code>-vvvv</code> lots of debug.</dl>
</dl>
<p> <code>&#8211;pidfile</code> <i>&lt;file&gt;</i></p>
<dl>
<dd>Write root task, service or page-server pid into a <i>&lt;file&gt;</i>.</dl>
<p> <code>-o</code>, <code>&#8211;log-file</code> <i>&lt;file&gt;</i></p>
<dl>
<dd>Write logging messages to <i>&lt;file&gt;</i>.</dl>
<p> <code>&#8211;log-pid</code></p>
<dl>
<dd>Write separate logging files per each pid.</dl>
<p> <code>-D</code>, <code>&#8211;images-dir</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Use path <i>&lt;path&gt;</i> as a base directory where to look for dump files set.</dl>
<p> <code>&#8211;prev-images-dir</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Use path <i>&lt;path&gt;</i> as a parent directory where to look for dump files set. This make sence in case of increment dumps.</dl>
<p> <code>-W</code>, <code>&#8211;work-dir</code> <i>&lt;dir&gt;</i></p>
<dl>
<dd>Use directory <i>&lt;dir&gt;</i> for putting logs, pidfiles and statistics. If not specified, <i>&lt;path&gt;</i> from <code>-D</code> option is taken.</dl>
<p> <code>&#8211;close</code> <i>&lt;fd&gt;</i></p>
<dl>
<dd>Close file with descriptor <i>&lt;fd&gt;</i> before any actions.</dl>
<p> <code>-L</code>, <code>&#8211;libdir</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Path to a plugins directory.</dl>
<p> <code>&#8211;action-script</code> <i>&lt;SCRIPT&gt;</i></p>
<dl>
<dd>Add an external action script. The environment variable <code>CRTOOLS_SCRIPT_ACTION</code> contains one of the actions: </p>
<dl>
<dd>&bull; <code>pre-dump</code> run an action prior to beginning a <code>dump</code></dl>
<dl>
<dd>&bull; <code>post-dump</code> run an action upon <code>dump</code> completion;</dl>
<dl>
<dd>&bull; <code>pre-restore</code> run an action prior to beginning a <code>restore</code></dl>
<dl>
<dd>&bull; <code>post-restore</code> run an action upon <code>restore</code> completion;</dl>
<dl>
<dd>&bull; <code>network-lock</code> lock network in a target network namespace;</dl>
<dl>
<dd>&bull; <code>network-unlock</code> unlock network in a target network namespace;</dl>
<dl>
<dd>&bull; <code>setup-namespaces</code> run an action once root task just been created with required namespaces, note it is early stage on restore nothing were restored yet except namespaces themselves.</dl>
</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Print program version and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a commands list and exit. The commands list is very short one just for overview and does not match this manual.</dl>
<h3>pre-dump</h3>
<p>Launches that named pre-dump procedure, where <code>criu</code> does snapshot of memory changes since previous pre-dump. Also <code>criu</code> forms fsnotify cache which speedup <code>restore</code> procedure. <code>pre-dump</code> requires at least <code>-t</code> option (see <code>dump</code> below). Optionally <code>page-server</code> options may be specified. </p>
<p> <code>&#8211;track-mem</code></p>
<dl>
<dd>Turn on memory changes tracker in the kernel. If the option is not passed the memory tracker get turned on implicitly.</dl>
<h3>dump</h3>
<p>Starts a checkpoint procedure. </p>
<p> <code>-t</code>, <code>&#8211;tree</code> <i>&lt;pid&gt;</i></p>
<dl>
<dd>Checkpoint the whole process tree starting from <i>&lt;pid&gt;</i>.</dl>
<p> <code>-R</code>, <code>&#8211;leave-running</code></p>
<dl>
<dd>Leave tasks in running state after checkpoint instead of killing them. This option is pretty dangerous and should be used if and only if you understand what you are doing. </p>
<p> If task is about to run after been checkpointed it can modify TCP connections, delete files and do other dangerous actions. So that <code>criu</code> itself can not guarantee that the next <code>restore</code> action will not fail. Most likely if a user starts <code>criu</code> with this option passed at least the file system snapshot must be done with help of <i>post-dump</i> script. </p>
<p> In other words, do not use it until really needed.</dl>
<p> <code>-s</code>, <code>&#8211;leave-stopped</code></p>
<dl>
<dd>Leave tasks in stopped state after checkpoint instead of killing them.</dl>
<p> <code>-x</code>, <code>&#8211;ext-unix-sk</code> [<i>&lt;inode&gt;</i>,&lt;inode&gt;&#8217;]</p>
<dl>
<dd>Dump external unix sockets. Optionally passing <i>&lt;inode&gt;</i> (or comma separated series) it assigns inodes which allowed for one sided dump.</dl>
<p> <code>&#8211;freeze-cgroup</code></p>
<dl>
<dd>Use cgroup freezer to collect processes.</dl>
<p> <code>&#8211;manage-cgroups</code></p>
<dl>
<dd>Collect cgroups into the image thus they gonna be restored then. Without this argument <code>criu</code> will not save cgroups configuration associated with a task.</dl>
<p> <code>&#8211;tcp-established</code></p>
<dl>
<dd>Checkpoint established TCP connections.</dl>
<p> <code>&#8211;veth-pair</code> <i>&lt;IN&gt;</i><code>=</code><i>&lt;OUT&gt;</i></p>
<dl>
<dd>Correspondence between outside and inside names of veth devices.</dl>
<p> <code>&#8211;evasive-devices</code></p>
<dl>
<dd>Use any path to a device file if the original one is inaccessible.</dl>
<p> <code>&#8211;page-server</code></p>
<dl>
<dd>Send pages to a page server (see <code>page-server</code> command).</dl>
<p> <code>&#8211;force-irmap</code></p>
<dl>
<dd>Force resolving names for inotify and fsnotify watches.</dl>
<p> <code>&#8211;auto-dedup</code></p>
<dl>
<dd>Deduplicate &quot;old&quot; data in pages images of previous <code>dump</code>. Which implies incremental <code>dump</code> mode (see <code>pre-dump</code> command).</dl>
<p> <code>-l</code>, <code>&#8211;file-locks</code></p>
<dl>
<dd>Dump file locks. It is necessary to make sure that all file lock users are taken into dump, so it is only safe to use this for enclojured containers where locks are not holed by someone outside of it.</dl>
<p> <code>-M</code>, <code>&#8211;ext-mount-map</code> <i>&lt;KEY&gt;</i><code>:</code><i>&lt;VAL&gt;</i></p>
<dl>
<dd>Setup mapping for external mounts. <i>&lt;KEY&gt;</i> is a mountpoint inside container and corresponding <i>&lt;VAL&gt;</i> is a string that will be written into the image as mountpoint&#8217;s root value.</dl>
<p> <code>&#8211;link-remap</code></p>
<dl>
<dd>Allow one to link unlinked files back when possible (modifies FS till <code>restore</code>).</dl>
<p> <code>&#8211;ghost-limit</code> <i>size</i></p>
<dl>
<dd>Allow one to specify maximum allowed size of deleted file to be carried inside image files. By default up to 1M file is allowed. It is done in a sake to not carry big files inside images. <i>size</i> may be postfixed with <i>K</i>, <i>M</i> or <i>G</i> (which stands for kilo, mega and gigabytes accordingly).</dl>
<p> <code>-j</code>, <code>&#8211;shell-job</code></p>
<dl>
<dd>Allow one to dump shell jobs. This implies the restored task will inherit session and process group ID from the criu itself. Also this option allows one to migrate a single external tty connection, in other words this option allows one to migrate such application as &quot;top&quot; and friends. If passed on <code>dump</code> it must be specified on <code>restore</code> as well.</dl>
<p> <code>&#8211;cpu-cap</code> [,<i>&lt;cap&gt;</i>]</p>
<dl>
<dd>Specify <i>cap</i> CPU capability to be written into an image file. Basically if <i>&lt;cap&gt;</i> is one of <code>all</code>, <code>cpu</code> or <code>ins</code>, then <code>criu</code> writes CPU related information into image file. If the option is omitted or set to <code>none</code> then image will not be written. By default <code>criu</code> do not write this image.</dl>
<h3>restore</h3>
<p>Restores previously checkpointed processes. </p>
<p> <code>&#8211;inherit-fd</code> <i>fd[&lt;num&gt;]:&lt;existing&gt;</i></p>
<dl>
<dd>Inherit file descriptors. This allows one to treat file descriptor <i>&lt;num&gt;</i> as being already opened via <i>&lt;existing&gt;</i> one and instead of trying to open we inherit it.</dl>
<p> <code>-d</code>, <code>&#8211;restore-detached</code></p>
<dl>
<dd>Detach <code>criu</code> itself once restore is complete.</dl>
<p> <code>-S</code>, <code>&#8211;restore-sibling</code></p>
<dl>
<dd>Restore root task as a sibling (make sense with <code>&#8211;restore-detached</code>) only.</dl>
<p> <code>-r</code>, <code>&#8211;root</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Change the root filesystem to &lt;path&gt; (when run in mount namespace).</dl>
<p> <code>&#8211;manage-cgroups</code> [&lt;mode&gt;]</p>
<dl>
<dd>Restore cgroups configuration associated with a task from the image. Controllers are always restored in optimistic way &#8212; if already present in system <code>criu</code> reuses it, otherwise it will be created. </p>
<p> The <i>&lt;mode&gt;</i> may be one of below. </p>
<dl>
<dd>&bull; <code>none</code>. Do not restore cgroup properties but require cgroup to pre-exist at the moment of <code>restore</code> procedure.</dl>
<dl>
<dd>&bull; <code>props</code>. Restore cgroup properties and require cgroup to pre-exist.</dl>
<dl>
<dd>&bull; <code>soft</code>. Restore cgroup properties if only cgroup has been created by <code>criu</code>, otherwise do not restore properies. This is the default if mode is unspecified.</dl>
<dl>
<dd>&bull; <code>full</code>. Always restore all cgroups and their properties.</dl>
<dl>
<dd>&bull; <code>strict</code>. Restore all cgroups and their properties from the scratch, requiring them to not present in the system.</dl>
</dl>
<p> <code>&#8211;cgroup-root</code> <i>[&lt;controller&gt;:]/&lt;newroot&gt;</i></p>
<dl>
<dd>Change the root cgroup the controller will be installed into. No controller means that root is the default for all controllers not specified.</dl>
<p> <code>&#8211;tcp-established</code></p>
<dl>
<dd>Restore previously dumped established TCP connections. This implies that the network has been locked between <code>dump</code> and <code>restore</code> phases so other side of a connection simply notice a kind of lag.</dl>
<p> <code>&#8211;veth-pair</code> <i>&lt;IN&gt;</i><code>=</code><i>&lt;OUT&gt;</i></p>
<dl>
<dd>Correspondence between outside and inside names of veth devices.</dl>
<p> <code>-l</code>, <code>&#8211;file-locks</code></p>
<dl>
<dd>Restore file locks from the image.</dl>
<p> <code>-M</code>, <code>&#8211;ext-mount-map</code> <i>&lt;KEY&gt;</i><code>:</code><i>&lt;VAL&gt;</i></p>
<dl>
<dd>Setup mapping for external mounts. <i>&lt;KEY&gt;</i> is the value from the image (<i>&lt;VAL&gt;</i> from dump) and the <i>&lt;VAL&gt;</i> is the path on host that will be bind-mounted into container (to the mountpoint path from image).</dl>
<p> <code>&#8211;ext-mount-map</code> <code>auto</code></p>
<dl>
<dd>This is a special case. If this flag is passed, when an external mount is missing from the command line <i></i><code>&#8211;ext-mount-map</code><i> &lt;KEY&gt;:&lt;VAL&gt;</i> syntax, criu attempts to automatically resolve this mount from its namespace.</dl>
<p> <code>&#8211;enable-external-sharing</code>, <code>&#8211;enable-external-masters</code></p>
<dl>
<dd>These flags enable external shared or slave mounts to be resolved automatically when <i></i><code>&#8211;ext-mount-map auto</code> is passed.</dl>
<p> <code>&#8211;auto-dedup</code></p>
<dl>
<dd>As soon as a page is restored it get punched out from image.</dl>
<p> <code>-j</code>, <code>&#8211;shell-job</code></p>
<dl>
<dd>Restore shell jobs, in other words inherit session and process group ID from the criu itself.</dl>
<p> <code>&#8211;cpu-cap</code> [<i>&lt;cap&gt;</i>,<i>&lt;cap&gt;</i>]</p>
<dl>
<dd>Specify <i>&lt;cap&gt;</i> CPU capability to be present on the CPU the process is restoring. To inverse capability prefix it with <code>^</code>. This option implies that <code>&#8211;cpu-cap</code> has been passed on <code>dump</code> as well, except <code>fpu</code> option case. </p>
<dl>
<dd>&bull; <code>all</code>. Require all capabilities. This is <code>default</code> mode if <code>&#8211;cpu-cap</code> is passed without arguments. Most safe mode.</dl>
<dl>
<dd>&bull; <code>cpu</code>. Require the CPU to have all capabilities in image to match runtime CPU.</dl>
<dl>
<dd>&bull; <code>fpu</code>. Requre the CPU to have comaptible FPU. For example the process might be dumped with xsave capability but attempted to restore without it present on target CPU. In such case we refuse to procceed. This is <code>default</code> mode if <code>&#8211;cpu-cap</code> is not present in command line. Note this argument might be passed even if on the <code>dump</code> no <code>&#8211;cpu-cap</code> have been specified becase FPU frames are always encoded into images.</dl>
<dl>
<dd>&bull; <code>ins</code>. Require CPU compatibility on instructions level.</dl>
<dl>
<dd>&bull; <code>none</code>. Ignore capabilities. Most dangerous mode. The behaviour is implementation dependent. Try to not use it until really required. </p>
<p> One possible need of using this option is when <code>&#8211;cpu-cap</code>=<code>cpu</code> has been passed on <code>dump</code> then images are migrated to a less capable processor and one need to <code>restore</code> this application, by default <code>criu</code> will refuse to proceed without relaxing capability with <code>&#8211;cpu-cap</code>=<code>none</code> parameter.</dl>
</dl>
<h3>check</h3>
<p>Checks whether the kernel supports the features that <code>criu</code> needs to successfully dump and restore a process tree. </p>
<p> There are three categories of kernel support as described below. <code>criu check</code> always checks Category 1 features unless <code>&#8211;feature</code> is specified which only checks the specified feature. </p>
<dl>
<dd>&bull; <code>Category 1</code>. Absolutely required. These are features like <i>/proc/&lt;pid&gt;/map_files</i>, <i>NETLINK_SOCK_DIAG</i> socket monitoring, <i>/proc/sys/kernel/ns_last_pid</i>, etc.</dl>
<dl>
<dd>&bull; <code>Category 2</code>. Required only for specific cases. These are features like aio remap, <i>/dev/net/tun</i>, etc. that are required if the process being dumped or restored is using them.</dl>
<dl>
<dd>&bull; <code>Category 3</code>. Experimental. These are features like task-diag that are used for experimental purposes (mostly during development).</dl>
<p> If there are no errors or warnings, <code>criu</code> prints &quot;Looks good.&quot; and its exit code will be 0. </p>
<p> A missing Category 1 feature causes <code>criu</code> to print &quot;Does not look good.&quot; and its exit code will be non-zero. </p>
<p> Missing Category 2 and 3 features cause <code>criu</code> to print &quot;Looks good but some kernel features are missing which, depending on your process tree, may cause dump or restore failure.&quot; and its exit code will be non-zero. </p>
<p> Without an argument, <code>criu check</code> checks Category 1 features. This behavior can change with the following options: </p>
<p> <code>&#8211;extra</code></p>
<dl>
<dd>Check kernel support for Category 2 features.</dl>
<p> <code>&#8211;experimental</code></p>
<dl>
<dd>Check kernel support for Category 3 features.</dl>
<p> <code>&#8211;all</code></p>
<dl>
<dd>Check kernel support for Category 1, 2, and 3 features.</dl>
<p> <code>&#8211;feature</code> <i>&lt;name&gt;</i></p>
<dl>
<dd>Check a specific feature. If <i>&lt;name&gt;</i> is <i>list</i>, a list of valid kernel feature names that can be checked will be printed.</dl>
<h3>page-server</h3>
<p>Launches <code>criu</code> in page server mode. </p>
<p> <code>&#8211;daemon</code></p>
<dl>
<dd>Runs page server as a daemon (background process).</dl>
<p> <code>&#8211;address</code> <i>&lt;address&gt;</i></p>
<dl>
<dd>Page server IP address.</dl>
<p> <code>&#8211;port</code> <i>&lt;number&gt;</i></p>
<dl>
<dd>Page server port number.</dl>
<h3>exec</h3>
<p>Executes a system call inside a destination task&#8217;s context.</p>
<h3>service</h3>
<p>Launches <code>criu</code> in RPC daemon mode where <code>criu</code> is listeninп for RPC commands over socket to perform. This is convenient for the case where daemon itself is running in a privilege (superuser) mode but clients are not.</p>
<h3>dedup</h3>
<p>Starts pagemap data deduplication procedure, where <code>criu</code> scans over all pagemap files and tries to minimalize the number of pagemap entries by obtaining the references from a parent pagemap image.</p>
<h3>cpuinfo dump</h3>
<p>Fetches current CPU features and write them into an image file.</p>
<h3>cpuinfo check</h3>
<p>Fetches current CPU features (ie CPU the <code>criu</code> is running on) and test if they are compatible with ones present in image file.</p>
<h2>Syscalls Execution</h2>
<p>To run a system call in another task&#8217;s context use </p>
<dl>
<dd>
<pre> criu exec -t pid syscall-string</pre>
</dl>
<p> command. The <i>syscall-string</i> should look like </p>
<dl>
<dd>
<pre> syscall-name syscall-arguments ...</pre>
</dl>
<p> Each command line argument is transformed into the system call argument by the following rules: </p>
<dl>
<dd>&bull; If one starts with <code>&amp;</code>, the rest of it gets copied to the target task&#8217;s address space and the respective syscall argument is the pointer to this string;</dl>
<dl>
<dd>&bull; Otherwise it is treated as a number (converted with strtol) and is directly passed into the system call.</dl>
<h2>Examples</h2>
<p>To checkpoint a program with pid of <code>1234</code> and write all image files into directory <code>checkpoint</code>: </p>
<dl>
<dd>
<pre> criu dump -D checkpoint -t 1234</pre>
</dl>
<p> To restore this program detaching criu itself: </p>
<dl>
<dd>
<pre> criu restore -d -D checkpoint</pre>
</dl>
<p> To close a file descriptor number <code>1</code> in task with pid <code>1234</code>: </p>
<dl>
<dd>
<pre> criu exec -t 1234 close 1</pre>
</dl>
<p> To open a file named <code>/foo/bar</code> for read-write in the task with pid <code>1234</code>: </p>
<dl>
<dd>
<pre> criu exec -t 1234 open '&amp;/foo/bar' 2</pre>
</dl>
<h2>Author</h2>
<p>OpenVZ team.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2011-2015, Parallels Inc.</p>
