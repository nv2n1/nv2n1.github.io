---
title: "rmic(1)"
name: "rmic"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmic/"
description: "rmic – Generates stub, skeleton, and tie classes for remote objects that use the Java Remote Method Protocol (JRMP) or Internet Inter-Orb protocol (IIOP). Also generates Object Management Group (OM..."
---

<h2>NAME</h2>
<p> rmic &#8211; Generates stub, skeleton, and tie classes for remote objects that use the Java Remote Method Protocol (JRMP) or Internet Inter-Orb protocol (IIOP). Also generates Object Management Group (OMG) Interface Definition Language (IDL)</p>
<h2>SYNOPSIS</h2>
<pre>
<code>rmic</code> [ <i>options</i> ] <i>package-qualified-class-names</i>
</pre>
<dl>
<dt><i>options</i></p>
<dd> The command-line <code>options</code>. See Options.</p>
<dt><i>package-qualified-class-names</i></p>
<dd> Class names that include their packages, for example, <code>java.awt.Color</code>.</dl>
<h2>DESCRIPTION</h2>
<p> <i>Deprecation Note:</i> Support for static generation of Java Remote Method Protocol (JRMP) stubs and skeletons has been deprecated. Oracle recommends that you use dynamically generated JRMP stubs instead, eliminating the need to use this tool for JRMP-based applications. See the <code>java.rmi.server.UnicastRemoteObject</code> specification at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/rmi/server/UnicastRemoteObject.html">http://docs.oracle.com/javase/8/docs/api/java/rmi/server/UnicastRemoteObject.html</a> for further information. </p>
<p> The <code>rmic</code> compiler generates stub and skeleton class files using the Java Remote Method Protocol (JRMP) and stub and tie class files (IIOP protocol) for remote objects. These class files are generated from compiled Java programming language classes that are remote object implementation classes. A remote implementation class is a class that implements the interface <code>java.rmi.Remote</code>. The class names in the <code>rmic</code> command must be for classes that were compiled successfully with the <code>javac</code> command and must be fully package qualified. For example, running the <code>rmic</code> command on the class file name <code>HelloImpl</code> as shown here creates the <code>HelloImpl_Stub.class</code>file in the hello subdirectory (named for the class&#8217;s package): </p>
<pre>
<code>rmic hello.HelloImpl</code>
</pre>
<pre>
</pre>
<p> A skeleton for a remote object is a JRMP protocol server-side entity that has a method that dispatches calls to the remote object implementation. </p>
<p> A tie for a remote object is a server-side entity similar to a skeleton, but communicates with the client with the IIOP protocol. </p>
<p> A stub is a client-side proxy for a remote object that is responsible for communicating method invocations on remote objects to the server where the actual remote object implementation resides. A client&#8217;s reference to a remote object, therefore, is actually a reference to a local stub. </p>
<p> By default, the <code>rmic</code> command generates stub classes that use the 1.2 JRMP stub protocol version only, as though the <code>-v1.2</code> option was specified. The <code>-vcompat</code> option was the default in releases before 5.0. Use the <code>-iiop</code> option to generate stub and tie classes for the IIOP protocol. See Options. </p>
<p> A stub implements only the remote interfaces, and not any local interfaces that the remote object also implements. Because a JRMP stub implements the same set of remote interfaces as the remote object, a client can use the Java programming language built-in operators for casting and type checking. For IIOP, the <code>PortableRemoteObject.narrow</code> method must be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-bootclasspath <i>path</i></p>
<dd>
 Overrides the location of bootstrap class files.</p>
<dt>-classpath path</p>
<dd>
 Specifies the path the <code>rmic</code> command uses to look up classes. This option overrides the default or the <code>CLASSPATH</code> environment variable when it is set. Directories are separated by colons. The general format for path is: <code>.:&lt;your_path&gt;</code>, for example: <code>.:/usr/local/java/classes</code>.</p>
<dt>-d <i>directory</i></p>
<dd>
 Specifies the root destination directory for the generated class hierarchy. You can use this option to specify a destination directory for the stub, skeleton, and tie files. For example, the following command places the stub and skeleton classes derived from MyClass into the directory /java/classes/exampleclass. </p>
<pre>
<code>rmic -d /java/classes exampleclass.MyClass</code>
</pre>
<pre>
</pre>
<p> If the <code>-d</code> option is not specified, then the default behavior is as if <code>-d .</code> was specified. The package hierarchy of the target class is created in the current directory, and stub/tie/skeleton files are placed within it. In some earlier releases of the <code>rmic</code> command, if the <code>-d</code> option was not specified, then the package hierarchy was not created, and all of the output files were placed directly in the current directory.</p>
<dt>-extdirs <i>path</i></p>
<dd>
 Overrides the location of installed extensions.</p>
<dt>-g</p>
<dd>
 Enables the generation of all debugging information, including local variables. By default, only line number information is generated.</p>
<dt>-idl</p>
<dd>
 Causes the <code>rmic</code> command to generate OMG IDL for the classes specified and any classes referenced. IDL provides a purely declarative, programming language-independent way to specify an API for an object. The IDL is used as a specification for methods and data that can be written in and called from any language that provides CORBA bindings. This includes Java and C++ among others. See Java IDL: IDL to Java Language Mapping at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/mapping/jidlMapping.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/mapping/jidlMapping.html</a> </p>
<p> When the <code>-idl</code> option is used, other options also include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The <code>-always</code> or <code>-alwaysgenerate</code> options force regeneration even when existing stubs/ties/IDL are newer than the input class.</p>
<dt>&bull;</p>
<dd> The <code>-factory</code> option uses the <code>factory</code> keyword in generated IDL.</p>
<dt>&bull;</p>
<dd> The <code>-idlModule</code> from J<code>avaPackage[.class]</code><code>toIDLModule</code> specifies <code>IDLEntity</code> package mapping, for example: <code>-idlModule</code><code>my.module my::real::idlmod</code>.</p>
<dt>&bull;</p>
<dd> <code>-idlFile</code><code>fromJavaPackage[.class] toIDLFile</code> specifies <code>IDLEntity</code> file mapping, for example: <code>-idlFile test.pkg.X TEST16.idl</code>.</dl>
</dl>
<dt>-iiop</p>
<dd>
 Causes the <code>rmic</code> command to generate IIOP stub and tie classes, rather than JRMP stub and skeleton classes. A stub class is a local proxy for a remote object and is used by clients to send calls to a server. Each remote interface requires a stub class, which implements that remote interface. A client reference to a remote object is a reference to a stub. Tie classes are used on the server side to process incoming calls, and dispatch the calls to the proper implementation class. Each implementation class requires a tie class. </p>
<p> If you call the <code>rmic</code> command with the <code>-iiop</code>, then it generates stubs and ties that conform to this naming convention: </p>
<pre>
<code>_&lt;implementationName&gt;_stub.class</code>
</pre>
<pre>
<code>_&lt;interfaceName&gt;_tie.class</code>
</pre>
<pre>
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> When you use the <code>-iiop</code> option, other options also include:</p>
<dt>&bull;</p>
<dd> The <code>-always</code> or <code>-alwaysgenerate</code> options force regeneration even when existing stubs/ties/IDL are newer than the input class.</p>
<dt>&bull;</p>
<dd> The <code>-nolocalstubs</code> option means do not create stubs optimized for same-process clients and servers.</p>
<dt>&bull;</p>
<dd> The <code>-noValueMethods</code> option must be used with the <code>-idl</code> option. The <code>-noValueMethods</code> option prevents the addition of <code>valuetype</code> methods and initializers to emitted IDL. These methods and initializers are optional for valuetypes, and are generated unless the <code>-noValueMethods</code> option is specified with the <code>-idl</code> option.</p>
<dt>&bull;</p>
<dd> The <code>-poa</code> option changes the inheritance from <code>org.omg.CORBA_2_3.portable.ObjectImpl</code> to <code>org.omg.PortableServer.Servant</code>. The <code>PortableServer</code> module for the Portable Object Adapter (POA) defines the native <code>Servant</code> type. In the Java programming language, the <code>Servant</code> type is mapped to the <code>Java org.omg.PortableServer.Servant</code> class. It serves as the base class for all POA servant implementations and provides a number of methods that can be called by the application programmer, and methods that are called by the POA and that can be overridden by the user to control aspects of servant behavior. Based on the OMG IDL to Java Language Mapping Specification, CORBA V 2.3.1 ptc/00-01-08.pdf..RE </p>
<dt>-J</p>
<dd>
 Used with any Java command, the <code>-J</code> option passes the argument that follows the <code>-J</code> (no spaces between the <code>-J</code>and the argument) to the Java interpreter</p>
<dt>-keep or -keepgenerated</p>
<dd>
 Retains the generated <code>.java</code> source files for the stub, skeleton, and tie classes and writes them to the same directory as the<code>.class</code> files.</p>
<dt>-nowarn</p>
<dd>
 Turns off warnings. When the <code>-nowarn</code> options is used. The compiler does not print out any warnings.</p>
<dt>-nowrite</p>
<dd>
 Does not write compiled classes to the file system.</p>
<dt>-vcompat (deprecated)</p>
<dd>
 Generates stub and skeleton classes that are compatible with both the 1.1 and 1.2 JRMP stub protocol versions. This option was the default in releases before 5.0. The generated stub classes use the 1.1 stub protocol version when loaded in a JDK 1.1 virtual machine and use the 1.2 stub protocol version when loaded into a 1.2 (or later) virtual machine. The generated skeleton classes support both 1.1 and 1.2 stub protocol versions. The generated classes are relatively large to support both modes of operation. Note: This option has been deprecated. See Description.</p>
<dt>-verbose</p>
<dd>
 Causes the compiler and linker to print out messages about what classes are being compiled and what class files are being loaded.</p>
<dt>-v1.1 (deprecated)</p>
<dd>
 Generates stub and skeleton classes for the 1.1 JRMP stub protocol version only. The <code>-v1.1</code> option is only useful for generating stub classes that are serialization-compatible with preexisting, statically deployed stub classes that were generated by the <code>rmic</code> command from JDK 1.1 and that cannot be upgraded (and dynamic class loading is not being used). Note: This option has been deprecated. See Description.</p>
<dt>-v1.2 (deprecated)</p>
<dd>
 (Default) Generates stub classes for the 1.2 JRMP stub protocol version only. No skeleton classes are generated because skeleton classes are not used with the 1.2 stub protocol version. The generated stub classes do not work when they are loaded into a JDK 1.1 virtual machine. Note: This option has been deprecated. See Description.</dl>
</dl>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>CLASSPATH</p>
<dd> Used to provide the system a path to user-defined classes. Directories are separated by colons, for example: <code>.:/usr/local/java/classes</code>.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-javac/">javac</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>&bull;</p>
<dd> Setting the Class Path </p>
</dl>
<h2>Index</h2>
