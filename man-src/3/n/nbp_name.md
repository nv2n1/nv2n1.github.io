---
title: "nbp_name(3)"
name: "nbp_name"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nbp_name/"
description: "nbp_name – NBP name parsing"
---

<p>nbp_name &#8211; NBP name parsing </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int nbp_name(char&nbsp;<wbr>*</code><i>name</i><code>, char&nbsp;<wbr>**</code><i>obj</i><code>, char&nbsp;<wbr>**</code><i>type</i><code>, char&nbsp;<wbr>**</code><i>zone</i><code>);</code></dl>
<h2>Description</h2>
<p><code>nbp_name()</code></p>
<dd>parses user supplied names into their component object, type, and zone. <code>obj</code>, <code>type</code>, and <i>zone</i> should be passed by reference, and should point to the caller&#8217;s default values. <code>nbp_name()</code> will change the pointers to the parsed-out values. <code>name</code> is of the form <i>object</i><code>:</code><i>type</i><code>@</code><i>zone</i>, where each of <i>object</i>, <code>:</code><i>type</i><code>,</code> and <code>@</code><i>zone</i> replace <code>obj</code>, <code>type</code>, and <code>zone,</code> respectively. <i>type</i> must be proceeded by `<code>:</code>&#8216;, and <i>zone</i> must be preceded by `<code>@</code>&#8216;.</p>
<h2>Example</h2>
<p>The argument of <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8)&#8217;s <code>-n</code> option is parsed with <code>nbp_name()</code>. The default value of <code>obj</code> is the first component of the machine&#8217;s hostname (as returned by <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3)). The default value of <code>type</code> is &#8220;AFPServer&#8221;, and of <i>zone</i> is &#8220;*&#8221;, the default zone. To cause <code>afpd</code> to register itself in some zone other than the default, one would invoke it as </p>
<dl COMPACT>
<dd>
<pre>afpd -n @some-other-zone</pre>
</dl>
<p> <code>obj</code> and <code>type</code> would retain their default values.</p>
<h2>Bugs</h2>
<p><code>obj</code>, <code>type</code>, and <i>zone</i> return pointers into static area which may be over-written on each call.</p>
