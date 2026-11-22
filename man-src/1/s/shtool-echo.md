---

title: "shtool-echo(1)"
name: "shtool-echo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-echo/"
description: "shtool echo – GNU shtool"
---

<p> shtool echo &#8211; GNU shtool </p>
<p><a href="/docs/linux/man/1-echo/">echo</a>(1) extensional command</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool echo</code> [<code>-n</code>|<code>&#8211;newline</code>] [<code>-e</code>|<code>&#8211;expand</code>] <i>string</i></p>
<h2>DESCRIPTION</h2>
<p> <code>shtool echo</code> is an <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1) style command which prints <i>string</i> to <i>stdout</i> and optionally provides special expansion constructs (terminal bold mode, environment details, date, etc) and newline control. The trick of this command is that it provides a portable <code>-n</code> option and hides the gory details needed to find out the environment details under option <code>-e</code>.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;newline</code></dt>
<dd> By default, output is written to <i>stdout</i> followed by a &#8220;newline&#8221; (ASCII character 0x0a). If option <code>-n</code> is used, this newline character is omitted.</dd>
<dt><code>-e</code>, <code>&#8211;expand</code></dt>
<dd> If option <code>-e</code> is used, <i>string</i> can contain special &quot;<code>%</code><i>x</i>&quot; constructs which are expanded before the output is written. Currently the following constructs are recognized:</dd>
<dl>
<dl>
<dt><code>%B</code></dt>
<dd> switch terminal mode to bold display mode.</dd>
<dt><code>%b</code></dt>
<dd> switch terminal mode back to normal display mode.</dd>
<dt><code>%u</code></dt>
<dd> the current user name.</dd>
<dt><code>%U</code></dt>
<dd> the current user id (numerical).</dd>
<dt><code>%g</code></dt>
<dd> the current group name.</dd>
<dt><code>%G</code></dt>
<dd> the current group id (numerical).</dd>
<dt><code>%h</code></dt>
<dd> the current hostname (without any domain extension).</dd>
<dt><code>%d</code></dt>
<dd> the current domain name.</dd>
<dt><code>%D</code></dt>
<dd> the current day of the month.</dd>
<dt><code>%M</code></dt>
<dd> the current month (numerical).</dd>
<dt><code>%m</code></dt>
<dd> the current month name.</dd>
<dt><code>%Y</code></dt>
<dd> the current year.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool echo -n -e &quot;Enter your name [%B%u%b]: &quot;; read name
 shtool echo -e &quot;Your Email address might be %u@%h%d&quot;
 shtool echo -e &quot;The current date is %D-%m-%Y&quot;
</pre>
<h2>HISTORY</h2>
<p> The <code>GNU</code><code> shtool</code> <code>echo</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <i>Website </i><i>META</i><i> Language</i> (WML) under the name <code>buildinfo</code>. It was later taken over into <code>GNU</code><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1). </p>
