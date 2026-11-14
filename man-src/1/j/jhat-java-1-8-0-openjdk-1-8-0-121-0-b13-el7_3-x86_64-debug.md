---
title: "jhat-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "jhat-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jhat-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "jhat – Analyzes the Java heap. This command is experimental and unsupported."
---

<p>jhat &#8211; Analyzes the Java heap. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jhat</code> [ <i>options</i> ] <i>heap-dump-file</i> </pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>heap-dump-file</i></p>
<dd>Java binary heap dump file to be browsed. For a dump file that contains multiple heap dumps, you can specify which dump in the file by appending <code>#&lt;number&gt;</code> to the file name, for example, <code>myfile.hprof#3</code>.</dl>
<h2>Description</h2>
<p>The <code>jhat</code> command parses a Java heap dump file and starts a web server. The <code>jhat</code> command lets you to browse heap dumps with your favorite web browser. The <code>jhat</code> command supports predesigned queries such as show all instances of a known class <code>MyClass</code>, and Object Query Language (OQL). OQL is similar to SQL, except for querying heap dumps. Help on OQL is available from the OQL help page shown by the <code>jhat</code> command. With the default port, OQL help is available at <a rel="nofollow" href="http://localhost:7000/oqlhelp/">http://localhost:7000/oqlhelp/</a> </p>
<p> There are several ways to generate a Java heap dump:</p>
<dl>
<dt>&bull;</p>
<dd>Use the <code>jmap -dump</code> option to obtain a heap dump at runtime. See <a href="/docs/linux/man/1-jmap/">jmap</a>(1).</p>
<dt>&bull;</p>
<dd>Use the <code>jconsole</code> option to obtain a heap dump through <code>HotSpotDiagnosticMXBean</code> at runtime. See <a href="/docs/linux/man/1-jconsole/">jconsole</a>(1) and the <code>HotSpotDiagnosticMXBean</code> interface description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/jre/api/management/extension/com/sun/management/HotSpotDiagnosticMXBean.html">http://docs.oracle.com/javase/8/docs/jre/api/management/extension/com/sun/management/HotSpotDiagnosticMXBean.html</a></p>
<dt>&bull;</p>
<dd>Heap dump is generated when an <code>OutOfMemoryError</code> is thrown by specifying the <code>-XX:+HeapDumpOnOutOfMemoryError</code> Java Virtual Machine (JVM) option.</p>
<dt>&bull;</p>
<dd>Use the <code>hprof</code> command. See the HPROF: A Heap/CPU Profiling Tool at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/samples/hprof.html">http://docs.oracle.com/javase/8/docs/technotes/samples/hprof.html</a></dl>
<h2>Options</h2>
<dl>
<dt>-stack false|true</p>
<dd>Turns off tracking object allocation call stack. If allocation site information is not available in the heap dump, then you have to set this flag to <code>false</code>. The default is <code>true</code>.</p>
<dt>-refs false|true</p>
<dd>Turns off tracking of references to objects. Default is <code>true</code>. By default, back pointers, which are objects that point to a specified object such as referrers or incoming references, are calculated for all objects in the heap.</p>
<dt>-port <i>port-number</i></p>
<dd>Sets the port for the <code>jhat</code> HTTP server. Default is 7000.</p>
<dt>-exclude <i>exclude-file</i></p>
<dd>Specifies a file that lists data members that should be excluded from the reachable objects query. For example, if the file lists <code>java.lang.String.value</code>, then, then whenever the list of objects that are reachable from a specific object <code>o</code> are calculated, reference paths that involve <code>java.lang.String.value</code> field are not considered.</p>
<dt>-baseline <i>exclude-file</i></p>
<dd>Specifies a baseline heap dump. Objects in both heap dumps with the same object ID are marked as not being new. Other objects are marked as new. This is useful for comparing two different heap dumps.</p>
<dt>-debug <i>int</i></p>
<dd>Sets the debug level for this tool. A level of 0 means no debug output. Set higher values for more verbose modes.</p>
<dt>-version</p>
<dd>Reports the release number and exits</p>
<dt>-h</p>
<dd>Dsiplays a help message and exits.</p>
<dt>-help</p>
<dd>Displays a help message and exits.</p>
<dt>-J<i>flag</i></p>
<dd>Passes <code>flag</code> to the Java Virtual Machine on which the <code>jhat</code> command is running. For example, <code>-J-Xmx512m</code> to use a maximum heap size of 512 MB.</dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jmap/">jmap</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jconsole/">jconsole</a>(1)</p>
<dt>&bull;</p>
<dd>HPROF: A Heap/CPU Profiling Tool at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/samples/hprof.html">http://docs.oracle.com/javase/8/docs/technotes/samples/hprof.html</a> </p>
</dl>
