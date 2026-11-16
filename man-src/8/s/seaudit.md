---
title: "seaudit(8)"
name: "seaudit"
section: "8"
letter: "s"
url: "/docs/linux/man/8-seaudit/"
description: "seaudit – SELinux graphical audit log analysis tool"
---

<p>seaudit &#8211; SELinux graphical audit log analysis tool</p>
<h2>Synopsis</h2>
<p><code>seaudit</code> [OPTIONS] [POLICY &#8230;]</p>
<h2>Description</h2>
<p><code>seaudit</code> allows the user to view and filter the contents of a log file. <code>seaudit</code> supports the syslog and auditd log formats and provides queries to inspect the SELinux policy based on log messages.</p>
<h2>Policy</h2>
<p><code>seaudit</code> supports loading a SELinux policy in one of four formats.</p>
<dl>
<dt>source</dt>
<dd>A single text file containing policy source for versions 12 through 21. This file is usually named policy.conf.</dd>
<dt>binary</dt>
<dd>A single file containing a monolithic kernel binary policy for versions 15 through 21. This file is usually named by version &#8211; for example, policy.20.</dd>
<dt>modular</dt>
<dd>A list of policy packages each containing a loadable policy module. The first module listed must be a base module.</dd>
<dt>policy list</dt>
<dd>A single text file containing all the information needed to load a policy, usually exported by SETools graphical utilities.</dd></dl>
<p> If no policy file is provided, <code>seaudit</code> will search for the system default policy: checking first for a source policy, next for a binary policy matching the running kernel&#8217;s preferred version, and finally for the highest version that can be found. If no policy can be found, <code>seaudit</code> will begin with no policy loaded.</p>
<h2>Options</h2>
<dl>
<dt>-l FILE, &#8211;log=FILE</dt>
<dd>Upon startup, open the log FILE instead of the system log file.</dd>
<dt>-h, &#8211;help</dt>
<dd>Print help information and exit.</dd>
<dt>-V, &#8211;version</dt>
<dd>Print version information and exit.</dd></dl>
<h2>Author</h2>
<p>This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright(C) 2006-2007 Tresys Technology, LLC</p>
<h2>Bugs</h2>
<p>Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>See Also</h2>
<p>seaudit-report(8) </p>
