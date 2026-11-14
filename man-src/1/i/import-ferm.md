---
title: "import-ferm(1)"
name: "import-ferm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-import-ferm/"
description: "import-ferm – import existing firewall rules into ferm"
---

<h2 class="name">NAME</h2>
<p> import-ferm &#8211; import existing firewall rules into ferm </p>
<h2>SYNOPSIS</h2>
<p> <code>import-ferm</code> &gt; ferm.conf </p>
<p> iptables-save | <code>import-ferm</code> &gt; ferm.conf </p>
<p> <code>import-ferm</code> <i>inputfile</i> &gt; ferm.conf</p>
<h2>DESCRIPTION</h2>
<p> This script helps you with porting an existing IPv4 firewall configuration to ferm. It reads a file generated with <code>iptables-save</code>, and tries to suggest a ferm configuration file. </p>
<p> If no input file was specified on the command line, <code>import-ferm</code> runs <i>iptables-save</i>.</p>
<h2>BUGS</h2>
<p> iptables-save older than 1.3 is unable to write valid saves &#8211; this is not a bug in <code>import-ferm</code>. </p>
<h2>Index</h2>
