---
title: "aa-exec(1)"
name: "aa-exec"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aa-exec/"
description: "aa-exec – confine a program with the specified AppArmor profile"
---

<h2 class="name">NAME</h2>
<p> aa-exec &#8211; confine a program with the specified AppArmor profile </p>
<h2>SYNOPSIS</h2>
<p> <code>aa-exec</code> [options] [&#8211;] [<i>&lt;command&gt;</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>aa-exec</code> is used to launch a program confined by the specified profile and or namespace. If both a profile and namespace are specified command will be confined by profile in the new policy namespace. If only a namespace is specified, the profile name of the current confinement will be used. If neither a profile or namespace is specified command will be run using standard profile attachment (ie. as if run without the aa-exec command). </p>
<p> If the arguments are to be pasted to the <i>&lt;command&gt;</i> being invoked by aa-exec then &#8212; should be used to separate aa-exec arguments from the command.<br />
&nbsp;<wbr>&nbsp;aa-exec -p profile1 &#8212; ls -l</p>
<h2>OPTIONS <code>aa-exec</code> accepts the following arguments:</h2>
<dl>
<dt>-p <font SIZE="-1">PROFILE,</font> &#8211;profile=PROFILE</dt>
<dd> confine <i>&lt;command&gt;</i> with <font SIZE="-1">PROFILE.</font> If the <font SIZE="-1">PROFILE</font> is not specified use the current profile name (likely unconfined).</dd>
<dt>-n <font SIZE="-1">NAMESPACE,</font> &#8211;namespace=NAMESPACE</dt>
<dd> use profiles in <font SIZE="-1">NAMESPACE.</font> This will result in confinement transitioning to using the new profile namespace.</dd>
<dt>-i, &#8211;immediate</dt>
<dd> transition to <font SIZE="-1">PROFILE</font> before doing executing <i>&lt;command&gt;</i>. This subjects the running of <i>&lt;command&gt;</i> to the exec transition rules of the current profile.</dd>
<dt>-v, &#8211;verbose</dt>
<dd> show commands being performed</dd>
<dt>-d, &#8211;debug</dt>
<dd> show commands and error codes</dd>
<dt>&#8212;</dt>
<dd> Signal the end of options and disables further option processing. Any arguments after the &#8212; are treated as arguments of the command. This is useful when passing arguments to the <i>&lt;command&gt;</i> being invoked by aa-exec.</dd></dl>
<h2>BUGS</h2>
<p> If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <code>aa-stack</code>(8), <code>aa-namespace</code>(8), <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code>aa_change_profile</code>(3), <code>aa_change_onexec</code>(3) and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
<h2>Index</h2>
