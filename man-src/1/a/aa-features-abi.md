---
title: "aa-features-abi(1)"
name: "aa-features-abi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aa-features-abi/"
description: "aa-features-abi – Extract, validate and manipulate AppArmor feature abis"
---

<h2 class="name">NAME</h2>
<p> aa-features-abi &#8211; Extract, validate and manipulate AppArmor feature abis </p>
<h2>SYNOPSIS</h2>
<p> <code>aa-features-abi</code> [<font SIZE="-1">OPTIONS</font>] &lt;<font SIZE="-1">SOURCE</font>&gt; [<font SIZE="-1">OUTPUT OPTIONS</font>]</p>
<h2>DESCRIPTION</h2>
<p> <code>aa-features-abi</code> is used to extract a features abi and output to either stdout or a specified file. A <font SIZE="-1">SOURCE_OPTION</font> must be specified. If an output option is not specified the features abi is written to stdout.</p>
<h2>OPTIONS</h2>
<p> <code>aa-features-abi</code> accepts the following arguments:</p>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display a brief usage guide.</p>
<dt>-d, &#8211;debug</p>
<dd> show messages with debugging information</p>
<dt>-v, &#8211;verbose</p>
<dd> show messages with stats</dl>
<h2>SOURCE</h2>
<dl>
<dt>-x, &#8211;extract</p>
<dd> Extract the features abi for the kernel</p>
<dt>-f <font SIZE="-1">FILE,</font> &#8211;file=FILE</p>
<dd> Load the features abi from <font SIZE="-1">FILE</font> and send it to <font SIZE="-1">OUTPUT OPTIONS.</font></dl>
<h2>OUTPUT OPTIONS</h2>
<dl>
<dt>&#8211;stdout</p>
<dd> Write the features abi to <i>stdout</i>, this is the default if no output option is specified.</p>
<dt>-w <font SIZE="-1">FILE,</font> &#8211;write <font SIZE="-1">FILE</font></p>
<dd> Write the features abi to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>.</dl>
<h2>BUGS</h2>
<p> If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code><a href="/docs/linux/man/3-aa_features/">aa_features</a></code>(3), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
<h2>Index</h2>
