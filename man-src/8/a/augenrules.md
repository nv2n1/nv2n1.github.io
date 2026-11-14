---
title: "augenrules(8)"
name: "augenrules"
section: "8"
letter: "a"
url: "/docs/linux/man/8-augenrules/"
description: "augenrules – a script that merges component audit rule files"
---

<p>augenrules &#8211; a script that merges component audit rule files</p>
<h2>Synopsis</h2>
<p><code>augenrules</code> [<i>&#8211;check</i>]&nbsp;<wbr>[<i>&#8211;load</i>]</p>
<h2>Description</h2>
<p><code>augenrules</code> is a script that merges all component audit rules files, found in the audit rules directory, <i>/etc/audit/rules.d</i>, placing the merged file in <i>/etc/audit/audit.rules</i>. Component audit rule files, must end in <i>.rules</i> in order to be processed. All other files in <i>/etc/audit/rules.d</i> are ignored. </p>
<p> The files are concatenated in order, based on their natural sort (see -v option of <a href="/docs/linux/man/1-ls/">ls</a>(1)) and stripped of empty and comment (#) lines. </p>
<p> The last processed &#8211;<i>D</i> directive without an option, if present, is always emitted as the first line in the resultant file. Those with an option are replicated in place. The last processed &#8211;<i>b</i> directive, if present, is always emitted as the second line in the resultant file. The last processed &#8211;<i>f</i> directive, if present, is always emitted as the third line in the resultant file. The last processed &#8211;<i>e</i> directive, if present, is always emitted as the last line in the resultant file. </p>
<p> The generated file is only copied to <i>/etc/audit/audit.rules</i>, if it differs.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd>test if rules have changed and need updating without overwriting audit.rules.</p>
<dt><code>&#8211;load</code></p>
<dd>load old or newly built rules into the kernel. </p>
</dl>
<h2>Files</h2>
<p>/etc/audit/rules.d/ /etc/audit/audit.rules</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audit-rules/">audit.rules</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
