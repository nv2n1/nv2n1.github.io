---
title: "extcheck-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64(1)"
name: "extcheck-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extcheck-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64/"
description: "extcheck – Detects version conflicts between a target Java Archive (JAR) file and currently installed extension JAR files."
---

<p>extcheck &#8211; Detects version conflicts between a target Java Archive (JAR) file and currently installed extension JAR files.</p>
<h2>Synopsis</h2>
<pre><code>extcheck</code> [<i>options</i>] <i>targetfile.jar</i></pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>targetfile.jar</i></p>
<dd>The target JAR file against which the currently installed extension JAR files are compared to detect version conflicts.</dl>
<h2>Description</h2>
<p>The <code>extcheck</code> command checks a specified JAR file for title and version conflicts with any extensions installed in the Java SE SDK. Before installing an extension, you can use this utility to see whether the same or a more recent version of the extension is already installed. </p>
<p> The <code>extcheck</code> command compares the Specification-title and Specification-version headers in the manifest of the <code>targetfile.jar</code> file against the corresponding headers in all JAR files currently installed in the extension directory. By default, the extension directory is <code>jre/lib/ext</code> on Oracle Solaris and <code>\jre\libxt</code> on Windows. The <code>extcheck</code> command compares version numbers in the same way as the <code>java.lang.Package.isCompatibleWith</code> method. </p>
<p> If no conflict is detected, then the return code is 0. </p>
<p> If the manifest of any JAR file in the extensions directory has the same <code>Specification-title</code> and the same or a newer <code>Specification-version</code> number, then a non-zero error code is returned. A non-zero error code is also returned when <code>targetfile.jar</code> does not have the <code>Specification-title</code> or <code>Specification-version</code> attributes in its manifest file.</p>
<h2>Options</h2>
<dl>
<dt>-verbose</p>
<dd>Lists JAR files in the extension directory as they are checked. Additionally, manifest attributes of the target JAR file and any conflicting JAR files are also reported.</p>
<dt>-J<i>option</i></p>
<dd>Passes <i>option</i> to the Java Virtual Machine (JVM), where option is one of the options described on the reference page for the Java launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jar/">jar</a>(1) </p>
</dl>
