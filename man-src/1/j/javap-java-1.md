---
title: "javap-java-1(1)"
name: "javap-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javap-java-1/"
description: "javap – The Java Class File Disassembler"
---

<h2>Name</h2>
<p> javap &#8211; The Java Class File Disassembler </p>
<p> Disassembles class files. </p>
<h2>SYNOPSIS</h2>
<pre>
<code>javap [ </code><code>options</code><code> ] classes</code>
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>javap</code> command disassembles one or more class files. Its output depends on the options used. If no options are used, <code>javap</code> prints out the package, protected, and public fields and methods of the classes passed to it. <code>javap</code> prints its output to stdout. </p>
<dl>
<dt>
<dd>
<dl>
<dt>options</p>
<dd> Command-line options.</p>
<dt>classes</p>
<dd> List of one or more classes (separated by spaces) to be processed for annotations (such as <i>DocFooter.class</i>). You may specify a class that can be found in the class path, by its file name (for example, <i>/home/user/myproject/src/DocFooter.class</i>), or with a URL (for example, <i>file:///home/user/myproject/src/DocFooter.class</i>).</dl>
</dl>
<p> For example, compile the following class declaration: </p>
<pre><code>
import java.awt.*;
import java.applet.*;
public
class DocFooter extends Applet
{
    String date;
    String email;
  public
    void init()
    {
        resize(500, 100);
        date = getParameter("LAST_UPDATED");
        email = getParameter("EMAIL");
    }
  public
    void paint(Graphics g)
    {
        g.drawString(date + " by ", 100, 15);
        g.drawString(email, 290, 15);
    }
}
</code></pre>
<p> The output from <code>javap DocFooter.class</code> yields: </p>
<p>Compiled from &#8220;DocFooter.java&#8221; public class DocFooter extends java.applet.Applet<br />
{<br />
    java.lang.String date;<br />
    java.lang.String email;<br />
  public<br />
    DocFooter();<br />
  public<br />
    void init();<br />
  public<br />
    void paint(java.awt.Graphics);<br />
}</p>
<p> The output from <code>javap -c DocFooter.class</code> yields: </p>
<pre><code>
Compiled from "DocFooter.java" public class DocFooter extends java.applet.Applet
{
    java.lang.String date;
    java.lang.String email;
  public
    DocFooter();
Code:
    0 : aload_0 1 : invokespecial #1 // Method java/applet/Applet."&lt;init&gt;":()V
                    4 : return public void
                        init();
Code:
    0 : aload_0 1 : sipush 500 4 : bipush 100 6 : invokevirtual #2                                                                             // Method resize:(II)V
                                                  9 : aload_0 10 : aload_0 11 : ldc #3                                                         // String LAST_UPDATED
                                                                                13 : invokevirtual #4                                          // Method getParameter:(Ljava/lang/String;)Ljava/lang/String;
                                                                                     16 : putfield #5                                          // Field date:Ljava/lang/String;
                                                                                          19 : aload_0 20 : aload_0 21 : ldc #6                // String EMAIL
                                                                                                                         23 : invokevirtual #4 // Method getParameter:(Ljava/lang/String;)Ljava/lang/String;
                                                                                                                              26 : putfield #7 // Field email:Ljava/lang/String;
                                                                                                                                   29 : return public void paint(java.awt.Graphics);
Code:
    0 : aload_1 1 : new #8                                                                                                                                                                   // class java/lang/StringBuilder
                    4 : dup 5 : invokespecial #9                                                                                                                                             // Method java/lang/StringBuilder."&lt;init&gt;":()V
                                8 : aload_0 9 : getfield #5                                                                                                                                  // Field date:Ljava/lang/String;
                                                12 : invokevirtual #10                                                                                                                       // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
                                                     15 : ldc #11                                                                                                                            // String  by
                                                          17 : invokevirtual #10                                                                                                             // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
                                                               20 : invokevirtual #12                                                                                                        // Method java/lang/StringBuilder.toString:()Ljava/lang/String;
                                                                    23 : bipush 100 25 : bipush 15 27 : invokevirtual #13                                                                    // Method java/awt/Graphics.drawString:(Ljava/lang/String;II)V
                                                                                                        30 : aload_1 31 : aload_0 32 : getfield #7                                           // Field email:Ljava/lang/String;
                                                                                                                                       35 : sipush 290 38 : bipush 15 40 : invokevirtual #13 // Method java/awt/Graphics.drawString:(Ljava/lang/String;II)V
                                                                                                                                                                           43 : return
}
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>-help &#8211;help -?</p>
<dd> Prints out help message for <code>javap</code>.</p>
<dt>-version</p>
<dd> Prints out version information.</p>
<dt>-l</p>
<dd> Prints out line and local variable tables.</p>
<dt>-public</p>
<dd> Shows only public classes and members.</p>
<dt>-protected</p>
<dd> Shows only protected and public classes and members.</p>
<dt>-package</p>
<dd> Shows only package, protected, and public classes and members. This is the default.</p>
<dt>-private -p</p>
<dd> Shows all classes and members.</p>
<dt>-Jflag</p>
<dd> Pass <i>flag</i> directly to the runtime system. Some examples: </p>
<pre>
<code>javap -J-version
javap -J-Djava.security.manager -J-Djava.security.policy=MyPolicy MyClassName</code>
</pre>
<dt>-s</p>
<dd> Prints internal type signatures.</p>
<dt>-sysinfo</p>
<dd> Shows system information (path, size, date, MD5 hash) of the class being processed.</p>
<dt>-constants</p>
<dd> Shows static final constants.</p>
<dt>-c</p>
<dd> Prints out disassembled code, i.e., the instructions that comprise the Java bytecodes, for each of the methods in the class. These are documented in the <i>Java Virtual Machine Specification</i> @ <a rel="nofollow" href="http://java.sun.com/docs/books/vmspec/.">http://java.sun.com/docs/books/vmspec/.</a></p>
<dt>-verbose</p>
<dd> Prints stack size, number of <i>locals</i> and <i>args</i> for methods.</p>
<dt>-classpath path</p>
<dd> Specifies the path <code>javap</code> uses to look up classes. Overrides the default or the CLASSPATH environment variable if it is set.</p>
<dt>-bootclasspath path</p>
<dd> Specifies path from which to load bootstrap classes. By default, the bootstrap classes are the classes implementing the core Java platform located in <i>jre/lib/rt.jar</i> and several other jar files.</p>
<dt>-extdirs dirs</p>
<dd> Overrides location at which installed extensions are searched for. The default location for extensions is the value of <i>java.ext.dirs</i>.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-javac/">javac</a>(1), <a href="/docs/linux/man/1-java/">java</a>(1), <a href="/docs/linux/man/1-jdb/">jdb</a>(1), <a href="/docs/linux/man/1-javah/">javah</a>(1), <a href="/docs/linux/man/1-javadoc/">javadoc</a>(1) </p>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
