---
title: "idlj-java-1-6-0-openjdk(1)"
name: "idlj-java-1-6-0-openjdk"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idlj-java-1-6-0-openjdk/"
description: "idlj – The IDL-to-Java Compiler"
---

<p>idlj &#8211; The IDL-to-Java Compiler </p>
<dl>
<dd><code>idlj</code> generates Java bindings from a given IDL file.</dl>
<h2>Synopsis</h2>
<pre><code>idlj [ </code><code>options</code><code> ] </code><tt>idl-file</tt></pre>
<p>where <i>idl-file</i> is the name of a file containing Interface Definition Language (IDL) definitions. <i>Options</i> may appear in any order, but must precede the <i>idl-file</i>. </p>
<h2>Description</h2>
<p>The IDL-to-Java Compiler generates the Java bindings for a given IDL file.&nbsp;<wbr> For binding details, see the OMG IDL to Java Language Language Mapping Specification. Some previous releases of the IDL-to-Java compiler were named <i>idltojava</i>.</p>
<h3>Emitting Client and Server Bindings</h3>
<dl>
<dd>To generate Java bindings for an IDL file named My.idl: <i>idlj My.idl</i> </p>
<p> This generates the client-side bindings and is equivalent to: <i>idlj </i><tt>-fclient</tt><i> My.idl</i> </p>
<p> The client-side bindings do not include the server-side skeleton. If you want to generate the server-side bindings for the interfaces: <i>idlj </i><tt>-fserver</tt><i> My.idl</i> </p>
<p> Server-side bindings include the client-side bindings plus the skeleton, all of which are <i>POA</i> (that is, Inheritance Model) classes. If you want to generate both client and server-side bindings, use one of the following (equivalent) commands: <i>idlj </i><tt>-fclient -fserver</tt><i> My.idl</i><br />
 <i>idlj </i><tt>-fall</tt><i> My.idl</i> </p>
<p> There are two possible server-side models: the Inheritance Model and the Tie Delegation Model. </p>
<p> The default server-side model is the <i>Portable Servant Inheritance Model</i>. Given an interface <i>My</i> defined in <i>My.idl</i>, the file <i>MyPOA.java</i> is generated. You must provide the implementation for <i>My</i> and it must inherit from <i>MyPOA</i>. </p>
<p> <i>MyPOA.java</i> is a stream-based skeleton that extends <i>org.omg.PortableServer.Servant</i> and implements the <i>InvokeHandler</i> interface and the operations interface associated with the IDL interface the skeleton implements. </p>
<p> The <i>PortableServer</i> module for the Portable Object Adapter (POA) defines the native <i>Servant</i> type. In the Java programming language, the <i>Servant</i> type is mapped to the Java <i>org.omg.PortableServer.Servant</i> class. It serves as the base class for all POA servant implementations and provides a number of methods that may be invoked by the application programmer, as well as methods which are invoked by the POA itself and may be overridden by the user to control aspects of servant behavior. </p>
<p> Another option for the Inheritance Model is to use the <i>-oldImplBase</i> flag in order to generate server-side bindings that are compatible with versions of the Java programming language prior to J2SE 1.4. Note that using the <i>-oldImplBase</i> flag is non-standard: these APIs are being deprecated. You would use this flag ONLY for compatibility with existing servers written in J2SE 1.3. In that case, you would need to modify an existing MAKEFILE to add the <i>-oldImplBase</i> flag to the <i>idlj</i> compiler, otherwise POA-based server-side mappings will be generated. To generate server-side bindings that are backwards compatible: </p>
<p> <i>idlj </i><tt>-fclient -fserver</tt><i> </i><tt>-oldImplBase</tt><i> My.idl</i><br />
 <i>idlj </i><tt>-fall</tt><i> </i><tt>-oldImplBase</tt><i> My.idl</i> </p>
