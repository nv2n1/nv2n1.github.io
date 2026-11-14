---
title: "cvtbatch(8)"
name: "cvtbatch"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cvtbatch/"
description: "cvtbatch – Convert Usenet batch files to INN format"
---

<p>cvtbatch &#8211; Convert Usenet batch files to INN format</p>
<h2>Synopsis</h2>
<p><code>cvtbatch</code> [<code>-w</code> <i>items</i>]</p>
<h2>Description</h2>
<p><code>cvtbatch</code> reads standard input as a sequence of lines, converts each line, and writes it to standard output. It is used to convert simple batch files that contain just the storage <font SIZE="-1">API</font> token of an article to <font SIZE="-1">INN</font> batch files that contain additional information about each article. </p>
<p> Each line is taken as a storage <font SIZE="-1">API</font> token indicating a Usenet article. Only the first word of each line is parsed; anything following whitespace is ignored. Lines not starting with a valid token are also silently ignored. </p>
<p> If the input file consists of a series of message-IDs, then use <code>grephistory</code> with the <code>-s</code> flag piped into <code>cvtbatch</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-w</code> <i>items</i></p>
<dd>The <code>-w</code> flag specifies how each output line should be written. The items for this flag should be chosen from the <tt>&quot;W&quot;</tt> flag items as specified in <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). They may be chosen from the following set: </p>
<pre> b Size of the article in bytes.
 f Storage API token of the article (same as &quot;n&quot;).
 m Article message-ID.
 n Storage API token of the article.
 t Arrival time of the article as seconds since epoch.</pre>
<p>The default is <tt>&quot;nm&quot;</tt>, that is to say the storage <font SIZE="-1">API</font> token followed by the message-ID of the article.</dl>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> cvtbatch.pod 8776 2009-11-15 09:24:06Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-grephistory/">grephistory</a></i>(1), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). </p>
