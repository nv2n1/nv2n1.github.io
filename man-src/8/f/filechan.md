---
title: "filechan(8)"
name: "filechan"
section: "8"
letter: "f"
url: "/docs/linux/man/8-filechan/"
description: "filechan – file-writing backend for InterNetNews"
---

<p>filechan &#8211; file-writing backend for InterNetNews</p>
<h2>Synopsis</h2>
<p><code>filechan</code> [ <code>-d</code><i> directory</i> ] [ <code>-f</code><i> num_fields</i> ] [ <code>-m</code><i> mapfile</i> ] [ <code>-p</code><i> pidfile</i> ]</p>
<h2>Description</h2>
<p><i>Filechan</i> reads lines from standard input and copies certain fields in each line into files named by other fields within the line. <i>Filechan</i> is intended to be called by <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) as a channel feed. (It is not a full exploder and does not accept commands; see <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) for a description of the difference, and <i><a href="/docs/linux/man/8-buffchan/">buffchan</a></i>(8) for an exploder program.) </p>
<p> <i>Filechan</i> input is interpreted as a sequence of lines. Each line contains a fixed number of initial fields, followed by a variable number of filename fields. All fields in a line are separated by whitespace. The default number of initial fields is one. </p>
<p> For each line of input, <i>filechan</i> writes the initial fields, separated by whitespace and followed by a newline, to each of the files named in the filename fields. When writing to a file, <i>filechan</i> opens it in append mode and tries to lock it and change the ownership to the user and group who owns the directory where the file is being written. </p>
<p> Because the time window in which a file is open is very small, complicated flushing and locking protocols are not needed; a <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1) followed by a <i><a href="/docs/linux/man/1-sleep/">sleep</a></i>(1) for a couple of seconds is sufficient.</p>
<h2>Options</h2>
<dl>
<dt><code>-f num_fields</code></p>
<dd>The &#8220;<code>-f</code>&#8221; flag may be used to specify a different number of initial fields.</p>
<dt><code>-d directory</code></p>
<dd>By default, <i>filechan</i> writes its output into the directory <i>&lt;pathoutgoing in inn.conf&gt;</i>. The &#8220;<code>-d</code>&#8221; flag may be used to specify a directory the program should change to before starting.</p>
<dt><code>-p pidfile</code></p>
<dd>If the &#8220;<code>-p</code>&#8221; flag is used, the program will write a line containing its process ID (in text) to the specified file.</p>
<dt><code>-m mapfile</code></p>
<dd>A map file may be specified by using the &#8220;<code>-m</code>&#8221; flag. Blank lines and lines starting with a number sign (&#8220;#&#8221;) are ignored. All other lines should have two host names separated by a colon. The first field is the name that may appear in the input stream; the second field names the file to be used when the name in the first field appears. For example, the following map file may be used to map the short names used in the example below to the full domain names:</dl>
<dl>
<dd>
<pre># This is a comment
uunet:news.uu.net
foo:foo.com
munnari:munnari.oz.au</pre>
</dl>
<h2>Examples</h2>
<p>If <i>filechan</i> is invoked with &#8220;<code>-f 2</code>&#8221; and given the following input: </p>
<dl>
<dd>
<pre>news/software/b/132 &lt;1643 [at] munnari.oz.au&gt; foo uunet
news/software/b/133 &lt;102060 [at] litchi.foo.com&gt; uunet munnari
comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt; foo uunet munnari</pre>
</dl>
<p> Then the file <i>foo</i> will have these lines: </p>
<dl>
<dd>
<pre>news/software/b/132 &lt;1643 [at] munnari.oz.au&gt;
comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt;</pre>
</dl>
<p> the file <i>munnari</i> will have these lines: </p>
<dl>
<dd>
<pre>news/software/b/133 &lt;102060 [at] litchi.foo.com&gt;
comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt;</pre>
</dl>
<p> and the file <i>uunet</i> will have these lines: </p>
<dl>
<dd>
<pre>news/software/b/132 &lt;1643 [at] munnari.oz.au&gt;
news/software/b/133 &lt;102060 [at] litchi.foo.com&gt;
comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt;</pre>
</dl>
<h2>History</h2>
<p>Written by Robert Elz &lt;kre [at] munnari.oz.au&gt;, flags added by Rich $alz &lt;rsalz [at] uunet.uu.net&gt;. This is revision 5909, dated 2002-12-03.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-buffchan/">buffchan</a>(8), <a href="/docs/linux/man/5-inn-conf/">inn.conf</a>(5), <a href="/docs/linux/man/8-innd/">innd</a>(8), <a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5). </p>
