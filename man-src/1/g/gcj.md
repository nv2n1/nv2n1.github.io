---
title: "gcj(1)"
name: "gcj"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcj/"
description: "gcj – Ahead-of-time compiler for the Java language"
---

<h2 class="name">NAME</h2>
<p> gcj &#8211; Ahead-of-time compiler for the Java language </p>
<h2>SYNOPSIS</h2>
<p> gcj [<code>-I</code><i>dir</i>&#8230;] [<code>-d</code> <i>dir</i>&#8230;]<br />
&nbsp;<wbr>[<code>&#8211;CLASSPATH</code>=<i>path</i>]&nbsp;<wbr>[<code>&#8211;classpath</code>=<i>path</i>]<br />
&nbsp;<wbr>[<code>-f</code><i>option</i>&#8230;]&nbsp;<wbr>[<code>&#8211;encoding</code>=<i>name</i>]<br />
&nbsp;<wbr>[<code>&#8211;main</code>=<i>classname</i>]&nbsp;<wbr>[<code>-D</code><i>name</i>[=<i>value</i>]&#8230;]<br />
&nbsp;<wbr>[<code>-C</code>]&nbsp;<wbr>[<code>&#8211;resource</code>&nbsp;<wbr><i>resource-name</i>]&nbsp;<wbr>[<code>-d</code>&nbsp;<wbr><i>directory</i>]<br />
&nbsp;<wbr>[<code>-W</code><i>warn</i>&#8230;]<br />
&nbsp;<wbr><i>sourcefile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> As <code>gcj</code> is just another front end to <code>gcc</code>, it supports many of the same options as gcc. This manual only documents the options specific to <code>gcj</code>.</p>
<h2>OPTIONS</h2>
<h2>Input and output files</h2>
<p> A <code>gcj</code> command is like a <code>gcc</code> command, in that it consists of a number of options and file names. The following kinds of input file names are supported:</p>
<dl>
<dt><i>file</i><code>.java</code></p>
<dd> Java source files.</p>
<dt><i>file</i><code>.class</code></p>
<dd> Java bytecode files.</p>
<dt><i>file</i><code>.zip</code></p>
<dd>
<dt><i>file</i><code>.jar</code></p>
<dd> An archive containing one or more <tt>&quot;.class&quot;</tt> files, all of which are compiled. The archive may be compressed. Files in an archive which don&#8217;t end with <code>.class</code> are treated as resource files; they are compiled into the resulting object file as <code>core:</code> URLs.</p>
<dt><code>@</code><i>file</i></p>
<dd> A file containing a whitespace-separated list of input file names. (Currently, these must all be <tt>&quot;.java&quot;</tt> source files, but that may change.) Each named file is compiled, just as if it had been on the command line.</p>
<dt><i>library</i><code>.a</code></p>
<dd>
<dt><i>library</i><code>.so</code></p>
<dd>
<dt><code>-l</code><i>libname</i></p>
<dd> Libraries to use when linking. See the <code>gcc</code> manual.</dl>
<p> You can specify more than one input file on the <code>gcj</code> command line, in which case they will all be compiled. If you specify a <tt>&quot;-o </tt>FILENAME<tt>&quot;</tt> option, all the input files will be compiled together, producing a single output file, named <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>. This is allowed even when using <tt>&quot;-S&quot;</tt> or <tt>&quot;-c&quot;</tt>, but not when using <tt>&quot;-C&quot;</tt> or <tt>&quot;--resource&quot;</tt>. (This is an extension beyond the what plain <code>gcc</code> allows.) (If more than one input file is specified, all must currently be <tt>&quot;.java&quot;</tt> files, though we hope to fix this.)</p>
<h2>Input Options</h2>
<p> <code>gcj</code> has options to control where it looks to find files it needs. For instance, <code>gcj</code> might need to load a class that is referenced by the file it has been asked to compile. Like other compilers for the Java language, <code>gcj</code> has a notion of a <i>class path</i>. There are several options and environment variables which can be used to manipulate the class path. When <code>gcj</code> looks for a given class, it searches the class path looking for matching <i>.class</i> or <i>.java</i> file. <code>gcj</code> comes with a built-in class path which points at the installed <i>libgcj.jar</i>, a file which contains all the standard classes. </p>
<p> In the text below, a directory or path component can refer either to an actual directory on the filesystem, or to a <i>.zip</i> or <i>.jar</i> file, which <code>gcj</code> will search as if it is a directory.</p>
<dl>
<dt><code>-I</code><i>dir</i></p>
<dd> All directories specified by <tt>&quot;-I&quot;</tt> are kept in order and prepended to the class path constructed from all the other options. Unless compatibility with tools like <tt>&quot;javac&quot;</tt> is important, we recommend always using <tt>&quot;-I&quot;</tt> instead of the other options for manipulating the class path.</p>
<dt><code>&#8211;classpath=</code><i>path</i></p>
<dd> This sets the class path to <i>path</i>, a colon-separated list of paths (on Windows-based systems, a semicolon-separate list of paths). This does not override the builtin (&#8220;boot&#8221;) search path.</p>
<dt><code>&#8211;CLASSPATH=</code><i>path</i></p>
<dd> Deprecated synonym for <tt>&quot;--classpath&quot;</tt>.</p>
<dt><code>&#8211;bootclasspath=</code><i>path</i></p>
<dd> Where to find the standard builtin classes, such as <tt>&quot;java.lang.String&quot;</tt>.</p>
<dt><code>&#8211;extdirs=</code><i>path</i></p>
<dd> For each directory in the <i>path</i>, place the contents of that directory at the end of the class path.</p>
<dt><font SIZE="-1"><code>CLASSPATH</code></font></p>
<dd> This is an environment variable which holds a list of paths.</dl>
<p> The final class path is constructed like so:</p>
<dl>
<dt>*</p>
<dd> First come all directories specified via <tt>&quot;-I&quot;</tt>.</p>
<dt>*</p>
<dd> If <code>&#8211;classpath</code> is specified, its value is appended. Otherwise, if the <tt>&quot;CLASSPATH&quot;</tt> environment variable is specified, then its value is appended. Otherwise, the current directory (<tt>&quot;.&quot;</tt>) is appended.</p>
<dt>*</p>
<dd> If <tt>&quot;--bootclasspath&quot;</tt> was specified, append its value. Otherwise, append the built-in system directory, <i>libgcj.jar</i>.</p>
<dt>*</p>
<dd> Finally, if <tt>&quot;--extdirs&quot;</tt> was specified, append the contents of the specified directories at the end of the class path. Otherwise, append the contents of the built-in extdirs at <tt>&quot;$(prefix)/share/java/ext&quot;</tt>.</dl>
<p> The classfile built by <code>gcj</code> for the class <tt>&quot;java.lang.Object&quot;</tt> (and placed in <tt>&quot;libgcj.jar&quot;</tt>) contains a special zero length attribute <tt>&quot;gnu.gcj.gcj-compiled&quot;</tt>. The compiler looks for this attribute when loading <tt>&quot;java.lang.Object&quot;</tt> and will report an error if it isn&#8217;t found, unless it compiles to bytecode (the option <tt>&quot;-fforce-classes-archive-check&quot;</tt> can be used to override this behavior in this particular case.)</p>
<dl>
<dt><code>-fforce-classes-archive-check</code></p>
<dd> This forces the compiler to always check for the special zero length attribute <tt>&quot;gnu.gcj.gcj-compiled&quot;</tt> in <tt>&quot;java.lang.Object&quot;</tt> and issue an error if it isn&#8217;t found.</p>
<dt><code>-fsource=</code><i></i><font SIZE="-1"><i>VERSION</i></font><i></i></p>
<dd> This option is used to choose the source version accepted by <code>gcj</code>. The default is <code>1.5</code>.</dl>
<h2>Encodings</h2>
<p> The Java programming language uses Unicode throughout. In an effort to integrate well with other locales, <code>gcj</code> allows <i>.java</i> files to be written using almost any encoding. <code>gcj</code> knows how to convert these encodings into its internal encoding at compile time. </p>
<p> You can use the <tt>&quot;--encoding=</tt>NAME<tt>&quot;</tt> option to specify an encoding (of a particular character set) to use for source files. If this is not specified, the default encoding comes from your current locale. If your host system has insufficient locale support, then <code>gcj</code> assumes the default encoding to be the <font SIZE="-1"><code>UTF-8</code></font> encoding of Unicode. </p>
<p> To implement <tt>&quot;--encoding&quot;</tt>, <code>gcj</code> simply uses the host platform&#8217;s <tt>&quot;iconv&quot;</tt> conversion routine. This means that in practice <code>gcj</code> is limited by the capabilities of the host platform. </p>
<p> The names allowed for the argument <tt>&quot;--encoding&quot;</tt> vary from platform to platform (since they are not standardized anywhere). However, <code>gcj</code> implements the encoding named <font SIZE="-1"><code>UTF-8</code></font> internally, so if you choose to use this for your source files you can be assured that it will work on every host.</p>
<h2>Warnings</h2>
<p> <code>gcj</code> implements several warnings. As with other generic <code>gcc</code> warnings, if an option of the form <tt>&quot;-Wfoo&quot;</tt> enables a warning, then <tt>&quot;-Wno-foo&quot;</tt> will disable it. Here we&#8217;ve chosen to document the form of the warning which will have an effect &#8212; the default being the opposite of what is listed.</p>
<dl>
<dt><code>-Wredundant-modifiers</code></p>
<dd> With this flag, <code>gcj</code> will warn about redundant modifiers. For instance, it will warn if an interface method is declared <tt>&quot;public&quot;</tt>.</p>
<dt><code>-Wextraneous-semicolon</code></p>
<dd> This causes <code>gcj</code> to warn about empty statements. Empty statements have been deprecated.</p>
<dt><code>-Wno-out-of-date</code></p>
<dd> This option will cause <code>gcj</code> not to warn when a source file is newer than its matching class file. By default <code>gcj</code> will warn about this.</p>
<dt><code>-Wno-deprecated</code></p>
<dd> Warn if a deprecated class, method, or field is referred to.</p>
<dt><code>-Wunused</code></p>
<dd> This is the same as <code>gcc</code>&#8216;s <tt>&quot;-Wunused&quot;</tt>.</p>
<dt><code>-Wall</code></p>
<dd> This is the same as <tt>&quot;-Wredundant-modifiers -Wextraneous-semicolon -Wunused&quot;</tt>.</dl>
<h2>Linking</h2>
<p> To turn a Java application into an executable program, you need to link it with the needed libraries, just as for C or C<font SIZE="-2">++</font>. The linker by default looks for a global function named <tt>&quot;main&quot;</tt>. Since Java does not have global functions, and a collection of Java classes may have more than one class with a <tt>&quot;main&quot;</tt> method, you need to let the linker know which of those <tt>&quot;main&quot;</tt> methods it should invoke when starting the application. You can do that in any of these ways:</p>
<dl>
<dt>*</p>
<dd> Specify the class containing the desired <tt>&quot;main&quot;</tt> method when you link the application, using the <tt>&quot;--main&quot;</tt> flag, described below.</p>
<dt>*</p>
<dd> Link the Java package(s) into a shared library (dll) rather than an executable. Then invoke the application using the <tt>&quot;gij&quot;</tt> program, making sure that <tt>&quot;gij&quot;</tt> can find the libraries it needs.</p>
<dt>*</p>
<dd> Link the Java packages(s) with the flag <tt>&quot;-lgij&quot;</tt>, which links in the <tt>&quot;main&quot;</tt> routine from the <tt>&quot;gij&quot;</tt> command. This allows you to select the class whose <tt>&quot;main&quot;</tt> method you want to run when you run the application. You can also use other <tt>&quot;gij&quot;</tt> flags, such as <tt>&quot;-D&quot;</tt> flags to set properties. Using the <tt>&quot;-lgij&quot;</tt> library (rather than the <tt>&quot;gij&quot;</tt> program of the previous mechanism) has some advantages: it is compatible with static linking, and does not require configuring or installing libraries.</dl>
<p> These <tt>&quot;gij&quot;</tt> options relate to linking an executable:</p>
<dl>
<dt><code>&#8211;main=</code><i></i><font SIZE="-1"><i>CLASSNAME</i></font><i></i></p>
<dd> This option is used when linking to specify the name of the class whose <tt>&quot;main&quot;</tt> method should be invoked when the resulting executable is run.</p>
<dt><code>-D</code><i>name</i><code>[=</code><i>value</i><code>]</code></p>
<dd> This option can only be used with <tt>&quot;--main&quot;</tt>. It defines a system property named <i>name</i> with value <i>value</i>. If <i>value</i> is not specified then it defaults to the empty string. These system properties are initialized at the program&#8217;s startup and can be retrieved at runtime using the <tt>&quot;java.lang.System.getProperty&quot;</tt> method.</p>
<dt><code>-lgij</code></p>
<dd> Create an application whose command-line processing is that of the <tt>&quot;gij&quot;</tt> command. </p>
<p> This option is an alternative to using <tt>&quot;--main&quot;</tt>; you cannot use both.</p>
<dt><code>-static-libgcj</code></p>
<dd> This option causes linking to be done against a static version of the libgcj runtime library. This option is only available if corresponding linker support exists. </p>
<p> <code>Caution:</code> Static linking of libgcj may cause essential parts of libgcj to be omitted. Some parts of libgcj use reflection to load classes at runtime. Since the linker does not see these references at link time, it can omit the referred to classes. The result is usually (but not always) a <tt>&quot;ClassNotFoundException&quot;</tt> being thrown at runtime. Caution must be used when using this option. For more details see: &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/wiki/Statically%20linking%20libgcj">http://gcc.gnu.org/wiki/Statically%20linking%20libgcj</a></code>&gt;</dl>
<h2>Code Generation</h2>
<p> In addition to the many <code>gcc</code> options controlling code generation, <code>gcj</code> has several options specific to itself.</p>
<dl>
<dt><code>-C</code></p>
<dd> This option is used to tell <code>gcj</code> to generate bytecode (<i>.class</i> files) rather than object code.</p>
<dt><code>&#8211;resource</code> <i>resource-name</i></p>
<dd> This option is used to tell <code>gcj</code> to compile the contents of a given file to object code so it may be accessed at runtime with the core protocol handler as <code>core:/</code><i>resource-name</i>. Note that <i>resource-name</i> is the name of the resource as found at runtime; for instance, it could be used in a call to <tt>&quot;ResourceBundle.getBundle&quot;</tt>. The actual file name to be compiled this way must be specified separately.</p>
<dt><code>-ftarget=</code><i></i><font SIZE="-1"><i>VERSION</i></font><i></i></p>
<dd> This can be used with <code>-C</code> to choose the version of bytecode emitted by <code>gcj</code>. The default is <code>1.5</code>. When not generating bytecode, this option has no effect.</p>
<dt><code>-d</code> <i>directory</i></p>
<dd> When used with <tt>&quot;-C&quot;</tt>, this causes all generated <i>.class</i> files to be put in the appropriate subdirectory of <i>directory</i>. By default they will be put in subdirectories of the current working directory.</p>
<dt><code>-fno-bounds-check</code></p>
<dd> By default, <code>gcj</code> generates code which checks the bounds of all array indexing operations. With this option, these checks are omitted, which can improve performance for code that uses arrays extensively. Note that this can result in unpredictable behavior if the code in question actually does violate array bounds constraints. It is safe to use this option if you are sure that your code will never throw an <tt>&quot;ArrayIndexOutOfBoundsException&quot;</tt>.</p>
<dt><code>-fno-store-check</code></p>
<dd> Don&#8217;t generate array store checks. When storing objects into arrays, a runtime check is normally generated in order to ensure that the object is assignment compatible with the component type of the array (which may not be known at compile-time). With this option, these checks are omitted. This can improve performance for code which stores objects into arrays frequently. It is safe to use this option if you are sure your code will never throw an <tt>&quot;ArrayStoreException&quot;</tt>.</p>
<dt><code>-fjni</code></p>
<dd> With <code>gcj</code> there are two options for writing native methods: <font SIZE="-1">CNI</font> and <font SIZE="-1">JNI</font>. By default <code>gcj</code> assumes you are using <font SIZE="-1">CNI</font>. If you are compiling a class with native methods, and these methods are implemented using <font SIZE="-1">JNI</font>, then you must use <tt>&quot;-fjni&quot;</tt>. This option causes <code>gcj</code> to generate stubs which will invoke the underlying <font SIZE="-1">JNI</font> methods.</p>
<dt><code>-fno-assert</code></p>
<dd> Don&#8217;t recognize the <tt>&quot;assert&quot;</tt> keyword. This is for compatibility with older versions of the language specification.</p>
<dt><code>-fno-optimize-static-class-initialization</code></p>
<dd> When the optimization level is greater or equal to <tt>&quot;-O2&quot;</tt>, <code>gcj</code> will try to optimize the way calls into the runtime are made to initialize static classes upon their first use (this optimization isn&#8217;t carried out if <tt>&quot;-C&quot;</tt> was specified.) When compiling to native code, <tt>&quot;-fno-optimize-static-class-initialization&quot;</tt> will turn this optimization off, regardless of the optimization level in use.</p>
<dt><code>&#8211;disable-assertions[=</code><i>class-or-package</i><code>]</code></p>
<dd> Don&#8217;t include code for checking assertions in the compiled code. If <tt>&quot;=</tt>class-or-package<tt>&quot;</tt> is missing disables assertion code generation for all classes, unless overridden by a more specific <tt>&quot;--enable-assertions&quot;</tt> flag. If <i>class-or-package</i> is a class name, only disables generating assertion checks within the named class or its inner classes. If <i>class-or-package</i> is a package name, disables generating assertion checks within the named package or a subpackage. </p>
<p> By default, assertions are enabled when generating class files or when not optimizing, and disabled when generating optimized binaries.</p>
<dt><code>&#8211;enable-assertions[=</code><i>class-or-package</i><code>]</code></p>
<dd> Generates code to check assertions. The option is perhaps misnamed, as you still need to turn on assertion checking at run-time, and we don&#8217;t support any easy way to do that. So this flag isn&#8217;t very useful yet, except to partially override <tt>&quot;--disable-assertions&quot;</tt>.</p>
<dt><code>-findirect-dispatch</code></p>
<dd> <code>gcj</code> has a special binary compatibility <font SIZE="-1">ABI</font>, which is enabled by the <tt>&quot;-findirect-dispatch&quot;</tt> option. In this mode, the code generated by <code>gcj</code> honors the binary compatibility guarantees in the Java Language Specification, and the resulting object files do not need to be directly linked against their dependencies. Instead, all dependencies are looked up at runtime. This allows free mixing of interpreted and compiled code. </p>
<p> Note that, at present, <tt>&quot;-findirect-dispatch&quot;</tt> can only be used when compiling <i>.class</i> files. It will not work when compiling from source. <font SIZE="-1">CNI</font> also does not yet work with the binary compatibility <font SIZE="-1">ABI</font>. These restrictions will be lifted in some future release. </p>
<p> However, if you compile <font SIZE="-1">CNI</font> code with the standard <font SIZE="-1">ABI</font>, you can call it from code built with the binary compatibility <font SIZE="-1">ABI</font>.</p>
<dt><code>-fbootstrap-classes</code></p>
<dd> This option can be use to tell <tt>&quot;libgcj&quot;</tt> that the compiled classes should be loaded by the bootstrap loader, not the system class loader. By default, if you compile a class and link it into an executable, it will be treated as if it was loaded using the system class loader. This is convenient, as it means that things like <tt>&quot;Class.forName()&quot;</tt> will search <font SIZE="-1"><code>CLASSPATH</code></font> to find the desired class.</p>
<dt><code>-freduced-reflection</code></p>
<dd> This option causes the code generated by <code>gcj</code> to contain a reduced amount of the class meta-data used to support runtime reflection. The cost of this savings is the loss of the ability to use certain reflection capabilities of the standard Java runtime environment. When set all meta-data except for that which is needed to obtain correct runtime semantics is eliminated. </p>
<p> For code that does not use reflection (i.e. serialization, <font SIZE="-1">RMI</font>, <font SIZE="-1">CORBA</font> or call methods in the <tt>&quot;java.lang.reflect&quot;</tt> package), <tt>&quot;-freduced-reflection&quot;</tt> will result in proper operation with a savings in executable code size. </p>
<p> <font SIZE="-1">JNI</font> (<tt>&quot;-fjni&quot;</tt>) and the binary compatibility <font SIZE="-1">ABI</font> (<tt>&quot;-findirect-dispatch&quot;</tt>) do not work properly without full reflection meta-data. Because of this, it is an error to use these options with <tt>&quot;-freduced-reflection&quot;</tt>. </p>
<p> <code>Caution:</code> If there is no reflection meta-data, code that uses a <tt>&quot;SecurityManager&quot;</tt> may not work properly. Also calling <tt>&quot;Class.forName()&quot;</tt> may fail if the calling method has no reflection meta-data.</dl>
<h2>Configure-time Options</h2>
<p> Some <code>gcj</code> code generations options affect the resulting <font SIZE="-1">ABI</font>, and so can only be meaningfully given when <tt>&quot;libgcj&quot;</tt>, the runtime package, is configured. <tt>&quot;libgcj&quot;</tt> puts the appropriate options from this group into a <code>spec</code> file which is read by <code>gcj</code>. These options are listed here for completeness; if you are using <tt>&quot;libgcj&quot;</tt> then you won&#8217;t want to touch these options.</p>
<dl>
<dt><code>-fuse-boehm-gc</code></p>
<dd> This enables the use of the Boehm <font SIZE="-1">GC</font> bitmap marking code. In particular this causes <code>gcj</code> to put an object marking descriptor into each vtable.</p>
<dt><code>-fhash-synchronization</code></p>
<dd> By default, synchronization data (the data used for <tt>&quot;synchronize&quot;</tt>, <tt>&quot;wait&quot;</tt>, and <tt>&quot;notify&quot;</tt>) is pointed to by a word in each object. With this option <code>gcj</code> assumes that this information is stored in a hash table and not in the object itself.</p>
<dt><code>-fuse-divide-subroutine</code></p>
<dd> On some systems, a library routine is called to perform integer division. This is required to get exception handling correct when dividing by zero.</p>
<dt><code>-fcheck-references</code></p>
<dd> On some systems it&#8217;s necessary to insert inline checks whenever accessing an object via a reference. On other systems you won&#8217;t need this because null pointer accesses are caught automatically by the processor.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-gcjh/">gcjh</a></i>(1), <i><a href="/docs/linux/man/1-gjnih/">gjnih</a></i>(1), <i><a href="/docs/linux/man/1-gij/">gij</a></i>(1), <i><a href="/docs/linux/man/1-jcf-dump/">jcf-dump</a></i>(1), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), and the Info entries for <i>gcj</i> and <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, the Front-Cover Texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the man page <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7). </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre>
     A GNU Manual
</pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre>
     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
</pre>
<h2>Index</h2>