<p> Given an interface <i>My</i> defined in <i>My.idl</i>, the file <i>_MyImplBase.java</i> is generated. You must provide the implementation for <i>My</i> and it must inherit from <i>_MyImplBase</i>. </p>
<p> The other server-side model is called the Tie Model. This is a delegation model. Because it is not possible to generate ties and skeletons at the same time, they must be generated separately. The following commands generate the bindings for the Tie Model: </p>
<p> <i>idlj </i><tt>-fall</tt><i> My.idl</i><br />
 <i>idlj </i><tt>-fallTIE</tt><i> My.idl</i> </p>
<p> For the interface <i>My</i>, the second command generates <i>MyPOATie.java</i>. The constructor to <i>MyPOATie</i> takes a <i>delegate</i>. In this example, using the default POA model, the constructor also needs a <i>poa</i>. You must provide the implementation for <i>delegate</i>, but it does not have to inherit from any other class, only the interface <i>MyOperations</i>. But to use it with the ORB, you must wrap your implementation within <i>MyPOATie</i>. For instance: </p>
<pre><code> ORB orb = ORB.init(args, System.getProperties());
 // Get reference to rootpoa &amp; activate the POAManager
 POA rootpoa = (POA)orb.resolve_initial_references(&quot;RootPOA&quot;);
 rootpoa.the_POAManager().activate();
 // create servant and register it with the ORB
 MyServant myDelegate = new MyServant();
 myDelegate.setORB(orb); 
 // create a tie, with servant being the delegate.
 MyPOATie tie = new MyPOATie(myDelegate, rootpoa);
 // obtain the objectRef for the tie
 My ref = tie._this(orb);</code></pre>
<p>You might want to use the Tie model instead of the typical Inheritance model if your implementation must inherit from some other implementation. Java allows any number of interface inheritance, but there is only one slot for class inheritance. If you use the inheritance model, that slot is used up . By using the Tie Model, that slot is freed up for your own use. The drawback is that it introduces a level of indirection: one extra method call occurs when invoking a method. </p>
<p> To generate server-side, Tie model bindings that are compatible with versions of the IDL to Java language mapping in versions prior to J2SE 1.4. </p>
<p> <i>idlj </i><tt>-oldImplBase</tt><i> </i><tt>-fall</tt><i> My.idl</i><br />
 <i>idlj </i><tt>-oldImplBase</tt><i> </i><tt>-fallTIE</tt><i> My.idl</i> </p>
<p> For the interface <i>My</i>, this will generate <i>My_Tie.java</i>. The constructor to <i>My_Tie</i> takes a <i>impl</i>. You must provide the implementation for <i>impl</i>, but it does not have to inherit from any other class, only the interface <i>HelloOperations</i>. But to use it with the ORB, you must wrap your implementation within <i>My_Tie</i>. For instance: </p>
<pre><code> ORB orb = ORB.init(args, System.getProperties());
 // create servant and register it with the ORB
 MyServant myDelegate = new MyServant();
 myDelegate.setORB(orb); 
 // create a tie, with servant being the delegate.
 MyPOATie tie = new MyPOATie(myDelegate);
 // obtain the objectRef for the tie
 My ref = tie._this(orb);</code></pre>
