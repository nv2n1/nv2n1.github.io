---

title: "w3mman(1)"
name: "w3mman"
section: "1"
letter: "w"
url: "/docs/linux/man/1-w3mman/"
description: "w3mman – an interface to the on-line reference manuals via"
---

<p> w3mman &#8211; an interface to the on-line reference manuals via </p>
<p> <a href="/docs/linux/man/1-w3m/">w3m</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>w3mman</code> [ <code>-M</code><i> path</i> ] [ [ <i>section</i> ] <i>page</i> ]<br/>
 <code>w3mman</code> [ <code>-M</code><i> path</i> ] [ <i>section</i> ] <code>-k</code><i> keyword</i><br/>
 <code>w3mman</code> <code>-l</code><i> file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>w3mman</code> is a Perl script that uses <code><a href="/docs/linux/man/1-w3m/">w3m</a></code>(1) to serve as a pager for on-line reference manuals.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-M</code><i> path</i></dt>
<dd> Specify <i>path</i> as alternative MANPATH to use.</dd>
<dt><code>-k</code><i> keyword</i></dt>
<dd> Specify <i>keyword</i>.</dd>
<dt><code>-l</code><i> file</i></dt>
<dd> Specify a <i>file</i>.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> Two variables are available for debugging.</p>
<dl>
<dt><code>W3MMAN_W3M</code></dt>
<dd> If W3MMAN_W3M is set, its value is used instead of w3m.</dd>
<dt><code>W3MMAN_MAN</code></dt>
<dd> If W3MMAN_MAN is set, its value is used instead of /usr/bin/man.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/lib/w3m/cgi-bin/w3mman2html.cgi</i></dt>
<dd> manual page to HTML converter.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-w3m/">w3m</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
