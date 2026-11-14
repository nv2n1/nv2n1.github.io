---
title: "javap-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "javap-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javap-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "javap – Disassembles one or more class files."
---

<p>javap &#8211; Disassembles one or more class files. </p>
<h2>Synopsis</h2>
<dl>
<dd>
<pre><code>javap</code> [<i>options</i>] <i>classfile</i>...</pre>
</dl>
<p> <i>options</i></p>
<dl>
<dd>The command-line options. See Options.</dl>
<p> <i>classfile</i></p>
<dl>
<dd>One or more classes separated by spaces to be processed for annotations such as DocFooter.class. You can specify a class that can be found in the class path, by its file name or with a URL such as <code>file:///home/user/myproject/src/DocFooter.class</code>.</dl>
<h2>Description</h2>
<p>The <code>javap</code> command disassembles one or more class files. The output depends on the options used. When no options are used, then the <code>javap</code> command prints the package, protected and public fields, and methods of the classes passed to it. The <code>javap</code> command prints its output to <code>stdout</code>.</p>
<h2>Options</h2>
<p>-help<br />
 &#8211;help<br />
 -?</p>
<dl>
<dd>Prints a help message for the <code>javap</code> command.</dl>
<p> -version</p>
<dl>
<dd>Prints release information.</dl>
<p> -l</p>
<dl>
<dd>Prints line and local variable tables.</dl>
<p> -public</p>
<dl>
<dd>Shows only public classes and members.</dl>
<p> -protected</p>
<dl>
<dd>Shows only protected and public classes and members.</dl>
<p> -private<br />
 -p</p>
