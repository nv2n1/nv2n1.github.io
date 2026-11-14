---
title: "olduname(2)"
name: "olduname"
section: "2"
letter: "o"
url: "/docs/linux/man/2-olduname/"
description: "uname – get name and information about current kernel"
---

<h2 class="name">NAME</h2>
<p> uname &#8211; get name and information about current kernel </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/utsname.h&gt;</code> </p>
<p> <code>int uname(struct utsname *</code><i>buf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>uname</code>() returns system information in the structure pointed to by <i>buf</i>. The <i>utsname</i> struct is defined in <i>&lt;sys/utsname.h&gt;</i>: </p>
<p> struct utsname {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char sysname[];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Operating system name&nbsp;(e.g.,&nbsp;&quot;Linux&quot;)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char nodename[];&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Name within&nbsp;&quot;some implementation-defined<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;network&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char release[];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Operating system release<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(e.g.,&nbsp;&quot;2.6.28&quot;)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char version[];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Operating system version&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char machine[];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Hardware identifier&nbsp;*/ #ifdef _GNU_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char domainname[];&nbsp;/*&nbsp;NIS or YP domain name&nbsp;*/ #endif }; </p>
<p> The length of the arrays in a <i>struct utsname</i> is unspecified (see NOTES); the fields are terminated by a null byte (&#8216;