</dl>
<h3>Specifying Alternate Locations for Emitted Files</h3>
<dl>
<dd>If you want to direct the emitted files to a directory other than the current directory, invoke the compiler as:</p>
<dl>
<dd><i>idlj </i><tt>-td /altdir</tt><i> My.idl</i></dl>
<p> For the interface <i>My</i>, the bindings will be emitted to <i>/altdir/My.java</i>, etc., instead of <i>./My.java</i>.</dl>
<h3>Specifying Alternate Locations for Include Files</h3>
<dl>
<dd>If <i>My.idl</i> included another idl file, <i>MyOther.idl</i>, the compiler assumes that <i>MyOther.idl</i> resides in the local directory. If it resides in <i>/includes</i>, for example, then you would invoke the compiler with the following command: <i>idlj </i><tt>-i /includes</tt><i> My.idl</i> </p>
<p> If <i>My.idl</i> also included <i>Another.idl</i> that resided in <i>/moreIncludes</i>, for example, then you would invoke the compiler with the following command: <i>idlj </i><tt>-i /includes -i /moreIncludes</tt><i> My.idl</i> </p>
<p> Since this form of include can become irritatingly long, another means of indicating to the compiler where to search for included files is provided. This technique is similar to the idea of an environment variable. Create a file named <i>idl.config</i> in a directory that is listed in your CLASSPATH. Inside of <i>idl.config</i>, provide a line with the following form: <i>includes=/includes;/moreIncludes</i> </p>
<p> The compiler will find this file and read in the includes list. Note that in this example the separator character between the two directories is a semicolon (;). This separator character is platform dependent. On the Windows platform, use a semicolon, on the Unix platform, use a colon, etc. For more information on <i>includes</i>, read the CLASSPATH&nbsp;<wbr>(Solaris) or CLASSPATH&nbsp;<wbr>(Windows) documentation.</dl>
<h3>Emitting Bindings for Include Files</h3>
<dl>
<dd>By default, only those interfaces, structs, etc, that are defined in the idl file on the command line have Java bindings generated for them. The types defined in included files are not generated. For example, assume the following two idl files: <tt>My.idl</tt> </p>
<p> <i>#include &lt;MyOther.idl&gt;</i><br />
 <i>interface My</i><br />
 <i>{</i><br />
 <i>};</i><br />
 <tt>MyOther.idl</tt> </p>
<p> <i>interface MyOther</i><br />
 <i>{</i><br />
 <i>};</i>&nbsp;<wbr> </p>
<p> The following command will only generate the java bindings for <i>My</i>: <i>idlj My.idl</i> </p>
<p> To generate all of the types in <i>My.idl</i> and all of the types in the files that <i>My.idl</i> includes (in this example, <i>MyOther.idl</i>), use the following command: <i>idlj </i><tt>-emitAll</tt><i> My.idl</i> </p>
<p> There is a caveat to the default rule. <i>#include</i> statements which appear at global scope are treated as described. These <i>#include</i> statements can be thought of as import statements. <i>#include</i> statements which appear within some enclosing scope are treated as true <i>#include</i> statements, meaning that the code within the included file is treated as if it appeared in the original file and, therefore, Java bindings are emitted for it. Here is an example: <tt>My.idl</tt> </p>
<p> <i>#include &lt;MyOther.idl&gt;</i><br />
 <i>interface My</i><br />
 <i>{</i><br />
 <i>&nbsp;<wbr> #include &lt;Embedded.idl&gt;</i><br />
 <i>};&nbsp;<wbr></i> <tt>MyOther.idl</tt> </p>
<p> <i>interface MyOther</i><br />
 <i>{</i><br />
 <i>};&nbsp;<wbr></i> <tt>Embedded.idl</tt> </p>
<p> <i>enum E {one, two, three};</i>&nbsp;<wbr> </p>
<p> Running the following command: <i>idlj My.idl</i> </p>
<p> will generate the following list of Java files: <i>./MyHolder.java</i><br />
 <i>./MyHelper.java</i><br />
 <i>./_MyStub.java</i><br />
 <i>./MyPackage</i><br />
 <i>./MyPackage/EHolder.java</i><br />
 <i>./MyPackage/EHelper.java</i><br />
 <i>./MyPackage/E.java</i><br />
 <i>./My.java</i> </p>
<p> Notice that <i>MyOther.java</i> was not generated because it is defined in an import-like <i>#include</i>. But <i>E.java</i> <i>was</i> generated because it was defined in a true <i>#include</i>. Also notice that since <i>Embedded.idl</i> was included within the scope of the interface <i>My</i>, it appears within the scope of <i>My</i> (that is,in <i>MyPackage</i>). </p>
<p> If the <i>-emitAll</i> flag had been used in the previous example, then all types in all included files would be emitted. </p>
</dl>
<h3>Inserting Package Prefixes</h3>
<dl>
<dd>Suppose that you work for a company named ABC that has constructed the following IDL file:<br />
 <tt>Widgets.idl</tt> </p>
