---
title: "extcheck-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64(1)"
name: "extcheck-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extcheck-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64/"
description: "extcheck – A utility to detect jar conflicts"
---

<p>extcheck &#8211; A utility to detect jar conflicts </p>
<p> <code>extcheck</code> detects version conflicts between a target jar file and currently installed extension jar files. </p>
<h2>Synopsis</h2>
<pre><code>extcheck [ -verbose ] targetfile.jar</code></pre>
<h2>Description</h2>
<p>The <code>extcheck</code> utility checks a specified Jar file for title and version conflicts with any extensions installed in the Java(TM) SDK. Before installing an extension, you can use this utility to see if the same or a more recent version of the extension is already installed. </p>
<p> The <code>extcheck</code> utility compares the <i>Specification-title</i> and <i>Specification-version</i> headers in the manifest of the <i>targetfile.jar</i> file against the corresponding headers in all Jar files currently installed in the extension directory. (The extension directory is <i>jre/lib/ext</i> by default.) The <code>extcheck</code> utility compares version numbers in the same way as the method <i>java.lang.Package.isCompatibleWith</i>. </p>
<p> If no conflict is detected, the return code is <i>0</i>. </p>
<p> If the manifest of any jar file in the extensions directory has the same <i>Specification-title</i> and the same or a newer <i>Specification-version</i> number, a non-zero error code is returned. A non-zero error code is also returned if <i>targetfile.jar</i> does not have the <i>Specification-title</i> or <i>Specification-version</i> attributes in its manifest. </p>
<h2>Options</h2>
<dl>
<dd>
<dl>
<dt>-verbose</p>
<dd>Lists Jar files in the extension directory as they are checked. Additionally, manifest attributes of the target jar file and any conflicting jar files are also reported.</p>
<dt>-Joption</p>
<dd>Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the <a href="/docs/linux/man/1-java/">java</a>(1). For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes.</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-jar/">jar</a>(1) </p>
<p>&nbsp;<wbr></p>
