---
title: "xjc-java-1-8-0-openjdk-1-8-0-31-5-b13-fc21-x86_64(1)"
name: "xjc-java-1-8-0-openjdk-1-8-0-31-5-b13-fc21-x86_64"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xjc-java-1-8-0-openjdk-1-8-0-31-5-b13-fc21-x86_64/"
description: "xjc – Compiles an XML schema file into fully annotated Java classes."
---

<p>xjc &#8211; Compiles an XML schema file into fully annotated Java classes.</p>
<h2>Synopsis</h2>
<pre><code>xjc</code> [ <i>options</i> ] <code>schema</code> <i>file/URL/dir/jar</i> ... [<code>-b</code> <i>bindinfo</i> ] ...</pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt>schema <i>file/URL/dir/jar &#8230;</i></p>
<dd>The location of the XML schema file. If <code>dir</code> is specified, then all schema files in it are compiled. If <code>jar</code> is specified, then the <code>/META-INF/sun-jaxb.episode</code> binding file is compiled.</p>
<dt>-b <i>bindinfo</i></p>
<dd>The location of the bindings files.</dl>
<h2>Description</h2>
<p>Start the binding compiler with the appropriate <code>xjc</code> shell script in the bin directory for your platform. There is also an Ant task to run the binding complier. See Using the XJC with Ant at <a rel="nofollow" href="http://jaxb.java.net/nonav/2.1.3/docs/xjcTask.html">http://jaxb.java.net/nonav/2.1.3/docs/xjcTask.html</a></p>
<h2>Options</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd>See also Nonstandard Options</p>
<dt>&bull;</p>
<dd>See also Deprecated and Removed Options</p>
<dt>-nv</p>
<dd>By default, the XJC binding compiler performs strict validation of the source schema before processing it. Use this option to disable strict schema validation. This does not mean that the binding compiler will not perform any validation, but means that it will perform a less-strict validation.</p>
<dt>-extension</p>
<dd>By default, the XJC binding compiler strictly enforces the rules outlined in the Compatibility chapter of the JAXB Specification. Appendix E.2 defines a set of W3C XML Schema features that are not completely supported by JAXB v1.0. In some cases, you may be allowed to use them in the <code>-extension</code> mode enabled by this switch. In the default (strict) mode, you are also limited to using only the binding customization defined in the specification. By using the <code>-extension</code> switch, you will be allowed to use the JAXB Vendor Extensions.</p>
<dt>-b <i>file</i></p>
<dd>Specifies one or more external binding files to process. Each binding file must have its own <code>-b</code> switch. The syntax of the external binding files is flexible. You can have a single binding file that contains customization for multiple schemas or you can break the customization into multiple bindings files: <code>xjc schema1.xsd schema2.xsd schema3.xsd -b bindings123.xjb</code><code>xjc schema1.xsd schema2.xsd schema3.xsd -b bindings1.xjb -b bindings2.xjb -b bindings3.xjb</code>. In addition, the ordering of the schema files and binding files on the command line does not matter.</p>
<dt>-d <i>dir</i></p>
<dd>By default, the XJC binding compiler generates the Java content classes in the current directory. Use this option to specify an alternate output directory. The output directory must already exist. The XJC binding compiler does not create it for you.</p>
<dt>-p <i>pkg</i></p>
<dd>When you specify a target package with this command-line option, it overrides any binding customization for the package name and the default package name algorithm defined in the specification.</p>
<dt>-httpproxy <i>proxy</i></p>
<dd>Specifies the HTTP or HTTPS proxy in the format <i>[user[:password]@]proxyHost[:proxyPort]</i>. The old <code>-host</code> and <code>-port</code> options are still supported by the RI for backward compatibility, but they were deprecated. The password specified with this option is an argument that is visible to other users who use the top command. For greater security, use the <code>-httpproxyfile</code> option.</p>
<dt>-httpproxyfile file</p>
<dd>Specifies the HTTP or HTTPS proxy with a file. The same format as the <code>-httpproxy</code> option, but the password specified in the file is not visible to other users.</p>
<dt>-classpath arg</p>
<dd>Specifies where to find client application class files used by the <i>jxb:javaType</i> and xjc:<i>superClass</i> customization.</p>
<dt>-catalog file</p>
<dd>Specifies catalog files to resolve external entity references. Supports the TR9401, XCatalog, and OASIS XML Catalog formats. See XML Entity and URI Resolvers at <a rel="nofollow" href="http://xerces.apache.org/xml-commons/components/resolver/resolver-article.html">http://xerces.apache.org/xml-commons/components/resolver/resolver-article.html</a></p>
<dt>-readOnly</p>
<dd>By default, the XJC binding compiler does not write-protect the Java source files it generates. Use this option to force the XJC binding compiler to mark the generated Java sources as read-only.</p>
<dt>-npa</p>
<dd>Suppresses the generation of package level annotations into <code>**/package-info.java</code>. Using this switch causes the generated code to internalize those annotations into the other generated classes.</p>
<dt>-no-header</p>
<dd>Suppresses the generation of a file header comment that includes some note and time stamp. Using this makes the generated code more compatible with the <code>diff</code> command.</p>
<dt>-target 2.0</p>
<dd>Avoids generating code that relies on any JAXB 2.1 features. This will allow the generated code to run with JAXB 2.0 runtime environment (such as Java SE 6).</p>
<dt>-xmlschema</p>
<dd>Treats input schemas as W3C XML Schema (default). If you do not specify this switch, then your input schemas are treated as though they are W3C XML Schemas.</p>
<dt>-relaxing</p>
<dd>Treats input schemas as RELAX NG (experimental and unsupported). Support for RELAX NG schemas is provided as a JAXB Vendor Extension.</p>
<dt>-relaxing-compact</p>
<dd>Treat input schemas as RELAX NG compact syntax (experimental and unsupported). Support for RELAX NG schemas is provided as a JAXB Vendor Extension.</p>
<dt>-dtd</p>
<dd>Treats input schemas as XML DTD (experimental and unsupported). Support for RELAX NG schemas is provided as a JAXB Vendor Extension.</p>
<dt>-wsdl</p>
<dd>Treats input as WSDL and compiles schemas inside it (experimental and unsupported).</p>
<dt>-quiet</p>
<dd>Suppress compiler output, such as progress information and warnings.</p>
<dt>-verbose</p>
<dd>Be extra verbose, such as printing informational messages or displaying stack traces upon some errors.</p>
<dt>-help</p>
<dd>Displays a brief summary of the compiler switches.</p>
<dt>-version</p>
<dd>Displays the compiler version information.</p>
<dt><i>schema file/URL/dir</i></p>
<dd>Specifies one or more schema files to compile. If you specify a directory, then the <code>xjc</code> command scans it for all schema files and compiles them.</dl>
<h3>Nonstandard Options</h3>
<dl COMPACT>
<dt>-XLocator</p>
<dd>Causes the generated code to expose SAX Locator information about the source XML in the Java bean instances after unmarshalling.</p>
<dt>-Xsync-methods</p>
<dd>Causes all of the generated method signatures to include the <code>synchronized</code> keyword.</p>
<dt>-mark-generated</p>
<dd>Marks the generated code with the annotation <code>@javax.annotation.Generated</code>.</p>
<dt>-episode file</p>
<dd>Generates the specified episode file for separate compilation.</dl>
<h3>Deprecated And Removed Options</h3>
<dl COMPACT>
<dt>-host &amp; -port</p>
<dd>These options are replaced with the <code>-httpproxy</code> option. For backward compatibility, these options are supported, but will not be documented and might be removed from future releases.</p>
<dt>-use-runtime</p>
<dd>Because the JAXB 2.0 specification has defined a portable runtime environment, it is no longer necessary for the JAXB RI to generate <code>**/impl/runtime</code>packages. Therefore, this switch is obsolete and was removed.</p>
<dt>-source</p>
<dd>The <code>-source</code> compatibility switch was introduced in the first JAXB 2.0 Early Access release. This switch is removed from future releases of JAXB 2.0. If you need to generate 1.0.x code, then use an installation of the 1.0.x code base.</dl>
<h2>Compiler Restrictions</h2>
<p>In general, it is safest to compile all related schemas as a single unit with the same binding compiler switches. Keep the following list of restrictions in mind when running the <code>xjc</code> command. Most of these issues only apply when you compile multiple schemas with multiple invocations of the <code>xjc</code> command. </p>
<p> To compile multiple schemas at the same time, keep the following precedence rules for the target Java package name in mind:</p>
<dl COMPACT>
<dt>1.</p>
<dd>The <code>-p</code> option has the highest precedence.</p>
<dt>2.</p>
<dd><i>jaxb:package</i> customization.</p>
<dt>3.</p>
<dd>If <code>targetNamespace</code> is declared, then apply the <code>t</code><code>argetNamespace</code> to the Java package name algorithm defined in the specification.</p>
<dt>4.</p>
<dd>If no <code>targetNamespace</code> is declared, then use a hard coded package named <code>generated</code>.</dl>
<p> You cannot have more than one <i>jaxb:schemaBindings</i> per name space, so it is impossible to have two schemas in the same target name space compiled into different Java packages. </p>
<p> All schemas being compiled into the same Java package must be submitted to the XJC binding compiler at the same time. They cannot be compiled independently and work as expected. </p>
<p> Element substitution groups that are spread across multiple schema files must be compiled at the same time.</p>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd>Binding Compiler (xjc) at <a rel="nofollow" href="http://jaxb.java.net/nonav/2.2.3u1/docs/xjc.html">http://jaxb.java.net/nonav/2.2.3u1/docs/xjc.html</a></p>
<dt>&bull;</p>
<dd>Java Architecture for XML Binding (JAXB) at <a rel="nofollow" href="http://www.oracle.com/technetwork/articles/javase/index-140168.html">http://www.oracle.com/technetwork/articles/javase/index-140168.html</a> </p>
</dl>
