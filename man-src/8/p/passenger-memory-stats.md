---
title: "passenger-memory-stats(8)"
name: "passenger-memory-stats"
section: "8"
letter: "p"
url: "/docs/linux/man/8-passenger-memory-stats/"
description: "passenger-memory-stats – reports a snapshot of the Apache and Phusion Passenger memory statistcs"
---

<p>passenger-memory-stats &#8211; reports a snapshot of the Apache and Phusion Passenger memory statistcs</p>
<h2>Synopsis</h2>
<p><code>passenger-memory-stats</code></p>
<h2>Description</h2>
<p><code>passenger-memory-stats</code> allows you to easily analyze the real memory usage of Phusion Passenger and Apache. </p>
<p> Process inspection tools such as <i>ps</i> and <i>top</i> are useful, but they rarely show the correct memory usage. The real memory usage is usually lower than what <i>ps</i> and <i>top</i> report. </p>
<p> There are many technical reasons why this is so, but an explanation is beyond the scope of this page. We refer the interested reader to operating systems literature about virtual memory and copy-on-write. </p>
<p> When you run this tool the <i>Private</i> or <i>private dirty RSS</i> field shows the real memory usage of processes.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>HTTPD</code></p>
<dd>The full filename to the Apache executable. By default, Passenger will attempt to autodetect the Apache executable. If autodetection fails for whatever reason, then Apache processes will not be shown in the memory statistics. In that case, you may manually specify the location to the Apache executable using this environment variable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-passenger-status/">passenger-status</a>(8), <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/1-top/">top</a>(1), </p>
<p> User guide at <a rel="nofollow" href="https://www.phusionpassenger.com/documentation_and_support">https://www.phusionpassenger.com/documentation_and_support</a></p>
<h2>Author</h2>
<p>Phusion Passenger is written by Phusion (<a rel="nofollow" href="http://www.phusion.nl)">http://www.phusion.nl)</a> </p>
<p> &quot;Phusion&quot; and &quot;Phusion Passenger&quot; are trademarks of Hongli Lai &amp; Ninh Bui. </p>
<p> This manual page was written by Neil Wilson &lt;neil [at] brightbox.co.uk&gt; for the Ubuntu project (but may be used by others).</p>
