---
title: "javac-java-1(1)"
name: "javac-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javac-java-1/"
description: "javac – Java programming language compiler"
---

<h2>Name</h2>
<p> javac &#8211; Java programming language compiler </p>
<h2>SYNOPSIS</h2>
<pre><code>
javac[options][sourcefiles][classes][@argfiles]
</code></pre>
<p> Arguments may be in any order. </p>
<dl>
<dt>
<dd>
<dl>
<dt>options</p>
<dd> Command-line options.</p>
<dt>sourcefiles</p>
<dd> One or more source files to be compiled (such as MyClass.java).</p>
<dt>classes</p>
<dd> One or more classes to be processed for annotations (such as MyPackage.MyClass).</p>
<dt>@argfiles</p>
<dd> One or more files that lists options and source files. The <i>-J</i> options are not allowed in these files.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>javac</code> tool reads class and interface definitions, written in the Java programming language, and compiles them into bytecode class files. It can also process annotations in Java source files and classes. </p>
<p> There are two ways to pass source code file names to <code>javac</code>: </p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> For a small number of source files, simply list the file names on the command line.</p>
<dt>o</p>
<dd> For a large number of source files, list the file names in a file, separated by blanks or line breaks. Then use the list file name on the <code>javac</code> command line, preceded by an <code>@</code> character.</dl>
</dl>
<p> Source code file names must have <i>.java</i> suffixes, class file names must have <i>.class</i> suffixes, and both source and class files must have root names that identify the class. For example, a class called <i>MyClass</i> would be written in a source file called <i>MyClass.java</i> and compiled into a bytecode class file called <i>MyClass.class</i>. </p>
<p> Inner class definitions produce additional class files. These class files have names combining the inner and outer class names, such as <i>MyClass$MyInnerClass.class</i>. </p>
<p> You should arrange source files in a directory tree that reflects their package tree. For example, if you keep all your source files in <code>/workspace</code>, the source code for <i>com.mysoft.mypack.MyClass</i> should be in <code>/workspace/com/mysoft/mypack/MyClass.java</code>. </p>
<p> By default, the compiler puts each class file in the same directory as its source file. You can specify a separate destination directory with <code>-d</code> (see Options, below). </p>
<h2>OPTIONS</h2>
<p> The compiler has a set of standard options that are supported on the current development environment and will be supported in future releases. An additional set of non-standard options are specific to the current virtual machine and compiler implementations and are subject to change in the future. Non-standard options begin with <code>-X</code>. </p>
<h3>Standard Options</h3>
<dl>
<dt>
<dd>
<dl>
<dt>-Akey[=value]</p>
<dd> Options to pass to annotation processors. These are not interpreted by javac directly, but are made available for use by individual processors. <i>key</i> should be one or more identifiers separated by &quot;.&quot;.</p>
<dt>-cp path or -classpath path</p>
<dd> Specify where to find user class files, and (optionally) annotation processors and source files. This class path overrides the user class path in the <code>CLASSPATH</code> environment variable. If neither <code>CLASSPATH</code>, <code>-cp</code> nor <code>-classpath</code> is specified, the user class path consists of the current directory. See Setting the Class Path for more details. </p>
<p> &gt;If the <code>-sourcepath</code> option is not specified, the user class path is also searched for source files. </p>
<p> If the <code>-processorpath</code> option is not specified, the class path is also searched for annotation processors.</p>
<dt>-Djava.ext.dirs=directories</p>
<dd> Override the location of installed extensions.</p>
<dt>-Djava.endorsed.dirs=directories</p>
<dd> Override the location of endorsed standards path.</p>
<dt>-d directory</p>
<dd> Set the destination directory for class files. The directory must already exist; <code>javac</code> will not create it. If a class is part of a package, <code>javac</code> puts the class file in a subdirectory reflecting the package name, creating directories as needed. For example, if you specify <code>-d /home/myclasses</code> and the class is called <i>com.mypackage.MyClass</i>, then the class file is called <i>/home/myclasses/com/mypackage/MyClass.class</i>. </p>
<p> If <code>-d</code> is not specified, <code>javac</code> puts each class files in the same directory as the source file from which it was generated. </p>
<p> <code>Note:</code> The directory specified by <code>-d</code> is not automatically added to your user class path.</p>
<dt>-deprecation</p>
<dd> Show a description of each use or override of a deprecated member or class. Without <code>-deprecation</code>, <code>javac</code> shows a summary of the source files that use or override deprecated members or classes. <code>-deprecation</code> is shorthand for <code>-Xlint:deprecation</code>.</p>
<dt>-encoding encoding</p>
<dd> Set the source file encoding name, such as <i>EUC-JP and UTF-8</i>. If <code>-encoding</code> is not specified, the platform default converter is used.</p>
<dt>-endorseddirs directories</p>
<dd> Override the location of endorsed standards path.</p>
<dt>-extdirs directories</p>
<dd> Overrides the location of the <i>ext</i> directory. The <i>directories</i> variable is a colon-separated list of directories. Each JAR archive in the specified directories is searched for class files. All JAR archives found are automatically part of the class path. </p>
<p> If you are cross-compiling (compiling classes against bootstrap and extension classes of a different Java platform implementation), this option specifies the directories that contain the extension classes. See Cross-Compilation Options for more information.</p>
<dt>-g</p>
<dd> Generate all debugging information, including local variables. By default, only line number and source file information is generated.</p>
<dt>-g:none</p>
<dd> Do not generate any debugging information.</p>
<dt>-g:{keyword list}</p>
<dd> Generate only some kinds of debugging information, specified by a comma separated list of keywords. Valid keywords are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>source</p>
<dd> Source file debugging information</p>
<dt>lines</p>
<dd> Line number debugging information</p>
<dt>vars</p>
<dd> Local variable debugging information</dl>
</dl>
<dt>-help</p>
<dd> Print a synopsis of standard options.</p>
<dt>-implicit:{class,none}</p>
<dd> Controls the generation of class files for implicitly loaded source files. To automatically generate class files, use <code>-implicit:class</code>. To suppress class file generation, use <code>-implicit:none</code>. If this option is not specified, the default is to automatically generate class files. In this case, the compiler will issue a warning if any such class files are generated when also doing annotation processing. The warning will not be issued if this option is set explicitly. See Searching For Types.</p>
<dt>-Joption</p>
<dd> Pass <i>option</i> to the <code>java</code> launcher called by <code>javac</code>. For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. It is a common convention for <code>-J</code> to pass options to the underlying VM executing applications written in Java. </p>
<p> <code>Note:</code> <code>CLASSPATH</code>, <code>-classpath</code>, <code>-bootclasspath</code>, and <code>-extdirs</code> do <i>not</i> specify the classes used to run <code>javac</code>. Fiddling with the implementation of the compiler in this way is usually pointless and always risky. If you do need to do this, use the <code>-J</code> option to pass through options to the underlying <code>java</code> launcher.</p>
<dt>-nowarn</p>
<dd> Disable warning messages. This has the same meaning as <code>-Xlint:none</code>.</p>
<dt>-proc: {none,only}</p>
<dd> Controls whether annotation processing and/or compilation is done. <code>-proc:none</code> means that compilation takes place without annotation processing. <code>-proc:only</code> means that only annotation processing is done, without any subsequent compilation.</p>
<dt>-processor class1[,class2,class3&#8230;]</p>
<dd> Names of the annotation processors to run. This bypasses the default discovery process.</p>
<dt>-processorpath path</p>
<dd> Specify where to find annotation processors; if this option is not used, the class path will be searched for processors.</p>
<dt>-s dir</p>
<dd> Specify the directory where to place generated source files. The directory must already exist; <code>javac</code> will not create it. If a class is part of a package, the compiler puts the source file in a subdirectory reflecting the package name, creating directories as needed. For example, if you specify <code>-s /home/mysrc</code> and the class is called <i>com.mypackage.MyClass</i>, then the source file will be placed in <i>/home/mysrc/com/mypackage/MyClass.java</i>.</p>
<dt>-source release</p>
<dd> Specifies the version of source code accepted. The following values for <i>release</i> are allowed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.3</p>
<dd> The compiler does <i>not</i> support assertions, generics, or other language features introduced after Java SE 1.3.</p>
<dt>1.4</p>
<dd> The compiler accepts code containing assertions, which were introduced in Java SE 1.4.</p>
<dt>1.5</p>
<dd> The compiler accepts code containing generics and other language features introduced in Java SE 5.</p>
<dt>5</p>
<dd> Synonym for 1.5.</p>
<dt>1.6</p>
<dd> No language changes were introduced in Java SE 6. However, encoding errors in source files are now reported as errors instead of warnings as in previous releases of Java SE.</p>
<dt>6</p>
<dd> Synonym for 1.6.</p>
<dt>1.7</p>
<dd> This is the default value. The compiler accepts code with features introduced in Java SE 7.</p>
<dt>7</p>
<dd> Synonym for 1.7.</dl>
</dl>
<dt>-sourcepath sourcepath</p>
<dd> Specify the source code path to search for class or interface definitions. As with the user class path, source path entries are separated by colons (<code>:</code>) and can be directories, JAR archives, or ZIP archives. If packages are used, the local path name within the directory or archive must reflect the package name. </p>
<p> <code>Note:</code> Classes found through the class path may be subject to automatic recompilation if their sources are also found. See Searching For Types.</p>
<dt>-verbose</p>
<dd> Verbose output. This includes information about each class loaded and each source file compiled.</p>
<dt>-version</p>
<dd> Print version information.</p>
<dt>-Werror</p>
<dd> Terminate compilation if warnings occur.</p>
<dt>-X</p>
<dd> Display information about non-standard options and exit.</dl>
</dl>
<h3>Cross-Compilation Options</h3>
<p> By default, classes are compiled against the bootstrap and extension classes of the platform that <code>javac</code> shipped with. But <code>javac</code> also supports <i>cross-compiling</i>, where classes are compiled against a bootstrap and extension classes of a different Java platform implementation. It is important to use <code>-bootclasspath</code> and <code>-extdirs</code> when cross-compiling; see Cross-Compilation Example below. </p>
<dl>
<dt>
<dd>
<dl>
<dt>-target version</p>
<dd> Generate class files that target a specified version of the VM. Class files will run on the specified target and on later versions, but not on earlier versions of the VM. Valid targets are <code>1.1</code>, <code>1.2</code>, <code>1.3</code>, <code>1.4</code>, <code>1.5</code> (also <code>5</code>), <code>1.6</code> (also <code>6</code>), and <code>1.7</code> (also <code>7</code>).</dl>
<p> The default for <code>-target</code> depends on the value of <code>-source</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> If -source is <code>not specified</code>, the value of -target is <code>1.7</code></p>
<dt>o</p>
<dd> If -source is <code>1.2</code>, the value of -target is <code>1.4</code></p>
<dt>o</p>
<dd> If -source is <code>1.3</code>, the value of -target is <code>1.4</code></p>
<dt>o</p>
<dd> If -source is <code>1.5</code>, the value of -target is <code>1.7</code></p>
<dt>o</p>
<dd> If -source is <code>1.6</code>, the value of -target is <code>1.7</code></p>
<dt>o</p>
<dd> For <code>all other values</code> of -source, the value of <code>-target</code> is the value of <code>-source</code>.</dl>
</dl>
<dl>
<dt>-bootclasspath bootclasspath</p>
<dd> Cross-compile against the specified set of boot classes. As with the user class path, boot class path entries are separated by colons (<code>:</code>) and can be directories, JAR archives, or ZIP archives.</dl>
</dl>
<h3>Non-Standard Options</h3>
<dl>
<dt>
<dd>
<dl>
<dt>-Xbootclasspath/p:path</p>
<dd> Prepend to the bootstrap class path.</p>
<dt>-Xbootclasspath/a:path</p>
<dd> Append to the bootstrap class path.</p>
<dt>-Xbootclasspath/:path</p>
<dd> Override location of bootstrap class files.</p>
<dt>-Xlint</p>
<dd> Enable all recommended warnings. In this release, enabling all available warnings is recommended.</p>
<dt>-Xlint:all</p>
<dd> Enable all recommended warnings. In this release, enabling all available warnings is recommended.</p>
<dt>-Xlint:none</p>
<dd> Disable all warnings.</p>
<dt>-Xlint:name</p>
<dd> Enable warning <i>name</i>. See the section Warnings That Can Be Enabled or Disabled with -Xlint Option for a list of warnings you can enable with this option.</p>
<dt>-Xlint:-name</p>
<dd> Disable warning <i>name</i>. See the section Warnings That Can Be Enabled or Disabled with -Xlint Option for a list of warnings you can disable with this option.</p>
<dt>-Xmaxerrs number</p>
<dd> Set the maximum number of errors to print.</p>
<dt>-Xmaxwarns number</p>
<dd> Set the maximum number of warnings to print.</p>
<dt>-Xstdout filename</p>
<dd> Send compiler messages to the named file. By default, compiler messages go to <i>System.err</i>.</p>
<dt>-Xprefer:{newer,source}</p>
<dd> Specify which file to read when both a source file and class file are found for a type. (See Searching For Types). If <i>-Xprefer:newer</i> is used, it reads the newer of the source or class file for a type (default). If the <i>-Xprefer:source</i> option is used, it reads source file. Use <i>-Xprefer:source</i> when you want to be sure that any annotation processors can access annotations declared with a retention policy of <i>SOURCE</i>.</p>
<dt>-Xpkginfo:{always,legacy,nonempty}</p>
<dd> Specify handling of package-info files</p>
<dt>-Xprint</p>
<dd> Print out textual representation of specified types for debugging purposes; perform neither annotation processing nor compilation. The format of the output may change.</p>
<dt>-XprintProcessorInfo</p>
<dd> Print information about which annotations a processor is asked to process.</p>
<dt>-XprintRounds</p>
<dd> Print information about initial and subsequent annotation processing rounds.</dl>
</dl>
<h3>Warnings That Can Be Enabled or Disabled with -Xlint Option</h3>
<p> Enable warning <i>name</i> with the option <code>-Xlint:</code><i>name</i>, where <i>name</i> is one of the following warning names. Similarly, you can disable warning <i>name</i> with the option <code>-Xlint:-</code><i>name</i>: </p>
<dl>
<dt>
<dd>
<dl>
<dt>cast</p>
<dd> Warn about unnecessary and redundant casts. For example: </p>
<pre>
<code>String s = (String)&quot;Hello!&quot;</code>
</pre>
<dt>classfile</p>
<dd> Warn about issues related to classfile contents.</p>
<dt>deprecation</p>
<dd> Warn about use of deprecated items. For example:<br />
java.util.Date myDate = new java.util.Date();<br />
int currentDay = myDate.getDay();<br />
 The method <i>java.util.Date.getDay</i> has been deprecated since JDK 1.1.</p>
<dt>dep-ann</p>
<dd> Warn about items that are documented with an <i>@deprecated</i> Javadoc comment, but do not have a <i>@Deprecated</i> annotation. For example:<br />
/**<br />
 * @deprecated As of Java SE 7, replaced by {@link #newMethod()}<br />
 */<br />
public<br />
static void deprecatedMethood()<br />
{<br />
}<br />
public<br />
static void newMethod()<br />
{<br />
}</p>
<dt>divzero</p>
<dd> Warn about division by constant integer 0. For example: </p>
<pre>
<code>    int divideByZero = 42 / 0;</code>
</pre>
<dt>empty</p>
<dd> Warn about empty statements after <i>if</i> statements. For example:<br />
class E<br />
{<br />
    void m()<br />
    {<br />
        if (true)<br />
            ;<br />
    }<br />
}</p>
<dt>fallthrough</p>
<dd> Check <i>switch</i> blocks for fall-through cases and provide a warning message for any that are found. Fall-through cases are cases in a <i>switch</i> block, other than the last case in the block, whose code does not include a <i>break</i> statement, allowing code execution to &quot;fall through&quot; from that case to the next case. For example, the code following the <i>case 1</i> label in this <i>switch</i> block does not end with a <i>break</i> statement:<br />
switch (x) {<br />
case 1:<br />
    System.out.println(&#8220;1&#8221;);<br />
    //  No break statement here.<br />
case 2:<br />
    System.out.println(&#8220;2&#8221;);<br />
}<br />
 If the <i>-Xlint:fallthrough</i> flag were used when compiling this code, the compiler would emit a warning about &quot;possible fall-through into case,&quot; along with the line number of the case in question.</p>
<dt>finally</p>
<dd> Warn about <i>finally</i> clauses that cannot complete normally. For example:<br />
public<br />
static int m()<br />
{<br />
    try {<br />
        throw new NullPointerException();<br />
    } catch (NullPointerException e) {<br />
        System.err.println(&#8220;Caught NullPointerException.&#8221;);<br />
        return 1;<br />
    } finally {<br />
        return 0;<br />
    }<br />
}<br />
 The compiler generates a warning for <i>finally</i> block in this example. When this method is called, it returns a value of <i>0</i>, not <i>1</i>. A <i>finally</i> block always executes when the <i>try</i> block exits. In this example, if control is transferred to the <i>catch</i>, then the method exits. However, the <i>finally</i> block must be executed, so it is executed, even though control has already been transferred outside the method.</p>
<dt>options</p>
<dd> Warn about issues relating to the use of command line options. See Cross-Compilation Example for an example of this kind of warning.</p>
<dt>overrides</p>
<dd> Warn about issues regarding method overrides. For example, consider the following two classes:<br />
public<br />
class ClassWithVarargsMethod<br />
{<br />
    void varargsMethod(String&#8230; s)<br />
    {<br />
    }<br />
}</p>
<p>public<br />
class ClassWithOverridingMethod extends ClassWithVarargsMethod<br />
{<br />
    @Override void varargsMethod(String[] s)<br />
    {<br />
    }<br />
}<br />
 The compiler generates a warning similar to the following: </p>
<p> <i>warning: [override] varargsMethod(String[]) in ClassWithOverridingMethod overrides varargsMethod(String&#8230;) in ClassWithVarargsMethod; overriding method is missing &#8216;&#8230;&#8217;</i> </p>
<p> When the compiler encounters a varargs method, it translates the varargs formal parameter into an array. In the method <i>ClassWithVarargsMethod.varargsMethod</i>, the compiler translates the varargs formal parameter <i>String&#8230; s</i> to the formal parameter <i>String[] s</i>, an array, which matches the formal parameter of the method <i>ClassWithOverridingMethod.varargsMethod</i>. Consequently, this example compiles.</p>
<dt>path</p>
<dd> Warn about invalid path elements and nonexistent path directories on the command line (with regards to the class path, the source path, and other paths). Such warnings cannot be suppressed with the <i>@SuppressWarnings</i> annotation. For example: </p>
<pre>
<code>javac -Xlint:path -classpath /nonexistentpath Example.java</code>
</pre>
<dt>processing</p>
<dd> Warn about issues regarding annotation processing. The compiler generates this warning if you have a class that has an annotation, and you use an annotation processor that cannot handle that type of exception. For example, the following is a simple annotation processor: </p>
<p> <code>Source file </code><tt>AnnoProc.java</tt>:<br />
import java.util.*;<br />
import javax.annotation.processing.*;<br />
import javax.lang.model.*;<br />
import javax.lang.model.element.*;<br />
@SupportedAnnotationTypes(&#8220;NotAnno&#8221;) public class AnnoProc extends AbstractProcessor<br />
{<br />
  public boolean process(Set&lt;? extends TypeElement&gt; elems, RoundEnvironment renv)<br />
    {<br />
        return true;<br />
    }<br />
  public<br />
    SourceVersion getSupportedSourceVersion()<br />
    {<br />
        return SourceVersion.latest();<br />
    }<br />
}<br />
 <code>Source file </code><tt>AnnosWithoutProcessors.java</tt><code>:</code><br />
@interface Anno {<br />
}<br />
@Anno class AnnosWithoutProcessors<br />
{<br />
}<br />
 The following commands compile the annotation processor <i>AnnoProc</i>, then run this annotation processor against the source file <i>AnnosWithoutProcessors.java</i>: </p>
<pre>
<code>% </code><code>javac AnnoProc.java</code>
% <code>javac -cp . -Xlint:processing -processor AnnoProc -proc:only AnnosWithoutProcessors.java</code>
</pre>
<p> When the compiler runs the annotation processor against the source file <i>AnnosWithoutProcessors.java</i>, it generates the following warning: </p>
<p> <i>warning: [processing] No processor claimed any of these annotations: Anno</i> </p>
<p> To resolve this issue, you can rename the annotation defined and used in the class <i>AnnosWithoutProcessors</i> from <i>Anno</i> to <i>NotAnno</i>.</p>
<dt>rawtypes</p>
<dd> Warn about unchecked operations on raw types. The following statement generates a <i>rawtypes</i> warning: </p>
<pre>
<code>void countElements(List l) { ... }</code>
</pre>
<p> The following does not generate a <i>rawtypes</i> warning: </p>
<pre>
<code>void countElements(List&lt;?&gt; l) { ... }</code>
</pre>
<p> <i>List</i> is a raw type. However, <i>List&lt;?&gt;</i> is a unbounded wildcard parameterized type. Because <i>List</i> is a parameterized interface, you should always specify its type argument. In this example, the <i>List</i> formal argument is specified with a unbounded wildcard (<i>?</i>) as its formal type parameter, which means that the <i>countElements</i> method can accept any instantiation of the <i>List</i> interface.</p>
<dt>serial</p>
<dd> Warn about missing <i>serialVersionUID</i> definitions on serializable classes. For example:<br />
public<br />
class PersistentTime implements Serializable<br />
{<br />
  private<br />
    Date time;<br />
  public<br />
    PersistentTime()<br />
    {<br />
        time = Calendar.getInstance().getTime();<br />
    }<br />
  public<br />
    Date getTime()<br />
    {<br />
        return time;<br />
    }<br />
}<br />
 The compiler generates the following warning: </p>
<p> <i>warning: [serial] serializable class PersistentTime has no definition of serialVersionUID</i> </p>
<p> If a serializable class does not explicitly declare a field named <i>serialVersionUID</i>, then the serialization runtime will calculate a default <i>serialVersionUID</i> value for that class based on various aspects of the class, as described in the Java Object Serialization Specification. However, it is strongly recommended that all serializable classes explicitly declare <i>serialVersionUID</i> values because the default process of computing <i>serialVersionUID</i> vales is highly sensitive to class details that may vary depending on compiler implementations, and can thus result in unexpected <i>InvalidClassExceptions</i> during deserialization. Therefore, to guarantee a consistent <i>serialVersionUID</i> value across different Java compiler implementations, a serializable class must declare an explicit <i>serialVersionUID</i> value.</p>
<dt>static</p>
<dd> Warn about issues relating to use of statics. For example:<br />
class XLintStatic<br />
{<br />
    static void m1()<br />
    {<br />
    }<br />
    void m2()<br />
    {<br />
        this.m1();<br />
    }<br />
}<br />
 The compiler generates the following warning:<br />
warning : [static] static method should be qualified by type name, XLintStatic, instead of by an expression<br />
 To resolve this issue, you can call the static method <i>m1</i> as follows: </p>
<pre>
<code>XLintStatic.m1();</code>
</pre>
<p> Alternatively, you can remove the <i>static</i> keyword from the declaration of the method <i>m1</i>.</p>
<dt>try</p>
<dd> Warn about issues relating to use of <i>try</i> blocks, including try-with-resources statements. For example, a warning is generated for the following statement because the resource <i>ac</i> declared in the <i>try</i> statement is not used: </p>
<pre>
<code>try ( AutoCloseable ac = getResource() ) {
    // do nothing
}</code>
</pre>
<dt>unchecked</p>
<dd> Give more detail for unchecked conversion warnings that are mandated by the Java Language Specification. For example: </p>
<pre>
<code>    List l = new ArrayList&lt;Number&gt;();
    List&lt;String&gt; ls = l;       // unchecked warning</code>
</pre>
<p> During type erasure, the types <i>ArrayList&lt;Number&gt;</i> and <i>List&lt;String&gt;</i> become <i>ArrayList</i> and <i>List</i>, respectively. </p>
<p> The variable <i>ls</i> has the parameterized type <i>List&lt;String&gt;</i>. When the <i>List</i> referenced by <i>l</i> is assigned to <i>ls</i>, the compiler generates an unchecked warning; the compiler is unable to determine at compile time, and moreover knows that the JVM will not be able to determine at runtime, if <i>l</i> refers to a <i>List&lt;String&gt;</i> type; it does not. Consequently, heap pollution occurs. </p>
<p> In detail, a heap pollution situation occurs when the <i>List</i> object <i>l</i>, whose static type is <i>List&lt;Number&gt;</i>, is assigned to another <i>List</i> object, <i>ls</i>, that has a different static type, <i>List&lt;String&gt;</i>. However, the compiler still allows this assignment. It must allow this assignment to preserve backwards compatibility with versions of Java SE that do not support generics. Because of type erasure, <i>List&lt;Number&gt;</i> and <i>List&lt;String&gt;</i> both become <i>List</i>. Consequently, the compiler allows the assignment of the object <i>l</i>, which has a raw type of <i>List</i>, to the object <i>ls</i>.</p>
<dt>varargs</p>
<dd> Warn about unsafe usages of variable arguments (varargs) methods, in particular, those that contain non-reifiable arguments. For example:<br />
public<br />
class ArrayBuilder<br />
{<br />
  public<br />
    static&lt;T&gt; void addToList(List&lt;T&gt; listArg, T&#8230; elements)<br />
    {<br />
        for (T x : elements) {<br />
            listArg.add(x);<br />
        }<br />
    }<br />
}<br />
 The compiler generates the following warning for the definition of the method <i>ArrayBuilder.addToList</i>: </p>
<pre>
<code>warning: [varargs] Possible heap pollution from parameterized vararg type T</code>
</pre>
<p> When the compiler encounters a varargs method, it translates the varargs formal parameter into an array. However, the Java programming language does not permit the creation of arrays of parameterized types. In the method <i>ArrayBuilder.addToList</i>, the compiler translates the varargs formal parameter <i>T&#8230; elements</i> to the formal parameter <i>T[] elements</i>, an array. However, because of type erasure, the compiler converts the varargs formal parameter to <i>Object[] elements</i>. Consequently, there is a possibility of heap pollution.</dl>
</dl>
<h2>COMMAND LINE ARGUMENT FILES</h2>
<p> To shorten or simplify the javac command line, you can specify one or more files that themselves contain arguments to the <i>javac</i> command (except <i>-J</i> options). This enables you to create javac commands of any length on any operating system. </p>
<p> An argument file can include javac options and source filenames in any combination. The arguments within a file can be space-separated or newline-separated. If a filename contains embedded spaces, put the whole filename in double quotes. </p>
<p> Filenames within an argument file are relative to the current directory, not the location of the argument file. Wildcards (*) are not allowed in these lists (such as for specifying <i>*.java</i>). Use of the &#8216;<i>@</i>&#8216; character to recursively interpret files is not supported. The <i>-J</i> options are not supported because they are passed to the launcher, which does not support argument files. </p>
<p> When executing javac, pass in the path and name of each argument file with the &#8216;<i>@</i>&#8216; leading character. When javac encounters an argument beginning with the character `<i>@</i>&#8216;, it expands the contents of that file into the argument list. </p>
<h3>Example &#8211; Single Arg File</h3>
<p> You could use a single argument file named &quot;<i>argfile</i>&quot; to hold all javac arguments: </p>
<pre>
<code>% </code><code>javac @argfile</code>
</pre>
<p> This argument file could contain the contents of both files shown in the next example. </p>
<h3>Example &#8211; Two Arg Files</h3>
<p> You can create two argument files &#8212; one for the javac options and the other for the source filenames: (Notice the following lists have no line-continuation characters.) </p>
<p> Create a file named &quot;<i>options</i>&quot; containing: </p>
<pre>
<code>     -d classes
     -g
     -sourcepath /java/pubs/ws/1.3/src/share/classes</code>
</pre>
<p> Create a file named &quot;<i>classes</i>&quot; containing: </p>
<pre>
<code>     MyClass1.java
     MyClass2.java
     MyClass3.java</code>
</pre>
<p> You would then run <code>javac</code> with: </p>
<pre>
<code>  % </code><code>javac @options @classes</code>
</pre>
<h3>Example &#8211; Arg Files with Paths</h3>
<p> The argument files can have paths, but any filenames inside the files are relative to the current working directory (not <i>path1</i> or <i>path2</i>): </p>
<pre>
<code>% </code><code>javac @path1/options @path2/classes</code>
</pre>
<h2>ANNOTATION PROCESSING</h2>
<p> <code>javac</code> provides direct support for annotation processing, superseding the need for the separate annotation processing tool, <code>apt</code>. </p>
<p> The API for annotation processors is defined in the <i>javax.annotation.processing</i> and <i>javax.lang.model</i> packages and subpackages. </p>
<h3>Overview of annotation processing</h3>
<p> Unless annotation processing is disabled with the <code>-proc:none</code> option, the compiler searches for any annotation processors that are available. The search path can be specified with the <code>-processorpath</code> option; if it is not given, the user class path is used. Processors are located by means of service provider-configuration files named <i>META-INF/services/javax.annotation.processing.Processor</i> on the search path. Such files should contain the names of any annotation processors to be used, listed one per line. Alternatively, processors can be specified explicitly, using the <code>-processor</code> option. </p>
<p> After scanning the source files and classes on the command line to determine what annotations are present, the compiler queries the processors to determine what annotations they process. When a match is found, the processor will be invoked. A processor may &quot;claim&quot; the annotations it processes, in which case no further attempt is made to find any processors for those annotations. Once all annotations have been claimed, the compiler does not look for additional processors. </p>
<p> If any processors generate any new source files, another round of annotation processing will occur: any newly generated source files will be scanned, and the annotations processed as before. Any processors invoked on previous rounds will also be invoked on all subsequent rounds. This continues until no new source files are generated. </p>
<p> After a round occurs where no new source files are generated, the annotation processors will be invoked one last time, to give them a chance to complete any work they may need to do. Finally, unless the <code>-proc:only</code> option is used, the compiler will compile the original and all the generated source files. </p>
<h3>Implicitly loaded source files</h3>
<p> To compile a set of source files, the compiler may need to implicitly load additional source files. (See Searching For Types). Such files are currently not subject to annotation processing. By default, the compiler will give a warning if annotation processing has occurred and any implicitly loaded source files are compiled. See the -implicit option for ways to suppress the warning. </p>
<h2>SEARCHING FOR TYPES</h2>
<p> When compiling a source file, the compiler often needs information about a type whose definition did not appear in the source files given on the command line. The compiler needs type information for every class or interface used, extended, or implemented in the source file. This includes classes and interfaces not explicitly mentioned in the source file but which provide information through inheritance. </p>
<p> For example, when you subclass <code>java.applet.Applet</code>, you are also using <code>Applet&#8217;s</code> ancestor classes: <code>java.awt.Panel</code>, <code>java.awt.Container</code>, <code>java.awt.Component</code>, and <code>java.lang.Object</code>. </p>
<p> When the compiler needs type information, it looks for a source file or class file which defines the type. The compiler searches for class files first in the bootstrap and extension classes, then in the user class path (which by default is the current directory). The user class path is defined by setting the <code>CLASSPATH</code> environment variable or by using the <code>-classpath</code> command line option. (For details, see Setting the Class Path). </p>
<p> If you set the -sourcepath option, the compiler searches the indicated path for source files; otherwise the compiler searches the user class path for both class files and source files. </p>
<p> You can specify different bootstrap or extension classes with the <code>-bootclasspath</code> and <code>-extdirs</code> options; see Cross-Compilation Options below. </p>
<p> A successful type search may produce a class file, a source file, or both. If both are found, you can use the -Xprefer option to instruct the compiler which to use. If <code>newer</code> is given, the compiler will use the newer of the two files. If <code>source</code> is given, it will use the source file. The default is <code>newer</code>. </p>
<p> If a type search finds a source file for a required type, either by itself, or as a result of the setting for <code>-Xprefer</code>, the compiler will read the source file to get the information it needs. In addition, it will by default compile the source file as well. You can use the -implicit option to specify the behavior. If <code>none</code> is given, no class files will be generated for the source file. If <code>class</code> is given, class files will be generated for the source file. </p>
<p> The compiler may not discover the need for some type information until after annotation processing is complete. If the type information is found in a source file and no <code>-implicit</code> option is given, the compiler will give a warning that the file is being compiled without being subject to annotation processing. To disable the warning, either specify the file on the command line (so that it will be subject to annotation processing) or use the <code>-implicit</code> option to specify whether or not class files should be generated for such source files. </p>
<h2>PROGRAMMATIC INTERFACE</h2>
<p> <code>javac</code> supports the new Java Compiler API defined by the classes and interfaces in the <i>javax.tools</i> package. </p>
<h3>Example</h3>
<p> To perform a compilation using arguments as you would give on the command line, you can use the following: </p>
<p>JavaCompiler javac = ToolProvider.getSystemJavaCompiler();<br />
int rc = javac.run(null, null, null, args);</p>
<p> This will write any diagnostics to the standard output stream, and return the exit code that <code>javac</code> would give when invoked from the command line. </p>
<p> You can use other methods on the <i>javax.tools.JavaCompiler</i> interface to handle diagnostics, control where files are read from and written to, and so on. </p>
<h3>Old Interface</h3>
<p> <code>Note:</code> This API is retained for backwards compatibility only; all new code should use the Java Compiler API, described above. </p>
<p> The <i>com.sun.tools.javac.Main</i> class provides two static methods to invoke the compiler from a program: </p>
<p>public<br />
static int compile(String[] args);<br />
public<br />
static int compile(String[] args, PrintWriter out);</p>
<p> The <i>args</i> parameter represents any of the command line arguments that would normally be passed to the javac program and are outlined in the above Synopsis section. </p>
<p> The <i>out</i> parameter indicates where the compiler&#8217;s diagnostic output is directed. </p>
<p> The return value is equivalent to the exit value from <code>javac</code>. </p>
<p> Note that all <code>other</code> classes and methods found in a package whose name starts with <i>com.sun.tools.javac</i> (informally known as sub-packages of <i>com.sun.tools.javac</i>) are strictly internal and subject to change at any time. </p>
<h2>EXAMPLES</h2>
<h3>Compiling a Simple Program</h3>
<p> One source file, <i>Hello.java</i>, defines a class called <code>greetings.Hello</code>. The <i>greetings</i> directory is the package directory both for the source file and the class file and is off the current directory. This allows us to use the default user class path. It also makes it unnecessary to specify a separate destination directory with <code>-d</code>. </p>
<pre><code>
% ls greetings /
    % ls greetings Hello.java % cat greetings / Hello.java package greetings;
public
class Hello
{
  public
    static void main(String[] args)
    {
        for (int i = 0; i &lt; args.length; i++) {
            System.out.println("Hello " + args[i]);
        }
    }
} % javac greetings / Hello.java % ls greetings Hello.class Hello.java % java greetings.Hello World Universe Everyone Hello World Hello Universe Hello Everyone
</code></pre>
<h3>Compiling Multiple Source Files</h3>
<p> This example compiles all the source files in the package <i>greetings</i>. </p>
<pre>
<code>% </code><code>ls</code>
greetings/
% <code>ls greetings</code>
Aloha.java         GutenTag.java      Hello.java         Hi.java
% <code>javac greetings/*.java</code>
% <code>ls greetings</code>
Aloha.class         GutenTag.class      Hello.class         Hi.class
Aloha.java          GutenTag.java       Hello.java          Hi.java
</pre>
<h3>Specifying a User Class Path</h3>
<p> Having changed one of the source files in the previous example, we recompile it: </p>
<pre>
<code>% </code><code>pwd</code>
/examples
% <code>javac greetings/Hi.java</code>
</pre>
<p> Since <i>greetings.Hi</i> refers to other classes in the <i>greetings</i> package, the compiler needs to find these other classes. The example above works, because our default user class path happens to be the directory containing the package directory. But suppose we want to recompile this file and not worry about which directory we&#8217;re in? Then we need to add <i>/examples</i> to the user class path. We can do this by setting <code>CLASSPATH</code>, but here we&#8217;ll use the <code>-classpath</code> option. </p>
<pre>
<code>% </code><code>javac -classpath /examples /examples/greetings/Hi.java</code>
</pre>
<p> If we change <i>greetings.Hi</i> again, to use a banner utility, that utility also needs to be accessible through the user class path. </p>
<pre>
<code>% </code><code>javac -classpath /examples:/lib/Banners.jar \ 
            /examples/greetings/Hi.java</code>
</pre>
<p> To execute a class in <i>greetings</i>, we need access both to <i>greetings</i> and to the classes it uses. </p>
<pre>
<code>% </code><code>java -classpath /examples:/lib/Banners.jar greetings.Hi</code>
</pre>
<h3>Separating Source Files and Class Files</h3>
<p> It often makes sense to keep source files and class files in separate directories, especially on large projects. We use <code>-d</code> to indicate the separate class file destination. Since the source files are not in the user class path, we use <code>-sourcepath</code> to help the compiler find them. </p>
<pre>
<code>% </code><code>ls</code>
classes/  lib/      src/
% <code>ls src</code>
farewells/
% <code>ls src/farewells</code>
Base.java      GoodBye.java
% <code>ls lib</code>
Banners.jar
% <code>ls classes</code>
% <code>javac -sourcepath src -classpath classes:lib/Banners.jar \ 
            src/farewells/GoodBye.java -d classes</code>
% <code>ls classes</code>
farewells/
% <code>ls classes/farewells</code>
Base.class      GoodBye.class
</pre>
<p> <code>Note:</code> The compiler compiled <i>src/farewells/Base.java</i>, even though we didn&#8217;t specify it on the command line. To trace automatic compiles, use the <code>-verbose</code> option. </p>
<h3>Cross-Compilation Example</h3>
<p> The following example uses <code>javac</code> to compile code that will run on a 1.6 VM. </p>
<pre>
<code>% </code><code>javac -source 1.6 -target 1.6 -bootclasspath jdk1.6.0/lib/rt.jar \ 
            -extdirs &quot;&quot; OldCode.java</code>
</pre>
<p> The <i>-source 1.6</i> option specifies that version 1.6 (or 6) of the Java programming language be used to compile <i>OldCode.java</i>. The option <code>-target 1.6</code> option ensures that the generated class files will be compatible with 1.6 VMs. Note that in most cases, the value of the <code>-target</code> option is the value of the <code>-source</code> option; in this example, you can omit the <code>-target</code> option. </p>
<p> You must specify the <code>-bootclasspath</code> option to specify the correct version of the bootstrap classes (the <i>rt.jar</i> library). If not, the compiler generates a warning: </p>
<pre>
<code>% </code><code>javac -source 1.6 OldCode.java</code>
warning: [options] bootstrap class path not set in conjunction with -source 1.6
</pre>
<p> If you do not specify the correct version of bootstrap classes, the compiler will use the old language rules (in this example, it will use version 1.6 of the Java programming language) combined with the new bootstrap classes, which can result in class files that do not work on the older platform (in this case, Java SE 6) because reference to non-existent methods can get included. </p>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>The javac Guide</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/javac/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/javac/index.html</a></p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-java/">java</a>(1) &#8211; the Java Application Launcher</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jdb/">jdb</a>(1) &#8211; Java Application Debugger</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-javah/">javah</a>(1) &#8211; C Header and Stub File Generator</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-javap/">javap</a>(1) &#8211; Class File Disassembler</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-javadoc/">javadoc</a>(1) &#8211; API Documentation Generator</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jar/">jar</a>(1) &#8211; JAR Archive Tool</p>
<dt>o</p>
<dd> <i>The Java Extensions Framework</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/extensions/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/extensions/index.html</a></dl>
</dl>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
