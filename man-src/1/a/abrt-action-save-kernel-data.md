---
title: "abrt-action-save-kernel-data(1)"
name: "abrt-action-save-kernel-data"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-save-kernel-data/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-save-kernel-data - Creates uReport mandatory files for kernel oopses. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-save-kernel-data</i>

<h2>DESCRIPTION</h2>

 

 The tool reads problem directory DIR. It analyzes contents of <i>kernel</i> element, checks database of installed packages, and creates new elements <i>pkg_name</i>, <i>pkg_arch</i>, <i>pkg_version</i>, <i>pkg_release</i>. 

 These files are required by reporter-ureporter (mandatory in uReport).

<h3>Integration with ABRT events</h3>

 

 This tool can be used as an ABRT reporter. Example fragment for /etc/libreport/report_event.conf: 

<dl>
<dt>
<dd> <pre>
# Determine in which package/component the crash happened (if not yet done):
EVENT=post-create analyzer=Kerneloops
        abrt-action-save-kernel-data
</pre></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


