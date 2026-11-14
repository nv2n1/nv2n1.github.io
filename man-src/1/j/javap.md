---
title: "javap(1)"
name: "javap"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javap/"
description: "javap – Disassembles one or more class files."
---

<h2 class="name">NAME</h2>
<p> javap &#8211; Disassembles one or more class files. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>
<pre>
<code>javap</code> [<i>options</i>] <i>classfile</i>...
</pre>
</dl>
<p> <i>options</i></p>
<dl>
<dt>
<dd> The command-line options. See Options.</dl>
<p> <i>classfile</i></p>
<dl>
<dt>
<dd> One or more classes separated by spaces to be processed for annotations such as DocFooter.class. You can specify a class that can be found in the class path, by its file name or with a URL such as <code>file:///home/user/myproject/src/DocFooter.class</code>.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>javap</code> command disassembles one or more class files. The output depends on the options used. When no options are used, then the <code>javap</code> command prints the package, protected and public fields, and methods of the classes passed to it. The <code>javap</code> command prints its output to <code>stdout</code>.</p>
<h2>OPTIONS</h2>
<p> -help<br />
 &#8211;help<br />
 -?</p>
<dl>
<dt>
<dd> Prints a help message for the <code>javap</code> command.</dl>
<p> -version</p>
<dl>
<dt>
<dd> Prints release information.</dl>
<p> -l</p>
<dl>
<dt>
<dd> Prints line and local variable tables.</dl>
<p> -public</p>
<dl>
<dt>
<dd> Shows only public classes and members.</dl>
<p> -protected</p>
<dl>
<dt>
<dd> Shows only protected and public classes and members.</dl>
<p> -private<br />
 -p</p>
<dl>
<dt>
<dd> Shows all classes and members.</dl>
<p> -J<i>option</i></p>
<dl>
<dt>
<dd> Passes the specified option to the JVM. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>javap -J-version</code>
<code>javap -J-Djava.security.manager -J-Djava.security.policy=MyPolicy MyClassName</code>
 
</pre>
</dl>
<p> For more information about JVM options, see the command documentation.</dl>
<p> -s</p>
<dl>
<dt>
<dd> Prints internal type signatures.</dl>
<p> -sysinfo</p>
<dl>
<dt>
<dd> Shows system information (path, size, date, MD5 hash) of the class being processed.</dl>
<p> -constants</p>
<dl>
<dt>
<dd> Shows <code>static final</code> constants.</dl>
<p> -c</p>
<dl>
<dt>
<dd> Prints disassembled code, for example, the instructions that comprise the Java bytecodes, for each of the methods in the class.</dl>
<p> -verbose</p>
<dl>
<dt>
<dd> Prints stack size, number of locals and arguments for methods.</dl>
<p> -classpath <i>path</i></p>
<dl>
<dt>
<dd> Specifies the path the <code>javap</code> command uses to look up classes. Overrides the default or the <code>CLASSPATH</code> environment variable when it is set.</dl>
<p> -bootclasspath <i>path</i></p>
<dl>
<dt>
<dd> Specifies the path from which to load bootstrap classes. By default, the bootstrap classes are the classes that implement the core Java platform located in <code>jre/lib/rt.jar</code> and several other JAR files.</dl>
<p> -extdir <i>dirs</i></p>
<dl>
<dt>
<dd> Overrides the location at which installed extensions are searched for. The default location for extensions is the value of <code>java.ext.dirs</code>.</dl>
<h2>EXAMPLE</h2>
<p> Compile the following <code>DocFooter</code> class: </p>
<dl>
<dt>
<dd>
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
</dl>
<p> The output from the <code>javap DocFooter.class</code> command yields the following: </p>
<dl>
<dt>
<dd>
Compiled from &#8220;DocFooter.java&#8221; public class DocFooter extends java.applet.Applet<br />
{<br />
    java.lang.String date;<br />
    java.lang.String email;<br />
  public<br />
    DocFooter();<br />
  public<br />
    void init();<br />
  public<br />
    void paint(java.awt.Graphics);<br />
}
</dl>
<p> The output from <code>javap -c DocFooter.class</code> command yields the following: </p>
<dl>
<dt>
<dd>
<pre><code>
Compiled from "DocFooter.java" public class DocFooter extends java.applet.Applet
{
    java.lang.String date;
    java.lang.String email;

  public
    DocFooter();
Code:
    0 : aload_0 1 : invokespecial #1 // Method
                    java /
                    applet / Applet."&lt;init&gt;" : () V 4 : return

                                                        public void
                                                        init();
Code:
    0 : aload_0 1 : sipush 500 4 : bipush 100 6 : invokevirtual #2                                    // Method resize:(II)V
                                                  9 : aload_0 10 : aload_0 11 : ldc #3                // String LAST_UPDATED
                                                                                13 : invokevirtual #4 // Method
                                                                                     getParameter : (Ljava / lang / String;) Ljava /
                                                                                                    lang / String;
    16 : putfield #5                                          // Field date:Ljava/lang/String;
         19 : aload_0 20 : aload_0 21 : ldc #6                // String EMAIL
                                        23 : invokevirtual #4 // Method
                                             getParameter : (Ljava / lang / String;) Ljava /
                                                            lang / String;
    26 : putfield #7 // Field email:Ljava/lang/String;
         29 : return

              public void paint(java.awt.Graphics);
Code:
    0 : aload_1 1 : new #8                       // class java/lang/StringBuilder
                    4 : dup 5 : invokespecial #9 // Method
                                java /
                                lang / StringBuilder."&lt;init&gt;" : () V 8 : aload_0 9 : getfield #5            // Field date:Ljava/lang/String;
                                                                                     12 : invokevirtual #10 // Method
                                                                                          java /
                                lang / StringBuilder.append : (Ljava / lang / String;) Ljava / lang / StringBuilder;
    15 : ldc #11                // String  by
         17 : invokevirtual #10 // Method
              java /
              lang / StringBuilder.append : (Ljava / lang / String;) Ljava / lang / StringBuilder;
    20 : invokevirtual #12 // Method
         java /
         lang / StringBuilder.toString : () Ljava / lang / String;
    23 : bipush 100 25 : bipush 15 27 : invokevirtual #13 // Method
                                        java /
                                        awt / Graphics.drawString : (Ljava / lang / String; II) V 30 : aload_1 31 : aload_0 32 : getfield #7                                           // Field email:Ljava/lang/String;
                                                                                                                                 35 : sipush 290 38 : bipush 15 40 : invokevirtual #13 // Method
                                                                                                                                                                     java /
                                        awt / Graphics.drawString : (Ljava / lang / String; II) V 43 : return
}
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-java/">java</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-javac/">javac</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-javadoc/">javadoc</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-jdb/">jdb</a>(1)</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-jdeps/">jdeps</a>(1)</dl>
<h2>Index</h2>
