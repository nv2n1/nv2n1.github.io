---
title: "nfsometer(1)"
name: "nfsometer"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfsometer/"
description: "nfsometer – NFS performance measurement tool"
---

<h2>NAME</h2>
<p> nfsometer &#8211; NFS performance measurement tool</p>
<h2>SYNOPSIS</h2>
<p> nfsometer [options] [mode] [[&lt;server:path&gt;] [workloads&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> nfsometer is a performance measurement framework for running workloads and reporting results across NFS protocol versions, NFS options and Linux NFS client implementations</p>
<h2>MODES</h2>
<p> Basic usage (no mode specified): </p>
<p>&nbsp;<wbr><code>nfsometer&nbsp;<wbr>&lt;server:path&gt;&nbsp;<wbr>[workloads&#8230;]</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This will fetch needed files, run traces, and generate reports,<br />
&nbsp;<wbr>&nbsp;<wbr>same as running the the&nbsp;<wbr>&#8216;fetch&#8217;,&nbsp;<wbr>&#8216;trace&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;report&#8217;&nbsp;<wbr>stages. </p>
<p> Advanced usage (specify modes): </p>
<p>&nbsp;<wbr><code>nfsometer list</code> </p>
<p>&nbsp;<wbr>List the contents of the results directory. </p>
<p>&nbsp;<wbr><code>nfsometer workloads</code> </p>
<p>&nbsp;<wbr>List available and unavailable workloads. </p>
<p>&nbsp;<wbr><code>nfsometer notes</code> </p>
<p>&nbsp;<wbr>Edit the notes file of the results directory. These notes will<br />
&nbsp;<wbr>be displayed in report headers. </p>
<p>&nbsp;<wbr><code>nfsometer loadgen&nbsp;<wbr>&lt;server:path&gt;&nbsp;<wbr>&lt;workload&gt;</code> </p>
<p>&nbsp;<wbr>Run in loadgen mode: don&#8217;t record any stats, just loop over<br />
&nbsp;<wbr>&lt;workload&gt;&nbsp;<wbr>against&nbsp;<wbr>&lt;server:path&gt;.&nbsp;<wbr>&nbsp;<wbr>Only one -o option is allowed.<br />
&nbsp;<wbr>Use the -n option to run multuple instances of the loadgen workload.<br />
&nbsp;<wbr>When running more than one instance, the intial start times are<br />
&nbsp;<wbr>staggered. </p>
<p>&nbsp;<wbr><code>nfsometer fetch&nbsp;<wbr>[workloads&#8230;]</code> </p>
<p>&nbsp;<wbr>Fetch all needed files for the specified workload(s).&nbsp;<wbr>&nbsp;<wbr>If no<br />
&nbsp;<wbr>workloads are specified, all workloads are fetched.<br />
&nbsp;<wbr>Fetched files are only downloaded once and are cached for<br />
&nbsp;<wbr>future runs. </p>
<p>&nbsp;<wbr><code>nfsometer trace&nbsp;<wbr>&lt;server:path&gt;&nbsp;<wbr>[workloads&#8230;]</code> </p>
<p>&nbsp;<wbr>Run traces against&nbsp;<wbr>&lt;server:path&gt;.&nbsp;<wbr>&nbsp;<wbr>The traces run will be:<br />
&nbsp;<wbr>(options&nbsp;<wbr>+&nbsp;<wbr>always options&nbsp;<wbr>+&nbsp;<wbr>tags)&nbsp;<wbr>X&nbsp;<wbr>(workloads)&nbsp;<wbr>X&nbsp;<wbr>(num runs)<br />
&nbsp;<wbr>This will only run traces that don&#8217;t already exist in the results<br />
&nbsp;<wbr>directory. </p>
<p>&nbsp;<wbr><code>nfsometer report</code> </p>
<p>&nbsp;<wbr>Generate all reports available from the results directory. </p>
<p>&nbsp;<wbr><code>nfsometer example</code> </p>
<p>&nbsp;<wbr>Show examples from man page</p>
<h2>OPTIONS</h2>
<dl>
<dt><code> -r &lt;dir&gt;</code>, <code>&#8211;resultdir=&lt;dir&gt;</code></p>
<dd> The directory used to save results. default: &#8216;/home/dros/nfsometer_results&#8217; </p>
<dt><code> -o &lt;mount.nfs options&gt;</code>, <code>&#8211;options=&lt;mount.nfs options&gt;</code></p>
<dd> Mount options to iterate through. This option may be used multiple times. Each mount option must have a version specified. </p>
<dt><code> -a &lt;mount.nfs options&gt;</code>, <code>&#8211;always-options=&lt;mount.nfs options&gt;</code></p>
<dd> Options added to every trace. This option may be used multiple times. </p>
<dt><code> -t &lt;tags&gt;</code>, <code>&#8211;tag=&lt;tags&gt;</code></p>
<dd> Tag all new traces with &#8216;tags&#8217;. This option may be used multiple times. </p>
<dt><code> -n &lt;num runs&gt;</code>, <code>&#8211;num-runs=&lt;num runs&gt;</code></p>
<dd> Number of runs for each trace of &lt;options&gt; X &lt;tags&gt; X &lt;workloads&gt; default: 1 </p>
<dt><code> &#8211;serial-graphs</code></p>
<dd> Generate graphs inline while generating reports. Useful for debugging graphing issues. </p>
<dt><code> &#8211;rand</code></p>
<dd> Randomize the order of traces </p>
<dt><code> -h</code>, <code>&#8211;help</code></p>
<dd> Show the help message</dl>
<h2>EXAMPLES</h2>
<p> Example 1: See what workloads are available </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>$&nbsp;<wbr>nfsometer workloads</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This command lists available workloads and will tell you why<br />
&nbsp;<wbr>&nbsp;<wbr>workloads are unavailable&nbsp;<wbr>(if any exist). </p>
<p> Example 2: Compare cthon, averaged over 3 runs,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>across nfs protocol versions </p>
<p><code>nfsometer -n 3 server:/export cthon</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This example uses the default for -o:&nbsp;<wbr>&quot;-o v3 -o v4 -o v4.1&quot;.<br />
&nbsp;<wbr>&nbsp;<wbr>To see the results, open results/index.html in a web browser. </p>
<p> Example 3: Compare cthon, averaged over 3 runs,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>between v3 and v4.0 only </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>nfsometer -n 3 -o v3 -o v4 server:/export cthon</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This example specifies v3 and v4 only.<br />
&nbsp;<wbr>&nbsp;<wbr>To see the results, open results/index.html in a web browser. </p>
<p> Example 4: Compare two kernels running iozone workload, averaged<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>over 2 runs, across all nfs protocol versions </p>
<p>&nbsp;<wbr>&nbsp;<wbr>nfsometer can compare two&nbsp;<wbr>(or more)&nbsp;<wbr>kernel versions, but<br />
&nbsp;<wbr>&nbsp;<wbr>has no way of building, installing or booting new kernels.<br />
&nbsp;<wbr>&nbsp;<wbr>It&#8217;s up to the user to install new kernels.<br />
&nbsp;<wbr>&nbsp;<wbr>In order for these kernels to be differentiated,&nbsp;<wbr>&#8216;uname -a&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>must be different. </p>
<p>1)&nbsp;<wbr>boot into kernel&nbsp;<wbr>#1 </p>
<p>2)&nbsp;<wbr><code>nfsometer -n 2 server:/export iozone</code> </p>
<p>3)&nbsp;<wbr>boot into kernel&nbsp;<wbr>#2 </p>
<p>4)&nbsp;<wbr><code>nfsometer -n 2 server:/export iozone</code> </p>
<p>5)&nbsp;<wbr>open results/index.html in a web browser </p>
<p>&nbsp;<wbr>&nbsp;<wbr>To see the results, open results/index.html in a web browser. </p>
<p> Example 5: Using tags </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Tags&nbsp;<wbr>(the -t option)&nbsp;<wbr>can be used to mark nfsometer runs as<br />
&nbsp;<wbr>&nbsp;<wbr>occurring with some configuration not captured by mount options<br />
&nbsp;<wbr>&nbsp;<wbr>or detectable tags, such as different sysctl settings&nbsp;<wbr>(client side),<br />
&nbsp;<wbr>&nbsp;<wbr>different server side options, or different network conditions. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1)&nbsp;<wbr>set server value foo to 2.3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>2)&nbsp;<wbr><code>nfsometer -o v4 -o v4.1 -t foo=2.3</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>3)&nbsp;<wbr>set server value foo to 10 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>4)&nbsp;<wbr><code>nfsometer -o v4 -o v4.1 -t foo=10</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>What is passed to -t is entirely up to the user &#8211; it will not be<br />
&nbsp;<wbr>&nbsp;<wbr>interpreted or checked by nfsometer at all, so be careful! </p>
<p>&nbsp;<wbr>&nbsp;<wbr>To see the results, open results/index.html in a web browser. </p>
<p> Example 6: Always options </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The -o flag specifies distinct option sets to run, but sometimes<br />
&nbsp;<wbr>&nbsp;<wbr>there are options that should be present in each.&nbsp;<wbr>&nbsp;<wbr>Instead of<br />
&nbsp;<wbr>&nbsp;<wbr>writing each one out, you can use the -a option: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>nfsometer -o v3 -o v4 -a sec=krb5 server:/export iozone</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>this is equivalent to: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>nfsometer -o v3,sec=krb5 -o v4,sec=krb5 server:/export iozone</code> </p>
<p> Example 7: Using the &quot;custom&quot; workload </p>
<p>&nbsp;<wbr>&nbsp;<wbr>A main use case of nfsometer is the&nbsp;<wbr>&quot;custom&quot;&nbsp;<wbr>workload &#8211; it allows<br />
&nbsp;<wbr>&nbsp;<wbr>the user to specify the command that nfsometer is to run. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>NOTE: the command&#8217;s cwd&nbsp;<wbr>(current working directory)&nbsp;<wbr>is the runroot<br />
&nbsp;<wbr>&nbsp;<wbr>created on the server. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>export NFSOMETER_CMD=&quot;echo foo&nbsp;<wbr>&gt;&nbsp;<wbr>bar&quot;</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>export NFSOMETER_NAME=&quot;echo&quot;</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>export NFSOMETER_DESC=&quot;Writes 4 bytes to a file&quot;</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>nfsometer server:/export custom</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This will run 3 traces&nbsp;<wbr>(v3, v4, v4.1)&nbsp;<wbr>against server:/export of<br />
&nbsp;<wbr>&nbsp;<wbr>the command:&nbsp;<wbr><code>echo foo&nbsp;<wbr>&gt;&nbsp;<wbr>bar</code>. </p>
<p> Example 8: Using the loadgen mode </p>
<p>&nbsp;<wbr>Loadgen runs several instances of a workload without capturing<br />
&nbsp;<wbr>traces. The idea is that you use several clients to generate<br />
&nbsp;<wbr>load, then another client to measure performance of a loaded<br />
&nbsp;<wbr>server. The&nbsp;<wbr>&quot;real&quot;&nbsp;<wbr>run of nfsometer&nbsp;<wbr>(not loadgen)&nbsp;<wbr>should mark<br />
&nbsp;<wbr>the traces using the -t option. </p>
<p>&nbsp;<wbr>1)&nbsp;<wbr>On client A, run the cthon workload to get a baseline of<br />
&nbsp;<wbr>a server without any load. </p>
<p><code>nfsometer trace server:/export cthon</code> </p>
<p>&nbsp;<wbr>2)&nbsp;<wbr>When that&#8217;s done, start loadgen on client B: </p>
<p><code>nfsometer -n 10 loadgen server:/export dd_100m_1k</code> </p>
<p>&nbsp;<wbr>This runs 10 instances of dd_100m_1k workload on server:/export.<br />
&nbsp;<wbr>It can take several minutes to start in an attempt to stagger<br />
&nbsp;<wbr>all the workload instances. </p>
<p>&nbsp;<wbr>3)&nbsp;<wbr>once all instances are started, run the&nbsp;<wbr>&quot;real&quot;&nbsp;<wbr>nfsometer<br />
&nbsp;<wbr>trace on client A.&nbsp;<wbr>&nbsp;<wbr>Use the -t option to mark the traces<br />
&nbsp;<wbr>as having run under load conditions: </p>
<p><code>nfsometer -t&nbsp;<wbr>&quot;10_dd&quot;&nbsp;<wbr>trace server:/export cthon</code> </p>
<p>&nbsp;<wbr>4)&nbsp;<wbr>Explain how the tests were set up in the result notes.<br />
&nbsp;<wbr>This should be run on client A&nbsp;<wbr>(which has the traces: </p>
<p><code>nfsometer notes</code> </p>
<p>&nbsp;<wbr>5)&nbsp;<wbr>Now generate the reports: </p>
<p><code>nfsometer report</code> </p>
<p> Example 8: Long running nfsometer trace </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The nfsometer.py script currently runs in the foreground.&nbsp;<wbr>&nbsp;<wbr>As<br />
&nbsp;<wbr>&nbsp;<wbr>such, it will be killed if the tty gets a hangup or the connection<br />
&nbsp;<wbr>&nbsp;<wbr>to the client is closed. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>For the time being, nfsometer should be run in a screen<br />
&nbsp;<wbr>&nbsp;<wbr>session, or run with nohup and the output redirected to a file. </p>
<p>1)&nbsp;<wbr><code>screen -RD</code><br />
2)&nbsp;<wbr><code>nfsometer -n 2 server:/export iozone</code><br />
3)&nbsp;<wbr>close terminal window&nbsp;<wbr>(or&nbsp;<wbr>^A^D)<br />
&#8230;<br />
4)&nbsp;<wbr>reattach later with&nbsp;<wbr><code>screen -RD</code><br />
5)&nbsp;<wbr>once nfsometer.py is done, results will be in results/index.html</p>
<h2>SEE ALSO</h2>
<p> mountstats, nfsstats</p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Weston Andros Adamson (dros [at] netapp.com) </p>
<h2>Index</h2>
