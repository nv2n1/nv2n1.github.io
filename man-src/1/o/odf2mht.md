---
title: "odf2mht(1)"
name: "odf2mht"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odf2mht/"
description: "odf2mht – Convert ODF to HTML archive"
---

<p>odf2mht &#8211; Convert ODF to HTML archive</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>odf2mht</code> <i>path</i></dl>
<h2>Description</h2>
<p> <code>Odf2mht</code></p>
<dd>is a program that will create a MIME-encapsulated web archive (.mht) format where images are preserved. The file can be read by Internet Explorer, MS-Word and many email programs such as MS-Outlook. It will write the web archive to stdout. </p>
<p> &#8220;Path&#8221; is assumed to be an OpenDocument file of text, spreadsheet or presentation type.</p>
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
odf2mht example.odt &gt;example.mht
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>Bugs</h2>
<p> IE6 seems to have problems with large MHT files.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-odftools/">odftools</a></code>(1), <code><a href="/docs/linux/man/1-odf2war/">odf2war</a></code>(1), <code><a href="/docs/linux/man/1-mailodf/">mailodf</a></code>(1)</p>
<h2>Author</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>