<p> <i>module Widgets</i><br />
 <i>{</i><br />
 <i>&nbsp;<wbr> interface W1 {&#8230;};</i><br />
 <i>&nbsp;<wbr> interface W2 {&#8230;};</i><br />
 <i>};</i>&nbsp;<wbr> </p>
<p> Running this file through the IDL-to-Java compiler will place the Java bindings for <i>W1</i> and <i>W2</i> within the package <i>Widgets</i>. But there is an industry convention that states that a company&#8217;s packages should reside within a package named <i>com.&lt;company name&gt;</i>. The <i>Widgets</i> package is not good enough. To follow convention, it should be <i>com.abc.Widgets</i>. To place this package prefix onto the <i>Widgets</i> module, execute the following: <i>idlj </i><tt>-pkgPrefix Widgets com.abc</tt><i> Widgets.idl</i> </p>
<p> If you have an IDL file which includes <i>Widgets.idl</i>, the <i>-pkgPrefix</i> flag must appear in that command also. If it does not, then your IDL file will be looking for a <i>Widgets</i> package rather than a <i>com.abc.Widgets</i> package. </p>
<p> If you have a number of these packages that require prefixes, it might be easier to place them into the <i>idl.config</i> file described above. Each package prefix line should be of the form: </p>
<p> <i>PkgPrefix.&lt;type&gt;=&lt;prefix&gt;</i> </p>
<p> So the line for the above example would be: <i>PkgPrefix.Widgets=com.abc</i> </p>
<p> The use of this option does not affect the Repository ID. </p>
</dl>
<h3>Defining Symbols Before Compilation</h3>
<dl>
<dd>You may need to define a symbol for compilation that is not defined within the IDL file, perhaps to include debugging code in the bindings. The command <i>idlj </i><tt>-d</tt><i> MYDEF My.idl</i> </p>
<p> is the equivalent of putting the line <i>#define MYDEF</i> inside <i>My.idl</i>.</dl>
<h3>Preserving Pre-Existing Bindings</h3>
<dl>
<dd>If the Java binding files already exist, the <i>-keep</i> flag will keep the compiler from overwriting them. The default is to generate all files without considering if they already exist. If you&#8217;ve customized those files (which you should not do unless you are very comfortable with their contents), then the <i>-keep</i> option is very useful. The command <i>idlj </i><tt>-keep</tt><i> My.idl</i> </p>
<p> emit all client-side bindings that do not already exist.</dl>
<h3>Viewing Progress of Compilation</h3>
<dl>
<dd>The IDL-to-Java compiler will generate status messages as it progresses through its phases of execution. Use the <i>-v</i> option to activate this &quot;verbose&quot; mode: <i>idlj </i><tt>-v</tt><i> My.idl</i> </p>
<p> By default the compiler does not operate in verbose mode.</dl>
<h3>Displaying Version Information</h3>
<dl>
<dd>To display the build version of the IDL-to-Java compiler, specify the <i>-version</i> option on the command-line: </p>
<p> <i>idlj -version</i> </p>
<p> Version information also appears within the bindings generated by the compiler. Any additional options appearing on the command-line are ignored. </p>
</dl>
<h2>Options</h2>
<dl>
<dd>
<dl>
<dt>-d symbol</p>
<dd>This is equivalent to the following line in an IDL file:</p>
<dl>
<dd>
<pre><code>#define </code><tt>symbol</tt></pre>
</dl>
<dt>-emitAll</p>
<dd>Emit all types, including those found in <i>#include</i> files.</p>
<dt>-fside</p>
<dd>Defines what bindings to emit. <i>side</i> is one of <i>client</i>, <i>server</i>, <i>serverTIE</i>, <i>all</i>, or <i>allTIE</i>. The <i>-fserverTIE</i> and <i>-fallTIE</i> options cause delegate model skeletons to be emitted. Assumes <i>-fclient</i> if the flag is not specified.</p>
<dt>-i include-path</p>
<dd>By default, the current directory is scanned for included files. This option adds another directory.</p>
<dt>-keep</p>
<dd>If a file to be generated already exists, do not overwrite it. By default it is overwritten.</p>
<dt>-noWarn</p>
<dd>Suppresses warning messages.</p>
<dt>-oldImplBase</p>
<dd>Generates skeletons compatible with pre-1.4 JDK ORBs. By default, the POA Inheritance Model server-side bindings are generated. This option provides backward-compatibility with older versions of the Java programming language by generating server-side bindings that are <i>ImplBase</i> Inheritance Model classes.</p>
<dt>-pkgPrefix type prefix</p>
<dd>Wherever <i>type</i> is encountered at file scope, prefix the generated Java package name with <i>prefix</i> for all files generated for that type. The <i>type</i> is the simple name of either a top-level module, or an IDL type defined outside of any module.</p>
<dt>-pkgTranslate type package</p>
<dd>Whenever the module name <i>type</i> is encountered in an identifier, replace it in the identifier with <i>package</i> for all files in the generated Java package. Note that <i>pkgPrefix</i> changes are made first. <i>type</i> is the simple name of either a top-level module, or an IDL type defined outside of any module, and must match the full package name exactly.</dl>
<p> If more than one translation matches an identifier, the longest match is chosen. For example, if the arguments include: </p>
<pre><code> -pkgTranslate foo bar -pkgTranslate foo.baz buzz.fizz</code></pre>
<p>The following translations would occur: </p>
<pre><code>foo =&gt; bar
foo.boo =&gt; bar.boo
foo.baz =&gt; buzz.fizz
foo.baz.bar =&gt; buzz.fizz.bar</code></pre>
<p>The following package names cannot be translated:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>org</i></p>
<dt>o</p>
<dd><i>org.omg</i> or any subpackages of <i>org.omg</i></dl>
</dl>
<p> Any attempt to translate these packages will result in uncompilable code, and the use of these packages as the first argument after <i>-pkgTranslate</i> will be treated as an error.</p>
<dl>
<dt>-skeletonName xxx%yyy</p>
<dd>Use <i>xxx%yyy</i> as the pattern for naming the skeleton. The defaults are:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>%POA for the <i>POA</i> base class (<i>-fserver</i> or <i>-fall</i>)</p>
<dt>o</p>
<dd>_%ImplBase for the <i>oldImplBase</i> class (<i>-oldImplBase</i> and (<i>-fserver</i> or <i>-fall</i>))</dl>
</dl>
<dt>-td dir</p>
<dd>Use <i>dir</i> for the output directory instead of the current directory.</p>
<dt>-tieName xxx%yyy</p>
<dd>Name the tie according to the pattern. The defaults are:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>%POATie for the <i>POA</i> tie base class (<i>-fserverTie</i> or <i>-fallTie</i>)</p>
<dt>o</p>
<dd>%_Tie for the <i>oldImplBase</i> tie class (<i>-oldImplBase</i> and (<i>-fserverTie</i> or <i>-fallTie</i>))</dl>
</dl>
<dt>-nowarn, -verbose</p>
<dd>Verbose mode.</p>
<dt>-version</p>
<dd>Display version information and terminate.</dl>
</dl>
<p> See the Description section for more option information.</p>
<h2>Restrictions:</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>Escaped identifiers in the global scope may not have the same spelling as IDL primitive types, <i>Object</i>, or <i>ValueBase</i>. This is because the symbol table is pre-loaded with these identifiers; allowing them to be redefined would overwrite their original definitions. (Possible permanent restriction).</p>
<dt>o</p>
<dd>The <i>fixed</i> IDL type is not supported.</dl>
</dl>
<h2>Known Problems:</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>No import generated for global identifiers. If you invoke on an unexported local impl, you do get an exception, but it seems to be due to a <i>NullPointerException</i> in the <i>ServerDelegate</i> DSI code.</dl>
</dl>
<p>&nbsp;<wbr></p>
