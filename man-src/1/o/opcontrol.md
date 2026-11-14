---
title: "opcontrol(1)"
name: "opcontrol"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opcontrol/"
description: "opcontrol – control OProfile profiling"
---

<h2 class="name">NAME</h2>
<p> opcontrol &#8211; control OProfile profiling </p>
<h2>SYNOPSIS</h2>
<p> <code>opcontrol</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>opcontrol</code> can be used to start profiling, end a profiling session, dump profile data, and set up the profiling parameters. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help / -?</code></p>
<dd> Show help message. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show version. </p>
<dt><code>&#8211;list-events / -l</code></p>
<dd> Shows the monitorable events. </p>
<dt><code>&#8211;init</code></p>
<dd> Load the OProfile module if required and make the OProfile driver interface available. </p>
<dt><code>&#8211;setup</code></p>
<dd> Followed by list options for profiling setup. Store setup in ~root/.oprofile/daemonrc. Optional. </p>
<dt><code>&#8211;status</code></p>
<dd> Show configuration information. </p>
<dt><code>&#8211;start-daemon</code></p>
<dd> Start the oprofile daemon without starting profiling. </p>
<dt><code>&#8211;start / -s</code></p>
<dd> Start data collection with either arguments provided by &#8211;setup or with information saved in ~root/.oprofile/daemonrc. </p>
<dt><code>&#8211;dump / -d</code></p>
<dd> Force a flush of the collected profiling data to the daemon. </p>
<dt><code>&#8211;stop / -t</code></p>
<dd> Stop data collection. </p>
<dt><code>&#8211;shutdown / -h</code></p>
<dd> Stop data collection and kill the daemon. </p>
<dt><code>&#8211;reset</code></p>
<dd> Clear out data from current session, but leaves saved sessions. </p>
<dt><code>&#8211;save=sessionname</code></p>
<dd> Save data from current session to sessionname. </p>
<dt><code>&#8211;deinit</code></p>
<dd> Shut down daemon. Unload the oprofile module and oprofilefs. </p>
<dt><code>&#8211;session-dir=dir_path</code></p>
<dd> Use sample database out of directory dir_path instead of the default location (/var/lib/oprofile). </p>
<dt><code>&#8211;buffer-size=num</code></p>
<dd> Set kernel buffer to num samples. The buffer watershed needs to be tweaked when changing this value. Rules: A non-zero value goes into effect after a &#8216;&#8211;shutdown/start&#8217; sequence. A value of zero sets this parameter back to default value, but does not go into effect until after &#8216;&#8211;deinit/init&#8217; sequence. </p>
<dt><code>&#8211;buffer-watershed=num</code></p>
<dd> Set kernel buffer watershed to num samples. When buffer-size &#8211; buffer-watershed free entries remain in the kernel buffer, data will be flushed to the daemon. Most useful values are in the range [0.25 &#8211; 0.5] * buffer-size. Same rules as defined for buffer-size. </p>
<dt><code>&#8211;cpu-buffer-size=num</code></p>
<dd> Set kernel per-cpu buffer to num samples. If you profile at high rate it can help to increase this if the log file show excessive count of sample lost cpu buffer overflow. Same rules as defined for buffer-size. </p>
<dt><code>&#8211;event / -e [event|default]</code></p>
<dd> Specify an event to measure for the hardware performance counters, or &quot;default&quot; for the default event. The event is of the form &quot;CPU_CLK_UNHALTED:30000:0:1:1&quot; where the numeric values are count, unit mask, kernel-space counting, user-space counting, respectively. Note that this over-rides all previous events selected; if you want to profile with two or more events simultaneously, you must specify them on the same opcontrol invocation. You can specify unit mask values using either a numerical value (hex values <i>must</i> begin with &quot;0x&quot;) or a symbolic name (if the <i>name=&lt;um_name&gt;</i> field is shown in the <code>ophelp</code> output). For some named unit masks, the hex value is not unique; thus, OProfile tools enforce specifying such unit masks value by name. </p>
<dt><code>&#8211;separate / -p [none,lib,kernel,thread,cpu,all]</code></p>
<dd> Separate samples based on the given separator. &#8216;lib&#8217; separates dynamically linked library samples per application. &#8216;kernel&#8217; separates kernel and kernel module samples per application; &#8216;kernel&#8217; implies &#8216;library&#8217;. &#8216;thread&#8217; gives separation for each thread and task. &#8216;cpu&#8217; separates for each CPU. &#8216;all&#8217; implies all of the above options and &#8216;none&#8217; turns off separation. </p>
<dt><code>&#8211;callgraph / -c [#depth]</code></p>
<dd> Enable callgraph sample collection with a maximum depth. Use 0 to disable callgraph profiling. This option is available on x86 using a 2.6+ kernel with callgraph support enabled. It is also available on PowerPC using a 2.6.17+ kernel. </p>
<dt><code>&#8211;image / -i [name,name&#8230;|all]</code></p>
<dd> Only profile the given absolute paths to binaries, or &quot;all&quot; to profile everything (the default). </p>
<dt><code>&#8211;vmlinux=file</code></p>
<dd> vmlinux kernel image. </p>
<dt><code>&#8211;no-vmlinux</code></p>
<dd> Use this when you don&#8217;t have a kernel vmlinux file, and you don&#8217;t want to profile the kernel. </p>
<dt><code>&#8211;verbose / -V [options]</code></p>
<dd> Be verbose in the daemon log. This has a high overhead. </p>
<dt><code>&#8211;kernel-range=start,end</code></p>
<dd> Set kernel range vma address in hexadecimal. </p>
</dl>
<h2>OPTIONS (specific to Xen)</h2>
<dl>
<dt><code>&#8211;xen=file</code></p>
<dd> Xen image </p>
<dt><code>&#8211;active-domains=&lt;list&gt;</code></p>
<dd> List of domain ids participating in a multi-domain profiling session. Each of the specified domains must run an instance of oprofile. The sequence of opcontrol commands in each domain must follow a given order which is specified in the oprofile user manual. If more than one domain is specified in &lt;list&gt; they should be separated using commas. This option can only be used in domain 0 which is the only domain that can coordinate a multi-domain profiling session. Including domain 0 in the list of active domains is optional. (e.g. &#8211;active-domains=2,5,6 and &#8211;active-domains=0,2,5,6 are equivalent). This option can only be specified if &#8211;start-daemon is also specified and it is only valid for the current run of the oprofile daemon; e.g. the list of active domains is not persistent. </p>
<dt><code>&#8211;passive-domains=&lt;list&gt;</code><i>or</i><code>&#8211;domains=&lt;list&gt;</code></p>
<dd> List of domain ids to be profiled, separated by commas. As opposed to the &#8211;active-domains option, the domains specified with this option do not need to run oprofile. This makes profiling multiple domains easier. However, with the passive-domains option, samples in user level processes and kernel modules cannot be mapped to specific symbols and are aggregated under a generic class. Both &#8211;active-domains and &#8211;passive-domains options can be specified in the same command, but the same domain cannot be specified in both options. This option can only be specified if either &#8211;start or &#8211;start-daemon is specified on the same command and it is only valid for the current run of the oprofile daemon; e.g. the list of passive domains is not persistent. </p>
<dt><code>&#8211;passive-images=&lt;list&gt;</code><i>or</i><code>&#8211;domains-images=&lt;list&gt;</code></p>
<dd> List of kernel images associated with the domains specified in the &#8211;passive-domains option, also separated by commas. The association between the images and domains is based on the order they are specified in both options.
</dl>
<h2>OPTIONS (specific to System z)</h2>
<dl>
<dt><code>&#8211;s390hwsampbufsize=num</code></p>
<dd> Number of 2MB areas used per CPU for storing sample data. The best size for the sample memory depends on the particular system and the workload to be measured. Providing the sampler with too little memory results in lost samples. Reserving too much system memory for the sampler impacts the overall performance and, hence, also the workload to be measured. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by opcontrol. </p>
<h2>FILES</h2>
<dl>
<dt><i>/root/.oprofile/daemonrc</i></p>
<dd> Configuration file for opcontrol</p>
<dt><i>/var/lib/oprofile/samples/</i></p>
<dd> The location of the generated sample files. </p>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
