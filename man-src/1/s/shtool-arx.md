---
title: "shtool-arx(1)"
name: "shtool-arx"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-arx/"
description: "shtool arx – GNU shtool"
---

<h2 class="name">NAME</h2>
<p> shtool arx &#8211; GNU shtool </p>
<p><a href="/docs/linux/man/1-ar/">ar</a>(1) extensional command</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool arx</code> [<code>-t</code>|<code>&#8211;trace</code>] [<code>-C</code>|<code>&#8211;command</code> <i>cmd</i>] <i>op</i> <i>archive</i> <i>file</i> [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>shtool arx</code> is a wrapper around the archiving tool <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1). It provides the ability to create archives out of existing archives, i.e., if one of <i>file</i> matches &quot;<tt>&quot;*.a&quot;</tt>&quot;, the archive member files of <i>file</i> are used instead of <i>file</i> itself. </p>
<p> The trick of this command is the automatic handling of archive members which is especially interesting if one wants to construct a (usually top-level) library archive out of pre-built sub-library archives (usually staying inside subdirs) in a large source tree. For <font SIZE="-1"><code>GNU</code></font><code> libtool</code> based projects, a similar functionality is provided by <font SIZE="-1"><code>GNU</code></font><code> libtool</code> internally, too.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Shows the actually involved shell commands.</p>
<dt><code>-C</code>, <code>&#8211;command</code> <i>cmd</i></p>
<dd> Set the used <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1) command to <i>cmd</i> instead of just &#8220;ar&#8221; (searched in <tt>$PATH</tt>).</dl>
<h2>EXAMPLE</h2>
<pre>
 #   Makefile
 AR=ar
 RANLIB=ranlib
   :
 OBJS=foo.o bar.o
 LIBS=baz/libbaz.a quux/libquux.a
   :
 libfoo.a: $(OBJS) $(LIBS)
     shtool arx -C $(AR) rc libfoo.a $(OBJS) $(LIBS)
     $(RANLIB) libfoo.a
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>arx</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1999 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>. It was prompted by need to build libraries out of sub-libraries inside the <font SIZE="-1"><code>OSSP</code></font> project.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1). </p>
<h2>Index</h2>
