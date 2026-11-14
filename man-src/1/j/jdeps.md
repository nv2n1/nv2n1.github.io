---
title: "jdeps(1)"
name: "jdeps"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jdeps/"
description: "jdeps – Java class dependency analyzer."
---

<h2>NAME</h2>
<p> jdeps &#8211; Java class dependency analyzer.</p>
<h2>SYNOPSIS</h2>
<pre>
<code>jdeps</code> [<i>options</i>] <i>classes</i> ...
</pre>
<dl>
<dt><i>options</i></p>
<dd> Command-line options. See Options.</p>
<dt><i>classes</i></p>
<dd> Name of the classes to analyze. You can specify a class that can be found in the class path, by its file name, a directory, or a JAR file.</dl>
<h2>DESCRIPTION</h2>
<p> The <i></i><code>jdeps</code> command shows the package-level or class-level dependencies of Java class files. The input class can be a path name to a <code>.class</code> file, a directory, a JAR file, or it can be a fully qualified class name to analyze all class files. The options determine the output. By default, <code>jdeps</code> outputs the dependencies to the system output. It can generate the dependencies in DOT language (see the <code>-dotoutput</code> option).</p>
<h2>OPTIONS</h2>
<dl>
<dt>-dotoutput &lt;<i>dir</i>&gt;</p>
<dd>
 Destination directory for DOT file output. If specified, <code>jdeps</code> will generate one dot file per each analyzed archive named &lt;<i>archive-file-name</i>&gt;.dot listing the dependencies, and also a summary file named summary.dot listing the dependencies among the archives.</p>
<dt>-s, -summary</p>
<dd>
 Prints dependency summary only.</p>
<dt>-v, -verbose</p>
<dd>
 Prints all class-level dependencies.</p>
<dt>-verbose:package</p>
<dd>
 Prints package-level dependencies excluding dependencies within the same archive.</p>
<dt>-verbose:class</p>
<dd>
 Prints class-level dependencies excluding dependencies within the same archive.</p>
<dt>-cp &lt;<i>path</i>&gt;, -classpath &lt;<i>path</i>&gt;</p>
<dd>
 Specifies where to find class files. </p>
<p> See also Setting the Class Path.</p>
<dt>-p &lt;<i>pkg name</i>&gt;, -package &lt;<i>pkg name</i>&gt;</p>
<dd>
 Finds dependencies in the specified package. You can specify this option multiple times for different packages. The <code>-p</code> and <code>-e</code> options are mutually exclusive.</p>
<dt>-e &lt;<i>regex</i>&gt;, -regex &lt;<i>regex</i>&gt;</p>
<dd>
 Finds dependencies in packages matching the specified regular expression pattern. The <code>-p</code> and <code>-e</code> options are mutually exclusive.</p>
<dt>-include &lt;<i>regex</i>&gt;</p>
<dd>
 Restricts analysis to classes matching pattern. This option filters the list of classes to be analyzed. It can be used together with <code>-p</code> and <code>-e</code> which apply pattern to the dependencies.</p>
<dt>-jdkinternals</p>
<dd>
 Finds class-level dependences in JDK internal APIs. By default, it analyzes all classes specified in the <code>-classpath</code> option and in input files unless you specified the <code>-include</code> option. You cannot use this option with the <code>-p</code>, <code>-e</code>, and <code>-s</code> options. </p>
<p> <i>Warning</i>: JDK internal APIs may not be accessible in upcoming releases.</p>
<dt>-P, -profile</p>
<dd>
 Shows profile or the file containing a package.</p>
<dt>-apionly</p>
<dd>
 Restricts analysis to APIs, for example, dependences from the signature of <code>public</code> and <code>protected</code> members of public classes including field type, method parameter types, returned type, and checked exception types.</p>
<dt>-R, -recursive</p>
<dd>
 Recursively traverses all dependencies.</p>
<dt>-version</p>
<dd>
 Prints version information.</p>
<dt>-h, -?, -help</p>
<dd>
 Prints help message for <code>jdeps</code>.</dl>
