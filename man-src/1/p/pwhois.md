---
title: "pwhois(1)"
name: "pwhois"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwhois/"
description: "pwhois – Perl written whois client"
---

<h2 class="name">NAME</h2>
<p> pwhois &#8211; Perl written whois client </p>
<h2>SYNOPSIS</h2>
<pre>
        pwhois perl.com
        pwhois gnu.org
        pwhois -s police.co.il
        pwhois -c there.is.no.tld.called.foobar
        pwhois yahoo.com whois.networksolutions.com
        pwhois -T 10 funet.fi
</pre>
<p> etc etc&#8230;..</p>
<h2>DESCRIPTION</h2>
<p> Just invoke with a domain name, optionally with a whois server name. Switches:<br />
&nbsp;<wbr><code>-s</code>&nbsp;<wbr>attempt to strip the copyright message or disclaimer.<br />
&nbsp;<wbr><code>-c</code>&nbsp;<wbr>attempts to return an empty answer for failed searches.<br />
&nbsp;<wbr><code>-e</code>&nbsp;<wbr>forces die if connection rate to server have been exceeded.<br />
&nbsp;<wbr><code>-T</code>&nbsp;<wbr>set timeout for connection attempts<br />
&nbsp;<wbr><code>-t</code>&nbsp;<wbr>enables caching.<br />
&nbsp;<wbr><code>-a</code>&nbsp;<wbr>specify an ip address that should be used as source address<br />
&nbsp;<wbr><code>-d</code>&nbsp;<wbr>enables debugging messages.<br />
&nbsp;<wbr><code>-F</code>&nbsp;<wbr>returns results of the first query of recursive whois requests<br />
&nbsp;<wbr><code>-L</code>&nbsp;<wbr>returns results of the last query of recursive whois requests&nbsp;<wbr>(the default)<br />
&nbsp;<wbr><code>-A</code>&nbsp;<wbr>returns results of the all queries of recursive whois requests</p>
<h2>AUTHORS</h2>
<p> Ariel Brosh <code>schop [at] cpan.org</code> </p>
<p> Current Maintainer: Walery Studennikov <code>despair [at] cpan.org</code></p>
<h2>SEE ALSO</h2>
<p> Net::Whois::Raw. </p>
<h2>Index</h2>
