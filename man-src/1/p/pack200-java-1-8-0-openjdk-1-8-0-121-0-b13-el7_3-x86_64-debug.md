---
title: "pack200-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "pack200-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pack200-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "pack200 – Packages a JAR file into a compressed pack200 file for web deployment."
---

<p>pack200 &#8211; Packages a JAR file into a compressed pack200 file for web deployment.</p>
<h2>Synopsis</h2>
<pre><code>pack200</code> [<i>options</i>] <i>output-file</i> <i>JAR-file</i></pre>
<p>Options can be in any order. The last option on the command line or in a properties file supersedes all previously specified options.</p>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>output-file</i></p>
<dd>Name of the output file.</p>
<dt><i>JAR-file</i></p>
<dd>Name of the input file.</dl>
<h2>Description</h2>
<p>The <code>pack200</code> command is a Java application that transforms a JAR file into a compressed pack200 file with the Java gzip compressor. The pack200 files are highly compressed files that can be directly deployed to save bandwidth and reduce download time. </p>
<p> The <code>pack200</code> command has several options to fine-tune and set the compression engine. The typical usage is shown in the following example, where <code>myarchive.pack.gz</code> is produced with the default <code>pack200</code> command settings: </p>
<pre><code>pack200 myarchive.pack.gz myarchive.jar</code></pre>
<h2>Options</h2>
<dl COMPACT>
<dt>-r, &#8211;repack</p>
<dd>Produces a JAR file by packing and unpacking a JAR file. The resulting file can be used as an input to the <code><a href="/docs/linux/man/1-jarsigner/">jarsigner</a></code>(1) tool. The following example packs and unpacks the myarchive.jar file: </p>
<pre><code>pack200 --repack myarchive-packer.jar myarchive.jar</code></pre>
<pre><code>pack200 --repack myarchive.jar</code></pre>
<p>The following example preserves the order of files in the input file.</p>
<dt>-g, &#8211;no-gzip</p>
<dd>Produces a <code>pack200</code> file. With this option, a suitable compressor must be used, and the target system must use a corresponding decompresser. </p>
<pre><code>pack200 --no-gzip myarchive.pack myarchive.jar</code></pre>
<dt>-G, &#8211;strip-debug</p>
<dd>Strips debugging attributes from the output. These include <code>SourceFile</code>, <code>LineNumberTable</code>, <code>LocalVariableTable</code> and <code>LocalVariableTypeTable</code>. Removing these attributes reduces the size of both downloads and installations, but reduces the usefulness of debuggers.</p>
<dt>&#8211;keep-file-order</p>
<dd>Preserve the order of files in the input file. This is the default behavior.</p>
<dt>-O, &#8211;no-keep-file-order</p>
<dd>The packer reorders and transmits all elements. The packer can also remove JAR directory names to reduce the download size. However, certain JAR file optimizations, such as indexing, might not work correctly.</p>
<dt>-S<i>value</i> , &#8211;segment-limit=<i>value</i></p>
<dd>The value is the estimated target size <i>N</i> (in bytes) of each archive segment. If a single input file requires more than <i>N</i> bytes, then its own archive segment is provided. As a special case, a value of <code>-1</code> produces a single large segment with all input files, while a value of 0 produces one segment for each class. Larger archive segments result in less fragmentation and better compression, but processing them requires more memory. </p>
<p> The size of each segment is estimated by counting the size of each input file to be transmitted in the segment with the size of its name and other transmitted properties. </p>
<p> The default is -1, which means that the packer creates a single segment output file. In cases where extremely large output files are generated, users are strongly encouraged to use segmenting or break up the input file into smaller JARs. </p>
<p> A 10 MB JAR packed without this limit typically packs about 10 percent smaller, but the packer might require a larger Java heap (about 10 times the segment limit).</p>
<dt>-E<i>value</i> , &#8211;effort=<i>value</i></p>
<dd>If the value is set to a single decimal digit, then the packer uses the indicated amount of effort in compressing the archive. Level 1 might produce somewhat larger size and faster compression speed, while level 9 takes much longer, but can produce better compression. The special value 0 instructs the <code>pack200</code> command to copy through the original JAR file directly with no compression. The JSR 200 standard requires any unpacker to understand this special case as a pass-through of the entire archive. </p>
<p> The default is 5, to invest a modest amount of time to produce reasonable compression.</p>
<dt>-H<i>value</i> , &#8211;deflate-hint=<i>value</i></p>
<dd>Overrides the default, which preserves the input information, but can cause the transmitted archive to be larger. The possible values are: <code>true</code>, <code>false</code>, or <code>keep</code>. </p>
<p> If the <code>value</code> is <code>true</code> or false, then the <code>packer200</code> command sets the deflation hint accordingly in the output archive and does not transmit the individual deflation hints of archive elements. </p>
<p> The <code>keep</code> value preserves deflation hints observed in the input JAR. This is the default.</p>
<dt>-m<i>value</i> , &#8211;modification-time=<i>value</i></p>
<dd>The possible values are <code>latest</code> and <code>keep</code>. </p>
<p> If the value is latest, then the packer attempts to determine the latest modification time, among all the available entries in the original archive, or the latest modification time of all the available entries in that segment. This single value is transmitted as part of the segment and applied to all the entries in each segment. This can marginally decrease the transmitted size of the archive at the expense of setting all installed files to a single date. </p>
<p> If the value is <code>keep</code>, then modification times observed in the input JAR are preserved. This is the default.</p>
<dt>-P<i>file</i> , &#8211;pass-file=<i>file</i></p>
<dd>Indicates that a file should be passed through bytewise with no compression. By repeating the option, multiple files can be specified. There is no pathname transformation, except that the system file separator is replaced by the JAR file separator forward slash (/). The resulting file names must match exactly as strings with their occurrences in the JAR file. If <code>file</code> is a directory name, then all files under that directory are passed.</p>
<dt>-U<i>action</i> , &#8211;unknown-attribute=<i>action</i></p>
<dd>Overrides the default behavior, which means that the class file that contains the unknown attribute is passed through with the specified <code>action</code>. The possible values for actions are <code>error</code>, <code>strip</code>, or <code>pass</code>. </p>
<p> If the value is <code>error</code>, then the entire <code>pack200</code> command operation fails with a suitable explanation. </p>
<p> If the value is <code>strip</code>, then the attribute is dropped. Removing the required Java Virtual Machine (JVM) attributes can cause class loader failures. </p>
<p> If the value is <code>pass</code>, then the entire class is transmitted as though it is a resource.</p>
<dt>
<pre><dd>-C<i>attribute-name</i>=<i>layout</i> , --class-attribute=<i>attribute-name</i>=<i>action</i>
<br></pre>
<p>See next option.</p>
<dt>
<pre><dd>-F<i>attribute-name</i>=<i>layout</i> , --field-attribute=<i>attribute-name</i>=<i>action</i>
<br></pre>
<p>See next option.</p>
<dt>
<pre><dd>-M<i>attribute-name</i>=<i>layout</i> , --method-attribute=<i>attribute-name</i>=<i>action</i>
<br></pre>
<p>See next option.</p>
<dt>
<pre><dd>-D<i>attribute-name</i>=<i>layout</i> , --code-attribute=<i>attribute-name</i>=<i>action</i>
<br></pre>
<p>With the previous four options, the attribute layout can be specified for a class entity, such as <code>class-attribute</code>, <code>field-attribute</code>, <code>method-attribute</code>, and <code>code-attribute</code>. The <i>attribute-name</i> is the name of the attribute for which the layout or action is being defined. The possible values for <i>action</i> are <code>some-layout-string</code>, <code>error</code>, <code>strip</code>, <code>pass</code>. </p>
<p> <code>some-layout-string</code>: The layout language is defined in the JSR 200 specification, for example: <code>&#8211;class-attribute=SourceFile=RUH</code>. </p>
<p> If the value is <code>error</code>, then the <code>pack200</code> operation fails with an explanation. </p>
<p> If the value is <code>strip</code>, then the attribute is removed from the output. Removing JVM-required attributes can cause class loader failures. For example, <code>&#8211;class-attribute=CompilationID=pass</code> causes the class file that contains this attribute to be passed through without further action by the packer. </p>
<p> If the value is <code>pass</code>, then the entire class is transmitted as though it is a resource.</p>
<dt>-f <i>pack.properties</i> , &#8211;config-file=<i>pack.properties</i></p>
<dd>A configuration file, containing Java properties to initialize the packer, can be specified on the command line. </p>
<pre><code>pack200 -f pack.properties myarchive.pack.gz myarchive.jar</code></pre>
<pre><code>more pack.properties</code></pre>
<pre><code># Generic properties for the packer.</code></pre>
<pre><code>modification.time=latest</code></pre>
<pre><code>deflate.hint=false</code></pre>
<pre><code>keep.file.order=false</code></pre>
<pre><code># This option will cause the files bearing new attributes to</code></pre>
<pre><code># be reported as an error rather than passed uncompressed.</code></pre>
<pre><code>unknown.attribute=error</code></pre>
<pre><code># Change the segment limit to be unlimited.</code></pre>
<pre><code>segment.limit=-1</code></pre>
<dt>-v, &#8211;verbose</p>
<dd>Outputs minimal messages. Multiple specification of this option will create more verbose messages.</p>
<dt>-q, &#8211;quiet</p>
<dd>Specifies quiet operation with no messages.</p>
<dt>-l<i>filename</i> , &#8211;log-file=<i>filename</i></p>
<dd>Specifies a log file to output messages.</p>
<dt>-?, -h, &#8211;help</p>
<dd>Prints help information about this command.</p>
<dt>-V, &#8211;version</p>
<dd>Prints version information about this command.</p>
<dt>-J<i>option</i></p>
<dd>Passes the specified option to the Java Virtual Machine. For more information, see the reference page for the <a href="/docs/linux/man/1-java/">java</a>(1) command. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB.</dl>
<h2>Exit Status</h2>
<p>The following exit values are returned: 0 for successful completion and a number greater than 0 when an error occurs.</p>
<h2>Notes</h2>
<p>This command should not be confused with <code><a href="/docs/linux/man/1-pack/">pack</a></code>(1). The <code>pack</code> and <code>pack200</code> commands are separate products. </p>
<p> The Java SE API Specification provided with the JDK is the superseding authority, when there are discrepancies.</p>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-unpack200/">unpack200</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jar/">jar</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jarsigner/">jarsigner</a>(1) </p>
</dl>
