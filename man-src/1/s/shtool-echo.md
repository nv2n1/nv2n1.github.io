---
title: "shtool-echo(1)"
name: "shtool-echo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-echo/"
description: "shtool echo – GNU shtool"
---

<h2 class="name">NAME</h2>
<p> shtool echo &#8211; GNU shtool </p>
<p><a href="/docs/linux/man/1-echo/">echo</a>(1) extensional command</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool echo</code> [<code>-n</code>|<code>&#8211;newline</code>] [<code>-e</code>|<code>&#8211;expand</code>] <i>string</i></p>
<h2>DESCRIPTION</h2>
<p> <code>shtool echo</code> is an <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1) style command which prints <i>string</i> to <i>stdout</i> and optionally provides special expansion constructs (terminal bold mode, environment details, date, etc) and newline control. The trick of this command is that it provides a portable <code>-n</code> option and hides the gory details needed to find out the environment details under option <code>-e</code>.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;newline</code></p>
<dd> By default, output is written to <i>stdout</i> followed by a &#8220;newline&#8221; (<font SIZE="-1">ASCII</font> character 0x0a). If option <code>-n</code> is used, this newline character is omitted.</p>
<dt><code>-e</code>, <code>&#8211;expand</code></p>
<dd> If option <code>-e</code> is used, <i>string</i> can contain special &quot;<code>%</code><i>x</i>&quot; constructs which are expanded before the output is written. Currently the following constructs are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>%B</code></p>
<dd> switch terminal mode to bold display mode.</p>
<dt><code>%b</code></p>
<dd> switch terminal mode back to normal display mode.</p>
<dt><code>%u</code></p>
<dd> the current user name.</p>
<dt><code>%U</code></p>
<dd> the current user id (numerical).</p>
<dt><code>%g</code></p>
<dd> the current group name.</p>
<dt><code>%G</code></p>
<dd> the current group id (numerical).</p>
<dt><code>%h</code></p>
<dd> the current hostname (without any domain extension).</p>
<dt><code>%d</code></p>
<dd> the current domain name.</p>
<dt><code>%D</code></p>
<dd> the current day of the month.</p>
<dt><code>%M</code></p>
<dd> the current month (numerical).</p>
<dt><code>%m</code></p>
<dd> the current month name.</p>
<dt><code>%Y</code></p>
<dd> the current year.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool echo -n -e &quot;Enter your name [%B%u%b]: &quot;; read name
 shtool echo -e &quot;Your Email address might be %u@%h%d&quot;
 shtool echo -e &quot;The current date is %D-%m-%Y&quot;
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>echo</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <i>Website </i><font SIZE="-1"><i>META</i></font><i> Language</i> (<font SIZE="-1">WML</font>) under the name <code>buildinfo</code>. It was later taken over into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1). </p>
<h2>Index</h2>
