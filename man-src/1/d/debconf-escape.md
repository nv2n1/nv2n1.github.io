---
title: "debconf-escape(1)"
name: "debconf-escape"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-escape/"
description: "debconf-escape – helper when working with debconf’s escape capability"
---

<h2 class="name">NAME</h2>
<p> debconf-escape &#8211; helper when working with debconf&#8217;s escape capability </p>
<h2>SYNOPSIS</h2>
<pre>
 debconf-escape -e &lt; unescaped-text
 debconf-escape -u &lt; escaped-text
</pre>
<h2>DESCRIPTION</h2>
<p> When debconf has the &#8216;escape&#8217; capability set, it will expect commands you send it to have backslashes and newlines escaped (as <tt>&quot;\&quot;</tt> and <tt>&quot;
&quot;</tt> respectively) and will in turn escape backslashes and newlines in its replies. This can be used, for example, to substitute multi-line strings into templates, or to get multi-line extended descriptions reliably using <tt>&quot;METAGET&quot;</tt>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7) (available in the debconf-doc package)</p>
<h2>AUTHOR</h2>
<p> Colin Watson &lt;cjwatson [at] debian.org&gt; </p>
<h2>Index</h2>
