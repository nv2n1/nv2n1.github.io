---
title: "jstat-java-1-8-0-openjdk-1-8-0-31-5-b13-fc21-x86_64(1)"
name: "jstat-java-1-8-0-openjdk-1-8-0-31-5-b13-fc21-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstat-java-1-8-0-openjdk-1-8-0-31-5-b13-fc21-x86_64/"
description: "jstat – Monitors Java Virtual Machine (JVM) statistics. This command is experimental and unsupported."
---

<p>jstat &#8211; Monitors Java Virtual Machine (JVM) statistics. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jstat</code> [ <i>generalOption</i> | <i>outputOptions vmid</i> [ <i>interval</i>[s|ms] [ <i>count </i>] ]</pre>
<dl>
<dt><i>generalOption</i></p>
<dd>A single general command-line option <code>-help</code> or <code>-options</code>. See General Options.</p>
<dt><i>outputOptions</i></p>
<dd>One or more output options that consist of a single <code>statOption</code>, plus any of the <code>-t</code>, <code>-h</code>, and <code>-J</code> options. See Output Options.</p>
<dt><i>vmid</i></p>
<dd>Virtual machine identifier, which is a string that indicates the target JVM. The general syntax is the following: </p>
<pre><code>[protocol:][//]lvmid[@hostname[:port]/servername]</code></pre>
<p>The syntax of the <code>vmid</code> string corresponds to the syntax of a URI. The <code>vmid</code> string can vary from a simple integer that represents a local JVM to a more complex construction that specifies a communications protocol, port number, and other implementation-specific values. See Virtual Machine Identifier.</p>
<dt><i>interval</i> [s|ms]</p>
<dd>Sampling interval in the specified units, seconds (s) or milliseconds (ms). Default units are milliseconds. Must be a positive integer. When specified, the <code>jstat</code> command produces its output at each interval.</p>
<dt><i>count</i></p>
<dd>Number of samples to display. The default value is infinity which causes the <code>jstat</code> command to display statistics until the target JVM terminates or the <code>jstat</code> command is terminated. This value must be a positive integer.</dl>
<h2>Description</h2>
<p>The <code>jstat</code> command displays performance statistics for an instrumented Java HotSpot VM. The target JVM is identified by its virtual machine identifier, or <code>vmid</code> option.</p>
<h2>Virtual Machine Identifier</h2>
<p>The syntax of the <code>vmid</code> string corresponds to the syntax of a URI: </p>
<pre><code>[protocol:][//]lvmid[@hostname[:port]/servername]</code></pre>
<dl>
<dt><i>protocol</i></p>
<dd>The communications protocol. If the <i>protocol</i> value is omitted and a host name is not specified, then the default protocol is a platform-specific optimized local protocol. If the <i>protocol</i> value is omitted and a host name is specified, then the default protocol is <code>rmi</code>.</p>
<dt><i>lvmid</i></p>
<dd>The local virtual machine identifier for the target JVM. The <code>lvmid</code> is a platform-specific value that uniquely identifies a JVM on a system. The <code>lvmid</code> is the only required component of a virtual machine identifier. The <code>lvmid</code> is typically, but not necessarily, the operating system&#8217;s process identifier for the target JVM process. You can use the <code>jps</code> command to determine the <code>lvmid</code>. Also, you can determine the <code>lvmid</code> on UNIX platforms with the <code>ps</code> command, and on Windows with the Windows Task Manager.</p>
<dt><i>hostname</i></p>
<dd>A hostname or IP address that indicates the target host. If the <i>hostname</i> value is omitted, then the target host is the local host.</p>
<dt><i>port</i></p>
<dd>The default port for communicating with the remote server. If the <i>hostname</i> value is omitted or the <i>protocol</i> value specifies an optimized, local protocol, then the <i>port</i> value is ignored. Otherwise, treatment of the <code>port</code> parameter is implementation-specific. For the default <code>rmi</code> protocol, the port value indicates the port number for the rmiregistry on the remote host. If the <i>port</i> value is omitted and the <i>protocol</i> value indicates <code>rmi</code>, then the default rmiregistry port (1099) is used.</p>
<dt><i>servername</i></p>
<dd>The treatment of the <code>servername</code> parameter depends on implementation. For the optimized local protocol, this field is ignored. For the <code>rmi</code> protocol, it represents the name of the RMI remote object on the remote host.</dl>
<h2>Options</h2>
<p>The <code>jstat</code> command supports two types of options, general options and output options. General options cause the <code>jstat</code> command to display simple usage and version information. Output options determine the content and format of the statistical output. </p>
<p> All options and their functionality are subject to change or removal in future releases.</p>
<h3>General Options</h3>
<p>If you specify one of the general options, then you cannot specify any other option or parameter.</p>
<dl>
<dt>-help</p>
<dd>Displays a help message.</p>
<dt>-options</p>
<dd>Displays a list of static options. See Output Options.</dl>
<h3>Output Options</h3>
<p>If you do not specify a general option, then you can specify output options. Output options determine the content and format of the <code>jstat</code> command&#8217;s output, and consist of a single <code>statOption</code>, plus any of the other output options (<code>-h</code>, <code>-t</code>, and <code>-J</code>). The <code>statOption</code> must come first. </p>
<p> Output is formatted as a table, with columns that are separated by spaces. A header row with titles describes the columns. Use the <code>-h</code> option to set the frequency at which the header is displayed. Column header names are consistent among the different options. In general, if two options provide a column with the same name, then the data source for the two columns is the same. </p>
<p> Use the <code>-t</code> option to display a time stamp column, labeled Timestamp as the first column of output. The Timestamp column contains the elapsed time, in seconds, since the target JVM started. The resolution of the time stamp is dependent on various factors and is subject to variation due to delayed thread scheduling on heavily loaded systems. </p>
<p> Use the interval and count parameters to determine how frequently and how many times, respectively, the <code>jstat</code> command displays its output. </p>
<p> <i>Note:</i> Do not to write scripts to parse the <code>jstat</code> command&#8217;s output because the format might change in future releases. If you write scripts that parse <code>jstat</code> command output, then expect to modify them for future releases of this tool.</p>
<dl>
<dt>&#8211;<i>statOption</i></p>
<dd>Determines the statistics information the <code>jstat</code> command displays. The following lists the available options. Use the <code>-options</code> general option to display the list of options for a particular platform installation. See Stat Options and Output. </p>
<p> <code>class</code>: Displays statistics about the behavior of the class loader. </p>
<p> <code>compiler</code>: Displays statistics about the behavior of the Java HotSpot VM Just-in-Time compiler. </p>
<p> <code>gc</code>: Displays statistics about the behavior of the garbage collected heap. </p>
<p> <code>gccapacity</code>: Displays statistics about the capacities of the generations and their corresponding spaces. </p>
<p> <code>gccause</code>: Displays a summary about garbage collection statistics (same as <code>-gcutil</code>), with the cause of the last and current (when applicable) garbage collection events. </p>
<p> <code>gcnew</code>: Displays statistics of the behavior of the new generation. </p>
<p> <code>gcnewcapacity</code>: Displays statistics about the sizes of the new generations and its corresponding spaces. </p>
<p> <code>gcold</code>: Displays statistics about the behavior of the old generation and Metaspace Statistics. </p>
<p> <code>gcoldcapacity</code>: Displays statistics about the sizes of the old generation. </p>
<p> <code>gcmetacapacity</code>: Displays statistics about the sizes of the metaspace. </p>
<p> <code>gcutil</code>: Displays a summary about garbage collection statistics. </p>
<p> <code>printcompilation</code>: Displays Java HotSpot VM compilation method statistics.</p>
<dt>-h <i>n</i></p>
<dd>Displays a column header every <i>n</i> samples (output rows), where <i>n</i> is a positive integer. Default value is 0, which displays the column header the first row of data.</p>
<dt>-t</p>
<dd>Display sa timestamp column as the first column of output. The time stamp is the time since the start time of the target JVM.</p>
<dt>-J<i>javaOption</i></p>
<dd>Passes <code>javaOption</code> to the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. For a complete list of options, see <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h3>Stat Options And Output</h3>
<p>The following information summarizes the columns that the <code>jstat</code> command outputs for each <i>statOption</i>.</p>
<dl>
<dt>-class <i>option</i></p>
<dd>Class loader statistics. </p>
<p> <code>Loaded</code>: Number of classes loaded. </p>
<p> <code>Bytes</code>: Number of KBs loaded. </p>
<p> <code>Unloaded</code>: Number of classes unloaded. </p>
<p> <code>Bytes</code>: Number of Kbytes unloaded. </p>
<p> <code>Time</code>: Time spent performing class loading and unloading operations.</p>
<dt>-compiler <i>option</i></p>
<dd>Java HotSpot VM Just-in-Time compiler statistics. </p>
<p> <code>Compiled</code>: Number of compilation tasks performed. </p>
<p> <code>Failed</code>: Number of compilations tasks failed. </p>
<p> <code>Invalid</code>: Number of compilation tasks that were invalidated. </p>
<p> <code>Time</code>: Time spent performing compilation tasks. </p>
<p> <code>FailedType</code>: Compile type of the last failed compilation. </p>
<p> <code>FailedMethod</code>: Class name and method of the last failed compilation.</p>
<dt>-gc <i>option</i></p>
<dd>Garbage-collected heap statistics. </p>
<p> <code>S0C</code>: Current survivor space 0 capacity (KB). </p>
<p> <code>S1C</code>: Current survivor space 1 capacity (KB). </p>
<p> <code>S0U</code>: Survivor space 0 utilization (KB). </p>
<p> <code>S1U</code>: Survivor space 1 utilization (KB). </p>
<p> <code>EC</code>: Current eden space capacity (KB). </p>
<p> <code>EU</code>: Eden space utilization (KB). </p>
<p> <code>OC</code>: Current old space capacity (KB). </p>
<p> <code>OU</code>: Old space utilization (KB). </p>
<p> <code>MC</code>: Metaspace capacity (KB). </p>
<p> <code>MU</code>: Metacspace utilization (KB). </p>
<p> <code>YGC</code>: Number of young generation garbage collection events. </p>
<p> <code>YGCT</code>: Young generation garbage collection time. </p>
<p> <code>FGC</code>: Number of full GC events. </p>
<p> <code>FGCT</code>: Full garbage collection time. </p>
<p> <code>GCT</code>: Total garbage collection time.</p>
<dt>-gccapacity <i>option</i></p>
<dd>Memory pool generation and space capacities. </p>
<p> <code>NGCMN</code>: Minimum new generation capacity (KB). </p>
<p> <code>NGCMX</code>: Maximum new generation capacity (KB). </p>
<p> <code>NGC</code>: Current new generation capacity (KB). </p>
<p> <code>S0C</code>: Current survivor space 0 capacity (KB). </p>
<p> <code>S1C</code>: Current survivor space 1 capacity (KB). </p>
<p> <code>EC</code>: Current eden space capacity (KB). </p>
<p> <code>OGCMN</code>: Minimum old generation capacity (KB). </p>
<p> <code>OGCMX</code>: Maximum old generation capacity (KB). </p>
<p> <code>OGC</code>: Current old generation capacity (KB). </p>
<p> <code>OC</code>: Current old space capacity (KB). </p>
<p> <code>MCMN</code>: Minimum metaspace capacity (KB). </p>
<p> <code>MCMX</code>: Maximum metaspace capacity (KB). </p>
<p> <code>MC</code>: Metaspace capacity (KB). </p>
<p> <code>YGC</code>: Number of Young generation GC Events. </p>
<p> <code>FGC</code>: Number of Full GC Events.</p>
<dt>-gccause <i>option</i></p>
<dd>This option displays the same summary of garbage collection statistics as the <code>-gcutil</code> option, but includes the causes of the last garbage collection event and (when applicable) the current garbage collection event. In addition to the columns listed for <code>-gcutil</code>, this option adds the following columns. </p>
<p> Garbage collection statistics, including garbage collection Events. </p>
<p> <code>LGCC</code>: Cause of last garbage collection. </p>
<p> <code>GCC</code>: Cause of current garbage collection.</p>
<dt>-gcnew <i>option</i></p>
<dd>New generation statistics. </p>
<p> <code>S0C</code>: Current survivor space 0 capacity (KB). </p>
<p> <code>S1C</code>: Current survivor space 1 capacity (KB). </p>
<p> <code>S0U</code>: Survivor space 0 utilization (KB). </p>
<p> <code>S1U</code>: Survivor space 1 utilization (KB). </p>
<p> <code>TT</code>: Tenuring threshold. </p>
<p> <code>MTT</code>: Maximum tenuring threshold. </p>
<p> <code>DSS</code>: Desired survivor size (KB). </p>
<p> <code>EC</code>: Current eden space capacity (KB). </p>
<p> <code>EU</code>: Eden space utilization (KB). </p>
<p> <code>YGC</code>: Number of young generation GC events. </p>
<p> <code>YGCT</code>: Young generation garbage collection time.</p>
<dt>-gcnewcapacity <i>option</i></p>
<dd>New generation space size statistics. </p>
<p> NGCMN: Minimum new generation capacity (KB). </p>
<p> <code>NGCMX</code>: Maximum new generation capacity (KB). </p>
<p> <code>NGC</code>: Current new generation capacity (KB). </p>
<p> <code>S0CMX</code>: Maximum survivor space 0 capacity (KB). </p>
<p> <code>S0C</code>: Current survivor space 0 capacity (KB). </p>
<p> <code>S1CMX</code>: Maximum survivor space 1 capacity (KB). </p>
<p> <code>S1C</code>: Current survivor space 1 capacity (KB). </p>
<p> <code>ECMX</code>: Maximum eden space capacity (KB). </p>
<p> <code>EC</code>: Current eden space capacity (KB). </p>
<p> <code>YGC</code>: Number of young generation GC events. </p>
<p> <code>FGC</code>: Number of Full GC Events.</p>
<dt>-gcold <i>option</i></p>
<dd>old and permanent generation statistics. </p>
<p> <code>MC</code>: Metaspace capacity (KB). </p>
<p> <code>MU</code>: Metaspace utilization (KB). </p>
<p> <code>OC</code>: Current old space capacity (KB). </p>
<p> <code>OU</code>: old space utilization (KB). </p>
<p> <code>YGC</code>: Number of young generation GC events. </p>
<p> <code>FGC</code>: Number of full GC events. </p>
<p> <code>FGCT</code>: Full garbage collection time. </p>
<p> <code>GCT</code>: Total garbage collection time.</p>
<dt>-gcoldcapacity <i>option</i></p>
<dd>Old generation statistics. </p>
<p> <code>OGCMN</code>: Minimum old generation capacity (KB). </p>
<p> <code>OGCMX</code>: Maximum old generation capacity (KB). </p>
<p> <code>OGC</code>: Current old generation capacity (KB). </p>
<p> <code>OC</code>: Current old space capacity (KB). </p>
<p> <code>YGC</code>: Number of young generation GC events. </p>
<p> <code>FGC</code>: Number of full GC events. </p>
<p> <code>FGCT</code>: Full garbage collection time. </p>
<p> <code>GCT</code>: Total garbage collection time.</p>
<dt>-gcmetacapacity <i>option</i></p>
<dd>Permanent generation statistics. </p>
<p> <code>MCMN</code>: Minimum metaspace capacity (KB). </p>
<p> <code>MCMX</code>: Maximum metaspace capacity (KB). </p>
<p> <code>MC</code>: Metaspace capacity (KB). </p>
<p> <code>YGC</code>: Number of young generation GC events. </p>
<p> <code>FGC</code>: Number of full GC events. </p>
<p> <code>FGCT</code>: Full garbage collection time. </p>
<p> <code>GCT</code>: Total garbage collection time.</p>
<dt>-gcutil <i>option</i></p>
<dd>Summary of garbage collection statistics. </p>
<p> <code>S0</code>: Survivor space 0 utilization as a percentage of the space&#8217;s current capacity. </p>
<p> <code>S1</code>: Survivor space 1 utilization as a percentage of the space&#8217;s current capacity. </p>
<p> <code>E</code>: Eden space utilization as a percentage of the space&#8217;s current capacity. </p>
<p> <code>O</code>: Old space utilization as a percentage of the space&#8217;s current capacity. </p>
<p> <code>M</code>: Metaspace utilization as a percentage of the space&#8217;s current capacity. </p>
<p> <code>YGC</code>: Number of young generation GC events. </p>
<p> <code>YGCT</code>: Young generation garbage collection time. </p>
<p> <code>FGC</code>: Number of full GC events. </p>
<p> <code>FGCT</code>: Full garbage collection time. </p>
<p> <code>GCT</code>: Total garbage collection time.</p>
<dt>-printcompilation <i>option</i></p>
<dd>Java HotSpot VM compiler method statistics. </p>
<p> <code>Compiled</code>: Number of compilation tasks performed by the most recently compiled method. </p>
<p> <code>Size</code>: Number of bytes of byte code of the most recently compiled method. </p>
<p> <code>Type</code>: Compilation type of the most recently compiled method. </p>
<p> <code>Method</code>: Class name and method name identifying the most recently compiled method. Class name uses slash (/) instead of dot (.) as a name space separator. Method name is the method within the specified class. The format for these two fields is consistent with the HotSpot <code>-XX:+PrintComplation</code> option.</dl>
<h2>Examples</h2>
<p>This section presents some examples of monitoring a local JVM with an <i>lvmid</i> of 21891.</p>
<h3>The Gcutil Option</h3>
<p>This example attaches to lvmid 21891 and takes 7 samples at 250 millisecond intervals and displays the output as specified by the &#8211;<code>gcutil</code> option. </p>
<p> The output of this example shows that a young generation collection occurred between the third and fourth sample. The collection took 0.001 seconds and promoted objects from the eden space (E) to the old space (O), resulting in an increase of old space utilization from 9.49% to 9.51%. Before the collection, the survivor space was 12.44% utilized, but after this collection it is only 7.74% utilized. </p>
<pre><code>jstat -gcutil 21891 250 7</code></pre>
<pre><code> S0 S1 E O M YGC YGCT FGC FGCT GCT</code></pre>
<pre><code>0.00 99.74 13.49 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<pre><code>0.00 99.74 13.49 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<pre><code>0.00 99.74 13.49 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<pre><code>0.00 99.74 13.49 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<pre><code>0.00 99.74 13.80 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<pre><code>0.00 99.74 13.80 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<pre><code>0.00 99.74 13.80 7.86 95.82 3 0.124 0 0.000 0.124</code></pre>
<h3>Repeat The Column Header String</h3>
<p>This example attaches to lvmid 21891 and takes samples at 250 millisecond intervals and displays the output as specified by <code>-gcutil</code> option. In addition, it uses the <code>-h3</code> option to output the column header after every 3 lines of data. </p>
<p> In addition to showing the repeating header string, this example shows that between the second and third samples, a young GC occurred. Its duration was 0.001 seconds. The collection found enough active data that the survivor space 0 utilization (S0U) would have exceeded the desired survivor Size (DSS). As a result, objects were promoted to the old generation (not visible in this output), and the tenuring threshold (TT) was lowered from 31 to 2. </p>
<p> Another collection occurs between the fifth and sixth samples. This collection found very few survivors and returned the tenuring threshold to 31. </p>
<pre><code>jstat -gcnew -h3 21891 250</code></pre>
<pre><code> S0C S1C S0U S1U TT MTT DSS EC EU YGC YGCT</code></pre>
<pre><code> 64.0 64.0 0.0 31.7 31 31 32.0 512.0 178.6 249 0.203</code></pre>
<pre><code> 64.0 64.0 0.0 31.7 31 31 32.0 512.0 355.5 249 0.203</code></pre>
<pre><code> 64.0 64.0 35.4 0.0 2 31 32.0 512.0 21.9 250 0.204</code></pre>
<pre><code> S0C S1C S0U S1U TT MTT DSS EC EU YGC YGCT</code></pre>
<pre><code> 64.0 64.0 35.4 0.0 2 31 32.0 512.0 245.9 250 0.204</code></pre>
<pre><code> 64.0 64.0 35.4 0.0 2 31 32.0 512.0 421.1 250 0.204</code></pre>
<pre><code> 64.0 64.0 0.0 19.0 31 31 32.0 512.0 84.4 251 0.204</code></pre>
<pre><code> S0C S1C S0U S1U TT MTT DSS EC EU YGC YGCT</code></pre>
<pre><code> 64.0 64.0 0.0 19.0 31 31 32.0 512.0 306.7 251 0.204</code></pre>
<h3>Include A Time Stamp For Each Sample</h3>
<p>This example attaches to lvmid 21891 and takes 3 samples at 250 millisecond intervals. The <code>-t</code> option is used to generate a time stamp for each sample in the first column. </p>
<p> The Timestamp column reports the elapsed time in seconds since the start of the target JVM. In addition, the <code>-gcoldcapacity</code> output shows the old generation capacity (OGC) and the old space capacity (OC) increasing as the heap expands to meet allocation or promotion demands. The old generation capacity (OGC) has grown to from 11,696 KB to 13820 KB after the eighty-first full garbage collection (FGC). The maximum capacity of the generation (and space) is 60,544 KB (OGCMX), so it still has room to expand. </p>
<pre><code>Timestamp OGCMN OGCMX OGC OC YGC FGC FGCT GCT</code></pre>
<pre><code> 150.1 1408.0 60544.0 11696.0 11696.0 194 80 2.874 3.799</code></pre>
<pre><code> 150.4 1408.0 60544.0 13820.0 13820.0 194 81 2.938 3.863</code></pre>
<pre><code> 150.7 1408.0 60544.0 13820.0 13820.0 194 81 2.938 3.863</code></pre>
<h3>Monitor Instrumentation For A Remote Jvm</h3>
<p>This example attaches to lvmid 40496 on the system named remote.domain using the <code>-gcutil</code> option, with samples taken every second indefinitely. </p>
<p> The lvmid is combined with the name of the remote host to construct a <i>vmid</i> of <code>40496 [at] remote.domain</code>. This vmid results in the use of the <code>rmi</code> protocol to communicate to the default <code>jstatd</code> server on the remote host. The <code>jstatd</code> server is located using the rmiregistry on <code>remote.domain</code> that is bound to the default rmiregistry port (port 1099). </p>
<pre><code>jstat -gcutil 40496 [at] remote.domain 1000</code></pre>
<pre><i>... output omitted</i></pre>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jps/">jps</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jstatd/">jstatd</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-rmiregistry/">rmiregistry</a>(1) </p>
</dl>
