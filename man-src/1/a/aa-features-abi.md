---

title: "aa-features-abi(1)"
name: "aa-features-abi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aa-features-abi/"
description: "aa-features-abi – Extract, validate and manipulate AppArmor feature abis"
---

<p> aa-features-abi &#8211; Extract, validate and manipulate AppArmor feature abis </p>
<h2>SYNOPSIS</h2>
<p> <code>aa-features-abi</code> [OPTIONS] &lt;SOURCE&gt; [OUTPUT OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> <code>aa-features-abi</code> is used to extract a features abi and output to either stdout or a specified file. A SOURCE_OPTION must be specified. If an output option is not specified the features abi is written to stdout.</p>
<h2>OPTIONS</h2>
<p> <code>aa-features-abi</code> accepts the following arguments:</p>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Display a brief usage guide.</dd>
<dt>-d, &#8211;debug</dt>
<dd> show messages with debugging information</dd>
<dt>-v, &#8211;verbose</dt>
<dd> show messages with stats</dd></dl>
<h2>SOURCE</h2>
<dl>
<dt>-x, &#8211;extract</dt>
<dd> Extract the features abi for the kernel</dd>
<dt>-f FILE, &#8211;file=FILE</dt>
<dd> Load the features abi from FILE and send it to OUTPUT OPTIONS.</dd></dl>
<h2>OUTPUT OPTIONS</h2>
<dl>
<dt>&#8211;stdout</dt>
<dd> Write the features abi to <i>stdout</i>, this is the default if no output option is specified.</dd>
<dt>-w FILE, &#8211;write FILE</dt>
<dd> Write the features abi to <i></i><i>FILE</i><i></i>.</dd></dl>
<h2>BUGS</h2>
<p> If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code>aa_features</code>(3), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
