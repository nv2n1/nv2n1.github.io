---
title: "overchan(8)"
name: "overchan"
section: "8"
letter: "o"
url: "/docs/linux/man/8-overchan/"
description: "overchan – Batch update the INN overview database"
---

<p>overchan &#8211; Batch update the INN overview database</p>
<h2>Synopsis</h2>
<p><code>overchan</code> [<i>file</i> &#8230;]</p>
<h2>Description</h2>
<p><code>overchan</code> reads overview data from the specified files or from standard input if no files are specified, and writes that data into the <font SIZE="-1">INN</font> overview database. (The file <tt>&quot;-&quot;</tt> means to read data from standard input as well.) Normally, overview data is stored by <code>innd</code> for articles as they&#8217;re accepted. For performance, however, it&#8217;s sometimes useful to have overview data written by a separate process. To do this, set <i>useoverchan</i> to true in <i>inn.conf</i> to tell <code>innd</code> to not write overview data directly and then add an <code>overchan</code> channel in <i>newsfeeds</i>: </p>
<pre> overview!:*:Tc,WnteO:&lt;pathbin&gt;/overchan</pre>
<p>where &lt;pathbin&gt; is <i>pathbin</i> in <i>inn.conf</i>. Additionally, <code>overchan</code> can be used to bulk-load overview data from appropriately formatted batch files (such as overflow files from an <code>overchan</code> channel). Each line of input should have the following format: </p>
<pre><code>&lt;token&gt; &lt;arrived&gt; &lt;expires&gt; &lt;data&gt;</code></pre>
<p> where &lt;token&gt; is the storage <font SIZE="-1">API</font> token of the article in textual form (surrounded by <tt>&quot;@&quot;</tt> characters), &lt;arrived&gt; is the arrival timestamp of the article in seconds since epoch, &lt;expires&gt; is the expiration time of the article in seconds since epoch or 0 if there is none, and &lt;data&gt; is the tab-separated overview data. Each of these fields must be separated by a single space.</p>
<h2>History</h2>
<p>Written by Rob Robertson &lt;rob [at] violet.berkeley.edu&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Man page rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> overchan.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) </p>