<h2>EXAMPLES</h2>
<p> Analyzing the dependencies of Notepad.jar. </p>
<pre>
<code>$ jdeps demo/jfc/Notepad/Notepad.jar</code>
</pre>
<pre>
</pre>
<pre>
<code>demo/jfc/Notepad/Notepad.jar -&gt; /usr/java/jre/lib/rt.jar</code>
</pre>
<pre>
<code>   &lt;unnamed&gt; (Notepad.jar)</code>
</pre>
<pre>
<code>      -&gt; java.awt                                           </code>
</pre>
<pre>
<code>      -&gt; java.awt.event                                     </code>
</pre>
<pre>
<code>      -&gt; java.beans                                         </code>
</pre>
<pre>
<code>      -&gt; java.io                                            </code>
</pre>
<pre>
<code>      -&gt; java.lang                                          </code>
</pre>
<pre>
<code>      -&gt; java.net                                           </code>
</pre>
<pre>
<code>      -&gt; java.util                                          </code>
</pre>
<pre>
<code>      -&gt; java.util.logging                                  </code>
</pre>
<pre>
<code>      -&gt; javax.swing                                        </code>
</pre>
<pre>
<code>      -&gt; javax.swing.border                                 </code>
</pre>
<pre>
<code>      -&gt; javax.swing.event                                  </code>
</pre>
<pre>
<code>      -&gt; javax.swing.text                                   </code>
</pre>
<pre>
<code>      -&gt; javax.swing.tree                                   </code>
</pre>
<pre>
<code>      -&gt; javax.swing.undo  </code>
</pre>
<pre>
</pre>
<p> Use -P or -profile option to show on which profile that Notepad depends. </p>
<pre>
<code>$ jdeps -profile demo/jfc/Notepad/Notepad.jar </code>
</pre>
<pre>
<code>demo/jfc/Notepad/Notepad.jar -&gt; /usr/java/jre/lib/rt.jar (Full JRE)</code>
</pre>
<pre>
<code>   &lt;unnamed&gt; (Notepad.jar)</code>
</pre>
<pre>
<code>      -&gt; java.awt                                           Full JRE</code>
</pre>
<pre>
<code>      -&gt; java.awt.event                                     Full JRE</code>
</pre>
<pre>
<code>      -&gt; java.beans                                         Full JRE</code>
</pre>
<pre>
<code>      -&gt; java.io                                            compact1</code>
</pre>
<pre>
<code>      -&gt; java.lang                                          compact1</code>
</pre>
<pre>
<code>      -&gt; java.net                                           compact1</code>
</pre>
<pre>
<code>      -&gt; java.util                                          compact1</code>
</pre>
<pre>
<code>      -&gt; java.util.logging                                  compact1</code>
</pre>
<pre>
<code>      -&gt; javax.swing                                        Full JRE</code>
</pre>
<pre>
<code>      -&gt; javax.swing.border                                 Full JRE</code>
</pre>
<pre>
<code>      -&gt; javax.swing.event                                  Full JRE</code>
</pre>
<pre>
<code>      -&gt; javax.swing.text                                   Full JRE</code>
</pre>
<pre>
<code>      -&gt; javax.swing.tree                                   Full JRE</code>
</pre>
<pre>
<code>      -&gt; javax.swing.undo                                   Full JRE</code>
</pre>
<pre>
</pre>
<p> Analyzing the immediate dependencies of a specific class in a given classpath, for example the <code>com.sun.tools.jdeps.Main</code> class in the tools.jar file. </p>
<pre>
<code>$ jdeps -cp lib/tools.jar com.sun.tools.jdeps.Main</code>
</pre>
<pre>
<code>lib/tools.jar -&gt; /usr/java/jre/lib/rt.jar</code>
</pre>
<pre>
<code>   com.sun.tools.jdeps (tools.jar)</code>
</pre>
<pre>
<code>      -&gt; java.io                                            </code>
</pre>
<pre>
<code>      -&gt; java.lang </code>
</pre>
<pre>
</pre>
<p> Use the <code>-verbose:class</code> option to find class-level dependencies or use the <code>-v</code> or <code>-verbose</code> option to include dependencies from the same JAR file. </p>
<pre>
<code>$ jdeps -verbose:class -cp lib/tools.jar com.sun.tools.jdeps.Main</code>
</pre>
<pre>
</pre>
<pre>
<code>lib/tools.jar -&gt; /usr/java/jre/lib/rt.jar</code>
</pre>
<pre>
<code>   com.sun.tools.jdeps.Main (tools.jar)</code>
</pre>
<pre>
<code>      -&gt; java.io.PrintWriter                                </code>
</pre>
<pre>
<code>      -&gt; java.lang.Exception                                </code>
</pre>
<pre>
<code>      -&gt; java.lang.Object                                   </code>
</pre>
<pre>
<code>      -&gt; java.lang.String                                   </code>
</pre>
<pre>
<code>      -&gt; java.lang.System </code>
</pre>
<pre>
</pre>
<p> Use the <code>-R</code> or <code>-recursive</code> option to analyze the transitive dependencies of the <code>com.sun.tools.jdeps.Main</code> class. </p>
<pre>
<code>$ jdeps -R -cp lib/tools.jar com.sun.tools.jdeps.Main</code>
</pre>
<pre>
<code>lib/tools.jar -&gt; /usr/java/jre/lib/rt.jar</code>
</pre>
<pre>
<code>   com.sun.tools.classfile (tools.jar)</code>
</pre>
<pre>
<code>      -&gt; java.io                                            </code>
</pre>
<pre>
<code>      -&gt; java.lang                                          </code>
</pre>
<pre>
<code>      -&gt; java.lang.reflect                                  </code>
</pre>
<pre>
<code>      -&gt; java.nio.charset                                   </code>
</pre>
<pre>
<code>      -&gt; java.nio.file                                      </code>
</pre>
<pre>
<code>      -&gt; java.util                                          </code>
</pre>
<pre>
<code>      -&gt; java.util.regex                                    </code>
</pre>
<pre>
<code>   com.sun.tools.jdeps (tools.jar)</code>
</pre>
<pre>
<code>      -&gt; java.io                                            </code>
</pre>
<pre>
<code>      -&gt; java.lang                                          </code>
</pre>
<pre>
<code>      -&gt; java.nio.file                                      </code>
</pre>
<pre>
<code>      -&gt; java.nio.file.attribute                            </code>
</pre>
<pre>
<code>      -&gt; java.text                                          </code>
</pre>
<pre>
<code>      -&gt; java.util                                          </code>
</pre>
<pre>
<code>      -&gt; java.util.jar                                      </code>
</pre>
<pre>
<code>      -&gt; java.util.regex                                    </code>
</pre>
<pre>
<code>      -&gt; java.util.zip                                      </code>
</pre>
<pre>
<code>/usr/java/jre/lib/jce.jar -&gt; /usr/java/jre/lib/rt.jar</code>
</pre>
<pre>
<code>   javax.crypto (jce.jar)</code>
</pre>
<pre>
<code>      -&gt; java.io                                            </code>
</pre>
<pre>
<code>      -&gt; java.lang                                          </code>
</pre>
<pre>
<code>      -&gt; java.lang.reflect                                  </code>
</pre>
<pre>
<code>      -&gt; java.net                                           </code>
</pre>
<pre>
<code>      -&gt; java.nio                                           </code>
</pre>
<pre>
<code>      -&gt; java.security                                      </code>
</pre>
<pre>
<code>      -&gt; java.security.cert                                 </code>
</pre>
<pre>
<code>      -&gt; java.security.spec                                 </code>
</pre>
<pre>
<code>      -&gt; java.util                                          </code>
</pre>
<pre>
<code>      -&gt; java.util.concurrent                               </code>
</pre>
<pre>
<code>      -&gt; java.util.jar                                      </code>
</pre>
<pre>
<code>      -&gt; java.util.regex                                    </code>
</pre>
<pre>
<code>      -&gt; java.util.zip                                      </code>
</pre>
<pre>
<code>      -&gt; javax.security.auth                                </code>
</pre>
<pre>
<code>      -&gt; sun.security.jca                                   JDK internal API (rt.jar)</code>
</pre>
<pre>
<code>      -&gt; sun.security.util                                  JDK internal API (rt.jar)</code>
</pre>
<pre>
<code>   javax.crypto.spec (jce.jar)</code>
</pre>
<pre>
<code>      -&gt; java.lang                                          </code>
</pre>
<pre>
<code>      -&gt; java.security.spec                                 </code>
</pre>
<pre>
<code>      -&gt; java.util                                          </code>
</pre>
<pre>
<code>/usr/java/jre/lib/rt.jar -&gt; /usr/java/jre/lib/jce.jar</code>
</pre>
<pre>
<code>   java.security (rt.jar)</code>
</pre>
<pre>
<code>      -&gt; javax.crypto</code>
</pre>
<pre>
</pre>
<p> Generate dot files of the dependencies of Notepad demo. </p>
<pre>
<code>$ jdeps -dotoutput dot demo/jfc/Notepad/Notepad.jar</code>
</pre>
<pre>
</pre>
<p> <code>jdeps</code> will create one dot file for each given JAR file named &lt;<i>filename</i>&gt;.dot in the dot directory specified in the <code>-dotoutput</code> option, and also a summary file named summary.dot that will list the dependencies among the JAR files </p>
<pre>
<code>$ cat dot/Notepad.jar.dot </code>
</pre>
<pre>
<code>digraph &quot;Notepad.jar&quot; {</code>
</pre>
<pre>
<code>    // Path: demo/jfc/Notepad/Notepad.jar</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.awt&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.awt.event&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.beans&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.io&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.lang&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.net&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.util&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;java.util.logging&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;javax.swing&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;javax.swing.border&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;javax.swing.event&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;javax.swing.text&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;javax.swing.tree&quot;;</code>
</pre>
<pre>
<code>   &quot;&lt;unnamed&gt;&quot;                                        -&gt; &quot;javax.swing.undo&quot;;</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<pre>
<code>$ cat dot/summary.dot</code>
</pre>
<pre>
<code>digraph &quot;summary&quot; {</code>
</pre>
<pre>
<code>   &quot;Notepad.jar&quot;                  -&gt; &quot;rt.jar&quot;;</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-javap/">javap</a>(1) </p>
</dl>
<h2>Index</h2>
