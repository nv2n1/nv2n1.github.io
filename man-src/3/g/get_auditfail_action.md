---
title: "get_auditfail_action(3)"
name: "get_auditfail_action"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_auditfail_action/"
description: "get_auditfail_action – Get failure_action tunable value"
---

<h2>NAME</h2>
<p> get_auditfail_action &#8211; Get failure_action tunable value</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libaudit.h&gt; </p>
<dl>
<dt>
<dd>int&nbsp;<wbr><code>get_auditfail_action</code>&nbsp;<wbr>(int *<i>failmode</i>); </p>
</dl>
<h2>DESCRIPTION</h2>
<p> This function gets the failure_action tunable value stored in <code>/etc/libaudit.conf</code>. <code>get_auditfail_action</code> should be called after an <code>audit_open</code> call returns an error to see what action the admin prefers. </p>
<p> The failure_action value found in <code>/etc/libaudit.conf</code> is copied into the <i>failmode</i> argument upon function return. This value should then be used by the calling application to determine what action should be taken when the audit subsystem is unavailable. </p>
<h2>RETURN VALUE</h2>
<p> Upon success, <code>get_auditfail_action</code> returns a zero, and the <i>failmode</i> argument will hold the failure_action value. The possible values for failure_action are: FAIL_IGNORE (0), FAIL_LOG (1), and FAIL_TERMINATE (2). Upon failure, <code>get_auditfail_action</code> returns a return code of one. </p>
<h2>ERRORS</h2>
<p> An error is returned if there is an error reading <code>/etc/libaudit.conf</code> or if the failure_action tunable is not found in the file. </p>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Sample code&nbsp;<wbr>*/<br />
&nbsp;<wbr>auditfail_t failmode;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<p>&nbsp;<wbr>if&nbsp;<wbr>((fd&nbsp;<wbr>=&nbsp;<wbr>audit_open()&nbsp;<wbr>)&nbsp;<wbr>&lt;&nbsp;<wbr>0&nbsp;<wbr>)&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fprintf&nbsp;<wbr>(stderr,&nbsp;<wbr>&quot;Cannot open netlink audit socket&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Get the failure_action&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>((rc&nbsp;<wbr>=&nbsp;<wbr>get_auditfail_action(&amp;failmode))&nbsp;<wbr>==&nbsp;<wbr>0)&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>(failmode&nbsp;<wbr>==&nbsp;<wbr>FAIL_LOG)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fprintf&nbsp;<wbr>(stderr,&nbsp;<wbr>&quot;Audit subsystem unavailable&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>else if&nbsp;<wbr>(failmode&nbsp;<wbr>==&nbsp;<wbr>FAIL_TERMINATE)&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit&nbsp;<wbr>(1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>If failmode&nbsp;<wbr>==&nbsp;<wbr>FAIL_IGNORE, do nothing&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}<br />
&nbsp;<wbr>} </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Lisa M. Smith. </p>
<h2>Index</h2>
