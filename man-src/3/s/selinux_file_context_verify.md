---
title: "selinux_file_context_verify(3)"
name: "selinux_file_context_verify"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_file_context_verify/"
description: "selinux_file_context_verify – Compare the SELinux security context on disk to the default security context required by the policy file contexts file"
---

<p>selinux_file_context_verify &#8211; Compare the SELinux security context on disk to the default security context required by the policy file contexts file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_file_context_verify(const char *path, mode_t mode);</code></pre>
<h2>Description</h2>
<p><code>selinux_file_context_verify</code>() compares the context of the specified <i>path</i> that is held on disk (in the extended attribute), to the system default entry held in the file contexts series of files. </p>
<p> The <i>mode</i> may be zero. </p>
<p> Note that the two contexts are compared for &quot;significant&quot; differences (i.e. the user component of the contexts are ignored) as shown in the <code>EXAMPLE</code> section.</p>
<h2>Return Value</h2>
<p>If the contexts significantly match, 1 (one) is returned. </p>
<p> If the contexts do not match 0 (zero) is returned and <i>errno</i> is set to either <code>ENOENT</code> or <code>EINVAL</code> for the reasons listed in the <code>ERRORS</code> section, or if <i>errno</i> = 0 then the contexts did not match. </p>
<p> On failure -1 is returned and <i>errno</i> set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOTSUP</code></p>
<dd>if extended attributes are not supported by the file system.</p>
<dt><code>ENOENT</code></p>
<dd>if there is no entry in the file contexts series of files or <i>path</i> does not exist.</p>
<dt><code>EINVAL</code></p>
<dd>if the entry in the file contexts series of files or <i>path</i> are invalid, or the returned context fails validation.</p>
<dt><code>ENOMEM</code></p>
<dd>if attempt to allocate memory failed.</dl>
<h2>Files</h2>
<p>The following configuration files (the file contexts series of files) supporting the active policy will be used (should they exist) to determine the <i>path</i> default context: </p>
<dl>
<dd><i>contexts/files/file_contexts</i> &#8211; This file must exist. </p>
<p> <i>contexts/files/file_contexts.local</i> &#8211; If exists has local customizations. </p>
<p> <i>contexts/files/file_contexts.homedirs</i> &#8211; If exists has users home directory customizations. </p>
<p> <i>contexts/files/file_contexts.subs</i> &#8211; If exists has substitutions that are then applied to the &#8216;in memory&#8217; version of the file contexts files.</dl>
<h2>Example</h2>
<p>If the files context is:</p>
<dl>
<dd>unconfined_u:object_r:admin_home_t:s0</dl>
<p> and the default context defined in the file contexts file is:</p>
<dl>
<dd>system_u:object_r:admin_home_t:s0</dl>
<p> then the actual strings compared are:</p>
<dl>
<dd>:object_r:admin_home_t:s0 and :object_r:admin_home_t:s0</dl>
<p> Therefore they will match and <code>selinux_file_context_verify</code>() will return 1.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
