---
title: "osinfo-detect(1)"
name: "osinfo-detect"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-detect/"
description: "osinfo-detect – Detect the operating system on installable media or trees"
---

<h2 class="name">NAME</h2>
<p> osinfo-detect &#8211; Detect the operating system on installable media or trees </p>
<h2>SYNOPSIS</h2>
<p> osinfo-detect [<font SIZE="-1">OPTIONS&#8230;</font>] PATH|URI</p>
<h2>DESCRIPTION</h2>
<p> Examine the <tt>&quot;PATH&quot;</tt> or <tt>&quot;URI&quot;</tt> to determine what (if any) operating system it is for, and whether it is installable or is a Live image. By default <tt>&quot;PATH&quot;</tt> or <tt>&quot;URI&quot;</tt> will be interpreted as pointing to <font SIZE="-1">ISO</font> media. To request examination of an install tree instead, the option <tt>&quot;--type=tree&quot;</tt> should be given. </p>
<p> The output information is formatted for humans; to obtain machine readable output, the option <tt>&quot;--format=env&quot;</tt> should be given to produce shell-like key/value pairs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;format=plain|env</code></p>
<dd> Switch between human readable output (<code>plain</code>, the default) or machine readable output (<code>env</code>).</p>
<dt><code>&#8211;type=media|tree</code></p>
<dd> Switch between looking for <font SIZE="-1">CD/DVD ISO</font> media (<code>media</code>, the default) or install trees (<code>tree</code>)</dl>
<h2>EXIT STATUS</h2>
<p> The exit status will be 0 if an operating system was detected, or 1 if none was found.</p>
<h2>AUTHORS</h2>
<p> Zeeshan Ali (Khattak) &lt;zeeshanak [at] gnome.org&gt;, Daniel P. Berrange &lt;berrange [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2012 Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> <tt>&quot;osinfo-detect&quot;</tt> is distributed under the termsof the <font SIZE="-1">GNU LGPL</font> v2 license. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font> </p>
<h2>Index</h2>
