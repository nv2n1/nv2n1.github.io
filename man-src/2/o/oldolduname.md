---

title: "oldolduname(2)"
name: "oldolduname"
section: "2"
letter: "o"
url: "/docs/linux/man/2-oldolduname/"
description: "uname – get name and information about current kernel"
---

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
<p> The length of the arrays in a <i>struct utsname</i> is unspecified (see NOTES); the fields are terminated by a null byte (&#8216;\0&#8217;).  </p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></dt>
<dd> <p> <i>buf</i> is not valid. </p>
 </dd></dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. There is no <code>uname</code>() call in 4.3BSD. </p>
<p> The <i>domainname</i> member (the NIS or YP domain name) is a GNU extension.  </p>
<h2>NOTES</h2>
<p> This is a system call, and the operating system presumably knows its name, release and version. It also knows what hardware it runs on. So, four of the fields of the struct are meaningful. On the other hand, the field <i>nodename</i> is meaningless: it gives the name of the present machine in some undefined network, but typically machines are in more than one network and have several names. Moreover, the kernel has no way of knowing about such things, so it has to be told what to answer here. The same holds for the additional <i>domainname</i> field. </p>
<p> To this end, Linux uses the system calls <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2) and <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2). Note that there is no standard that says that the hostname set by <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2) is the same string as the <i>nodename</i> field of the struct returned by <code>uname</code>() (indeed, some systems allow a 256-byte hostname and an 8-byte nodename), but this is true on Linux. The same holds for <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2) and the <i>domainname</i> field. </p>
<p> The length of the fields in the struct varies. Some operating systems or libraries use a hardcoded 9 or 33 or 65 or 257. Other systems use <code>SYS_NMLN</code> or <code>_SYS_NMLN</code> or <code>UTSLEN</code> or <code>_UTSNAME_LENGTH</code>. Clearly, it is a bad idea to use any of these constants; just use sizeof(...). Often 257 is chosen in order to have room for an internet hostname. </p>
<p> Part of the utsname information is also accessible via <i>/proc/sys/kernel/</i>{<i>ostype</i>, <i>hostname</i>, <i>osrelease</i>, <i>version</i>, <i>domainname</i>}.  </p>
<h3>C library/kernel differences</h3>
<p> Over time, increases in the size of the <i>utsname</i> structure have led to three successive versions of <code>uname</code>(): <i>sys_olduname</i>() (slot <i>__NR_oldolduname</i>), <i>sys_uname</i>() (slot <i>__NR_olduname</i>), and <i>sys_newuname</i>() (slot <i>__NR_uname)</i>. The first one used length 9 for all fields; the second used 65; the third also uses 65 but adds the <i>domainname</i> field. The glibc <code>uname</code>() wrapper function hides these details from applications, invoking the most recent version of the system call provided by the kernel.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-uname/">uname</a></code>(1), <code><a href="/docs/linux/man/2-getdomainname/">getdomainname</a></code>(2), <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
