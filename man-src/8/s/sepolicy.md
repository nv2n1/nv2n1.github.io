---
title: "sepolicy(8)"
name: "sepolicy"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy/"
description: "sepolicy – SELinux Policy Inspection tool"
---

<p>sepolicy &#8211; SELinux Policy Inspection tool </p>
<h2>Synopsis</h2>
<p><code>sepolicy [-h] [-P policy_path ] {booleans,communicate,generate,interface,manpage,network,transition} OPTIONS</code><br />
 Arguments:<br />
 <code>booleans</code><br />
 Query SELinux policy to see description of booleans <code><a href="/docs/linux/man/8-sepolicy-boolean/">sepolicy-boolean</a>(8)</code><br />
 <code>communicate</code><br />
 Query SELinux policy to see if domains can communicate with each other <code><a href="/docs/linux/man/8-sepolicy-communicate/">sepolicy-communicate</a>(8)</code><br />
 <code>generate</code> </p>
<p> Generate SELinux Policy module template <code>gui</code> </p>
<p> Launch Graphical User Interface for SELinux Policy, requires policycoreutils-gui package. <code><a href="/docs/linux/man/8-sepolicy-generate/">sepolicy-generate</a>(8)</code><br />
 <code>interface</code> </p>
<p> Print SELinux Policy interface information <code><a href="/docs/linux/man/8-sepolicy-interface/">sepolicy-interface</a>(8)</code><br />
 <code>manpage</code><br />
 Generate SELinux man pages <code><a href="/docs/linux/man/8-sepolicy-manpage/">sepolicy-manpage</a>(8)</code><br />
 <code>network</code><br />
 Query SELinux policy network information <code><a href="/docs/linux/man/8-sepolicy-network/">sepolicy-network</a>(8)</code><br />
 <code>transition </code><br />
 Query SELinux Policy to see how a source process domain can transition to the target process domain <code><a href="/docs/linux/man/8-sepolicy-transition/">sepolicy-transition</a>(8)</code> </p>
<h2>Description</h2>
<p>sepolicy is a tools set that will query the installed SELinux policy and generate useful reports, man pages, or even new policy modules. See the argument specific man pages for options and descriptions. </p>
<h2>Options</h2>
<dl>
<dt><i>-P, &#8211;policy</i></p>
<dd>Alternate policy to analyze. (Defaults to currently installed policy /sys/fs/selinux/policy)</p>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-sepolicy-booleans/">sepolicy-booleans</a>(8), <a href="/docs/linux/man/8-sepolicy-communicate/">sepolicy-communicate</a>(8), <a href="/docs/linux/man/8-sepolicy-generate/">sepolicy-generate</a>(8),<a href="/docs/linux/man/8-sepolicy-gui/">sepolicy-gui</a>(8), <a href="/docs/linux/man/8-sepolicy-interface/">sepolicy-interface</a>(8), <a href="/docs/linux/man/8-sepolicy-network/">sepolicy-network</a>(8), <a href="/docs/linux/man/8-sepolicy-manpage/">sepolicy-manpage</a>(8), <a href="/docs/linux/man/8-sepolicy-transition/">sepolicy-transition</a>(8) </p>
