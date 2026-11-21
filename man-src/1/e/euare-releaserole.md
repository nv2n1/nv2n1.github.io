---

title: "euare-releaserole(1)"
name: "euare-releaserole"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-releaserole/"
description: "euare-releaserole – Release IAM role credentials"
---

<p> euare-releaserole &#8211; Release IAM role credentials</p>
<h2>SYNOPSIS</h2>
<p> euare-releaserole [-c | <code>-s]</code> [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</p>
<h2>DESCRIPTION</h2>
<p> Release IAM role credentials</p>
<h2>DESCRIPTION</h2>
<p> The euare-releaserole utility removes the credentials created by euareassumerole(1) by outputting shellcode that deletes the environment variables it creates. Use it inside an eval command to make this process seamless:</p>
<h2>DESCRIPTION</h2>
<p> $ eval `euare-releaserole`</p>
<h2>DESCRIPTION</h2>
<p> Note that if the credentials used to initially assume the role were supplied in the form of environment variables those environment variables will need to be reset:</p>
<h2>DESCRIPTION</h2>
<p> $ source eucarc</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code></dt>
<dd> generate C-shell commands on stdout (default if SHELL looks like a csh-style shell</dd>
<dt><code>-s</code></dt>
<dd> generate Bourne shell commands on stdout (default if SHELL does not look like a csh-style shell</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
