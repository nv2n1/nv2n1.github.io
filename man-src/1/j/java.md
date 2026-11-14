---
title: "java(1)"
name: "java"
section: "1"
letter: "j"
url: "/docs/linux/man/1-java/"
description: "java – Launches a Java application."
---

<h2 class="name">NAME</h2>
<p> java &#8211; Launches a Java application. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>
<pre><code>
java[options] classname[args]
</code></pre>
</dl>
<dl>
<dt>
<dd>
java[options] &#8211; jar filename[args]
</dl>
<p> <i>options</i></p>
<dl>
<dt>
<dd> Command-line options separated by spaces. See Options.</dl>
<p> <i>classname</i></p>
<dl>
<dt>
<dd> The name of the class to be launched.</dl>
<p> <i>filename</i></p>
<dl>
<dt>
<dd> The name of the Java Archive (JAR) file to be called. Used only with the <code>-jar</code> option.</dl>
<p> <i>args</i></p>
<dl>
<dt>
<dd> The arguments passed to the <code>main()</code> method separated by spaces.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>java</code> command starts a Java application. It does this by starting the Java Runtime Environment (JRE), loading the specified class, and calling that class&#8217;s <code>main()</code> method. The method must be declared <i>public</i> and <i>static</i>, it must not return any value, and it must accept a <code>String</code> array as a parameter. The method declaration has the following form: </p>
<dl>
<dt>
<dd>
<pre><code>
public
static void main(String[] args)
</code></pre>
</dl>
<p> The <code>java</code> command can be used to launch a JavaFX application by loading a class that either has a <code>main()</code> method or that extends <code>javafx.application.Application</code>. In the latter case, the launcher constructs an instance of the <code>Application</code> class, calls its <code>init()</code> method, and then calls the <code>start(javafx.stage.Stage)</code> method. </p>
<p> By default, the first argument that is not an option of the <code>java</code> command is the fully qualified name of the class to be called. If the <code>-jar</code> option is specified, its argument is the name of the JAR file containing class and resource files for the application. The startup class must be indicated by the <code>Main-Class</code> manifest header in its source code. </p>
<p> The JRE searches for the startup class (and other classes used by the application) in three sets of locations: the bootstrap class path, the installed extensions, and the user&#8217;s class path. </p>
<p> Arguments after the class file name or the JAR file name are passed to the <code>main()</code> method.</p>
<h2>OPTIONS</h2>
<p> The <code>java</code> command supports a wide range of options that can be divided into the following categories: </p>
<dl>
<dt>
<dd> &bull; Standard Options</dl>
<dl>
<dt>
<dd> &bull; Non-Standard Options</dl>
<dl>
<dt>
<dd> &bull; Advanced Runtime Options</dl>
<dl>
<dt>
<dd> &bull; Advanced JIT Compiler Options</dl>
<dl>
<dt>
<dd> &bull; Advanced Serviceability Options</dl>
<dl>
<dt>
<dd> &bull; Advanced Garbage Collection Options</dl>
<p> Standard options are guaranteed to be supported by all implementations of the Java Virtual Machine (JVM). They are used for common actions, such as checking the version of the JRE, setting the class path, enabling verbose output, and so on. </p>
<p> Non-standard options are general purpose options that are specific to the Java HotSpot Virtual Machine, so they are not guaranteed to be supported by all JVM implementations, and are subject to change. These options start with <code>-X</code>. </p>
<p> Advanced options are not recommended for casual use. These are developer options used for tuning specific areas of the Java HotSpot Virtual Machine operation that often have specific system requirements and may require privileged access to system configuration parameters. They are also not guaranteed to be supported by all JVM implementations, and are subject to change. Advanced options start with <code>-XX</code>. </p>
<p> To keep track of the options that were deprecated or removed in the latest release, there is a section named Deprecated and Removed Options at the end of the document. </p>
<p> Boolean options are used to either enable a feature that is disabled by default or disable a feature that is enabled by default. Such options do not require a parameter. Boolean <code>-XX</code> options are enabled using the plus sign (<code>-XX:+</code><i>OptionName</i>) and disabled using the minus sign (<code>-XX:-</code><i>OptionName</i>). </p>
<p> For options that require an argument, the argument may be separated from the option name by a space, a colon (:), or an equal sign (=), or the argument may directly follow the option (the exact syntax differs for each option). If you are expected to specify the size in bytes, you can use no suffix, or use the suffix <code>k</code> or <code>K</code> for kilobytes (KB), <code>m</code> or <code>M</code> for megabytes (MB), <code>g</code> or <code>G</code> for gigabytes (GB). For example, to set the size to 8 GB, you can specify either <code>8g</code>, <code>8192m</code>, <code>8388608k</code>, or <code>8589934592</code> as the argument. If you are expected to specify the percentage, use a number from 0 to 1 (for example, specify <code>0.25</code> for 25%).</p>
<h3>Standard Options</h3>
<p> These are the most commonly used options that are supported by all implementations of the JVM. </p>
<p> -agentlib:<i>libname</i>[=<i>options</i>]</p>
<dl>
<dt>
<dd> Loads the specified native agent library. After the library name, a comma-separated list of options specific to the library can be used. </p>
<p> If the option <code>-agentlib:foo</code> is specified, then the JVM attempts to load the library named <code>libfoo.so</code> in the location specified by the <code>LD_LIBRARY_PATH</code> system variable (on OS X this variable is <code>DYLD_LIBRARY_PATH</code>). </p>
<p> The following example shows how to load the heap profiling tool (HPROF) library and get sample CPU information every 20 ms, with a stack depth of 3: </p>
<dl>
<dt>
<dd>
<pre>
<code>-agentlib:hprof=cpu=samples,interval=20,depth=3</code>
 
</pre>
</dl>
<p> The following example shows how to load the Java Debug Wire Protocol (JDWP) library and listen for the socket connection on port 8000, suspending the JVM before the main class loads: </p>
<dl>
<dt>
<dd>
<pre>
<code>-agentlib:jdwp=transport=dt_socket,server=y,address=8000</code>
 
