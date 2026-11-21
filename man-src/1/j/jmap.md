---
title: "jmap(1)"
name: "jmap"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jmap/"
description: "jmap – Prints shared object memory maps or heap memory details for a process, core file, or remote debug server. This command is experimental and unsupported."
---
<h2>NAME</h2>
<p> jmap - Prints shared object memory maps or heap memory details for a process, core file, or remote debug server. This command is experimental and unsupported.  </p>
<h2>SYNOPSIS</h2>
<pre><code>
 jmap  [ options  ] pid 
</code></pre>
<pre><code>
 jmap  [ options  ] executable  core 
</code></pre>
<pre><code>
 jmap  [ options  ] [ pid  ] server-id @ ] remote-hostname-or-IP 
</code></pre>
<dl>
<dt><i>options</i></dt>
<dd> <p> The command-line options. See Options. </p>
 </dd>
<dt><i>pid</i></dt>
<dd> <p> The process ID for which the memory map is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command. </p>
 </dd>
<dt><i>executable</i></dt>
<dd> <p> The Java executable from which the core dump was produced. </p>
 </dd>
<dt><i>core</i></dt>
<dd> <p> The core file for which the memory map is to be printed. </p>
 </dd>
<dt><i>remote-hostname-or-IP</i></dt>
<dd> <p> The remote debug server <code>hostname</code> or <code>IP</code> address. See jsadebugd(1). </p>
 </dd>
<dt><i>server-id</i></dt>
<dd> <p> An optional unique ID to use when multiple debug servers are running on the same remote host. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>jmap</code> command prints shared object memory maps or heap memory details of a specified process, core file, or remote debug server. If the specified process is running on a 64-bit Java Virtual Machine (JVM), then you might need to specify the <code>-J-d64</code> option, for example: <code>jmap</code><code>-J-d64 -heap pid</code>. </p>
<p> <i>Note:</i> This utility is unsupported and might not be available in future releases of the JDK. On Windows Systems where the <code>dbgeng.dll</code> file is not present, Debugging Tools For Windows must be installed to make these tools work. The <code>PATH</code> environment variable should contain the location of the <code>jvm.dll</code> file that is used by the target process or the location from which the crash dump file was produced, for example: <code>set PATH=%JDK_HOME%\jre\bin\client;%PATH%</code>.  </p>
<h2>OPTIONS</h2>
<dl>
<dt>&lt;no option&gt;</dt>
<dd> <p> When no option is used, the <code>jmap</code> command prints shared object mappings. For each shared object loaded in the target JVM, the start address, size of the mapping, and the full path of the shared object file are printed. This behavior is similar to the Oracle Solaris <code>pmap</code> utility. </p>
 </dd>
<dt>-dump:[live,] format=b, file=<i>filename</i></dt>
<dd> <p> <br />
 Dumps the Java heap in <code>hprof</code> binary format to <code>filename</code>. The <code>live</code> suboption is optional, but when specified, only the active objects in the heap are dumped. To browse the heap dump, you can use the jhat(1) command to read the generated file. </p>
 </dd>
<dt>-finalizerinfo</dt>
<dd> <p> <br />
 Prints information about objects that are awaiting finalization. </p>
 </dd>
<dt>-heap</dt>
<dd> <p> <br />
 Prints a heap summary of the garbage collection used, the head configuration, and generation-wise heap usage. In addition, the number and size of interned Strings are printed. </p>
 </dd>
<dt>-histo[:live]</dt>
<dd> <p> <br />
 Prints a histogram of the heap. For each Java class, the number of objects, memory size in bytes, and the fully qualified class names are printed. The JVM internal class names are printed with an asterisk (*) prefix. If the <code>live</code> suboption is specified, then only active objects are counted. </p>
 </dd>
<dt>-clstats</dt>
<dd> <p> <br />
 Prints class loader wise statistics of Java heap. For each class loader, its name, how active it is, address, parent class loader, and the number and size of classes it has loaded are printed. </p>
 </dd>
<dt>-F</dt>
<dd> <p> <br />
 Force. Use this option with the <code>jmap -dump</code> or <code>jmap -histo</code> option when the pid does not respond. The <code>live</code> suboption is not supported in this mode. </p>
 </dd>
<dt>-h</dt>
<dd> <p> <br />
 Prints a help message. </p>
 </dd>
<dt>-help</dt>
<dd> <p> <br />
 Prints a help message. </p>
 </dd>
<dt>-J <i>flag</i></dt>
<dd> <p> <br />
 Passes <code>flag</code> to the Java Virtual Machine where the <code>jmap</code> command is running. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> jhat(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <a href="/docs/linux/man/1-jps/">jps</a>(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> jsadebugd(1) <br />
 </p>
 </dd></dl>
