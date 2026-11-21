---

title: "rtas(2)"
name: "rtas"
section: "2"
letter: "r"
url: "/docs/linux/man/2-rtas/"
description: "rtas – Allows userspace to call RTAS (Run Time Abstraction Services)"
---

<p> rtas &#8211; Allows userspace to call RTAS (Run Time Abstraction Services)</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
</dt><dd>int&nbsp;<wbr><code>ppc_rtas</code>&nbsp;<wbr>(struct rtas_args&nbsp;<wbr><i>*uargs</i>); </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>ppc_rtas</code> enables userspace manipulation of the RunTime Abstraction Services (RTAS). RTAS provides for a portable method of access and setting system information. For example, you could gather information on various system sensors and set poweron values. RTAS is accessed via the /proc entry called &quot;rtas&quot;. Manipulations on RTAS are implemented via command line arguments on /proc/rtas. The values for <i>uargs</i> vary greatly. For more information, see the <i>view/arch/ppcKconfig</i> file. </p>
<h2>RETURN VALUE</h2>
<p> <code>rtas</code> returns 0 on success; otherwise it returns one of the errors listed in the &quot;Errors&quot; section. </p>
<h2>ERRORS</h2>
<dl>
<dt>-EPERM</dt>
<dd> User does not have CAP_SYS_ADMIN capabilities. </dd>
<dt>-EFAULT</dt>
<dd> Problem copying <i>uargs</i> values to/from user space. </dd>
<dt>-EINVAL</dt>
<dd> Either number of <i>uargs</i> passed in too large or size of <i>uargs</i> array too large. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Niki Rahimi. </p>
