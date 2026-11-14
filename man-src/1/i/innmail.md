---
title: "innmail(1)"
name: "innmail"
section: "1"
letter: "i"
url: "/docs/linux/man/1-innmail/"
description: "innmail – Simple mail-sending program"
---

<h2 class="name">NAME</h2>
<p> innmail &#8211; Simple mail-sending program </p>
<h2>SYNOPSIS</h2>
<p> <code>innmail</code> [<code>-h</code>] [<code>-s</code> <i>subject</i>] <i>address</i> [<i>address</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>innmail</code> is a Perl script intended to provide the non-interactive mail-sending functionality of <i><a href="/docs/linux/man/1-mail/">mail</a></i>(1) while avoiding nasty security problems. It takes the body of a mail message on standard input and sends it to the specified addresses by invoking the value of <i>mta</i> in <i>inn.conf</i>. </p>
<p> At least one address (formatted for the <font SIZE="-1">MTA</font> specified in <i>inn.conf</i>, if it matters) is required. <code>innmail</code> will sanitize the addresses so that they contain only alphanumerics and the symbols <tt>&quot;@&quot;</tt>, <tt>&quot;.&quot;</tt>, <tt>&quot;-&quot;</tt>, <tt>&quot;+&quot;</tt>, <tt>&quot;_&quot;</tt>, and <tt>&quot;%&quot;</tt>. </p>
<p> <code>innmail</code> was written to be suitable for the <i>mailcmd</i> setting in <i>inn.conf</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Gives usage information.</p>
<dt><code>-s</code> <i>subject</i></p>
<dd> Sets the Subject: header of the message. A warning is issued if this option is omitted.</dl>
<h2>EXAMPLES</h2>
<p> This sends a one-line message to the local user <tt>&quot;joe&quot;</tt>: </p>
<pre>
    echo &quot;A one-line message.&quot; | innmail -s &quot;Simple message&quot; joe
</pre>
<p> <code>innmail</code> by default is used by <font SIZE="-1">INN</font> for sending nightly reports and control message reports.</p>
<h2>BUGS</h2>
<p> <code>innmail</code> fails on addresses that begin with <tt>&quot;-&quot;</tt>, although one might hope that the news server will not need to contact any such addresses. </p>
<p> There are many &#8220;correct&#8221; addresses that will be silently modified by the sanitization process. A news administrator should be careful to use particularly sane addresses if they may be passed to <code>innmail</code>.</p>
<h2>HISTORY</h2>
<p> <code>innmail</code> was written by James Brister &lt;brister [at] vix.com&gt; for InterNetNews. This manual page was originally written by Jeffrey M. Vinocur. </p>
<p> <tt>$Id:</tt> innmail.pod 7851 2008-05-26 19:33:08Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/1-mail/">mail</a></i>(1). </p>
<h2>Index</h2>
