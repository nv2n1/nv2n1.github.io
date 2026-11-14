---
title: "varnetload(8)"
name: "varnetload"
section: "8"
letter: "v"
url: "/docs/linux/man/8-varnetload/"
description: "varnetload – tool to create reproducable network traffic"
---

<p>varnetload &#8211; tool to create reproducable network traffic</p>
<h2>Synopsis</h2>
<p><code>varnetload</code> [<i>-d delay</i>] [<i>-t time to run</i>] [<i>-u url</i>]</p>
<h2>Description</h2>
<p><code>varnetload</code> is a simple python script to create reproducable sustained network traffic. In order to use it effectively, you need to have an HTTP server present in your local LAN where you can put files. Upload a large HTML (or any other kind of file) to the HTTP server. Use the -u option of the script to point to that URL. Play with the delay option to vary the load put on your network.</p>
<dl>
<dt>delay</p>
<dd>Sets delay between individual downloads in miliseconds. Default value is 1000. But you my find values range from 0 to 500 more useful.</p>
<dt>time to run</p>
<dd>Sets total run time in seconds. Default value is 60.</p>
<dt>url</p>
<dd>Sets downloaded resource. Default is <a rel="nofollow" href="http://myhost.mydomain/index.html.">http://myhost.mydomain/index.html.</a> </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tuned/">tuned</a>(8) <a href="/docs/linux/man/8-diskdevstat/">diskdevstat</a>(8) <a href="/docs/linux/man/8-netdevstat/">netdevstat</a>(8) <a href="/docs/linux/man/8-scomes/">scomes</a>(8)</p>
<h2>Author</h2>
<p>Written by Phil Knirsch &lt;pknirsch [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;pknirsch [at] redhat.com&gt;.</p>
