---
title: "nettee(1)"
name: "nettee"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nettee/"
---

<h2 class="name">NAME</h2>
<dl>
<dt>nettee &#8211; a network &quot;tee&quot; program</p>
<dd>
</dl>
<h2>SYNOPSIS</h2>
<p> <code>nettee</code> <i>[options]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>nettee</code> passes a data stream to one or more child nodes using a daisychain method. On each node <code>nettee</code> may also direct the stream to a file or pipe. <code>nettee</code> allows large amounts of data to be quickly distributed to multiple nodes on a network at a rate limited only by the network bandwidth. The distribution chain is typically linear for each network switch but may branch when nodes utilize multiple switches. For maximum throughput only one instance of <code>nettee</code> should utilize each network interface. </p>
<p> When <code>nettee</code> starts it waits for a connection from the upstream node before attempting to connect to its downstream nodes. Consequently <code>nettee</code> may be started on the nodes in any order (by a script, rsh, ssh, and so forth.) Typically only the node that reads the data stream for stdin or a file will be set to log messages, so that the progress of the transfer may be monitored. Transmission errors are detected by comparing the total number of bytes read by each child node with the number of bytes transmitted to that child. </p>
<h3>Error Handling</h3>
<p> By default severe errors cause the entire chain to abort. By utilizing the <code>-conwf</code> and <code>-colwf</code> options <code>nettee</code> may be instructed to do its best to continue processing in the event of certain write failures of the data stream. Note that failures which occur while the distribution chain is forming are still fatal events. To allow the program to continue with a truncated or alternate chain if chain formation errors are encountered utilize the <code>-connf</code> option, and optionally specify alternate targets in each hostlist. If the node above the failed node is allowed to emit messages and errors ( for instance: <code>-v 5</code> ) messages similar to these will be sent to the log destination ( <code>-log</code> ): </p>
<p> <code>Failures detected in child 0 [node34]: NWF</code><br />
 <code>Failures detected in child 1 [node35]: NONE</code><br />
 <code>Failures detected in chain: NWF</code> </p>
