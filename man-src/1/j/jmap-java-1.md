---
title: "jmap-java-1(1)"
name: "jmap-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jmap-java-1/"
description: "jmap – Memory Map"
---
<h2>Name</h2>
<p> jmap - Memory Map </p>
<h2>SYNOPSIS</h2>
<pre><code>
 jmap  [ option ] pid
 jmap  [ option ] executable core
 jmap  [ option ] [server-id@]remote-hostname-or-IP
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dd>  </dd>
<dl>
<dt>option </dt>
<dd> <p> Options are mutually exclusive. Option, if used, should follow immediately after the command name. </p>
 </dd>
<dt>pid </dt>
<dd> <p> process id for which the memory map is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, <a href="/docs/linux/man/1-jps/">jps</a>(1) may be used. <br />
 </p>
 </dd>
<dt>executable </dt>
<dd> <p> Java executable from which the core dump was produced. <br />
 </p>
 </dd>
<dt>core </dt>
<dd> <p> core file for which the memory map is to be printed. <br />
 </p>
 </dd>
<dt>remote-hostname-or-IP </dt>
<dd> <p> remote debug server&#8217;s (see jsadebugd(1)) hostname or IP address. <br />
 </p>
 </dd>
<dt>server-id </dt>
<dd> <p> optional unique id, if multiple debug servers are running on the same remote host. <br />
 </p>
 </dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jmap</code> prints shared object memory maps or heap memory details of a given process or core file or a remote debug server. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<pre><code>
 jmap -J-d64 -heap pid 
</code></pre>
<p> <code>NOTE: This utility is unsupported and may or may not be available in future versions of the JDK. In Windows Systems where dbgeng.dll is not present, &#8216;Debugging Tools For Windows&#8217; needs to be installed to have these tools working. Also, </code><code>PATH</code><code> environment variable should contain the location of </code><code>jvm.dll</code><code> used by the target process or the location from which the Crash Dump file was produced.</code> </p>
<p> <code>For example, </code><code>set PATH=&lt;jdk&gt;\jre\bin\client;%PATH%</code> </p>
<p> <br />
 </p>
<h2>OPTIONS</h2>
<dl>
<dd>  </dd>
<dl>
<dt>&lt;no option&gt; </dt>
<dd> <p> When no option is used jmap prints shared object mappings. For each shared object loaded in the target VM, start address, the size of the mapping, and the full path of the shared object file are printed. This is similar to the Solaris <code>pmap</code> utility. <br />
 </p>
 </dd>
<dt>-dump:[live,]format=b,file=&lt;filename&gt; </dt>
<dd> <p> Dumps the Java heap in hprof binary format to filename. The <i>live</i> suboption is optional. If specified, only the live objects in the heap are dumped. To browse the heap dump, you can use jhat(1) (Java Heap Analysis Tool) to read the generated file. <br />
 </p>
 </dd>
<dt>-finalizerinfo </dt>
<dd> <p> Prints information on objects awaiting finalization. <br />
 </p>
 </dd>
<dt>-heap </dt>
<dd> <p> Prints a heap summary. GC algorithm used, heap configuration and generation wise heap usage are printed. <br />
 </p>
 </dd>
<dt>-histo[:live] </dt>
<dd> <p> Prints a histogram of the heap. For each Java class, number of objects, memory size in bytes, and fully qualified class names are printed. VM internal class names are printed with &#8216;*&#8216; prefix. If the <i>live</i> suboption is specified, only live objects are counted. <br />
 </p>
 </dd>
<dt>-permstat </dt>
<dd> <p> Prints class loader wise statistics of permanent generation of Java heap. For each class loader, its name, liveness, address, parent class loader, and the number and size of classes it has loaded are printed. In addition, the number and size of interned Strings are printed. <br />
 </p>
 </dd>
<dt>-F </dt>
<dd> <p> Force. Use with jmap -dump or jmap -histo option if the pid does not respond. The <i>live</i> suboption is not supported in this mode. <br />
 </p>
 </dd>
<dt>-h </dt>
<dd> <p> Prints a help message. <br />
 <br />
 </p>
 </dd>
<dt>-help </dt>
<dd> <p> Prints a help message. <br />
 <br />
 </p>
 </dd>
<dt>-J&lt;flag&gt; </dt>
<dd> <p> Passes &lt;flag&gt; to the Java virtual machine on which jmap is run. <br />
 </p>
 </dd></dl>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <a href="/docs/linux/man/1-pmap/">pmap</a>(1) </p>
 </dd>
<dt>o</dt>
<dd> <p> jhat(1) </p>
 </dd>
<dt>o</dt>
<dd> <p> <a href="/docs/linux/man/1-jps/">jps</a>(1) </p>
 </dd>
<dt>o</dt>
<dd> <p> jsadebugd(1) </p>
 </dd></dl>
</dl>
<p> <br />
&nbsp;<wbr> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">Name</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">PARAMETERS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">SEE ALSO</a></dt>
<dd>  </dd></dl>