</pre>
</dl>
<p> For more information about the native agent libraries, refer to the following: </p>
<dl>
<dt>
<dd> &bull; The <code>java.lang.instrument</code> package description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html">http://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html</a></dl>
<dl>
<dt>
<dd> &bull; Agent Command Line Options in the JVM Tools Interface guide at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html#starting">http://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html#starting</a></dl>
</dl>
<p> -agentpath:<i>pathname</i>[=<i>options</i>]</p>
<dl>
<dt>
<dd> Loads the native agent library specified by the absolute path name. This option is equivalent to <code>-agentlib</code> but uses the full path and file name of the library.</dl>
<p> -client</p>
<dl>
<dt>
<dd> Selects the Java HotSpot Client VM. The 64-bit version of the Java SE Development Kit (JDK) currently ignores this option and instead uses the Server JVM. </p>
<p> For default JVM selection, see Server-Class Machine Detection at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/vm/server-class.html">http://docs.oracle.com/javase/8/docs/technotes/guides/vm/server-class.html</a></dl>
<p> -D<i>property</i>=<i>value</i></p>
<dl>
<dt>
<dd> Sets a system property value. The <i>property</i> variable is a string with no spaces that represents the name of the property. The <i>value</i> variable is a string that represents the value of the property. If <i>value</i> is a string with spaces, then enclose it in quotation marks (for example <code>-Dfoo=&quot;foo bar&quot;</code>).</dl>
<p> -d32</p>
<dl>
<dt>
<dd> Runs the application in a 32-bit environment. If a 32-bit environment is not installed or is not supported, then an error will be reported. By default, the application is run in a 32-bit environment unless a 64-bit system is used.</dl>
<p> -d64</p>
<dl>
<dt>
<dd> Runs the application in a 64-bit environment. If a 64-bit environment is not installed or is not supported, then an error will be reported. By default, the application is run in a 32-bit environment unless a 64-bit system is used. </p>
<p> Currently only the Java HotSpot Server VM supports 64-bit operation, and the <code>-server</code> option is implicit with the use of <code>-d64</code>. The <code>-client</code> option is ignored with the use of <code>-d64</code>. This is subject to change in a future release.</dl>
<p> -disableassertions[:[<i>packagename</i>]&#8230;|:<i>classname</i>]<br />
 -da[:[<i>packagename</i>]&#8230;|:<i>classname</i>]</p>
<dl>
<dt>
<dd> Disables assertions. By default, assertions are disabled in all packages and classes. </p>
<p> With no arguments, <code>-disableassertions</code> (<code>-da</code>) disables assertions in all packages and classes. With the <i>packagename</i> argument ending in <code>&#8230;</code>, the switch disables assertions in the specified package and any subpackages. If the argument is simply <code>&#8230;</code>, then the switch disables assertions in the unnamed package in the current working directory. With the <i>classname</i> argument, the switch disables assertions in the specified class. </p>
<p> The <code>-disableassertions</code> (<code>-da</code>) option applies to all class loaders and to system classes (which do not have a class loader). There is one exception to this rule: if the option is provided with no arguments, then it does not apply to system classes. This makes it easy to disable assertions in all classes except for system classes. The <code>-disablesystemassertions</code> option enables you to disable assertions in all system classes. </p>
<p> To explicitly enable assertions in specific packages or classes, use the <code>-enableassertions</code> (<code>-ea</code>) option. Both options can be used at the same time. For example, to run the <code>MyClass</code> application with assertions enabled in package <code>com.wombat.fruitbat</code> (and any subpackages) but disabled in class <code>com.wombat.fruitbat.Brickbat</code>, use the following command: </p>
<dl>
<dt>
<dd>
<pre>
<code>java -ea:com.wombat.fruitbat... -da:com.wombat.fruitbat.Brickbat MyClass</code>
 
</pre>
</dl>
</dl>
<p> -disablesystemassertions<br />
 -dsa</p>
<dl>
<dt>
<dd> Disables assertions in all system classes.</dl>
<p> -enableassertions[:[<i>packagename</i>]&#8230;|:<i>classname</i>]<br />
 -ea[:[<i>packagename</i>]&#8230;|:<i>classname</i>]</p>
<dl>
<dt>
<dd> Enables assertions. By default, assertions are disabled in all packages and classes. </p>
<p> With no arguments, <code>-enableassertions</code> (<code>-ea</code>) enables assertions in all packages and classes. With the <i>packagename</i> argument ending in <code>&#8230;</code>, the switch enables assertions in the specified package and any subpackages. If the argument is simply <code>&#8230;</code>, then the switch enables assertions in the unnamed package in the current working directory. With the <i>classname</i> argument, the switch enables assertions in the specified class. </p>
<p> The <code>-enableassertions</code> (<code>-ea</code>) option applies to all class loaders and to system classes (which do not have a class loader). There is one exception to this rule: if the option is provided with no arguments, then it does not apply to system classes. This makes it easy to enable assertions in all classes except for system classes. The <code>-enablesystemassertions</code> option provides a separate switch to enable assertions in all system classes. </p>
<p> To explicitly disable assertions in specific packages or classes, use the <code>-disableassertions</code> (<code>-da</code>) option. If a single command contains multiple instances of these switches, then they are processed in order before loading any classes. For example, to run the <code>MyClass</code> application with assertions enabled only in package <code>com.wombat.fruitbat</code> (and any subpackages) but disabled in class <code>com.wombat.fruitbat.Brickbat</code>, use the following command: </p>
<dl>
<dt>
<dd>
<pre>
<code>java -ea:com.wombat.fruitbat... -da:com.wombat.fruitbat.Brickbat MyClass</code>
 
</pre>
</dl>
</dl>
<p> -enablesystemassertions<br />
 -esa</p>
<dl>
<dt>
<dd> Enables assertions in all system classes.</dl>
<p> -help<br />
 -?</p>
<dl>
<dt>
<dd> Displays usage information for the <code>java</code> command without actually running the JVM.</dl>
<p> -jar <i>filename</i></p>
<dl>
<dt>
<dd> Executes a program encapsulated in a JAR file. The <i>filename</i> argument is the name of a JAR file with a manifest that contains a line in the form <code>Main-Class:</code><i>classname</i> that defines the class with the <code>public static void main(String[] args)</code> method that serves as your application&#8217;s starting point. </p>
<p> When you use the <code>-jar</code> option, the specified JAR file is the source of all user classes, and other class path settings are ignored. </p>
<p> For more information about JAR files, see the following resources: </p>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-jar/">jar</a>(1)</dl>
<dl>
<dt>
<dd> &bull; The Java Archive (JAR) Files guide at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/jar/index.html">http://docs.oracle.com/javase/8/docs/technotes/guides/jar/index.html</a></dl>
<dl>
<dt>
<dd> &bull; Lesson: Packaging Programs in JAR Files at </p>
<p> <a rel="nofollow" href="http://docs.oracle.com/javase/tutorial/deployment/jar/index.html">http://docs.oracle.com/javase/tutorial/deployment/jar/index.html</a></dl>
</dl>
<p> -javaagent:<i>jarpath</i>[=<i>options</i>]</p>
<dl>
<dt>
<dd> Loads the specified Java programming language agent. For more information about instrumenting Java applications, see the <code>java.lang.instrument</code> package description in the Java API documentation at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html">http://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html</a></dl>
<p> -jre-restrict-search</p>
<dl>
<dt>
<dd> Includes user-private JREs in the version search.</dl>
<p> -no-jre-restrict-search</p>
<dl>
<dt>
<dd> Excludes user-private JREs from the version search.</dl>
<p> -server</p>
<dl>
<dt>
<dd> Selects the Java HotSpot Server VM. The 64-bit version of the JDK supports only the Server VM, so in that case the option is implicit. </p>
<p> For default JVM selection, see Server-Class Machine Detection at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/vm/server-class.html">http://docs.oracle.com/javase/8/docs/technotes/guides/vm/server-class.html</a></dl>
<p> -showversion</p>
<dl>
<dt>
<dd> Displays version information and continues execution of the application. This option is equivalent to the <code>-version</code> option except that the latter instructs the JVM to exit after displaying version information.</dl>
<p> -splash:<i>imgname</i></p>
<dl>
<dt>
<dd> Shows the splash screen with the image specified by <i>imgname</i>. For example, to show the <code>splash.gif</code> file from the <code>images</code> directory when starting your application, use the following option: </p>
<dl>
<dt>
<dd>
<pre>
<code>-splash:images/splash.gif</code>
 
</pre>
</dl>
</dl>
<p> -verbose:class</p>
<dl>
<dt>
<dd> Displays information about each loaded class.</dl>
<p> -verbose:gc</p>
<dl>
<dt>
<dd> Displays information about each garbage collection (GC) event.</dl>
<p> -verbose:jni</p>
<dl>
<dt>
<dd> Displays information about the use of native methods and other Java Native Interface (JNI) activity.</dl>
<p> -version</p>
<dl>
<dt>
<dd> Displays version information and then exits. This option is equivalent to the <code>-showversion</code> option except that the latter does not instruct the JVM to exit after displaying version information.</dl>
<p> -version:<i>release</i></p>
<dl>
<dt>
<dd> Specifies the release version to be used for running the application. If the version of the <code>java</code> command called does not meet this specification and an appropriate implementation is found on the system, then the appropriate implementation will be used. </p>
<p> The <i>release</i> argument specifies either the exact version string, or a list of version strings and ranges separated by spaces. A <i>version string</i> is the developer designation of the version number in the following form: <code>1.</code><i>x</i><code>.0_</code><i>u</i> (where <i>x</i> is the major version number, and <i>u</i> is the update version number). A <i>version range</i> is made up of a version string followed by a plus sign (<code>+</code>) to designate this version or later, or a part of a version string followed by an asterisk (<code>*</code>) to designate any version string with a matching prefix. Version strings and ranges can be combined using a space for a logical <i>OR</i> combination, or an ampersand (<code>&amp;</code>) for a logical <i>AND</i> combination of two version strings/ranges. For example, if running the class or JAR file requires either JRE 6u13 (1.6.0_13), or any JRE 6 starting from 6u10 (1.6.0_10), specify the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>-version:&quot;1.6.0_13 1.6* &amp; 1.6.0_10+&quot;</code>
 
</pre>
</dl>
<p> Quotation marks are necessary only if there are spaces in the <i>release</i> parameter. </p>
<p> For JAR files, the preference is to specify version requirements in the JAR file manifest rather than on the command line.</dl>
<h3>Non-Standard Options</h3>
<p> These options are general purpose options that are specific to the Java HotSpot Virtual Machine. </p>
<p> -X</p>
<dl>
<dt>
<dd> Displays help for all available <code>-X</code> options.</dl>
<p> -Xbatch</p>
<dl>
<dt>
<dd> Disables background compilation. By default, the JVM compiles the method as a background task, running the method in interpreter mode until the background compilation is finished. The <code>-Xbatch</code> flag disables background compilation so that compilation of all methods proceeds as a foreground task until completed. </p>
<p> This option is equivalent to <code>-XX:-BackgroundCompilation</code>.</dl>
<p> -Xbootclasspath:<i>path</i></p>
<dl>
<dt>
<dd> Specifies a list of directories, JAR files, and ZIP archives separated by colons (:) to search for boot class files. These are used in place of the boot class files included in the JDK. </p>
<p> Do not deploy applications that use this option to override a class in <code>rt.jar</code>, because this violates the JRE binary code license.</dl>
<p> -Xbootclasspath/a:<i>path</i></p>
<dl>
<dt>
<dd> Specifies a list of directories, JAR files, and ZIP archives separated by colons (:) to append to the end of the default bootstrap class path. </p>
<p> Do not deploy applications that use this option to override a class in <code>rt.jar</code>, because this violates the JRE binary code license.</dl>
<p> -Xbootclasspath/p:<i>path</i></p>
<dl>
<dt>
<dd> Specifies a list of directories, JAR files, and ZIP archives separated by colons (:) to prepend to the front of the default bootstrap class path. </p>
<p> Do not deploy applications that use this option to override a class in <code>rt.jar</code>, because this violates the JRE binary code license.</dl>
<p> -Xcheck:jni</p>
<dl>
<dt>
<dd> Performs additional checks for Java Native Interface (JNI) functions. Specifically, it validates the parameters passed to the JNI function and the runtime environment data before processing the JNI request. Any invalid data encountered indicates a problem in the native code, and the JVM will terminate with an irrecoverable error in such cases. Expect a performance degradation when this option is used.</dl>
<p> -Xcomp</p>
<dl>
<dt>
<dd> Forces compilation of methods on first invocation. By default, the Client VM (<code>-client</code>) performs 1,000 interpreted method invocations and the Server VM (<code>-server</code>) performs 10,000 interpreted method invocations to gather information for efficient compilation. Specifying the <code>-Xcomp</code> option disables interpreted method invocations to increase compilation performance at the expense of efficiency. </p>
<p> You can also change the number of interpreted method invocations before compilation using the <code>-XX:CompileThreshold</code> option.</dl>
<p> -Xdebug</p>
<dl>
<dt>
<dd> Does nothing. Provided for backward compatibility.</dl>
<p> -Xdiag</p>
<dl>
<dt>
<dd> Shows additional diagnostic messages.</dl>
<p> -Xfuture</p>
<dl>
<dt>
<dd> Enables strict class-file format checks that enforce close conformance to the class-file format specification. Developers are encouraged to use this flag when developing new code because the stricter checks will become the default in future releases.</dl>
<p> -Xint</p>
<dl>
<dt>
<dd> Runs the application in interpreted-only mode. Compilation to native code is disabled, and all bytecode is executed by the interpreter. The performance benefits offered by the just in time (JIT) compiler are not present in this mode.</dl>
<p> -Xinternalversion</p>
<dl>
<dt>
<dd> Displays more detailed JVM version information than the <code>-version</code> option, and then exits.</dl>
<p> -Xloggc:<i>filename</i></p>
<dl>
<dt>
<dd> Sets the file to which verbose GC events information should be redirected for logging. The information written to this file is similar to the output of <code>-verbose:gc</code> with the time elapsed since the first GC event preceding each logged event. The <code>-Xloggc</code> option overrides <code>-verbose:gc</code> if both are given with the same <code>java</code> command. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>-Xloggc:garbage-collection.log</code>
 
</pre>
</dl>
</dl>
<p> -Xmaxjitcodesize=<i>size</i></p>
<dl>
<dt>
<dd> Specifies the maximum code cache size (in bytes) for JIT-compiled code. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default maximum code cache size is 240 MB; if you disable tiered compilation with the option <code>-XX:-TieredCompilation</code>, then the default size is 48 MB: </p>
<dl>
<dt>
<dd>
<pre>
<code>-Xmaxjitcodesize=240m</code>
 
</pre>
</dl>
<p> This option is equivalent to <code>-XX:ReservedCodeCacheSize</code>.</dl>
<p> -Xmixed</p>
<dl>
<dt>
<dd> Executes all bytecode by the interpreter except for hot methods, which are compiled to native code.</dl>
<p> -Xmn<i>size</i></p>
<dl>
<dt>
<dd> Sets the initial and maximum size (in bytes) of the heap for the young generation (nursery). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. </p>
<p> The young generation region of the heap is used for new objects. GC is performed in this region more often than in other regions. If the size for the young generation is too small, then a lot of minor garbage collections will be performed. If the size is too large, then only full garbage collections will be performed, which can take a long time to complete. Oracle recommends that you keep the size for the young generation between a half and a quarter of the overall heap size. </p>
<p> The following examples show how to set the initial and maximum size of young generation to 256 MB using various units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-Xmn256m</code>
<code>-Xmn262144k</code>
<code>-Xmn268435456</code>
 
</pre>
</dl>
<p> Instead of the <code>-Xmn</code> option to set both the initial and maximum size of the heap for the young generation, you can use <code>-XX:NewSize</code> to set the initial size and <code>-XX:MaxNewSize</code> to set the maximum size.</dl>
<p> -Xms<i>size</i></p>
<dl>
<dt>
<dd> Sets the initial size (in bytes) of the heap. This value must be a multiple of 1024 and greater than 1 MB. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. </p>
<p> The following examples show how to set the size of allocated memory to 6 MB using various units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-Xms6291456</code>
<code>-Xms6144k</code>
<code>-Xms6m</code>
 
</pre>
</dl>
<p> If you do not set this option, then the initial size will be set as the sum of the sizes allocated for the old generation and the young generation. The initial size of the heap for the young generation can be set using the <code>-Xmn</code> option or the <code>-XX:NewSize</code> option.</dl>
<p> -Xmx<i>size</i></p>
<dl>
<dt>
<dd> Specifies the maximum size (in bytes) of the memory allocation pool in bytes. This value must be a multiple of 1024 and greater than 2 MB. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default value is chosen at runtime based on system configuration. For server deployments, <code>-Xms</code> and <code>-Xmx</code> are often set to the same value. See the section &quot;Ergonomics&quot; in <i>Java SE HotSpot Virtual Machine Garbage Collection Tuning Guide</i> at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/index.html.">http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/index.html.</a> </p>
<p> The following examples show how to set the maximum allowed size of allocated memory to 80 MB using various units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-Xmx83886080</code>
<code>-Xmx81920k</code>
<code>-Xmx80m</code>
 
</pre>
</dl>
<p> The <code>-Xmx</code> option is equivalent to <code>-XX:MaxHeapSize</code>.</dl>
<p> -Xnoclassgc</p>
<dl>
<dt>
<dd> Disables garbage collection (GC) of classes. This can save some GC time, which shortens interruptions during the application run. </p>
<p> When you specify <code>-Xnoclassgc</code> at startup, the class objects in the application will be left untouched during GC and will always be considered live. This can result in more memory being permanently occupied which, if not used carefully, will throw an out of memory exception.</dl>
<p> -Xrs</p>
<dl>
<dt>
<dd> Reduces the use of operating system signals by the JVM. </p>
<p> Shutdown hooks enable orderly shutdown of a Java application by running user cleanup code (such as closing database connections) at shutdown, even if the JVM terminates abruptly. </p>
<p> The JVM catches signals to implement shutdown hooks for unexpected termination. The JVM uses <code>SIGHUP</code>, <code>SIGINT</code>, and <code>SIGTERM</code> to initiate the running of shutdown hooks. </p>
<p> The JVM uses a similar mechanism to implement the feature of dumping thread stacks for debugging purposes. The JVM uses <code>SIGQUIT</code> to perform thread dumps. </p>
<p> Applications embedding the JVM frequently need to trap signals such as <code>SIGINT</code> or <code>SIGTERM</code>, which can lead to interference with the JVM signal handlers. The <code>-Xrs</code> option is available to address this issue. When <code>-Xrs</code> is used, the signal masks for <code>SIGINT</code>, <code>SIGTERM</code>, <code>SIGHUP</code>, and <code>SIGQUIT</code> are not changed by the JVM, and signal handlers for these signals are not installed. </p>
<p> There are two consequences of specifying <code>-Xrs</code>: </p>
<dl>
<dt>
<dd> &bull; <code>SIGQUIT</code> thread dumps are not available.</dl>
<dl>
<dt>
<dd> &bull; User code is responsible for causing shutdown hooks to run, for example, by calling <code>System.exit()</code> when the JVM is to be terminated.</dl>
</dl>
<p> -Xshare:<i>mode</i></p>
<dl>
<dt>
<dd> Sets the class data sharing (CDS) mode. Possible <i>mode</i> arguments for this option include the following: </p>
<p> auto</p>
<dl>
<dt>
<dd> Use CDS if possible. This is the default value for Java HotSpot 32-Bit Client VM.</dl>
<p> on</p>
<dl>
<dt>
<dd> Require the use of CDS. Print an error message and exit if class data sharing cannot be used.</dl>
<p> off</p>
<dl>
<dt>
<dd> Do not use CDS. This is the default value for Java HotSpot 32-Bit Server VM, Java HotSpot 64-Bit Client VM, and Java HotSpot 64-Bit Server VM.</dl>
<p> dump</p>
<dl>
<dt>
<dd> Manually generate the CDS archive. Specify the application class path as described in &quot;Setting the Class Path &quot;. </p>
<p> You should regenerate the CDS archive with each new JDK release.</dl>
</dl>
<p> -XshowSettings:<i>category</i></p>
<dl>
<dt>
<dd> Shows settings and continues. Possible <i>category</i> arguments for this option include the following: </p>
<p> all</p>
<dl>
<dt>
<dd> Shows all categories of settings. This is the default value.</dl>
<p> locale</p>
<dl>
<dt>
<dd> Shows settings related to locale.</dl>
<p> properties</p>
<dl>
<dt>
<dd> Shows settings related to system properties.</dl>
<p> vm</p>
<dl>
<dt>
<dd> Shows the settings of the JVM.</dl>
</dl>
<p> -Xss<i>size</i></p>
<dl>
<dt>
<dd> Sets the thread stack size (in bytes). Append the letter <code>k</code> or <code>K</code> to indicate KB, <code>m</code> or <code>M</code> to indicate MB, <code>g</code> or <code>G</code> to indicate GB. The default value depends on the platform: </p>
<dl>
<dt>
<dd> &bull; Linux/ARM (32-bit): 320 KB</dl>
<dl>
<dt>
<dd> &bull; Linux/i386 (32-bit): 320 KB</dl>
<dl>
<dt>
<dd> &bull; Linux/x64 (64-bit): 1024 KB</dl>
<dl>
<dt>
<dd> &bull; OS X (64-bit): 1024 KB</dl>
<dl>
<dt>
<dd> &bull; Oracle Solaris/i386 (32-bit): 320 KB</dl>
<dl>
<dt>
<dd> &bull; Oracle Solaris/x64 (64-bit): 1024 KB</dl>
<p> The following examples set the thread stack size to 1024 KB in different units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-Xss1m</code>
<code>-Xss1024k</code>
<code>-Xss1048576</code>
 
</pre>
</dl>
<p> This option is equivalent to <code>-XX:ThreadStackSize</code>.</dl>
<p> -Xusealtsigs</p>
<dl>
<dt>
<dd> Use alternative signals instead of <code>SIGUSR1</code> and <code>SIGUSR2</code> for JVM internal signals. This option is equivalent to <code>-XX:+UseAltSigs</code>.</dl>
<p> -Xverify:<i>mode</i></p>
<dl>
<dt>
<dd> Sets the mode of the bytecode verifier. Bytecode verification helps to troubleshoot some problems, but it also adds overhead to the running application. Possible <i>mode</i> arguments for this option include the following: </p>
<p> none</p>
<dl>
<dt>
<dd> Do not verify the bytecode. This reduces startup time and also reduces the protection provided by Java.</dl>
<p> remote</p>
<dl>
<dt>
<dd> Verify those classes that are not loaded by the bootstrap class loader. This is the default behavior if you do not specify the <code>-Xverify</code> option.</dl>
<p> all</p>
<dl>
<dt>
<dd> Verify all classes.</dl>
</dl>
<h3>Advanced Runtime Options</h3>
<p> These options control the runtime behavior of the Java HotSpot VM. </p>
<p> -XX:+DisableAttachMechanism</p>
<dl>
<dt>
<dd> Enables the option that disables the mechanism that lets tools attach to the JVM. By default, this option is disabled, meaning that the attach mechanism is enabled and you can use tools such as <code>jcmd</code>, <code>jstack</code>, <code>jmap</code>, and <code>jinfo</code>.</dl>
<p> -XX:ErrorFile=<i>filename</i></p>
<dl>
<dt>
<dd> Specifies the path and file name to which error data is written when an irrecoverable error occurs. By default, this file is created in the current working directory and named <code>hs_err_pid</code><i>pid</i><code>.log</code> where <i>pid</i> is the identifier of the process that caused the error. The following example shows how to set the default log file (note that the identifier of the process is specified as <code>%p</code>): </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:ErrorFile=./hs_err_pid%p.log</code>
 
</pre>
</dl>
<p> The following example shows how to set the error log to <code>/var/log/java/java_error.log</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:ErrorFile=/var/log/java/java_error.log</code>
 
</pre>
</dl>
<p> If the file cannot be created in the specified directory (due to insufficient space, permission problem, or another issue), then the file is created in the temporary directory for the operating system. The temporary directory is <code>/tmp</code>.</dl>
<p> -XX:+FailOverToOldVerifier</p>
<dl>
<dt>
<dd> Enables automatic failover to the old verifier when the new type checker fails. By default, this option is disabled and it is ignored (that is, treated as disabled) for classes with a recent bytecode version. You can enable it for classes with older versions of the bytecode.</dl>
<p> -XX:LargePageSizeInBytes=<i>size</i></p>
<dl>
<dt>
<dd> On Solaris, sets the maximum size (in bytes) for large pages used for Java heap. The <i>size</i> argument must be a power of 2 (2, 4, 8, 16, &#8230;). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. By default, the size is set to 0, meaning that the JVM chooses the size for large pages automatically. </p>
<p> The following example illustrates how to set the large page size to 4 megabytes (MB): </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:LargePageSizeInBytes=4m</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxDirectMemorySize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum total size (in bytes) of the New I/O (the <code>java.nio</code> package) direct-buffer allocations. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. By default, the size is set to 0, meaning that the JVM chooses the size for NIO direct-buffer allocations automatically. </p>
<p> The following examples illustrate how to set the NIO size to 1024 KB in different units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxDirectMemorySize=1m</code>
<code>-XX:MaxDirectMemorySize=1024k</code>
<code>-XX:MaxDirectMemorySize=1048576</code>
 
</pre>
</dl>
</dl>
<p> -XX:NativeMemoryTracking=<i>mode</i></p>
<dl>
<dt>
<dd> Specifies the mode for tracking JVM native memory usage. Possible <i>mode</i> arguments for this option include the following: </p>
<p> off</p>
<dl>
<dt>
<dd> Do not track JVM native memory usage. This is the default behavior if you do not specify the <code>-XX:NativeMemoryTracking</code> option.</dl>
<p> summary</p>
<dl>
<dt>
<dd> Only track memory usage by JVM subsystems, such as Java heap, class, code, and thread.</dl>
<p> detail</p>
<dl>
<dt>
<dd> In addition to tracking memory usage by JVM subsystems, track memory usage by individual <code>CallSite</code>, individual virtual memory region and its committed regions.</dl>
</dl>
<p> -XX:ObjectAlignmentInBytes=<i>alignment</i></p>
<dl>
<dt>
<dd> Sets the memory alignment of Java objects (in bytes). By default, the value is set to 8 bytes. The specified value should be a power of two, and must be within the range of 8 and 256 (inclusive). This option makes it possible to use compressed pointers with large Java heap sizes. </p>
<p> The heap size limit in bytes is calculated as: </p>
<p> <code>4GB * ObjectAlignmentInBytes</code> </p>
<p> Note: As the alignment value increases, the unused space between objects will also increase. As a result, you may not realize any benefits from using compressed pointers with large Java heap sizes.</dl>
<p> -XX:OnError=<i>string</i></p>
<dl>
<dt>
<dd> Sets a custom command or a series of semicolon-separated commands to run when an irrecoverable error occurs. If the string contains spaces, then it must be enclosed in quotation marks. </p>
<p> The following example shows how the <code>-XX:OnError</code> option can be used to run the <code>gcore</code> command to create the core image, and the debugger is started to attach to the process in case of an irrecoverable error (the <code>%p</code> designates the current process): </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:OnError=&quot;gcore %p;dbx - %p&quot;</code>
 
</pre>
</dl>
</dl>
<p> -XX:OnOutOfMemoryError=<i>string</i></p>
<dl>
<dt>
<dd> Sets a custom command or a series of semicolon-separated commands to run when an <code>OutOfMemoryError</code> exception is first thrown. If the string contains spaces, then it must be enclosed in quotation marks. For an example of a command string, see the description of the <code>-XX:OnError</code> option.</dl>
<p> -XX:+PerfDataSaveToFile</p>
<dl>
<dt>
<dd> If enabled, saves <a href="/docs/linux/man/1-jstat/">jstat</a>(1) binary data when the Java application exits. This binary data is saved in a file named <code>hsperfdata_</code><i>&lt;pid&gt;</i>, where <i>&lt;pid&gt;</i> is the process identifier of the Java application you ran. Use <code>jstat</code> to display the performance data contained in this file as follows: </p>
<dl>
<dt>
<dd>
<pre>
<code>jstat -class file:///</code><i>&lt;path&gt;</i><code>/hsperfdata_</code><i>&lt;pid&gt;</i>
<code>jstat -gc file:///</code><i>&lt;path&gt;</i><code>/hsperfdata_</code><i>&lt;pid&gt;</i>
</pre>
</dl>
</dl>
<p> -XX:+PrintCommandLineFlags</p>
<dl>
<dt>
<dd> Enables printing of ergonomically selected JVM flags that appeared on the command line. It can be useful to know the ergonomic values set by the JVM, such as the heap space size and the selected garbage collector. By default, this option is disabled and flags are not printed.</dl>
<p> -XX:+PrintNMTStatistics</p>
<dl>
<dt>
<dd> Enables printing of collected native memory tracking data at JVM exit when native memory tracking is enabled (see <code>-XX:NativeMemoryTracking</code>). By default, this option is disabled and native memory tracking data is not printed.</dl>
<p> -XX:+RelaxAccessControlCheck</p>
<dl>
<dt>
<dd> Decreases the amount of access control checks in the verifier. By default, this option is disabled, and it is ignored (that is, treated as disabled) for classes with a recent bytecode version. You can enable it for classes with older versions of the bytecode.</dl>
<p> -XX:+ShowMessageBoxOnError</p>
<dl>
<dt>
<dd> Enables displaying of a dialog box when the JVM experiences an irrecoverable error. This prevents the JVM from exiting and keeps the process active so that you can attach a debugger to it to investigate the cause of the error. By default, this option is disabled.</dl>
<p> -XX:ThreadStackSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the thread stack size (in bytes). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default value depends on the platform: </p>
<dl>
<dt>
<dd> &bull; Linux/ARM (32-bit): 320 KB</dl>
<dl>
<dt>
<dd> &bull; Linux/i386 (32-bit): 320 KB</dl>
<dl>
<dt>
<dd> &bull; Linux/x64 (64-bit): 1024 KB</dl>
<dl>
<dt>
<dd> &bull; OS X (64-bit): 1024 KB</dl>
<dl>
<dt>
<dd> &bull; Oracle Solaris/i386 (32-bit): 320 KB</dl>
<dl>
<dt>
<dd> &bull; Oracle Solaris/x64 (64-bit): 1024 KB</dl>
<p> The following examples show how to set the thread stack size to 1024 KB in different units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:ThreadStackSize=1m</code>
<code>-XX:ThreadStackSize=1024k</code>
<code>-XX:ThreadStackSize=1048576</code>
 
</pre>
</dl>
<p> This option is equivalent to <code>-Xss</code>.</dl>
<p> -XX:+TraceClassLoading</p>
<dl>
<dt>
<dd> Enables tracing of classes as they are loaded. By default, this option is disabled and classes are not traced.</dl>
<p> -XX:+TraceClassLoadingPreorder</p>
<dl>
<dt>
<dd> Enables tracing of all loaded classes in the order in which they are referenced. By default, this option is disabled and classes are not traced.</dl>
<p> -XX:+TraceClassResolution</p>
<dl>
<dt>
<dd> Enables tracing of constant pool resolutions. By default, this option is disabled and constant pool resolutions are not traced.</dl>
<p> -XX:+TraceClassUnloading</p>
<dl>
<dt>
<dd> Enables tracing of classes as they are unloaded. By default, this option is disabled and classes are not traced.</dl>
<p> -XX:+TraceLoaderConstraints</p>
<dl>
<dt>
<dd> Enables tracing of the loader constraints recording. By default, this option is disabled and loader constraints recording is not traced.</dl>
<p> -XX:+UseAltSigs</p>
<dl>
<dt>
<dd> Enables the use of alternative signals instead of <code>SIGUSR1</code> and <code>SIGUSR2</code> for JVM internal signals. By default, this option is disabled and alternative signals are not used. This option is equivalent to <code>-Xusealtsigs</code>.</dl>
<p> -XX:-UseBiasedLocking</p>
<dl>
<dt>
<dd> Disables the use of biased locking. Some applications with significant amounts of uncontended synchronization may attain significant speedups with this flag enabled, whereas applications with certain patterns of locking may see slowdowns. For more information about the biased locking technique, see the example in Java Tuning White Paper at <a rel="nofollow" href="http://www.oracle.com/technetwork/java/tuning-139912.html#section4.2.5">http://www.oracle.com/technetwork/java/tuning-139912.html#section4.2.5</a> </p>
<p> By default, this option is enabled.</dl>
<p> -XX:-UseCompressedOops</p>
<dl>
<dt>
<dd> Disables the use of compressed pointers. By default, this option is enabled, and compressed pointers are used when Java heap sizes are less than 32 GB. When this option is enabled, object references are represented as 32-bit offsets instead of 64-bit pointers, which typically increases performance when running the application with Java heap sizes less than 32 GB. This option works only for 64-bit JVMs. </p>
<p> It is also possible to use compressed pointers when Java heap sizes are greater than 32GB. See the <code>-XX:ObjectAlignmentInBytes</code> option.</dl>
<p> -XX:+UseHugeTLBFS</p>
<dl>
<dt>
<dd> This option for Linux is the equivalent of specifying <code>-XX:+UseLargePages</code>. This option is disabled by default. This option pre-allocates all large pages up-front, when memory is reserved; consequently the JVM cannot dynamically grow or shrink large pages memory areas; see <code>-XX:UseTransparentHugePages</code> if you want this behavior. </p>
<p> For more information, see &quot;Large Pages&quot;.</dl>
<p> -XX:+UseLargePages</p>
<dl>
<dt>
<dd> Enables the use of large page memory. By default, this option is disabled and large page memory is not used. </p>
<p> For more information, see &quot;Large Pages&quot;.</dl>
<p> -XX:+UseMembar</p>
<dl>
<dt>
<dd> Enables issuing of membars on thread state transitions. This option is disabled by default on all platforms except ARM servers, where it is enabled. (It is recommended that you do not disable this option on ARM servers.)</dl>
<p> -XX:+UsePerfData</p>
<dl>
<dt>
<dd> Enables the <code>perfdata</code> feature. This option is enabled by default to allow JVM monitoring and performance testing. Disabling it suppresses the creation of the <code>hsperfdata_userid</code> directories. To disable the <code>perfdata</code> feature, specify <code>-XX:-UsePerfData</code>.</dl>
<p> -XX:+UseTransparentHugePages</p>
<dl>
<dt>
<dd> On Linux, enables the use of large pages that can dynamically grow or shrink. This option is disabled by default. You may encounter performance problems with transparent huge pages as the OS moves other pages around to create huge pages; this option is made available for experimentation. </p>
<p> For more information, see &quot;Large Pages&quot;.</dl>
<p> -XX:+AllowUserSignalHandlers</p>
<dl>
<dt>
<dd> Enables installation of signal handlers by the application. By default, this option is disabled and the application is not allowed to install signal handlers.</dl>
<h3>Advanced JIT Compiler Options</h3>
<p> These options control the dynamic just-in-time (JIT) compilation performed by the Java HotSpot VM. </p>
<p> -XX:+AggressiveOpts</p>
<dl>
<dt>
<dd> Enables the use of aggressive performance optimization features, which are expected to become default in upcoming releases. By default, this option is disabled and experimental performance features are not used.</dl>
<p> -XX:AllocateInstancePrefetchLines=<i>lines</i></p>
<dl>
<dt>
<dd> Sets the number of lines to prefetch ahead of the instance allocation pointer. By default, the number of lines to prefetch is set to 1: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:AllocateInstancePrefetchLines=1</code>
 
</pre>
</dl>
<p> Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:AllocatePrefetchDistance=<i>size</i></p>
<dl>
<dt>
<dd> Sets the size (in bytes) of the prefetch distance for object allocation. Memory about to be written with the value of new objects is prefetched up to this distance starting from the address of the last allocated object. Each Java thread has its own allocation point. </p>
<p> Negative values denote that prefetch distance is chosen based on the platform. Positive values are bytes to prefetch. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default value is set to -1. </p>
<p> The following example shows how to set the prefetch distance to 1024 bytes: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:AllocatePrefetchDistance=1024</code>
 
</pre>
</dl>
<p> Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:AllocatePrefetchInstr=<i>instruction</i></p>
<dl>
<dt>
<dd> Sets the prefetch instruction to prefetch ahead of the allocation pointer. Only the Java HotSpot Server VM supports this option. Possible values are from 0 to 3. The actual instructions behind the values depend on the platform. By default, the prefetch instruction is set to 0: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:AllocatePrefetchInstr=0</code>
 
</pre>
</dl>
<p> Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:AllocatePrefetchLines=<i>lines</i></p>
<dl>
<dt>
<dd> Sets the number of cache lines to load after the last object allocation by using the prefetch instructions generated in compiled code. The default value is 1 if the last allocated object was an instance, and 3 if it was an array. </p>
<p> The following example shows how to set the number of loaded cache lines to 5: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:AllocatePrefetchLines=5</code>
 
</pre>
</dl>
<p> Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:AllocatePrefetchStepSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the step size (in bytes) for sequential prefetch instructions. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. By default, the step size is set to 16 bytes: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:AllocatePrefetchStepSize=16</code>
 
</pre>
</dl>
<p> Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:AllocatePrefetchStyle=<i>style</i></p>
<dl>
<dt>
<dd> Sets the generated code style for prefetch instructions. The <i>style</i> argument is an integer from 0 to 3: </p>
<p> 0</p>
<dl>
<dt>
<dd> Do not generate prefetch instructions.</dl>
<p> 1</p>
<dl>
<dt>
<dd> Execute prefetch instructions after each allocation. This is the default parameter.</dl>
<p> 2</p>
<dl>
<dt>
<dd> Use the thread-local allocation block (TLAB) watermark pointer to determine when prefetch instructions are executed.</dl>
<p> 3</p>
<dl>
<dt>
<dd> Use BIS instruction on SPARC for allocation prefetch.</dl>
<p> Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:+BackgroundCompilation</p>
<dl>
<dt>
<dd> Enables background compilation. This option is enabled by default. To disable background compilation, specify <code>-XX:-BackgroundCompilation</code> (this is equivalent to specifying <code>-Xbatch</code>).</dl>
<p> -XX:CICompilerCount=<i>threads</i></p>
<dl>
<dt>
<dd> Sets the number of compiler threads to use for compilation. By default, the number of threads is set to 2 for the server JVM, to 1 for the client JVM, and it scales to the number of cores if tiered compilation is used. The following example shows how to set the number of threads to 2: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CICompilerCount=2</code>
 
</pre>
</dl>
</dl>
<p> -XX:CodeCacheMinimumFreeSpace=<i>size</i></p>
<dl>
<dt>
<dd> Sets the minimum free space (in bytes) required for compilation. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. When less than the minimum free space remains, compiling stops. By default, this option is set to 500 KB. The following example shows how to set the minimum free space to 1024 MB: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CodeCacheMinimumFreeSpace=1024m</code>
 
</pre>
</dl>
</dl>
<p> -XX:CompileCommand=<i>command</i>,<i>method</i>[,<i>option</i>]</p>
<dl>
<dt>
<dd> Specifies a command to perform on a method. For example, to exclude the <code>indexOf()</code> method of the <code>String</code> class from being compiled, use the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileCommand=exclude,java/lang/String.indexOf</code>
 
</pre>
</dl>
<p> Note that the full class name is specified, including all packages and subpackages separated by a slash (<code>/</code>). For easier cut and paste operations, it is also possible to use the method name format produced by the <code>-XX:+PrintCompilation</code> and <code>-XX:+LogCompilation</code> options: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileCommand=exclude,java.lang.String::indexOf</code>
 
</pre>
</dl>
<p> If the method is specified without the signature, the command will be applied to all methods with the specified name. However, you can also specify the signature of the method in the class file format. In this case, you should enclose the arguments in quotation marks, because otherwise the shell treats the semicolon as command end. For example, if you want to exclude only the <code>indexOf(String)</code> method of the <code>String</code> class from being compiled, use the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileCommand=&quot;exclude,java/lang/String.indexOf,(Ljava/lang/String;)I&quot;</code>
 
</pre>
</dl>
<p> You can also use the asterisk (*) as a wildcard for class and method names. For example, to exclude all <code>indexOf()</code> methods in all classes from being compiled, use the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileCommand=exclude,*.indexOf</code>
 
</pre>
</dl>
<p> The commas and periods are aliases for spaces, making it easier to pass compiler commands through a shell. You can pass arguments to <code>-XX:CompileCommand</code> using spaces as separators by enclosing the argument in quotation marks: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileCommand=&quot;exclude java/lang/String indexOf&quot;</code>
 
</pre>
</dl>
<p> Note that after parsing the commands passed on the command line using the <code>-XX:CompileCommand</code> options, the JIT compiler then reads commands from the <code>.hotspot_compiler</code> file. You can add commands to this file or specify a different file using the <code>-XX:CompileCommandFile</code> option. </p>
<p> To add several commands, either specify the <code>-XX:CompileCommand</code> option multiple times, or separate each argument with the newline separator (<code>
</code>). The following commands are available: </p>
<p> break</p>
<dl>
<dt>
<dd> Set a breakpoint when debugging the JVM to stop at the beginning of compilation of the specified method.</dl>
<p> compileonly</p>
<dl>
<dt>
<dd> Exclude all methods from compilation except for the specified method. As an alternative, you can use the <code>-XX:CompileOnly</code> option, which allows to specify several methods.</dl>
<p> dontinline</p>
<dl>
<dt>
<dd> Prevent inlining of the specified method.</dl>
<p> exclude</p>
<dl>
<dt>
<dd> Exclude the specified method from compilation.</dl>
<p> help</p>
<dl>
<dt>
<dd> Print a help message for the <code>-XX:CompileCommand</code> option.</dl>
<p> inline</p>
<dl>
<dt>
<dd> Attempt to inline the specified method.</dl>
<p> log</p>
<dl>
<dt>
<dd> Exclude compilation logging (with the <code>-XX:+LogCompilation</code> option) for all methods except for the specified method. By default, logging is performed for all compiled methods.</dl>
<p> option</p>
<dl>
<dt>
<dd> This command can be used to pass a JIT compilation option to the specified method in place of the last argument (<i>option</i>). The compilation option is set at the end, after the method name. For example, to enable the <code>BlockLayoutByFrequency</code> option for the <code>append()</code> method of the <code>StringBuffer</code> class, use the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileCommand=option,java/lang/StringBuffer.append,BlockLayoutByFrequency</code>
 
</pre>
</dl>
<p> You can specify multiple compilation options, separated by commas or spaces.</dl>
<p> print</p>
<dl>
<dt>
<dd> Print generated assembler code after compilation of the specified method.</dl>
<p> quiet</p>
<dl>
<dt>
<dd> Do not print the compile commands. By default, the commands that you specify with the &#8211;<code>XX:CompileCommand</code> option are printed; for example, if you exclude from compilation the <code>indexOf()</code> method of the <code>String</code> class, then the following will be printed to standard output: </p>
<dl>
<dt>
<dd>
<pre>
<code>CompilerOracle: exclude java/lang/String.indexOf</code>
 
</pre>
</dl>
<p> You can suppress this by specifying the <code>-XX:CompileCommand=quiet</code> option before other <code>-XX:CompileCommand</code> options.</dl>
</dl>
<p> -XX:CompileCommandFile=<i>filename</i></p>
<dl>
<dt>
<dd> Sets the file from which JIT compiler commands are read. By default, the <code>.hotspot_compiler</code> file is used to store commands performed by the JIT compiler. </p>
<p> Each line in the command file represents a command, a class name, and a method name for which the command is used. For example, this line prints assembly code for the <code>toString()</code> method of the <code>String</code> class: </p>
<dl>
<dt>
<dd>
<pre>
<code>print java/lang/String toString</code>
 
</pre>
</dl>
<p> For more information about specifying the commands for the JIT compiler to perform on methods, see the <code>-XX:CompileCommand</code> option.</dl>
<p> -XX:CompileOnly=<i>methods</i></p>
<dl>
<dt>
<dd> Sets the list of methods (separated by commas) to which compilation should be restricted. Only the specified methods will be compiled. Specify each method with the full class name (including the packages and subpackages). For example, to compile only the <code>length()</code> method of the <code>String</code> class and the <code>size()</code> method of the <code>List</code> class, use the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileOnly=java/lang/String.length,java/util/List.size</code>
 
</pre>
</dl>
<p> Note that the full class name is specified, including all packages and subpackages separated by a slash (<code>/</code>). For easier cut and paste operations, it is also possible to use the method name format produced by the <code>-XX:+PrintCompilation</code> and <code>-XX:+LogCompilation</code> options: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileOnly=java.lang.String::length,java.util.List::size</code>
 
</pre>
</dl>
<p> Although wildcards are not supported, you can specify only the class or package name to compile all methods in that class or package, as well as specify just the method to compile methods with this name in any class: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileOnly=java/lang/String</code>
<code>-XX:CompileOnly=java/lang</code>
<code>-XX:CompileOnly=.length</code>
 
</pre>
</dl>
</dl>
<p> -XX:CompileThreshold=<i>invocations</i></p>
<dl>
<dt>
<dd> Sets the number of interpreted method invocations before compilation. By default, in the server JVM, the JIT compiler performs 10,000 interpreted method invocations to gather information for efficient compilation. For the client JVM, the default setting is 1,500 invocations. This option is ignored when tiered compilation is enabled; see the option <code>-XX:+TieredCompilation</code>. The following example shows how to set the number of interpreted method invocations to 5,000: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CompileThreshold=5000</code>
 
</pre>
</dl>
<p> You can completely disable interpretation of Java methods before compilation by specifying the <code>-Xcomp</code> option.</dl>
<p> -XX:+DoEscapeAnalysis</p>
<dl>
<dt>
<dd> Enables the use of escape analysis. This option is enabled by default. To disable the use of escape analysis, specify <code>-XX:-DoEscapeAnalysis</code>. Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:InitialCodeCacheSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the initial code cache size (in bytes). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default value is set to 500 KB. The initial code cache size should be not less than the system&#8217;s minimal memory page size. The following example shows how to set the initial code cache size to 32 KB: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:InitialCodeCacheSize=32k</code>
 
</pre>
</dl>
</dl>
<p> -XX:+Inline</p>
<dl>
<dt>
<dd> Enables method inlining. This option is enabled by default to increase performance. To disable method inlining, specify <code>-XX:-Inline</code>.</dl>
<p> -XX:InlineSmallCode=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum code size (in bytes) for compiled methods that should be inlined. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. Only compiled methods with the size smaller than the specified size will be inlined. By default, the maximum code size is set to 1000 bytes: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:InlineSmallCode=1000</code>
 
</pre>
</dl>
</dl>
<p> -XX:+LogCompilation</p>
<dl>
<dt>
<dd> Enables logging of compilation activity to a file named <code>hotspot.log</code> in the current working directory. You can specify a different log file path and name using the <code>-XX:LogFile</code> option. </p>
<p> By default, this option is disabled and compilation activity is not logged. The <code>-XX:+LogCompilation</code> option has to be used together with the <code>-XX:UnlockDiagnosticVMOptions</code> option that unlocks diagnostic JVM options. </p>
<p> You can enable verbose diagnostic output with a message printed to the console every time a method is compiled by using the <code>-XX:+PrintCompilation</code> option.</dl>
<p> -XX:MaxInlineSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum bytecode size (in bytes) of a method to be inlined. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. By default, the maximum bytecode size is set to 35 bytes: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxInlineSize=35</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxNodeLimit=<i>nodes</i></p>
<dl>
<dt>
<dd> Sets the maximum number of nodes to be used during single method compilation. By default, the maximum number of nodes is set to 65,000: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxNodeLimit=65000</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxTrivialSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum bytecode size (in bytes) of a trivial method to be inlined. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. By default, the maximum bytecode size of a trivial method is set to 6 bytes: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxTrivialSize=6</code>
 
</pre>
</dl>
</dl>
<p> -XX:+OptimizeStringConcat</p>
<dl>
<dt>
<dd> Enables the optimization of <code>String</code> concatenation operations. This option is enabled by default. To disable the optimization of <code>String</code> concatenation operations, specify <code>-XX:-OptimizeStringConcat</code>. Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:+PrintAssembly</p>
<dl>
<dt>
<dd> Enables printing of assembly code for bytecoded and native methods by using the external <code>disassembler.so</code> library. This enables you to see the generated code, which may help you to diagnose performance issues. </p>
<p> By default, this option is disabled and assembly code is not printed. The <code>-XX:+PrintAssembly</code> option has to be used together with the <code>-XX:UnlockDiagnosticVMOptions</code> option that unlocks diagnostic JVM options.</dl>
<p> -XX:+PrintCompilation</p>
<dl>
<dt>
<dd> Enables verbose diagnostic output from the JVM by printing a message to the console every time a method is compiled. This enables you to see which methods actually get compiled. By default, this option is disabled and diagnostic output is not printed. </p>
<p> You can also log compilation activity to a file by using the <code>-XX:+LogCompilation</code> option.</dl>
<p> -XX:+PrintInlining</p>
<dl>
<dt>
<dd> Enables printing of inlining decisions. This enables you to see which methods are getting inlined. </p>
<p> By default, this option is disabled and inlining information is not printed. The <code>-XX:+PrintInlining</code> option has to be used together with the <code>-XX:+UnlockDiagnosticVMOptions</code> option that unlocks diagnostic JVM options.</dl>
<p> -XX:ReservedCodeCacheSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum code cache size (in bytes) for JIT-compiled code. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default maximum code cache size is 240 MB; if you disable tiered compilation with the option <code>-XX:-TieredCompilation</code>, then the default size is 48 MB. This option has a limit of 2 GB; otherwise, an error is generated. The maximum code cache size should not be less than the initial code cache size; see the option <code>-XX:InitialCodeCacheSize</code>. This option is equivalent to <code>-Xmaxjitcodesize</code>.</dl>
<p> -XX:RTMAbortRatio=<i>abort_ratio</i></p>
<dl>
<dt>
<dd> The RTM abort ratio is specified as a percentage (%) of all executed RTM transactions. If a number of aborted transactions becomes greater than this ratio, then the compiled code will be deoptimized. This ratio is used when the <code>-XX:+UseRTMDeopt</code> option is enabled. The default value of this option is 50. This means that the compiled code will be deoptimized if 50% of all transactions are aborted.</dl>
<p> -XX:RTMRetryCount=<i>number_of_retries</i></p>
<dl>
<dt>
<dd> RTM locking code will be retried, when it is aborted or busy, the number of times specified by this option before falling back to the normal locking mechanism. The default value for this option is 5. The <code>-XX:UseRTMLocking</code> option must be enabled.</dl>
<p> -XX:-TieredCompilation</p>
<dl>
<dt>
<dd> Disables the use of tiered compilation. By default, this option is enabled. Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:+UseAES</p>
<dl>
<dt>
<dd> Enables hardware-based AES intrinsics for Intel, AMD, and SPARC hardware. Intel Westmere (2010 and newer), AMD Bulldozer (2011 and newer), and SPARC (T4 and newer) are the supported hardware. UseAES is used in conjunction with UseAESIntrinsics.</dl>
<p> -XX:+UseAESIntrinsics</p>
<dl>
<dt>
<dd> UseAES and UseAESIntrinsics flags are enabled by default and are supported only for Java HotSpot Server VM 32-bit and 64-bit. To disable hardware-based AES intrinsics, specify <code>-XX:-UseAES -XX:-UseAESIntrinsics</code>. For example, to enable hardware AES, use the following flags: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:+UseAES -XX:+UseAESIntrinsics</code>
 
</pre>
</dl>
<p> To support UseAES and UseAESIntrinsics flags for 32-bit and 64-bit use <code>-server</code> option to choose Java HotSpot Server VM. These flags are not supported on Client VM.</dl>
<p> -XX:+UseCodeCacheFlushing</p>
<dl>
<dt>
<dd> Enables flushing of the code cache before shutting down the compiler. This option is enabled by default. To disable flushing of the code cache before shutting down the compiler, specify <code>-XX:-UseCodeCacheFlushing</code>.</dl>
<p> -XX:+UseCondCardMark</p>
<dl>
<dt>
<dd> Enables checking of whether the card is already marked before updating the card table. This option is disabled by default and should only be used on machines with multiple sockets, where it will increase performance of Java applications that rely heavily on concurrent operations. Only the Java HotSpot Server VM supports this option.</dl>
<p> -XX:+UseRTMDeopt</p>
<dl>
<dt>
<dd> Auto-tunes RTM locking depending on the abort ratio. This ratio is specified by <code>-XX:RTMAbortRatio</code> option. If the number of aborted transactions exceeds the abort ratio, then the method containing the lock will be deoptimized and recompiled with all locks as normal locks. This option is disabled by default. The <code>-XX:+UseRTMLocking</code> option must be enabled.</dl>
<p> -XX:+UseRTMLocking</p>
<dl>
<dt>
<dd> Generate Restricted Transactional Memory (RTM) locking code for all inflated locks, with the normal locking mechanism as the fallback handler. This option is disabled by default. Options related to RTM are only available for the Java HotSpot Server VM on x86 CPUs that support Transactional Synchronization Extensions (TSX). </p>
<p> RTM is part of Intel&#8217;s TSX, which is an x86 instruction set extension and facilitates the creation of multithreaded applications. RTM introduces the new instructions <code>XBEGIN</code>, <code>XABORT</code>, <code>XEND</code>, and <code>XTEST</code>. The <code>XBEGIN</code> and <code>XEND</code> instructions enclose a set of instructions to run as a transaction. If no conflict is found when running the transaction, the memory and register modifications are committed together at the <code>XEND</code> instruction. The <code>XABORT</code> instruction can be used to explicitly abort a transaction and the <code>XEND</code> instruction to check if a set of instructions are being run in a transaction. </p>
<p> A lock on a transaction is inflated when another thread tries to access the same transaction, thereby blocking the thread that did not originally request access to the transaction. RTM requires that a fallback set of operations be specified in case a transaction aborts or fails. An RTM lock is a lock that has been delegated to the TSX&#8217;s system. </p>
<p> RTM improves performance for highly contended locks with low conflict in a critical region (which is code that must not be accessed by more than one thread concurrently). RTM also improves the performance of coarse-grain locking, which typically does not perform well in multithreaded applications. (Coarse-grain locking is the strategy of holding locks for long periods to minimize the overhead of taking and releasing locks, while fine-grained locking is the strategy of trying to achieve maximum parallelism by locking only when necessary and unlocking as soon as possible.) Also, for lightly contended locks that are used by different threads, RTM can reduce false cache line sharing, also known as cache line ping-pong. This occurs when multiple threads from different processors are accessing different resources, but the resources share the same cache line. As a result, the processors repeatedly invalidate the cache lines of other processors, which forces them to read from main memory instead of their cache.</dl>
<p> -XX:+UseSHA</p>
<dl>
<dt>
<dd> Enables hardware-based intrinsics for SHA crypto hash functions for SPARC hardware. <code>UseSHA</code> is used in conjunction with the <code>UseSHA1Intrinsics</code>, <code>UseSHA256Intrinsics</code>, and <code>UseSHA512Intrinsics</code> options. </p>
<p> The <code>UseSHA</code> and <code>UseSHA*Intrinsics</code> flags are enabled by default, and are supported only for Java HotSpot Server VM 64-bit on SPARC T4 and newer. </p>
<p> This feature is only applicable when using the <code>sun.security.provider.Sun</code> provider for SHA operations. </p>
<p> To disable all hardware-based SHA intrinsics, specify <code>-XX:-UseSHA</code>. To disable only a particular SHA intrinsic, use the appropriate corresponding option. For example: <code>-XX:-UseSHA256Intrinsics</code>.</dl>
<p> -XX:+UseSHA1Intrinsics</p>
<dl>
<dt>
<dd> Enables intrinsics for SHA-1 crypto hash function.</dl>
<p> -XX:+UseSHA256Intrinsics</p>
<dl>
<dt>
<dd> Enables intrinsics for SHA-224 and SHA-256 crypto hash functions.</dl>
<p> -XX:+UseSHA512Intrinsics</p>
<dl>
<dt>
<dd> Enables intrinsics for SHA-384 and SHA-512 crypto hash functions.</dl>
<p> -XX:+UseSuperWord</p>
<dl>
<dt>
<dd> Enables the transformation of scalar operations into superword operations. This option is enabled by default. To disable the transformation of scalar operations into superword operations, specify <code>-XX:-UseSuperWord</code>. Only the Java HotSpot Server VM supports this option.</dl>
<h3>Advanced Serviceability Options</h3>
<p> These options provide the ability to gather system information and perform extensive debugging. </p>
<p> -XX:+ExtendedDTraceProbes</p>
<dl>
<dt>
<dd> Enables additional <code>dtrace</code> tool probes that impact the performance. By default, this option is disabled and <code>dtrace</code> performs only standard probes.</dl>
<p> -XX:+HeapDumpOnOutOfMemory</p>
<dl>
<dt>
<dd> Enables the dumping of the Java heap to a file in the current directory by using the heap profiler (HPROF) when a <code>java.lang.OutOfMemoryError</code> exception is thrown. You can explicitly set the heap dump file path and name using the <code>-XX:HeapDumpPath</code> option. By default, this option is disabled and the heap is not dumped when an <code>OutOfMemoryError</code> exception is thrown.</dl>
<p> -XX:HeapDumpPath=<i>path</i></p>
<dl>
<dt>
<dd> Sets the path and file name for writing the heap dump provided by the heap profiler (HPROF) when the <code>-XX:+HeapDumpOnOutOfMemoryError</code> option is set. By default, the file is created in the current working directory, and it is named <code>java_pid</code><i>pid</i><code>.hprof</code> where <i>pid</i> is the identifier of the process that caused the error. The following example shows how to set the default file explicitly (<code>%p</code> represents the current process identificator): </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:HeapDumpPath=./java_pid%p.hprof</code>
 
</pre>
</dl>
<p> The following example shows how to set the heap dump file to <code>/var/log/java/java_heapdump.hprof</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:HeapDumpPath=/var/log/java/java_heapdump.hprof</code>
 
</pre>
</dl>
</dl>
<p> -XX:LogFile=<i>path</i></p>
<dl>
<dt>
<dd> Sets the path and file name where log data is written. By default, the file is created in the current working directory, and it is named <code>hotspot.log</code>. </p>
<p> The following example shows how to set the log file to <code>/var/log/java/hotspot.log</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:LogFile=/var/log/java/hotspot.log</code>
 
</pre>
</dl>
</dl>
<p> -XX:+PrintClassHistogram</p>
<dl>
<dt>
<dd> Enables printing of a class instance histogram after a <code>Control+C</code> event (<code>SIGTERM</code>). By default, this option is disabled. </p>
<p> Setting this option is equivalent to running the <code>jmap -histo</code> command, or the <code>jcmd </code><i>pid</i><code> GC.class_histogram</code> command, where <i>pid</i> is the current Java process identifier.</dl>
<p> -XX:+PrintConcurrentLocks</p>
<dl>
<dt>
<dd> Enables printing of locks after a event. By default, this option is disabled. </p>
<p> Enables printing of <code>java.util.concurrent</code> locks after a <code>Control+C</code> event (<code>SIGTERM</code>). By default, this option is disabled. </p>
<p> Setting this option is equivalent to running the <code>jstack -l</code> command or the <code>jcmd </code><i>pid</i><code> Thread.print -l</code> command, where <i>pid</i> is the current Java process identifier.</dl>
<p> -XX:+UnlockDiagnosticVMOptions</p>
<dl>
<dt>
<dd> Unlocks the options intended for diagnosing the JVM. By default, this option is disabled and diagnostic options are not available.</dl>
<h3>Advanced Garbage Collection Options</h3>
<p> These options control how garbage collection (GC) is performed by the Java HotSpot VM. </p>
<p> -XX:+AggressiveHeap</p>
<dl>
<dt>
<dd> Enables Java heap optimization. This sets various parameters to be optimal for long-running jobs with intensive memory allocation, based on the configuration of the computer (RAM and CPU). By default, the option is disabled and the heap is not optimized.</dl>
<p> -XX:+AlwaysPreTouch</p>
<dl>
<dt>
<dd> Enables touching of every page on the Java heap during JVM initialization. This gets all pages into the memory before entering the <code>main()</code> method. The option can be used in testing to simulate a long-running system with all virtual memory mapped to physical memory. By default, this option is disabled and all pages are committed as JVM heap space fills.</dl>
<p> -XX:+CMSClassUnloadingEnabled</p>
<dl>
<dt>
<dd> Enables class unloading when using the concurrent mark-sweep (CMS) garbage collector. This option is enabled by default. To disable class unloading for the CMS garbage collector, specify <code>-XX:-CMSClassUnloadingEnabled</code>.</dl>
<p> -XX:CMSExpAvgFactor=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of time (0 to 100) used to weight the current sample when computing exponential averages for the concurrent collection statistics. By default, the exponential averages factor is set to 25%. The following example shows how to set the factor to 15%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CMSExpAvgFactor=15</code>
 
</pre>
</dl>
</dl>
<p> -XX:CMSInitiatingOccupancyFraction=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of the old generation occupancy (0 to 100) at which to start a CMS collection cycle. The default value is set to -1. Any negative value (including the default) implies that <code>-XX:CMSTriggerRatio</code> is used to define the value of the initiating occupancy fraction. </p>
<p> The following example shows how to set the occupancy fraction to 20%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CMSInitiatingOccupancyFraction=20</code>
 
</pre>
</dl>
</dl>
<p> -XX:+CMSScavengeBeforeRemark</p>
<dl>
<dt>
<dd> Enables scavenging attempts before the CMS remark step. By default, this option is disabled.</dl>
<p> -XX:CMSTriggerRatio=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage (0 to 100) of the value specified by <code>-XX:MinHeapFreeRatio</code> that is allocated before a CMS collection cycle commences. The default value is set to 80%. </p>
<p> The following example shows how to set the occupancy fraction to 75%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:CMSTriggerRatio=75</code>
 
</pre>
</dl>
</dl>
<p> -XX:ConcGCThreads=<i>threads</i></p>
<dl>
<dt>
<dd> Sets the number of threads used for concurrent GC. The default value depends on the number of CPUs available to the JVM. </p>
<p> For example, to set the number of threads for concurrent GC to 2, specify the following option: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:ConcGCThreads=2</code>
 
</pre>
</dl>
</dl>
<p> -XX:+DisableExplicitGC</p>
<dl>
<dt>
<dd> Enables the option that disables processing of calls to <code>System.gc()</code>. This option is disabled by default, meaning that calls to <code>System.gc()</code> are processed. If processing of calls to <code>System.gc()</code> is disabled, the JVM still performs GC when necessary.</dl>
<p> -XX:+ExplicitGCInvokesConcurrent</p>
<dl>
<dt>
<dd> Enables invoking of concurrent GC by using the <code>System.gc()</code> request. This option is disabled by default and can be enabled only together with the <code>-XX:+UseConcMarkSweepGC</code> option.</dl>
<p> -XX:+ExplicitGCInvokesConcurrentAndUnloadsClasses</p>
<dl>
<dt>
<dd> Enables invoking of concurrent GC by using the <code>System.gc()</code> request and unloading of classes during the concurrent GC cycle. This option is disabled by default and can be enabled only together with the <code>-XX:+UseConcMarkSweepGC</code> option.</dl>
<p> -XX:G1HeapRegionSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the size of the regions into which the Java heap is subdivided when using the garbage-first (G1) collector. The value can be between 1 MB and 32 MB. The default region size is determined ergonomically based on the heap size. </p>
<p> The following example shows how to set the size of the subdivisions to 16 MB: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:G1HeapRegionSize=16m</code>
 
</pre>
</dl>
</dl>
<p> -XX:+G1PrintHeapRegions</p>
<dl>
<dt>
<dd> Enables the printing of information about which regions are allocated and which are reclaimed by the G1 collector. By default, this option is disabled.</dl>
<p> -XX:G1ReservePercent=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of the heap (0 to 50) that is reserved as a false ceiling to reduce the possibility of promotion failure for the G1 collector. By default, this option is set to 10%. </p>
<p> The following example shows how to set the reserved heap to 20%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:G1ReservePercent=20</code>
 
</pre>
</dl>
</dl>
<p> -XX:InitialHeapSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the initial size (in bytes) of the memory allocation pool. This value must be either 0, or a multiple of 1024 and greater than 1 MB. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default value is chosen at runtime based on system configuration. See the section &quot;Ergonomics&quot; in <i>Java SE HotSpot Virtual Machine Garbage Collection Tuning Guide</i> at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/index.html.">http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/index.html.</a> </p>
<p> The following examples show how to set the size of allocated memory to 6 MB using various units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:InitialHeapSize=6291456</code>
<code>-XX:InitialHeapSize=6144k</code>
<code>-XX:InitialHeapSize=6m</code>
 
</pre>
</dl>
<p> If you set this option to 0, then the initial size will be set as the sum of the sizes allocated for the old generation and the young generation. The size of the heap for the young generation can be set using the <code>-XX:NewSize</code> option.</dl>
<p> -XX:InitialSurvivorRatio=<i>ratio</i></p>
<dl>
<dt>
<dd> Sets the initial survivor space ratio used by the throughput garbage collector (which is enabled by the <code>-XX:+UseParallelGC</code> and/or &#8211;<code>XX:+UseParallelOldGC</code> options). Adaptive sizing is enabled by default with the throughput garbage collector by using the <code>-XX:+UseParallelGC</code> and <code>-XX:+UseParallelOldGC</code> options, and survivor space is resized according to the application behavior, starting with the initial value. If adaptive sizing is disabled (using the <code>-XX:-UseAdaptiveSizePolicy</code> option), then the <code>-XX:SurvivorRatio</code> option should be used to set the size of the survivor space for the entire execution of the application. </p>
<p> The following formula can be used to calculate the initial size of survivor space (S) based on the size of the young generation (Y), and the initial survivor space ratio (R): </p>
<dl>
<dt>
<dd>
<pre>
<code>S=Y/(R+2)</code>
 
</pre>
</dl>
<p> The 2 in the equation denotes two survivor spaces. The larger the value specified as the initial survivor space ratio, the smaller the initial survivor space size. </p>
<p> By default, the initial survivor space ratio is set to 8. If the default value for the young generation space size is used (2 MB), the initial size of the survivor space will be 0.2 MB. </p>
<p> The following example shows how to set the initial survivor space ratio to 4: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:InitialSurvivorRatio=4</code>
 
</pre>
</dl>
</dl>
<p> -XX:InitiatingHeapOccupancyPercent=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of the heap occupancy (0 to 100) at which to start a concurrent GC cycle. It is used by garbage collectors that trigger a concurrent GC cycle based on the occupancy of the entire heap, not just one of the generations (for example, the G1 garbage collector). </p>
<p> By default, the initiating value is set to 45%. A value of 0 implies nonstop GC cycles. The following example shows how to set the initiating heap occupancy to 75%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:InitiatingHeapOccupancyPercent=75</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxGCPauseMillis=<i>time</i></p>
<dl>
<dt>
<dd> Sets a target for the maximum GC pause time (in milliseconds). This is a soft goal, and the JVM will make its best effort to achieve it. By default, there is no maximum pause time value. </p>
<p> The following example shows how to set the maximum target pause time to 500 ms: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxGCPauseMillis=500</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxHeapSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum size (in byes) of the memory allocation pool. This value must be a multiple of 1024 and greater than 2 MB. Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. The default value is chosen at runtime based on system configuration. For server deployments, <code>-XX:InitialHeapSize</code> and <code>-XX:MaxHeapSize</code> are often set to the same value. See the section &quot;Ergonomics&quot; in <i>Java SE HotSpot Virtual Machine Garbage Collection Tuning Guide</i> at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/index.html.">http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/index.html.</a> </p>
<p> The following examples show how to set the maximum allowed size of allocated memory to 80 MB using various units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxHeapSize=83886080</code>
<code>-XX:MaxHeapSize=81920k</code>
<code>-XX:MaxHeapSize=80m</code>
 
</pre>
</dl>
<p> On Oracle Solaris 7 and Oracle Solaris 8 SPARC platforms, the upper limit for this value is approximately 4,000 MB minus overhead amounts. On Oracle Solaris 2.6 and x86 platforms, the upper limit is approximately 2,000 MB minus overhead amounts. On Linux platforms, the upper limit is approximately 2,000 MB minus overhead amounts. </p>
<p> The <code>-XX:MaxHeapSize</code> option is equivalent to <code>-Xmx</code>.</dl>
<p> -XX:MaxHeapFreeRatio=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the maximum allowed percentage of free heap space (0 to 100) after a GC event. If free heap space expands above this value, then the heap will be shrunk. By default, this value is set to 70%. </p>
<p> The following example shows how to set the maximum free heap ratio to 75%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxHeapFreeRatio=75</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxMetaspaceSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum amount of native memory that can be allocated for class metadata. By default, the size is not limited. The amount of metadata for an application depends on the application itself, other running applications, and the amount of memory available on the system. </p>
<p> The following example shows how to set the maximum class metadata size to 256 MB: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxMetaspaceSize=256m</code>
 
</pre>
</dl>
</dl>
<p> -XX:MaxNewSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum size (in bytes) of the heap for the young generation (nursery). The default value is set ergonomically.</dl>
<p> -XX:MaxTenuringThreshold=<i>threshold</i></p>
<dl>
<dt>
<dd> Sets the maximum tenuring threshold for use in adaptive GC sizing. The largest value is 15. The default value is 15 for the parallel (throughput) collector, and 6 for the CMS collector. </p>
<p> The following example shows how to set the maximum tenuring threshold to 10: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MaxTenuringThreshold=10</code>
 
</pre>
</dl>
</dl>
<p> -XX:MetaspaceSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the size of the allocated class metadata space that will trigger a garbage collection the first time it is exceeded. This threshold for a garbage collection is increased or decreased depending on the amount of metadata used. The default size depends on the platform.</dl>
<p> -XX:MinHeapFreeRatio=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the minimum allowed percentage of free heap space (0 to 100) after a GC event. If free heap space falls below this value, then the heap will be expanded. By default, this value is set to 40%. </p>
<p> The following example shows how to set the minimum free heap ratio to 25%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:MinHeapFreeRatio=25</code>
 
</pre>
</dl>
</dl>
<p> -XX:NewRatio=<i>ratio</i></p>
<dl>
<dt>
<dd> Sets the ratio between young and old generation sizes. By default, this option is set to 2. The following example shows how to set the young/old ratio to 1: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:NewRatio=1</code>
 
</pre>
</dl>
</dl>
<p> -XX:NewSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the initial size (in bytes) of the heap for the young generation (nursery). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. </p>
<p> The young generation region of the heap is used for new objects. GC is performed in this region more often than in other regions. If the size for the young generation is too low, then a large number of minor GCs will be performed. If the size is too high, then only full GCs will be performed, which can take a long time to complete. Oracle recommends that you keep the size for the young generation between a half and a quarter of the overall heap size. </p>
<p> The following examples show how to set the initial size of young generation to 256 MB using various units: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:NewSize=256m</code>
<code>-XX:NewSize=262144k</code>
<code>-XX:NewSize=268435456</code>
 
</pre>
</dl>
<p> The <code>-XX:NewSize</code> option is equivalent to <code>-Xmn</code>.</dl>
<p> -XX:ParallelGCThreads=<i>threads</i></p>
<dl>
<dt>
<dd> Sets the number of threads used for parallel garbage collection in the young and old generations. The default value depends on the number of CPUs available to the JVM. </p>
<p> For example, to set the number of threads for parallel GC to 2, specify the following option: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:ParallelGCThreads=2</code>
 
</pre>
</dl>
</dl>
<p> -XX:+ParallelRefProcEnabled</p>
<dl>
<dt>
<dd> Enables parallel reference processing. By default, this option is disabled.</dl>
<p> -XX:+PrintAdaptiveSizePolicy</p>
<dl>
<dt>
<dd> Enables printing of information about adaptive generation sizing. By default, this option is disabled.</dl>
<p> -XX:+PrintGC</p>
<dl>
<dt>
<dd> Enables printing of messages at every GC. By default, this option is disabled.</dl>
<p> -XX:+PrintGCApplicationConcurrentTime</p>
<dl>
<dt>
<dd> Enables printing of how much time elapsed since the last pause (for example, a GC pause). By default, this option is disabled.</dl>
<p> -XX:+PrintGCApplicationStoppedTime</p>
<dl>
<dt>
<dd> Enables printing of how much time the pause (for example, a GC pause) lasted. By default, this option is disabled.</dl>
<p> -XX:+PrintGCDateStamps</p>
<dl>
<dt>
<dd> Enables printing of a date stamp at every GC. By default, this option is disabled.</dl>
<p> -XX:+PrintGCDetails</p>
<dl>
<dt>
<dd> Enables printing of detailed messages at every GC. By default, this option is disabled.</dl>
<p> -XX:+PrintGCTaskTimeStamps</p>
<dl>
<dt>
<dd> Enables printing of time stamps for every individual GC worker thread task. By default, this option is disabled.</dl>
<p> -XX:+PrintGCTimeStamps</p>
<dl>
<dt>
<dd> Enables printing of time stamps at every GC. By default, this option is disabled.</dl>
<p> -XX:+PrintStringDeduplicationStatistics</p>
<dl>
<dt>
<dd> Prints detailed deduplication statistics. By default, this option is disabled. See the <code>-XX:+UseStringDeduplication</code> option.</dl>
<p> -XX:+PrintTenuringDistribution</p>
<dl>
<dt>
<dd> Enables printing of tenuring age information. The following is an example of the output: </p>
<dl>
<dt>
<dd>
<pre>
<code>Desired survivor size 48286924 bytes, new threshold 10 (max 10)</code>
<code>- age 1: 28992024 bytes, 28992024 total</code>
<code>- age 2: 1366864 bytes, 30358888 total</code>
<code>- age 3: 1425912 bytes, 31784800 total</code>
<code>...</code>
 
</pre>
</dl>
<p> Age 1 objects are the youngest survivors (they were created after the previous scavenge, survived the latest scavenge, and moved from eden to survivor space). Age 2 objects have survived two scavenges (during the second scavenge they were copied from one survivor space to the next). And so on. </p>
<p> In the preceding example, 28 992 024 bytes survived one scavenge and were copied from eden to survivor space, 1 366 864 bytes are occupied by age 2 objects, etc. The third value in each row is the cumulative size of objects of age n or less. </p>
<p> By default, this option is disabled.</dl>
<p> -XX:+ScavengeBeforeFullGC</p>
<dl>
<dt>
<dd> Enables GC of the young generation before each full GC. This option is enabled by default. Oracle recommends that you <i>do not</i> disable it, because scavenging the young generation before a full GC can reduce the number of objects reachable from the old generation space into the young generation space. To disable GC of the young generation before each full GC, specify <code>-XX:-ScavengeBeforeFullGC</code>.</dl>
<p> -XX:SoftRefLRUPolicyMSPerMB=<i>time</i></p>
<dl>
<dt>
<dd> Sets the amount of time (in milliseconds) a softly reachable object is kept active on the heap after the last time it was referenced. The default value is one second of lifetime per free megabyte in the heap. The <code>-XX:SoftRefLRUPolicyMSPerMB</code> option accepts integer values representing milliseconds per one megabyte of the current heap size (for Java HotSpot Client VM) or the maximum possible heap size (for Java HotSpot Server VM). This difference means that the Client VM tends to flush soft references rather than grow the heap, whereas the Server VM tends to grow the heap rather than flush soft references. In the latter case, the value of the <code>-Xmx</code> option has a significant effect on how quickly soft references are garbage collected. </p>
<p> The following example shows how to set the value to 2.5 seconds: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:SoftRefLRUPolicyMSPerMB=2500</code>
 
</pre>
</dl>
</dl>
<p> -XX:StringDeduplicationAgeThreshold=<i>threshold</i></p>
<dl>
<dt>
<dd> <code>String</code> objects reaching the specified age are considered candidates for deduplication. An object&#8217;s age is a measure of how many times it has survived garbage collection. This is sometimes referred to as tenuring; see the <code>-XX:+PrintTenuringDistribution</code> option. Note that <code>String</code> objects that are promoted to an old heap region before this age has been reached are always considered candidates for deduplication. The default value for this option is <code>3</code>. See the <code>-XX:+UseStringDeduplication</code> option.</dl>
<p> -XX:SurvivorRatio=<i>ratio</i></p>
<dl>
<dt>
<dd> Sets the ratio between eden space size and survivor space size. By default, this option is set to 8. The following example shows how to set the eden/survivor space ratio to 4: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:SurvivorRatio=4</code>
 
</pre>
</dl>
</dl>
<p> -XX:TargetSurvivorRatio=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the desired percentage of survivor space (0 to 100) used after young garbage collection. By default, this option is set to 50%. </p>
<p> The following example shows how to set the target survivor space ratio to 30%: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:TargetSurvivorRatio=30</code>
 
</pre>
</dl>
</dl>
<p> -XX:TLABSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the initial size (in bytes) of a thread-local allocation buffer (TLAB). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes, <code>m</code> or <code>M</code> to indicate megabytes, <code>g</code> or <code>G</code> to indicate gigabytes. If this option is set to 0, then the JVM chooses the initial size automatically. </p>
<p> The following example shows how to set the initial TLAB size to 512 KB: </p>
<dl>
<dt>
<dd>
<pre>
<code>-XX:TLABSize=512k</code>
 
</pre>
</dl>
</dl>
<p> -XX:+UseAdaptiveSizePolicy</p>
<dl>
<dt>
<dd> Enables the use of adaptive generation sizing. This option is enabled by default. To disable adaptive generation sizing, specify <code>-XX:-UseAdaptiveSizePolicy</code> and set the size of the memory allocation pool explicitly (see the <code>-XX:SurvivorRatio</code> option).</dl>
<p> -XX:+UseCMSInitiatingOccupancyOnly</p>
<dl>
<dt>
<dd> Enables the use of the occupancy value as the only criterion for initiating the CMS collector. By default, this option is disabled and other criteria may be used.</dl>
<p> -XX:+UseConcMarkSweepGC</p>
<dl>
<dt>
<dd> Enables the use of the CMS garbage collector for the old generation. Oracle recommends that you use the CMS garbage collector when application latency requirements cannot be met by the throughput (<code>-XX:+UseParallelGC</code>) garbage collector. The G1 garbage collector (<code>-XX:+UseG1GC</code>) is another alternative. </p>
<p> By default, this option is disabled and the collector is chosen automatically based on the configuration of the machine and type of the JVM. When this option is enabled, the <code>-XX:+UseParNewGC</code> option is automatically set and you should not disable it, because the following combination of options has been deprecated in JDK 8: <code>-XX:+UseConcMarkSweepGC -XX:-UseParNewGC</code>.</dl>
<p> -XX:+UseG1GC</p>
<dl>
<dt>
<dd> Enables the use of the garbage-first (G1) garbage collector. It is a server-style garbage collector, targeted for multiprocessor machines with a large amount of RAM. It meets GC pause time goals with high probability, while maintaining good throughput. The G1 collector is recommended for applications requiring large heaps (sizes of around 6 GB or larger) with limited GC latency requirements (stable and predictable pause time below 0.5 seconds). </p>
<p> By default, this option is disabled and the collector is chosen automatically based on the configuration of the machine and type of the JVM.</dl>
<p> -XX:+UseGCOverheadLimit</p>
<dl>
<dt>
<dd> Enables the use of a policy that limits the proportion of time spent by the JVM on GC before an <code>OutOfMemoryError</code> exception is thrown. This option is enabled, by default and the parallel GC will throw an <code>OutOfMemoryError</code> if more than 98% of the total time is spent on garbage collection and less than 2% of the heap is recovered. When the heap is small, this feature can be used to prevent applications from running for long periods of time with little or no progress. To disable this option, specify <code>-XX:-UseGCOverheadLimit</code>.</dl>
<p> -XX:+UseNUMA</p>
<dl>
<dt>
<dd> Enables performance optimization of an application on a machine with nonuniform memory architecture (NUMA) by increasing the application&#8217;s use of lower latency memory. By default, this option is disabled and no optimization for NUMA is made. The option is only available when the parallel garbage collector is used (<code>-XX:+UseParallelGC</code>).</dl>
<p> -XX:+UseParallelGC</p>
<dl>
<dt>
<dd> Enables the use of the parallel scavenge garbage collector (also known as the throughput collector) to improve the performance of your application by leveraging multiple processors. </p>
<p> By default, this option is disabled and the collector is chosen automatically based on the configuration of the machine and type of the JVM. If it is enabled, then the <code>-XX:+UseParallelOldGC</code> option is automatically enabled, unless you explicitly disable it.</dl>
<p> -XX:+UseParallelOldGC</p>
<dl>
<dt>
<dd> Enables the use of the parallel garbage collector for full GCs. By default, this option is disabled. Enabling it automatically enables the <code>-XX:+UseParallelGC</code> option.</dl>
<p> -XX:+UseParNewGC</p>
<dl>
<dt>
<dd> Enables the use of parallel threads for collection in the young generation. By default, this option is disabled. It is automatically enabled when you set the <code>-XX:+UseConcMarkSweepGC</code> option. Using the <code>-XX:+UseParNewGC</code> option without the <code>-XX:+UseConcMarkSweepGC</code> option was deprecated in JDK 8.</dl>
<p> -XX:+UseSerialGC</p>
<dl>
<dt>
<dd> Enables the use of the serial garbage collector. This is generally the best choice for small and simple applications that do not require any special functionality from garbage collection. By default, this option is disabled and the collector is chosen automatically based on the configuration of the machine and type of the JVM.</dl>
<p> -XX:+UseSHM</p>
<dl>
<dt>
<dd> On Linux, enables the JVM to use shared memory to setup large pages. </p>
<p> For more information, see &quot;Large Pages&quot;.</dl>
<p> -XX:+UseStringDeduplication</p>
<dl>
<dt>
<dd> Enables string deduplication. By default, this option is disabled. To use this option, you must enable the garbage-first (G1) garbage collector. See the <code>-XX:+UseG1GC</code> option. </p>
<p> <i>String deduplication</i> reduces the memory footprint of <code>String</code> objects on the Java heap by taking advantage of the fact that many <code>String</code> objects are identical. Instead of each <code>String</code> object pointing to its own character array, identical <code>String</code> objects can point to and share the same character array.</dl>
<p> -XX:+UseTLAB</p>
<dl>
<dt>
<dd> Enables the use of thread-local allocation blocks (TLABs) in the young generation space. This option is enabled by default. To disable the use of TLABs, specify <code>-XX:-UseTLAB</code>.</dl>
<h3>Deprecated and Removed Options</h3>
<p> These options were included in the previous release, but have since been considered unnecessary. </p>
<p> -Xincgc</p>
<dl>
<dt>
<dd> Enables incremental garbage collection. This option was deprecated in JDK 8 with no replacement.</dl>
<p> -Xrun<i>libname</i></p>
<dl>
<dt>
<dd> Loads the specified debugging/profiling library. This option was superseded by the <code>-agentlib</code> option.</dl>
<p> -XX:CMSIncrementalDutyCycle=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of time (0 to 100) between minor collections that the concurrent collector is allowed to run. This option was deprecated in JDK 8 with no replacement, following the deprecation of the <code>-XX:+CMSIncrementalMode</code> option.</dl>
<p> -XX:CMSIncrementalDutyCycleMin=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of time (0 to 100) between minor collections that is the lower bound for the duty cycle when <code>-XX:+CMSIncrementalPacing</code> is enabled. This option was deprecated in JDK 8 with no replacement, following the deprecation of the <code>-XX:+CMSIncrementalMode</code> option.</dl>
<p> -XX:+CMSIncrementalMode</p>
<dl>
<dt>
<dd> Enables the incremental mode for the CMS collector. This option was deprecated in JDK 8 with no replacement, along with other options that start with <code>CMSIncremental</code>.</dl>
<p> -XX:CMSIncrementalOffset=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of time (0 to 100) by which the incremental mode duty cycle is shifted to the right within the period between minor collections. This option was deprecated in JDK 8 with no replacement, following the deprecation of the <code>-XX:+CMSIncrementalMode</code> option.</dl>
<p> -XX:+CMSIncrementalPacing</p>
<dl>
<dt>
<dd> Enables automatic adjustment of the incremental mode duty cycle based on statistics collected while the JVM is running. This option was deprecated in JDK 8 with no replacement, following the deprecation of the <code>-XX:+CMSIncrementalMode</code> option.</dl>
<p> -XX:CMSIncrementalSafetyFactor=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of time (0 to 100) used to add conservatism when computing the duty cycle. This option was deprecated in JDK 8 with no replacement, following the deprecation of the <code>-XX:+CMSIncrementalMode</code> option.</dl>
<p> -XX:CMSInitiatingPermOccupancyFraction=<i>percent</i></p>
<dl>
<dt>
<dd> Sets the percentage of the permanent generation occupancy (0 to 100) at which to start a GC. This option was deprecated in JDK 8 with no replacement.</dl>
<p> -XX:MaxPermSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum permanent generation space size (in bytes). This option was deprecated in JDK 8, and superseded by the <code>-XX:MaxMetaspaceSize</code> option.</dl>
<p> -XX:PermSize=<i>size</i></p>
<dl>
<dt>
<dd> Sets the space (in bytes) allocated to the permanent generation that triggers a garbage collection if it is exceeded. This option was deprecated un JDK 8, and superseded by the <code>-XX:MetaspaceSize</code> option.</dl>
<p> -XX:+UseSplitVerifier</p>
<dl>
<dt>
<dd> Enables splitting of the verification process. By default, this option was enabled in the previous releases, and verification was split into two phases: type referencing (performed by the compiler) and type checking (performed by the JVM runtime). This option was deprecated in JDK 8, and verification is now split by default without a way to disable it.</dl>
<p> -XX:+UseStringCache</p>
<dl>
<dt>
<dd> Enables caching of commonly allocated strings. This option was removed from JDK 8 with no replacement.</dl>
<h2>PERFORMANCE TUNING EXAMPLES</h2>
<p> The following examples show how to use experimental tuning flags to either optimize throughput or to provide lower response time. </p>
<p> <code>Example 1 </code>Tuning for Higher Throughput</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>java -d64 -server -XX:+AggressiveOpts -XX:+UseLargePages -Xmn10g  -Xms26g -Xmx26g</code>
 
</pre>
</dl>
</dl>
<p> <code>Example 2 </code>Tuning for Lower Response Time</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>java -d64 -XX:+UseG1GC -Xms26g Xmx26g -XX:MaxGCPauseMillis=500 -XX:+PrintGCTimeStamp</code>
 
</pre>
</dl>
</dl>
<h2>LARGE PAGES</h2>
<p> Also known as huge pages, large pages are memory pages that are significantly larger than the standard memory page size (which varies depending on the processor and operating system). Large pages optimize processor Translation-Lookaside Buffers. </p>
<p> A Translation-Lookaside Buffer (TLB) is a page translation cache that holds the most-recently used virtual-to-physical address translations. TLB is a scarce system resource. A TLB miss can be costly as the processor must then read from the hierarchical page table, which may require multiple memory accesses. By using a larger memory page size, a single TLB entry can represent a larger memory range. There will be less pressure on TLB, and memory-intensive applications may have better performance. </p>
<p> However, large pages page memory can negatively affect system performance. For example, when a large mount of memory is pinned by an application, it may create a shortage of regular memory and cause excessive paging in other applications and slow down the entire system. Also, a system that has been up for a long time could produce excessive fragmentation, which could make it impossible to reserve enough large page memory. When this happens, either the OS or JVM reverts to using regular pages.</p>
<h3>Large Pages Support</h3>
<p> Solaris and Linux support large pages. </p>
<p> <font SIZE="+1"> <code>Solaris</code></p>
<dl>
<dt>
<dd>
<p> Solaris 9 and later include Multiple Page Size Support (MPSS); no additional configuration is necessary. See <a rel="nofollow" href="http://www.oracle.com/technetwork/server-storage/solaris10/overview/solaris9-features-scalability-135663.html.">http://www.oracle.com/technetwork/server-storage/solaris10/overview/solaris9-features-scalability-135663.html.</a></dl>
<p> </font><font SIZE="+2"> <code>Linux</code></p>
<dl>
<dt>
<dd>
<p> The 2.6 kernel supports large pages. Some vendors have backported the code to their 2.4-based releases. To check if your system can support large page memory, try the following: </p>
<dl>
<dt>
<dd> </font></p>
<pre>
<code># cat /proc/meminfo | grep Huge</code>
<code>HugePages_Total: 0</code>
<code>HugePages_Free: 0</code>
<code>Hugepagesize: 2048 kB</code>
 
</pre>
</dl>
<p> If the output shows the three &quot;Huge&quot; variables, then your system can support large page memory but it needs to be configured. If the command prints nothing, then your system does not support large pages. To configure the system to use large page memory, login as <code>root</code>, and then follow these steps: </p>
<dl>
<dt>
<dd> 1. If you are using the option <code>-XX:+UseSHM</code> (instead of <code>-XX:+UseHugeTLBFS</code>), then increase the <code>SHMMAX</code> value. It must be larger than the Java heap size. On a system with 4 GB of physical RAM (or less), the following will make all the memory sharable: </p>
<dl>
<dt>
<dd>
<pre>
<code># echo 4294967295 &gt; /proc/sys/kernel/shmmax</code>
 
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. If you are using the option <code>-XX:+UseSHM</code> or <code>-XX:+UseHugeTLBFS</code>, then specify the number of large pages. In the following example, 3 GB of a 4 GB system are reserved for large pages (assuming a large page size of 2048kB, then 3 GB = 3 * 1024 MB = 3072 MB = 3072 * 1024 kB = 3145728 kB and 3145728 kB / 2048 kB = 1536): </p>
<dl>
<dt>
<dd>
<pre>
<code># echo 1536 &gt; /proc/sys/vm/nr_hugepages</code>
 
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<table BORDER>
<tr VALIGN=top>
<td>
<dl>
<dt>
<dd> &bull; Note that the values contained in <code>/proc</code> will reset after you reboot your system, so may want to set them in an initialization script (for example, <code>rc.local</code> or <code>sysctl.conf</code>).</dl>
<dl>
<dt>
<dd> &bull; If you configure (or resize) the OS kernel parameters <code>/proc/sys/kernel/shmmax</code> or <code>/proc/sys/vm/nr_hugepages</code>, Java processes may allocate large pages for areas in addition to the Java heap. These steps can allocate large pages for the following areas: </p>
<dl>
<dt>
<dd> &bull; Java heap</dl>
<dl>
<dt>
<dd> &bull; Code cache</dl>
<dl>
<dt>
<dd> &bull; The marking bitmap data structure for the parallel GC</dl>
<p> Consequently, if you configure the <code>nr_hugepages</code> parameter to the size of the Java heap, then the JVM can fail in allocating the code cache areas on large pages because these areas are quite large in size.</dl>
</td>
</tr>
</table>
</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> The following exit values are typically returned by the launcher when the launcher is called with the wrong arguments, serious errors, or exceptions thrown by the JVM. However, a Java application may choose to return any value by using the API call <code>System.exit(exitValue)</code>. The values are: </p>
<dl>
<dt>
<dd> &bull; <code>0</code>: Successful completion</dl>
<dl>
<dt>
<dd> &bull; <code>&gt;0</code>: An error occurred</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-javac/">javac</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-jdb/">jdb</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-jar/">jar</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-jstat/">jstat</a>(1)</dl>
<h2>Index</h2>
