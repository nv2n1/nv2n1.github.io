---
title: "controlchan(8)"
name: "controlchan"
section: "8"
letter: "c"
url: "/docs/linux/man/8-controlchan/"
description: "controlchan – Channel-fed control message handler"
---

<p>controlchan &#8211; Channel-fed control message handler</p>
<h2>Synopsis</h2>
<p><code>controlchan</code> [<code>-ch</code>]</p>
<h2>Description</h2>
<p><code>controlchan</code> removes the responsibility for handling control messages (except cancels) from <code>innd</code> and instead processes them from a channel or file feed. </p>
<p> The two Perl modules <tt>&quot;Encode&quot;</tt> and <tt>&quot;MIME::Parser&quot;</tt> are required by <code>controlchan</code>. </p>
<p> To reduce load, <code>controlchan</code> keeps a copy of <i>control.ctl</i> and <i>control.ctl.local</i> in memory and checks permissions (including any required <font SIZE="-1">PGP</font> headers) before any scripts are called. These two configuration files are automatically reloaded when <code>controlchan</code> notices they have been modified. Also, the default case of an unrecognized control article is handled internally. The <tt>&quot;drop&quot;</tt> case is handled with far less fuss. </p>
<p> Normally, <code>controlchan</code> is invoked by <code>innd</code> as configured in <i>newsfeeds</i>. An example entry is below. Make sure that the newsgroup <tt>&quot;control.cancel&quot;</tt> exists so that <code>controlchan</code> does not have to scan through cancels, which it will not be processing anyway. </p>
<pre> controlchan!\
 :!*,control,control.*,!control.cancel\
 :AC,Tc,Wnsm\
 :&lt;pathbin in inn.conf&gt;/controlchan</pre>
<p><code>controlchan</code> can also be manually invoked with a mere path to a file (containing a complete control article with its headers and its body) or a token on its standard input: </p>
<pre> echo '/path/to/a/control/article' | controlchan
 echo '@0303465234000000000000235AE000000002@' | controlchan</pre>
<p>Note that in the (very, very unlikely) event that you need to process ihave/sendme control messages, be sure that <i>logipaddr</i> is set to false in <i>inn.conf</i>, because in this case <code>controlchan</code> needs a site name, not an <font SIZE="-1">IP</font> address. </p>
<p> <code>controlchan</code> tries to report all log messages through <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3), unless connected to an interactive terminal. To enable <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3)&#8217;ing for versions of Perl prior to 5.6.0, you will need to have run <code>h2ph</code> on your system include files at some point (this is required to make <tt>&quot;Sys::Syslog&quot;</tt> work). If you have not done so, do this: </p>
<pre> cd /usr/include
 h2ph * sys/*</pre>
<p>If you run FreeBSD, you will need to run the following in addition: </p>
<pre> h2ph machine/*</pre>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>By default, <code>controlchan</code> does not process articles whose Date: or Injection-Date: header fields are too far in the past (more than <i>artcutoff</i> days, as set in <i>inn.conf</i>) or one day in the future. It allows to prevent a malicious replay of old control articles. </p>
<p> Using the <code>-c</code> flag disables this check on the cutoff date.</p>
<dt><code>-h</code></p>
<dd>Gives usage information.</dl>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> controlchan.pod 9241 2011-07-12 09:57:44Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-control-ctl/">control.ctl</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5). </p>
