---
title: "jhat-java-1-6-0-openjdk(1)"
name: "jhat-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jhat-java-1-6-0-openjdk/"
description: "jhat – Java Heap Analysis Tool"
---

<p>jhat &#8211; Java Heap Analysis Tool</p>
<h2>Synopsis</h2>
<pre><code>jhat</code> [ <i>options</i> ] &lt;heap-dump-file&gt;</pre>
<h2>Parameters</h2>
<dl>
<dt>options</dt>
<dd>Options, if used, should follow immediately after the command name.</dd>
<dt>heap-dump-file</dt>
<dd>Java binary heap dump file to be browsed. For a dump file that contains multiple heap dumps, you may specify which dump in the file by appending &quot;#&lt;number&gt; to the file name, i.e. &quot;foo.hprof#3&quot;.</dd></dl>
<h2>Description</h2>
<p>The <code>jhat</code> command parses a java heap dump file and launches a webserver. jhat enables you to browse heap dumps using your favorite webbrowser. jhat supports pre-designed queries (such as &#8216;show all instances of a known class &quot;Foo&quot;&#8217;) as well as <code>OQL</code> (<code>O</code>bject <code>Q</code>uery <code>L</code>anguage) &#8211; a SQL-like query language to query heap dumps. Help on OQL is available from the OQL help page shown by jhat. With the default port, OQL help is available at <a rel="nofollow" href="http://localhost:7000/oqlhelp/">http://localhost:7000/oqlhelp/</a> </p>
<p> There are several ways to generate a java heap dump: </p>
<dl>
<dd>
</dd><dl>
<dt>*</dt>
<dd>Use jmap -dump option to obtain a heap dump at runtime;</dd>
<dt>*</dt>
<dd>Use jconsole option to obtain a heap dump via <i>HotSpotDiagnosticMXBean</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/jre/api/management/extension/com/sun/management/HotSpotDiagnosticsMXBean.html">http://java.sun.com/javase/6/docs/jre/api/management/extension/com/sun/management/HotSpotDiagnosticsMXBean.html</a> at runtime;</dd>
<dt>*</dt>
<dd>Heap dump will be generated when OutOfMemoryError is thrown by specifying -XX:+HeapDumpOnOutOfMemoryError VM option;</dd>
<dt>*</dt>
<dd>Use <i>hprof</i> @ <a rel="nofollow" href="https://docs.oracle.com/javase/7/docs/technotes/samples/hprof.html.">https://docs.oracle.com/javase/7/docs/technotes/samples/hprof.html.</a></dd></dl>
</dl>
<p> <code>NOTE:</code> This tool is <code>experimental</code> and may <code>not</code> be available in future versions of the JDK. </p>
<h2>Options</h2>
<dl>
<dt>-stack false/true</dt>
<dd>Turn off tracking object allocation call stack. Note that if allocation site information is not available in the heap dump, you have to set this flag to false. Default is true.</dd>
<dt>-refs false/true</dt>
<dd>Turn off tracking of references to objects. Default is true. By default, back pointers (objects pointing to a given object a.k.a referrers or in-coming references) are calculated for all objects in the heap.</dd>
<dt>-port port-number</dt>
<dd>Set the port for the jhat&#8217;s HTTP server. Default is 7000.</dd>
<dt>-exclude exclude-file</dt>
<dd>Specify a file that lists data members that should be excluded from the &quot;reachable objects&quot; query. For example, if the file lists <i>java.lang.String.value</i>, then, whenever list of objects reachable from a specific object &quot;o&quot; are calculated, reference paths involving <i>java.lang.String.value</i> field will not considered.</dd>
<dt>-baseline baseline-dump-file</dt>
<dd>Specify a baseline heap dump. Objects in both heap dumps with the same object ID will be marked as not being &quot;new&quot;. Other objects will be marked as &quot;new&quot;. This is useful while comparing two different heap dumps.</dd>
<dt>-debug int</dt>
<dd>Set debug level for this tool. 0 means no debug output. Set higher values for more verbose modes.</dd>
<dt>-version&nbsp;<wbr></dt>
<dd>Report version number and exit.</dd>
<dt>-h&nbsp;<wbr></dt>
<dd>Output help message and exit.</dd>
<dt>-help&nbsp;<wbr></dt>
<dd>Output help message and exit.</dd>
<dt>-J&lt;flag&gt;&nbsp;<wbr></dt>
<dd>Pass &lt;flag&gt; to the Java virtual machine on which jhat is run. For example, -J-Xmx512m to use a maximum heap size of 512MB.</dd></dl>
<h2>See Also</h2>
<dl>
<dd>
</dd><dl>
<dt>*</dt>
<dd>jmap &#8211; Java Memory Map</dd>
<dt>*</dt>
<dd>jconsole &#8211; Java Monitoring and Management Console</dd>
<dt>*</dt>
<dd><i>hprof &#8211; Heap and CPU profiling tool</i> @ <a rel="nofollow" href="https://docs.oracle.com/javase/7/docs/technotes/samples/hprof.html.">https://docs.oracle.com/javase/7/docs/technotes/samples/hprof.html.</a></dd></dl>
</dl>
<p>&nbsp;<wbr></p>
