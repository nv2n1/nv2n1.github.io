---
title: "xjc-java-1(1)"
name: "xjc-java-1"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xjc-java-1/"
description: "xjc – Java(TM) Architecture for XML Binding Binding Compiler"
---

<h2>Name</h2>
<p> xjc &#8211; Java(TM) Architecture for XML Binding<br />
 Binding Compiler </p>
<p> <code>Specification Version:</code> 2.1<br />
 <code>Reference Implementation (RI) Version:</code> 2.1.3 </p>
<h2>Launching xjc</h2>
<p> The binding compiler can be launched using the appropriate <i>xjc</i> shell script in the <i>bin</i> directory for your platform. We also provide an Ant task to run the binding complier &#8211; see the instructions for <i>using the XJC Ant task</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/xjcTask.html.">https://jaxb.dev.java.net/nonav/2.1.3/docs/xjcTask.html.</a> </p>
<p> <i>% xjc -help</i> </p>
<h3>Output</h3>
<pre><code>
Usage : xjc[-options...]&lt;schema file / URL / dir / jar&gt;...[-b&lt;bindinfo&gt;]... If dir is specified, all schema files in it will be compiled.If jar is specified, / META - INF / sun - jaxb.episode binding file will be compiled.Options : -nv : do not perform strict validation of the input schema(s) - extension : allow vendor extensions - do not strictly follow the Compatibility Rules and App E .2 from the JAXB Spec - b&lt;file / dir&gt; : specify external bindings files(each&lt;file&gt; must have its own - b);
if a directory is given, **/*.xjb is searched
  -d &lt;dir&gt;           :  generated files will go into this directory
  -p &lt;pkg&gt;           :  specifies the target package
  -httpproxy &lt;proxy&gt; :  set HTTP/HTTPS proxy; format is [user[:password]@]proxyHost:proxyPort
  -httpproxyfile &lt;f&gt; :  works like -httpproxy but takes the argument in a file to protect password
  -classpath &lt;arg&gt;   :  specify where to find user class files
  -catalog &lt;file&gt;    :  specify catalog files to resolve external entity references; support TR9401, XCatalog, and OASIS XML Catalog format
  -readOnly          :  generated files will be in read-only mode
  -npa               :  suppress generation of package level annotations (**/package-info.java)
  -no-header         :  suppress generation of a file header with timestamp
  -target 2.0        :  behave like XJC 2.0 and generate code that doesnt use any 2.1 features
  -xmlschema         :  treat input as W3C XML Schema (default)
  -relaxng           :  treat input as RELAX NG (experimental,unsupported)
  -relaxng-compact   :  treat input as RELAX NG compact syntax (experimental,unsupported)
  -dtd               :  treat input as XML DTD (experimental,unsupported)
  -wsdl              :  treat input as WSDL and compile schemas inside it (experimental,unsupported)
  -verbose           :  be extra verbose
  -quiet             :  suppress compiler output
  -help              :  display this help message
  -version           :  display version information
Extensions:
  -Xlocator          :  enable source location support for generated code
  -Xsync-methods     :  generate accessor methods with the 'synchronized' keyword
  -mark-generated    :  mark the generated code as @javax.annotation.Generated
  -episode &lt;FILE&gt;    :  generate the episode file for separate compilation
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>-nv</p>
<dd> By default, the XJC binding compiler performs strict validation of the source schema before processing it. Use this option to disable strict schema validation. This does not mean that the binding compiler will not perform any validation, it simply means that it will perform less-strict validation.</p>
<dt>-extension</p>
<dd> By default, the XJC binding compiler strictly enforces the rules outlined in the Compatibility chapter of the JAXB Specification. Appendix E.2 defines a set of W3C XML Schema features that are not completely supported by JAXB v1.0. In some cases, you may be allowed to use them in the &quot;-extension&quot; mode enabled by this switch. In the default (strict) mode, you are also limited to using only the binding customizations defined in the specification. By using the &quot;-extension&quot; switch, you will be allowed to use the JAXB Vendor Extensions</p>
<dt>-b &lt;file&gt;</p>
<dd> Specify one or more external binding files to process. (Each binding file must have its own <i>&quot;-b&quot;</i> switch.) The syntax of the external binding files is extremely flexible. You may have a single binding file that contains customizations for multiple schemas or you can break the customizations into multiple bindings files: <i>xjc schema1.xsd schema2.xsd schema3.xsd -b bindings123.xjb</i><br />
 <i>xjc schema1.xsd schema2.xsd schema3.xsd -b bindings1.xjb -b bindings2.xjb -b bindings3.xjb</i> In addition, the ordering of the schema files and binding files on the command line does not matter.</p>