<p> The first type of message describes the failures that were detected in the named child node, that is, those named in the <code>-next</code> option. The second message describes failures that were detected anywhere further on in the chain. The error codes currently defined are: <code>NONE</code> no errors, <code>NWF</code> network write failure, <code>LWF</code> local write failure, <code>BBC</code> child returned incorrect byte count, <code>BSTAT</code> child returned unknown or bad status, and <code>NNF</code> could not connect to (one or more) downstream chain nodes.</p>
<h3>Exit Status</h3>
<p> <code>nettee</code> will normally emit an <code>EXIT_SUCCESS</code> status. (0 on Unix.) This is true even if the errors were detected and handled in the node itself or in a child node. <code>nettee</code> will emit an <code>EXIT_FAILURE</code> status if it was forced to close by an unhandled event such as a timeout, write failure, or unexpected socket closure. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print help information. </p>
<dt><code>-hexamples</code></p>
<dd> Print examples. </p>
<dt><code>-herrors</code></p>
<dd> Print error status codes. </p>
<dt><code>-i</code></p>
<dd> Print version, license, and copyright information. </p>
<dt><code>-in</code><i> &lt;SRC&gt;</i></p>
<dd> Reads data from <i>&lt;SRC&gt;</i> which may have one of three values: <code>nettee</code> reads from the upstream node; <code>&#8211;</code> reads from stdin; <code>socket</code> read the output of a command from a socket; <code>filename</code> reads from a file. If no <code>-in</code> option is present the programs reads data from the upstream node. </p>
<dt><code>-out</code><i> &lt;DST&gt;</i></p>
<dd> Writes data locally to <i>&lt;DST&gt;</i> which may have one of three values: <code>none</code> writes nothing locally; <code>&#8211;</code> writes to stdout; <code>socket</code> write the datastream to a command through a socket; <code>filename</code> writes to a file. If no <code>-out</code> option is present the program writes data to stdout. </p>
<dt><code>-next</code><i> &lt;HOSTLISTS&gt;</i></p>
<dd> Writes data to downstream destination[s] <code>hostlist1(,hostlist2(,hostlist3(&#8230;)))</code> where the hostlist entries are separated by commas or spaces. A hostlist consists of either a single hostname, or a comma separated list of hostnames enclosed in square brackets. Example: <code>node1,[node2,node3],[node4,node5,node6],node7.</code> The bracketed form allows for automatic failover if unreachable nodes are encountered and if <code>-connf</code> is specified. The first hostname in the list is tried, then the next, and so on. There may be 1-8 hostlists. The number of hostlists controls the topology of the distribution chain. Use a linear distribution chain (a single hostlist) when all nodes share a single network switch. Use a forked distribution chain (multiple hostlist) when nodes are connected to two or more network switches. The End of Chain condition (no downstream write) is indicated by a <i>&lt;HOSTS&gt;</i> value of <code>.</code> , , or <code>_EOC_.</code> An End of Chain condition is also indicated by the absence of an <code>-next</code> option. If End of Chain is indicated there may not be any other hostslists specified. </p>
<dt><code>-cmd</code><i> &lt;COMMAND&gt;</i></p>
<dd> Specifies the command to use in conjunction with an <code>-in socket</code> or <code>-out socket</code> option. Since only a single <code>&lt;COMMAND&gt;</code> may be specified <code>socket</code> may not be applied to both <code>-in</code> and <code>-out</code> at the same time. When <code>-cmd</code> is used with <code>-in socket</code> a child process running <code>&lt;COMMAND&gt;</code> reads data from a disk or other device and writes the resulting data stream to stdout. When <code>-cmd</code> is used with <code>-out socket</code> a child process running <code>&lt;COMMAND&gt;</code> reads the datastream from stdin and writes the processed data to a disk or other device. Typically the <code>&lt;COMMAND&gt;</code> string invokes <code>tar</code> or some other archiving program. In some instances using sockets and <code>-cmd</code> will be faster than using the same command in a pipe due to the larger buffer size used for the socket. Run <code>nettee -hexamples</code> to see a usage example. </p>
<dt><code>-stm</code><i> &lt;EOS&gt;</i></p>
<dd> stream text through a <code>nettee </code> chain until the string <code>&lt;EOS&gt;</code> is encountered, then exit. This allows short text messages to traverse the chain without waiting for a buffer to fill. Since the text message can very rapidly traverse the <code>nettee</code> chain it can be piped into <code>execinput</code> (or any other program that will execute its stdin as commands) to produce essentially simultaneous execution on all target nodes. The <code>&lt;EOS&gt;</code> string is not passed through the data chain and its length is ignored. When used to start further <code>nettee</code> processes on the target nodes <code>&lt;PORT&gt;</code> values must be chosen to avoid interference. While this mode may be convenient for setting up Beowulf nodes it is exceedingly dangerous for general use since any command introduced into the command stream will execute on all chain nodes as if submitted by the owner of the nettee process on that node. Run <code>nettee -hexamples</code> to see a usage example. </p>
<dt><code>-name</code><i> &lt;STRING&gt;</i></p>
<dd> Specify the node name used in messages (&lt;=127 characters). If not supplied the values of the environmental variables <code>MYHOSTNAME</code> and <code>HOSTNAME</code> are first checked, and if those are not defined, the result of a <code>gethostname()</code> call is used. </p>
<dt><code>-log</code><i> &lt;LDST&gt;</i></p>
<dd> Errors and messages are written to <i>&lt;LDST&gt;</i> which may have one of two values: <code>&#8211;</code> writes to stderr or <code>filename</code> writes to a file. If no <code>-log</code> option is present the program writes messages to stderr. </p>
<dt><code>-p,-port</code><i> &lt;PORT&gt;</i></p>
<dd> First of two consecutive ports use for communication. If no <code>-port</code> option is present the program uses the default value of 9997. </p>
<dt><code>-v</code><i> &lt;VERBOSE&gt;</i></p>
<dd> <code>&lt;VERBOSE&gt;</code> is a bit mask which controls the types of warning and error messages which are sent to the <code>-log</code> destination. Bit values indicate: <code>1 </code> show error messages; <code>2 </code> show command line settings; <code>4</code> show messages; <code>8</code> show periodic status messages during transfer; <code>16</code> prepend nodename to all messages. Use a <code>&lt;VERBOSE&gt;</code> value of 0 to eliminate all messages. If no <code>-v</code> is present the program uses a default <code>&lt;VERBOSE&gt;</code> value of 1. </p>
<dt><code>-q</code></p>
<dd> Suppresss &quot;ignored signal&quot; messages. </p>
<dt><code>-t</code><i> &lt;WAIT&gt;</i></p>
<dd> Wait up to <code>&lt;WAIT&gt;</code> seconds for a connection from upstream in the chain to form or data to be received. If neither of these events occur exit with an error. A value of <code>0</code> waits forever and will only exit on an end of data condition. If no <code>-t</code> is present the program uses a default <code>&lt;WAIT&gt;</code> value of 0. The <code>-iconnf</code><i>&lt;WAIT&gt;</i> and <code>-w</code> options control timeouts for downstream connections. </p>
<dt><code>-w</code></p>
<dd> Wait for the next node to boot or attach to the network. If not specified and the next node is not reachable <code>nettee</code> will exit with an error no matter what the <code>-t</code><i> &lt;WAIT&gt;</i> and <code>-iconnf</code><i> &lt;WAIT&gt;</i> timeout values are. </p>
<dt><code>-colwf</code></p>
<dd> Continue on Local Write Failure. Normally the failure of a write of the data stream to the local output will be fatal and the entire distribution chain will collapse immediately. (Typically this happens when data is written to disk and a partition fills or there is an ownership problem. A complete disk failure may initially present this way but often goes on to crash the node, resulting also in a network write failure.) When <code>-colwf</code> is set and a local write failure occurs on a node that node will continue to relay data down the chain. The node that failed will not have correctly processed the data stream locally but all other nodes will be unaffected by this failure. The top node will emit an error message when this occurs so that a subsequent analysis with other tools may locate the node(s) which failed. This option may only be employed on a node that reads data from an upstream node.<br />
&nbsp;<wbr></p>
<dt><code>-conwf</code></p>
<dd> Continue on Network Write Failure. Normally the failure of a write of the data stream to the next node will be fatal and the entire distribution chain will collapse immediately. (Typically this happens when a node crashes while nettee is running.) When <code>-conwf</code> is set and a network write failure occurs on a node (indicating that the next node has failed) the node will continue to process the data stream locally but will make no further attempts to transfer data to the next node in the chain. This allows the data transfer to complete on a chain down to the node above a failed node. The top node will emit an error message when this occurs so that a subsequent analysis with other tools may locate the node(s) which failed. This option may only be employed on a node that reads data from an upstream node </p>
<dt><code>-connf</code><i> &lt;WAIT&gt;</i></p>
<dd> Continue on Next Node Failure. Give each node in a hostlist <code>&lt;WAIT&gt;</code> seconds to join the chain. After that each successive host in the hostlist is given <code>&lt;WAIT&gt;</code> seconds to join, and if none succeed, no data will be sent to any of those hosts. If <code>-connf</code> is not specified or the wait time is set to zero seconds, the program will wait forever for a connection to the first node in each hostlist. </p>
<dt><code>-progress</code><i> &lt;INTERVAL&gt;</i></p>
<dd> If <code>-v 8</code> is used a status message is emitted every <code>&lt;INTERVAL&gt;</code> bytes transferred. The default value of 10000000 will be too small for a very fast network. </p>
</dl>
<h2>RELATED PROGRAMS</h2>
<p> <code><a href="/docs/linux/man/1-netcat/">netcat</a>(1).</code> </p>
<p> <code>nettee</code> is derived from Felix Rauch&#8217;s <code>dolly</code> which is available here: <code><a rel="nofollow" href="http://www.cs.inf.ethz.ch/CoPs/patagonia/#dolly">http://www.cs.inf.ethz.ch/CoPs/patagonia/#dolly</a></code> </p>
<p> The <code>nettee</code> home page is: <code><a rel="nofollow" href="http://saf.bio.caltech.edu/nettee.html">http://saf.bio.caltech.edu/nettee.html</a></code> </p>
<h2>COPYRIGHTS</h2>
<pre>
Copyright: 2008 David Mathog and Caltech.
Copyright: Felix Rauch and ETH Zurich
</pre>
<h2>LICENSE</h2>
<p> Freely distributed under the second GNU General Public License (GPL 2). </p>
<h2>AUTHOR</h2>
<pre>
David Mathog
Biology Division, Caltech
</pre>
<h2>Index</h2>
