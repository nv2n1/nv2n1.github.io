---

title: "virsh(1)"
name: "virsh"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virsh/"
description: "virsh – management user interface"
---

<p> virsh &#8211; management user interface </p>
<h2>SYNOPSIS</h2>
<p> <code>virsh</code> [<i></i><i>OPTION</i><i></i>]&#8230; [<i></i><i>COMMAND_STRING</i><i></i>] </p>
<p> <code>virsh</code> [<i></i><i>OPTION</i><i></i>]&#8230; <i></i><i>COMMAND</i><i></i> [<i></i><i>ARG</i><i></i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>virsh</code> program is the main interface for managing virsh guest domains. The program can be used to create, pause, and shutdown domains. It can also be used to list current domains. Libvirt is a C toolkit to interact with the virtualization capabilities of recent versions of Linux (and other OSes). It is free software available under the GNU Lesser General Public License. Virtualization of the Linux Operating System means the ability to run multiple instances of Operating Systems concurrently on a single hardware system where the basic resources are driven by a Linux instance. The library aims at providing a long term stable C API.  It currently supports Xen, QEMU, KVM, LXC, OpenVZ, VirtualBox and VMware ESX. </p>
<p> The basic structure of most virsh usage is: </p>
<pre><code>
virsh[OPTION]...&lt;command&gt;&lt;domain&gt;[ARG]...
</code></pre>
<p> Where <i>command</i> is one of the commands listed below; <i>domain</i> is the numeric domain id, or the domain name, or the domain UUID; and <i></i><i>ARGS</i><i></i> are command specific options. There are a few exceptions to this rule in the cases where the command in question acts on all domains, the entire machine, or directly on the xen hypervisor. Those exceptions will be clear for each of those commands. Note: it is permissible to give numeric names to domains, however, doing so will result in a domain that can only be identified by domain id. In other words, if a numeric value is supplied it will be interpreted as a domain id, not as a name. </p>
<p> The <code>virsh</code> program can be used either to run one <i></i><i>COMMAND</i><i></i> by giving the command and its arguments on the shell command line, or a <i></i><i>COMMAND_STRING</i><i></i> which is a single shell argument consisting of multiple <i></i><i>COMMAND</i><i></i> actions and their arguments joined with whitespace, and separated by semicolons between commands. Within <i></i><i>COMMAND_STRING</i><i></i>, virsh understands the same single, double, and backslash escapes as the shell, although you must add another layer of shell escaping in creating the single shell argument. If no command is given in the command line, <code>virsh</code> will then start a minimal interpreter waiting for your commands, and the <code>quit</code> command will then exit the program. </p>
<p> The <code>virsh</code> program understands the following <i></i><i>OPTIONS</i><i></i>.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;connect</code> <i></i><i>URI</i><i></i></dt>
<dd> Connect to the specified <i></i><i>URI</i><i></i>, as if by the <code>connect</code> command, instead of the default connection.</dd>
<dt><code>-d</code>, <code>&#8211;debug</code> <i></i><i>LEVEL</i><i></i></dt>
<dd> Enable debug messages at integer <i></i><i>LEVEL</i><i></i> and above. <i></i><i>LEVEL</i><i></i> can range from 0 to 4 (default). See the documentation of <code>VIRSH_DEBUG</code> environment variable below for the description of each <i></i><i>LEVEL</i><i></i>.</dd>
<dt><code>-e</code>, <code>&#8211;escape</code> <i>string</i></dt>
<dd> Set alternative escape sequence for <i>console</i> command. By default, telnet&#8217;s <code>^]</code> is used. Allowed characters when using hat notation are: alphabetic character, @, [, ], \, ^, _.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Ignore all other arguments, and behave as if the <code>help</code> command were given instead.</dd>
<dt><code>-k</code>, <code>&#8211;keepalive-interval</code> <i></i><i>INTERVAL</i><i></i></dt>
<dd> Set an <i></i><i>INTERVAL</i><i></i> (in seconds) for sending keepalive messages to check whether connection to the server is still alive. Setting the interval to 0 disables client keepalive mechanism.</dd>
<dt><code>-K</code>, <code>&#8211;keepalive-count</code> <i></i><i>COUNT</i><i></i></dt>
<dd> Set a number of times keepalive message can be sent without getting an answer from the server without marking the connection dead. There is no effect to this setting in case the <i></i><i>INTERVAL</i><i></i> is set to 0.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> <i></i><i>FILE</i><i></i></dt>
<dd> Output logging details to <i></i><i>FILE</i><i></i>.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Avoid extra informational messages.</dd>
<dt><code>-r</code>, <code>&#8211;readonly</code></dt>
<dd> Make the initial connection read-only, as if by the <i>&#8211;readonly</i> option of the <code>connect</code> command.</dd>
<dt><code>-t</code>, <code>&#8211;timing</code></dt>
<dd> Output elapsed time information for each command.</dd>
<dt><code>-v</code>, <code>&#8211;version[=short]</code></dt>
<dd> Ignore all other arguments, and prints the version of the libvirt library virsh is coming from</dd>
<dt><code>-V</code>, <code>&#8211;version=long</code></dt>
<dd> Ignore all other arguments, and prints the version of the libvirt library virsh is coming from and which options and driver are compiled in.</dd></dl>
<h2>NOTES</h2>
<p> Most <code>virsh</code> operations rely upon the libvirt library being able to connect to an already running libvirtd service. This can usually be done using the command <code>service libvirtd start</code>. </p>
<p> Most <code>virsh</code> commands require root privileges to run due to the communications channels used to talk to the hypervisor. Running as non root will return an error. </p>
<p> Most <code>virsh</code> commands act synchronously, except maybe shutdown, setvcpus and setmem. In those cases the fact that the <code>virsh</code> program returned, may not mean the action is complete and you must poll periodically to detect that the guest completed the operation. </p>
<p> <code>virsh</code> strives for backward compatibility. Although the <code>help</code> command only lists the preferred usage of a command, if an older version of <code>virsh</code> supported an alternate spelling of a command or option (such as <i>&#8211;tunnelled</i> instead of <i>&#8211;tunneled</i>), then scripts using that older spelling will continue to work. </p>
<p> Several <code>virsh</code> commands take an optionally scaled integer; if no scale is provided, then the default is listed in the command (for historical reasons, some commands default to bytes, while other commands default to kibibytes). The following case-insensitive suffixes can be used to select a specific scale:<br/>
&nbsp;<wbr>&nbsp;<wbr>b, byte&nbsp;<wbr>&nbsp;<wbr>byte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1<br/>
&nbsp;<wbr>&nbsp;<wbr>KB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>kilobyte&nbsp;<wbr>&nbsp;<wbr>1,000<br/>
&nbsp;<wbr>&nbsp;<wbr>k, KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>kibibyte&nbsp;<wbr>&nbsp;<wbr>1,024<br/>
&nbsp;<wbr>&nbsp;<wbr>MB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>megabyte&nbsp;<wbr>&nbsp;<wbr>1,000,000<br/>
&nbsp;<wbr>&nbsp;<wbr>M, MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mebibyte&nbsp;<wbr>&nbsp;<wbr>1,048,576<br/>
&nbsp;<wbr>&nbsp;<wbr>GB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gigabyte&nbsp;<wbr>&nbsp;<wbr>1,000,000,000<br/>
&nbsp;<wbr>&nbsp;<wbr>G, GiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gibibyte&nbsp;<wbr>&nbsp;<wbr>1,073,741,824<br/>
&nbsp;<wbr>&nbsp;<wbr>TB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>terabyte&nbsp;<wbr>&nbsp;<wbr>1,000,000,000,000<br/>
&nbsp;<wbr>&nbsp;<wbr>T, TiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tebibyte&nbsp;<wbr>&nbsp;<wbr>1,099,511,627,776<br/>
&nbsp;<wbr>&nbsp;<wbr>PB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>petabyte&nbsp;<wbr>&nbsp;<wbr>1,000,000,000,000,000<br/>
&nbsp;<wbr>&nbsp;<wbr>P, PiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pebibyte&nbsp;<wbr>&nbsp;<wbr>1,125,899,906,842,624<br/>
&nbsp;<wbr>&nbsp;<wbr>EB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exabyte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1,000,000,000,000,000,000<br/>
&nbsp;<wbr>&nbsp;<wbr>E, EiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exbibyte&nbsp;<wbr>&nbsp;<wbr>1,152,921,504,606,846,976</p>
<h2>GENERIC COMMANDS</h2>
<p> The following commands are generic i.e. not specific to a domain.</p>
<dl>
<dt><code>help</code> [<i>command-or-group</i>]</dt>
<dd> This lists each of the virsh commands. When used without options, all commands are listed, one per line, grouped into related categories, displaying the keyword for each group. </dd>
<p> To display only commands for a specific group, give the keyword for that group as an option. For example: </p>
<pre>
 virsh # help host
  Host and Hypervisor (help keyword 'host'):
     capabilities                   capabilities
     cpu-models                     show the CPU models for an architecture
     connect                        (re)connect to hypervisor
     freecell                       NUMA free memory
     hostname                       print the hypervisor hostname
     qemu-attach                    Attach to existing QEMU process
     qemu-monitor-command           QEMU Monitor Command
     qemu-agent-command             QEMU Guest Agent Command
     sysinfo                        print the hypervisor sysinfo
     uri                            print the hypervisor canonical URI
</pre>
<p> To display detailed information for a specific command, give its name as the option instead. For example: </p>
<p>virsh #help list<br/>
        NAME<br/>
            list &#8211;<br/>
    list domains<br/>
        SYNOPSIS<br/>
            list[&#8211;inactive][&#8211;all] DESCRIPTION<br/>
                Returns list of domains.OPTIONS&#8211; inactive list inactive domains&#8211; all list inactive &amp;active domains</p>
<dt><code>quit</code>, <code>exit</code></dt>
<dd> quit this interactive terminal</dd>
<dt><code>version</code> [<i>&#8211;daemon</i>]</dt>
<dd> Will print out the major version info about what this built from. If <i>&#8211;daemon</i> is specified then the version of the libvirt daemon is included in the output.</dd>
<dl>
<dl>
<dt>
</dt><dd> <code>Example</code> </dd>
<pre>
 $ virsh version
 Compiled against library: libvirt 1.2.3
 Using library: libvirt 1.2.3
 Using API: QEMU 1.2.3
 Running hypervisor: QEMU 2.0.50
 $ virsh version --daemon
 Compiled against library: libvirt 1.2.3
 Using library: libvirt 1.2.3
 Using API: QEMU 1.2.3
 Running hypervisor: QEMU 2.0.50
 Running against daemon: 1.2.6
</pre>
</dl>
</dl>
<dl>
</dl>
<dt><code>cd</code> [<i>directory</i>]</dt>
<dd> Will change current directory to <i>directory</i>. The default directory for the <code>cd</code> command is the home directory or, if there is no <i></i><i>HOME</i><i></i> variable in the environment, the root directory. </dd>
<p> This command is only available in interactive mode.</p>
<dt><code>pwd</code></dt>
<dd> Will print the current directory.</dd>
<dt><code>connect</code> [<i></i><i>URI</i><i></i>] [<i>&#8211;readonly</i>]</dt>
<dd> (Re)-Connect to the hypervisor. When the shell is first started, this is automatically run with the <i></i><i>URI</i><i></i> parameter requested by the <tt>&quot;-c&quot;</tt> option on the command line. The <i></i><i>URI</i><i></i> parameter specifies how to connect to the hypervisor. The documentation page at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; list the values supported, but the most common are:</dd>
<dl>
<dl>
<dt><a href="xen:///">xen:///</a></dt>
<dd> this is used to connect to the local Xen hypervisor</dd>
<dt><a href="qemu:///system">qemu:///system</a></dt>
<dd> connect locally as root to the daemon supervising QEMU and KVM domains</dd>
<dt><a href="qemu:///session">qemu:///session</a></dt>
<dd> connect locally as a normal user to his own set of QEMU and KVM domains</dd>
<dt><a href="lxc:///">lxc:///</a></dt>
<dd> connect to a local linux container</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> To find the currently used URI, check the <i>uri</i> command documented below. </p>
<p> For remote access see the documentation page at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; on how to make URIs. The <i>&#8211;readonly</i> option allows for read-only connection</dd></dl>
<dt><code>uri</code></dt>
<dd> Prints the hypervisor canonical URI, can be useful in shell mode.</dd>
<dt><code>hostname</code></dt>
<dd> Print the hypervisor hostname.</dd>
<dt><code>sysinfo</code></dt>
<dd> Print the XML representation of the hypervisor sysinfo, if available.</dd>
<dt><code>nodeinfo</code></dt>
<dd> Returns basic information about the node, like number and type of CPU, and size of the physical memory. The output corresponds to virNodeInfo structure. Specifically, the &#8220;CPU socket(s)&#8221; field means number of CPU sockets per NUMA cell. The information libvirt displays is dependent upon what each architecture may provide.</dd>
<dt><code>nodecpumap</code> [<i>&#8211;pretty</i>]</dt>
<dd> Displays the node&#8217;s total number of CPUs, the number of online CPUs and the list of online CPUs. </dd>
<p> With <i>&#8211;pretty</i> the online CPUs are printed as a range instead of a list.</p>
<dt><code>nodecpustats</code> [<i>cpu</i>] [<i>&#8211;percent</i>]</dt>
<dd> Returns cpu stats of the node. If <i>cpu</i> is specified, this will print the specified cpu statistics only. If <i>&#8211;percent</i> is specified, this will print the percentage of each kind of cpu statistics during 1 second.</dd>
<dt><code>nodememstats</code> [<i>cell</i>]</dt>
<dd> Returns memory stats of the node. If <i>cell</i> is specified, this will print the specified cell statistics only.</dd>
<dt><code>nodesuspend</code> [<i>target</i>] [<i>duration</i>]</dt>
<dd> Puts the node (host machine) into a system-wide sleep state and schedule the node&#8217;s Real-Time-Clock interrupt to resume the node after the time duration specified by <i>duration</i> is out. <i>target</i> specifies the state to which the host will be suspended to, it can be &#8220;mem&#8221; (suspend to RAM), &#8220;disk&#8221; (suspend to disk), or &#8220;hybrid&#8221; (suspend to both RAM and disk). <i>duration</i> specifies the time duration in seconds for which the host has to be suspended, it should be at least 60 seconds.</dd>
<dt><code>node-memory-tune</code> [<i>shm-pages-to-scan</i>] [<i>shm-sleep-millisecs</i>] [<i>shm-merge-across-nodes</i>]</dt>
<dd> Allows you to display or set the node memory parameters. <i>shm-pages-to-scan</i> can be used to set the number of pages to scan before the shared memory service goes to sleep; <i>shm-sleep-millisecs</i> can be used to set the number of millisecs the shared memory service should sleep before next scan; <i>shm-merge-across-nodes</i> specifies if pages from different numa nodes can be merged. When set to 0, only pages which physically reside in the memory area of same NUMA node can be merged. When set to 1, pages from all nodes can be merged. Default to 1. </dd>
<p> <code>Note</code>: Currently the &#8220;shared memory service&#8221; only means KSM (Kernel Samepage Merging).</p>
<dt><code>capabilities</code></dt>
<dd> Print an XML document describing the capabilities of the hypervisor we are currently connected to. This includes a section on the host capabilities in terms of CPU and features, and a set of description for each kind of guest which can be virtualized. For a more complete description see:<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;<a rel="nofollow" href="http://libvirt.org/formatcaps.html">http://libvirt.org/formatcaps.html</a>&gt; The XML also show the NUMA topology information if available.</dd>
<dt><code>domcapabilities</code> [<i>virttype</i>] [<i>emulatorbin</i>] [<i>arch</i>] [<i>machine</i>]</dt>
<dd> Print an XML document describing the domain capabilities for the hypervisor we are connected to using information either sourced from an existing domain or taken from the <code>virsh capabilities</code> output. This may be useful if you intend to create a new domain and are curious if for instance it could make use of VFIO by creating a domain for the hypervisor with a specific emulator and architecture. </dd>
<p> Each hypervisor will have different requirements regarding which options are required and which are optional. A hypervisor can support providing a default value for any of the options. </p>
<p> The <i>virttype</i> option specifies the virtualization type used. The value to be used is either from the &#8216;type&#8217; attribute of the &lt;domain/&gt; top level element from the domain XML or the &#8216;type&#8217; attribute found within each &lt;guest/&gt; element from the <code>virsh capabilities</code> output. The <i>emulatorbin</i> option specifies the path to the emulator. The value to be used is either the &lt;emulator&gt; element in the domain XML or the <code>virsh capabilities</code> output. The <i>arch</i> option specifies the architecture to be used for the domain. The value to be used is either the &#8220;arch&#8221; attribute from the domain&#8217;s XML &lt;os/&gt; element and &lt;type/&gt; subelement or the &#8220;name&#8221; attribute of an &lt;arch/&gt; element from the <code>virsh capabililites</code> output. The <i>machine</i> specifies the machine type for the emulator. The value to be used is either the &#8220;machine&#8221; attribute from the domain&#8217;s XML &lt;os/&gt; element and &lt;type/&gt; subelement or one from a list of machines from the <code>virsh capabilities</code> output for a specific architecture and domain type. </p>
<p> For the qemu hypervisor, a <i>virttype</i> of either &#8216;qemu&#8217; or &#8216;kvm&#8217; must be supplied along with either the <i>emulatorbin</i> or <i>arch</i> in order to generate output for the default <i>machine</i>. Supplying a <i>machine</i> value will generate output for the specific machine.</p>
<dt><code>inject-nmi</code> <i>domain</i></dt>
<dd> Inject NMI to the guest.</dd>
<dt><code>list</code> [<i>&#8211;inactive</i> | <i>&#8211;all</i>] [<i>&#8211;managed-save</i>] [<i>&#8211;title</i>] { [<i>&#8211;table</i>] | <i>&#8211;name</i> | <i>&#8211;uuid</i> } [<i>&#8211;persistent</i>] [<i>&#8211;transient</i>] [<i>&#8211;with-managed-save</i>] [<i>&#8211;without-managed-save</i>] [<i>&#8211;autostart</i>] [<i>&#8211;no-autostart</i>] [<i>&#8211;with-snapshot</i>] [<i>&#8211;without-snapshot</i>] [<i>&#8211;state-running</i>] [<i>&#8211;state-paused</i>] [<i>&#8211;state-shutoff</i>] [<i>&#8211;state-other</i>]</dt>
<dd> Prints information about existing domains. If no options are specified it prints out information about running domains. </dd>
<p> An example format for the list is as follows: </p>
<p> <code>virsh</code> list<br/>
&nbsp;<wbr>&nbsp;<wbr>Id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>State<br/>
&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br/>
&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Domain-0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>running<br/>
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fedora&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>paused </p>
<p> Name is the name of the domain. ID the domain numeric id. State is the run state (see below). </p>
<p> <code>STATES</code> </p>
<p> The State field lists what state each domain is currently in. A domain can be in one of the following possible states:</p>
<dl>
<dl>
<dt><code>running</code></dt>
<dd> The domain is currently running on a CPU</dd>
<dt><code>idle</code></dt>
<dd> The domain is idle, and not running or runnable. This can be caused because the domain is waiting on IO (a traditional wait state) or has gone to sleep because there was nothing else for it to do.</dd>
<dt><code>paused</code></dt>
<dd> The domain has been paused, usually occurring through the administrator running <code>virsh suspend</code>. When in a paused state the domain will still consume allocated resources like memory, but will not be eligible for scheduling by the hypervisor.</dd>
<dt><code>in shutdown</code></dt>
<dd> The domain is in the process of shutting down, i.e. the guest operating system has been notified and should be in the process of stopping its operations gracefully.</dd>
<dt><code>shut off</code></dt>
<dd> The domain is not running. Usually this indicates the domain has been shut down completely, or has not been started.</dd>
<dt><code>crashed</code></dt>
<dd> The domain has crashed, which is always a violent ending. Usually this state can only occur if the domain has been configured not to restart on crash.</dd>
<dt><code>pmsuspended</code></dt>
<dd> The domain has been suspended by guest power management, e.g. entered into s3 state.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Normally only active domains are listed. To list inactive domains specify <i>&#8211;inactive</i> or <i>&#8211;all</i> to list both active and inactive domains. </p>
<p> To further filter the list of domains you may specify one or more of filtering flags supported by the <code>list</code> command. These flags are grouped by function. Specifying one or more flags from a group enables the filter group. Note that some combinations of flags may yield no results. Supported filtering flags and groups:</p>
</dd><dl>
<dt><code>Persistence</code></dt>
<dd> Flag <i>&#8211;persistent</i> is used to include persistent domains in the returned list. To include transient domains specify <i>&#8211;transient</i>.</dd>
<dt><code>Existence of managed save image</code></dt>
<dd> To list domains having a managed save image specify flag <i>&#8211;with-managed-save</i>. For domains that don&#8217;t have a managed save image specify <i>&#8211;without-managed-save</i>.</dd>
<dt><code>Domain state</code></dt>
<dd> The following filter flags select a domain by its state: <i>&#8211;state-running</i> for running domains, <i>&#8211;state-paused</i> for paused domains, <i>&#8211;state-shutoff</i> for turned off domains and <i>&#8211;state-other</i> for all other states as a fallback.</dd>
<dt><code>Autostarting domains</code></dt>
<dd> To list autostarting domains use the flag <i>&#8211;autostart</i>. To list domains with this feature disabled use <i>&#8211;no-autostart</i>.</dd>
<dt><code>Snapshot existence</code></dt>
<dd> Domains that have snapshot images can be listed using flag <i>&#8211;with-snapshot</i>, domains without a snapshot <i>&#8211;without-snapshot</i>.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> When talking to older servers, this command is forced to use a series of API calls with an inherent race, where a domain might not be listed or might appear more than once if it changed state between calls while the list was being collected. Newer servers do not have this problem. </p>
<p> If <i>&#8211;managed-save</i> is specified, then domains that have managed save state (only possible if they are in the <code>shut off</code> state, so you need to specify <i>&#8211;inactive</i> or <i>&#8211;all</i> to actually list them) will instead show as <code>saved</code> in the listing. This flag is usable only with the default <i>&#8211;table</i> output. Note that this flag does not filter the list of domains. </p>
<p> If <i>&#8211;name</i> is specified, domain names are printed instead of the table formatted one per line. If <i>&#8211;uuid</i> is specified domain&#8217;s UUID&#8216;s are printed instead of names. Flag <i>&#8211;table</i> specifies that the legacy table-formatted output should be used. This is the default. </p>
<p> If both <i>&#8211;name</i> and <i>&#8211;uuid</i> are specified, domain UUID&#8216;s and names are printed side by side without any header. Flag <i>&#8211;table</i> specifies that the legacy table-formatted output should be used. This is the default if neither <i>&#8211;name</i> nor <i>&#8211;uuid</i> are specified. Option <i>&#8211;table</i> is mutually exclusive with options <i>&#8211;uuid</i> and <i>&#8211;name</i>. </p>
<p> If <i>&#8211;title</i> is specified, then the short domain description (title) is printed in an extra column. This flag is usable only with the default <i>&#8211;table</i> output. </p>
<p> Example: </p>
<p> <code>virsh</code> list &#8211;title<br/>
&nbsp;<wbr>&nbsp;<wbr>Id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>State&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Title<br/>
&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br/>
&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Domain-0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>running&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mailserver 1<br/>
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fedora&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>paused</dd></dl>
<dt><code>freecell</code> [{ [<i>&#8211;cellno</i>] <code>cellno</code> | <i>&#8211;all</i> }]</dt>
<dd> Prints the available amount of memory on the machine or within a NUMA cell. The freecell command can provide one of three different displays of available memory on the machine depending on the options specified. With no options, it displays the total free memory on the machine. With the &#8211;all option, it displays the free memory in each cell and the total free memory on the machine. Finally, with a numeric argument or with &#8211;cellno plus a cell number it will display the free memory for the specified cell only.</dd>
<dt><code>freepages</code> [{ [<i>&#8211;cellno</i>] <i>cellno</i> [<i>&#8211;pagesize</i>] <i>pagesize</i> | <i>&#8211;all</i> }]</dt>
<dd> Prints the available amount of pages within a NUMA cell. <i>cellno</i> refers to the NUMA cell you&#8217;re interested in. <i>pagesize</i> is a scaled integer (see <code>NOTES</code> above). Alternatively, if <i>&#8211;all</i> is used, info on each possible combination of NUMA cell and page size is printed out.</dd>
<dt><code>allocpages</code> [<i>&#8211;pagesize</i>] <i>pagesize</i> [<i>&#8211;pagecount</i>] <i>pagecount</i> [[<i>&#8211;cellno</i>] <i>cellno</i>] [<i>&#8211;add</i>] [<i>&#8211;all</i>]</dt>
<dd> Change the size of pages pool of <i>pagesize</i> on the host. If <i>&#8211;add</i> is specified, then <i>pagecount</i> pages are added into the pool. However, if <i>&#8211;add</i> wasn&#8217;t specified, then the <i>pagecount</i> is taken as the new absolute size of the pool (this may be used to free some pages and size the pool down). The <i>cellno</i> modifier can be used to narrow the modification down to a single host NUMA cell. On the other end of spectrum lies <i>&#8211;all</i> which executes the modification on all NUMA cells.</dd>
<dt><code>cpu-baseline</code> <i></i><i>FILE</i><i></i> [<i>&#8211;features</i>] [<i>&#8211;migratable</i>]</dt>
<dd> Compute baseline CPU which will be supported by all host CPUs given in &lt;file&gt;. The list of host CPUs is built by extracting all &lt;cpu&gt; elements from the &lt;file&gt;. Thus, the &lt;file&gt; can contain either a set of &lt;cpu&gt; elements separated by new lines or even a set of complete &lt;capabilities&gt; elements printed by <code>capabilities</code> command. If <i>&#8211;features</i> is specified then the resulting XML description will explicitly include all features that make up the CPU, without this option features that are part of the CPU model will not be listed in the XML description. If <i>&#8211;migratable</i> is specified, features that block migration will not be included in the resulting CPU.</dd>
<dt><code>cpu-compare</code> <i></i><i>FILE</i><i></i> [<i>&#8211;error</i>]</dt>
<dd> Compare CPU definition from XML &lt;file&gt; with host CPU. The XML &lt;file&gt; may contain either host or guest CPU definition. The host CPU definition is the &lt;cpu&gt; element and its contents as printed by <code>capabilities</code> command. The guest CPU definition is the &lt;cpu&gt; element and its contents from domain XML definition. For more information on guest CPU definition see: &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsCPU">http://libvirt.org/formatdomain.html#elementsCPU</a>&gt;. If <i>&#8211;error</i> is specified, the command will return an error when the given CPU is incompatible with host CPU and a message providing more details about the incompatibility will be printed out.</dd>
<dt><code>cpu-models</code> <i>arch</i></dt>
<dd> Print the list of CPU models known for the specified architecture.</dd>
<dt><code>echo</code> [<i>&#8211;shell</i>] [<i>&#8211;xml</i>] [<i>arg</i>&#8230;]</dt>
<dd> Echo back each <i>arg</i>, separated by space. If <i>&#8211;shell</i> is specified, then the output will be single-quoted where needed, so that it is suitable for reuse in a shell context. If <i>&#8211;xml</i> is specified, then the output will be escaped for use in XML.</dd></dl>
<h2>DOMAIN COMMANDS</h2>
<p> The following commands manipulate domains directly, as stated previously most commands take domain as the first parameter. The <i>domain</i> can be specified as a short integer, a name or a full UUID.</p>
<dl>
<dt><code>autostart</code> [<i>&#8211;disable</i>] <i>domain</i></dt>
<dd> Configure a domain to be automatically started at boot. </dd>
<p> The option <i>&#8211;disable</i> disables autostarting.</p>
<dt><code>console</code> <i>domain</i> [<i>devname</i>] [<i>&#8211;safe</i>] [<i>&#8211;force</i>]</dt>
<dd> Connect the virtual serial console for the guest. The optional <i>devname</i> parameter refers to the device alias of an alternate console, serial or parallel device configured for the guest. If omitted, the primary console will be opened. </dd>
<p> If the flag <i>&#8211;safe</i> is specified, the connection is only attempted if the driver supports safe console handling. This flag specifies that the server has to ensure exclusive access to console devices. Optionally the <i>&#8211;force</i> flag may be specified, requesting to disconnect any existing sessions, such as in a case of a broken connection.</p>
<dt><code>create</code> <i></i><i>FILE</i><i></i> [<i>&#8211;console</i>] [<i>&#8211;paused</i>] [<i>&#8211;autodestroy</i>] [<i>&#8211;pass-fds N,M,&#8230;</i>]</dt>
<dd> Create a domain from an XML &lt;file&gt;. An easy way to create the XML &lt;file&gt; is to use the <code>dumpxml</code> command to obtain the definition of a pre-existing guest. The domain will be paused if the <i>&#8211;paused</i> option is used and supported by the driver; otherwise it will be running. If <i>&#8211;console</i> is requested, attach to the console after creation. If <i>&#8211;autodestroy</i> is requested, then the guest will be automatically destroyed when virsh closes its connection to libvirt, or otherwise exits. </dd>
<p> If <i>&#8211;pass-fds</i> is specified, the argument is a comma separated list of open file descriptors which should be pass on into the guest. The file descriptors will be re-numbered in the guest, starting from 3. This is only supported with container based virtualization. </p>
<p> <code>Example</code> </p>
<pre>
 virsh dumpxml &lt;domain&gt; &gt; domain.xml
 vi domain.xml (or make changes with your other text editor)
 virsh create domain.xml
</pre>
<dt><code>define</code> <i></i><i>FILE</i><i></i></dt>
<dd> Define a domain from an XML &lt;file&gt;. The domain definition is registered but not started. If domain is already running, the changes will take effect on the next boot.</dd>
<dt><code>desc</code> <i>domain</i> [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] [<i>&#8211;title</i>] [<i>&#8211;edit</i>] [<i>&#8211;new-desc</i> New description or title message]</dt>
<dd> Show or modify description and title of a domain. These values are user fields that allow to store arbitrary textual data to allow easy identification of domains. Title should be short, although it&#8217;s not enforced. (See also <code>metadata</code> that works with XML based domain metadata.) </dd>
<p> Flags <i>&#8211;live</i> or <i>&#8211;config</i> select whether this command works on live or persistent definitions of the domain. If both <i>&#8211;live</i> and <i>&#8211;config</i> are specified, the <i>&#8211;config</i> option takes precedence on getting the current description and both live configuration and config are updated while setting the description. <i>&#8211;current</i> is exclusive and implied if none of these was specified. </p>
<p> Flag <i>&#8211;edit</i> specifies that an editor with the contents of current description or title should be opened and the contents saved back afterwards. </p>
<p> Flag <i>&#8211;title</i> selects operation on the title field instead of description. </p>
<p> If neither of <i>&#8211;edit</i> and <i>&#8211;new-desc</i> are specified the note or description is displayed instead of being modified.</p>
<dt><code>destroy</code> <i>domain</i> [<i>&#8211;graceful</i>]</dt>
<dd> Immediately terminate the domain <i>domain</i>. This doesn&#8217;t give the domain OS any chance to react, and it&#8217;s the equivalent of ripping the power cord out on a physical machine. In most cases you will want to use the <code>shutdown</code> command instead. However, this does not delete any storage volumes used by the guest, and if the domain is persistent, it can be restarted later. </dd>
<p> If <i>domain</i> is transient, then the metadata of any snapshots will be lost once the guest stops running, but the snapshot contents still exist, and a new domain with the same name and UUID can restore the snapshot metadata with <code>snapshot-create</code>. </p>
<p> If <i>&#8211;graceful</i> is specified, don&#8217;t resort to extreme measures (e.g. SIGKILL) when the guest doesn&#8217;t stop after a reasonable timeout; return an error instead.</p>
<dt><code>domblkstat</code> <i>domain</i> [<i>block-device</i>] [<i>&#8211;human</i>]</dt>
<dd> Get device block stats for a running domain. A <i>block-device</i> corresponds to a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names). On a lxc or qemu domain, omitting the <i>block-device</i> yields device block stats summarily for the entire domain. </dd>
<p> Use <i>&#8211;human</i> for a more human readable output. </p>
<p> Availability of these fields depends on hypervisor. Unsupported fields are missing from the output. Other fields may appear if communicating with a newer version of libvirtd. </p>
<p> <code>Explanation of fields</code> (fields appear in the following order):<br/>
&nbsp;<wbr>&nbsp;<wbr>rd_req&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; count of read operations<br/>
&nbsp;<wbr>&nbsp;<wbr>rd_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; count of read bytes<br/>
&nbsp;<wbr>&nbsp;<wbr>wr_req&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; count of write operations<br/>
&nbsp;<wbr>&nbsp;<wbr>wr_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; count of written bytes<br/>
&nbsp;<wbr>&nbsp;<wbr>errs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; error count<br/>
&nbsp;<wbr>&nbsp;<wbr>flush_operations&nbsp;<wbr>&nbsp;<wbr>&#8211; count of flush operations<br/>
&nbsp;<wbr>&nbsp;<wbr>rd_total_times&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; total time read operations took&nbsp;<wbr>(ns)<br/>
&nbsp;<wbr>&nbsp;<wbr>wr_total_times&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; total time write operations took&nbsp;<wbr>(ns)<br/>
&nbsp;<wbr>&nbsp;<wbr>flush_total_times &#8211; total time flush operations took&nbsp;<wbr>(ns)<br/>
&nbsp;<wbr>&lt;&#8211; other fields provided by hypervisor &#8211;&gt;</p>
<dt><code>domifaddr</code> <i>domain</i> [<i>interface</i>] [<i>&#8211;full</i>] [<i>&#8211;source lease|agent</i>]</dt>
<dd> Get a list of interfaces of a running domain along with their IP and MAC addresses, or limited output just for one interface if <i>interface</i> is specified. Note that <i>interface</i> can be driver dependent, it can be the name within guest OS or the name you would see in domain XML. Moreover, the whole command may require a guest agent to be configured for the queried domain under some drivers, notably qemu. If <i>&#8211;full</i> is specified, the interface name is always displayed when the interface has multiple addresses or alias, otherwise it only displays the interface name for the first address, and &#8220;-&#8221; for the others. The <i>&#8211;source</i> argument specifies what data source to use for the addresses, currently one of &#8216;lease&#8217; to read DHCP leases, or &#8216;agent&#8217; to query the guest OS via an agent. If unspecified, &#8216;lease&#8217; is the default.</dd>
<dt><code>domifstat</code> <i>domain</i> <i>interface-device</i></dt>
<dd> Get network interface stats for a running domain.</dd>
<dt><code>domif-setlink</code> <i>domain</i> <i>interface-device</i> <i>state</i> [<i>&#8211;config</i>]</dt>
<dd> Modify link state of the domain&#8217;s virtual interface. Possible values for state are &#8220;up&#8221; and &#8220;down&#8221;. If <i>&#8211;config</i> is specified, only the persistent configuration of the domain is modified, for compatibility purposes, <i>&#8211;persistent</i> is alias of <i>&#8211;config</i>. <i>interface-device</i> can be the interface&#8217;s target name or the MAC address.</dd>
<dt><code>domif-getlink</code> <i>domain</i> <i>interface-device</i> [<i>&#8211;config</i>]</dt>
<dd> Query link state of the domain&#8217;s virtual interface. If <i>&#8211;config</i> is specified, query the persistent configuration, for compatibility purposes, <i>&#8211;persistent</i> is alias of <i>&#8211;config</i>. </dd>
<p> <i>interface-device</i> can be the interface&#8217;s target name or the MAC address.</p>
<dt><code>domiftune</code> <i>domain</i> <i>interface-device</i> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]] [<i>&#8211;inbound average,peak,burst,floor</i>] [<i>&#8211;outbound average,peak,burst</i>]</dt>
<dd> Set or query the domain&#8217;s network interface&#8217;s bandwidth parameters. <i>interface-device</i> can be the interface&#8217;s target name (&lt;target dev=&#8217;name&#8217;/&gt;), or the MAC address. </dd>
<p> If no <i>&#8211;inbound</i> or <i>&#8211;outbound</i> is specified, this command will query and show the bandwidth settings. Otherwise, it will set the inbound or outbound bandwidth. <i>average,peak,burst,floor</i> is the same as in command <i>attach-interface</i>. Values for <i>average</i>, <i>peak</i> and <i>floor</i> are expressed in kilobytes per second, while <i>burst</i> is expressed in kilobytes in a single burst at <i>peak</i> speed as described in the Network XML documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatnetwork.html#elementQoS">http://libvirt.org/formatnetwork.html#elementQoS</a>&gt;. </p>
<p> To clear inbound or outbound settings, use <i>&#8211;inbound</i> or <i>&#8211;outbound</i> respectfully with average value of zero. </p>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor.</p>
<dt><code>dommemstat</code> <i>domain</i> [<i>&#8211;period</i> <code>seconds</code>] [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Get memory stats for a running domain. </dd>
<p> Availability of these fields depends on hypervisor. Unsupported fields are missing from the output. Other fields may appear if communicating with a newer version of libvirtd. </p>
<p> <code>Explanation of fields</code>:<br/>
&nbsp;<wbr>&nbsp;<wbr>swap_in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The amount of data read from swap space&nbsp;<wbr>(in kB)<br/>
&nbsp;<wbr>&nbsp;<wbr>swap_out&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The amount of memory written out to swap space&nbsp;<wbr>(in kB)<br/>
&nbsp;<wbr>&nbsp;<wbr>major_fault&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The number of page faults where disk&nbsp;<wbr>IO&nbsp;<wbr>was required<br/>
&nbsp;<wbr>&nbsp;<wbr>minor_fault&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The number of other page faults<br/>
&nbsp;<wbr>&nbsp;<wbr>unused&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The amount of memory left unused by the system&nbsp;<wbr>(in kB)<br/>
&nbsp;<wbr>&nbsp;<wbr>available&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The amount of usable memory as seen by the domain&nbsp;<wbr>(in kB)<br/>
&nbsp;<wbr>&nbsp;<wbr>actual&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Current balloon value&nbsp;<wbr>(in&nbsp;<wbr>KB)<br/>
&nbsp;<wbr>&nbsp;<wbr>rss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Resident Set Size of the running domain&#8217;s process&nbsp;<wbr>(in kB)<br/>
&nbsp;<wbr>&nbsp;<wbr>usable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The amount of memory which can be reclaimed by balloon without causing host swapping (in KB)<br/>
&nbsp;<wbr>&nbsp;<wbr>last-update&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Timestamp of the last update of statistics&nbsp;<wbr>(in seconds) </p>
<p> For QEMU/KVM with a memory balloon, setting the optional <i>&#8211;period</i> to a value larger than 0 in seconds will allow the balloon driver to return additional statistics which will be displayed by subsequent <code>dommemstat</code> commands. Setting the <i>&#8211;period</i> to 0 will stop the balloon driver collection, but does not clear the statistics in the balloon driver. Requires at least QEMU/KVM 1.5 to be running on the host. </p>
<p> The <i>&#8211;live</i>, <i>&#8211;config</i>, and <i>&#8211;current</i> flags are only valid when using the <i>&#8211;period</i> option in order to set the collection period for the balloon driver. If <i>&#8211;live</i> is specified, only the running guest collection period is affected. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. </p>
<p> Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on the guest state.</p>
<dt><code>domblkerror</code> <i>domain</i></dt>
<dd> Show errors on block devices. This command usually comes handy when <code>domstate</code> command says that a domain was paused due to I/O error. The <code>domblkerror</code> command lists all block devices in error state and the error seen on each of them.</dd>
<dt><code>domblkinfo</code> <i>domain</i> <i>block-device</i></dt>
<dd> Get block device size info for a domain. A <i>block-device</i> corresponds to a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names).</dd>
<dt><code>domblklist</code> <i>domain</i> [<i>&#8211;inactive</i>] [<i>&#8211;details</i>]</dt>
<dd> Print a table showing the brief information of all block devices associated with <i>domain</i>. If <i>&#8211;inactive</i> is specified, query the block devices that will be used on the next boot, rather than those currently in use by a running domain. If <i>&#8211;details</i> is specified, disk type and device value will also be printed. Other contexts that require a block device name (such as <i>domblkinfo</i> or <i>snapshot-create</i> for disk snapshots) will accept either target or unique source names printed by this command.</dd>
<dt><code>domstats</code> [<i>&#8211;raw</i>] [<i>&#8211;enforce</i>] [<i>&#8211;backing</i>] [<i>&#8211;state</i>] [<i>&#8211;cpu-total</i>] [<i>&#8211;balloon</i>] [<i>&#8211;vcpu</i>] [<i>&#8211;interface</i>] [<i>&#8211;block</i>] [<i>&#8211;perf</i>] [[<i>&#8211;list-active</i>] [<i>&#8211;list-inactive</i>] [<i>&#8211;list-persistent</i>] [<i>&#8211;list-transient</i>] [<i>&#8211;list-running</i>] [<i>&#8211;list-paused</i>] [<i>&#8211;list-shutoff</i>] [<i>&#8211;list-other</i>]] | [<i>domain</i> &#8230;]</dt>
<dd> Get statistics for multiple or all domains. Without any argument this command prints all available statistics for all domains. </dd>
<p> The list of domains to gather stats for can be either limited by listing the domains as a space separated list, or by specifying one of the filtering flags <i>&#8211;list-*</i>. (The approaches can&#8217;t be combined.) </p>
<p> By default some of the returned fields may be converted to more human friendly values by a set of pretty-printers. To suppress this behavior use the <i>&#8211;raw</i> flag. </p>
<p> The individual statistics groups are selectable via specific flags. By default all supported statistics groups are returned. Supported statistics groups flags are: <i>&#8211;state</i>, <i>&#8211;cpu-total</i>, <i>&#8211;balloon</i>, <i>&#8211;vcpu</i>, <i>&#8211;interface</i>, <i>&#8211;block</i>, <i>&#8211;perf</i>. </p>
<p> Note that &#8211; depending on the hypervisor type and version or the domain state &#8211; not all of the following statistics may be returned. </p>
<p> When selecting the <i>&#8211;state</i> group the following fields are returned: </p>
<p> &#8220;state.state&#8221; &#8211; state of the VM, returned as number from<br/>
                 virDomainState enum<br/>
 &#8220;state.reason&#8221; &#8211; reason for entering given state, returned<br/>
                  as int from virDomain*Reason enum corresponding<br/>
                  to given state</p>
<p> <i>&#8211;cpu-total</i> returns: </p>
<pre>
 &quot;cpu.time&quot; - total cpu time spent for this domain in nanoseconds
 &quot;cpu.user&quot; - user cpu time spent in nanoseconds
 &quot;cpu.system&quot; - system cpu time spent in nanoseconds
</pre>
<p> <i>&#8211;balloon</i> returns: </p>
<pre>
 &quot;balloon.current&quot; - the memory in kiB currently used
 &quot;balloon.maximum&quot; - the maximum memory in kiB allowed
 &quot;balloon.swap_in&quot; - the amount of data read from swap space (in kB)
 &quot;balloon.swap_out&quot; - the amount of memory written out to swap
                      space (in kB)
 &quot;balloon.major_fault&quot; - the number of page faults then disk IO
                         was required
 &quot;balloon.minor_fault&quot; - the number of other page faults
 &quot;balloon.unused&quot; - the amount of memory left unused by the
                    system (in kB)
 &quot;balloon.available&quot; - the amount of usable memory as seen by
                       the domain (in kB)
 &quot;balloon.rss&quot; - Resident Set Size of running domain's process
                 (in kB)
 &quot;balloon.usable&quot; - the amount of memory which can be reclaimed by
                    balloon without causing host swapping (in KB)
 &quot;balloon.last-update&quot; - timestamp of the last update of statistics
                         (in seconds)
</pre>
<p> <i>&#8211;vcpu</i> returns: </p>
<pre>
 &quot;vcpu.current&quot; - current number of online virtual CPUs
 &quot;vcpu.maximum&quot; - maximum number of online virtual CPUs
 &quot;vcpu.&lt;num&gt;.state&quot; - state of the virtual CPU &lt;num&gt;, as
                      number from virVcpuState enum
 &quot;vcpu.&lt;num&gt;.time&quot; - virtual cpu time spent by virtual
                     CPU &lt;num&gt; (in microseconds)
 &quot;vcpu.&lt;num&gt;.wait&quot; - virtual cpu time spent by virtual
                     CPU &lt;num&gt; waiting on I/O (in microseconds)
 &quot;vcpu.&lt;num&gt;.halted&quot; - virtual CPU &lt;num&gt; is halted: yes or
                       no (may indicate the processor is idle
                       or even disabled, depending on the
                       architecture)
</pre>
<p> <i>&#8211;interface</i> returns: </p>
<pre>
 &quot;net.count&quot; - number of network interfaces on this domain
 &quot;net.&lt;num&gt;.name&quot; - name of the interface &lt;num&gt;
 &quot;net.&lt;num&gt;.rx.bytes&quot; - number of bytes received
 &quot;net.&lt;num&gt;.rx.pkts&quot; - number of packets received
 &quot;net.&lt;num&gt;.rx.errs&quot; - number of receive errors
 &quot;net.&lt;num&gt;.rx.drop&quot; - number of receive packets dropped
 &quot;net.&lt;num&gt;.tx.bytes&quot; - number of bytes transmitted
 &quot;net.&lt;num&gt;.tx.pkts&quot; - number of packets transmitted
 &quot;net.&lt;num&gt;.tx.errs&quot; - number of transmission errors
 &quot;net.&lt;num&gt;.tx.drop&quot; - number of transmit packets dropped
</pre>
<p> <i>&#8211;perf</i> returns the statistics of all enabled perf events: </p>
<pre>
 &quot;perf.cmt&quot; - the cache usage in Byte currently used
 &quot;perf.mbmt&quot; - total system bandwidth from one level of cache
 &quot;perf.mbml&quot; - bandwidth of memory traffic for a memory controller
 &quot;perf.cpu_cycles&quot; - the count of cpu cycles (total/elapsed)
 &quot;perf.instructions&quot; - the count of instructions
 &quot;perf.cache_references&quot; - the count of cache hits
 &quot;perf.cache_misses&quot; - the count of caches misses
 &quot;perf.branch_instructions&quot; - the count of branch instructions
 &quot;perf.branch_misses&quot; - the count of branch misses
 &quot;perf.bus_cycles&quot; - the count of bus cycles
 &quot;perf.stalled_cycles_frontend&quot; - the count of stalled frontend
                                  cpu cycles
 &quot;perf.stalled_cycles_backend&quot; - the count of stalled backend
                                 cpu cycles
 &quot;perf.ref_cpu_cycles&quot; - the count of ref cpu cycles
 &quot;perf.cpu_clock&quot; - the count of cpu clock time
 &quot;perf.task_clock&quot; - the count of task clock time
 &quot;perf.page_faults&quot; - the count of page faults
 &quot;perf.context_switches&quot; - the count of context switches
 &quot;perf.cpu_migrations&quot; - the count of cpu migrations
 &quot;perf.page_faults_min&quot; - the count of minor page faults
 &quot;perf.page_faults_maj&quot; - the count of major page faults
 &quot;perf.alignment_faults&quot; - the count of alignment faults
 &quot;perf.emulation_faults&quot; - the count of emulation faults
</pre>
<p> See the <code>perf</code> command for more details about each event. </p>
<p> <i>&#8211;block</i> returns information about disks associated with each domain. Using the <i>&#8211;backing</i> flag extends this information to cover all resources in the backing chain, rather than the default of limiting information to the active layer for each guest disk. Information listed includes: </p>
<p> &#8220;block.count&#8221; &#8211; number of block devices being listed<br/>
 &#8220;block.&lt;num&gt;.name&#8221; &#8211; name of the target of the block<br/>
                      device &lt;num&gt; (the same name for<br/>
                      multiple entries if I&lt;&#8211;backing&gt;<br/>
                      is present)<br/>
 &#8220;block.&lt;num&gt;.backingIndex&#8221; &#8211; when I&lt;&#8211;backing&gt; is present,<br/>
                              matches up with the &lt;backingStore&gt;<br/>
                              index listed in domain XML for<br/>
                              backing files<br/>
 &#8220;block.&lt;num&gt;.path&#8221; &#8211; file source of block device &lt;num&gt;, if<br/>
                      it is a local file or block device<br/>
 &#8220;block.&lt;num&gt;.rd.reqs&#8221; &#8211; number of read requests<br/>
 &#8220;block.&lt;num&gt;.rd.bytes&#8221; &#8211; number of read bytes<br/>
 &#8220;block.&lt;num&gt;.rd.times&#8221; &#8211; total time (ns)<br/>
 spent on reads<br/>
     &#8220;block.&lt;num&gt;.wr.reqs&#8221; &#8211;<br/>
     number of write requests<br/>
     &#8220;block.&lt;num&gt;.wr.bytes&#8221; &#8211;<br/>
     number of written bytes<br/>
     &#8220;block.&lt;num&gt;.wr.times&#8221; &#8211;<br/>
     total time(ns)<br/>
 spent on writes<br/>
     &#8220;block.&lt;num&gt;.fl.reqs&#8221; &#8211;<br/>
     total flush requests<br/>
     &#8220;block.&lt;num&gt;.fl.times&#8221; &#8211;<br/>
     total time(ns) spent on cache flushing<br/>
 &#8220;block.&lt;num&gt;.errors&#8221; &#8211; Xen only: the &#8216;oo_req&#8217; value<br/>
 &#8220;block.&lt;num&gt;.allocation&#8221; &#8211; offset of highest written sector in bytes<br/>
 &#8220;block.&lt;num&gt;.capacity&#8221; &#8211; logical size of source file in bytes<br/>
 &#8220;block.&lt;num&gt;.physical&#8221; &#8211; physical size of source file in bytes<br/>
 &#8220;block.&lt;num&gt;.threshold&#8221; &#8211; threshold (in bytes) for delivering the<br/>
                           VIR_DOMAIN_EVENT_ID_BLOCK_THRESHOLD event<br/>
                           See domblkthreshold.</p>
<p> Selecting a specific statistics groups doesn&#8217;t guarantee that the daemon supports the selected group of stats. Flag <i>&#8211;enforce</i> forces the command to fail if the daemon doesn&#8217;t support the selected group.</p>
<dt><code>domiflist</code> <i>domain</i> [<i>&#8211;inactive</i>]</dt>
<dd> Print a table showing the brief information of all virtual interfaces associated with <i>domain</i>. If <i>&#8211;inactive</i> is specified, query the virtual interfaces that will be used on the next boot, rather than those currently in use by a running domain. Other contexts that require a MAC address of virtual interface (such as <i>detach-interface</i> or <i>domif-setlink</i>) will accept the MAC address printed by this command.</dd>
<dt><code>blockcommit</code> <i>domain</i> <i>path</i> [<i>bandwidth</i>] [<i>&#8211;bytes</i>] [<i>base</i>] [<i>&#8211;shallow</i>] [<i>top</i>] [<i>&#8211;delete</i>] [<i>&#8211;keep-relative</i>] [<i>&#8211;wait</i> [<i>&#8211;async</i>] [<i>&#8211;verbose</i>]] [<i>&#8211;timeout</i> <code>seconds</code>] [<i>&#8211;active</i>] [{<i>&#8211;pivot</i> | <i>&#8211;keep-overlay</i>}]</dt>
<dd> Reduce the length of a backing image chain, by committing changes at the top of the chain (snapshot or delta files) into backing images. By default, this command attempts to flatten the entire chain. If <i>base</i> and/or <i>top</i> are specified as files within the backing chain, then the operation is constrained to committing just that portion of the chain; <i>&#8211;shallow</i> can be used instead of <i>base</i> to specify the immediate backing file of the resulting top image to be committed. The files being committed are rendered invalid, possibly as soon as the operation starts; using the <i>&#8211;delete</i> flag will attempt to remove these invalidated files at the successful completion of the commit operation. When the <i>&#8211;keep-relative</i> flag is used, the backing file paths will be kept relative. </dd>
<p> When <i>top</i> is omitted or specified as the active image, it is also possible to specify <i>&#8211;active</i> to trigger a two-phase active commit. In the first phase, <i>top</i> is copied into <i>base</i> and the job can only be canceled, with top still containing data not yet in base. In the second phase, <i>top</i> and <i>base</i> remain identical until a call to <code>blockjob</code> with the <i>&#8211;abort</i> flag (keeping top as the active image that tracks changes from that point in time) or the <i>&#8211;pivot</i> flag (making base the new active image and invalidating top). </p>
<p> By default, this command returns as soon as possible, and data for the entire disk is committed in the background; the progress of the operation can be checked with <code>blockjob</code>. However, if <i>&#8211;wait</i> is specified, then this command will block until the operation completes (or for <i>&#8211;active</i>, enters the second phase), or until the operation is canceled because the optional <i>timeout</i> in seconds elapses or SIGINT is sent (usually with <tt>&quot;Ctrl-C&quot;</tt>). Using <i>&#8211;verbose</i> along with <i>&#8211;wait</i> will produce periodic status updates. If job cancellation is triggered, <i>&#8211;async</i> will return control to the user as fast as possible, otherwise the command may continue to block a little while longer until the job is done cleaning up. Using <i>&#8211;pivot</i> is shorthand for combining <i>&#8211;active</i> <i>&#8211;wait</i> with an automatic <code>blockjob</code> <i>&#8211;pivot</i>; and using <i>&#8211;keep-overlay</i> is shorthand for combining <i>&#8211;active</i> <i>&#8211;wait</i> with an automatic <code>blockjob</code> <i>&#8211;abort</i>. </p>
<p> <i>path</i> specifies fully-qualified path of the disk; it corresponds to a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names). <i>bandwidth</i> specifies copying bandwidth limit in MiB/s, although for qemu, it may be non-zero only for an online domain. For further information on the <i>bandwidth</i> argument see the corresponding section for the <code>blockjob</code> command.</p>
<dt><code>blockcopy</code> <i>domain</i> <i>path</i> { <i>dest</i> [<i>format</i>] [<i>&#8211;blockdev</i>] | <i>&#8211;xml</i> <code>file</code> } [<i>&#8211;shallow</i>] [<i>&#8211;reuse-external</i>] [<i>bandwidth</i>] [<i>&#8211;wait</i> [<i>&#8211;async</i>] [<i>&#8211;verbose</i>]] [{<i>&#8211;pivot</i> | <i>&#8211;finish</i>}] [<i>&#8211;timeout</i> <code>seconds</code>] [<i>granularity</i>] [<i>buf-size</i>] [<i>&#8211;bytes</i>] [<i>&#8211;transient-job</i>]</dt>
<dd> Copy a disk backing image chain to a destination. Either <i>dest</i> as the destination file name, or <i>&#8211;xml</i> with the name of an XML file containing a top-level &lt;disk&gt; element describing the destination, must be present. Additionally, if <i>dest</i> is given, <i>format</i> should be specified to declare the format of the destination (if <i>format</i> is omitted, then libvirt will reuse the format of the source, or with <i>&#8211;reuse-external</i> will be forced to probe the destination format, which could be a potential security hole). The command supports <i>&#8211;raw</i> as a boolean flag synonym for <i>&#8211;format=raw</i>. When using <i>dest</i>, the destination is treated as a regular file unless <i>&#8211;blockdev</i> is used to signal that it is a block device. By default, this command flattens the entire chain; but if <i>&#8211;shallow</i> is specified, the copy shares the backing chain. </dd>
<p> If <i>&#8211;reuse-external</i> is specified, then the destination must exist and have sufficient space to hold the copy. If <i>&#8211;shallow</i> is used in conjunction with <i>&#8211;reuse-external</i> then the pre-created image must have guest visible contents identical to guest visible contents of the backing file of the original image. This may be used to modify the backing file names on the destination. </p>
<p> By default, the copy job runs in the background, and consists of two phases. Initially, the job must copy all data from the source, and during this phase, the job can only be canceled to revert back to the source disk, with no guarantees about the destination. After this phase completes, both the source and the destination remain mirrored until a call to <code>blockjob</code> with the <i>&#8211;abort</i> and <i>&#8211;pivot</i> flags pivots over to the copy, or a call without <i>&#8211;pivot</i> leaves the destination as a faithful copy of that point in time. However, if <i>&#8211;wait</i> is specified, then this command will block until the mirroring phase begins, or cancel the operation if the optional <i>timeout</i> in seconds elapses or SIGINT is sent (usually with <tt>&quot;Ctrl-C&quot;</tt>). Using <i>&#8211;verbose</i> along with <i>&#8211;wait</i> will produce periodic status updates. Using <i>&#8211;pivot</i> (similar to <code>blockjob</code> <i>&#8211;pivot</i>) or <i>&#8211;finish</i> (similar to <code>blockjob</code> <i>&#8211;abort</i>) implies <i>&#8211;wait</i>, and will additionally end the job cleanly rather than leaving things in the mirroring phase. If job cancellation is triggered by timeout or by <i>&#8211;finish</i>, <i>&#8211;async</i> will return control to the user as fast as possible, otherwise the command may continue to block a little while longer until the job has actually cancelled. </p>
<p> <i>path</i> specifies fully-qualified path of the disk. <i>bandwidth</i> specifies copying bandwidth limit in MiB/s. Specifying a negative value is interpreted as an unsigned long long value that might be essentially unlimited, but more likely would overflow; it is safer to use 0 for that purpose. For further information on the <i>bandwidth</i> argument see the corresponding section for the <code>blockjob</code> command. Specifying <i>granularity</i> allows fine-tuning of the granularity that will be copied when a dirty region is detected; larger values trigger less I/O overhead but may end up copying more data overall (the default value is usually correct); hypervisors may restrict this to be a power of two or fall within a certain range. Specifying <i>buf-size</i> will control how much data can be simultaneously in-flight during the copy; larger values use more memory but may allow faster completion (the default value is usually correct). </p>
<p> <i>&#8211;transient-job</i> allows to specify that the user does not require the job to be recovered if the VM crashes or is turned off before the job completes. This flag removes the restriction of copy jobs to transient domains if that restriction is applied by the hypervisor.</p>
<dt><code>blockpull</code> <i>domain</i> <i>path</i> [<i>bandwidth</i>] [<i>&#8211;bytes</i>] [<i>base</i>] [<i>&#8211;wait</i> [<i>&#8211;verbose</i>] [<i>&#8211;timeout</i> <code>seconds</code>] [<i>&#8211;async</i>]] [<i>&#8211;keep-relative</i>]</dt>
<dd> Populate a disk from its backing image chain. By default, this command flattens the entire chain; but if <i>base</i> is specified, containing the name of one of the backing files in the chain, then that file becomes the new backing file and only the intermediate portion of the chain is pulled. Once all requested data from the backing image chain has been pulled, the disk no longer depends on that portion of the backing chain. </dd>
<p> By default, this command returns as soon as possible, and data for the entire disk is pulled in the background; the progress of the operation can be checked with <code>blockjob</code>. However, if <i>&#8211;wait</i> is specified, then this command will block until the operation completes, or cancel the operation if the optional <i>timeout</i> in seconds elapses or SIGINT is sent (usually with <tt>&quot;Ctrl-C&quot;</tt>). Using <i>&#8211;verbose</i> along with <i>&#8211;wait</i> will produce periodic status updates. If job cancellation is triggered, <i>&#8211;async</i> will return control to the user as fast as possible, otherwise the command may continue to block a little while longer until the job is done cleaning up. </p>
<p> Using the <i>&#8211;keep-relative</i> flag will keep the backing chain names relative. </p>
<p> <i>path</i> specifies fully-qualified path of the disk; it corresponds to a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names). <i>bandwidth</i> specifies copying bandwidth limit in MiB/s. For further information on the <i>bandwidth</i> argument see the corresponding section for the <code>blockjob</code> command.</p>
<dt><code>blkdeviotune</code> <i>domain</i> <i>device</i> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]] [[<i>total-bytes-sec</i>] | [<i>read-bytes-sec</i>] [<i>write-bytes-sec</i>]] [[<i>total-iops-sec</i>] | [<i>read-iops-sec</i>] [<i>write-iops-sec</i>]] [[<i>total-bytes-sec-max</i>] | [<i>read-bytes-sec-max</i>] [<i>write-bytes-sec-max</i>]] [[<i>total-iops-sec-max</i>] | [<i>read-iops-sec-max</i>] [<i>write-iops-sec-max</i>]] [[<i>total-bytes-sec-max-length</i>] | [<i>read-bytes-sec-max-length</i>] [<i>write-bytes-sec-max-length</i>]] [[<i>total-iops-sec-max-length</i>] | [<i>read-iops-sec-max-length</i>] [<i>write-iops-sec-max-length</i>]] [<i>size-iops-sec</i>] [<i>group-name</i>]</dt>
<dd> Set or query the block disk io parameters for a block device of <i>domain</i>. <i>device</i> specifies a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names). </dd>
<p> If no limit is specified, it will query current I/O limits setting. Otherwise, alter the limits with these flags: <i>&#8211;total-bytes-sec</i> specifies total throughput limit as a scaled integer, the default being bytes per second if no suffix is specified. <i>&#8211;read-bytes-sec</i> specifies read throughput limit as a scaled integer, the default being bytes per second if no suffix is specified. <i>&#8211;write-bytes-sec</i> specifies write throughput limit as a scaled integer, the default being bytes per second if no suffix is specified. <i>&#8211;total-iops-sec</i> specifies total I/O operations limit per second. <i>&#8211;read-iops-sec</i> specifies read I/O operations limit per second. <i>&#8211;write-iops-sec</i> specifies write I/O operations limit per second. <i>&#8211;total-bytes-sec-max</i> specifies maximum total throughput limit as a scaled integer, the default being bytes per second if no suffix is specified <i>&#8211;read-bytes-sec-max</i> specifies maximum read throughput limit as a scaled integer, the default being bytes per second if no suffix is specified. <i>&#8211;write-bytes-sec-max</i> specifies maximum write throughput limit as a scaled integer, the default being bytes per second if no suffix is specified. <i>&#8211;total-iops-sec-max</i> specifies maximum total I/O operations limit per second. <i>&#8211;read-iops-sec-max</i> specifies maximum read I/O operations limit per second. <i>&#8211;write-iops-sec-max</i> specifies maximum write I/O operations limit per second. <i>&#8211;total-bytes-sec-max-length</i> specifies duration in seconds to allow maximum total throughput limit. <i>&#8211;read-bytes-sec-max-length</i> specifies duration in seconds to allow maximum read throughput limit. <i>&#8211;write-bytes-sec-max-length</i> specifies duration in seconds to allow maximum write throughput limit. <i>&#8211;total-iops-sec-max-length</i> specifies duration in seconds to allow maximum total I/O operations limit. <i>&#8211;read-iops-sec-max-length</i> specifies duration in seconds to allow maximum read I/O operations limit. <i>&#8211;write-iops-sec-max-length</i> specifies duration in seconds to allow maximum write I/O operations limit. <i>&#8211;size-iops-sec</i> specifies size I/O operations limit per second. <i>&#8211;group-name</i> specifies group name to share I/O quota between multiple drives. For a qemu domain, if no name is provided, then the default is to have a single group for each <i>device</i>. </p>
<p> Older versions of virsh only accepted these options with underscore instead of dash, as in <i>&#8211;total_bytes_sec</i>. </p>
<p> Bytes and iops values are independent, but setting only one value (such as &#8211;read-bytes-sec) resets the other two in that category to unlimited. An explicit 0 also clears any limit. A non-zero value for a given total cannot be mixed with non-zero values for read or write. </p>
<p> It is up to the hypervisor to determine how to handle the length values. For the qemu hypervisor, if an I/O limit value or maximum value is set, then the default value of 1 second will be displayed. Supplying a 0 will reset the value back to the default. </p>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. When setting the disk io parameters both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. For querying only one of <i>&#8211;live</i>, <i>&#8211;config</i> or <i>&#8211;current</i> can be specified. If no flag is specified, behavior is different depending on hypervisor.</p>
<dt><code>blockjob</code> <i>domain</i> <i>path</i> { [<i>&#8211;abort</i>] [<i>&#8211;async</i>] [<i>&#8211;pivot</i>] | [<i>&#8211;info</i>] [<i>&#8211;raw</i>] [<i>&#8211;bytes</i>] | [<i>bandwidth</i>] }</dt>
<dd> Manage active block operations. There are three mutually-exclusive modes: <i>&#8211;info</i>, <i>bandwidth</i>, and <i>&#8211;abort</i>. <i>&#8211;async</i> and <i>&#8211;pivot</i> imply abort mode; <i>&#8211;raw</i> implies info mode; and if no mode was given, <i>&#8211;info</i> mode is assumed. </dd>
<p> <i>path</i> specifies fully-qualified path of the disk; it corresponds to a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names). </p>
<p> In <i>&#8211;abort</i> mode, the active job on the specified disk will be aborted. If <i>&#8211;async</i> is also specified, this command will return immediately, rather than waiting for the cancellation to complete. If <i>&#8211;pivot</i> is specified, this requests that an active copy or active commit job be pivoted over to the new image. </p>
<p> In <i>&#8211;info</i> mode, the active job information on the specified disk will be printed. By default, the output is a single human-readable summary line; this format may change in future versions. Adding <i>&#8211;raw</i> lists each field of the struct, in a stable format. If the <i>&#8211;bytes</i> flag is set, then the command errors out if the server could not supply bytes/s resolution; when omitting the flag, raw output is listed in MiB/s and human-readable output automatically selects the best resolution supported by the server. </p>
<p> <i>bandwidth</i> can be used to set bandwidth limit for the active job in MiB/s. If <i>&#8211;bytes</i> is specified then the bandwidth value is interpreted in bytes/s. Specifying a negative value is interpreted as an unsigned long value or essentially unlimited. The hypervisor can choose whether to reject the value or convert it to the maximum value allowed. Optionally a scaled positive number may be used as bandwidth (see <code>NOTES</code> above). Using <i>&#8211;bytes</i> with a scaled value allows to use finer granularity. A scaled value used without <i>&#8211;bytes</i> will be rounded down to MiB/s. Note that the <i>&#8211;bytes</i> may be unsupported by the hypervisor.</p>
<dt><code>domblkthreshold</code> <i>domain</i> <i>dev</i> <i>threshold</i></dt>
<dd> Set the threshold value for delivering the block-threshold event. <i>dev</i> specifies the disk device target or backing chain element of given device using the &#8216;target[1]&#8217; syntax. <i>threshold</i> is a scaled value of the offset. If the block device should write beyond that offset the event will be delivered.</dd>
<dt><code>blockresize</code> <i>domain</i> <i>path</i> <i>size</i></dt>
<dd> Resize a block device of domain while the domain is running, <i>path</i> specifies the absolute path of the block device; it corresponds to a unique target name (&lt;target dev=&#8217;name&#8217;/&gt;) or source file (&lt;source file=&#8217;name&#8217;/&gt;) for one of the disk devices attached to <i>domain</i> (see also <code>domblklist</code> for listing these names). </dd>
<p> <i>size</i> is a scaled integer (see <code>NOTES</code> above) which defaults to KiB (blocks of 1024 bytes) if there is no suffix. You must use a suffix of &#8220;B&#8221; to get bytes (note that for historical reasons, this differs from <code>vol-resize</code> which defaults to bytes without a suffix).</p>
<dt><code>domdisplay</code> <i>domain</i> [<i>&#8211;include-password</i>] [[<i>&#8211;type</i>] <code>type</code>] [<i>&#8211;all</i>]</dt>
<dd> Output a URI which can be used to connect to the graphical display of the domain via VNC, SPICE or RDP.  The particular graphical display type can be selected using the <code>type</code> parameter (e.g. &#8220;vnc&#8221;, &#8220;spice&#8221;, &#8220;rdp&#8221;). If <i>&#8211;include-password</i> is specified, the SPICE channel password will be included in the URI. If <i>&#8211;all</i> is specified, then all show all possible graphical displays, for a VM could have more than one graphical displays.</dd>
<dt><code>domfsinfo</code> <i>domain</i></dt>
<dd> Show a list of mounted filesystems within the running domain. The list contains mountpoints, names of a mounted device in the guest, filesystem types, and unique target names used in the domain XML (&lt;target dev=&#8217;name&#8217;/&gt;). </dd>
<p> Note that this command requires a guest agent configured and running in the domain&#8217;s guest OS.</p>
<dt><code>domfsfreeze</code> <i>domain</i> [[<i>&#8211;mountpoint</i>] <code>mountpoint</code>&#8230;]</dt>
<dd> Freeze mounted filesystems within a running domain to prepare for consistent snapshots. </dd>
<p> The <i>&#8211;mountpoint</i> option takes a parameter <code>mountpoint</code>, which is a mount point path of the filesystem to be frozen. This option can occur multiple times. If this is not specified, every mounted filesystem is frozen. </p>
<p> Note: <code>snapshot-create</code> command has a <i>&#8211;quiesce</i> option to freeze and thaw the filesystems automatically to keep snapshots consistent. <code>domfsfreeze</code> command is only needed when a user wants to utilize the native snapshot features of storage devices not supported by libvirt.</p>
<dt><code>domfsthaw</code> <i>domain</i> [[<i>&#8211;mountpoint</i>] <code>mountpoint</code>&#8230;]</dt>
<dd> Thaw mounted filesystems within a running domain, which have been frozen by domfsfreeze command. </dd>
<p> The <i>&#8211;mountpoint</i> option takes a parameter <code>mountpoint</code>, which is a mount point path of the filesystem to be thawed. This option can occur multiple times. If this is not specified, every mounted filesystem is thawed.</p>
<dt><code>domfstrim</code> <i>domain</i> [<i>&#8211;minimum</i> <code>bytes</code>] [<i>&#8211;mountpoint mountPoint</i>]</dt>
<dd> Issue a fstrim command on all mounted filesystems within a running domain. It discards blocks which are not in use by the filesystem. If <i>&#8211;minimum</i> <code>bytes</code> is specified, it tells guest kernel length of contiguous free range. Smaller than this may be ignored (this is a hint and the guest may not respect it). By increasing this value, the fstrim operation will complete more quickly for filesystems with badly fragmented free space, although not all blocks will be discarded. The default value is zero, meaning &#8220;discard every free block&#8221;. Moreover, if a user wants to trim only one mount point, it can be specified via optional <i>&#8211;mountpoint</i> parameter.</dd>
<dt><code>domhostname</code> <i>domain</i></dt>
<dd> Returns the hostname of a domain, if the hypervisor makes it available.</dd>
<dt><code>dominfo</code> <i>domain</i></dt>
<dd> Returns basic information about the domain.</dd>
<dt><code>domuuid</code> <i>domain-name-or-id</i></dt>
<dd> Convert a domain name or id to domain UUID</dd>
<dt><code>domid</code> <i>domain-name-or-uuid</i></dt>
<dd> Convert a domain name (or UUID) to a domain id</dd>
<dt><code>domjobabort</code> <i>domain</i></dt>
<dd> Abort the currently running domain job.</dd>
<dt><code>domjobinfo</code> <i>domain</i> [<i>&#8211;completed</i>]</dt>
<dd> Returns information about jobs running on a domain. <i>&#8211;completed</i> tells virsh to return information about a recently finished job. Statistics of a completed job are automatically destroyed once read or when libvirtd is restarted. Note that time information returned for completed migrations may be completely irrelevant unless both source and destination hosts have synchronized time (i.e., NTP daemon is running on both of them).</dd>
<dt><code>domname</code> <i>domain-id-or-uuid</i></dt>
<dd> Convert a domain Id (or UUID) to domain name</dd>
<dt><code>domrename</code> <i>domain</i> <i>new-name</i></dt>
<dd> Rename a domain. This command changes current domain name to the new name specified in the second argument. </dd>
<p> <code>Note</code>: Domain must be inactive and without snapshots.</p>
<dt><code>domstate</code> <i>domain</i> [<i>&#8211;reason</i>]</dt>
<dd> Returns state about a domain. <i>&#8211;reason</i> tells virsh to also print reason for the state.</dd>
<dt><code>domcontrol</code> <i>domain</i></dt>
<dd> Returns state of an interface to VMM used to control a domain. For states other than &#8220;ok&#8221; or &#8220;error&#8221; the command also prints number of seconds elapsed since the control interface entered its current state.</dd>
<dt><code>domtime</code> <i>domain</i> { [<i>&#8211;now</i>] [<i>&#8211;pretty</i>] [<i>&#8211;sync</i>] [<i>&#8211;time</i> <code>time</code>] }</dt>
<dd> Gets or sets the domain&#8217;s system time. When run without any arguments (but <i>domain</i>), the current domain&#8217;s system time is printed out. The <i>&#8211;pretty</i> modifier can be used to print the time in more human readable form. </dd>
<p> When <i>&#8211;time</i> <code>time</code> is specified, the domain&#8217;s time is not gotten but set instead. The <i>&#8211;now</i> modifier acts like if it was an alias for <i>&#8211;time</i> $now, which means it sets the time that is currently on the host virsh is running at. In both cases (setting and getting), time is in seconds relative to Epoch of 1970-01-01 in UTC. The <i>&#8211;sync</i> modifies the set behavior a bit: The time passed is ignored, but the time to set is read from domain&#8217;s RTC instead. Please note, that some hypervisors may require a guest agent to be configured in order to get or set the guest time.</p>
<dt><code>domxml-from-native</code> <i>format</i> <i>config</i></dt>
<dd> Convert the file <i>config</i> in the native guest configuration format named by <i>format</i> to a domain XML format. For QEMU/KVM hypervisor, the <i>format</i> argument must be <code>qemu-argv</code>. For Xen hypervisor, the <i>format</i> argument may be <code>xen-xm</code>, <code>xen-xl</code>, or <code>xen-sxpr</code>. For LXC hypervisor, the <i>format</i> argument must be <code>lxc-tools</code>.</dd>
<dt><code>domxml-to-native</code> <i>format</i> <i>xml</i></dt>
<dd> Convert the file <i>xml</i> in domain XML format to the native guest configuration format named by <i>format</i>. For QEMU/KVM hypervisor, the <i>format</i> argument must be <code>qemu-argv</code>. For Xen hypervisor, the <i>format</i> argument may be <code>xen-xm</code>, <code>xen-xl</code>, or <code>xen-sxpr</code>. For LXC hypervisor, the <i>format</i> argument must be <code>lxc-tools</code>.</dd>
<dt><code>dump</code> <i>domain</i> <i>corefilepath</i> [<i>&#8211;bypass-cache</i>] { [<i>&#8211;live</i>] | [<i>&#8211;crash</i>] | [<i>&#8211;reset</i>] } [<i>&#8211;verbose</i>] [<i>&#8211;memory-only</i>] [<i>&#8211;format</i> <i>string</i>]</dt>
<dd> Dumps the core of a domain to a file for analysis. If <i>&#8211;live</i> is specified, the domain continues to run until the core dump is complete, rather than pausing up front. If <i>&#8211;crash</i> is specified, the domain is halted with a crashed status, rather than merely left in a paused state. If <i>&#8211;reset</i> is specified, the domain is reset after successful dump. Note, these three switches are mutually exclusive. If <i>&#8211;bypass-cache</i> is specified, the save will avoid the file system cache, although this may slow down the operation. If <i>&#8211;memory-only</i> is specified, the file is elf file, and will only include domain&#8217;s memory and cpu common register value. It is very useful if the domain uses host devices directly. <i>&#8211;format</i> <i>string</i> is used to specify the format of &#8216;memory-only&#8217; dump, and <i>string</i> can be one of them: elf, kdump-zlib(kdump-compressed format with zlib-compressed), kdump-lzo(kdump-compressed format with lzo-compressed), kdump-snappy(kdump-compressed format with snappy-compressed). </dd>
<p> The progress may be monitored using <code>domjobinfo</code> virsh command and canceled with <code>domjobabort</code> command (sent by another virsh instance). Another option is to send SIGINT (usually with <tt>&quot;Ctrl-C&quot;</tt>) to the virsh process running <code>dump</code> command. <i>&#8211;verbose</i> displays the progress of dump. </p>
<p> NOTE: Some hypervisors may require the user to manually ensure proper permissions on file and path specified by argument <i>corefilepath</i>. </p>
<p> NOTE: Crash dump in a old kvmdump format is being obsolete and cannot be loaded and processed by crash utility since its version 6.1.0. A &#8211;memory-only option is required in order to produce valid ELF file which can be later processed by the crash utility.</p>
<dt><code>dumpxml</code> <i>domain</i> [<i>&#8211;inactive</i>] [<i>&#8211;security-info</i>] [<i>&#8211;update-cpu</i>] [<i>&#8211;migratable</i>]</dt>
<dd> Output the domain information as an XML dump to stdout, this format can be used by the <code>create</code> command. Additional options affecting the XML dump may be used. <i>&#8211;inactive</i> tells virsh to dump domain configuration that will be used on next start of the domain as opposed to the current domain configuration. Using <i>&#8211;security-info</i> will also include security sensitive information in the XML dump. <i>&#8211;update-cpu</i> updates domain CPU requirements according to host CPU. With <i>&#8211;migratable</i> one can request an XML that is suitable for migrations, i.e., compatible with older libvirt releases and possibly amended with internal run-time options. This option may automatically enable other options (<i>&#8211;update-cpu</i>, <i>&#8211;security-info</i>, &#8230;) as necessary.</dd>
<dt><code>edit</code> <i>domain</i></dt>
<dd> Edit the XML configuration file for a domain, which will affect the next boot of the guest. </dd>
<p> This is equivalent to: </p>
<pre>
 virsh dumpxml --inactive --security-info domain &gt; domain.xml
 vi domain.xml (or make changes with your other text editor)
 virsh define domain.xml
</pre>
<p> except that it does some error checking. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>.</p>
<dt><code>event</code> {[<i>domain</i>] { <i>event</i> | <i>&#8211;all</i> } [<i>&#8211;loop</i>] [<i>&#8211;timeout</i> <i>seconds</i>] [<i>&#8211;timestamp</i>] | <i>&#8211;list</i>}</dt>
<dd> Wait for a class of domain events to occur, and print appropriate details of events as they happen. The events can optionally be filtered by <i>domain</i>. Using <i>&#8211;list</i> as the only argument will provide a list of possible <i>event</i> values known by this client, although the connection might not allow registering for all these events. It is also possible to use <i>&#8211;all</i> instead of <i>event</i> to register for all possible event types at once. </dd>
<p> By default, this command is one-shot, and returns success once an event occurs; you can send SIGINT (usually via <tt>&quot;Ctrl-C&quot;</tt>) to quit immediately. If <i>&#8211;timeout</i> is specified, the command gives up waiting for events after <i>seconds</i> have elapsed. With <i>&#8211;loop</i>, the command prints all events until a timeout or interrupt key. </p>
<p> When <i>&#8211;timestamp</i> is used, a human-readable timestamp will be printed before the event.</p>
<dt><code>iothreadinfo</code> <i>domain</i> [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Display basic domain IOThreads information including the IOThread ID and the CPU Affinity for each IOThread. </dd>
<p> If <i>&#8211;live</i> is specified, get the IOThreads data from the running guest. If the guest is not running, an error is returned. If <i>&#8211;config</i> is specified, get the IOThreads data from the next boot of a persistent guest. If <i>&#8211;current</i> is specified or <i>&#8211;live</i> and <i>&#8211;config</i> are not specified, then get the IOThread data based on the current guest state.</p>
<dt><code>iothreadpin</code> <i>domain</i> <i>iothread</i> <i>cpulist</i> [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Change the pinning of a domain IOThread to host physical CPUs. In order to retrieve a list of all IOThreads, use <code>iothreadinfo</code>. To pin an <i>iothread</i> specify the <i>cpulist</i> desired for the IOThread ID as listed in the <code>iothreadinfo</code> output. </dd>
<p> <i>cpulist</i> is a list of physical CPU numbers. Its syntax is a comma separated list and a special markup using &#8216;-&#8216; and &#8216;^&#8217; (ex. &#8216;0-4&#8217;, &#8216;0-3,^2&#8217;) can also be allowed. The &#8216;-&#8216; denotes the range and the &#8216;^&#8217; denotes exclusive. If you want to reset iothreadpin setting, that is, to pin an <i>iothread</i> to all physical cpus, simply specify &#8216;r&#8217; as a <i>cpulist</i>. </p>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If the guest is not running, an error is returned. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified or <i>&#8211;live</i> and <i>&#8211;config</i> are not specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given if <i>cpulist</i> is present, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor. </p>
<p> <code>Note</code>: The expression is sequentially evaluated, so &#8220;0-15,^8&#8221; is identical to &#8220;9-14,0-7,15&#8221; but not identical to &#8220;^8,0-15&#8221;.</p>
<dt><code>iothreadadd</code> <i>domain</i> <i>iothread_id</i> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Add a new IOThread to the domain using the specified <i>iothread_id</i>. If the <i>iothread_id</i> already exists, the command will fail. The <i>iothread_id</i> must be greater than zero. </dd>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If the guest is not running an error is returned. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified or <i>&#8211;live</i> and <i>&#8211;config</i> are not specified, affect the current guest state.</p>
<dt><code>iothreaddel</code> <i>domain</i> <i>iothread_id</i> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Delete an IOThread from the domain using the specified <i>iothread_id</i>. If an IOThread is currently assigned to a disk resource such as via the <code>attach-disk</code> command, then the attempt to remove the IOThread will fail. If the <i>iothread_id</i> does not exist an error will occur. </dd>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If the guest is not running an error is returned. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified or <i>&#8211;live</i> and <i>&#8211;config</i> are not specified, affect the current guest state.</p>
<dt><code>managedsave</code> <i>domain</i> [<i>&#8211;bypass-cache</i>] [{<i>&#8211;running</i> | <i>&#8211;paused</i>}] [<i>&#8211;verbose</i>]</dt>
<dd> Save and destroy (stop) a running domain, so it can be restarted from the same state at a later time. When the virsh <code>start</code> command is next run for the domain, it will automatically be started from this saved state. If <i>&#8211;bypass-cache</i> is specified, the save will avoid the file system cache, although this may slow down the operation. </dd>
<p> The progress may be monitored using <code>domjobinfo</code> virsh command and canceled with <code>domjobabort</code> command (sent by another virsh instance). Another option is to send SIGINT (usually with <tt>&quot;Ctrl-C&quot;</tt>) to the virsh process running <code>managedsave</code> command. <i>&#8211;verbose</i> displays the progress of save. </p>
<p> Normally, starting a managed save will decide between running or paused based on the state the domain was in when the save was done; passing either the <i>&#8211;running</i> or <i>&#8211;paused</i> flag will allow overriding which state the <code>start</code> should use. </p>
<p> The <code>dominfo</code> command can be used to query whether a domain currently has any managed save image.</p>
<dt><code>managedsave-remove</code> <i>domain</i></dt>
<dd> Remove the <code>managedsave</code> state file for a domain, if it exists. This ensures the domain will do a full boot the next time it is started.</dd>
<dt><code>maxvcpus</code> [<i>type</i>]</dt>
<dd> Provide the maximum number of virtual CPUs supported for a guest VM on this connection. If provided, the <i>type</i> parameter must be a valid type attribute for the &lt;domain&gt; element of XML.</dd>
<dt><code>cpu-stats</code> <i>domain</i> [<i>&#8211;total</i>] [<i>start</i>] [<i>count</i>]</dt>
<dd> Provide cpu statistics information of a domain. The domain should be running. Default it shows stats for all CPUs, and a total. Use <i>&#8211;total</i> for only the total stats, <i>start</i> for only the per-cpu stats of the CPUs from <i>start</i>, <i>count</i> for only <i>count</i> CPUs&#8217; stats.</dd>
<dt><code>metadata</code> <i>domain</i> [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] [<i>&#8211;edit</i>] [<i>uri</i>] [<i>key</i>] [<i>set</i>] [<i>&#8211;remove</i>]</dt>
<dd> Show or modify custom XML metadata of a domain. The metadata is a user defined XML that allows to store arbitrary XML data in the domain definition. Multiple separate custom metadata pieces can be stored in the domain XML. The pieces are identified by a private XML namespace provided via the <i>uri</i> argument. (See also <code>desc</code> that works with textual metadata of a domain.) </dd>
<p> Flags <i>&#8211;live</i> or <i>&#8211;config</i> select whether this command works on live or persistent definitions of the domain. If both <i>&#8211;live</i> and <i>&#8211;config</i> are specified, the <i>&#8211;config</i> option takes precedence on getting the current description and both live configuration and config are updated while setting the description. <i>&#8211;current</i> is exclusive and implied if none of these was specified. </p>
<p> Flag <i>&#8211;remove</i> specifies that the metadata element specified by the <i>uri</i> argument should be removed rather than updated. </p>
<p> Flag <i>&#8211;edit</i> specifies that an editor with the metadata identified by the <i>uri</i> argument should be opened and the contents saved back afterwards. Otherwise the new contents can be provided via the <i>set</i> argument. </p>
<p> When setting metadata via <i>&#8211;edit</i> or <i>set</i> the <i>key</i> argument must be specified and is used to prefix the custom elements to bind them to the private namespace. </p>
<p> If neither of <i>&#8211;edit</i> and <i>set</i> are specified the XML metadata corresponding to the <i>uri</i> namespace is displayed instead of being modified.</p>
<dt><code>migrate</code> [<i>&#8211;live</i>] [<i>&#8211;offline</i>] [<i>&#8211;direct</i>] [<i>&#8211;p2p</i> [<i>&#8211;tunnelled</i>]] [<i>&#8211;persistent</i>] [<i>&#8211;undefinesource</i>] [<i>&#8211;suspend</i>] [<i>&#8211;copy-storage-all</i>] [<i>&#8211;copy-storage-inc</i>] [<i>&#8211;change-protection</i>] [<i>&#8211;unsafe</i>] [<i>&#8211;verbose</i>] [<i>&#8211;rdma-pin-all</i>] [<i>&#8211;abort-on-error</i>] [<i>&#8211;postcopy</i>] [<i>&#8211;postcopy-after-precopy</i>] <i>domain</i> <i>desturi</i> [<i>migrateuri</i>] [<i>graphicsuri</i>] [<i>listen-address</i>] [<i>dname</i>] [<i>&#8211;timeout</i> <code>seconds</code> [<i>&#8211;timeout-suspend</i> | <i>&#8211;timeout-postcopy</i>]] [<i>&#8211;xml</i> <code>file</code>] [<i>&#8211;migrate-disks</i> <code>disk-list</code>] [<i>&#8211;disks-port</i> <code>port</code>] [<i>&#8211;compressed</i>] [<i>&#8211;comp-methods</i> <code>method-list</code>] [<i>&#8211;comp-mt-level</i>] [<i>&#8211;comp-mt-threads</i>] [<i>&#8211;comp-mt-dthreads</i>] [<i>&#8211;comp-xbzrle-cache</i>] [<i>&#8211;auto-converge</i>] [<i>auto-converge-initial</i>] [<i>auto-converge-increment</i>] [<i>&#8211;persistent-xml</i> <code>file</code>] [<i>&#8211;tls</i>]</dt>
<dd> Migrate domain to another host. Add <i>&#8211;live</i> for live migration; &lt;&#8211;p2p&gt; for peer-2-peer migration; <i>&#8211;direct</i> for direct migration; or <i>&#8211;tunnelled</i> for tunnelled migration. <i>&#8211;offline</i> migrates domain definition without starting the domain on destination and without stopping it on source host. Offline migration may be used with inactive domains and it must be used with <i>&#8211;persistent</i> option. <i>&#8211;persistent</i> leaves the domain persistent on destination host, <i>&#8211;undefinesource</i> undefines the domain on the source host, and <i>&#8211;suspend</i> leaves the domain paused on the destination host. <i>&#8211;copy-storage-all</i> indicates migration with non-shared storage with full disk copy, <i>&#8211;copy-storage-inc</i> indicates migration with non-shared storage with incremental copy (same base image shared between source and destination). In both cases the disk images have to exist on destination host, the <i>&#8211;copy-storage-&#8230;</i> options only tell libvirt to transfer data from the images on source host to the images found at the same place on the destination host. By default only non-shared non-readonly images are transferred. Use <i>&#8211;migrate-disks</i> to explicitly specify a list of disk targets to transfer via the comma separated <code>disk-list</code> argument. <i>&#8211;change-protection</i> enforces that no incompatible configuration changes will be made to the domain while the migration is underway; this flag is implicitly enabled when supported by the hypervisor, but can be explicitly used to reject the migration if the hypervisor lacks change protection support. <i>&#8211;verbose</i> displays the progress of migration. <i>&#8211;abort-on-error</i> cancels the migration if a soft error (for example I/O error) happens during the migration. <i>&#8211;postcopy</i> enables post-copy logic in migration, but does not actually start post-copy, i.e., migration is started in pre-copy mode. Once migration is running, the user may switch to post-copy using the <code>migrate-postcopy</code> command sent from another virsh instance or use <i>&#8211;postcopy-after-precopy</i> along with <i>&#8211;postcopy</i> to let libvirt automatically switch to post-copy after the first pass of pre-copy is finished. </dd>
<p> <i>&#8211;auto-converge</i> forces convergence during live migration. The initial guest CPU throttling rate can be set with <i>auto-converge-initial</i>. If the initial throttling rate is not enough to ensure convergence, the rate is periodically increased by <i>auto-converge-increment</i>. </p>
<p> <i>&#8211;rdma-pin-all</i> can be used with RDMA migration (i.e., when <i>migrateuri</i> starts with <a href="rdma://)">rdma://)</a> to tell the hypervisor to pin all domain&#8217;s memory at once before migration starts rather than letting it pin memory pages as needed. </p>
<p> <code>Note</code>: Individual hypervisors usually do not support all possible types of migration. For example, QEMU does not support direct migration. </p>
<p> In some cases libvirt may refuse to migrate the domain because doing so may lead to potential problems such as data corruption, and thus the migration is considered unsafe. For QEMU domain, this may happen if the domain uses disks without explicitly setting cache mode to &#8220;none&#8221;. Migrating such domains is unsafe unless the disk images are stored on coherent clustered filesystem, such as GFS2 or GPFS. If you are sure the migration is safe or you just do not care, use <i>&#8211;unsafe</i> to force the migration. </p>
<p> <i>dname</i> is used for renaming the domain to new name during migration, which also usually can be omitted. Likewise, <i>&#8211;xml</i> <code>file</code> is usually omitted, but can be used to supply an alternative XML file for use on the destination to supply a larger set of changes to any host-specific portions of the domain XML, such as accounting for naming differences between source and destination in accessing underlying storage. If <i>&#8211;persistent</i> is enabled, <i>&#8211;persistent-xml</i> <code>file</code> can be used to supply an alternative XML file which will be used as the persistent domain definition on the destination host. </p>
<p> <i>&#8211;timeout</i> <code>seconds</code> tells virsh to run a specified action when live migration exceeds that many seconds. It can only be used with <i>&#8211;live</i>. If <i>&#8211;timeout-suspend</i> is specified, the domain will be suspended after the timeout and the migration will complete offline; this is the default if no <i>&#8211;timeout-*</i> option is specified on the command line. When <i>&#8211;timeout-postcopy</i> is used, virsh will switch migration from pre-copy to post-copy upon timeout; migration has to be started with <i>&#8211;postcopy</i> option for this to work. </p>
<p> <i>&#8211;compressed</i> activates compression, the compression method is chosen with <i>&#8211;comp-methods</i>. Supported methods are &#8220;mt&#8221; and &#8220;xbzrle&#8221; and can be used in any combination. When no methods are specified, a hypervisor default methods will be used. QEMU defaults to &#8220;xbzrle&#8221;. Compression methods can be tuned further. <i>&#8211;comp-mt-level</i> sets compression level. Values are in range from 0 to 9, where 1 is maximum speed and 9 is maximum compression. <i>&#8211;comp-mt-threads</i> and <i>&#8211;comp-mt-dthreads</i> set the number of compress threads on source and the number of decompress threads on target respectively. <i>&#8211;comp-xbzrle-cache</i> sets size of page cache in bytes. </p>
<p> Providing <i>&#8211;tls</i> causes the migration to use the host configured TLS setup (see migrate_tls_x509_cert_dir in /etc/libvirt/qemu.conf) in order to perform the migration of the domain. Usage requires proper TLS setup for both source and target. </p>
<p> Running migration can be canceled by interrupting virsh (usually using <tt>&quot;Ctrl-C&quot;</tt>) or by <code>domjobabort</code> command sent from another virsh instance. </p>
<p> The <i>desturi</i> and <i>migrateuri</i> parameters can be used to control which destination the migration uses. <i>desturi</i> is important for managed migration, but unused for direct migration; <i>migrateuri</i> is required for direct migration, but can usually be automatically determined for managed migration. </p>
<p> <code>Note</code>: The <i>desturi</i> parameter for normal migration and peer2peer migration has different semantics:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> normal migration: the <i>desturi</i> is an address of the target host as seen from the client machine.</dd>
<dt>&bull;</dt>
<dd> peer2peer migration: the <i>desturi</i> is an address of the target host as seen from the source machine.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> When <i>migrateuri</i> is not specified, libvirt will automatically determine the hypervisor specific URI.  Some hypervisors, including QEMU, have an optional &#8220;migration_host&#8221; configuration parameter (useful when the host has multiple network interfaces). If this is unspecified, libvirt determines a name by looking up the target host&#8217;s configured hostname. </p>
<p> There are a few scenarios where specifying <i>migrateuri</i> may help:</p>
</dd><dl>
<dt>&bull;</dt>
<dd> The configured hostname is incorrect, or DNS is broken. If a host has a hostname which will not resolve to match one of its public IP addresses, then libvirt will generate an incorrect URI.  In this case <i>migrateuri</i> should be explicitly specified, using an IP address, or a correct hostname.</dd>
<dt>&bull;</dt>
<dd> The host has multiple network interfaces. If a host has multiple network interfaces, it might be desirable for the migration data stream to be sent over a specific interface for either security or performance reasons. In this case <i>migrateuri</i> should be explicitly specified, using an IP address associated with the network to be used.</dd>
<dt>&bull;</dt>
<dd> The firewall restricts what ports are available. When libvirt generates a migration URI, it will pick a port number using hypervisor specific rules. Some hypervisors only require a single port to be open in the firewalls, while others require a whole range of port numbers. In the latter case <i>migrateuri</i> might be specified to choose a specific port number outside the default range in order to comply with local firewall policies.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> See &lt;<a rel="nofollow" href="http://libvirt.org/migration.html#uris">http://libvirt.org/migration.html#uris</a>&gt; for more details on migration URIs. </p>
<p> Optional <i>graphicsuri</i> overrides connection parameters used for automatically reconnecting a graphical clients at the end of migration. If omitted, libvirt will compute the parameters based on target host IP address. In case the client does not have a direct access to the network virtualization hosts are connected to and needs to connect through a proxy, <i>graphicsuri</i> may be used to specify the address the client should connect to. The URI is formed as follows: </p>
<p>protocol: // hostname[:port]/[?parameters]</p>
<p> where protocol is either &#8220;spice&#8221; or &#8220;vnc&#8221; and parameters is a list of protocol specific parameters separated by &#8216;&amp;&#8217;. Currently recognized parameters are &#8220;tlsPort&#8221; and &#8220;tlsSubject&#8221;. For example, </p>
<pre>
    <a href="spice://target.host.com:1234/?tlsPort=4567">spice://target.host.com:1234/?tlsPort=4567</a>
</pre>
<p> Optional <i>listen-address</i> sets the listen address that hypervisor on the destination side should bind to for incoming migration. Both IPv4 and IPv6 addresses are accepted as well as hostnames (the resolving is done on destination). Some hypervisors do not support this feature and will return an error if this parameter is used. </p>
<p> Optional <i>disks-port</i> sets the port that hypervisor on destination side should bind to for incoming disks traffic. Currently it is supported only by qemu.</dd></dl>
<dt><code>migrate-setmaxdowntime</code> <i>domain</i> <i>downtime</i></dt>
<dd> Set maximum tolerable downtime for a domain which is being live-migrated to another host. The <i>downtime</i> is a number of milliseconds the guest is allowed to be down at the end of live migration.</dd>
<dt><code>migrate-compcache</code> <i>domain</i> [<i>&#8211;size</i> <code>bytes</code>]</dt>
<dd> Sets and/or gets size of the cache (in bytes) used for compressing repeatedly transferred memory pages during live migration. When called without <i>size</i>, the command just prints current size of the compression cache. When <i>size</i> is specified, the hypervisor is asked to change compression cache to <i>size</i> bytes and then the current size is printed (the result may differ from the requested size due to rounding done by the hypervisor). The <i>size</i> option is supposed to be used while the domain is being live-migrated as a reaction to migration progress and increasing number of compression cache misses obtained from domjobinfo.</dd>
<dt><code>migrate-setspeed</code> <i>domain</i> <i>bandwidth</i></dt>
<dd> Set the maximum migration bandwidth (in MiB/s) for a domain which is being migrated to another host. <i>bandwidth</i> is interpreted as an unsigned long long value. Specifying a negative value results in an essentially unlimited value being provided to the hypervisor. The hypervisor can choose whether to reject the value or convert it to the maximum value allowed.</dd>
<dt><code>migrate-getspeed</code> <i>domain</i></dt>
<dd> Get the maximum migration bandwidth (in MiB/s) for a domain.</dd>
<dt><code>migrate-postcopy</code> <i>domain</i></dt>
<dd> Switch the current migration from pre-copy to post-copy. This is only supported for a migration started with <i>&#8211;postcopy</i> option.</dd>
<dt><code>numatune</code> <i>domain</i> [<i>&#8211;mode</i> <code>mode</code>] [<i>&#8211;nodeset</i> <code>nodeset</code>] [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Set or get a domain&#8217;s numa parameters, corresponding to the &lt;numatune&gt; element of domain XML.  Without flags, the current settings are displayed. </dd>
<p> <i>mode</i> can be one of `strict&#8217;, `interleave&#8217; and `preferred&#8217; or any valid number from the virDomainNumatuneMemMode enum in case the daemon supports it. For a running domain, the mode can&#8217;t be changed, and the nodeset can be changed only if the domain was started with a mode of `strict&#8217;. </p>
<p> <i>nodeset</i> is a list of numa nodes used by the host for running the domain. Its syntax is a comma separated list, with &#8216;-&#8216; for ranges and &#8216;^&#8217; for excluding a node. </p>
<p> If <i>&#8211;live</i> is specified, set scheduler information of a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state.</p>
<dt><code>reboot</code> <i>domain</i> [<i>&#8211;mode MODE-LIST</i>]</dt>
<dd> Reboot a domain. This acts just as if the domain had the <code>reboot</code> command run from the console. The command returns as soon as it has executed the reboot action, which may be significantly before the domain actually reboots. </dd>
<p> The exact behavior of a domain when it reboots is set by the <i>on_reboot</i> parameter in the domain&#8217;s XML definition. </p>
<p> By default the hypervisor will try to pick a suitable shutdown method. To specify an alternative method, the <i>&#8211;mode</i> parameter can specify a comma separated list which includes <tt>&quot;acpi&quot;</tt>, <tt>&quot;agent&quot;</tt>, <tt>&quot;initctl&quot;</tt>, <tt>&quot;signal&quot;</tt> and <tt>&quot;paravirt&quot;</tt>. The order in which drivers will try each mode is undefined, and not related to the order specified to virsh. For strict control over ordering, use a single mode at a time and repeat the command.</p>
<dt><code>reset</code> <i>domain</i></dt>
<dd> Reset a domain immediately without any guest shutdown. <code>reset</code> emulates the power reset button on a machine, where all guest hardware sees the RST line set and reinitializes internal state. </dd>
<p> <code>Note</code>: Reset without any guest OS shutdown risks data loss.</p>
<dt><code>restore</code> <i>state-file</i> [<i>&#8211;bypass-cache</i>] [<i>&#8211;xml</i> <code>file</code>] [{<i>&#8211;running</i> | <i>&#8211;paused</i>}]</dt>
<dd> Restores a domain from a <code>virsh save</code> state file. See <i>save</i> for more info. </dd>
<p> If <i>&#8211;bypass-cache</i> is specified, the restore will avoid the file system cache, although this may slow down the operation. </p>
<p> <i>&#8211;xml</i> <code>file</code> is usually omitted, but can be used to supply an alternative XML file for use on the restored guest with changes only in the host-specific portions of the domain XML.  For example, it can be used to account for file naming differences in underlying storage due to disk snapshots taken after the guest was saved. </p>
<p> Normally, restoring a saved image will use the state recorded in the save image to decide between running or paused; passing either the <i>&#8211;running</i> or <i>&#8211;paused</i> flag will allow overriding which state the domain should be started in. </p>
<p> <code>Note</code>: To avoid corrupting file system contents within the domain, you should not reuse the saved state file for a second <code>restore</code> unless you have also reverted all storage volumes back to the same contents as when the state file was created.</p>
<dt><code>save</code> <i>domain</i> <i>state-file</i> [<i>&#8211;bypass-cache</i>] [<i>&#8211;xml</i> <code>file</code>] [{<i>&#8211;running</i> | <i>&#8211;paused</i>}] [<i>&#8211;verbose</i>]</dt>
<dd> Saves a running domain (RAM, but not disk state) to a state file so that it can be restored later. Once saved, the domain will no longer be running on the system, thus the memory allocated for the domain will be free for other domains to use. <code>virsh restore</code> restores from this state file. If <i>&#8211;bypass-cache</i> is specified, the save will avoid the file system cache, although this may slow down the operation. </dd>
<p> The progress may be monitored using <code>domjobinfo</code> virsh command and canceled with <code>domjobabort</code> command (sent by another virsh instance). Another option is to send SIGINT (usually with <tt>&quot;Ctrl-C&quot;</tt>) to the virsh process running <code>save</code> command. <i>&#8211;verbose</i> displays the progress of save. </p>
<p> This is roughly equivalent to doing a hibernate on a running computer, with all the same limitations. Open network connections may be severed upon restore, as TCP timeouts may have expired. </p>
<p> <i>&#8211;xml</i> <code>file</code> is usually omitted, but can be used to supply an alternative XML file for use on the restored guest with changes only in the host-specific portions of the domain XML.  For example, it can be used to account for file naming differences that are planned to be made via disk snapshots of underlying storage after the guest is saved. </p>
<p> Normally, restoring a saved image will decide between running or paused based on the state the domain was in when the save was done; passing either the <i>&#8211;running</i> or <i>&#8211;paused</i> flag will allow overriding which state the <code>restore</code> should use. </p>
<p> Domain saved state files assume that disk images will be unchanged between the creation and restore point. For a more complete system restore point, where the disk state is saved alongside the memory state, see the <code>snapshot</code> family of commands.</p>
<dt><code>save-image-define</code> <i>file</i> <i>xml</i> [{<i>&#8211;running</i> | <i>&#8211;paused</i>}]</dt>
<dd> Update the domain XML that will be used when <i>file</i> is later used in the <code>restore</code> command. The <i>xml</i> argument must be a file name containing the alternative XML, with changes only in the host-specific portions of the domain XML.  For example, it can be used to account for file naming differences resulting from creating disk snapshots of underlying storage after the guest was saved. </dd>
<p> The save image records whether the domain should be restored to a running or paused state. Normally, this command does not alter the recorded state; passing either the <i>&#8211;running</i> or <i>&#8211;paused</i> flag will allow overriding which state the <code>restore</code> should use.</p>
<dt><code>save-image-dumpxml</code> <i>file</i> [<i>&#8211;security-info</i>]</dt>
<dd> Extract the domain XML that was in effect at the time the saved state file <i>file</i> was created with the <code>save</code> command. Using <i>&#8211;security-info</i> will also include security sensitive information.</dd>
<dt><code>save-image-edit</code> <i>file</i> [{<i>&#8211;running</i> | <i>&#8211;paused</i>}]</dt>
<dd> Edit the XML configuration associated with a saved state file <i>file</i> created by the <code>save</code> command. </dd>
<p> The save image records whether the domain should be restored to a running or paused state. Normally, this command does not alter the recorded state; passing either the <i>&#8211;running</i> or <i>&#8211;paused</i> flag will allow overriding which state the <code>restore</code> should use. </p>
<p> This is equivalent to: </p>
<pre>
 virsh save-image-dumpxml state-file &gt; state-file.xml
 vi state-file.xml (or make changes with your other text editor)
 virsh save-image-define state-file state-file-xml
</pre>
<p> except that it does some error checking. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>.</p>
<dt><code>schedinfo</code> <i>domain</i> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]] [[<i>&#8211;set</i>] <code>parameter=value</code>]&#8230;</dt>
<dd>
</dd><dt><code>schedinfo</code> [<i>&#8211;weight</i> <code>number</code>] [<i>&#8211;cap</i> <code>number</code>] <i>domain</i></dt>
<dd> Allows you to show (and set) the domain scheduler parameters. The parameters available for each hypervisor are: </dd>
<p> LXC (posix scheduler) : cpu_shares, vcpu_period, vcpu_quota </p>
<p> QEMU/KVM (posix scheduler): cpu_shares, vcpu_period, vcpu_quota, emulator_period, emulator_quota, iothread_quota, iothread_period </p>
<p> Xen (credit scheduler): weight, cap </p>
<p> ESX (allocation scheduler): reservation, limit, shares </p>
<p> If <i>&#8211;live</i> is specified, set scheduler information of a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. </p>
<p> <code>Note</code>: The cpu_shares parameter has a valid value range of 0-262144; Negative values are wrapped to positive, and larger values are capped at the maximum. Therefore, -1 is a useful shorthand for 262144. On the Linux kernel, the values 0 and 1 are automatically converted to a minimal value of 2. </p>
<p> <code>Note</code>: The weight and cap parameters are defined only for the XEN_CREDIT scheduler. </p>
<p> <code>Note</code>: The vcpu_period, emulator_period, and iothread_period parameters have a valid value range of 1000-1000000 or 0, and the vcpu_quota, emulator_quota, and iothread_quota parameters have a valid value range of 1000-18446744073709551 or less than 0. The value 0 for either parameter is the same as not specifying that parameter.</p>
<dt><code>screenshot</code> <i>domain</i> [<i>imagefilepath</i>] [<i>&#8211;screen</i> <code>screenID</code>]</dt>
<dd> Takes a screenshot of a current domain console and stores it into a file. Optionally, if hypervisor supports more displays for a domain, <i>screenID</i> allows to specify which screen will be captured. It is the sequential number of screen. In case of multiple graphics cards, heads are enumerated before devices, e.g. having two graphics cards, both with four heads, screen ID 5 addresses the second head on the second card.</dd>
<dt><code>send-key</code> <i>domain</i> [<i>&#8211;codeset</i> <code>codeset</code>] [<i>&#8211;holdtime</i> <code>holdtime</code>] <i>keycode</i>&#8230;</dt>
<dd> Parse the <i>keycode</i> sequence as keystrokes to send to <i>domain</i>. Each <i>keycode</i> can either be a numeric value or a symbolic name from the corresponding codeset. If <i>&#8211;holdtime</i> is given, each keystroke will be held for that many milliseconds. The default codeset is <code>linux</code>, but use of the <i>&#8211;codeset</i> option allows other codesets to be chosen. </dd>
<p> If multiple keycodes are specified, they are all sent simultaneously to the guest, and they may be received in random order. If you need distinct keypresses, you must use multiple send-key invocations.</p>
<dl>
<dl>
<dt><code>linux</code></dt>
<dd> The numeric values are those defined by the Linux generic input event subsystem. The symbolic names match the corresponding Linux key constant macro names.</dd>
<dt><code>xt</code></dt>
<dd> The numeric values are those defined by the original XT keyboard controller. No symbolic names are provided</dd>
<dt><code>atset1</code></dt>
<dd> The numeric values are those defined by the AT keyboard controller, set 1 (aka XT compatible set). Extended keycoes from <code>atset1</code> may differ from extended keycodes in the <code>xt</code> codeset. No symbolic names are provided</dd>
<dt><code>atset2</code></dt>
<dd> The numeric values are those defined by the AT keyboard controller, set 2. No symbolic names are provided</dd>
<dt><code>atset3</code></dt>
<dd> The numeric values are those defined by the AT keyboard controller, set 3 (aka PS/2 compatible set). No symbolic names are provided</dd>
<dt><code>os_x</code></dt>
<dd> The numeric values are those defined by the OS-X keyboard input subsystem. The symbolic names match the corresponding OS-X key constant macro names</dd>
<dt><code>xt_kbd</code></dt>
<dd> The numeric values are those defined by the Linux KBD device. These are a variant on the original XT codeset, but often with different encoding for extended keycodes. No symbolic names are provided.</dd>
<dt><code>win32</code></dt>
<dd> The numeric values are those defined by the Win32 keyboard input subsystem. The symbolic names match the corresponding Win32 key constant macro names</dd>
<dt><code>usb</code></dt>
<dd> The numeric values are those defined by the USB HID specification for keyboard input. No symbolic names are provided</dd>
<dt><code>rfb</code></dt>
<dd> The numeric values are those defined by the RFB extension for sending raw keycodes. These are a variant on the XT codeset, but extended keycodes have the low bit of the second byte set, instead of the high bit of the first byte. No symbolic names are provided.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <code>Examples</code><br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>send three strokes&nbsp;<wbr>&#8216;k&#8217;,&nbsp;<wbr>&#8216;e&#8217;,&nbsp;<wbr>&#8216;y&#8217;, using xt codeset. these<br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>are all pressed simultaneously and may be received by the guest<br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>in random order<br/>
&nbsp;<wbr>&nbsp;<wbr>virsh send-key dom &#8211;codeset xt 37 18 21 </p>
<pre>
  # send one stroke 'right-ctrl+C'
  virsh send-key dom KEY_RIGHTCTRL KEY_C
  # send a tab, held for 1 second
  virsh send-key --holdtime 1000 0xf
</pre>
</dd></dl>
<dt><code>send-process-signal</code> <i>domain-id</i> <i>pid</i> <i>signame</i></dt>
<dd> Send a signal <i>signame</i> to the process identified by <i>pid</i> running in the virtual domain <i>domain-id</i>. The <i>pid</i> is a process ID in the virtual domain namespace. </dd>
<p> The <i>signame</i> argument may be either an integer signal constant number, or one of the symbolic names: </p>
<pre>
    &quot;nop&quot;, &quot;hup&quot;, &quot;int&quot;, &quot;quit&quot;, &quot;ill&quot;,
    &quot;trap&quot;, &quot;abrt&quot;, &quot;bus&quot;, &quot;fpe&quot;, &quot;kill&quot;,
    &quot;usr1&quot;, &quot;segv&quot;, &quot;usr2&quot;, &quot;pipe&quot;, &quot;alrm&quot;,
    &quot;term&quot;, &quot;stkflt&quot;, &quot;chld&quot;, &quot;cont&quot;, &quot;stop&quot;,
    &quot;tstp&quot;, &quot;ttin&quot;, &quot;ttou&quot;, &quot;urg&quot;, &quot;xcpu&quot;,
    &quot;xfsz&quot;, &quot;vtalrm&quot;, &quot;prof&quot;, &quot;winch&quot;, &quot;poll&quot;,
    &quot;pwr&quot;, &quot;sys&quot;, &quot;rt0&quot;, &quot;rt1&quot;, &quot;rt2&quot;, &quot;rt3&quot;,
    &quot;rt4&quot;, &quot;rt5&quot;, &quot;rt6&quot;, &quot;rt7&quot;, &quot;rt8&quot;, &quot;rt9&quot;,
    &quot;rt10&quot;, &quot;rt11&quot;, &quot;rt12&quot;, &quot;rt13&quot;, &quot;rt14&quot;, &quot;rt15&quot;,
    &quot;rt16&quot;, &quot;rt17&quot;, &quot;rt18&quot;, &quot;rt19&quot;, &quot;rt20&quot;, &quot;rt21&quot;,
    &quot;rt22&quot;, &quot;rt23&quot;, &quot;rt24&quot;, &quot;rt25&quot;, &quot;rt26&quot;, &quot;rt27&quot;,
    &quot;rt28&quot;, &quot;rt29&quot;, &quot;rt30&quot;, &quot;rt31&quot;, &quot;rt32&quot;
</pre>
<p> The symbol name may optionally be prefixed with &#8216;sig&#8217; or &#8216;sig_&#8217; and may be in uppercase or lowercase. </p>
<p> <code>Examples</code><br/>
&nbsp;<wbr>&nbsp;<wbr>virsh send-process-signal myguest 1 15<br/>
&nbsp;<wbr>&nbsp;<wbr>virsh send-process-signal myguest 1 term<br/>
&nbsp;<wbr>&nbsp;<wbr>virsh send-process-signal myguest 1 sigterm<br/>
&nbsp;<wbr>&nbsp;<wbr>virsh send-process-signal myguest 1&nbsp;<wbr>SIG_HUP</p>
<dt><code>setmem</code> <i>domain</i> <code>size</code> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Change the memory allocation for a guest domain. If <i>&#8211;live</i> is specified, perform a memory balloon of a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor. </dd>
<p> <i>size</i> is a scaled integer (see <code>NOTES</code> above); it defaults to kibibytes (blocks of 1024 bytes) unless you provide a suffix (and the older option name <i>&#8211;kilobytes</i> is available as a deprecated synonym) . Libvirt rounds up to the nearest kibibyte. Some hypervisors require a larger granularity than KiB, and requests that are not an even multiple will be rounded up. For example, vSphere/ESX rounds the parameter up to mebibytes (1024 kibibytes). </p>
<p> For Xen, you can only adjust the memory of a running domain if the domain is paravirtualized or running the PV balloon driver. </p>
<p> For LXC, the value being set is the cgroups value for limit_in_bytes or the maximum amount of user memory (including file cache). When viewing memory inside the container, this is the /proc/meminfo &#8220;MemTotal&#8221; value. When viewing the value from the host, use the <code>virsh memtune</code> command. In order to view the current memory in use and the maximum value allowed to set memory, use the <code>virsh dominfo</code> command.</p>
<dt><code>set-user-password</code> <i>domain</i> <i>user</i> <i>password</i> [<i>&#8211;encrypted</i>]</dt>
<dd> Set the password for the <i>user</i> account in the guest domain. </dd>
<p> If <i>&#8211;encrypted</i> is specified, the password is assumed to be already encrypted by the method required by the guest OS. </p>
<p> For QEMU/KVM, this requires the guest agent to be configured and running.</p>
<dt><code>setmaxmem</code> <i>domain</i> <code>size</code> [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Change the maximum memory allocation limit for a guest domain. If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor. </dd>
<p> Some hypervisors such as QEMU/KVM don&#8217;t support live changes (especially increasing) of the maximum memory limit. Even persistent configuration changes might not be performed with some hypervisors/configuration (e.g. on NUMA enabled domains on QEMU). For complex configuration changes use command <code>edit</code> instead). </p>
<p> <i>size</i> is a scaled integer (see <code>NOTES</code> above); it defaults to kibibytes (blocks of 1024 bytes) unless you provide a suffix (and the older option name <i>&#8211;kilobytes</i> is available as a deprecated synonym) . Libvirt rounds up to the nearest kibibyte. Some hypervisors require a larger granularity than KiB, and requests that are not an even multiple will be rounded up. For example, vSphere/ESX rounds the parameter up to mebibytes (1024 kibibytes).</p>
<dt><code>memtune</code> <i>domain</i> [<i>&#8211;hard-limit</i> <code>size</code>] [<i>&#8211;soft-limit</i> <code>size</code>] [<i>&#8211;swap-hard-limit</i> <code>size</code>] [<i>&#8211;min-guarantee</i> <code>size</code>] [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Allows you to display or set the domain memory parameters. Without flags, the current settings are displayed; with a flag, the appropriate limit is adjusted if supported by the hypervisor. LXC and QEMU/KVM support <i>&#8211;hard-limit</i>, <i>&#8211;soft-limit</i>, and <i>&#8211;swap-hard-limit</i>. <i>&#8211;min-guarantee</i> is supported only by ESX hypervisor. Each of these limits are scaled integers (see <code>NOTES</code> above), with a default of kibibytes (blocks of 1024 bytes) if no suffix is present. Libvirt rounds up to the nearest kibibyte. Some hypervisors require a larger granularity than KiB, and requests that are not an even multiple will be rounded up. For example, vSphere/ESX rounds the parameter up to mebibytes (1024 kibibytes). </dd>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor. </p>
<p> For QEMU/KVM, the parameters are applied to the QEMU process as a whole. Thus, when counting them, one needs to add up guest RAM, guest video RAM, and some memory overhead of QEMU itself. The last piece is hard to determine so one needs guess and try. </p>
<p> For LXC, the displayed hard_limit value is the current memory setting from the XML or the results from a <code>virsh setmem</code> command.</p>
<dl>
<dl>
<dt><i>&#8211;hard-limit</i></dt>
<dd> The maximum memory the guest can use.</dd>
<dt><i>&#8211;soft-limit</i></dt>
<dd> The memory limit to enforce during memory contention.</dd>
<dt><i>&#8211;swap-hard-limit</i></dt>
<dd> The maximum memory plus swap the guest can use. This has to be more than hard-limit value provided.</dd>
<dt><i>&#8211;min-guarantee</i></dt>
<dd> The guaranteed minimum memory allocation for the guest.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Specifying -1 as a value for these limits is interpreted as unlimited.</dd></dl>
<dt><code>perf</code> <i>domain</i> [<i>&#8211;enable</i> <code>eventSpec</code>] [<i>&#8211;disable</i> <code>eventSpec</code>] [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Get the current perf events setting or enable/disable specific perf events for a guest domain. </dd>
<p> Perf is a performance analyzing tool in Linux, and it can instrument CPU performance counters, tracepoints, kprobes, and uprobes (dynamic tracing). Perf supports a list of measurable events, and can measure events coming from different sources. For instance, some event are pure kernel counters, in this case they are called software events, including context-switches, minor-faults, etc.. Now dozens of events from different sources can be supported by perf. </p>
<p> Currently only QEMU/KVM supports this command. The <i>&#8211;enable</i> and <i>&#8211;disable</i> option combined with <code>eventSpec</code> can be used to enable or disable specific performance event. <code>eventSpec</code> is a string list of one or more events separated by commas. Valid event names are as follows: </p>
<p> <code>Valid perf event names</code><br/>
&nbsp;<wbr>&nbsp;<wbr>cmt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; A PQos&nbsp;<wbr>(Platform Qos)&nbsp;<wbr>feature to monitor the<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>usage of cache by applications running on the<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>mbmt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides a way to monitor the total system<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>memory bandwidth between one level of cache<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and another.<br/>
&nbsp;<wbr>&nbsp;<wbr>mbml&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides a way to limit the amount of data<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bytes/s)&nbsp;<wbr>send through the memory controller<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on the socket.<br/>
&nbsp;<wbr>&nbsp;<wbr>cache_misses&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides the count of cache misses by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>cache_references &#8211; Provides the count of cache hits by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on th e platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>instructions&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides the count of instructions executed<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>cpu_cycles&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides the count of cpu cycles<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(total/elapsed). May be used with<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instructions in order to get a cycles<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>per instruction.<br/>
&nbsp;<wbr>&nbsp;<wbr>branch_instructions &#8211; Provides the count of branch instructions<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>executed by applications running on the<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>branch_misses&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides the count of branch misses executed<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>bus_cycles&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Provides the count of bus cycles executed<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>stalled_cycles_frontend &#8211; Provides the count of stalled cpu<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cycles in the frontend of the<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instruction processor pipeline by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>stalled_cycles_backend &#8211; Provides the count of stalled cpu<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cycles in the backend of the<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instruction processor pipeline by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>ref_cpu_cycles&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>Provides the count of total cpu cycles<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>not affected by&nbsp;<wbr>CPU&nbsp;<wbr>frequency scaling by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>cpu_clock &#8211; Provides the cpu clock time consumed by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>task_clock &#8211; Provides the task clock time consumed by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>page_faults &#8211; Provides the count of page faults by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>context_switches &#8211; Provides the count of context switches<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>cpu_migrations &#8211; Provides the count cpu migrations by<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>page_faults_min &#8211; Provides the count minor page faults<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>page_faults_maj &#8211; Provides the count major page faults<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>alignment_faults &#8211; Provides the count alignment faults<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform.<br/>
&nbsp;<wbr>&nbsp;<wbr>emulation_faults &#8211; Provides the count emulation faults<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by applications running on the platform. </p>
<p> <code>Note</code>: The statistics can be retrieved using the <code>domstats</code> command using the <i>&#8211;perf</i> flag. </p>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor.</p>
<dt><code>blkiotune</code> <i>domain</i> [<i>&#8211;weight</i> <code>weight</code>] [<i>&#8211;device-weights</i> <code>device-weights</code>] [<i>&#8211;device-read-iops-sec</i> <code>device-read-iops-sec</code>] [<i>&#8211;device-write-iops-sec</i> <code>device-write-iops-sec</code>] [<i>&#8211;device-read-bytes-sec</i> <code>device-read-bytes-sec</code>] [<i>&#8211;device-write-bytes-sec</i> <code>device-write-bytes-sec</code>] [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Display or set the blkio parameters. QEMU/KVM supports <i>&#8211;weight</i>. <i>&#8211;weight</i> is in range [100, 1000]. After kernel 2.6.39, the value could be in the range [10, 1000]. </dd>
<p> <code>device-weights</code> is a single string listing one or more device/weight pairs, in the format of /path/to/device,weight,/path/to/device,weight. Each weight is in the range [100, 1000], [10, 1000] after kernel 2.6.39, or the value 0 to remove that device from per-device listings. Only the devices listed in the string are modified; any existing per-device weights for other devices remain unchanged. </p>
<p> <code>device-read-iops-sec</code> is a single string listing one or more device/read_iops_sec pairs, int the format of /path/to/device,read_iops_sec,/path/to/device,read_iops_sec. Each read_iops_sec is a number which type is unsigned int, value 0 to remove that device from per-device listing. Only the devices listed in the string are modified; any existing per-device read_iops_sec for other devices remain unchanged. </p>
<p> <code>device-write-iops-sec</code> is a single string listing one or more device/write_iops_sec pairs, int the format of /path/to/device,write_iops_sec,/path/to/device,write_iops_sec. Each write_iops_sec is a number which type is unsigned int, value 0 to remove that device from per-device listing. Only the devices listed in the string are modified; any existing per-device write_iops_sec for other devices remain unchanged. </p>
<p> <code>device-read-bytes-sec</code> is a single string listing one or more device/read_bytes_sec pairs, int the format of /path/to/device,read_bytes_sec,/path/to/device,read_bytes_sec. Each read_bytes_sec is a number which type is unsigned long long, value 0 to remove that device from per-device listing. Only the devices listed in the string are modified; any existing per-device read_bytes_sec for other devices remain unchanged. </p>
<p> <code>device-write-bytes-sec</code> is a single string listing one or more device/write_bytes_sec pairs, int the format of /path/to/device,write_bytes_sec,/path/to/device,write_bytes_sec. Each write_bytes_sec is a number which type is unsigned long long, value 0 to remove that device from per-device listing. Only the devices listed in the string are modified; any existing per-device write_bytes_sec for other devices remain unchanged. </p>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor.</p>
<dt><code>setvcpus</code> <i>domain</i> <i>count</i> [<i>&#8211;maximum</i>] [[<i>&#8211;config</i>] [<i>&#8211;live</i>] | [<i>&#8211;current</i>]] [<i>&#8211;guest</i>] [<i>&#8211;hotpluggable</i>]</dt>
<dd> Change the number of virtual CPUs active in a guest domain. By default, this command works on active guest domains. To change the settings for an inactive guest domain, use the <i>&#8211;config</i> flag. </dd>
<p> The <i>count</i> value may be limited by host, hypervisor, or a limit coming from the original description of the guest domain. For Xen, you can only adjust the virtual CPUs of a running domain if the domain is paravirtualized. </p>
<p> If the <i>&#8211;config</i> flag is specified, the change is made to the stored XML configuration for the guest domain, and will only take effect when the guest domain is next started. </p>
<p> If <i>&#8211;live</i> is specified, the guest domain must be active, and the change takes place immediately. Both the <i>&#8211;config</i> and <i>&#8211;live</i> flags may be specified together if supported by the hypervisor. If this command is run before the guest has finished booting, the guest may fail to process the change. </p>
<p> If <i>&#8211;current</i> is specified, affect the current guest state. </p>
<p> When no flags are given, the <i>&#8211;live</i> flag is assumed and the guest domain must be active. In this situation it is up to the hypervisor whether the <i>&#8211;config</i> flag is also assumed, and therefore whether the XML configuration is adjusted to make the change persistent. </p>
<p> If <i>&#8211;guest</i> is specified, then the count of cpus is modified in the guest instead of the hypervisor. This flag is usable only for live domains and may require guest agent to be configured in the guest. </p>
<p> To allow adding vcpus to persistent definitions that can be later hotunplugged after the domain is booted it is necessary to specify the <i>&#8211;hotpluggable</i> flag. Vcpus added to live domains supporting vcpu unplug are automatically marked as hotpluggable. </p>
<p> The <i>&#8211;maximum</i> flag controls the maximum number of virtual cpus that can be hot-plugged the next time the domain is booted. As such, it must only be used with the <i>&#8211;config</i> flag, and not with the <i>&#8211;live</i> or the <i>&#8211;current</i> flag.</p>
<dt><code>setvcpu</code> <i>domain</i> <i>vcpulist</i> [<i>&#8211;enable</i>] | [<i>&#8211;disable</i>] [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Change state of individual vCPUs using hot(un)plug mechanism. </dd>
<p> See <code>vcpupin</code> for information on format of <i>vcpulist</i>. Hypervisor drivers may require that <i>vcpulist</i> contains exactly vCPUs belonging to one hotpluggable entity. This is usually just a single vCPU but certain architectures such as ppc64 require a full core to be specified at once. </p>
<p> Note that hypervisors may refuse to disable certain vcpus such as vcpu 0 or others. </p>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. This is the default. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive.</p>
<dt><code>shutdown</code> <i>domain</i> [<i>&#8211;mode MODE-LIST</i>]</dt>
<dd> Gracefully shuts down a domain. This coordinates with the domain OS to perform graceful shutdown, so there is no guarantee that it will succeed, and may take a variable length of time depending on what services must be shutdown in the domain. </dd>
<p> The exact behavior of a domain when it shuts down is set by the <i>on_poweroff</i> parameter in the domain&#8217;s XML definition. </p>
<p> If <i>domain</i> is transient, then the metadata of any snapshots will be lost once the guest stops running, but the snapshot contents still exist, and a new domain with the same name and UUID can restore the snapshot metadata with <code>snapshot-create</code>. </p>
<p> By default the hypervisor will try to pick a suitable shutdown method. To specify an alternative method, the <i>&#8211;mode</i> parameter can specify a comma separated list which includes <tt>&quot;acpi&quot;</tt>, <tt>&quot;agent&quot;</tt>, <tt>&quot;initctl&quot;</tt>, <tt>&quot;signal&quot;</tt> and <tt>&quot;paravirt&quot;</tt>. The order in which drivers will try each mode is undefined, and not related to the order specified to virsh. For strict control over ordering, use a single mode at a time and repeat the command.</p>
<dt><code>start</code> <i>domain-name-or-uuid</i> [<i>&#8211;console</i>] [<i>&#8211;paused</i>] [<i>&#8211;autodestroy</i>] [<i>&#8211;bypass-cache</i>] [<i>&#8211;force-boot</i>] [<i>&#8211;pass-fds N,M,&#8230;</i>]</dt>
<dd> Start a (previously defined) inactive domain, either from the last <code>managedsave</code> state, or via a fresh boot if no managedsave state is present. The domain will be paused if the <i>&#8211;paused</i> option is used and supported by the driver; otherwise it will be running. If <i>&#8211;console</i> is requested, attach to the console after creation. If <i>&#8211;autodestroy</i> is requested, then the guest will be automatically destroyed when virsh closes its connection to libvirt, or otherwise exits. If <i>&#8211;bypass-cache</i> is specified, and managedsave state exists, the restore will avoid the file system cache, although this may slow down the operation. If <i>&#8211;force-boot</i> is specified, then any managedsave state is discarded and a fresh boot occurs. </dd>
<p> If <i>&#8211;pass-fds</i> is specified, the argument is a comma separated list of open file descriptors which should be pass on into the guest. The file descriptors will be re-numbered in the guest, starting from 3. This is only supported with container based virtualization.</p>
<dt><code>suspend</code> <i>domain</i></dt>
<dd> Suspend a running domain. It is kept in memory but won&#8217;t be scheduled anymore.</dd>
<dt><code>resume</code> <i>domain</i></dt>
<dd> Moves a domain out of the suspended state. This will allow a previously suspended domain to now be eligible for scheduling by the underlying hypervisor.</dd>
<dt><code>dompmsuspend</code> <i>domain</i> <i>target</i> [<i>&#8211;duration</i>]</dt>
<dd> Suspend a running domain into one of these states (possible <i>target</i> values):<br/>
&nbsp;<wbr>mem equivalent of S3&nbsp;<wbr>ACPI&nbsp;<wbr>state<br/>
&nbsp;<wbr>disk equivalent of S4&nbsp;<wbr>ACPI&nbsp;<wbr>state<br/>
&nbsp;<wbr>hybrid&nbsp;<wbr>RAM&nbsp;<wbr>is saved to disk but not powered off </dd>
<p> The <i>&#8211;duration</i> argument specifies number of seconds before the domain is woken up after it was suspended (see also <code>dompmwakeup</code>). Default is 0 for unlimited suspend time. (This feature isn&#8217;t currently supported by any hypervisor driver and 0 should be used.). </p>
<p> Note that this command requires a guest agent configured and running in the domain&#8217;s guest OS. </p>
<p> Beware that at least for QEMU, the domain&#8217;s process will be terminated when target disk is used and a new process will be launched when libvirt is asked to wake up the domain. As a result of this, any runtime changes, such as device hotplug or memory settings, are lost unless such changes were made with <i>&#8211;config</i> flag.</p>
<dt><code>dompmwakeup</code> <i>domain</i></dt>
<dd> Wakeup a domain from pmsuspended state (either suspended by dompmsuspend or from the guest itself). Injects a wakeup into the guest that is in pmsuspended state, rather than waiting for the previously requested duration (if any) to elapse. This operation doesn&#8217;t not necessarily fail if the domain is running.</dd>
<dt><code>ttyconsole</code> <i>domain</i></dt>
<dd> Output the device used for the TTY console of the domain. If the information is not available the processes will provide an exit code of 1.</dd>
<dt><code>undefine</code> <i>domain</i> [<i>&#8211;managed-save</i>] [<i>&#8211;snapshots-metadata</i>] [<i>&#8211;nvram</i>] [<i>&#8211;keep-nvram</i>] [ {<i>&#8211;storage</i> <code>volumes</code> | <i>&#8211;remove-all-storage</i> [<i>&#8211;delete-snapshots</i>]} <i>&#8211;wipe-storage</i>]</dt>
<dd> Undefine a domain. If the domain is running, this converts it to a transient domain, without stopping it. If the domain is inactive, the domain configuration is removed. </dd>
<p> The <i>&#8211;managed-save</i> flag guarantees that any managed save image (see the <code>managedsave</code> command) is also cleaned up. Without the flag, attempts to undefine a domain with a managed save image will fail. </p>
<p> The <i>&#8211;snapshots-metadata</i> flag guarantees that any snapshots (see the <code>snapshot-list</code> command) are also cleaned up when undefining an inactive domain. Without the flag, attempts to undefine an inactive domain with snapshot metadata will fail. If the domain is active, this flag is ignored. </p>
<p> <i>&#8211;nvram</i> and <i>&#8211;keep-nvram</i> specify accordingly to delete or keep nvram (/domain/os/nvram/) file. If the domain has an nvram file and the flags are omitted, the undefine will fail. </p>
<p> The <i>&#8211;storage</i> flag takes a parameter <code>volumes</code>, which is a comma separated list of volume target names or source paths of storage volumes to be removed along with the undefined domain. Volumes can be undefined and thus removed only on inactive domains. Volume deletion is only attempted after the domain is undefined; if not all of the requested volumes could be deleted, the error message indicates what still remains behind. If a volume path is not found in the domain definition, it&#8217;s treated as if the volume was successfully deleted. Only volumes managed by libvirt in storage pools can be removed this way. (See <code>domblklist</code> for list of target names associated to a domain). Example: &#8211;storage vda,/path/to/storage.img </p>
<p> The <i>&#8211;remove-all-storage</i> flag specifies that all of the domain&#8217;s storage volumes should be deleted. </p>
<p> The <i>&#8211;delete-snapshots</i> flag specifies that any snapshots associated with the storage volume should be deleted as well. Requires the <i>&#8211;remove-all-storage</i> flag to be provided. Not all storage drivers support this option, presently only rbd. </p>
<p> The flag <i>&#8211;wipe-storage</i> specifies that the storage volumes should be wiped before removal. </p>
<p> NOTE: For an inactive domain, the domain name or UUID must be used as the <i>domain</i>.</p>
<dt><code>vcpucount</code> <i>domain</i> [{<i>&#8211;maximum</i> | <i>&#8211;active</i>} {<i>&#8211;config</i> | <i>&#8211;live</i> | <i>&#8211;current</i>}] [<i>&#8211;guest</i>]</dt>
<dd> Print information about the virtual cpu counts of the given <i>domain</i>. If no flags are specified, all possible counts are listed in a table; otherwise, the output is limited to just the numeric value requested. For historical reasons, the table lists the label &#8220;current&#8221; on the rows that can be queried in isolation via the <i>&#8211;active</i> flag, rather than relating to the <i>&#8211;current</i> flag. </dd>
<p> <i>&#8211;maximum</i> requests information on the maximum cap of vcpus that a domain can add via <code>setvcpus</code>, while <i>&#8211;active</i> shows the current usage; these two flags cannot both be specified. <i>&#8211;config</i> requires a persistent domain and requests information regarding the next time the domain will be booted, <i>&#8211;live</i> requires a running domain and lists current values, and <i>&#8211;current</i> queries according to the current state of the domain (corresponding to <i>&#8211;live</i> if running, or <i>&#8211;config</i> if inactive); these three flags are mutually exclusive. </p>
<p> If <i>&#8211;guest</i> is specified, then the count of cpus is reported from the perspective of the guest. This flag is usable only for live domains and may require guest agent to be configured in the guest.</p>
<dt><code>vcpuinfo</code> <i>domain</i> [<i>&#8211;pretty</i>]</dt>
<dd> Returns basic information about the domain virtual CPUs, like the number of vCPUs, the running time, the affinity to physical processors. </dd>
<p> With <i>&#8211;pretty</i>, cpu affinities are shown as ranges. </p>
<p> An example output is </p>
<pre>
 $ virsh vcpuinfo fedora
 VCPU:           0
 CPU:            0
 State:          running
 CPU time:       7,0s
 CPU Affinity:   yyyy
 VCPU:           1
 CPU:            1
 State:          running
 CPU time:       0,7s
 CPU Affinity:   yyyy
</pre>
<p> <code>STATES</code> </p>
<p> The State field displays the current operating state of a virtual CPU</p>
<dl>
<dl>
<dt><code>offline</code></dt>
<dd> The virtual CPU is offline and not usable by the domain. This state is not supported by all hypervisors.</dd>
<dt><code>running</code></dt>
<dd> The virtual CPU is available to the domain and is operating.</dd>
<dt><code>blocked</code></dt>
<dd> The virtual CPU is available to the domain but is waiting for a resource. This state is not supported by all hypervisors, in which case <i>running</i> may be reported instead.</dd>
<dt><code>no state</code></dt>
<dd> The virtual CPU state could not be determined. This could happen if the hypervisor is newer than virsh.</dd>
<dt><code>N/A</code></dt>
<dd> There&#8217;s no information about the virtual CPU state available. This can be the case if the domain is not running or the hypervisor does not report the virtual CPU state.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>vcpupin</code> <i>domain</i> [<i>vcpu</i>] [<i>cpulist</i>] [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Query or change the pinning of domain VCPUs to host physical CPUs. To pin a single <i>vcpu</i>, specify <i>cpulist</i>; otherwise, you can query one <i>vcpu</i> or omit <i>vcpu</i> to list all at once. </dd>
<p> <i>cpulist</i> is a list of physical CPU numbers. Its syntax is a comma separated list and a special markup using &#8216;-&#8216; and &#8216;^&#8217; (ex. &#8216;0-4&#8217;, &#8216;0-3,^2&#8217;) can also be allowed. The &#8216;-&#8216; denotes the range and the &#8216;^&#8217; denotes exclusive. For pinning the <i>vcpu</i> to all physical cpus specify &#8216;r&#8217; as a <i>cpulist</i>. If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given if <i>cpulist</i> is present, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor. </p>
<p> <code>Note</code>: The expression is sequentially evaluated, so &#8220;0-15,^8&#8221; is identical to &#8220;9-14,0-7,15&#8221; but not identical to &#8220;^8,0-15&#8221;.</p>
<dt><code>emulatorpin</code> <i>domain</i> [<i>cpulist</i>] [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Query or change the pinning of domain&#8217;s emulator threads to host physical CPUs. </dd>
<p> See <code>vcpupin</code> for <i>cpulist</i>. </p>
<p> If <i>&#8211;live</i> is specified, affect a running guest. If <i>&#8211;config</i> is specified, affect the next boot of a persistent guest. If <i>&#8211;current</i> is specified, affect the current guest state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given if <i>cpulist</i> is present, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor.</p>
<dt><code>guestvcpus</code> <i>domain</i> [[<i>&#8211;enable</i>] | [<i>&#8211;disable</i>]] [<i>cpulist</i>]</dt>
<dd> Query or change state of vCPUs from guest&#8217;s point of view using the guest agent. When invoked without <i>cpulist</i> the guest is queried for available guest vCPUs, their state and possibility to be offlined. </dd>
<p> If <i>cpulist</i> is provided then one of <i>&#8211;enable</i> or <i>&#8211;disable</i> must be provided too. The desired operation is then executed on the domain. </p>
<p> See <code>vcpupin</code> for information on <i>cpulist</i>.</p>
<dt><code>vncdisplay</code> <i>domain</i></dt>
<dd> Output the IP address and port number for the VNC display. If the information is not available the processes will provide an exit code of 1.</dd></dl>
<h2>DEVICE COMMANDS</h2>
<p> The following commands manipulate devices associated to domains. The <i>domain</i> can be specified as a short integer, a name or a full UUID. To better understand the values allowed as options for the command reading the documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html">http://libvirt.org/formatdomain.html</a>&gt; on the format of the device sections to get the most accurate set of accepted values.</p>
<dl>
<dt><code>attach-device</code> <i>domain</i> <i></i><i>FILE</i><i></i> [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]]</dt>
<dd> Attach a device to the domain, using a device definition in an XML file using a device definition element such as &lt;disk&gt; or &lt;interface&gt; as the top-level element. See the documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsDevices">http://libvirt.org/formatdomain.html#elementsDevices</a>&gt; to learn about libvirt XML format for a device. If <i>&#8211;config</i> is specified the command alters the persistent domain configuration with the device attach taking effect the next time libvirt starts the domain. For cdrom and floppy devices, this command only replaces the media within an existing device; consider using <code>update-device</code> for this usage. For passthrough host devices, see also <code>nodedev-detach</code>, needed if the PCI device does not use managed mode. </dd>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. When no flag is specified legacy API is used whose behavior depends on the hypervisor driver. </p>
<p> For compatibility purposes, <i>&#8211;persistent</i> behaves like <i>&#8211;config</i> for an offline domain, and like <i>&#8211;live</i> <i>&#8211;config</i> for a running domain. </p>
<p> <code>Note</code>: using of partial device definition XML files may lead to unexpected results as some fields may be autogenerated and thus match devices other than expected.</p>
<dt><code>attach-disk</code> <i>domain</i> <i>source</i> <i>target</i> [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]] [<i>&#8211;targetbus bus</i>] [<i>&#8211;driver driver</i>] [<i>&#8211;subdriver subdriver</i>] [<i>&#8211;iothread iothread</i>] [<i>&#8211;cache cache</i>] [<i>&#8211;type type</i>] [<i>&#8211;mode mode</i>] [<i>&#8211;sourcetype sourcetype</i>] [<i>&#8211;serial serial</i>] [<i>&#8211;wwn wwn</i>] [<i>&#8211;rawio</i>] [<i>&#8211;address address</i>] [<i>&#8211;multifunction</i>] [<i>&#8211;print-xml</i>]</dt>
<dd> Attach a new disk device to the domain. <i>source</i> is path for the files and devices. <i>target</i> controls the bus or device under which the disk is exposed to the guest OS. It indicates the &#8220;logical&#8221; device name; the optional <i>targetbus</i> attribute specifies the type of disk device to emulate; possible values are driver specific, with typical values being <i>ide</i>, <i>scsi</i>, <i>virtio</i>, <i>xen</i>, <i>usb</i>, <i>sata</i>, or <i>sd</i>, if omitted, the bus type is inferred from the style of the device name (e.g. a device named &#8216;sda&#8217; will typically be exported using a SCSI bus). <i>driver</i> can be <i>file</i>, <i>tap</i> or <i>phy</i> for the Xen hypervisor depending on the kind of access; or <i>qemu</i> for the QEMU emulator. Further details to the driver can be passed using <i>subdriver</i>. For Xen <i>subdriver</i> can be <i>aio</i>, while for QEMU subdriver should match the format of the disk source, such as <i>raw</i> or <i>qcow2</i>. Hypervisor default will be used if <i>subdriver</i> is not specified. However, the default may not be correct, esp. for QEMU as for security reasons it is configured not to detect disk formats. <i>type</i> can indicate <i>lun</i>, <i>cdrom</i> or <i>floppy</i> as alternative to the disk default, although this use only replaces the media within the existing virtual cdrom or floppy device; consider using <code>update-device</code> for this usage instead. <i>mode</i> can specify the two specific mode <i>readonly</i> or <i>shareable</i>. <i>sourcetype</i> can indicate the type of source (block|file) <i>cache</i> can be one of &#8220;default&#8221;, &#8220;none&#8221;, &#8220;writethrough&#8221;, &#8220;writeback&#8221;, &#8220;directsync&#8221; or &#8220;unsafe&#8221;. <i>iothread</i> is the number within the range of domain IOThreads to which this disk may be attached (QEMU only). <i>serial</i> is the serial of disk device. <i>wwn</i> is the wwn of disk device. <i>rawio</i> indicates the disk needs rawio capability. <i>address</i> is the address of disk device in the form of pci:domain.bus.slot.function, scsi:controller.bus.unit, ide:controller.bus.unit or ccw:cssid.ssid.devno. Virtio-ccw devices must have their cssid set to 0xfe. <i>multifunction</i> indicates specified pci address is a multifunction pci device address. </dd>
<p> If <i>&#8211;print-xml</i> is specified, then the XML of the disk that would be attached is printed instead. </p>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. When no flag is specified legacy API is used whose behavior depends on the hypervisor driver. </p>
<p> For compatibility purposes, <i>&#8211;persistent</i> behaves like <i>&#8211;config</i> for an offline domain, and like <i>&#8211;live</i> <i>&#8211;config</i> for a running domain. Likewise, <i>&#8211;shareable</i> is an alias for <i>&#8211;mode shareable</i>.</p>
<dt><code>attach-interface</code> <i>domain</i> <i>type</i> <i>source</i> [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]] [<i>&#8211;target target</i>] [<i>&#8211;mac mac</i>] [<i>&#8211;script script</i>] [<i>&#8211;model model</i>] [<i>&#8211;inbound average,peak,burst,floor</i>] [<i>&#8211;outbound average,peak,burst</i>] [<i>&#8211;managed</i>] [<i>&#8211;print-xml</i>]</dt>
<dd> Attach a new network interface to the domain. </dd>
<p> <code>type</code> can be one of the:</p>
<dl>
<dl>
<dt>
</dt><dd> <i>network</i> to indicate connection via a libvirt virtual network, </dd>
<p> <i>bridge</i> to indicate connection via a bridge device on the host, </p>
<p> <i>direct</i> to indicate connection directly to one of the host&#8217;s network interfaces or bridges, </p>
<p> <i>hostdev</i> to indicate connection using a passthrough of PCI device on the host.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <code>source</code> indicates the source of the connection. The source depends on the type of the interface: </p>
</dd><dl>
<dt>
</dt><dd> <i>network</i> name of the virtual network, </dd>
<p> <i>bridge</i> the name of the bridge device, </p>
<p> <i>direct</i> the name of the host&#8217;s interface or bridge, </p>
<p> <i>hostdev</i> the PCI address of the host&#8217;s interface formatted as domain:bus:slot.function.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <code>&#8211;target</code> is used to specify the tap/macvtap device to be used to connect the domain to the source. Names starting with &#8216;vnet&#8217; are considered as auto-generated and are blanked out/regenerated each time the interface is attached. </p>
<p> <code>&#8211;mac</code> specifies the MAC address of the network interface; if a MAC address is not given, a new address will be automatically generated (and stored in the persistent configuration if &#8220;&#8211;config&#8221; is given on the command line). </p>
<p> <code>&#8211;script</code> is used to specify a path to a custom script to be called while attaching to a bridge &#8211; this will be called instead of the default script not in addition to it. This is valid only for interfaces of <i>bridge</i> type and only for Xen domains. </p>
<p> <code>&#8211;model</code> specifies the network device model to be presented to the domain. </p>
<p> <code>&#8211;inbound</code> and <code>&#8211;outbound</code> control the bandwidth of the interface. At least one from the <i>average</i>, <i>floor</i> pair must be specified. The other two <i>peak</i> and <i>burst</i> are optional, so &#8220;average,peak&#8221;, &#8220;average,,burst&#8221;, &#8220;average,,,floor&#8221;, &#8220;average&#8221; and &#8220;,,,floor&#8221; are also legal. Values for <i>average</i>, <i>floor</i> and <i>peak</i> are expressed in kilobytes per second, while <i>burst</i> is expressed in kilobytes in a single burst at <i>peak</i> speed as described in the Network XML documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatnetwork.html#elementQoS">http://libvirt.org/formatnetwork.html#elementQoS</a>&gt;. </p>
<p> <code>&#8211;managed</code> is usable only for <i>hostdev</i> type and tells libvirt that the interface should be managed, which means detached and reattached from/to the host by libvirt. </p>
<p> If <code>&#8211;print-xml</code> is specified, then the XML of the interface that would be attached is printed instead. </p>
<p> If <code>&#8211;live</code> is specified, affect a running domain. If <code>&#8211;config</code> is specified, affect the next startup of a persistent domain. If <code>&#8211;current</code> is specified, affect the current domain state. Both <code>&#8211;live</code> and <code>&#8211;config</code> flags may be given, but <code>&#8211;current</code> is exclusive. When no flag is specified legacy API is used whose behavior depends on the hypervisor driver. </p>
<p> For compatibility purposes, <code>&#8211;persistent</code> behaves like <code>&#8211;config</code> for an offline domain, and like <code>&#8211;live</code> <code>&#8211;config</code> for a running domain. </p>
<p> <code>Note</code>: the optional target value is the name of a device to be created as the back-end on the node. If not provided a device named &#8220;vnetN&#8221; or &#8220;vifN&#8221; will be created automatically.</dd></dl>
<dt><code>detach-device</code> <i>domain</i> <i></i><i>FILE</i><i></i> [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]]</dt>
<dd> Detach a device from the domain, takes the same kind of XML descriptions as command <code>attach-device</code>. For passthrough host devices, see also <code>nodedev-reattach</code>, needed if the device does not use managed mode. </dd>
<p> <code>Note</code>: The supplied XML description of the device should be as specific as its definition in the domain XML. The set of attributes used to match the device are internal to the drivers. Using a partial definition, or attempting to detach a device that is not present in the domain XML, but shares some specific attributes with one that is present, may lead to unexpected results. </p>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. When no flag is specified legacy API is used whose behavior depends on the hypervisor driver. </p>
<p> For compatibility purposes, <i>&#8211;persistent</i> behaves like <i>&#8211;config</i> for an offline domain, and like <i>&#8211;live</i> <i>&#8211;config</i> for a running domain. </p>
<p> Note that older versions of virsh used <i>&#8211;config</i> as an alias for <i>&#8211;persistent</i>.</p>
<dt><code>detach-disk</code> <i>domain</i> <i>target</i> [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]]</dt>
<dd> Detach a disk device from a domain. The <i>target</i> is the device as seen from the domain. </dd>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. When no flag is specified legacy API is used whose behavior depends on the hypervisor driver. </p>
<p> For compatibility purposes, <i>&#8211;persistent</i> behaves like <i>&#8211;config</i> for an offline domain, and like <i>&#8211;live</i> <i>&#8211;config</i> for a running domain. </p>
<p> Note that older versions of virsh used <i>&#8211;config</i> as an alias for <i>&#8211;persistent</i>.</p>
<dt><code>detach-interface</code> <i>domain</i> <i>type</i> [<i>&#8211;mac mac</i>] [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]]</dt>
<dd> Detach a network interface from a domain. <i>type</i> can be either <i>network</i> to indicate a physical network device or <i>bridge</i> to indicate a bridge to a device. It is recommended to use the <i>mac</i> option to distinguish between the interfaces if more than one are present on the domain. </dd>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. When no flag is specified legacy API is used whose behavior depends on the hypervisor driver. </p>
<p> For compatibility purposes, <i>&#8211;persistent</i> behaves like <i>&#8211;config</i> for an offline domain, and like <i>&#8211;live</i> <i>&#8211;config</i> for a running domain. </p>
<p> Note that older versions of virsh used <i>&#8211;config</i> as an alias for <i>&#8211;persistent</i>.</p>
<dt><code>update-device</code> <i>domain</i> <i>file</i> [<i>&#8211;force</i>] [[[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] | [<i>&#8211;persistent</i>]]</dt>
<dd> Update the characteristics of a device associated with <i>domain</i>, based on the device definition in an XML <i>file</i>. The <i>&#8211;force</i> option can be used to force device update, e.g., to eject a CD-ROM even if it is locked/mounted in the domain. See the documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsDevices">http://libvirt.org/formatdomain.html#elementsDevices</a>&gt; to learn about libvirt XML format for a device. </dd>
<p> If <i>&#8211;live</i> is specified, affect a running domain. If <i>&#8211;config</i> is specified, affect the next startup of a persistent domain. If <i>&#8211;current</i> is specified, affect the current domain state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. Not specifying any flag is the same as specifying <i>&#8211;current</i>. </p>
<p> For compatibility purposes, <i>&#8211;persistent</i> behaves like <i>&#8211;config</i> for an offline domain, and like <i>&#8211;live</i> <i>&#8211;config</i> for a running domain. </p>
<p> Note that older versions of virsh used <i>&#8211;config</i> as an alias for <i>&#8211;persistent</i>. </p>
<p> <code>Note</code>: using of partial device definition XML files may lead to unexpected results as some fields may be autogenerated and thus match devices other than expected.</p>
<dt><code>change-media</code> <i>domain</i> <i>path</i> [<i>&#8211;eject</i>] [<i>&#8211;insert</i>] [<i>&#8211;update</i>] [<i>source</i>] [<i>&#8211;force</i>] [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]] [<i>&#8211;print-xml</i>] [<i>&#8211;block</i>]</dt>
<dd> Change media of CDROM or floppy drive. <i>path</i> can be the fully-qualified path or the unique target name (&lt;target dev=&#8217;hdc&#8217;&gt;) of the disk device. <i>source</i> specifies the path of the media to be inserted or updated. Flag <i>&#8211;block</i> allows to set the backing type in case a block device is used as media for the CDROM or floppy drive instead of a file. </dd>
<p> <i>&#8211;eject</i> indicates the media will be ejected. <i>&#8211;insert</i> indicates the media will be inserted. <i>source</i> must be specified. If the device has source (e.g. &lt;source file=&#8217;media&#8217;&gt;), and <i>source</i> is not specified, <i>&#8211;update</i> is equal to <i>&#8211;eject</i>. If the device has no source, and <i>source</i> is specified, <i>&#8211;update</i> is equal to <i>&#8211;insert</i>. If the device has source, and <i>source</i> is specified, <i>&#8211;update</i> behaves like combination of <i>&#8211;eject</i> and <i>&#8211;insert</i>. If none of <i>&#8211;eject</i>, <i>&#8211;insert</i>, and <i>&#8211;update</i> is specified, <i>&#8211;update</i> is used by default. The <i>&#8211;force</i> option can be used to force media changing. If <i>&#8211;live</i> is specified, alter live configuration of running guest. If <i>&#8211;config</i> is specified, alter persistent configuration, effect observed on next boot. <i>&#8211;current</i> can be either or both of <i>live</i> and <i>config</i>, depends on the hypervisor&#8217;s implementation. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. If no flag is specified, behavior is different depending on hypervisor. If <i>&#8211;print-xml</i> is specified, the XML that would be used to change media is printed instead of changing the media.</dl>
<h2>NODEDEV COMMANDS</h2>
<p> The following commands manipulate host devices that are intended to be passed through to guest domains via &lt;hostdev&gt; elements in a domain&#8217;s &lt;devices&gt; section. A node device key is generally specified by the bus name followed by its address, using underscores between all components, such as pci_0000_00_02_1, usb_1_5_3, or net_eth1_00_27_13_6a_fe_00. The <code>nodedev-list</code> gives the full list of host devices that are known to libvirt, although this includes devices that cannot be assigned to a guest (for example, attempting to detach the PCI device that controls the host&#8217;s hard disk controller where the guest&#8217;s disk images live could cause the host system to lock up or reboot). </p>
<p> For more information on node device definition see: &lt;<a rel="nofollow" href="http://libvirt.org/formatnode.html">http://libvirt.org/formatnode.html</a>&gt;. </p>
<p> Passthrough devices cannot be simultaneously used by the host and its guest domains, nor by multiple active guests at once. If the &lt;hostdev&gt; description of a PCI device includes the attribute <code>managed=&#8217;yes&#8217;</code>, and the hypervisor driver supports it, then the device is in managed mode, and attempts to use that passthrough device in an active guest will automatically behave as if <code>nodedev-detach</code> (guest start, device hot-plug) and <code>nodedev-reattach</code> (guest stop, device hot-unplug) were called at the right points. If a PCI device is not marked as managed, then it must manually be detached before guests can use it, and manually reattached to be returned to the host. Also, if a device is manually detached, then the host does not regain control of the device without a matching reattach, even if the guests use the device in managed mode.</p>
<dl>
<dt><code>nodedev-create</code> <i></i><i>FILE</i><i></i></dt>
<dd> Create a device on the host node that can then be assigned to virtual machines. Normally, libvirt is able to automatically determine which host nodes are available for use, but this allows registration of host hardware that libvirt did not automatically detect. <i>file</i> contains xml for a top-level &lt;device&gt; description of a node device.</dd>
<dt><code>nodedev-destroy</code> <i>device</i></dt>
<dd> Destroy (stop) a device on the host. <i>device</i> can be either device name or wwn pair in &#8220;wwnn,wwpn&#8221; format (only works for vHBA currently). Note that this makes libvirt quit managing a host device, and may even make that device unusable by the rest of the physical host until a reboot.</dd>
<dt><code>nodedev-detach</code> <i>nodedev</i> [<i>&#8211;driver backend_driver</i>]</dt>
<dd> Detach <i>nodedev</i> from the host, so that it can safely be used by guests via &lt;hostdev&gt; passthrough. This is reversed with <code>nodedev-reattach</code>, and is done automatically for managed devices. </dd>
<p> Different backend drivers expect the device to be bound to different dummy devices. For example, QEMU&#8216;s &#8220;kvm&#8221; backend driver (the default) expects the device to be bound to pci-stub, but its &#8220;vfio&#8221; backend driver expects the device to be bound to vfio-pci. The <i>&#8211;driver</i> parameter can be used to specify the desired backend driver.</p>
<dt><code>nodedev-dumpxml</code> <i>device</i></dt>
<dd> Dump a &lt;device&gt; XML representation for the given node device, including such information as the device name, which bus owns the device, the vendor and product id, and any capabilities of the device usable by libvirt (such as whether device reset is supported). <i>device</i> can be either device name or wwn pair in &#8220;wwnn,wwpn&#8221; format (only works for HBA).</dd>
<dt><code>nodedev-list</code> <i>cap</i> <i>&#8211;tree</i></dt>
<dd> List all of the devices available on the node that are known by libvirt. <i>cap</i> is used to filter the list by capability types, the types must be separated by comma, e.g. &#8211;cap pci,scsi. Valid capability types include &#8216;system&#8217;, &#8216;pci&#8217;, &#8216;usb_device&#8217;, &#8216;usb&#8217;, &#8216;net&#8217;, &#8216;scsi_host&#8217;, &#8216;scsi_target&#8217;, &#8216;scsi&#8217;, &#8216;storage&#8217;, &#8216;fc_host&#8217;, &#8216;vports&#8217;, &#8216;scsi_generic&#8217;, &#8216;drm&#8217;, &#8216;mdev&#8217;, &#8216;mdev_types&#8217;. If <i>&#8211;tree</i> is used, the output is formatted in a tree representing parents of each node. <i>cap</i> and <i>&#8211;tree</i> are mutually exclusive.</dd>
<dt><code>nodedev-reattach</code> <i>nodedev</i></dt>
<dd> Declare that <i>nodedev</i> is no longer in use by any guests, and that the host can resume normal use of the device. This is done automatically for PCI devices in managed mode and USB devices, but must be done explicitly to match any explicit <code>nodedev-detach</code>.</dd>
<dt><code>nodedev-reset</code> <i>nodedev</i></dt>
<dd> Trigger a device reset for <i>nodedev</i>, useful prior to transferring a node device between guest passthrough or the host. Libvirt will often do this action implicitly when required, but this command allows an explicit reset when needed.</dd>
<dt><code>nodedev-event</code> {[<i>nodedev</i>] <i>event</i> [<i>&#8211;loop</i>] [<i>&#8211;timeout</i> <i>seconds</i>] [<i>&#8211;timestamp</i>] | <i>&#8211;list</i>}</dt>
<dd> Wait for a class of node device events to occur, and print appropriate details of events as they happen. The events can optionally be filtered by <i>nodedev</i>. Using <i>&#8211;list</i> as the only argument will provide a list of possible <i>event</i> values known by this client, although the connection might not allow registering for all these events. </dd>
<p> By default, this command is one-shot, and returns success once an event occurs; you can send SIGINT (usually via <tt>&quot;Ctrl-C&quot;</tt>) to quit immediately. If <i>&#8211;timeout</i> is specified, the command gives up waiting for events after <i>seconds</i> have elapsed. With <i>&#8211;loop</i>, the command prints all events until a timeout or interrupt key. </p>
<p> When <i>&#8211;timestamp</i> is used, a human-readable timestamp will be printed before the event.</dl>
<h2>VIRTUAL NETWORK COMMANDS</h2>
<p> The following commands manipulate networks. Libvirt has the capability to define virtual networks which can then be used by domains and linked to actual network devices. For more detailed information about this feature see the documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatnetwork.html">http://libvirt.org/formatnetwork.html</a>&gt; . Many of the commands for virtual networks are similar to the ones used for domains, but the way to name a virtual network is either by its name or UUID.</p>
<dl>
<dt><code>net-autostart</code> <i>network</i> [<i>&#8211;disable</i>]</dt>
<dd> Configure a virtual network to be automatically started at boot. The <i>&#8211;disable</i> option disable autostarting.</dd>
<dt><code>net-create</code> <i>file</i></dt>
<dd> Create a transient (temporary) virtual network from an XML <i>file</i> and instantiate (start) the network. See the documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatnetwork.html">http://libvirt.org/formatnetwork.html</a>&gt; to get a description of the XML network format used by libvirt.</dd>
<dt><code>net-define</code> <i>file</i></dt>
<dd> Define an inactive persistent virtual network or modify an existing persistent one from the XML <i>file</i>.</dd>
<dt><code>net-destroy</code> <i>network</i></dt>
<dd> Destroy (stop) a given transient or persistent virtual network specified by its name or UUID. This takes effect immediately.</dd>
<dt><code>net-dumpxml</code> <i>network</i> [<i>&#8211;inactive</i>]</dt>
<dd> Output the virtual network information as an XML dump to stdout. If <i>&#8211;inactive</i> is specified, then physical functions are not expanded into their associated virtual functions.</dd>
<dt><code>net-edit</code> <i>network</i></dt>
<dd> Edit the XML configuration file for a network. </dd>
<p> This is equivalent to: </p>
<pre>
 virsh net-dumpxml --inactive network &gt; network.xml
 vi network.xml (or make changes with your other text editor)
 virsh net-define network.xml
</pre>
<p> except that it does some error checking. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>.</p>
<dt><code>net-event</code> {[<i>network</i>] <i>event</i> [<i>&#8211;loop</i>] [<i>&#8211;timeout</i> <i>seconds</i>] [<i>&#8211;timestamp</i>] | <i>&#8211;list</i>}</dt>
<dd> Wait for a class of network events to occur, and print appropriate details of events as they happen. The events can optionally be filtered by <i>network</i>. Using <i>&#8211;list</i> as the only argument will provide a list of possible <i>event</i> values known by this client, although the connection might not allow registering for all these events. </dd>
<p> By default, this command is one-shot, and returns success once an event occurs; you can send SIGINT (usually via <tt>&quot;Ctrl-C&quot;</tt>) to quit immediately. If <i>&#8211;timeout</i> is specified, the command gives up waiting for events after <i>seconds</i> have elapsed. With <i>&#8211;loop</i>, the command prints all events until a timeout or interrupt key. </p>
<p> When <i>&#8211;timestamp</i> is used, a human-readable timestamp will be printed before the event.</p>
<dt><code>net-info</code> <i>network</i></dt>
<dd> Returns basic information about the <i>network</i> object.</dd>
<dt><code>net-list</code> [<i>&#8211;inactive</i> | <i>&#8211;all</i>] { [<i>&#8211;table</i>] | <i>&#8211;name</i> | <i>&#8211;uuid</i> } [<i>&#8211;persistent</i>] [&lt;&#8211;transient&gt;] [<i>&#8211;autostart</i>] [&lt;&#8211;no-autostart&gt;]</dt>
<dd> Returns the list of active networks, if <i>&#8211;all</i> is specified this will also include defined but inactive networks, if <i>&#8211;inactive</i> is specified only the inactive ones will be listed. You may also want to filter the returned networks by <i>&#8211;persistent</i> to list the persistent ones, <i>&#8211;transient</i> to list the transient ones, <i>&#8211;autostart</i> to list the ones with autostart enabled, and <i>&#8211;no-autostart</i> to list the ones with autostart disabled. </dd>
<p> If <i>&#8211;name</i> is specified, network names are printed instead of the table formatted one per line. If <i>&#8211;uuid</i> is specified network&#8217;s UUID&#8216;s are printed instead of names. Flag <i>&#8211;table</i> specifies that the legacy table-formatted output should be used. This is the default. All of these are mutually exclusive. </p>
<p> NOTE: When talking to older servers, this command is forced to use a series of API calls with an inherent race, where a pool might not be listed or might appear more than once if it changed state between calls while the list was being collected. Newer servers do not have this problem.</p>
<dt><code>net-name</code> <i>network-UUID</i></dt>
<dd> Convert a network UUID to network name.</dd>
<dt><code>net-start</code> <i>network</i></dt>
<dd> Start a (previously defined) inactive network.</dd>
<dt><code>net-undefine</code> <i>network</i></dt>
<dd> Undefine the configuration for a persistent network. If the network is active, make it transient.</dd>
<dt><code>net-uuid</code> <i>network-name</i></dt>
<dd> Convert a network name to network UUID.</dd>
<dt><code>net-update</code> <i>network</i> <i>command</i> <i>section</i> <i>xml</i> [<i>&#8211;parent-index</i> <i>index</i>] [[<i>&#8211;live</i>] [<i>&#8211;config</i>] | [<i>&#8211;current</i>]]</dt>
<dd> Update the given section of an existing network definition, with the changes optionally taking effect immediately, without needing to destroy and re-start the network. </dd>
<p> <i>command</i> is one of &#8220;add-first&#8221;, &#8220;add-last&#8221;, &#8220;add&#8221; (a synonym for add-last), &#8220;delete&#8221;, or &#8220;modify&#8221;. </p>
<p> <i>section</i> is one of &#8220;bridge&#8221;, &#8220;domain&#8221;, &#8220;ip&#8221;, &#8220;ip-dhcp-host&#8221;, &#8220;ip-dhcp-range&#8221;, &#8220;forward&#8221;, &#8220;forward-interface&#8221;, &#8220;forward-pf&#8221;, &#8220;portgroup&#8221;, &#8220;dns-host&#8221;, &#8220;dns-txt&#8221;, or &#8220;dns-srv&#8221;, each section being named by a concatenation of the xml element hierarchy leading to the element being changed. For example, &#8220;ip-dhcp-host&#8221; will change a &lt;host&gt; element that is contained inside a &lt;dhcp&gt; element inside an &lt;ip&gt; element of the network. </p>
<p> <i>xml</i> is either the text of a complete xml element of the type being changed (e.g. &#8220;&lt;host mac=&#8221;00:11:22:33:44:55&#8242; ip=&#8217;1.2.3.4&#8217;/&gt;&#8220;, or the name of a file that contains a complete xml element. Disambiguation is done by looking at the first character of the provided text &#8211; if the first character is &#8221;&lt;&#8220;, it is xml text, if the first character is not &#8221;&lt;&quot;, it is the name of a file that contains the xml text to be used. </p>
<p> The <i>&#8211;parent-index</i> option is used to specify which of several parent elements the requested element is in (0-based). For example, a dhcp &lt;host&gt; element could be in any one of multiple &lt;ip&gt; elements in the network; if a parent-index isn&#8217;t provided, the &#8220;most appropriate&#8221; &lt;ip&gt; element will be selected (usually the only one that already has a &lt;dhcp&gt; element), but if <i>&#8211;parent-index</i> is given, that particular instance of &lt;ip&gt; will get the modification. </p>
<p> If <i>&#8211;live</i> is specified, affect a running network. If <i>&#8211;config</i> is specified, affect the next startup of a persistent network. If <i>&#8211;current</i> is specified, affect the current network state. Both <i>&#8211;live</i> and <i>&#8211;config</i> flags may be given, but <i>&#8211;current</i> is exclusive. Not specifying any flag is the same as specifying <i>&#8211;current</i>.</p>
<dt><code>net-dhcp-leases</code> <i>network</i> [<i>mac</i>]</dt>
<dd> Get a list of dhcp leases for all network interfaces connected to the given virtual <i>network</i> or limited output just for one interface if <i>mac</i> is specified.</dd></dl>
<h2>INTERFACE COMMANDS</h2>
<p> The following commands manipulate host interfaces. Often, these host interfaces can then be used by name within domain &lt;interface&gt; elements (such as a system-created bridge interface), but there is no requirement that host interfaces be tied to any particular guest configuration XML at all. </p>
<p> Many of the commands for host interfaces are similar to the ones used for domains, and the way to name an interface is either by its name or its MAC address. However, using a MAC address for an <i>iface</i> argument only works when that address is unique (if an interface and a bridge share the same MAC address, which is often the case, then using that MAC address results in an error due to ambiguity, and you must resort to a name instead).</p>
<dl>
<dt><code>iface-bridge</code> <i>interface</i> <i>bridge</i> [<i>&#8211;no-stp</i>] [<i>delay</i>] [<i>&#8211;no-start</i>]</dt>
<dd> Create a bridge device named <i>bridge</i>, and attach the existing network device <i>interface</i> to the new bridge. The new bridge defaults to starting immediately, with STP enabled and a delay of 0; these settings can be altered with <i>&#8211;no-stp</i>, <i>&#8211;no-start</i>, and an integer number of seconds for <i>delay</i>. All IP address configuration of <i>interface</i> will be moved to the new bridge device. </dd>
<p> See also <code>iface-unbridge</code> for undoing this operation.</p>
<dt><code>iface-define</code> <i>file</i></dt>
<dd> Define an inactive persistent physical host interface or modify an existing persistent one from the XML <i>file</i>.</dd>
<dt><code>iface-destroy</code> <i>interface</i></dt>
<dd> Destroy (stop) a given host interface, such as by running &#8220;if-down&#8221; to disable that interface from active use. This takes effect immediately.</dd>
<dt><code>iface-dumpxml</code> <i>interface</i> [<i>&#8211;inactive</i>]</dt>
<dd> Output the host interface information as an XML dump to stdout. If <i>&#8211;inactive</i> is specified, then the output reflects the persistent state of the interface that will be used the next time it is started.</dd>
<dt><code>iface-edit</code> <i>interface</i></dt>
<dd> Edit the XML configuration file for a host interface. </dd>
<p> This is equivalent to: </p>
<pre>
 virsh iface-dumpxml iface &gt; iface.xml
 vi iface.xml (or make changes with your other text editor)
 virsh iface-define iface.xml
</pre>
<p> except that it does some error checking. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>.</p>
<dt><code>iface-list</code> [<i>&#8211;inactive</i> | <i>&#8211;all</i>]</dt>
<dd> Returns the list of active host interfaces. If <i>&#8211;all</i> is specified this will also include defined but inactive interfaces. If <i>&#8211;inactive</i> is specified only the inactive ones will be listed.</dd>
<dt><code>iface-name</code> <i>interface</i></dt>
<dd> Convert a host interface MAC to interface name, if the MAC address is unique among the host&#8217;s interfaces. </dd>
<p> <i>interface</i> specifies the interface MAC address.</p>
<dt><code>iface-mac</code> <i>interface</i></dt>
<dd> Convert a host interface name to MAC address. </dd>
<p> <i>interface</i> specifies the interface name.</p>
<dt><code>iface-start</code> <i>interface</i></dt>
<dd> Start a (previously defined) host interface, such as by running &#8220;if-up&#8221;.</dd>
<dt><code>iface-unbridge</code> <i>bridge</i> [<i>&#8211;no-start</i>]</dt>
<dd> Tear down a bridge device named <i>bridge</i>, releasing its underlying interface back to normal usage, and moving all IP address configuration from the bridge device to the underlying device. The underlying interface is restarted unless <i>&#8211;no-start</i> is present; this flag is present for symmetry, but generally not recommended. </dd>
<p> See also <code>iface-bridge</code> for creating a bridge.</p>
<dt><code>iface-undefine</code> <i>interface</i></dt>
<dd> Undefine the configuration for an inactive host interface.</dd>
<dt><code>iface-begin</code></dt>
<dd> Create a snapshot of current host interface settings, which can later be committed (<i>iface-commit</i>) or restored (<i>iface-rollback</i>). If a snapshot already exists, then this command will fail until the previous snapshot has been committed or restored. Undefined behavior results if any external changes are made to host interfaces outside of the libvirt API between the beginning of a snapshot and its eventual commit or rollback.</dd>
<dt><code>iface-commit</code></dt>
<dd> Declare all changes since the last <i>iface-begin</i> as working, and delete the rollback point. If no interface snapshot has already been started, then this command will fail.</dd>
<dt><code>iface-rollback</code></dt>
<dd> Revert all host interface settings back to the state recorded in the last <i>iface-begin</i>. If no interface snapshot has already been started, then this command will fail. Rebooting the host also serves as an implicit rollback point.</dd></dl>
<h2>STORAGE POOL COMMANDS</h2>
<p> The following commands manipulate storage pools. Libvirt has the capability to manage various storage solutions, including files, raw partitions, and domain-specific formats, used to provide the storage volumes visible as devices within virtual machines. For more detailed information about this feature, see the documentation at &lt;<a rel="nofollow" href="http://libvirt.org/formatstorage.html">http://libvirt.org/formatstorage.html</a>&gt; . Many of the commands for pools are similar to the ones used for domains.</p>
<dl>
<dt><code>find-storage-pool-sources</code> <i>type</i> [<i>srcSpec</i>]</dt>
<dd> Returns XML describing all possible available storage pool sources that could be used to create or define a storage pool of a given <i>type</i>. If <i>srcSpec</i> is provided, it is a file that contains XML to further restrict the query for pools. </dd>
<p> Not all storage pools support discovery in this manner. Furthermore, for those that do support discovery, only specific XML elements are required in order to return valid data, while other elements and even attributes of some elements are ignored since they are not necessary to find the pool based on the search criteria. The following lists the supported <i>type</i> options and the expected minimal XML elements used to perform the search. </p>
<p> For a &#8220;netfs&#8221; or &#8220;gluster&#8221; pool, the minimal expected XML required is the &lt;host&gt; element with a &#8220;name&#8221; attribute describing the IP address or hostname to be used to find the pool. The &#8220;port&#8221; attribute will be ignored as will any other provided XML elements in <i>srcSpec</i>. </p>
<p> For a &#8220;logical&#8221; pool, the contents of the <i>srcSpec</i> file are ignored, although if provided the file must at least exist. </p>
<p> For an &#8220;iscsi&#8221; pool, the minimal expect XML required is the &lt;host&gt; element with a &#8220;name&#8221; attribute describing the IP address or hostname to be used to find the pool (the iSCSI server address). Optionally, the &#8220;port&#8221; attribute may be provided, although it will default to 3260. Optionally, an &lt;initiator&gt; XML element with a &#8220;name&#8221; attribute may be provided to further restrict the iSCSI target search to a specific initiator for multi-iqn iSCSI storage pools.</p>
<dt><code>find-storage-pool-sources-as</code> <i>type</i> [<i>host</i>] [<i>port</i>] [<i>initiator</i>]</dt>
<dd> Rather than providing <i>srcSpec</i> XML file for <code>find-storage-pool-sources</code> use this command option in order to have virsh generate the query XML file using the optional arguments. The command will return the same output XML as <code>find-storage-pool-sources</code>. </dd>
<p> Use <i>host</i> to describe a specific host to use for networked storage, such as netfs, gluster, and iscsi <i>type</i> pools. </p>
<p> Use <i>port</i> to further restrict which networked port to utilize for the connection if required by the specific storage backend, such as iscsi. </p>
<p> Use <i>initiator</i> to further restrict the iscsi <i>type</i> pool searches to specific target initiators.</p>
<dt><code>pool-autostart</code> <i>pool-or-uuid</i> [<i>&#8211;disable</i>]</dt>
<dd> Configure whether <i>pool</i> should automatically start at boot.</dd>
<dt><code>pool-build</code> <i>pool-or-uuid</i> [<i>&#8211;overwrite</i>] [<i>&#8211;no-overwrite</i>]</dt>
<dd> Build a given pool. </dd>
<p> Options <i>&#8211;overwrite</i> and <i>&#8211;no-overwrite</i> can only be used for <code>pool-build</code> a filesystem, disk, or logical pool. </p>
<p> For a file system pool if neither flag is specified, then <code>pool-build</code> just makes the target path directory and no attempt to run mkfs on the target volume device. If <i>&#8211;no-overwrite</i> is specified, it probes to determine if a filesystem already exists on the target device, returning an error if one exists or using mkfs to format the target device if not. If <i>&#8211;overwrite</i> is specified, mkfs is always executed and any existing data on the target device is overwritten unconditionally. </p>
<p> For a disk pool, if neither of them is specified or <i>&#8211;no-overwrite</i> is specified, <code>pool-build</code> will check the target volume device for existing filesystems or partitions before attempting to write a new label on the target volume device. If the target volume device already has a label, the command will fail. If <i>&#8211;overwrite</i> is specified, then no check will be made on the target volume device prior to writing a new label. Writing of the label uses the pool source format type or &#8220;dos&#8221; if not specified. </p>
<p> For a logical pool, if neither of them is specified or <i>&#8211;no-overwrite</i> is specified, <code>pool-build</code> will check the target volume devices for existing filesystems or partitions before attempting to initialize and format each device for usage by the logical pool. If any target volume device already has a label, the command will fail. If <i>&#8211;overwrite</i> is specified, then no check will be made on the target volume devices prior to initializing and formatting each device. Once all the target volume devices are properly formatted via pvcreate, the volume group will be created using all the devices.</p>
<dt><code>pool-create</code> <i>file</i> [<i>&#8211;build</i>] [[<i>&#8211;overwrite</i>] | [<i>&#8211;no-overwrite</i>]]</dt>
<dd> Create and start a pool object from the XML <i>file</i>. </dd>
<p> [<i>&#8211;build</i>] [[<i>&#8211;overwrite</i>] | [<i>&#8211;no-overwrite</i>]] perform a <code>pool-build</code> after creation in order to remove the need for a follow-up command to build the pool. The <i>&#8211;overwrite</i> and <i>&#8211;no-overwrite</i> flags follow the same rules as <code>pool-build</code>. If just <i>&#8211;build</i> is provided, then <code>pool-build</code> is called with no flags.</p>
<dt><code>pool-create-as</code> <i>name</i> <i>type</i> [<i>&#8211;source-host hostname</i>] [<i>&#8211;source-path path</i>] [<i>&#8211;source-dev path</i>] [<i>&#8211;source-name name</i>] [<i>&#8211;target path</i>] [<i>&#8211;source-format format</i>] [<i>&#8211;auth-type authtype</i> <i>&#8211;auth-username username</i> <i>&#8211;secret-usage usage</i>] [[<i>&#8211;adapter-name name</i>] | [<i>&#8211;adapter-wwnn</i> <i>&#8211;adapter-wwpn</i>] [<i>&#8211;adapter-parent parent</i>]] [<i>&#8211;build</i>] [[<i>&#8211;overwrite</i>] | [<i>&#8211;no-overwrite</i>]] [<i>&#8211;print-xml</i>]</dt>
<dd> Create and start a pool object <i>name</i> from the raw parameters. If <i>&#8211;print-xml</i> is specified, then print the XML of the pool object without creating the pool. Otherwise, the pool has the specified <i>type</i>. When using <code>pool-create-as</code> for a pool of <i>type</i> &#8220;disk&#8221;, the existing partitions found on the <i>&#8211;source-dev path</i> will be used to populate the disk pool. Therefore, it is suggested to use <code>pool-define-as</code> and <code>pool-build</code> with the <i>&#8211;overwrite</i> in order to properly initialize the disk pool. </dd>
<p> [<i>&#8211;source-host hostname</i>] provides the source hostname for pools backed by storage from a remote server (pool types netfs, iscsi, rbd, sheepdog, gluster). </p>
<p> [<i>&#8211;source-path path</i>] provides the source directory path for pools backed by directories (pool type dir). </p>
<p> [<i>&#8211;source-dev path</i>] provides the source path for pools backed by physical devices (pool types fs, logical, disk, iscsi, zfs). </p>
<p> [<i>&#8211;source-name name</i>] provides the source name for pools backed by storage from a named element (pool types logical, rbd, sheepdog, gluster). </p>
<p> [<i>&#8211;target path</i>] is the path for the mapping of the storage pool into the host file system. </p>
<p> [<i>&#8211;source-format format</i>] provides information about the format of the pool (pool types fs, netfs, disk, logical). </p>
<p> [<i>&#8211;auth-type authtype</i> <i>&#8211;auth-username username</i> <i>&#8211;secret-usage usage</i>] provides the elements required to generate authentication credentials for the storage pool. The <i>authtype</i> is either chap for iscsi <i>type</i> pools or ceph for rbd <i>type</i> pools. </p>
<p> [<i>&#8211;adapter-name name</i>] defines the scsi_hostN adapter name to be used for the scsi_host adapter type pool. </p>
<p> [<i>&#8211;adapter-wwnn</i> <i>&#8211;adapter-wwpn</i> [<i>&#8211;adapter-parent parent</i>]] defines the wwnn and wwpn to be used for the fc_host adapter type pool. The parent optionally provides the name of the scsi_hostN node device to be used for the vHBA. </p>
<p> [<i>&#8211;build</i>] [[<i>&#8211;overwrite</i>] | [<i>&#8211;no-overwrite</i>]] perform a <code>pool-build</code> after creation in order to remove the need for a follow-up command to build the pool. The <i>&#8211;overwrite</i> and <i>&#8211;no-overwrite</i> flags follow the same rules as <code>pool-build</code>. If just <i>&#8211;build</i> is provided, then <code>pool-build</code> is called with no flags. </p>
<p> For a &#8220;logical&#8221; pool only [<i>&#8211;name</i>] needs to be provided. The [<i>&#8211;source-name</i>] if provided must match the Volume Group name. If not provided, one will be generated using the [<i>&#8211;name</i>]. If provided the [<i>&#8211;target</i>] is ignored and a target source is generated using the [<i>&#8211;source-name</i>] (or as generated from the [<i>&#8211;name</i>]).</p>
<dt><code>pool-define</code> <i>file</i></dt>
<dd> Define an inactive persistent storage pool or modify an existing persistent one from the XML <i>file</i>.</dd>
<dt><code>pool-define-as</code> <i>name</i> <i>type</i> [<i>&#8211;source-host hostname</i>] [<i>&#8211;source-path path</i>] [<i>&#8211;source-dev path</i>] [<i>&#8211;source-name name</i>] [<i>&#8211;target path</i>] [<i>&#8211;source-format format</i>] [<i>&#8211;auth-type authtype</i> <i>&#8211;auth-username username</i> <i>&#8211;secret-usage usage</i>] [[<i>&#8211;adapter-name name</i>] | [<i>&#8211;adapter-wwnn</i> <i>&#8211;adapter-wwpn</i>] [<i>&#8211;adapter-parent parent</i>]] [<i>&#8211;print-xml</i>]</dt>
<dd> Create, but do not start, a pool object <i>name</i> from the raw parameters. If <i>&#8211;print-xml</i> is specified, then print the XML of the pool object without defining the pool. Otherwise, the pool has the specified <i>type</i>. </dd>
<p> Use the same arguments as <code>pool-create-as</code>, except for the <i>&#8211;build</i>, <i>&#8211;overwrite</i>, and <i>&#8211;no-overwrite</i> options.</p>
<dt><code>pool-destroy</code> <i>pool-or-uuid</i></dt>
<dd> Destroy (stop) a given <i>pool</i> object. Libvirt will no longer manage the storage described by the pool object, but the raw data contained in the pool is not changed, and can be later recovered with <code>pool-create</code>.</dd>
<dt><code>pool-delete</code> <i>pool-or-uuid</i></dt>
<dd> Destroy the resources used by a given <i>pool</i> object. This operation is non-recoverable. The <i>pool</i> object will still exist after this command, ready for the creation of new storage volumes.</dd>
<dt><code>pool-dumpxml</code> [<i>&#8211;inactive</i>] <i>pool-or-uuid</i></dt>
<dd> Returns the XML information about the <i>pool</i> object. <i>&#8211;inactive</i> tells virsh to dump pool configuration that will be used on next start of the pool as opposed to the current pool configuration.</dd>
<dt><code>pool-edit</code> <i>pool-or-uuid</i></dt>
<dd> Edit the XML configuration file for a storage pool. </dd>
<p> This is equivalent to: </p>
<pre>
 virsh pool-dumpxml pool &gt; pool.xml
 vi pool.xml (or make changes with your other text editor)
 virsh pool-define pool.xml
</pre>
<p> except that it does some error checking. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>.</p>
<dt><code>pool-info</code> [<i>&#8211;bytes</i>] <i>pool-or-uuid</i></dt>
<dd> Returns basic information about the <i>pool</i> object. If <i>&#8211;bytes</i> is specified the sizes of basic info are not converted to human friendly units.</dd>
<dt><code>pool-list</code> [<i>&#8211;inactive</i>] [<i>&#8211;all</i>] [<i>&#8211;persistent</i>] [<i>&#8211;transient</i>] [<i>&#8211;autostart</i>] [<i>&#8211;no-autostart</i>] [[<i>&#8211;details</i>] [<i>&#8211;uuid</i>] [<i>&#8211;name</i>] [&lt;type&gt;]</dt>
<dd> List pool objects known to libvirt. By default, only active pools are listed; <i>&#8211;inactive</i> lists just the inactive pools, and <i>&#8211;all</i> lists all pools. </dd>
<p> In addition, there are several sets of filtering flags. <i>&#8211;persistent</i> is to list the persistent pools, <i>&#8211;transient</i> is to list the transient pools. <i>&#8211;autostart</i> lists the autostarting pools, <i>&#8211;no-autostart</i> lists the pools with autostarting disabled. If <i>&#8211;uuid</i> is specified only pool&#8217;s UUIDs are printed. If <i>&#8211;name</i> is specified only pool&#8217;s names are printed. If both <i>&#8211;name</i> and <i>&#8211;uuid</i> are specified, pool&#8217;s UUID and names are printed side by side without any header. Option <i>&#8211;details</i> is mutually exclusive with options <i>&#8211;uuid</i> and <i>&#8211;name</i>. </p>
<p> You may also want to list pools with specified types using <i>type</i>, the pool types must be separated by comma, e.g. &#8211;type dir,disk. The valid pool types include &#8216;dir&#8217;, &#8216;fs&#8217;, &#8216;netfs&#8217;, &#8216;logical&#8217;, &#8216;disk&#8217;, &#8216;iscsi&#8217;, &#8216;scsi&#8217;, &#8216;mpath&#8217;, &#8216;rbd&#8217;, &#8216;sheepdog&#8217; and &#8216;gluster&#8217;. </p>
<p> The <i>&#8211;details</i> option instructs virsh to additionally display pool persistence and capacity related information where available. </p>
<p> NOTE: When talking to older servers, this command is forced to use a series of API calls with an inherent race, where a pool might not be listed or might appear more than once if it changed state between calls while the list was being collected. Newer servers do not have this problem.</p>
<dt><code>pool-name</code> <i>uuid</i></dt>
<dd> Convert the <i>uuid</i> to a pool name.</dd>
<dt><code>pool-refresh</code> <i>pool-or-uuid</i></dt>
<dd> Refresh the list of volumes contained in <i>pool</i>.</dd>
<dt><code>pool-start</code> <i>pool-or-uuid</i> [<i>&#8211;build</i>] [[<i>&#8211;overwrite</i>] | [<i>&#8211;no-overwrite</i>]]</dt>
<dd> Start the storage <i>pool</i>, which is previously defined but inactive. </dd>
<p> [<i>&#8211;build</i>] [[<i>&#8211;overwrite</i>] | [<i>&#8211;no-overwrite</i>]] perform a <code>pool-build</code> prior to <code>pool-start</code> to ensure the pool environment is in an expected state rather than needing to run the build command prior to startup. The <i>&#8211;overwrite</i> and <i>&#8211;no-overwrite</i> flags follow the same rules as <code>pool-build</code>. If just <i>&#8211;build</i> is provided, then <code>pool-build</code> is called with no flags. </p>
<p> <code>Note</code>: A storage pool that relies on remote resources such as an &#8220;iscsi&#8221; or a (v)HBA backed &#8220;scsi&#8221; pool may need to be refreshed multiple times in order to have all the volumes detected (see <code>pool-refresh</code>). This is because the corresponding volume devices may not be present in the host&#8217;s filesystem during the initial pool startup or the current refresh attempt. The number of refresh retries is dependent upon the network connection and the time the host takes to export the corresponding devices.</p>
<dt><code>pool-undefine</code> <i>pool-or-uuid</i></dt>
<dd> Undefine the configuration for an inactive <i>pool</i>.</dd>
<dt><code>pool-uuid</code> <i>pool</i></dt>
<dd> Returns the UUID of the named <i>pool</i>.</dd>
<dt><code>pool-event</code> {[<i>pool</i>] <i>event</i> [<i>&#8211;loop</i>] [<i>&#8211;timeout</i> <i>seconds</i>] [<i>&#8211;timestamp</i>] | <i>&#8211;list</i>}</dt>
<dd> Wait for a class of storage pool events to occur, and print appropriate details of events as they happen. The events can optionally be filtered by <i>pool</i>. Using <i>&#8211;list</i> as the only argument will provide a list of possible <i>event</i> values known by this client, although the connection might not allow registering for all these events. </dd>
<p> By default, this command is one-shot, and returns success once an event occurs; you can send SIGINT (usually via <tt>&quot;Ctrl-C&quot;</tt>) to quit immediately. If <i>&#8211;timeout</i> is specified, the command gives up waiting for events after <i>seconds</i> have elapsed. With <i>&#8211;loop</i>, the command prints all events until a timeout or interrupt key. </p>
<p> When <i>&#8211;timestamp</i> is used, a human-readable timestamp will be printed before the event.</dl>
<h2>VOLUME COMMANDS</h2>
<dl>
<dt><code>vol-create</code> <i>pool-or-uuid</i> <i></i><i>FILE</i><i></i> [<i>&#8211;prealloc-metadata</i>]</dt>
<dd> Create a volume from an XML &lt;file&gt;. <i>pool-or-uuid</i> is the name or UUID of the storage pool to create the volume in. <i></i><i>FILE</i><i></i> is the XML &lt;file&gt; with the volume definition. An easy way to create the XML &lt;file&gt; is to use the <code>vol-dumpxml</code> command to obtain the definition of a pre-existing volume. [<i>&#8211;prealloc-metadata</i>] preallocate metadata (for qcow2 images which don&#8217;t support full allocation). This option creates a sparse image file with metadata, resulting in higher performance compared to images with no preallocation and only slightly higher initial disk space usage. </dd>
<p> <code>Example</code> </p>
<pre>
 virsh vol-dumpxml --pool storagepool1 appvolume1 &gt; newvolume.xml
 vi newvolume.xml (or make changes with your other text editor)
 virsh vol-create differentstoragepool newvolume.xml
</pre>
<dt><code>vol-create-from</code> <i>pool-or-uuid</i> <i></i><i>FILE</i><i></i> [<i>&#8211;inputpool</i> <i>pool-or-uuid</i>] <i>vol-name-or-key-or-path</i> [<i>&#8211;prealloc-metadata</i>] [<i>&#8211;reflink</i>]</dt>
<dd> Create a volume, using another volume as input. <i>pool-or-uuid</i> is the name or UUID of the storage pool to create the volume in. <i></i><i>FILE</i><i></i> is the XML &lt;file&gt; with the volume definition. <i>&#8211;inputpool</i> <i>pool-or-uuid</i> is the name or uuid of the storage pool the source volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the source volume. [<i>&#8211;prealloc-metadata</i>] preallocate metadata (for qcow2 images which don&#8217;t support full allocation). This option creates a sparse image file with metadata, resulting in higher performance compared to images with no preallocation and only slightly higher initial disk space usage. When <i>&#8211;reflink</i> is specified, perform a COW lightweight copy, where the data blocks are copied only when modified. If this is not possible, the copy fails.</dd>
<dt><code>vol-create-as</code> <i>pool-or-uuid</i> <i>name</i> <i>capacity</i> [<i>&#8211;allocation</i> <i>size</i>] [<i>&#8211;format</i> <i>string</i>] [<i>&#8211;backing-vol</i> <i>vol-name-or-key-or-path</i>] [<i>&#8211;backing-vol-format</i> <i>string</i>] [<i>&#8211;prealloc-metadata</i>] [<i>&#8211;print-xml</i>]</dt>
<dd> Create a volume from a set of arguments unless <i>&#8211;print-xml</i> is specified, in which case just the XML of the volume object is printed out without any actual object creation. <i>pool-or-uuid</i> is the name or UUID of the storage pool to create the volume in. <i>name</i> is the name of the new volume. For a disk pool, this must match the partition name as determined from the pool&#8217;s source device path and the next available partition. For example, a source device path of /dev/sdb and there are no partitions on the disk, then the name must be sdb1 with the next name being sdb2 and so on. <i>capacity</i> is the size of the volume to be created, as a scaled integer (see <code>NOTES</code> above), defaulting to bytes if there is no suffix. <i>&#8211;allocation</i> <i>size</i> is the initial size to be allocated in the volume, also as a scaled integer defaulting to bytes. <i>&#8211;format</i> <i>string</i> is used in file based storage pools to specify the volume file format to use; raw, bochs, qcow, qcow2, vmdk, qed. Use extended for disk storage pools in order to create an extended partition (other values are validity checked but not preserved when libvirtd is restarted or the pool is refreshed). <i>&#8211;backing-vol</i> <i>vol-name-or-key-or-path</i> is the source backing volume to be used if taking a snapshot of an existing volume. <i>&#8211;backing-vol-format</i> <i>string</i> is the format of the snapshot backing volume; raw, bochs, qcow, qcow2, qed, vmdk, host_device. These are, however, meant for file based storage pools. [<i>&#8211;prealloc-metadata</i>] preallocate metadata (for qcow2 images which don&#8217;t support full allocation). This option creates a sparse image file with metadata, resulting in higher performance compared to images with no preallocation and only slightly higher initial disk space usage.</dd>
<dt><code>vol-clone</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-key-or-path</i> <i>name</i> [<i>&#8211;prealloc-metadata</i>] [<i>&#8211;reflink</i>]</dt>
<dd> Clone an existing volume within the parent pool. Less powerful, but easier to type, version of <code>vol-create-from</code>. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool that contains the source volume, and will contain the new volume. <i>vol-name-or-key-or-path</i> is the name or key or path of the source volume. <i>name</i> is the name of the new volume. [<i>&#8211;prealloc-metadata</i>] preallocate metadata (for qcow2 images which don&#8217;t support full allocation). This option creates a sparse image file with metadata, resulting in higher performance compared to images with no preallocation and only slightly higher initial disk space usage. When <i>&#8211;reflink</i> is specified, perform a COW lightweight copy, where the data blocks are copied only when modified. If this is not possible, the copy fails.</dd>
<dt><code>vol-delete</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-key-or-path</i> [<i>&#8211;delete-snapshots</i>]</dt>
<dd> Delete a given volume. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume to delete. </dd>
<p> The <i>&#8211;delete-snapshots</i> flag specifies that any snapshots associated with the storage volume should be deleted as well. Not all storage drivers support this option, presently only rbd.</p>
<dt><code>vol-upload</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] [<i>&#8211;offset</i> <i>bytes</i>] [<i>&#8211;length</i> <i>bytes</i>] <i>vol-name-or-key-or-path</i> <i>local-file</i></dt>
<dd> Upload the contents of <i>local-file</i> to a storage volume. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume where the file will be uploaded. <i>&#8211;offset</i> is the position in the storage volume at which to start writing the data. The value must be 0 or larger. <i>&#8211;length</i> is an upper bound of the amount of data to be uploaded. A negative value is interpreted as an unsigned long long value to essentially include everything from the offset to the end of the volume. An error will occur if the <i>local-file</i> is greater than the specified length. See the description for the libvirt virStorageVolUpload API for details regarding possible target volume and pool changes as a result of the pool refresh when the upload is attempted.</dd>
<dt><code>vol-download</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] [<i>&#8211;offset</i> <i>bytes</i>] [<i>&#8211;length</i> <i>bytes</i>] <i>vol-name-or-key-or-path</i> <i>local-file</i></dt>
<dd> Download the contents of a storage volume to <i>local-file</i>. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume to download. <i>&#8211;offset</i> is the position in the storage volume at which to start reading the data. The value must be 0 or larger. <i>&#8211;length</i> is an upper bound of the amount of data to be downloaded. A negative value is interpreted as an unsigned long long value to essentially include everything from the offset to the end of the volume.</dd>
<dt><code>vol-wipe</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] [<i>&#8211;algorithm</i> <i>algorithm</i>] <i>vol-name-or-key-or-path</i></dt>
<dd> Wipe a volume, ensure data previously on the volume is not accessible to future reads. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume to wipe. It is possible to choose different wiping algorithms instead of re-writing volume with zeroes. This can be done via <i>&#8211;algorithm</i> switch. </dd>
<p> <code>Supported algorithms</code><br/>
&nbsp;<wbr>&nbsp;<wbr>zero&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 1-pass all zeroes<br/>
&nbsp;<wbr>&nbsp;<wbr>nnsa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 4-pass&nbsp;<wbr>NNSA&nbsp;<wbr>Policy Letter&nbsp;<wbr>NAP-14.1-C&nbsp;<wbr>(XVI-8)&nbsp;<wbr>for<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sanitizing removable and non-removable hard disks:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>random x2, 0x00, verify.<br/>
&nbsp;<wbr>&nbsp;<wbr>dod&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 4-pass DoD 5220.22-M section 8-306 procedure for<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sanitizing removable and non-removable rigid<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disks: random, 0x00, 0xff, verify.<br/>
&nbsp;<wbr>&nbsp;<wbr>bsi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 9-pass method recommended by the German Center of<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Security in Information Technologies<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(<a rel="nofollow" href="http://www.bsi.bund.de">http://www.bsi.bund.de</a>):&nbsp;<wbr>0xff, 0xfe, 0xfd, 0xfb,<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0xf7, 0xef, 0xdf, 0xbf, 0x7f.<br/>
&nbsp;<wbr>&nbsp;<wbr>gutmann&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The canonical 35-pass sequence described in<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gutmann&#8217;s paper.<br/>
&nbsp;<wbr>&nbsp;<wbr>schneier&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 7-pass method described by Bruce Schneier in<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8220;Applied Cryptography&#8221;&nbsp;<wbr>(1996): 0x00, 0xff,<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>random x5.<br/>
&nbsp;<wbr>&nbsp;<wbr>pfitzner7&nbsp;<wbr>&nbsp;<wbr>&#8211; Roy Pfitzner&#8217;s 7-random-pass method: random x7.<br/>
&nbsp;<wbr>&nbsp;<wbr>pfitzner33 &#8211; Roy Pfitzner&#8217;s 33-random-pass method: random x33.<br/>
&nbsp;<wbr>&nbsp;<wbr>random&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 1-pass pattern: random.<br/>
&nbsp;<wbr>&nbsp;<wbr>trim&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 1-pass trimming the volume using&nbsp;<wbr>TRIM&nbsp;<wbr>or&nbsp;<wbr>DISCARD </p>
<p> <code>Note</code>: The <tt>&quot;scrub&quot;</tt> binary will be used to handle the &#8216;nnsa&#8217;, &#8216;dod&#8217;, &#8216;bsi&#8217;, &#8216;gutmann&#8217;, &#8216;schneier&#8217;, &#8216;pfitzner7&#8217; and &#8216;pfitzner33&#8217; algorithms. The availability of the algorithms may be limited by the version of the <tt>&quot;scrub&quot;</tt> binary installed on the host. The &#8216;zero&#8217; algorithm will write zeroes to the entire volume. For some volumes, such as sparse or rbd volumes, this may result in completely filling the volume with zeroes making it appear to be completely full. As an alternative, the &#8216;trim&#8217; algorithm does not overwrite all the data in a volume, rather it expects the storage driver to be able to discard all bytes in a volume. It is up to the storage driver to handle how the discarding occurs. Not all storage drivers or volume types can support &#8216;trim&#8217;.</p>
<dt><code>vol-dumpxml</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-key-or-path</i></dt>
<dd> Output the volume information as an XML dump to stdout. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume to output the XML of.</dd>
<dt><code>vol-info</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-key-or-path</i> [<i>&#8211;bytes</i>] [<i>&#8211;physical</i>]</dt>
<dd> Returns basic information about the given storage volume. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume to return information for. If <i>&#8211;bytes</i> is specified the sizes are not converted to human friendly units. If <i>&#8211;physical</i> is specified, then the host physical size is returned and displayed instead of the allocation value. The physical value for some file types, such as qcow2 may have a different (larger) physical value than is shown for allocation. Additionally sparse files will have different physical and allocation values.</dd>
<dt><code>vol-list</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] [<i>&#8211;details</i>]</dt>
<dd> Return the list of volumes in the given storage pool. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool. The <i>&#8211;details</i> option instructs virsh to additionally display volume type and capacity related information where available.</dd>
<dt><code>vol-pool</code> [<i>&#8211;uuid</i>] <i>vol-key-or-path</i></dt>
<dd> Return the pool name or UUID for a given volume. By default, the pool name is returned. If the <i>&#8211;uuid</i> option is given, the pool UUID is returned instead. <i>vol-key-or-path</i> is the key or path of the volume to return the pool information for.</dd>
<dt><code>vol-path</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-key</i></dt>
<dd> Return the path for a given volume. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key</i> is the name or key of the volume to return the path for.</dd>
<dt><code>vol-name</code> <i>vol-key-or-path</i></dt>
<dd> Return the name for a given volume. <i>vol-key-or-path</i> is the key or path of the volume to return the name for.</dd>
<dt><code>vol-key</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-path</i></dt>
<dd> Return the volume key for a given volume. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-path</i> is the name or path of the volume to return the volume key for.</dd>
<dt><code>vol-resize</code> [<i>&#8211;pool</i> <i>pool-or-uuid</i>] <i>vol-name-or-path</i> <i>pool-or-uuid</i> <i>capacity</i> [<i>&#8211;allocate</i>] [<i>&#8211;delta</i>] [<i>&#8211;shrink</i>]</dt>
<dd> Resize the capacity of the given volume, in bytes. <i>&#8211;pool</i> <i>pool-or-uuid</i> is the name or UUID of the storage pool the volume is in. <i>vol-name-or-key-or-path</i> is the name or key or path of the volume to resize. The new capacity might be sparse unless <i>&#8211;allocate</i> is specified. Normally, <i>capacity</i> is the new size, but if <i>&#8211;delta</i> is present, then it is added to the existing size. Attempts to shrink the volume will fail unless <i>&#8211;shrink</i> is present; <i>capacity</i> cannot be negative unless <i>&#8211;shrink</i> is provided, but a negative sign is not necessary. <i>capacity</i> is a scaled integer (see <code>NOTES</code> above), which defaults to bytes if there is no suffix. This command is only safe for storage volumes not in use by an active guest; see also <code>blockresize</code> for live resizing.</dd></dl>
<h2>SECRET COMMANDS</h2>
<p> The following commands manipulate &#8220;secrets&#8221; (e.g. passwords, passphrases and encryption keys). Libvirt can store secrets independently from their use, and other objects (e.g. volumes or domains) can refer to the secrets for encryption or possibly other uses. Secrets are identified using a UUID.  See &lt;<a rel="nofollow" href="http://libvirt.org/formatsecret.html">http://libvirt.org/formatsecret.html</a>&gt; for documentation of the XML format used to represent properties of secrets.</p>
<dl>
<dt><code>secret-define</code> <i>file</i></dt>
<dd> Create a secret with the properties specified in <i>file</i>, with no associated secret value. If <i>file</i> does not specify a UUID, choose one automatically. If <i>file</i> specifies a UUID of an existing secret, replace its properties by properties defined in <i>file</i>, without affecting the secret value.</dd>
<dt><code>secret-dumpxml</code> <i>secret</i></dt>
<dd> Output properties of <i>secret</i> (specified by its UUID) as an XML dump to stdout.</dd>
<dt><code>secret-event</code> {[<i>secret</i>] <i>event</i> [<i>&#8211;loop</i>] [<i>&#8211;timeout</i> <i>seconds</i>] [<i>&#8211;timestamp</i>] | <i>&#8211;list</i>}</dt>
<dd> Wait for a class of secret events to occur, and print appropriate details of events as they happen. The events can optionally be filtered by <i>secret</i>. Using <i>&#8211;list</i> as the only argument will provide a list of possible <i>event</i> values known by this client, although the connection might not allow registering for all these events. </dd>
<p> By default, this command is one-shot, and returns success once an event occurs; you can send SIGINT (usually via <tt>&quot;Ctrl-C&quot;</tt>) to quit immediately. If <i>&#8211;timeout</i> is specified, the command gives up waiting for events after <i>seconds</i> have elapsed. With <i>&#8211;loop</i>, the command prints all events until a timeout or interrupt key. </p>
<p> When <i>&#8211;timestamp</i> is used, a human-readable timestamp will be printed before the event.</p>
<dt><code>secret-set-value</code> <i>secret</i> <i>base64</i></dt>
<dd> Set the value associated with <i>secret</i> (specified by its UUID) to the value Base64-encoded value <i>base64</i>.</dd>
<dt><code>secret-get-value</code> <i>secret</i></dt>
<dd> Output the value associated with <i>secret</i> (specified by its UUID) to stdout, encoded using Base64.</dd>
<dt><code>secret-undefine</code> <i>secret</i></dt>
<dd> Delete a <i>secret</i> (specified by its UUID), including the associated value, if any.</dd>
<dt><code>secret-list</code> [<i>&#8211;ephemeral</i>] [<i>&#8211;no-ephemeral</i>] [<i>&#8211;private</i>] [<i>&#8211;no-private</i>]</dt>
<dd> Returns the list of secrets. You may also want to filter the returned secrets by <i>&#8211;ephemeral</i> to list the ephemeral ones, <i>&#8211;no-ephemeral</i> to list the non-ephemeral ones, <i>&#8211;private</i> to list the private ones, and <i>&#8211;no-private</i> to list the non-private ones.</dd></dl>
<h2>SNAPSHOT COMMANDS</h2>
<p> The following commands manipulate domain snapshots. Snapshots take the disk, memory, and device state of a domain at a point-of-time, and save it for future use. They have many uses, from saving a &#8220;clean&#8221; copy of an OS image to saving a domain&#8217;s state before a potentially destructive operation. Snapshots are identified with a unique name. See &lt;<a rel="nofollow" href="http://libvirt.org/formatsnapshot.html">http://libvirt.org/formatsnapshot.html</a>&gt; for documentation of the XML format used to represent properties of snapshots.</p>
<dl>
<dt><code>snapshot-create</code> <i>domain</i> [<i>xmlfile</i>] {[<i>&#8211;redefine</i> [<i>&#8211;current</i>]] | [<i>&#8211;no-metadata</i>] [<i>&#8211;halt</i>] [<i>&#8211;disk-only</i>] [<i>&#8211;reuse-external</i>] [<i>&#8211;quiesce</i>] [<i>&#8211;atomic</i>] [<i>&#8211;live</i>]}</dt>
<dd> Create a snapshot for domain <i>domain</i> with the properties specified in <i>xmlfile</i>. Normally, the only properties settable for a domain snapshot are the &lt;name&gt; and &lt;description&gt; elements, as well as &lt;disks&gt; if <i>&#8211;disk-only</i> is given; the rest of the fields are ignored, and automatically filled in by libvirt. If <i>xmlfile</i> is completely omitted, then libvirt will choose a value for all fields. The new snapshot will become current, as listed by <code>snapshot-current</code>. </dd>
<p> If <i>&#8211;halt</i> is specified, the domain will be left in an inactive state after the snapshot is created. </p>
<p> If <i>&#8211;disk-only</i> is specified, the snapshot will only include disk state rather than the usual system checkpoint with vm state. Disk snapshots are faster than full system checkpoints, but reverting to a disk snapshot may require fsck or journal replays, since it is like the disk state at the point when the power cord is abruptly pulled; and mixing <i>&#8211;halt</i> and <i>&#8211;disk-only</i> loses any data that was not flushed to disk at the time. </p>
<p> If <i>&#8211;redefine</i> is specified, then all XML elements produced by <code>snapshot-dumpxml</code> are valid; this can be used to migrate snapshot hierarchy from one machine to another, to recreate hierarchy for the case of a transient domain that goes away and is later recreated with the same name and UUID, or to make slight alterations in the snapshot metadata (such as host-specific aspects of the domain XML embedded in the snapshot). When this flag is supplied, the <i>xmlfile</i> argument is mandatory, and the domain&#8217;s current snapshot will not be altered unless the <i>&#8211;current</i> flag is also given. </p>
<p> If <i>&#8211;no-metadata</i> is specified, then the snapshot data is created, but any metadata is immediately discarded (that is, libvirt does not treat the snapshot as current, and cannot revert to the snapshot unless <i>&#8211;redefine</i> is later used to teach libvirt about the metadata again). </p>
<p> If <i>&#8211;reuse-external</i> is specified, and the snapshot XML requests an external snapshot with a destination of an existing file, then the destination must exist and be pre-created with correct format and metadata. The file is then reused; otherwise, a snapshot is refused to avoid losing contents of the existing files. </p>
<p> If <i>&#8211;quiesce</i> is specified, libvirt will try to use guest agent to freeze and unfreeze domain&#8217;s mounted file systems. However, if domain has no guest agent, snapshot creation will fail. Currently, this requires <i>&#8211;disk-only</i> to be passed as well. </p>
<p> If <i>&#8211;atomic</i> is specified, libvirt will guarantee that the snapshot either succeeds, or fails with no changes; not all hypervisors support this. If this flag is not specified, then some hypervisors may fail after partially performing the action, and <code>dumpxml</code> must be used to see whether any partial changes occurred. </p>
<p> If <i>&#8211;live</i> is specified, libvirt takes the snapshot (checkpoint) while the guest is running. Both disk snapshot and domain memory snapshot are taken. This increases the size of the memory image of the external checkpoint. This is currently supported only for external checkpoints. </p>
<p> Existence of snapshot metadata will prevent attempts to <code>undefine</code> a persistent domain. However, for transient domains, snapshot metadata is silently lost when the domain quits running (whether by command such as <code>destroy</code> or by internal guest action).</p>
<dt><code>snapshot-create-as</code> <i>domain</i> {[<i>&#8211;print-xml</i>] | [<i>&#8211;no-metadata</i>] [<i>&#8211;halt</i>] [<i>&#8211;reuse-external</i>]} [<i>name</i>] [<i>description</i>] [<i>&#8211;disk-only</i> [<i>&#8211;quiesce</i>]] [<i>&#8211;atomic</i>] [[<i>&#8211;live</i>] [<i>&#8211;memspec</i> <code>memspec</code>]] [<i>&#8211;diskspec</i>] <code>diskspec</code>]&#8230;</dt>
<dd> Create a snapshot for domain <i>domain</i> with the given &lt;name&gt; and &lt;description&gt;; if either value is omitted, libvirt will choose a value. If <i>&#8211;print-xml</i> is specified, then XML appropriate for <i>snapshot-create</i> is output, rather than actually creating a snapshot. Otherwise, if <i>&#8211;halt</i> is specified, the domain will be left in an inactive state after the snapshot is created, and if <i>&#8211;disk-only</i> is specified, the snapshot will not include vm state. </dd>
<p> The <i>&#8211;memspec</i> option can be used to control whether a checkpoint is internal or external. The <i>&#8211;memspec</i> flag is mandatory, followed by a <code>memspec</code> of the form <code>[file=]name[,snapshot=type]</code>, where type can be <code>no</code>, <code>internal</code>, or <code>external</code>. To include a literal comma in <code>file=name</code>, escape it with a second comma. <i>&#8211;memspec</i> cannot be used together with <i>&#8211;disk-only</i>. </p>
<p> The <i>&#8211;diskspec</i> option can be used to control how <i>&#8211;disk-only</i> and external checkpoints create external files. This option can occur multiple times, according to the number of &lt;disk&gt; elements in the domain xml. Each &lt;diskspec&gt; is in the form <code>disk[,snapshot=type][,driver=type][,file=name]</code>. A <i>diskspec</i> must be provided for disks backed by block devices as libvirt doesn&#8217;t auto-generate file names for those. To include a literal comma in <code>disk</code> or in <code>file=name</code>, escape it with a second comma. A literal <i>&#8211;diskspec</i> must precede each <code>diskspec</code> unless all three of <i>domain</i>, <i>name</i>, and <i>description</i> are also present. For example, a diskspec of &#8220;vda,snapshot=external,file=/path/to,,new&#8221; results in the following XML:<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;disk name=&#8217;vda&#8217;&nbsp;<wbr>snapshot=&#8217;external&#8217;&gt;<br/>
&nbsp;<wbr>&lt;source file=&#8217;/path/to,new&#8217;/&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;/disk&gt; </p>
<p> If <i>&#8211;reuse-external</i> is specified, and the domain XML or <i>diskspec</i> option requests an external snapshot with a destination of an existing file, then the destination must exist and be pre-created with correct format and metadata. The file is then reused; otherwise, a snapshot is refused to avoid losing contents of the existing files. </p>
<p> If <i>&#8211;quiesce</i> is specified, libvirt will try to use guest agent to freeze and unfreeze domain&#8217;s mounted file systems. However, if domain has no guest agent, snapshot creation will fail. Currently, this requires <i>&#8211;disk-only</i> to be passed as well. </p>
<p> If <i>&#8211;no-metadata</i> is specified, then the snapshot data is created, but any metadata is immediately discarded (that is, libvirt does not treat the snapshot as current, and cannot revert to the snapshot unless <code>snapshot-create</code> is later used to teach libvirt about the metadata again). This flag is incompatible with <i>&#8211;print-xml</i>. </p>
<p> If <i>&#8211;atomic</i> is specified, libvirt will guarantee that the snapshot either succeeds, or fails with no changes; not all hypervisors support this. If this flag is not specified, then some hypervisors may fail after partially performing the action, and <code>dumpxml</code> must be used to see whether any partial changes occurred. </p>
<p> If <i>&#8211;live</i> is specified, libvirt takes the snapshot while the guest is running. This increases the size of the memory image of the external checkpoint. This is currently supported only for external checkpoints.</p>
<dt><code>snapshot-current</code> <i>domain</i> {[<i>&#8211;name</i>] | [<i>&#8211;security-info</i>] | [<i>snapshotname</i>]}</dt>
<dd> Without <i>snapshotname</i>, this will output the snapshot XML for the domain&#8217;s current snapshot (if any). If <i>&#8211;name</i> is specified, just the current snapshot name instead of the full xml. Otherwise, using <i>&#8211;security-info</i> will also include security sensitive information in the XML. </dd>
<p> With <i>snapshotname</i>, this is a request to make the existing named snapshot become the current snapshot, without reverting the domain.</p>
<dt><code>snapshot-edit</code> <i>domain</i> [<i>snapshotname</i>] [<i>&#8211;current</i>] {[<i>&#8211;rename</i>] | [<i>&#8211;clone</i>]}</dt>
<dd> Edit the XML configuration file for <i>snapshotname</i> of a domain. If both <i>snapshotname</i> and <i>&#8211;current</i> are specified, also force the edited snapshot to become the current snapshot. If <i>snapshotname</i> is omitted, then <i>&#8211;current</i> must be supplied, to edit the current snapshot. </dd>
<p> This is equivalent to: </p>
<pre><code>
virsh snapshot - dumpxml dom name &gt; snapshot.xml
                                            vi snapshot.xml(or make changes with your other text editor)
                                                virsh snapshot
                                        - create dom snapshot.xml-- redefine[--current]
</code></pre>
<p> except that it does some error checking. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>. </p>
<p> If <i>&#8211;rename</i> is specified, then the edits can change the snapshot name. If <i>&#8211;clone</i> is specified, then changing the snapshot name will create a clone of the snapshot metadata. If neither is specified, then the edits must not change the snapshot name. Note that changing a snapshot name must be done with care, since the contents of some snapshots, such as internal snapshots within a single qcow2 file, are accessible only from the original name.</p>
<dt><code>snapshot-info</code> <i>domain</i> {<i>snapshot</i> | <i>&#8211;current</i>}</dt>
<dd> Output basic information about a named &lt;snapshot&gt;, or the current snapshot with <i>&#8211;current</i>.</dd>
<dt><code>snapshot-list</code> <i>domain</i> [<i>&#8211;metadata</i>] [<i>&#8211;no-metadata</i>] [{<i>&#8211;parent</i> | <i>&#8211;roots</i> | [{<i>&#8211;tree</i> | <i>&#8211;name</i>}]}] [{[<i>&#8211;from</i>] <code>snapshot</code> | <i>&#8211;current</i>} [<i>&#8211;descendants</i>]] [<i>&#8211;leaves</i>] [<i>&#8211;no-leaves</i>] [<i>&#8211;inactive</i>] [<i>&#8211;active</i>] [<i>&#8211;disk-only</i>] [<i>&#8211;internal</i>] [<i>&#8211;external</i>]</dt>
<dd> List all of the available snapshots for the given domain, defaulting to show columns for the snapshot name, creation time, and domain state. </dd>
<p> If <i>&#8211;parent</i> is specified, add a column to the output table giving the name of the parent of each snapshot. If <i>&#8211;roots</i> is specified, the list will be filtered to just snapshots that have no parents. If <i>&#8211;tree</i> is specified, the output will be in a tree format, listing just snapshot names. These three options are mutually exclusive. If <i>&#8211;name</i> is specified only the snapshot name is printed. This option is mutually exclusive with <i>&#8211;tree</i>. </p>
<p> If <i>&#8211;from</i> is provided, filter the list to snapshots which are children of the given <code>snapshot</code>; or if <i>&#8211;current</i> is provided, start at the current snapshot. When used in isolation or with <i>&#8211;parent</i>, the list is limited to direct children unless <i>&#8211;descendants</i> is also present. When used with <i>&#8211;tree</i>, the use of <i>&#8211;descendants</i> is implied. This option is not compatible with <i>&#8211;roots</i>. Note that the starting point of <i>&#8211;from</i> or <i>&#8211;current</i> is not included in the list unless the <i>&#8211;tree</i> option is also present. </p>
<p> If <i>&#8211;leaves</i> is specified, the list will be filtered to just snapshots that have no children. Likewise, if <i>&#8211;no-leaves</i> is specified, the list will be filtered to just snapshots with children. (Note that omitting both options does no filtering, while providing both options will either produce the same list or error out depending on whether the server recognizes the flags). Filtering options are not compatible with <i>&#8211;tree</i>. </p>
<p> If <i>&#8211;metadata</i> is specified, the list will be filtered to just snapshots that involve libvirt metadata, and thus would prevent <code>undefine</code> of a persistent domain, or be lost on <code>destroy</code> of a transient domain. Likewise, if <i>&#8211;no-metadata</i> is specified, the list will be filtered to just snapshots that exist without the need for libvirt metadata. </p>
<p> If <i>&#8211;inactive</i> is specified, the list will be filtered to snapshots that were taken when the domain was shut off. If <i>&#8211;active</i> is specified, the list will be filtered to snapshots that were taken when the domain was running, and where the snapshot includes the memory state to revert to that running state. If <i>&#8211;disk-only</i> is specified, the list will be filtered to snapshots that were taken when the domain was running, but where the snapshot includes only disk state. </p>
<p> If <i>&#8211;internal</i> is specified, the list will be filtered to snapshots that use internal storage of existing disk images. If <i>&#8211;external</i> is specified, the list will be filtered to snapshots that use external files for disk images or memory state.</p>
<dt><code>snapshot-dumpxml</code> <i>domain</i> <i>snapshot</i> [<i>&#8211;security-info</i>]</dt>
<dd> Output the snapshot XML for the domain&#8217;s snapshot named <i>snapshot</i>. Using <i>&#8211;security-info</i> will also include security sensitive information. Use <code>snapshot-current</code> to easily access the XML of the current snapshot.</dd>
<dt><code>snapshot-parent</code> <i>domain</i> {<i>snapshot</i> | <i>&#8211;current</i>}</dt>
<dd> Output the name of the parent snapshot, if any, for the given <i>snapshot</i>, or for the current snapshot with <i>&#8211;current</i>.</dd>
<dt><code>snapshot-revert</code> <i>domain</i> {<i>snapshot</i> | <i>&#8211;current</i>} [{<i>&#8211;running</i> | <i>&#8211;paused</i>}] [<i>&#8211;force</i>]</dt>
<dd> Revert the given domain to the snapshot specified by <i>snapshot</i>, or to the current snapshot with <i>&#8211;current</i>. Be aware that this is a destructive action; any changes in the domain since the last snapshot was taken will be lost. Also note that the state of the domain after snapshot-revert is complete will be the state of the domain at the time the original snapshot was taken. </dd>
<p> Normally, reverting to a snapshot leaves the domain in the state it was at the time the snapshot was created, except that a disk snapshot with no vm state leaves the domain in an inactive state. Passing either the <i>&#8211;running</i> or <i>&#8211;paused</i> flag will perform additional state changes (such as booting an inactive domain, or pausing a running domain). Since transient domains cannot be inactive, it is required to use one of these flags when reverting to a disk snapshot of a transient domain. </p>
<p> There are two cases where a snapshot revert involves extra risk, which requires the use of <i>&#8211;force</i> to proceed. One is the case of a snapshot that lacks full domain information for reverting configuration (such as snapshots created prior to libvirt 0.9.5); since libvirt cannot prove that the current configuration matches what was in use at the time of the snapshot, supplying <i>&#8211;force</i> assures libvirt that the snapshot is compatible with the current configuration (and if it is not, the domain will likely fail to run). The other is the case of reverting from a running domain to an active state where a new hypervisor has to be created rather than reusing the existing hypervisor, because it implies drawbacks such as breaking any existing VNC or Spice connections; this condition happens with an active snapshot that uses a provably incompatible configuration, as well as with an inactive snapshot that is combined with the <i>&#8211;start</i> or <i>&#8211;pause</i> flag.</p>
<dt><code>snapshot-delete</code> <i>domain</i> {<i>snapshot</i> | <i>&#8211;current</i>} [<i>&#8211;metadata</i>] [{<i>&#8211;children</i> | <i>&#8211;children-only</i>}]</dt>
<dd> Delete the snapshot for the domain named <i>snapshot</i>, or the current snapshot with <i>&#8211;current</i>. If this snapshot has child snapshots, changes from this snapshot will be merged into the children. If <i>&#8211;children</i> is passed, then delete this snapshot and any children of this snapshot. If <i>&#8211;children-only</i> is passed, then delete any children of this snapshot, but leave this snapshot intact. These two flags are mutually exclusive. </dd>
<p> If <i>&#8211;metadata</i> is specified, then only delete the snapshot metadata maintained by libvirt, while leaving the snapshot contents intact for access by external tools; otherwise deleting a snapshot also removes the data contents from that point in time.</dl>
<h2>NWFILTER COMMANDS</h2>
<p> The following commands manipulate network filters. Network filters allow filtering of the network traffic coming from and going to virtual machines. Individual network traffic filters are written in XML and may contain references to other network filters, describe traffic filtering rules, or contain both. Network filters are referenced by virtual machines from within their interface description. A network filter may be referenced by multiple virtual machines&#8217; interfaces.</p>
<dl>
<dt><code>nwfilter-define</code> <i>xmlfile</i></dt>
<dd> Make a new network filter known to libvirt. If a network filter with the same name already exists, it will be replaced with the new XML. Any running virtual machine referencing this network filter will have its network traffic rules adapted. If for any reason the network traffic filtering rules cannot be instantiated by any of the running virtual machines, then the new XML will be rejected.</dd>
<dt><code>nwfilter-undefine</code> <i>nwfilter-name</i></dt>
<dd> Delete a network filter. The deletion will fail if any running virtual machine is currently using this network filter.</dd>
<dt><code>nwfilter-list</code></dt>
<dd> List all of the available network filters.</dd>
<dt><code>nwfilter-dumpxml</code> <i>nwfilter-name</i></dt>
<dd> Output the network filter XML.</dd>
<dt><code>nwfilter-edit</code> <i>nwfilter-name</i></dt>
<dd> Edit the XML of a network filter. </dd>
<p> This is equivalent to: </p>
<pre>
 virsh nwfilter-dumpxml myfilter &gt; myfilter.xml
 vi myfilter.xml (or make changes with your other text editor)
 virsh nwfilter-define myfilter.xml
</pre>
<p> except that it does some error checking. The new network filter may be rejected due to the same reason as mentioned in <i>nwfilter-define</i>. </p>
<p> The editor used can be supplied by the <tt>$VISUAL</tt> or <tt>$EDITOR</tt> environment variables, and defaults to <tt>&quot;vi&quot;</tt>.</dl>
<h2>HYPERVISOR-SPECIFIC COMMANDS</h2>
<p> NOTE: Use of the following commands is <code>strongly</code> discouraged. They can cause libvirt to become confused and do the wrong thing on subsequent operations. Once you have used these commands, please do not report problems to the libvirt developers; the reports will be ignored. If you find that these commands are the only way to accomplish something, then it is better to request that the feature be added as a first-class citizen in the regular libvirt library.</p>
<dl>
<dt><code>qemu-attach</code> <i>pid</i></dt>
<dd> Attach an externally launched QEMU process to the libvirt QEMU driver. The QEMU process must have been created with a monitor connection using the UNIX driver. Ideally the process will also have had the &#8216;-name&#8217; argument specified.</dd>
<dl>
<dt>
</dt><dd>
<pre>
     $ qemu-kvm -cdrom ~/demo.iso \
         -monitor unix:/tmp/demo,server,nowait \
         -name foo \
         -uuid cece4f9f-dff0-575d-0e8e-01fe380f12ea  &amp;
     $ QEMUPID=$!
     $ virsh qemu-attach $QEMUPID
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<p> Not all functions of libvirt are expected to work reliably after attaching to an externally launched QEMU process. There may be issues with the guest ABI changing upon migration and device hotplug or hotunplug may not work. The attached environment should be considered primarily read-only.</dd></dl>
<dt><code>qemu-monitor-command</code> <i>domain</i> { [<i>&#8211;hmp</i>] | [<i>&#8211;pretty</i>] } <i>command</i>&#8230;</dt>
<dd> Send an arbitrary monitor command <i>command</i> to domain <i>domain</i> through the qemu monitor. The results of the command will be printed on stdout. If <i>&#8211;hmp</i> is passed, the command is considered to be a human monitor command and libvirt will automatically convert it into QMP if needed. In that case the result will also be converted back from QMP.  If <i>&#8211;pretty</i> is given, and the monitor uses QMP, then the output will be pretty-printed. If more than one argument is provided for <i>command</i>, they are concatenated with a space in between before passing the single command to the monitor.</dd>
<dt><code>qemu-agent-command</code> <i>domain</i> [<i>&#8211;timeout</i> <i>seconds</i> | <i>&#8211;async</i> | <i>&#8211;block</i>] <i>command</i>&#8230;</dt>
<dd> Send an arbitrary guest agent command <i>command</i> to domain <i>domain</i> through qemu agent. <i>&#8211;timeout</i>, <i>&#8211;async</i> and <i>&#8211;block</i> options are exclusive. <i>&#8211;timeout</i> requires timeout seconds <i>seconds</i> and it must be positive. When <i>&#8211;aysnc</i> is given, the command waits for timeout whether success or failed. And when <i>&#8211;block</i> is given, the command waits forever with blocking timeout.</dd>
<dt><code>qemu-monitor-event</code> [<i>domain</i>] [<i>&#8211;event</i> <i>event-name</i>] [<i>&#8211;loop</i>] [<i>&#8211;timeout</i> <i>seconds</i>] [<i>&#8211;pretty</i>] [<i>&#8211;regex</i>] [<i>&#8211;no-case</i>] [<i>&#8211;timestamp</i>]</dt>
<dd> Wait for arbitrary QEMU monitor events to occur, and print out the details of events as they happen. The events can optionally be filtered by <i>domain</i> or <i>event-name</i>. The &#8216;query-events&#8217; QMP command can be used via <i>qemu-monitor-command</i> to learn what events are supported. If <i>&#8211;regex</i> is used, <i>event-name</i> is a basic regular expression instead of a literal string. If <i>&#8211;no-case</i> is used, <i>event-name</i> will match case-insensitively. </dd>
<p> By default, this command is one-shot, and returns success once an event occurs; you can send SIGINT (usually via <tt>&quot;Ctrl-C&quot;</tt>) to quit immediately. If <i>&#8211;timeout</i> is specified, the command gives up waiting for events after <i>seconds</i> have elapsed. With <i>&#8211;loop</i>, the command prints all events until a timeout or interrupt key. If <i>&#8211;pretty</i> is specified, any JSON event details are pretty-printed for better legibility. </p>
<p> When <i>&#8211;timestamp</i> is used, a human-readable timestamp will be printed before the event, and the timing information provided by QEMU will be omitted.</p>
<dt><code>lxc-enter-namespace</code> <i>domain</i> [<i>&#8211;noseclabel</i>] &#8212; /path/to/binary [arg1, [arg2, &#8230;]]</dt>
<dd> Enter the namespace of <i>domain</i> and execute the command <tt>&quot;/path/to/binary&quot;</tt> passing the requested args. The binary path is relative to the container root filesystem, not the host root filesystem. The binary will inherit the environment variables / console visible to virsh. The command will be run with the same sVirt context and cgroups placement as processes within the container. This command only works when connected to the LXC hypervisor driver. This command succeeds only if <tt>&quot;/path/to/binary&quot;</tt> has 0 exit status. </dd>
<p> By default the new process will run with the security label of the new parent container. Use the <i>&#8211;noseclabel</i> option to instead have the process keep the same security label as <tt>&quot;virsh&quot;</tt>.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables can be set to alter the behaviour of <tt>&quot;virsh&quot;</tt></p>
<dl>
<dt>VIRSH_DEBUG=&lt;0 to 4&gt;</dt>
<dd> Turn on verbose debugging of virsh commands. Valid levels are</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> VIRSH_DEBUG=0 </dd>
<p> DEBUG &#8211; Messages at ALL levels get logged</p>
<dt>&bull;</dt>
<dd> VIRSH_DEBUG=1 </dd>
<p> INFO &#8211; Logs messages at levels INFO, NOTICE, WARNING and ERROR</p>
<dt>&bull;</dt>
<dd> VIRSH_DEBUG=2 </dd>
<p> NOTICE &#8211; Logs messages at levels NOTICE, WARNING and ERROR</p>
<dt>&bull;</dt>
<dd> VIRSH_DEBUG=3 </dd>
<p> WARNING &#8211; Logs messages at levels WARNING and ERROR</p>
<dt>&bull;</dt>
<dd> VIRSH_DEBUG=4 </dd>
<p> ERROR &#8211; Messages at only ERROR level gets logged.</dl>
</dl>
<dl>
</dl>
<dt>VIRSH_LOG_FILE=&quot;LOGFILE&quot;</dt>
<dd> The file to log virsh debug messages.</dd>
<dt>VIRSH_DEFAULT_CONNECT_URI</dt>
<dd> The hypervisor to connect to by default. Set this to a URI, in the same format as accepted by the <code>connect</code> option. This environment variable is deprecated in favour of the global <code>LIBVIRT_DEFAULT_URI</code> variable which serves the same purpose.</dd>
<dt>LIBVIRT_DEFAULT_URI</dt>
<dd> The hypervisor to connect to by default. Set this to a URI, in the same format as accepted by the <code>connect</code> option. This overrides the default URI set in any client config file and prevents libvirt from probing for drivers.</dd>
<dt>VISUAL</dt>
<dd> The editor to use by the <code>edit</code> and related options.</dd>
<dt>EDITOR</dt>
<dd> The editor to use by the <code>edit</code> and related options, if <tt>&quot;VISUAL&quot;</tt> is not set.</dd>
<dt>VIRSH_HISTSIZE</dt>
<dd> The number of commands to remember in the command history. The default value is 500.</dd>
<dt>LIBVIRT_DEBUG=LEVEL</dt>
<dd> Turn on verbose debugging of all libvirt API calls. Valid levels are</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> LIBVIRT_DEBUG=1 </dd>
<p> Messages at level DEBUG or above</p>
<dt>&bull;</dt>
<dd> LIBVIRT_DEBUG=2 </dd>
<p> Messages at level INFO or above</p>
<dt>&bull;</dt>
<dd> LIBVIRT_DEBUG=3 </dd>
<p> Messages at level WARNING or above</p>
<dt>&bull;</dt>
<dd> LIBVIRT_DEBUG=4 </dd>
<p> Messages at level ERROR</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> For further information about debugging options consult &lt;<a rel="nofollow" href="http://libvirt.org/logging.html">http://libvirt.org/logging.html</a>&gt;</dd></dl>
</dl>
<h2>BUGS</h2>
<p> Report any bugs discovered to the libvirt community via the mailing list &lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt; or bug tracker &lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;. Alternatively report bugs to your software distributor / vendor.</p>
<h2>AUTHORS</h2>
<pre>
  Please refer to the AUTHORS file distributed with libvirt.
  Based on the xm man page by:
  Sean Dague &lt;sean at dague dot net&gt;
  Daniel Stekloff &lt;dsteklof at us dot ibm dot com&gt;
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005, 2007-2015 Red Hat, Inc., and the authors listed in the libvirt AUTHORS file.</p>
<h2>LICENSE</h2>
<p> virsh is distributed under the terms of the GNU LGPL v2+. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1), <i><a href="/docs/linux/man/1-virt-xml-validate/">virt-xml-validate</a></i>(1), <i><a href="/docs/linux/man/1-virt-top/">virt-top</a></i>(1), <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt; </p>
