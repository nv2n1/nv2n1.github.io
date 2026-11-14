---
title: "mha-decode(1)"
name: "mha-decode"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mha-decode/"
description: "mha-decode – Decode MIME messages"
---

<h2 class="name">NAME</h2>
<p> mha-decode &#8211; Decode MIME messages </p>
<h2>SYNOPSIS</h2>
<p> <code>mha-decode</code>&nbsp;<wbr>[<i>options</i>]&nbsp;<wbr><i>mailfolder</i>&nbsp;<wbr>&#8230; </p>
<p> <code>mha-decode</code>&nbsp;<wbr>[<i>options</i>]&nbsp;<wbr>-single&nbsp;<wbr><i>msg.822</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mha-decode</code> is a utility program that is part of the <code>MHonArc</code> software package. <code>mha-decode</code> provides basic <font SIZE="-1">MIME</font> decoding for mail messages. </p>
<p> If given mail folders as input, all messages within in the mail folders will be decoded. All message parts are written to files. If a filename is specified for a message part, that filename will be used when writing the part to a file. If no filename is specified in the message, a unique name will be used based upon the content-type of the message part. </p>
<p> A single message can be decoded by using the <tt>&quot;-single&quot;</tt> option.</p>
<h2>OPTIONS</h2>
<p> <code>mha-decode</code> takes options available to <code>mhonarc</code>, but only those options affect parsing of mail folders are applicable: <tt>&quot;-conlen&quot;</tt>, <tt>&quot;-mhpattern&quot;</tt>, <tt>&quot;-msgsep&quot;</tt>, <tt>&quot;-noconlen&quot;</tt>, <tt>&quot;-outdir&quot;</tt>, <tt>&quot;-perlinc&quot;</tt>, <tt>&quot;-rcfile&quot;</tt>, <tt>&quot;-single&quot;</tt>, <tt>&quot;-umask&quot;</tt>. </p>
<p> Also, <code>mha-decode</code> supports the following additional options:</p>
<dl>
<dt>&quot;-dcd-digest&quot;</p>
<dd> Run in message digest mode. When this option is specified, any embedded <tt>&quot;message/rfc822&quot;</tt> and <tt>&quot;message/news&quot;</tt> parts will be saved instead of recursively decoding any parts contained within.</dl>
<h2>NOTES</h2>
<p> The documentation for <code>MHonArc</code> is distributed in <font SIZE="-1">HTML</font> format. Due to its size and organization, it is not suited for manpage format. Consult your system administrator for where the documentation has been installed, or see &#8220;<font SIZE="-1">AVAILABILITY</font>&#8221; on where you can access the documentation on the web.</p>
<h2>AVAILABILITY</h2>
<p> &lt;<i><a rel="nofollow" href="http://www.mhonarc.org/">http://www.mhonarc.org/</a></i>&gt;</p>
<h2>AUTHOR</h2>
<p> Earl Hood, mhonarc [at] mhonarc.org </p>
<p> MHonArc comes with <font SIZE="-1">ABSOLUTELY</font> <font SIZE="-1">NO</font> <font SIZE="-1">WARRANTY</font> and MHonArc may be copied only under the terms of the <font SIZE="-1">GNU</font> General Public License, which may be found in the MHonArc distribution. </p>
<h2>Index</h2>
