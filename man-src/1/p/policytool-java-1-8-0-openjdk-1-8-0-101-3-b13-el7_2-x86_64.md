---
title: "policytool-java-1-8-0-openjdk-1-8-0-101-3-b13-el7_2-x86_64(1)"
name: "policytool-java-1-8-0-openjdk-1-8-0-101-3-b13-el7_2-x86_64"
section: "1"
letter: "p"
url: "/docs/linux/man/1-policytool-java-1-8-0-openjdk-1-8-0-101-3-b13-el7_2-x86_64/"
description: "policytool – Reads and writes a plain text policy file based on user input through the utility GUI."
---

<p>policytool &#8211; Reads and writes a plain text policy file based on user input through the utility GUI.</p>
<h2>Synopsis</h2>
<pre><code>policytool</code> [ <code>-file</code> ] [ <i>filename</i> ] </pre>
<dl COMPACT>
<dt>-file</dt>
<dd>Directs the <code>policytool</code> command to load a policy file.</dd>
<dt><i>filename</i></dt>
<dd>The name of the file to be loaded.</dd></dl>
<p> <i>Examples</i>: </p>
<p> Run the policy tool administrator utility: </p>
<pre><code>policytool</code></pre>
<p>Run the <code>policytool</code> command and load the specified file: </p>
<pre><code>policytool -file </code><i>mypolicyfile</i></pre>
<h2>Description</h2>
<p>The <code>policytool</code> command calls an administrator&#8217;s GUI that enables system administrators to manage the contents of local policy files. A policy file is a plain-text file with a <code>.policy</code> extension, that maps remote requestors by domain, to permission objects. For details, see Default Policy Implementation and Policy File Syntax at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html</a></p>
<h2>Options</h2>
<dl COMPACT>
<dt>-file</dt>
<dd>Directs the <code>policytool</code> command to load a policy file.</dd></dl>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</dt>
<dd>Default Policy Implementation and Policy File Syntax at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html</a></dd>
<dt>&bull;</dt>
<dd>Policy File Creation and Management at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyGuide.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyGuide.html</a></dd>
<dt>&bull;</dt>
<dd>Permissions in Java SE Development Kit (JDK) at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/permissions.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/permissions.html</a></dd>
<dt>&bull;</dt>
<dd>Java Security Overview at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/overview/jsoverview.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/overview/jsoverview.html</a></dd>
<dt>&bull;</dt>
<dd>Java Cryptography Architecture (JCA) Reference Guide at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html</a> </dd>
</dl>
