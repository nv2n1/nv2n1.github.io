---
title: "mailodf(1)"
name: "mailodf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailodf/"
description: "mailodf – Email ODF file as HTML archive"
---

<p>mailodf &#8211; Email ODF file as HTML archive</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mailodf</code> [-f&nbsp;<wbr><i>from</i>] [-s&nbsp;<wbr><i>subject</i>] <i>inputfile</i> <i>recipients</i>&#8230;</dl>
<h2>Description</h2>
<dd>mailodf is a program that will create a MIME-encapsulated web archive and then sends it as an email. Most email programs that understand HTML understands this format. </p>
<p> &#8220;Inputfile&#8221; is assumed to be an OpenDocument file of text, spreadsheet or presentation type.</p>
<h2>References</h2>
<dl>
<dt>
<dd> HTTRACK (<a rel="nofollow" href="http://www.httrack.com/)">http://www.httrack.com/)</a> can create such archives with the -%M option.</dl>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://en.wikipedia.org/wiki/MHTML">http://en.wikipedia.org/wiki/MHTML</a></dl>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.dsv.su.se/~jpalme/ietf/mhtml.html">http://www.dsv.su.se/~jpalme/ietf/mhtml.html</a></dl>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://users.otenet.gr/~geosp/kmhtconvert/">http://users.otenet.gr/~geosp/kmhtconvert/</a></dl>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.faqs.org/rfcs/rfc2557.html">http://www.faqs.org/rfcs/rfc2557.html</a></dl>
<h2>Example</h2>
<dl>
<dt>
<dd> <font SIZE="-1"> </font></p>
<pre>
mailodf -f lars.oppermann [at] sun.com -s &quot;F.Y.I&quot; odf-file
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>See Also</h2>
<p> odf2mht</p>
<h2>Author</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>
