---
title: "iprsos(8)"
name: "iprsos"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprsos/"
description: "iprsos – IBM Power RAID report generator"
---

<p>iprsos &#8211; IBM Power RAID report generator</p>
<h2>Synopsis</h2>
<p><code>iprsos</code> </p>
<h2>Description</h2>
<p><code>iprsos</code> is used to generate an sosreport-like report by collecting hardware information from the system, along with other system calls such as lspci, lscsi, and others. The information is collected from &#8216;iprconfig&#8217; commands and printed on stdin by default. User can specify the log file by -o /path/to/report/file of his/her choice.</p>
<h2>Files</h2>
<p>A detailed report file is printed both at stdin and the /path/to/report/file specified by the user, with the information collected from the hardware and system information. If no files are used, the information will be only displayed at stdin.</p>
<h2>Authors</h2>
<p>Daniel B. Kreling &lt;kreling [at] linux.vnet.ibm.com&gt;<br />
 Brian King &lt;brking [at] us.ibm.com&gt;</p>
