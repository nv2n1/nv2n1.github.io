---
title: "mailaddr(7)"
name: "mailaddr"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mailaddr/"
description: "mailaddr – mail addressing description"
---

<p>mailaddr &#8211; mail addressing description</p>
<h2>Description</h2>
<p>This manual page gives a brief introduction to SMTP mail addresses, as used on the Internet. These addresses are in the general format </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>user [at] domain</p>
<p> where a domain is a hierarchical dot-separated list of subdomains. These examples are valid forms of the same address: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>john.doe [at] monet.example.com</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>John Doe &lt;john.doe [at] monet.example.com&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>john.doe [at] monet.example.com (John Doe)</p>
<p> The domain part (&quot;monet.example.com&quot;) is a mail-accepting domain. It can be a host and in the past it usually was, but it doesn&#8217;t have to be. The domain part is not case sensitive. </p>
<p> The local part (&quot;john.doe&quot;) is often a username, but its meaning is defined by the local software. Sometimes it is case sensitive, although that is unusual. If you see a local-part that looks like garbage, it is usually because of a gateway between an internal e-mail system and the net, here are some examples: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&quot;surname/admd=telemail/c=us/o=hp/prmd=hp&quot;@some.where</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>USER%SOMETHING [at] some.where</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>machine!machine!name [at] some.where</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>I2461572 [at] some.where</p>
<p> (These are, respectively, an X.400 gateway, a gateway to an arbitrary internal mail system that lacks proper internet support, an UUCP gateway, and the last one is just boring username policy.) </p>
<p> The real-name part (&quot;John Doe&quot;) can either be placed before &lt;&gt;, or in () at the end. (Strictly speaking the two aren&#8217;t the same, but the difference is beyond the scope of this page.) The name may have to be quoted using &quot;&quot;, for example, if it contains &quot;.&quot;: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&quot;John Q. Doe&quot; &lt;john.doe [at] monet.example.com&gt;</p>
<h3>Abbreviation</h3>
<p>Some mail systems let users abbreviate the domain name. For instance, users at example.com may get away with &quot;john.doe [at] monet&quot; to send mail to John Doe. <i>This behavior is deprecated.</i> Sometimes it works, but you should not depend on it.</p>
<h3>Route-addrs</h3>
<p>In the past, sometimes one had to route a message through several hosts to get it to its final destination. Addresses which show these relays are termed &quot;route-addrs&quot;. These use the syntax: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;@hosta,@hostb:user [at] hostc&gt;</p>
<p> This specifies that the message should be sent to hosta, from there to hostb, and finally to hostc. Many hosts disregard route-addrs and send directly to hostc. </p>
<p> Route-addrs are very unusual now. They occur sometimes in old mail archives. It is generally possible to ignore all but the &quot;user [at] hostc&quot; part of the address to determine the actual address.</p>
<h3>Postmaster</h3>
<p>Every site is required to have a user or user alias designated &quot;postmaster&quot; to which problems with the mail system may be addressed. The &quot;postmaster&quot; address is not case sensitive.</p>
<h2>Files</h2>
<p><i>/etc/aliases</i><br />
 <i>~/.forward</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), <code><a href="/docs/linux/man/5-forward/">forward</a></code>(5), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8) </p>
<p> IETF RFC 5322</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