<dl>
<dd>Shows all classes and members.</dl>
<p> -J<i>option</i></p>
<dl>
<dd>Passes the specified option to the JVM. For example: </p>
<dl>
<dd>
<pre><code>javap -J-version</code>
<code>javap -J-Djava.security.manager -J-Djava.security.policy=MyPolicy MyClassName</code></pre>
</dl>
<p> For more information about JVM options, see the command documentation.</dl>
<p> -s</p>
<dl>
<dd>Prints internal type signatures.</dl>
<p> -sysinfo</p>
<dl>
<dd>Shows system information (path, size, date, MD5 hash) of the class being processed.</dl>
<p> -constants</p>
<dl>
<dd>Shows <code>static final</code> constants.</dl>
<p> -c</p>
<dl>
<dd>Prints disassembled code, for example, the instructions that comprise the Java bytecodes, for each of the methods in the class.</dl>
<p> -verbose</p>
<dl>
<dd>Prints stack size, number of locals and arguments for methods.</dl>
<p> -classpath <i>path</i></p>
<dl>
<dd>Specifies the path the <code>javap</code> command uses to look up classes. Overrides the default or the <code>CLASSPATH</code> environment variable when it is set.</dl>
<p> -bootclasspath <i>path</i></p>
<dl>
<dd>Specifies the path from which to load bootstrap classes. By default, the bootstrap classes are the classes that implement the core Java platform located in <code>jre/lib/rt.jar</code> and several other JAR files.</dl>
<p> -extdir <i>dirs</i></p>
<dl>
<dd>Overrides the location at which installed extensions are searched for. The default location for extensions is the value of <code>java.ext.dirs</code>.</dl>
<h2>Example</h2>
<p>Compile the following <code>DocFooter</code> class: </p>
<dl>
<dd>
<pre><code>import java.awt.*;</code>
<code>import java.applet.*;</code>
<code>public class DocFooter extends Applet {</code>
<code> String date;</code>
<code> String email;</code>
<code> public void init() {</code>
<code> resize(500,100);</code>
<code> date = getParameter(&quot;LAST_UPDATED&quot;);</code>
<code> email = getParameter(&quot;EMAIL&quot;);</code>
<code> }</code>
<code> public void paint(Graphics g) {</code>
<code> g.drawString(date + &quot; by &quot;,100, 15);</code>
<code> g.drawString(email,290,15);</code>
<code> }</code>
<code>}</code></pre>
</dl>
<p> The output from the <code>javap DocFooter.class</code> command yields the following: </p>
<dl>
<dd>
<pre><code>Compiled from &quot;DocFooter.java&quot;</code>
<code>public class DocFooter extends java.applet.Applet {</code>
<code> java.lang.String date;</code>
<code> java.lang.String email;</code>
<code> public DocFooter();</code>
<code> public void init();</code>
<code> public void paint(java.awt.Graphics);</code>
<code>}</code></pre>
</dl>
<p> The output from <code>javap -c DocFooter.class</code> command yields the following: </p>
<dl>
<dd>
<pre><code>Compiled from &quot;DocFooter.java&quot;</code>
<code>public class DocFooter extends java.applet.Applet {</code>
<code> java.lang.String date;</code>
<code> java.lang.String email;</code>
 
<code> public DocFooter();</code>
<code> Code:</code>
<code> 0: aload_0 </code>
<code> 1: invokespecial #1 // Method</code>
<code>java/applet/Applet.&quot;&lt;init&gt;&quot;:()V</code>
<code> 4: return </code>
 
<code> public void init();</code>
<code> Code:</code>
<code> 0: aload_0 </code>
<code> 1: sipush 500</code>
<code> 4: bipush 100</code>
<code> 6: invokevirtual #2 // Method resize:(II)V</code>
<code> 9: aload_0 </code>
<code> 10: aload_0 </code>
<code> 11: ldc #3 // String LAST_UPDATED</code>
<code> 13: invokevirtual #4 // Method</code>
<code> getParameter:(Ljava/lang/String;)Ljava/lang/String;</code>
<code> 16: putfield #5 // Field date:Ljava/lang/String;</code>
<code> 19: aload_0 </code>
<code> 20: aload_0 </code>
<code> 21: ldc #6 // String EMAIL</code>
<code> 23: invokevirtual #4 // Method</code>
<code> getParameter:(Ljava/lang/String;)Ljava/lang/String;</code>
<code> 26: putfield #7 // Field email:Ljava/lang/String;</code>
<code> 29: return </code>
 
<code> public void paint(java.awt.Graphics);</code>
<code> Code:</code>
<code> 0: aload_1 </code>
<code> 1: new #8 // class java/lang/StringBuilder</code>
<code> 4: dup </code>
<code> 5: invokespecial #9 // Method</code>
<code> java/lang/StringBuilder.&quot;&lt;init&gt;&quot;:()V</code>
<code> 8: aload_0 </code>
<code> 9: getfield #5 // Field date:Ljava/lang/String;</code>
<code> 12: invokevirtual #10 // Method</code>
<code> java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;</code>
<code> 15: ldc #11 // String by </code>
<code> 17: invokevirtual #10 // Method</code>
<code> java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;</code>
<code> 20: invokevirtual #12 // Method</code>
<code> java/lang/StringBuilder.toString:()Ljava/lang/String;</code>
<code> 23: bipush 100</code>
<code> 25: bipush 15</code>
<code> 27: invokevirtual #13 // Method</code>
<code> java/awt/Graphics.drawString:(Ljava/lang/String;II)V</code>
<code> 30: aload_1 </code>
<code> 31: aload_0 </code>
<code> 32: getfield #7 // Field email:Ljava/lang/String;</code>
<code> 35: sipush 290</code>
<code> 38: bipush 15</code>
<code> 40: invokevirtual #13 // Method</code>
<code>java/awt/Graphics.drawString:(Ljava/lang/String;II)V</code>
<code> 43: return </code>
<code>}</code></pre>
</dl>
<h2>See Also</h2>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-java/">java</a>(1)</dl>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-javac/">javac</a>(1)</dl>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-javadoc/">javadoc</a>(1)</dl>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-javah/">javah</a>(1)</dl>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-jdb/">jdb</a>(1)</dl>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-jdeps/">jdeps</a>(1)</dl>
