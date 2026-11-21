---
title: "jstack(1)"
name: "jstack"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstack/"
description: "jstack – Prints Java thread stack traces for a Java process, core file, or remote debug server. This command is experimental and unsupported."
---
<h2>NAME</h2>
<p> jstack - Prints Java thread stack traces for a Java process, core file, or remote debug server. This command is experimental and unsupported.  </p>
<h2>SYNOPSIS</h2>
<pre><code>
 jstack  [ options  ] pid 
</code></pre>
<pre><code>
 jstack  [ options  ] executable  core 
</code></pre>
<pre><code>
 jstack  [ options  ] [ server-id @ ] remote-hostname-or-IP 
</code></pre>
<dl>
<dt><i>options</i></dt>
<dd> <p> The command-line options. See Options. </p>
 </dd>
<dt><i>pid</i></dt>
<dd> <p> The process ID for which the stack trace is printed. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command. </p>
 </dd>
<dt><i>executable</i></dt>
<dd> <p> The Java executable from which the core dump was produced. </p>
 </dd>
<dt><i>core</i></dt>
<dd> <p> The core file for which the stack trace is to be printed. </p>
 </dd>
<dt><i>remote-hostname-or-IP</i></dt>
<dd> <p> The remote debug server <code>hostname</code> or <code>IP</code> address. See jsadebugd(1). </p>
 </dd>
<dt><i>server-id</i></dt>
<dd> <p> An optional unique ID to use when multiple debug servers are running on the same remote host. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>jstack</code> command prints Java stack traces of Java threads for a specified Java process, core file, or remote debug server. For each Java frame, the full class name, method name, byte code index (BCI), and line number, when available, are printed. With the <code>-m</code> option, the <code>jstack</code> command prints both Java and native frames of all threads with the program counter (PC). For each native frame, the closest native symbol to PC, when available, is printed. C++ mangled names are not demangled. To demangle C++ names, the output of this command can be piped to <code>c++filt</code>. When the specified process is running on a 64-bit Java Virtual Machine, you might need to specify the <code>-J-d64</code> option, for example: <code>jstack -J-d64 -m pid</code>. </p>
<p> <i>Note:</i> This utility is unsupported and might not be available in future release of the JDK. In Windows Systems where the dbgeng.dll file is not present, Debugging Tools For Windows must be installed so these tools work. The <code>PATH</code> environment variable needs to contain the location of the jvm.dll that is used by the target process, or the location from which the crash dump file was produced. For example: </p>
<pre><code>
 set PATH=&lt;jdk&gt;\jre\bin\client;%PATH% 
</code></pre>
<pre><code>
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt>-F</dt>
<dd> <p> <br />
 Force a stack dump when <code>jstack</code> [<code>-l</code>] <code>pid</code> does not respond. </p>
 </dd>
<dt>-l</dt>
<dd> <p> <br />
 Long listing. Prints additional information about locks such as a list of owned <code>java.util.concurrent</code> ownable synchronizers. See the <code>AbstractOwnableSynchronizer</code> class description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/AbstractOwnableSynchronizer.html">http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/AbstractOwnableSynchronizer.html</a> </p>
 </dd>
<dt>-m</dt>
<dd> <p> <br />
 Prints a mixed mode stack trace that has both Java and native C/C++ frames. </p>
 </dd>
<dt>-h</dt>
<dd> <p> <br />
 Prints a help message. </p>
 </dd>
<dt>-help</dt>
<dd> <p> <br />
 Prints a help message. </p>
 </dd></dl>
<h2>KNOWN BUGS</h2>
<p> In mixed mode stack trace, the <code>-m</code> option does not work with the remote debug server.  </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> pstack(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> C++filt(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <a href="/docs/linux/man/1-jps/">jps</a>(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> jsadebugd(1) <br />
 </p>
 </dd></dl>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME </a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS </a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION </a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS </a></dt>
<dd>  </dd>
<dt><a href="#lbAF">KNOWN BUGS </a></dt>
<dd>  </dd>
<dt><a href="#lbAG">SEE ALSO </a></dt>
<dd>  </dd></dl>
