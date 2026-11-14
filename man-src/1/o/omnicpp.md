---
title: "omnicpp(1)"
name: "omnicpp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-omnicpp/"
description: "omnicpp – OmniORB cpp preprocessor for IDL compiler"
---

<h2 class="name">NAME</h2>
<p> omnicpp &#8211; OmniORB cpp preprocessor for IDL compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>omnicpp</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>omnicpp</code> command. </p>
<p> <code>omniidl</code> is omniORBs IDL compiler and uses <code>omnicpp</code> as it&#8217;s C preprocessor. <code>omnicpp</code> is really just the GNU C preprocessor under a different name. Normally you should not need to invoke this directly but should use <code>omniidl</code> instead.</p>
<h2>OPTIONS</h2>
<p> As this is just the GNU C preprocessor <code>cpp</code> you can see that program for the full options. Normally you should not be invoking this directly but should use <code>omniidl</code> instead. The options listed here should really be given to <code>omniidl</code>, but they are passed straight to <code>omnicpp</code>.</p>
<dl>
<dt><code>-D</code><i>&nbsp;<wbr>name</i></p>
<dd> Define <i>name</i> for the preprocessor.</p>
<dt><code>-U</code><i>&nbsp;<wbr>name</i></p>
<dd> Undefine <i>name</i> for the preprocessor.</p>
<dt><code>-I</code><i>&nbsp;<wbr>dir</i></p>
<dd> Include <i>dir</i> in the preprocessor search path. Note that the current directory is not on the include search path by default. Use <i>-I.</i> for that.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-omniidl/">omniidl</a></code>(1).<br />
 The programs are documented fully by the HTML documentation in the omniorb4-doc package.</p>
<h2>AUTHOR</h2>
<p> omnicpp was written by Duncan Grisby &lt;duncan [at] grisby.org&gt; </p>
<p> This manual page was written by Floris Bruynooghe &lt;floris.bruynooghe [at] gmail.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
