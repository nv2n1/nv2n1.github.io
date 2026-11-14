---
title: "idlj-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "idlj-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idlj-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "idlj – Generates Java bindings for a specified Interface Definition Language (IDL) file."
---

<p>idlj &#8211; Generates Java bindings for a specified Interface Definition Language (IDL) file.</p>
<h2>Synopsis</h2>
<pre><code>idlj</code> [ <i>options</i> ] <i>idlfile</i></pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options. Options can appear in any order, but must precede the <code>idlfile</code>.</p>
<dt><i>idlfile</i></p>
<dd>The name of a file that contains Interface Definition Language (IDL) definitions.</dl>
<h2>Description</h2>
<p>The IDL-to-Java Compiler generates the Java bindings for a specified IDL file. For binding details, see Java IDL: IDL to Java Language Mapping at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/mapping/jidlMapping.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/mapping/jidlMapping.html</a> </p>
<p> Some earlier releases of the IDL-to-Java compiler were named <code>idltojava</code>.</p>
<h3>Emit Client And Server Bindings</h3>
<p>The following <code>idlj</code> command generates an IDL file named <code>My.idl</code> with client-side bindings. </p>
<pre><code>idlj My.idl</code></pre>
<p>The previous syntax is equivalent to the following: </p>
<pre><code>idlj -fclient My.idl</code></pre>
<p>The next example generates the server-side bindings, and includes the client-side bindings plus the skeleton, all of which are POA (Inheritance Model). </p>
<pre><code>idlg -fserver My.idl</code></pre>
<p>If you want to generate both client and server-side bindings, then use one of the following (equivalent) commands: </p>
<pre><code>idlj -fclient -fserver My.idl</code></pre>
<pre><code>idlj -fall My.idl</code></pre>
<p>There are two possible server-side models: the Portal Servant Inheritance Model and the Tie Model. See Tie Delegation Model. </p>
<p> <code>Portable Servant Inheritance Model</code>. The default server-side model is the Portable Servant Inheritance Model. Given an interface <code>My</code> defined in <code>My.idl</code>, the file <code>MyPOA.java</code> is generated. You must provide the implementation for the <code>My</code> interface, and the <code>My</code> interface must inherit from the <code>MyPOA</code> class. <code>MyPOA.java</code> is a stream-based skeleton that extends the <code>org.omg.PortableServer.Servant</code> class at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/org/omg/PortableServer/Servant.html">http://docs.oracle.com/javase/8/docs/api/org/omg/PortableServer/Servant.html</a> The <code>My</code> interface implements the <code>callHandler</code> interface and the operations interface associated with the IDL interface the skeleton implements.The <code>PortableServer</code> module for the Portable Object Adapter (POA) defines the native <code>Servant</code> type. See Portable Object Adapter (POA) at <a href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/POA.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/POA.html</a> In the Java programming language, the <code>Servant</code> type is mapped to the Java <code>org.omg.PortableServer.Servant</code> class. It serves as the base class for all POA servant implementations and provides a number of methods that can be called by the application programmer, and methods that are called by the POA and that can be overridden by the user to control aspects of servant behavior.Another option for the Inheritance Model is to use the <code>-oldImplBase</code> flag to generate server-side bindings that are compatible with releases of the Java programming language before Java SE 1.4. The &#8211;<code>oldImplBase</code> flag is nonstandard, and these APIs are deprecated. You would use this flag only for compatibility with existing servers written in Java SE 1.3. In that case, you would need to modify an existing make file to add the <code>-oldImplBase</code> flag to the <code>idlj</code> compiler. Otherwise POA-based server-side mappings are generated. To generate server-side bindings that are backward compatible, do the following: </p>
<pre><code>idlj -fclient -fserver -oldImplBase My.idl</code></pre>
<pre><code>idlj -fall -oldImplBase My.idl</code></pre>
<p>Given an interface <code>My</code> defined in <code>My.idl</code>, the file <code>_MyImplBase.java</code> is generated. You must provide the implementation for the <code>My</code> interface, and the <code>My</code> interface must inherit from the <code>_MyImplBase</code> class. </p>
<p> <code>Tie Delegation Model</code>. The other server-side model is called the Tie Model. This is a delegation model. Because it is not possible to generate ties and skeletons at the same time, they must be generated separately. The following commands generate the bindings for the Tie Model: </p>
<pre><code>idlj -fall My.idl</code></pre>
<pre><code>idlj -fallTIE My.idl</code></pre>
<p>For the <code>My</code> interface, the second command generates <code>MyPOATie.java</code>. The constructor to the <code>MyPOATie</code> class takes a delegate. In this example, using the default POA model, the constructor also needs a POA. You must provide the implementation for the delegate, but it does not have to inherit from any other class, only the interface <code>MyOperations</code>. To use it with the ORB, you must wrap your implementation within the <code>MyPOATie</code> class, for example: </p>
<pre><code>ORB orb = ORB.init(args, System.getProperties());</code></pre>
<pre><code>// Get reference to rootpoa &amp; activate the POAManager</code></pre>
<pre><code>POA rootpoa = (POA)orb.resolve_initial_references(&quot;RootPOA&quot;);</code></pre>
<pre><code>rootpoa.the_POAManager().activate();</code></pre>
<pre><code>// create servant and register it with the ORB</code></pre>
<pre><code>MyServant myDelegate = new MyServant();</code></pre>
<pre><code>myDelegate.setORB(orb); </code></pre>
<pre><code>// create a tie, with servant being the delegate.</code></pre>
<pre><code>MyPOATie tie = new MyPOATie(myDelegate, rootpoa);</code></pre>
<pre><code>// obtain the objectRef for the tie</code></pre>
<pre><code>My ref = tie._this(orb);</code></pre>
<p>You might want to use the Tie model instead of the typical Inheritance model when your implementation must inherit from some other implementation. Java allows any number of interface inheritance, but there is only one slot for class inheritance. If you use the inheritance model, then that slot is used up. With the Tie Model, that slot is freed up for your own use. The drawback is that it introduces a level of indirection: one extra method call occurs when a method is called. </p>
<p> For server-side generation, Tie model bindings that are compatible with versions of the IDL to Java language mapping in versions earlier than Java SE 1.4. </p>
<pre><code>idlj -oldImplBase -fall My.idl</code></pre>
<pre><code>idlj -oldImplBase -fallTIE My.idl</code></pre>
<p>For the <code>My</code> interface, the this generates <code>My_Tie.java</code>. The constructor to the <code>My_Tie</code> class takes an <code>impl</code> object. You must provide the implementation for <code>impl</code>, but it does not have to inherit from any other class, only the interface <code>HelloOperations</code>. But to use it with the ORB, you must wrap your implementation within <code>My_Tie</code>, for example: </p>
<pre><code>ORB orb = ORB.init(args, System.getProperties());</code></pre>
<pre><code>// create servant and register it with the ORB</code></pre>
<pre><code>MyServant myDelegate = new MyServant();</code></pre>
<pre><code>myDelegate.setORB(orb); </code></pre>
<pre><code>// create a tie, with servant being the delegate.</code></pre>
<pre><code>MyPOATie tie = new MyPOATie(myDelegate);</code></pre>
<pre><code>// obtain the objectRef for the tie</code></pre>
<pre><code>My ref = tie._this(orb);</code></pre>
<h3>Specify Alternate Locations For Emitted Files</h3>
<p>If you want to direct the emitted files to a directory other than the current directory, then call the compiler this way: <code>i</code><code>dlj -td /altdir My.idl</code>. </p>
<p> For the <code>My</code> interface, the bindings are emitted to <code>/altdir/My.java</code>, etc., instead of <code>./My.java</code>.</p>
<h3>Specify Alternate Locations For Include Files</h3>
<p>If the <code>My.idl</code> file includes another <code>idl</code> file, <code>MyOther.idl</code>, then the compiler assumes that the <code>MyOther.idl</code> file resides in the local directory. If it resides in <code>/includes</code>, for example, then you call the compiler with the following command: </p>
<pre><code>idlj -i /includes My.idl</code></pre>
<p>If <code>My.idl</code> also included <code>Another.idl</code> that resided in <code>/moreIncludes</code>, for example, then you call the compiler with the following command: </p>
<pre><code>idlj -i /includes -i /moreIncludes My.idl</code></pre>
<p>Because this form of <code>include</code> can become long, another way to indicate to the compiler where to search for included files is provided. This technique is similar to the idea of an environment variable. Create a file named idl.config in a directory that is listed in your <code>CLASSPATH</code> variable. Inside of <code>idl.config</code>, provide a line with the following form: </p>
<pre><code>includes=/includes;/moreIncludes</code></pre>
<p>The compiler will find this file and read in the includes list. Note that in this example the separator character between the two directories is a semicolon (;). This separator character is platform dependent. On the Windows platform, use a semicolon, on the Unix platform, use a colon, and so on.</p>
<h3>Emit Bindings For Include Files</h3>
<p>By default, only those interfaces, structures, and so on, that are defined in the <code>idl</code> file on the command line have Java bindings generated for them. The types defined in included files are not generated. For example, assume the following two <code>idl</code> files: </p>
<pre><code>My.idl file:</code></pre>
<pre><code>#include &lt;MyOther.idl&gt;</code></pre>
<pre><code>interface My</code></pre>
<pre><code>{</code></pre>
<pre><code>};</code></pre>
<pre><code>MyOther.idl file:</code></pre>
<pre><code>interface MyOther</code></pre>
<pre><code>{</code></pre>
<pre><code>};</code></pre>
<p>There is a caveat to the default rule. Any <code>#include</code> statements that appear at the global scope are treated as described. These <code>#include</code> statements can be thought of as import statements. The <code>#include</code> statements that appear within an enclosed scope are treated as true <code>#include</code> statements, which means that the code within the included file is treated as though it appeared in the original file and, therefore, Java bindings are emitted for it. Here is an example: </p>
<pre><code>My.idl file:</code></pre>
<pre><code>#include &lt;MyOther.idl&gt;</code></pre>
<pre><code>interface My</code></pre>
<pre><code>{</code></pre>
<pre><code> #include &lt;Embedded.idl&gt;</code></pre>
<pre><code>};</code></pre>
<pre><code>MyOther.idl file:</code></pre>
<pre><code>interface MyOther</code></pre>
<pre><code>{</code></pre>
<pre><code>};</code></pre>
<pre><code>Embedded.idl</code></pre>
<pre><code>enum E {one, two, three};</code></pre>
<p>Run<code>idlj My.idl</code>to generate the following list of Java files. Notice that <code>MyOther.java</code> is not generated because it is defined in an import-like <code>#include</code>. But <code>E.java</code> was generated because it was defined in a true <code>#include</code>. Notice that because the <code>Embedded.idl</code> file is included within the scope of the interface <code>My</code>, it appears within the scope of <code>My</code> (in <code>MyPackage</code>). If the <code>-emitAll</code> flag had been used, then all types in all included files would have been emitted. </p>
<pre><code>./MyHolder.java</code></pre>
<pre><code>./MyHelper.java</code></pre>
<pre><code>./_MyStub.java</code></pre>
<pre><code>./MyPackage</code></pre>
<pre><code>./MyPackage/EHolder.java</code></pre>
<pre><code>./MyPackage/EHelper.java</code></pre>
<pre><code>./MyPackage/E.java</code></pre>
<pre><code>./My.java</code></pre>
<h3>Insert Package Prefixes</h3>
<p>Suppose that you work for a company named ABC that has constructed the following IDL file: </p>
<pre><code>Widgets.idl file:</code></pre>
<pre><code>module Widgets</code></pre>
<pre><code>{</code></pre>
<pre><code> interface W1 {...};</code></pre>
<pre><code> interface W2 {...};</code></pre>
<pre><code>};</code></pre>
<p>If you run this file through the IDL-to-Java compiler, then the Java bindings for W1 and W2 are placed within the <code>Widgets</code> package. There is an industry convention that states that a company&#8217;s packages should reside within a package named <code>com.&lt;company name&gt;</code>. To follow this convention, the package name should be <code>com.abc.Widgets</code>. To place this package prefix onto the Widgets module, execute the following: </p>
<pre><code>idlj -pkgPrefix Widgets com.abc Widgets.idl</code></pre>
<p>If you have an IDL file that includes Widgets.idl, then the <code>-pkgPrefix</code> flag must appear in that command also. If it does not, then your IDL file will be looking for a <code>Widgets</code> package rather than a <code>com.abc.Widgets</code> package. </p>
<p> If you have a number of these packages that require prefixes, then it might be easier to place them into the idl.config file described previously. Each package prefix line should be of the form: <code>PkgPrefix.&lt;type&gt;=&lt;prefix&gt;</code>. The line for the previous example would be <code>PkgPrefix.Widgets=com.abc</code>. This option does not affect the Repository ID.</p>
<h3>Define Symbols Before Compilation</h3>
<p>You might need to define a symbol for compilation that is not defined within the IDL file, perhaps to include debugging code in the bindings. The command <code>idlj -d MYDEF My.idl</code>is equivalent to putting the line <code>#define MYDEF</code> inside My.idl.</p>
<h3>Preserve Preexisting Bindings</h3>
<p>If the Java binding files already exist, then the <code>-keep</code> flag keeps the compiler from overwriting them. The default is to generate all files without considering that they already exist. If you have customized those files (which you should not do unless you are very comfortable with their contents), then the <code>-keep</code> option is very useful. The command <code>idlj -keep My.idl</code> emits all client-side bindings that do not already exist.</p>
<h3>View Compilation Progress</h3>
<p>The IDL-to-Java compiler generates status messages as it progresses through its phases of execution. Use the <code>-v</code> option to activate the verbose mode: <code>idlj -v My.idl</code>. </p>
<p> By default the compiler does not operate in verbose mode</p>
<h3>Display Version Information</h3>
<p>To display the build version of the IDL-to-Java compiler, specify the <code>-version</code> option on the command-line: <code>idlj -version</code>. </p>
<p> Version information also appears within the bindings generated by the compiler. Any additional options appearing on the command-line are ignored.</p>
<h2>Options</h2>
<dl>
<dt>-d <i>symbol</i></p>
<dd>This is equivalent to the following line in an IDL file: </p>
<pre><code>#define </code><i>symbol</i></pre>
<dt>-demitAll</p>
<dd>Emit all types, including those found in <code>#include</code> files.</p>
<dt>-fside</p>
<dd>Defines what bindings to emit. The <code>side</code> parameter can be <code>client</code>, <code>server</code>, <code>serverTIE</code>, <code>all</code>, or <code>allTIE</code>. The <code>-fserverTIE</code> and <code>-fallTIE</code> options cause delegate model skeletons to be emitted. Defaults to <code>-fclient</code> when the flag is not specified.</p>
<dt>-i <i>include-path</i></p>
<dd>By default, the current directory is scanned for included files. This option adds another directory.</p>
<dt>-i <i>keep</i></p>
<dd>If a file to be generated already exists, then do not overwrite it. By default it is overwritten.</p>
<dt>-noWarn</p>
<dd>Suppress warning messages.</p>
<dt>-oldImplBase</p>
<dd>Generates skeletons compatible with pre-1.4 JDK ORBs. By default, the POA Inheritance Model server-side bindings are generated. This option provides backward-compatibility with earlier releases of the Java programming language by generating server-side bindings that are <code>ImplBase</code> Inheritance Model classes.</p>
<dt>-pkgPrefix <i>type</i><i>prefix</i></p>
<dd>Wherever <code>type</code> is encountered at file scope, prefix the generated Java package name with <code>prefix</code> for all files generated for that type. The type is the simple name of either a top-level module, or an IDL type defined outside of any module.</p>
<dt>-pkgTranslate <i>type</i><i>package</i></p>
<dd>Whenever the module name type is encountered in an identifier, replace it in the identifier with package for all files in the generated Java package. Note that <code>pkgPrefix</code> changes are made first. The type value is the simple name of either a top-level module, or an IDL type defined outside of any module and must match the full package name exactly. </p>
<p> If more than one translation matches an identifier, then the longest match is chosen as shown in the following example: </p>
<p> <i>Command</i>: </p>
<pre><code>pkgTranslate type pkg -pkgTranslate type2.baz pkg2.fizz</code></pre>
<p><i>Resulting Translation</i>: </p>
<pre><code>type =&gt; pkg</code></pre>
<pre><code>type.ext =&gt; pkg.ext</code></pre>
<pre><code>type.baz =&gt; pkg2.fizz</code></pre>
<pre><code>type2.baz.pkg =&gt; pkg2.fizz.pkg</code></pre>
<p>The following package names <code>org</code>, <code>org</code>.o<code>mg</code>, or any subpackages of <code>org.omg</code> cannot be translated. Any attempt to translate these packages results in uncompilable code, and the use of these packages as the first argument after <code>-pkgTranslate</code> is treated as an error.</p>
<dt>-skeletonName <i>xxx%yyy</i></p>
<dd>Use <code>xxx%yyy</code> as the pattern for naming the skeleton. The defaults are: <code>%POA</code> for the <code>POA</code> base class (<code>-fserver</code> or <code>-fall</code>), and <code>_%ImplBase</code> for the <code>oldImplBase</code> class (-<code>oldImplBase</code>) and (<code>-fserver</code> or <code>-fall</code>)).</p>
<dt>-td <i>dir</i></p>
<dd>Use <i>dir</i> for the output directory instead of the current directory.</p>
<dt>-tieName <i>xxx%yyy</i></p>
<dd>Use <code>xxx%yyy</code> according to the pattern. The defaults are: <code>%POA</code> for the <code>POA</code> base class (<code>-fserverTie or -fallTie</code>), and <code>_%Tie</code> for the <code>oldImplBase</code> tie class (-<code>oldImplBase</code>) and (<code>-fserverTie</code> or <code>-fallTie</code>))</p>
<dt>-nowarn, -verbose</p>
<dd>Displays release information and terminates.</p>
<dt>-version</p>
<dd>Displays release information and terminates.</dl>
<h2>Restrictions</h2>
<p>Escaped identifiers in the global scope cannot have the same spelling as IDL primitive types, <code>Object</code>, or <code>ValueBase</code>. This is because the symbol table is preloaded with these identifiers. Allowing them to be redefined would overwrite their original definitions. Possible permanent restriction. </p>
<p> The <code>fixed</code> IDL type is not supported.</p>
<h2>Known Problems</h2>
<p>No import is generated for global identifiers. If you call an unexported local <code>impl</code> object, then you do get an exception, but it seems to be due to a <code>NullPointerException</code> in the <code>ServerDelegate</code> DSI code.</p>
