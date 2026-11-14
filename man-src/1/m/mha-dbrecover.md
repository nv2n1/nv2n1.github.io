---
title: "mha-dbrecover(1)"
name: "mha-dbrecover"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mha-dbrecover/"
description: "mha-dbrecover – rebuild a MHonArc archive database"
---

<h2 class="name">NAME</h2>
<p> mha-dbrecover &#8211; rebuild a MHonArc archive database </p>
<h2>SYNOPSIS</h2>
<p> <code>mha-dbrecover</code>&nbsp;<wbr>[<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>mha-dbrecover</code> is a utility program that is part of the <code>MHonArc</code> software package. The program allows can be used to rebuild a <code>MHonArc</code> archive database from the <font SIZE="-1">HTML</font> message files. This allows database recovery if the database gets corrupted or accidentally deleted. </p>
<p> The documentation for <code>MHonArc</code> is distributed in <font SIZE="-1">HTML</font> format. Due to its size and organization, it is not suited for manpage format. Consult your system administrator for where the documentation has been installed, or see &#8220;<font SIZE="-1">AVAILABILITY</font>&#8221; on where you can access the documentation on the web.</p>
<h2>OPTIONS</h2>
<p> <code>mha-dbrecover</code> takes all the options available to <code>mhonarc</code> along with the following additional options:</p>
<dl>
<dt>&quot;-dbr-startnum&quot; <i>#</i></p>
<dd> The starting message number to recover data from. This option is useful if you have many message files in a directory, but you only want to recover a subset of the files. </p>
<p> If this option is not specified, the starting number is 0.</p>
<dt>&quot;-dbr-endnum&quot; <i>#</i></p>
<dd> The ending message number to recover data from. This option is useful if you have many message files in a directory, but you only want to recover a subset of the files. </p>
<p> If this option is not specified, all messages starting from <tt>&quot;-dbr-startnum&quot;</tt> will be recovered.</dl>
<p> <font SIZE="-1"><code>NOTE:</code></font> Only a subset of the options available to <code>mhonarc</code> are actually supported since many options are not applicable for recovering operations.</p>
<h2>AVAILABILITY</h2>
<p> &lt;<i><a rel="nofollow" href="http://www.mhonarc.org/">http://www.mhonarc.org/</a></i>&gt;</p>
<h2>AUTHOR</h2>
<p> Earl Hood, mhonarc [at] mhonarc.org </p>
<p> MHonArc comes with <font SIZE="-1">ABSOLUTELY</font> <font SIZE="-1">NO</font> <font SIZE="-1">WARRANTY</font> and MHonArc may be copied only under the terms of the <font SIZE="-1">GNU</font> General Public License, which may be found in the MHonArc distribution. </p>
<h2>Index</h2>
