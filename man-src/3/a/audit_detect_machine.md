---
title: "audit_detect_machine(3)"
name: "audit_detect_machine"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_detect_machine/"
description: "audit_detect_machine – Detects the current machine type"
---

<h2>NAME</h2>
<p> audit_detect_machine &#8211; Detects the current machine type</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_detect_machine (void); </p>
<h2>DESCRIPTION</h2>
<p> audit_detect_machine queries uname and converts the kernel machine string to an enum value defined in machine_t. The machine type is needed for any use of the audit_name_to_syscall function. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, the return value is the machine&#8217;s type. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-uname/">uname</a></code>(3), <code><a href="/docs/linux/man/3-audit_name_to_syscall/">audit_name_to_syscall</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
