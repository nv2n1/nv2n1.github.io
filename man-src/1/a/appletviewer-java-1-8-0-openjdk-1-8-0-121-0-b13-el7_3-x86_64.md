---
title: "appletviewer-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64(1)"
name: "appletviewer-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64"
section: "1"
letter: "a"
url: "/docs/linux/man/1-appletviewer-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64/"
description: "appletviewer – Runs applets outside of a web browser."
---

<p>appletviewer &#8211; Runs applets outside of a web browser.</p>
<h2>Synopsis</h2>
<pre><code>appletviewer</code> [<i>options</i>] <i>url</i>...</pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options separated by spaces. See Options.</p>
<dt><i>url</i></p>
<dd>The location of the documents or resources to be displayed. You can specify multiple URLs separated by spaces.</dl>
<h2>Description</h2>
<p>The <code>appletviewer</code> command connects to the documents or resources designated by <i>urls</i> and displays each applet referenced by the documents in its own window. If the documents referred to by urls do not reference any applets with the <code>OBJECT</code>, <code>EMBED</code>, or <code>APPLET</code> tag, then the <code>appletviewer</code> command does nothing. For details about the HTML tags that the <code>appletviewer</code> command supports, see AppletViewer Tags at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/tools/appletviewertags.html">http://docs.oracle.com/javase/8/docs/technotes/tools/appletviewertags.html</a> </p>
<p> The <code>appletviewer</code> command requires encoded URLs according to the escaping mechanism defined in RFC2396. Only encoded URLs are supported. However, file names must be unencoded, as specified in RFC2396. </p>
<p> <i>Note:</i> The <code>appletviewer</code> command is intended for development purposes only. For more information, see About Sample/Test Applications and Code at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/samples/aboutCodeSamples.html">http://docs.oracle.com/javase/8/docs/technotes/samples/aboutCodeSamples.html</a></p>
<h2>Options</h2>
<dl>
<dt>-debug</p>
<dd>Starts the Applet Viewer in the Java debugger with the <code>jdb</code> command to debug the applets in the document.</p>
<dt>-encoding <i>encoding-name</i></p>
<dd>Specifies the input HTML file encoding name.</p>
<dt>-J<i>javaoption</i></p>
<dd>Passes the string <code>javaoption</code> as a single argument to the Java interpreter, which runs the Applet Viewer. The argument should not contain spaces. Multiple argument words must all begin with the prefix <code>-J</code>. This is useful for adjusting the compiler&#8217;s execution environment or memory usage.</dl>
