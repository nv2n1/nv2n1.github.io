---
title: "javap-java-1-6-0-openjdk(1)"
name: "javap-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javap-java-1-6-0-openjdk/"
description: "javap – The Java Class File Disassembler"
---

<p>javap &#8211; The Java Class File Disassembler </p>
<p> Disassembles class files.</p>
<h2>Synopsis</h2>
<pre><code>javap [ </code><code>options</code><code> ] class. . .</code></pre>
<h2>Description</h2>
<p>The <code>javap</code> command disassembles a class file. Its output depends on the options used. If no options are used, <code>javap</code> prints out the package, protected, and public fields and methods of the classes passed to it. <code>javap</code> prints its output to stdout. For example, compile the following class declaration: </p>
<dl>
<dd>
<pre><code>import java.awt.*;
import java.applet.*;
public class DocFooter extends Applet {
 String date;
 String email;
 public void init() {
 resize(500,100);
 date = getParameter(&quot;LAST_UPDATED&quot;);
 email = getParameter(&quot;EMAIL&quot;);
 }
 public void paint(Graphics g) {
 g.drawString(date + &quot; by &quot;,100, 15);
 g.drawString(email,290,15);
 }
}</code></pre>
</dl>
<p> The output from <code>javap DocFooter</code> yields: </p>
<dl>
<dd>
<pre><code>Compiled from DocFooter.java
public class DocFooter extends java.applet.Applet {
 java.lang.String date;
 java.lang.String email;
 public DocFooter();
 public void init();
 public void paint(java.awt.Graphics);
}</code></pre>
</dl>
<p> The output from <code>javap -c DocFooter</code> yields: </p>
<dl>
<dd>
<pre><code>Compiled from DocFooter.java
public class DocFooter extends java.applet.Applet {
 java.lang.String date;
 java.lang.String email;
 public DocFooter();
 public void init();
 public void paint(java.awt.Graphics);
}
Method DocFooter()
 0 aload_0
 1 invokespecial #1 &lt;Method java.applet.Applet()&gt;
 4 return
Method void init()
 0 aload_0
 1 sipush 500
 4 bipush 100
 6 invokevirtual #2 &lt;Method void resize(int, int)&gt;
 9 aload_0
 10 aload_0
 11 ldc #3 &lt;String &quot;LAST_UPDATED&quot;&gt;
 13 invokevirtual #4 &lt;Method java.lang.String getParameter(java.lang.String)&gt;
 16 putfield #5 &lt;Field java.lang.String date&gt;
 19 aload_0
 20 aload_0
 21 ldc #6 &lt;String &quot;EMAIL&quot;&gt;
 23 invokevirtual #4 &lt;Method java.lang.String getParameter(java.lang.String)&gt;
 26 putfield #7 &lt;Field java.lang.String email&gt;
 29 return
Method void paint(java.awt.Graphics)
 0 aload_1
 1 new #8 &lt;Class java.lang.StringBuffer&gt;
 4 dup
 5 invokespecial #9 &lt;Method java.lang.StringBuffer()&gt;
 8 aload_0
 9 getfield #5 &lt;Field java.lang.String date&gt;
 12 invokevirtual #10 &lt;Method java.lang.StringBuffer append(java.lang.String)&gt;
 15 ldc #11 &lt;String &quot; by &quot;&gt;
 17 invokevirtual #10 &lt;Method java.lang.StringBuffer append(java.lang.String)&gt;
 20 invokevirtual #12 &lt;Method java.lang.String toString()&gt;
 23 bipush 100
 25 bipush 15
 27 invokevirtual #13 &lt;Method void drawString(java.lang.String, int, int)&gt;
 30 aload_1
 31 aload_0
 32 getfield #7 &lt;Field java.lang.String email&gt;
 35 sipush 290
 38 bipush 15
 40 invokevirtual #13 &lt;Method void drawString(java.lang.String, int, int)&gt;
 43 return</code></pre>
</dl>
<h2>Options</h2>
<dl>
<dt>-help</p>
<dd>Prints out help message for <code>javap</code>.</p>
<dt>-l</p>
<dd>Prints out line and local variable tables.</p>
<dt>-b</p>
<dd>Ensures backward compatibility with <code>javap</code> in JDK 1.1.</p>
<dt>-public</p>
<dd>Shows only public classes and members.</p>
<dt>-protected</p>
<dd>Shows only protected and public classes and members.</p>
<dt>-package</p>
<dd>Shows only package, protected, and public classes and members. This is the default.</p>
<dt>-private</p>
<dd>Shows all classes and members.</p>
<dt>-Jflag</p>
<dd>Pass <i>flag</i> directly to the runtime system. Some examples:</p>
<dl>
<dd>
<pre><code>javap -J-version
javap -J-Djava.security.manager -J-Djava.security.policy=MyPolicy MyClassName</code></pre>
</dl>
<dt>-s</p>
<dd>Prints internal type signatures.</p>
<dt>-c</p>
<dd>Prints out disassembled code, i.e., the instructions that comprise the Java bytecodes, for each of the methods in the class. These are documented in the <i>Java Virtual Machine Specification</i> @ <a rel="nofollow" href="http://java.sun.com/docs/books/vmspec/.">http://java.sun.com/docs/books/vmspec/.</a></p>
<dt>-verbose</p>
<dd>Prints stack size, number of <i>locals</i> and <i>args</i> for methods.</p>
<dt>-classpath path</p>
<dd>Specifies the path <code>javap</code> uses to look up classes. Overrides the default or the CLASSPATH environment variable if it is set. Directories are separated by colons. Thus the general format for <i>path</i> is: </p>
<pre><code> .:&lt;your_path&gt;</code></pre>
<p>For example:</p>
<dt>-bootclasspath path</p>
<dd>Specifies path from which to load bootstrap classes. By default, the bootstrap classes are the classes implementing the core Java platform located in <i>jre/lib/rt.jar</i> and several other jar files.</p>
<dt>-extdirs dirs</p>
<dd>Overrides location at which installed extensions are searched for. The default location for extensions is the value of <i>java.ext.dirs</i>.</dl>
<h2>Environment Variables</h2>
<dl>
<dt>CLASSPATH</p>
<dd>Used to provide the system a path to user-defined classes. Directories are separated by colons, for example, For example:</p>
<dl>
<dd></dl>
</dl>
<h2>See Also</h2>
<p>javac, java, jdb, javah, javadoc </p>
<p>&nbsp;<wbr></p>
