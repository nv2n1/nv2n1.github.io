---
title: "checkmodule(8)"
name: "checkmodule"
section: "8"
letter: "c"
url: "/docs/linux/man/8-checkmodule/"
description: "checkmodule – SELinux policy module compiler"
---

<p>checkmodule &#8211; SELinux policy module compiler</p>
<h2>Synopsis</h2>
<p><code>checkmodule</code> <i>[-h] [-b] [-C] [-m] [-M] [-U handle_unknown ] [-V] [-o output_file] [input_file]</i></p>
<h2>Description</h2>
<p>This manual page describes the <code>checkmodule</code> command. <code>checkmodule</code> is a program that checks and compiles a SELinux security policy module into a binary representation. It can generate either a base policy module (default) or a non-base policy module (-m option); typically, you would build a non-base policy module to add to an existing module store that already has a base module provided by the base policy. Use semodule_package to combine this module with its optional file contexts to create a policy package, and then use semodule to install the module package into the module store and load the resulting policy. </p>
<h2>Options</h2>
<dl>
<dt><code>-b,&#8211;binary</code></p>
<dd>Read an existing binary policy module file rather than a source policy module file. This option is a development/debugging aid.</p>
<dt><code>-C,&#8211;cil</code></p>
<dd>Write CIL policy file rather than binary policy file.</p>
<dt><code>-h,&#8211;help</code></p>
<dd>Print usage.</p>
<dt><code>-m</code></p>
<dd>Generate a non-base policy module.</p>
<dt><code>-M,&#8211;mls</code></p>
<dd>Enable the MLS/MCS support when checking and compiling the policy module.</p>
<dt><code>-V,&#8211;version</code></p>
<dd>&nbsp;<wbr>Show policy versions created by this program.&nbsp;<wbr>&nbsp;<wbr>Note that you cannot currently build older versions.</p>
<dt><code>-o,&#8211;output filename</code></p>
<dd>Write a binary policy module file to the specified filename. Otherwise, checkmodule will only check the syntax of the module source file and will not generate a binary module at all.</p>
<dt><code>-U,&#8211;handle-unknown &lt;action&gt;</code></p>
<dd>Specify how the kernel should handle unknown classes or permissions (deny, allow or reject). </p>
</dl>
<h2>Example</h2>
<pre># Build a MLS/MCS-enabled non-base policy module.
$ checkmodule -M -m httpd.te -o httpd.mod</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-semodule/">semodule</a>(8), <a href="/docs/linux/man/8-semodule_package/">semodule_package</a>(8)</code> SELinux documentation at <a rel="nofollow" href="http://www.nsa.gov/research/selinux,">http://www.nsa.gov/research/selinux,</a> especially &quot;Configuring the SELinux Policy&quot;. </p>
<h2>Author</h2>
<p>This manual page was copied from the checkpolicy man page written by Arpad Magosanyi &lt;mag [at] bunuel.tii.matav.hu&gt;, and edited by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The program was written by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;.</p>
