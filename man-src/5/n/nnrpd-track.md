---
title: "nnrpd-track(5)"
name: "nnrpd-track"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nnrpd-track/"
---

nnrpd.track - file to specify hosts to be tracked by nnrpd.

<h2>Description</h2>

This file, which is located in <i>&lt;pathetc in inn.conf&gt;,</i> specifies which hosts are to have their activities recorded during an <i>nnrpd</i> session. The <i>nnrpd</i> server reads it when first spawned by <i>innd</i>, provided <i>readertrack</i> in <i>inn.conf</i> is true; otherwise this file is not used. 

 Entries consist of one host specification per line, each line having two fields, separated by a colon:
<dl><dd><pre>host:identity</pre></dl>
 

 The first field is either the FQDN of a host, or a domain name (in the form *.domain.com). 

 The second field is simply a segment of text which may be used to more easily identify the client, typically an e-mail address or other identifying mark. 

 For example:
<dl><dd><pre>nasty.foo.com:nasty [at] foo.com
*.bar.com:VeryNastyClient</pre></dl>
 

 Written by Steve Carrie &lt;stephenc [at] uk.uu.net&gt; for InterNetNews. This is revision 5909, dated 2002-12-03.

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-inn-conf/">inn.conf</a>(5), <a HREF="/docs/linux/man/8-innd/">innd</a>(8), <a HREF="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5), <a HREF="/docs/linux/man/8-nnrpd/">nnrpd</a>(8), 
