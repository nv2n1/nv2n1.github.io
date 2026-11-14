---
title: "checkpolicy(8)"
name: "checkpolicy"
section: "8"
letter: "c"
url: "/docs/linux/man/8-checkpolicy/"
description: "checkpolicy – SELinux policy compiler"
---

<p>checkpolicy &#8211; SELinux policy compiler</p>
<h2>Synopsis</h2>
<p><code>checkpolicy</code> <i>[-b] [-C] [-d] [-M] [-c policyvers] [-o output_file] [input_file]</i></p>
<h2>Description</h2>
<p>This manual page describes the <code>checkpolicy</code> command. <code>checkpolicy</code> is a program that checks and compiles a SELinux security policy configuration into a binary representation that can be loaded into the kernel. If no input file name is specified, checkpolicy will attempt to read from policy.conf or policy, depending on whether the -b flag is specified. </p>
<h2>Options</h2>
<dl>
<dt><code>-b,&#8211;binary</code></p>
<dd>Read an existing binary policy file rather than a source policy.conf file.</p>
<dt><code>-C,&#8211;cil</code></p>
<dd>Write CIL policy file rather than binary policy file.</p>
<dt><code>-d,&#8211;debug</code></p>
<dd>Enter debug mode after loading the policy.</p>
<dt><code>-M,&#8211;mls</code></p>
<dd>Enable the MLS policy when checking and compiling the policy.</p>
<dt><code>-o,&#8211;output filename</code></p>
<dd>Write a binary policy file to the specified filename.</p>
<dt><code>-c policyvers</code></p>
<dd>Specify the policy version, defaults to the latest.</p>
<dt><code>-t,&#8211;target</code></p>
<dd>Specify the target platform (selinux or xen).</p>
<dt><code>-U,&#8211;handle-unknown &lt;action&gt;</code></p>
<dd>Specify how the kernel should handle unknown classes or permissions (deny, allow or reject).</p>
<dt><code>-V,&#8211;version</code></p>
<dd>Show version information.</p>
<dt><code>-h,&#8211;help</code></p>
<dd>Show usage information. </p>
</dl>
<h2>See Also</h2>
<p>SELinux documentation at <a rel="nofollow" href="http://www.nsa.gov/research/selinux,">http://www.nsa.gov/research/selinux,</a> especially &quot;Configuring the SELinux Policy&quot;. </p>
<h2>Author</h2>
<p>This manual page was written by Arpad Magosanyi &lt;mag [at] bunuel.tii.matav.hu&gt;, and edited by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;. The program was written by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;.</p>
