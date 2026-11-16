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
<dt><code>-b,&#8211;binary</code></dt>
<dd>Read an existing binary policy file rather than a source policy.conf file.</dd>
<dt><code>-C,&#8211;cil</code></dt>
<dd>Write CIL policy file rather than binary policy file.</dd>
<dt><code>-d,&#8211;debug</code></dt>
<dd>Enter debug mode after loading the policy.</dd>
<dt><code>-M,&#8211;mls</code></dt>
<dd>Enable the MLS policy when checking and compiling the policy.</dd>
<dt><code>-o,&#8211;output filename</code></dt>
<dd>Write a binary policy file to the specified filename.</dd>
<dt><code>-c policyvers</code></dt>
<dd>Specify the policy version, defaults to the latest.</dd>
<dt><code>-t,&#8211;target</code></dt>
<dd>Specify the target platform (selinux or xen).</dd>
<dt><code>-U,&#8211;handle-unknown &lt;action&gt;</code></dt>
<dd>Specify how the kernel should handle unknown classes or permissions (deny, allow or reject).</dd>
<dt><code>-V,&#8211;version</code></dt>
<dd>Show version information.</dd>
<dt><code>-h,&#8211;help</code></dt>
<dd>Show usage information. </dd>
</dl>
<h2>See Also</h2>
<p>SELinux documentation at <a rel="nofollow" href="http://www.nsa.gov/research/selinux,">http://www.nsa.gov/research/selinux,</a> especially &quot;Configuring the SELinux Policy&quot;. </p>
<h2>Author</h2>
<p>This manual page was written by Arpad Magosanyi &lt;mag [at] bunuel.tii.matav.hu&gt;, and edited by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;. The program was written by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;.</p>
