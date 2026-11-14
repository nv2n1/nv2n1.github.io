---
title: "appletviewer-java-1-6-0-openjdk(1)"
name: "appletviewer-java-1-6-0-openjdk"
section: "1"
letter: "a"
url: "/docs/linux/man/1-appletviewer-java-1-6-0-openjdk/"
description: "appletviewer – The Java Applet Viewer"
---

<p>appletviewer &#8211; The Java Applet Viewer </p>
<p> The <code>appletviewer</code> command allows you to run applets outside of a web browser.</p>
<h2>Synopsis</h2>
<p><tt>appletviewer</tt> <i>[</i> <i>options</i> <i>] </i><i>urls</i> &#8230; </p>
<h2>Description</h2>
<p>The <code>appletviewer</code> command connects to the documents or resources designated by <i>urls</i> and displays each applet referenced by the documents in its own window. Note: if the documents referred to by <i>urls</i> do not reference any applets with the <i>OBJECT</i>, <i>EMBED</i>, or <i>APPLET</i> tag, then <code>appletviewer</code> does nothing. For details on the HTML tags that <code>appletviewer</code> supports, see <i>AppletViewer Tags</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/tools/appletviewertags.html.">http://java.sun.com/javase/6/docs/technotes/tools/appletviewertags.html.</a> </p>
<p> <code>Note:</code> The <code>appletviewer</code> requires encoded URLs according to the escaping mechanism defined in RFC2396. Only encoded URLs are supported. However, file names must be unencoded, as specified in RFC2396. </p>
<h2>Options</h2>
<dl>
<dt>-debug</p>
<dd>Starts the applet viewer in the Java debugger, <code>jdb</code>, thus allowing you to debug the applets in the document.</p>
<dt>-encoding &nbsp;<wbr> &nbsp;<wbr>encoding name</p>
<dd>Specify the input HTML file encoding name.</p>
<dt>-Jjavaoption</p>
<dd>Passes through the string <i>javaoption</i> as a single argument to the Java interpreter which runs the appletviewer. The argument should not contain spaces. Multiple argument words must all begin with the prefix <code>-J</code>, which is stripped. This is useful for adjusting the compiler&#8217;s execution environment or memory usage.</dl>
<p>&nbsp;<wbr></p>
