---
title: "abrt-auto-reporting(1)"
name: "abrt-auto-reporting"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-auto-reporting/"
---

<h2 class="name">NAME</h2>
 

 abrt-auto-reporting - Get or modify the auto reporting option values 

<h2>SYNOPSIS</h2>

 

 <i>abrt-auto-reporting</i> [-v] [ enabled | yes | 1 | on | disabled | no | 0 | off ]

<h2>DESCRIPTION</h2>

 

 Reads the configuration from abrt.conf and saves the changes to the same file. 

 The changes will take effect immediately without necessity to restart any ABRT process and will be persistent. 

 <i>disabled</i>
<dl>
<dt>
<dd> User have to report the detect problems manually</dl>
 

 <i>enabled</i>
<dl>
<dt>
<dd> ABRT uploads an uReport which was generated for a detected problem immediately after the detection phase.</dl>

<h3>uReport description</h3>

 

 ABRT supports uReports for four types of crashes: crashes of C/C++ programs that result in a core dump, uncaught Python exceptions, uncaught Java exceptions and kernel oopses. 

 Each uReport generally contains a stack trace, or multiple stack traces in the case of multi-threaded C/C++ and Java programs. The stack trace only describes the call stack of the program at the time of the crash and does not contain contents of any variables. 

 Every uReport also contains identification of the operating system, versions of the RPM packages involved in the crash, and whether the program ran under a root user. 

 There are also items specific to each crash type: 

 C/C++ crashes
<dl>
<dt>
<dd> these are path to the executable and signal delivered to the program,</dl>
 

 Python exceptions
<dl>
<dt>
<dd> there is the type of the exception (without the error message, which may contain sensitive data),</dl>
 

 for kernel oopses
<dl>
<dt>
<dd> these are list of loaded kernel modules, list of taint flags, and full text of the kernel oops.</dl>
 

 <i>Warning</i>: The full text of a kernel oops might contain information like the identification of the host hardware type. You should disable the autoreporting feature if you do not want to share this information with Red Hat.

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


