---
title: "shtool-slo(1)"
name: "shtool-slo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-slo/"
description: "shtool slo – GNU shtool separate linker options by library class"
---

<h2 class="name">NAME</h2>
<p> shtool slo &#8211; GNU shtool separate linker options by library class </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool slo</code> [<code>-p</code>|<code>&#8211;prefix</code> <i>str</i>] &#8212; <code>-L</code><i>dir</i> <code>-l</code><i>lib</i> [<code>-L</code><i>dir</i> <code>-l</code><i>lib</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This command separates the linker options &#8220;<code>-L</code>&#8221; and &#8220;<code>-l</code>&#8221; by library class. It&#8217;s argument line can actually be an arbitrary command line where those options are contained. <code>slo</code> parses these two options only and ignores the remaining contents. The result is a trivial shell script on <tt>&quot;stdout&quot;</tt> which defines six variables containing the &#8220;<code>-L</code>&#8221; and &#8220;<code>-l</code>&#8221; options sorted by class: </p>
<p> &#8220;<tt>&quot;SLO_DIRS_OBJ&quot;</tt>&#8221; and &#8220;<tt>&quot;SLO_LIBS_OBJ&quot;</tt>&#8221; contains the &#8220;<code>-L</code>&#8221; and &#8220;<code>-l</code>&#8221; options of static libraries, &#8220;<tt>&quot;SLO_DIRS_PIC&quot;</tt>&#8221; and &#8220;<tt>&quot;SLO_LIBS_PIC&quot;</tt>&#8221; contains the &#8220;<code>-L</code>&#8221; and &#8220;<code>-l</code>&#8221; options of static libraries containing <font SIZE="-1">PIC </font>(&#8220;Position Independent Code&#8221;) and &#8220;<tt>&quot;SLO_DIRS_DSO&quot;</tt>&#8221; and &#8220;<tt>&quot;SLO_LIBS_DSO&quot;</tt>&#8221; contains the &#8220;<code>-L</code>&#8221; and &#8220;<code>-l</code>&#8221; options of shared libraries. The <code>-p</code> option can be used to change the default variable prefix from &quot;<tt>&quot;SLO_&quot;</tt>&quot; to <i>str</i>. </p>
<p> The intent of this separation is to provide a way between static and shared libraries which is important if one wants to link custom DSOs against libraries, because not all platforms all one to link these DSOs against shared libraries. So one first has to separate out the shared libraries and link the <font SIZE="-1">DSO</font> only against the static libraries. One can use this command also to just sort the options.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-p</code>, <code>&#8211;prefix</code> <i>str</i></p>
<dd>
<pre>
    FIXME
</pre>
<dt><code>-L</code><i>dir</i></p>
<dd> Directory where libraries are searched in.</p>
<dt><code>-l</code><i>lib</i></p>
<dd> Library to search for.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   configure.in
 LINK_STD=&quot;$LDFLAGS $LIBS&quot;
 eval `shtool slo $LINK_STD`
 LINK_DSO=&quot;$SLO_DIRS_OBJ $SLO_LIBS_OBJ $SLO_DIRS_PIC $SLO_LIBS_PIC&quot;
   :
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>slo</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <code>Apache</code>. It was later taken over into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1). </p>
<h2>Index</h2>
