---
title: "jmap-java-1-6-0-openjdk(1)"
name: "jmap-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jmap-java-1-6-0-openjdk/"
description: "jmap – Memory Map"
---

<p>jmap &#8211; Memory Map</p>
<h2>Synopsis</h2>
<pre><code>jmap</code> [ option ] pid
<code>jmap</code> [ option ] executable core
<code>jmap</code> [ option ] [server-id@]remote-hostname-or-IP</pre>
<h2>Parameters</h2>
<dl>
<dt>option</dt>
<dd>Options are mutually exclusive. Option, if used, should follow immediately after the command name.</dd>
<dt>pid</dt>
<dd>process id for which the memory map is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, jps may be used.</dd>
<dt>executable</dt>
<dd>Java executable from which the core dump was produced.</dd>
<dt>core</dt>
<dd>core file for which the memory map is to be printed.</dd>
<dt>remote-hostname-or-IP</dt>
<dd>remote debug server&#8217;s (see jsadebugd) hostname or IP address.</dd>
<dt>server-id</dt>
<dd>optional unique id, if multiple debug servers are running on the same remote host. </dd>
</dl>
<h2>Description</h2>
<p><code>jmap</code> prints shared object memory maps or heap memory details of a given process or core file or a remote debug server. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<dl>
<dd>
<pre><code>jmap -J-d64 -heap pid</code></pre>
</dd></dl>
<p> <code>NOTE &#8211; This utility is unsupported and may or may not be available in future versions of the JDK.</code> </p>
<p> The only forms of jmap available on the Windows platform are</p>
<dl>
<dd>jmap -dump:&lt;<i>dump-options</i>&gt; pid</dd></dl>
<p> and</p>
<dl>
<dd>jmap -histo[:live] pid</dd></dl>
<h2>Options</h2>
<dl>
<dt>&lt;no</dt>
<dd>option&gt; When no option is used jmap prints shared object mappings. For each shared object loaded in the target VM, start address, the size of the mapping, and the full path of the shared object file are printed. This is similar to the Solaris <code>pmap</code> utility.</dd>
<dt>-dump:[live,]format=b,file=&lt;filename&gt;</dt>
<dd>Dumps the Java heap in hprof binary format to filename. The <i>live</i> suboption is optional. If specified, only the live objects in the heap are dumped. To browse the heap dump, you can use jhat (Java Heap Analysis Tool) to read the generated file.</dd>
<dt>-finalizerinfo</dt>
<dd>Prints information on objects awaiting finalization.</dd>
<dt>-heap</dt>
<dd>Prints a heap summary. GC algorithm used, heap configuration and generation wise heap usage are printed.</dd>
<dt>-histo[:live]</dt>
<dd>Prints a histogram of the heap. For each Java class, number of objects, memory size in bytes, and fully qualified class names are printed. VM internal class names are printed with &#8216;*&#8217; prefix. If the <i>live</i> suboption is specified, only live objects are counted.</dd>
<dt>-permstat</dt>
<dd>Prints class loader wise statistics of permanent generation of Java heap. For each class loader, its name, liveness, address, parent class loader, and the number and size of classes it has loaded are printed. In addition, the number and size of interned Strings are printed.</dd>
<dt>-F</dt>
<dd>Force. Use with jmap -dump or jmap -histo option if the pid does not respond. The <i>live</i> suboption is not supported in this mode.</dd>
<dt>-h</dt>
<dd>Prints a help message. </dd>
<dt>-help</dt>
<dd>Prints a help message. </dd>
<dt>-J&lt;flag&gt;</dt>
<dd>Passes &lt;flag&gt; to the Java virtual machine on which jmap is run. </dd>
</dl>
<h2>See Also</h2>
<dl>
<dd>
</dd><dl>
<dt>*</dt>
<dd>pmap (1)</dd>
<dt>*</dt>
<dd>jhat</dd>
<dt>*</dt>
<dd>jps</dd>
<dt>*</dt>
<dd>jsadebugd</dd></dl>
</dl>
<p>&nbsp;<wbr></p>
