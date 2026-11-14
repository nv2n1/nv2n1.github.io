---
title: "java-java-1-6-0-openjdk(1)"
name: "java-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-java-java-1-6-0-openjdk/"
description: "java – the Java application launcher"
---

<p>java &#8211; the Java application launcher</p>
<h2>Synopsis</h2>
<pre><code>java</code> [ options ] class [ argument ... ]
 <code>java</code> [ options ] <code>-jar</code> file.jar [ argument ... ]</pre>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>options</p>
<dd>Command-line options.</p>
<dt>class</p>
<dd>Name of the class to be invoked.</p>
<dt>file.jar</p>
<dd>Name of the jar file to be invoked. Used only with <i>-jar</i>.</p>
<dt>argument</p>
<dd>Argument passed to the <code>main</code> function.</dl>
</dl>
</dl>
<h2>Description</h2>
<p>The <code>java</code> tool launches a Java application. It does this by starting a Java runtime environment, loading a specified class, and invoking that class&#8217;s <code>main</code> method. </p>
<p> The method must be declared public and static, it must not return any value, and it must accept a <i>String</i> array as a parameter. The method declaration must look like the following: </p>
<pre><code> public static void main(String args[])</code></pre>
<p>By default, the first non-option argument is the name of the class to be invoked. A fully-qualified class name should be used. If the <code>-jar</code> option is specified, the first non-option argument is the name of a <code>JAR</code> archive containing class and resource files for the application, with the startup class indicated by the <code>Main-Class</code> manifest header. </p>
<p> The Java runtime searches for the startup class, and other classes used, in three sets of locations: the bootstrap class path, the installed extensions, and the user class path. </p>
<p> Non-option arguments after the class name or JAR file name are passed to the <code>main</code> function. </p>
<h2>Options</h2>
<p>The launcher has a set of standard options that are supported on the current runtime environment and will be supported in future releases. In addition, the current implementations of the virtual machines support a set of non-standard options that are subject to change in future releases. </p>
<h2>Standard Options</h2>
<dl>
<dd>
<dl>
<dt>-client</p>
<dd></dl>
<p> Select the Java HotSpot Client VM. A 64-bit capable jdk currently ignores this option and instead uses the Java Hotspot Server VM. </p>
<p> For default VM selection, see Server-Class Machine Detection</p>
<dl>
<dt>-server</p>
<dd></dl>
<p> Select the Java HotSpot Server VM. On a 64-bit capable jdk only the Java Hotspot Server VM is supported so the -server option is implicit. </p>
<p> For default VM selection, see Server-Class Machine Detection</p>
<dl>
<dt>-agentlib:libname[=options]</p>
<dd>Load native agent library <i>libname</i>, e.g.</dl>
<p> -agentlib:hprof </p>
<p> -agentlib:jdwp=help </p>
<p> -agentlib:hprof=help </p>
<p> For more information, see JVMTI Agent Command Line Options.</p>
<dl>
<dt>-agentpath:pathname[=options]</p>
<dd>Load a native agent library by full pathname. For more information, see JVMTI Agent Command Line Options.</p>
<dt>-classpath classpath</p>
<dd>
<dt>-cp classpath</p>
<dd>Specify a list of directories, JAR archives, and ZIP archives to search for class files. Class path entries are separated by colons (<code>:</code>). Specifying <code>-classpath</code> or <code>-cp</code> overrides any setting of the <code>CLASSPATH</code> environment variable.</dl>
<p> If <code>-classpath</code> and <code>-cp</code> are not used and <code>CLASSPATH</code> is not set, the user class path consists of the current directory (<tt>.</tt>). </p>
<p> As a special convenience, a class path element containing a basename of <i>*</i> is considered equivalent to specifying a list of all the files in the directory with the extension <i>.jar</i> or <i>.JAR</i> (a java program cannot tell the difference between the two invocations). </p>
<p> For example, if directory <i>foo</i> contains <i>a.jar</i> and <i>b.JAR</i>, then the class path element <i>foo/*</i> is expanded to a <i>A.jar:b.JAR</i>, except that the order of jar files is unspecified. All jar files in the specified directory, even hidden ones, are included in the list. A classpath entry consisting simply of <i>*</i> expands to a list of all the jar files in the current directory. The <i>CLASSPATH</i> environment variable, where defined, will be similarly expanded. Any classpath wildcard expansion occurs before the Java virtual machine is started &#8212; no Java program will ever see unexpanded wildcards except by querying the environment. For example; by invoking <i>System.getenv(&quot;CLASSPATH&quot;)</i>. </p>
<p> For more information on class paths, see Setting the Class Path.</p>
<dl>
<dt>-Dproperty=value</p>
<dd>Set a system property value.</p>
<dt>-d32</p>
<dd>
<dt>-d64</p>
<dd>Request that the program to be run in a 32-bit or 64-bit environment, respectively. If the requested environment is not installed or is not supported, an error is reported.</dl>
<p> Currently only the Java HotSpot Server VM supports 64-bit operation, and the &quot;-server&quot; option is implicit with the use of -d64. And the &quot;-client&quot; option is ignored with the use of -d64. This is subject to change in a future release. </p>
<p> If neither <code>-d32</code> nor <code>-d64</code> is specified, the default is to run in a 32-bit environment, except for 64-bit only systems. This is subject to change in a future release.</p>
<dl>
<dt>-enableassertions[:&lt;package name&gt;&quot;&#8230;&quot; | :&lt;class name&gt; ]</p>
<dd>
<dt>-ea[:&lt;package name&gt;&quot;&#8230;&quot; | :&lt;class name&gt; ]</p>
<dd>Enable assertions. Assertions are disabled by default.</dl>
<p> With no arguments, <code>enableassertions</code> or <code>-ea</code> enables assertions. With one argument ending in <i>&quot;&#8230;&quot;</i>, the switch enables assertions in the specified package and any subpackages. If the argument is simply <i>&quot;&#8230;&quot;</i>, the switch enables assertions in the unnamed package in the current working directory. With one argument not ending in <i>&quot;&#8230;&quot;</i>, the switch enables assertions in the specified class. </p>
<p> If a single command line contains multiple instances of these switches, they are processed in order before loading any classes. So, for example, to run a program with assertions enabled only in package <i>com.wombat.fruitbat</i> (and any subpackages), the following command could be used: </p>
<pre><code>java -ea:com.wombat.fruitbat... &lt;Main Class&gt;</code></pre>
<p>The <code>-enableassertions</code> and <code>-ea</code> switches apply to <i>all</i> class loaders and to system classes (which do not have a class loader). There is one exception to this rule: in their no-argument form, the switches do <i>not</i> apply to system. This makes it easy to turn on asserts in all classes except for system classes. A separate switch is provided to enable asserts in all system classes; see <code>-enablesystemassertions</code> below.</p>
<dl>
<dt>-disableassertions[:&lt;package name&gt;&quot;&#8230;&quot; | :&lt;class name&gt; ]</p>
<dd>
<dt>-da[:&lt;package name&gt;&quot;&#8230;&quot; | :&lt;class name&gt; ]</p>
<dd>Disable assertions. This is the default.</dl>
<p> With no arguments, <code>disableassertions</code> or <code>-da</code> disables assertions. With one argument ending in <i>&quot;&#8230;&quot;</i>, the switch disables assertions in the specified package and any subpackages. If the argument is simply <i>&quot;&#8230;&quot;</i>, the switch disables assertions in the unnamed package in the current working directory. With one argument not ending in <i>&quot;&#8230;&quot;</i>, the switch disables assertions in the specified class. </p>
<p> To run a program with assertions enabled in package <i>com.wombat.fruitbat</i> but disabled in class <i>com.wombat.fruitbat.Brickbat</i>, the following command could be used: </p>
<pre><code>java -ea:com.wombat.fruitbat... -da:com.wombat.fruitbat.Brickbat &lt;Main Class&gt;</code></pre>
<p>The <code>-disableassertions</code> and <code>-da</code> switches apply to <i>all</i> class loaders and to system classes (which do not have a class loader). There is one exception to this rule: in their no-argument form, the switches do <i>not</i> apply to system. This makes it easy to turn on asserts in all classes except for system classes. A separate switch is provided to enable asserts in all system classes; see <code>-disablesystemassertions</code> below.</p>
<dl>
<dt>-enablesystemassertions</p>
<dd>
<dt>-esa</p>
<dd>Enable asserts in all system classes (sets the <i>default assertion status</i> for system classes to <i>true</i>).</p>
<dt>-disablesystemassertions</p>
<dd>
<dt>-dsa</p>
<dd>Disables asserts in all system classes.</dl>
<dl>
<dt>-jar</p>
<dd>Execute a program encapsulated in a JAR file. The first argument is the name of a JAR file instead of a startup class name. In order for this option to work, the manifest of the JAR file must contain a line of the form <code>Main-Class: </code><tt>classname</tt>. Here, <i>classname</i> identifies the class having the <i>public static void main(String[]&nbsp;<wbr>args)</i> method that serves as your application&#8217;s starting point. See the Jar tool reference page and the Jar trail of the <i>Java Tutorial</i> @ <a rel="nofollow" href="http://java.sun.com/docs/books/tutorial/jar">http://java.sun.com/docs/books/tutorial/jar</a> for information about working with Jar files and Jar-file manifests.</dl>
<p> When you use this option, the JAR file is the source of all user classes, and other user class path settings are ignored. </p>
<p> Note that JAR files that can be run with the &quot;java -jar&quot; option can have their execute permissions set so they can be run without using &quot;java -jar&quot;. Refer to Java Archive (JAR) Files.</p>
<dl>
<dt>-javaagent:jarpath[=options]</p>
<dd>Load a Java programming language agent, see java.lang.instrument.</p>
<dt>-verbose</p>
<dd>
<dt>-verbose:class</p>
<dd>Display information about each class loaded.</p>
<dt>-verbose:gc</p>
<dd>Report on each garbage collection event.</p>
<dt>-verbose:jni</p>
<dd>Report information about use of native methods and other Java Native Interface activity.</p>
<dt>-version</p>
<dd>Display version information and exit.</p>
<dt>-version:release</p>
<dd>Specifies that the version specified by <i>release</i> is required by the class or jar file specified on the command line. If the version of the java command invoked does not meet this specification and an appropriate implementation is found on the system, the appropriate implementation will be used.</dl>
<p> <i>release</i> not only can specify an exact version, but can also specify a list of versions called a version string. A version string is an ordered list of version ranges separated by spaces. A version range is either a version-id, a version-id followed by a star (*), a version-id followed by a plus sign (+) , or two version-ranges combined using an ampersand (&amp;). The star means prefix match, the plus sign means this version or greater, and the ampersand means the logical anding of the two version-ranges. For example: </p>
<pre><code>-version:&quot;1.5.0_04 1.5*&amp;1.5.1_02+&quot;</code></pre>
<p>The meaning of the above is that the class or jar file requires either version 1.5.0_02, or a version with 1.5 as a version-id prefix and that is not less than 1.5.1_02. The exact syntax and definition of version strings may be found in Appendix A of the Java Network Launching Protocol &amp; API Specification (JSR-56). </p>
<p> For jar files, the usual preference is to specify version requirements in the jar file manifest rather than on the command line. </p>
<p> See the following NOTES section for important policy information on the use of this option.</p>
<dl>
<dt>-showversion</p>
<dd>Display version information and continue.</p>
<dt>-?</p>
<dd>
<dt>-help</p>
<dd>Display usage information and exit.</p>
<dt>-X</p>
<dd>Display information about non-standard options and exit.</dl>
</dl>
<h3>Non-Standard Options</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-Xint</p>
<dd>Operate in interpreted-only mode. Compilation to native code is disabled, and all bytecodes are executed by the interpreter. The performance benefits offered by the Java HotSpot VMs&#8217; adaptive compiler will not be present in this mode.</p>
<dt>-Xbatch</p>
<dd>Disable background compilation. Normally the VM will compile the method as a background task, running the method in interpreter mode until the background compilation is finished. The <i>-Xbatch</i> flag disables background compilation so that compilation of all methods proceeds as a foreground task until completed.</p>
<dt>-Xbootclasspath:bootclasspath</p>
<dd>Specify a colon-separated list of directories, JAR archives, and ZIP archives to search for boot class files. These are used in place of the boot class files included in the Java 2 SDK. <i>Note: Applications that use this option for the purpose of overriding a class in rt.jar should not be deployed as doing so would contravene the Java 2 Runtime Environment binary code license.</i></p>
<dt>-Xbootclasspath/a:path</p>
<dd>Specify a colon-separated path of directires, JAR archives, and ZIP archives to append to the default bootstrap class path.</p>
<dt>-Xbootclasspath/p:path</p>
<dd>Specify a colon-separated path of directires, JAR archives, and ZIP archives to prepend in front of the default bootstrap class path. <i>Note: Applications that use this option for the purpose of overriding a class in rt.jar should not be deployed as doing so would contravene the Java 2 Runtime Environment binary code license.</i></p>
<dt>-Xcheck:jni</p>
<dd>Perform additional checks for Java Native Interface (JNI) functions. Specifically, the Java Virtual Machine validates the parameters passed to the JNI function as well as the runtime environment data before processing the JNI request. Any invalid data encountered indicates a problem in the native code, and the Java Virtual Machine will terminate with a fatal error in such cases. Expect a performance degradation when this option is used.</p>
<dt>-Xfuture</p>
<dd>Perform strict class-file format checks. For purposes of backwards compatibility, the default format checks performed by the Java 2 SDK&#8217;s virtual machine are no stricter than the checks performed by 1.1.x versions of the JDK software. The <code>-Xfuture</code> flag turns on stricter class-file format checks that enforce closer conformance to the class-file format specification. Developers are encouraged to use this flag when developing new code because the stricter checks will become the default in future releases of the Java application launcher.</p>
<dt>-Xnoclassgc</p>
<dd>Disable class garbage collection. Use of this option will prevent memory recovery from loaded classes thus increasing overall memory usage. This could cause OutOfMemoryError to be thrown in some applications.</p>
<dt>-Xincgc</p>
<dd>Enable the incremental garbage collector. The incremental garbage collector, which is off by default, will reduce the occasional long garbage-collection pauses during program execution. The incremental garbage collector will at times execute concurrently with the program and during such times will reduce the processor capacity available to the program.</p>
<dt>-Xloggc:file</p>
<dd>Report on each garbage collection event, as with -verbose:gc, but log this data to <i>file</i>. In addition to the information <i>-verbose:gc</i> gives, each reported event will be preceeded by the time (in seconds) since the first garbage-collection event.</dl>
<p> Always use a local file system for storage of this file to avoid stalling the JVM due to network latency. The file may be truncated in the case of a full file system and logging will continue on the truncated file. This option overrides <i>-verbose:gc</i> if both are given on the command line. </p>
<dl>
<dt>-Xmsn</p>
<dd>Specify the initial size, in bytes, of the memory allocation pool. This value must be a multiple of 1024 greater than 1MB. Append the letter <i>k</i> or <i>K</i> to indicate kilobytes, or <i>m</i> or <i>M</i> to indicate megabytes. The default value is chosen at runtime based on system configuration. For more information, see HotSpot Ergonomics<br />
 Examples:</p>
<dl>
<dd>
<pre><code> -Xms6291456
 -Xms6144k
 -Xms6m
 </code></pre>
</dl>
<dt>-Xmxn</p>
<dd>Specify the maximum size, in bytes, of the memory allocation pool. This value must a multiple of 1024 greater than 2MB. Append the letter <i>k</i> or <i>K</i> to indicate kilobytes, or <i>m</i> or <i>M</i> to indicate megabytes. The default value is chosen at runtime based on system configuration. For more information, see HotSpot Ergonomics<br />
 Examples:</p>
<dl>
<dd>
<pre><code> -Xmx83886080
 -Xmx81920k
 -Xmx80m
 </code></pre>
</dl>
<p> On Solaris 7 and Solaris 8 SPARC platforms, the upper limit for this value is approximately 4000m minus overhead amounts. On Solaris 2.6 and x86 platforms, the upper limit is approximately 2000m minus overhead amounts. On Linux platforms, the upper limit is approximately 2000m minus overhead amounts.</p>
<dt>-Xprof</p>
<dd>Profiles the running program, and sends profiling data to standard output. This option is provided as a utility that is useful in program development and is not intended to be be used in production systems.</dl>
<dl>
<dt>-Xrs</p>
<dd>Reduces use of operating-system signals by the Java virtual machine (JVM).</dl>
<p> In a previous release, the Shutdown Hooks facility was added to allow orderly shutdown of a Java application. The intent was to allow user cleanup code (such as closing database connections) to run at shutdown, even if the JVM terminates abruptly. </p>
<p> Sun&#8217;s JVM catches signals to implement shutdown hooks for abnormal JVM termination. The JVM uses SIGHUP, SIGINT, and SIGTERM to initiate the running of shutdown hooks. </p>
<p> The JVM uses a similar mechanism to implement the pre-1.2 feature of dumping thread stacks for debugging purposes. Sun&#8217;s JVM uses SIGQUIT to perform thread dumps. </p>
<p> Applications embedding the JVM frequently need to trap signals like SIGINT or SIGTERM, which can lead to interference with the JVM&#8217;s own signal handlers. The <code>-Xrs</code> command-line option is available to address this issue. When <code>-Xrs</code> is used on Sun&#8217;s JVM, the signal masks for SIGINT, SIGTERM, SIGHUP, and SIGQUIT are not changed by the JVM, and signal handlers for these signals are not installed. </p>
<p> There are two consequences of specifying <code>-Xrs</code>:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>SIGQUIT thread dumps are not available.</p>
<dt>o</p>
<dd>User code is responsible for causing shutdown hooks to run, for example by calling System.exit() when the JVM is to be terminated.</dl>
</dl>
<dl>
<dt>-Xssn</p>
<dd>Set thread stack size.</p>
<dt>-XX:+UseAltSigs</p>
<dd>The VM uses <i>SIGUSR1</i> and <i>SIGUSR2</i> by default, which can sometimes conflict with applications that signal-chain <i>SIGUSR1</i> and <i>SIGUSR2</i>. The <i>-XX:+UseAltSigs</i> option will cause the VM to use signals other than <i>SIGUSR1</i> and <i>SIGUSR2</i> as the default.</dl>
</dl>
</dl>
<h2>Notes</h2>
<p>The <code>-version:</code><i>release</i> command line option places no restrictions on the complexity of the release specification. However, only a restricted subset of the possible release specifications represent sound policy and only these are fully supported. These policies are:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Any version, represented by not using this option.</p>
<dt>2.</p>
<dd>Any version greater than an arbitrarily precise version-id. For example: </p>
<pre><code>&quot;1.5.0_03+&quot;</code></pre>
</dl>
<p> Would utilize any version greater than 1.5.0_03. This is useful for a case where an interface was introduced (or a bug fixed) in the release specified.</p>
<dl>
<dt>3.</p>
<dd>A version greater than an arbitrarily precise version-id, bounded by the upper bound of that release family. For example: </p>
<pre><code>&quot;1.5.0_03+&amp;1.5*&quot;</code></pre>
<dt>4.</p>
<dd>&quot;Or&quot; expressions of items 2. or 3. above. For example: </p>
<pre><code>&quot;1.4.2_05+&amp;1.4* 1.5+&quot;</code></pre>
<p>Similar to item 2. this is useful when a change was introduced in a release (1.5) but also made available in updates to previous releases.</dl>
</dl>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>javac &#8211; the Java programming language compiler</p>
<dt>o</p>
<dd>jdb &#8211; Java Application Debugger</p>
<dt>o</p>
<dd>javah &#8211; C Header and Stub File Generator</p>
<dt>o</p>
<dd>jar &#8211; JAR Archive Tool</p>
<dt>o</p>
<dd>The Java Extensions Framework</p>
<dt>o</p>
<dd>Security Features.</p>
<dt>o</p>
<dd><i>HotSpot VM Specific Options</i> @ <a rel="nofollow" href="http://java.sun.com/docs/hotspot/VMOptions.html.">http://java.sun.com/docs/hotspot/VMOptions.html.</a></dl>
</dl>
<p>&nbsp;<wbr></p>
