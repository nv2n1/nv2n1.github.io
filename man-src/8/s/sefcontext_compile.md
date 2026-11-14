---
title: "sefcontext_compile(8)"
name: "sefcontext_compile"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sefcontext_compile/"
description: "sefcontext_compile – compile file context regular expression files"
---

<p>sefcontext_compile &#8211; compile file context regular expression files</p>
<h2>Synopsis</h2>
<p><code>sefcontext_compile</code> [<code>-o</code> <i>outputfile</i>] [<code>-p</code> <i>policyfile</i>] <i>inputfile</i></p>
<h2>Description</h2>
<p><code>sefcontext_compile</code> is used to compile file context regular expressions into <code><a href="/docs/linux/man/3-pcre/">pcre</a></code>(3) format. </p>
<p> The compiled file is used by libselinux file labeling functions. </p>
<p> By default <code>sefcontext_compile</code> writes the compiled pcre file with the <code>.bin</code> suffix appended (e.g. <i>inputfile</i><code>.bin</code>).</p>
<h2>Options</h2>
<dl>
<dt><code>-o</code></p>
<dd>Specify an <i>outputfile</i> that must be a fully qualified file name as the <code>.bin</code> suffix is not automatically added.</p>
<dt><code>-p</code></p>
<dd>Specify a binary <i>policyfile</i> that will be used to validate the context entries in the <i>inputfile</i><br />
 If an invalid context is found the pcre formatted file will not be written and an error will be returned. </p>
</dl>
<h2>Return Value</h2>
<p>On error -1 is returned. On success 0 is returned. </p>
<h2>Examples</h2>
<p><code>Example 1:</code><br />
 sefcontext_compile /etc/selinux/targeted/contexts/files/file_contexts </p>
<p> Results in the following file being generated:</p>
<dl>
<dd>/etc/selinux/targeted/contexts/files/file_contexts.bin</dl>
<p> <code>Example 2:</code><br />
 sefcontext_compile -o new_fc.bin /etc/selinux/targeted/contexts/files/file_contexts </p>
<p> Results in the following file being generated in the cwd:</p>
<dl>
<dd>new_fc.bin</dl>
<h2>Author</h2>
<p>Dan Walsh, &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-semanage/">semanage</a></code>(8), </p>
