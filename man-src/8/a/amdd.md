---
title: "amdd(8)"
name: "amdd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amdd/"
description: "amdd – Amanda version of dd"
---

<p>amdd &#8211; Amanda version of dd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amdd</code> [-d] [<i>if=input</i>] [<i>of=output</i>] [<i>bs=blocksize</i>] [<i>skip=count</i>] [<i>count=count</i>]</dl>
<h2>Description</h2>
<p><code>Amdd</code></p>
<dd>provides just enough of the standard UNIX <code>dd</code> command for the needs of <i>Amanda</i>. This is handy when doing a full restore and the standard <code>dd</code> program has not yet been found. </p>
<p> <code>Amdd</code> also provides access to the <i>Amanda</i> output drivers that support various tape simulations. This may be used for debugging or to convert from one format to another. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about <i>Amanda</i>. See the <code>OUTPUT DRIVERS</code> section of <i><a href="/docs/linux/man/8-amanda/">amanda</a>(8)</i> for more information on the <i>Amanda</i> output drivers.</p>
<h2>Options</h2>
<p><code>-d</code></p>
<dl>
<dd>Turn on debugging output.</dl>
<p> <code>-l</code><i>length</i></p>
<dl>
<dd>Set the output length. If the output driver limits the output size, this controls when end of tape will be simulated. </p>
<p> <i>Length</i> may have a multiplier suffix: </p>
<dl>
<dd>
<pre>k -&gt; 1024 (Kilobytes)
b -&gt; 512 (Blocks)
M -&gt; 1024*1024 (Megabytes)</pre>
</dl>
<p> The default is no multiplier (bytes).</dl>
<p> <code>if=</code><i>input</i></p>
<dl>
<dd>Input to <code>dd</code>. Default is stdin.</dl>
<p> <code>of=</code><i>output</i></p>
<dl>
<dd>Where to send the output of <code>dd</code>. Default is stdout.</dl>
<p> <code>bs=</code><i>blocksize</i></p>
<dl>
<dd>Size of each record. Input records smaller than this will <i>not</i> be padded. Output records will be the same size as the corresponding input record. Default is 512 bytes. </p>
<p> <i>Blocksize</i> may have a multiplier suffix: </p>
<dl>
<dd>
<pre>k -&gt; 1024 (Kilobytes)
b -&gt; 512 (Blocks)
M -&gt; 1024*1024 (Megabytes)</pre>
</dl>
<p> The default is no multiplier (bytes).</dl>
<p> <code>count=</code><i>count</i></p>
<dl>
<dd>Number of records to copy. Default is all records until end of file.</dl>
<p> <code>skip=</code><i>count</i></p>
<dl>
<dd>Number of records to skip before copying input to output. Default is zero.</dl>
<h2>Author</h2>
<p>Marc Mengel &lt;mengel [at] fnal.gov&gt;, John R. Jackson &lt;jrj [at] purdue.edu&gt; : Original text </p>
<p> Stefan G. Weichinger, &lt;sgw [at] amanda.org&gt;, maintainer of the <i>Amanda</i>-documentation: XML-conversion</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), : <a rel="nofollow" href="http://wiki.zmanda.com">http://wiki.zmanda.com</a> </p>
