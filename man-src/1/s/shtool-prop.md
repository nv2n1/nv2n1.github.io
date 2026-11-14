---
title: "shtool-prop(1)"
name: "shtool-prop"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-prop/"
description: "shtool prop – GNU shtool propeller processing indication"
---

<h2 class="name">NAME</h2>
<p> shtool prop &#8211; GNU shtool propeller processing indication </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool prop</code> [<code>-p</code>|<code>&#8211;prefix</code> <i>str</i>]</p>
<h2>DESCRIPTION</h2>
<p> This command displays a processing indication though a running propeller. It is intended to be run at the end of a pipe (&quot;<tt>&quot;|&quot;</tt>&quot;) sequence where on <tt>&quot;stdin&quot;</tt> logging/processing informations found. For every line on <tt>&quot;stdin&quot;</tt> the propeller advances one step clock-wise.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-p</code>, <code>&#8211;prefix</code> <i>str</i></p>
<dd> Set a particular prefix <i>str</i> which is displayed in front of the propeller. The default is no prefix string.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 configure 2&gt;&amp;1 |\
     tee logfile |\
     shtool prop -p &quot;Configuring sources&quot;
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>prop</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <code>mod_ssl</code>. It was later taken over into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1). </p>
<h2>Index</h2>
