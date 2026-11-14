---
title: "jstat-java-1(1)"
name: "jstat-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstat-java-1/"
description: "jstat – Java Virtual Machine Statistics Monitoring Tool"
---

<h2>Name</h2>
<p> jstat &#8211; Java Virtual Machine Statistics Monitoring Tool </p>
<h2>SYNOPSIS</h2>
<pre><code>
jstat[generalOption | outputOptions vmid[interval[s | ms][count]]]
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>generalOption</p>
<dd> A single general command-line option (-help, -options, or -version)</p>
<dt>outputOptions</p>
<dd> One or more output options, consisting of a single <i>statOption</i>, plus any of the -t, -h, and -J options.</p>
<dt>vmid</p>
<dd> Virtual machine identifier, a string indicating the target Java virtual machine (JVM). The general syntax is<br />
[protocol:][//]lvmid[@hostname[:port]/servername]<br />
 The syntax of the vmid string largely corresponds to the syntax of a URI. The <i>vmid</i> can vary from a simple integer representing a local JVM to a more complex construction specifying a communications protocol, port number, and other implementation-specific values. See Virtual Machine Identifier for details.</p>
<dt>interval[s|ms]</p>
<dd> Sampling interval in the specified units, seconds (s) or milliseconds (ms). Default units are milliseconds. Must be a positive integer. If specified, <code>jstat</code> will produce its output at each interval.</p>
<dt>count</p>
<dd> Number of samples to display. Default value is infinity; that is, <code>jstat</code> displays statistics until the target JVM terminates or the <code>jstat</code> command is terminated. Must be a positive integer.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>jstat</code> tool displays performance statistics for an instrumented HotSpot Java virtual machine (JVM). The target JVM is identified by its virtual machine identifier, or <i>vmid</i> option described below. </p>
<p> <code>NOTE</code>: This utility is unsupported and may not be available in future versions of the JDK. It is not currently available on Windows 98 and Windows ME. platforms. </p>
<h3>VIRTUAL MACHINE IDENTIFIER</h3>
<p> The syntax of the <i>vmid</i> string largely corresponds to the syntax of a URI: </p>
<pre><code>
[protocol:][//]lvmid[@hostname][:port][/servername]
</code></pre>
<dl>
<dt>
<dd>
<dl>
<dt>protocol</p>
<dd> The communications protocol. If the <i>protocol</i> is omitted and a <i>hostname</i> is not specified, the default protocol is a platform specific optimized local protocol. If the <i>protocol</i> is omitted and a <i>hostname</i> is specified, then the default protocol is <code>rmi</code>.</p>
<dt>lvmid</p>
<dd> The local virtual machine identifier for the target JVM. The <i>lvmid</i> is a platform-specific value that uniquely identifies a JVM on a system. The <i>lvmid</i> is the only required component of a virtual machine identifier. The <i>lvmid</i> is typically, but not necessarily, the operating system&#8217;s process identifier for the target JVM process. You can use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command to determine the <i>lvmid</i>. Also, you can determine <i>lvmid</i> on Unix platforms with the <code>ps</code> command, and on Windows with the Windows Task Manager.</p>
<dt>hostname</p>
<dd> A hostname or IP address indicating the target host. If <i>hostname</i> is omitted, then the target host is the local host.</p>
<dt>port</p>
<dd> The default port for communicating with the remote server. If the <i>hostname</i> is omitted or the <i>protocol</i> specifies an optimized, local protocol, then <i>port</i> is ignored. Otherwise, treatment of the <i>port</i> parameter is implementation specific. For the default <code>rmi</code> protocol, the <i>port</i> indicates the port number for the rmiregistry on the remote host. If <i>port</i> is omitted, and <i>protocol</i> indicates <code>rmi</code>, then the default rmiregistry port (1099) is used.</p>
<dt>servername</p>
<dd> The treatment of this parameter depends on implementation. For the optimized local protocol, this field is ignored. For the <code>rmi</code> protocol, it represents the name of the RMI remote object on the remote host.</dl>
</dl>
<h2>OPTIONS</h2>
<p> The <code>jstat</code> command supports two types of options, general options and output options. General options cause <code>jstat</code> to display simple usage and version information. Output options determine the content and format of the statistical output. </p>
<p> <code>NOTE</code>: All options, and their functionality are subject to change or removal in future releases. </p>
<h3>GENERAL OPTIONS</h3>
<p> If you specify one of the general options, you cannot specify any other option or parameter. </p>
<dl>
<dt>
<dd>
<dl>
<dt>-help</p>
<dd> Display help message.</p>
<dt>-version</p>
<dd> Display version information.</p>
<dt>-options</p>
<dd> Display list of statistics options. See the Output Options section below.</dl>
</dl>
<h3>OUTPUT OPTIONS</h3>
<p> If you do not specify a general option, then you can specify output options. Output options determine the content and format of <code>jstat</code>&#8216;s output, and consist of a single <i>statOption</i>, plus any of the other output options (-h, -t, and -J). The <i>statOption</i> must come first. </p>
<p> Output is formatted as a table, with columns are separated by spaces. A header row with titles describes the columns. Use the <code>-h</code> option to set the frequency at which the header is displayed. Column header names are generally consistent between the different options. In general, if two options provide a column with the same name, then the data source for the two columns are the same. </p>
<p> Use the <code>-t</code> option to display a time stamp column, labeled <i>Timestamp</i> as the first column of output. The <i>Timestamp</i> column contains the elapsed time, in seconds, since startup of the target JVM. The resolution of the time stamp is dependent on various factors and is subject to variation due to delayed thread scheduling on heavily loaded systems. </p>
<p> Use the <i>interval</i> and <i>count</i> parameters to determine how frequently and how many times, respectively, <code>jstat</code> displays its output. </p>
<p> <code>NOTE</code>: You are advised not to write scripts to parse <code>jstat&#8217;s</code> output since the format may change in future releases. If you choose to write scripts that parse <code>jstat</code> output, expect to modify them for future releases of this tool. </p>
<dl>
<dt>
<dd>
<dl>
<dt>-statOption</p>
<dd> Determines the statistics information that <code>jstat</code> displays. The following table lists the available options. Use the <code>-options</code> general option to display the list of options for a particular platform installation. </p>
</dl>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<code>Option</code><code>Displays...</code>
class
compiler
gc
gccapacity
gccause
gcnew
gcnewcapacity
gcold
gcoldcapacity
gcpermcapacity
gcutil
printcompilation
<dl>
<dt>-h n <dd>Display a column header every <i>n</i> samples (output rows), where <i>n</i> is a positive integer. Default value is 0, which displays the column header above the first row of data. 
<dt>-t n <dd>Display a timestamp column as the first column of output. The timestamp is the time since the start time of the target JVM. 
<dt>-JjavaOption <dd>Pass <i>javaOption</i> to the <code>java</code> application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. For a complete list of options, see <a href="//www.systutorials.com/docs/linux/man/1-java/">java</a>(1) 
</dl>
</dl>
</pre>
<h3>STATOPTIONS AND OUTPUT</h3>
<p> The following tables summarize the columns that <code>jstat</code> outputs for each <i>statOption</i>. </p>
<h3>-class Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Class Loader Statistics
<code>Column</code><code>Description</code>
LoadedNumber of classes loaded.
BytesNumber of Kbytes loaded.
Unloaded
Bytes
Time
</pre>
<h3>-compiler Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
HotSpot Just-In-Time Compiler Statistics
<code>Column</code><code>Description</code>
Compiled
Failed
Invalid
Time
FailedType
FailedMethod
</pre>
<h3>-gc Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Garbage-collected heap statistics
<code>Column</code><code>Description</code>
S0C
S1C
S0U
S1U
EC
EU
OC
OU
PC
PU
YGC
YGCT
FGCNumber of full GC events.
FGCT
GCT
</pre>
<h3>-gccapacity Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Memory Pool Generation and Space Capacities
<code>Column</code><code>Description</code>
NGCMN
NGCMX
NGC
S0C
S1C
EC
OGCMN
OGCMX
OGC
OC
PGCMN
PGCMX
PGC
PC
YGC
FGCNumber of Full GC Events.
</pre>
<h3>-gccause Option</h3>
<p> This option displays the same summary of garbage collection statistics as the <code>-gcutil</code> option, but includes the causes of the last garbage collection event and (if applicable) the current garbage collection event. In addition to the columns listed for <code>-gcutil</code>, this option adds the following columns: </p>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Garbage Collection Statistics, Including GC Events
<code>Column</code><code>Description</code>
LGCC
GCC
</pre>
<h3>-gcnew Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
New Generation Statistics
<code>Column</code><code>Description</code>
S0C
S1C
S0U
S1U
TTTenuring threshold.
MTT
DSS
EC
EU
YGC
YGCT
</pre>
<h3>-gcnewcapacity Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
New Generation Space Size Statistics
<code>Column</code><code>Description</code>
NGCMN
NGCMX
NGC
S0CMX
S0C
S1CMX
S1C
ECMX
EC
YGC
FGCNumber of Full GC Events.
</pre>
<h3>-gcold Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Old and Permanent Generation Statistics
<code>Column</code><code>Description</code>
PC
PU
OC
OU
YGC
FGCNumber of full GC events.
FGCT
GCT
</pre>
<h3>-gcoldcapacity Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Old Generation Statistics
<code>Column</code><code>Description</code>
OGCMN
OGCMX
OGC
OC
YGC
FGCNumber of full GC events.
FGCT
GCT
</pre>
<h3>-gcpermcapacity Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Permanent Generation Statistics
<code>Column</code><code>Description</code>
PGCMN
PGCMX
PGC
PC
YGC
FGCNumber of full GC events.
FGCT
GCT
</pre>
<h3>-gcutil Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Summary of Garbage Collection Statistics
<code>Column</code><code>Description</code>
S0
S1
E
O
P
YGC
YGCT
FGCNumber of full GC events.
FGCT
GCT
</pre>
<h3>-printcompilation Option</h3>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
HotSpot Compiler Method Statistics
<code>Column</code><code>Description</code>
Compiled
Size
TypeCompilation type.
Method
</pre>
<h2>EXAMPLES</h2>
<p> This section presents some examples of monitoring a local JVM with a <i>lvmid</i> of 21891. </p>
<h3>Using the gcutil option</h3>
<p> This example attaches to <i>lvmid</i> 21891 and takes 7 samples at 250 millisecond intervals and displays the output as specified by the <code>-gcutil</code> option. </p>
<pre>
<code>jstat -gcutil 21891 250 7</code>
<br>
  S0     S1     E      O      P     YGC    YGCT    FGC    FGCT     GCT
<br>
 12.44   0.00  27.20   9.49  96.70    78    0.176     5    0.495    0.672
<br>
 12.44   0.00  62.16   9.49  96.70    78    0.176     5    0.495    0.672
<br>
 12.44   0.00  83.97   9.49  96.70    78    0.176     5    0.495    0.672
<br>
  0.00   7.74   0.00   9.51  96.70    79    0.177     5    0.495    0.673
<br>
  0.00   7.74  23.37   9.51  96.70    79    0.177     5    0.495    0.673
<br>
  0.00   7.74  43.82   9.51  96.70    79    0.177     5    0.495    0.673
<br>
  0.00   7.74  58.11   9.51  96.71    79    0.177     5    0.495    0.673
<br>
</pre>
<p> The output of this example shows that a young generation collection occurred between the 3rd and 4th sample. The collection took 0.001 seconds and promoted objects from the eden space (E) to the old space (O), resulting in an increase of old space utilization from 9.49% to 9.51%. Before the collection, the survivor space was 12.44% utilized, but after this collection it is only 7.74% utilized. </p>
<h3>Repeating the column header string</h3>
<p> This example attaches to <i>lvmid</i> 21891 and takes samples at 250 millisecond intervals and displays the output as specified by <code>-gcutil</code> option. In addition, it uses the <code>-h3</code> option to output the column header after every 3 lines of data. </p>
<pre>
<code>jstat -gcnew -h3 21891 250</code>
<br>
 S0C    S1C    S0U    S1U   TT MTT  DSS      EC       EU     YGC     YGCT
<br>
  64.0   64.0    0.0   31.7 31  31   32.0    512.0    178.6    249    0.203
<br>
  64.0   64.0    0.0   31.7 31  31   32.0    512.0    355.5    249    0.203
<br>
  64.0   64.0   35.4    0.0  2  31   32.0    512.0     21.9    250    0.204
<br>
 S0C    S1C    S0U    S1U   TT MTT  DSS      EC       EU     YGC     YGCT
<br>
  64.0   64.0   35.4    0.0  2  31   32.0    512.0    245.9    250    0.204
<br>
  64.0   64.0   35.4    0.0  2  31   32.0    512.0    421.1    250    0.204
<br>
  64.0   64.0    0.0   19.0 31  31   32.0    512.0     84.4    251    0.204
<br>
 S0C    S1C    S0U    S1U   TT MTT  DSS      EC       EU     YGC     YGCT
<br>
  64.0   64.0    0.0   19.0 31  31   32.0    512.0    306.7    251    0.204
<br>
</pre>
<p> In addition to showing the repeating header string, this example shows that between the 2nd and 3rd samples, a young GC occurred. Its duration was 0.001 seconds. The collection found enough live data that the survivor space 0 utilization (S0U) would would have exceeded the desired survivor Size (DSS). As a result, objects were promoted to the old generation (not visible in this output), and the tenuring threshold (TT) was lowered from 31 to 2. </p>
<p> Another collection occurs between the 5th and 6th samples. This collection found very few survivors and returned the tenuring threshold to 31. </p>
<h3>Including a time stamp for each sample</h3>
<p> This example attaches to <i>lvmid</i> 21891 and takes 3 samples at 250 millisecond intervals. The <code>-t</code> option is used to generate a time stamp for each sample in the first column. </p>
<pre>
<code>jstat -gcoldcapacity -t 21891 250 3</code>
<br>
Timestamp          OGCMN        OGCMX         OGC           OC       YGC   FGC    FGCT    GCT
<br>
          150.1       1408.0      60544.0      11696.0      11696.0   194    80    2.874   3.799
<br>
          150.4       1408.0      60544.0      13820.0      13820.0   194    81    2.938   3.863
<br>
          150.7       1408.0      60544.0      13820.0      13820.0   194    81    2.938   3.863
<br>
</pre>
<p> The <i>Timestamp</i> column reports the elapsed time in seconds since the start of the target JVM. In addition, the <code>-gcoldcapacity</code> output shows the old generation capacity (OGC) and the old space capacity (OC) increasing as the heap expands to meet allocation and/or promotion demands. The old generation capacity (OGC) has grown to from 11696 KB to 13820 KB after the 81st Full GC (FGC). The maximum capacity of the generation (and space) is 60544 KB (OGCMX), so it still has room to expand. </p>
<h3>Monitor instrumentation for a remote JVM</h3>
<p> This example attaches to <i>lvmid</i> 40496 on the system named <i>remote.domain</i> using the <code>-gcutil</code> option, with samples taken every second indefinitely. </p>
<pre>
<code>jstat -gcutil 40496 [at] remote.domain 1000</code>
<br>
<br>
</pre>
<p> The <i>lvmid</i> is combined with the name of the remote host to construct a <i>vmid</i> of <i>40496 [at] remote.domain</i>. This <i>vmid</i> results in the use of the <code>rmi</code> protocol to communicate to the default <code>jstatd</code> server on the remote host. The <code>jstatd</code> server is located using the <code>rmiregistry</code> on <i>remote.domain</i> that is bound to the default <code>rmiregistry</code> port (port 1099). </p>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-java/">java</a>(1) &#8211; the Java Application Launcher</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jps/">jps</a>(1) &#8211; the Java Process Status Application</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jstatd/">jstatd</a>(1) &#8211; the jvmstat daemon</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-rmiregistry/">rmiregistry</a>(1) &#8211; the Java Remote Object Registry</dl>
</dl>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