<dt>-d &lt;dir&gt;</p>
<dd> By default, the XJC binding compiler will generate the Java content classes in the current directory. Use this option to specify an alternate output directory. The output directory must already exist, the XJC binding compiler will not create it for you.</p>
<dt>-p &lt;pkg&gt;</p>
<dd> Specifying a target package via this command-line option overrides any binding customization for package name and the default package name algorithm defined in the specification.</p>
<dt>-httpproxy &lt;proxy&gt;</p>
<dd> Specify the HTTP/HTTPS proxy. The format is [user[:password]@]proxyHost[:proxyPort]. The old <i>-host</i> and <i>-port</i> are still supported by the RI for backwards compatibility, but they have been deprecated. Note that the password specified with this option is an argument that is visible to other users who use the <i>top</i> command, for example. For greater security, use <i>-httpproxyfile</i>, below.</p>
<dt>-httpproxyfile &lt;file&gt;</p>
<dd> Specify the HTTP/HTTPS proxy using a file. Same format as above, but the password specified in the file is not visible to other users.</p>
<dt>-classpath &lt;arg&gt;</p>
<dd> Specify where to find client application class files used by the <i>&lt;jxb:javaType&gt;</i> and <i>&lt;xjc:superClass&gt;</i> customizations.</p>
<dt>-catalog &lt;file&gt;</p>
<dd> Specify catalog files to resolve external entity references. Supports TR9401, XCatalog, and OASIS XML Catalog format. Please read the XML Entity and URI Resolvers document or the <i>catalog-resolver</i> sample application.</p>
<dt>-readOnly</p>
<dd> By default, the XJC binding compiler does not write-protect the Java source files it generates. Use this option to force the XJC binding compiler to mark the generated Java sources read-only.</p>
<dt>-npa</p>
<dd> Supress the generation of package level annotations into **/package-info.java. Using this switch causes the generated code to internalize those annotations into the other generated classes.</p>
<dt>-no-header</p>
<dd> Supress the generation of a file header comment that includes some note and timestamp. Using this makes the generated code more diff-friendly.</p>
<dt>-target 2.0</p>
<dd> Avoid generating code that relies on any JAXB 2.1 features. This will allow the generated code to run with JAXB 2.0 runtime (such as JavaSE 6.)</p>
<dt>-xmlschema</p>
<dd> Treat input schemas as W3C XML Schema (default). If you do not specify this switch, your input schemas will be treated as W3C XML Schema.</p>
<dt>-relaxng</p>
<dd> Treat input schemas as RELAX NG (experimental, unsupported). Support for RELAX NG schemas is provided as a JAXB Vendor Extension.</p>
<dt>-relaxng-compact</p>
<dd> Treat input schemas as RELAX NG compact syntax(experimental, unsupported). Support for RELAX NG schemas is provided as a JAXB Vendor Extension.</p>
<dt>-dtd</p>
<dd> Treat input schemas as XML DTD (experimental, unsupported). Support for RELAX NG schemas is provided as a JAXB Vendor Extension.</p>
<dt>-wsdl</p>
<dd> Treat input as WSDL and compile schemas inside it (experimental,unsupported).</p>
<dt>-quiet</p>
<dd> Suppress compiler output, such as progress information and warnings.</p>
<dt>-verbose</p>
<dd> Be extra verbose, such as printing informational messages or displaying stack traces upon some errors.</p>
<dt>-help</p>
<dd> Display a brief summary of the compiler switches.</p>
<dt>-version</p>
<dd> Display the compiler version information.</p>
<dt>&lt;schema file/URL/dir&gt;</p>
<dd> Specify one or more schema files to compile. If you specify a directory, then xjc will scan it for all schema files and compile them.</dl>
</dl>
<h3>Non-Standard Command Line Options</h3>
<dl>
<dt>
<dd>
<dl>
<dt>-Xlocator</p>
<dd> Causes the generated code to expose SAX Locator information about the source XML in the Java bean instances after unmarshalling.</p>
<dt>-Xsync-methods</p>
<dd> Causes all of the generated method signatures to include the <i>synchronized</i> keyword.</p>
<dt>-mark-generated</p>
<dd> Mark the generated code with the annotation <i>@javax.annotation.Generated</i>.</p>
<dt>-episode &lt;file&gt;</p>
<dd> Generate the specified episode file for separate compilation.</dl>
</dl>
<h3>Deprecated and Removed Command Line Options</h3>
<dl>
<dt>
<dd>
<dl>
<dt>-host &amp; -port</p>
<dd> These options have been deprecated and replaced with the <code>-httpproxy</code> option. For backwards compatibility, we will continue to support these options, but they will no longer be documented and may be removed from future releases.</p>
<dt>-use-runtime</p>
<dd> Since the JAXB 2.0 specification has defined a portable runtime, it is no longer necessary for the JAXB RI to generate **/impl/runtime packages. Therefore, this switch is obsolete and has been removed.</p>
<dt>-source</p>
<dd> The -source compatibility switch was introduced in the first JAXB 2.0 Early Access release. We have decided to remove this switch from future releases of JAXB 2.0. If you need to generate 1.0.x code, please use an installation of the 1.0.x codebase.</dl>
</dl>
<h3>Compiler Restrictions</h3>
<p> In general, it is safest to compile all related schemas as a single unit with the same binding compiler switches. </p>
<p> Please keep the following list of restrictions in mind when running xjc. Most of these issues only apply when compiling multiple schemas with multiple invocations of xjc. </p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> To compile multiple schemas at the same time, keep the following precedence rules for the target Java package name in mind:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> The &quot;<i>-p</i>&quot; command line option takes the highest precedence.</p>
<dt>2.</p>
<dd> &lt;<i>jaxb:package</i>&gt; customization</p>
<dt>3.</p>
<dd> If <i>targetNamespace</i> is declared, apply <i>targetNamespace</i> -&gt; Java package name algorithm defined in the specification.</p>
<dt>4.</p>
<dd> If no <i>targetNamespace</i> is declared, use a hardcoded package named &quot;generated&quot;.</dl>
</dl>
<dt>o</p>
<dd> It is not legal to have more than one &lt;<i>jaxb:schemaBindings</i>&gt; per namespace, so it is impossible to have two schemas in the same target namespace compiled into different Java packages.</p>
<dt>o</p>
<dd> All schemas being compiled into the same Java package must be submitted to the XJC binding compiler at the same time &#8211; they cannot be compiled independently and work as expected.</p>
<dt>o</p>
<dd> Element substitution groups spread across multiple schema files must be compiled at the same time.</dl>
</dl>
<h2>See Also</h2>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Running the binding compiler (XJC): [ <i>command-line instructions</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/xjc.html,">https://jaxb.dev.java.net/nonav/2.1.3/docs/xjc.html,</a> <i>using the XJC Ant task</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/xjcTask.html]">https://jaxb.dev.java.net/nonav/2.1.3/docs/xjcTask.html]</a></p>
<dt>o</p>
<dd> <i>Java Architecture for XML Binding (JAXB)</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/xml/jaxb/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/xml/jaxb/index.html</a></dl>
</dl>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
