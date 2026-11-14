---
title: "unpack200-java-1-6-0-openjdk(1)"
name: "unpack200-java-1-6-0-openjdk"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unpack200-java-1-6-0-openjdk/"
---

unpack200 - JAR Unpacking tool
<h2>Synopsis</h2><tt>unpack200</tt><i> [ </i><i>options</i> ] <i>input-file</i> <i>JAR-file</i> 

 

 Options may be in any order. The last option on the command line supersedes all previously specified options. 

<dl COMPACT><dd><dl COMPACT><dt>input-file
<dd>Name of the input file, which can be a pack200 gzip file or a pack200 file. The input could also be JAR file produced by <a HREF="/docs/linux/man/1-pack200/">pack200</a>(1) with an effort of 0. In this case the contents of the input file will be copied to the output JAR file with the Pack200 marker.
<dt>JAR-file
<dd>Name of the output JAR file.</dl></dl><h2>Description</h2><i>unpack200</i> is a native implementation that transforms a packed file produced by <i><a HREF="/docs/linux/man/1-pack200/">pack200</a></i>(1) into a JAR file. Typical usage: 

<dl COMPACT><dd><i>% unpack200 myarchive.pack.gz myarchive.jar</i> 

</dl>
 

 In this example, the <i>myarchive.jar</i> is produced from <i>myarchive.pack.gz</i> using the default <i>unpack200</i> settings. 

<h2>Options</h2><h3>Standard Options</h3><tt>-Hvalue --deflate-hint=</tt><i>value</i> 

<dl COMPACT><dd>Sets the deflation to be <i>true</i>, <i>false</i>, or <i>keep</i> on all entries within a JAR file. The default mode is <i>keep</i>. If <i>true</i> or <i>false</i>, overrides the default behavior and sets the deflation mode on all entries within the output JAR file. 

</dl><h3>Non-Standard Options</h3><tt>-r --remove-pack-file</tt> 

<dl COMPACT><dd>Removes the input packed file. 

</dl>
 

 <tt>-v --verbose</tt> 

<dl COMPACT><dd>Outputs minimal messages. Multiple specification of this option will output more verbose messages. 

</dl>
 

 <tt>-q --quiet</tt> 

<dl COMPACT><dd>Specifies quiet operation with no messages. 

</dl>
 

 <tt>-lfilename --log-file=</tt><i>filename</i> 

<dl COMPACT><dd>Specifies a log file to output messages. 

</dl><h2>Exit Status</h2>The following exit values are returned: 

<dl COMPACT><dd><i>&nbsp;<wbr>0</i> if successful completion; 

 

 <i>&gt;0</i> if an error occurred. 

</dl><h2>See Also</h2><dl COMPACT><dd><dl COMPACT><dt>*
<dd>pack200 - JAR Packing Tool
<dt>*
<dd><i><a HREF="/docs/linux/man/1-pack200/">pack200</a>(1)</i>, <i><a HREF="/docs/linux/man/1-jar/">jar</a>(1)</i>, <i><a HREF="/docs/linux/man/1-jarsigner/">jarsigner</a>(1)</i>, <i><a HREF="/docs/linux/man/5-attributes/">attributes</a>(5)</i> man pages
<dt>*
<dd>Java SE Documentation
<dt>*
<dd><i>Java Deployment Guide - Pack200</i> @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/guides/deployment/deployment-guide/pack200.html">http://java.sun.com/javase/6/docs/technotes/guides/deployment/deployment-guide/pack200.html</a>
<dt>*
<dd><i>jar</i> - Java Archive Tool
<dt>*
<dd><i>jarsigner</i> - JAR Signer tool @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/tools/solaris/jarsigner.html">http://java.sun.com/javase/6/docs/technotes/tools/solaris/jarsigner.html</a></dl></dl><h2>Notes</h2>This command should not be confused with <i><a HREF="/docs/linux/man/1-unpack/">unpack</a>(1)</i>. They are distinctly separate products. 

 

 The Java SE API Specification provided with the SDK is the superseding authority, in case of discrepancies. 

 
&nbsp;<wbr>
