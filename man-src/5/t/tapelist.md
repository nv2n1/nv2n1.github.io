---
title: "tapelist(5)"
name: "tapelist"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tapelist/"
description: "tapelist – The list of Amanda volumes in use"
---

<p>tapelist &#8211; The list of Amanda volumes in use</p>
<h2>Description</h2>
<p>The <i>tapelist</i> file contains the list of tapes in active use. This file is not ordinarily ordinarily edited or examined manually. Its format may change, or it may be removed altogether, in future versions of Amanda. It contains lines of the form: </p>
<pre>YYYYMMDD label flags [BARCODE:barcode] [META:meta] [BLOCKSIZE:blocksize] [#comment]</pre>
<p>Where <i>YYYYMMDD</i> is the date the tape was written, <i>label</i> is a label for the tape as written by <code>amlabel</code> and <i>flags</i> is one of &quot;reuse&quot; or &quot;no-reuse&quot; and tells Amanda whether the tape may be reused. A non-reusable tape will not be overwritten, even if it is older than <code>dumpcycle</code> dumps. See the <code>reuse</code> options of <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8). The optional barcode is prefixed with &#8216;BARCODE&#8217; if the volume have a barcode. The optional meta label is prefixed with &#8216;META&#8217; if the volume is on a meta volume. The optional blocksize is prefixed with &#8216;BLOCKSIZE&#8217;. The optional comment is prefixed with a &#8216;#&#8217; and continues to the end of the line. Amanda will maintain this comment until the tape is overwritten. Note that comments are not allowed on blank lines. </p>
<p> The file is sorted such that the most-recently used tape appears on the first line, and the oldest tape appears on the last line. </p>
<p> <code>Amdump</code> and <code>amflush</code> will by default refuse to write to an unlabeled tape, or to a labeled tape that is considered active or marked &quot;no-reuse&quot;. There must be more tapes in active rotation (see the <code>tapecycle</code> option) than there are runs in the backup cycle (see the <code>dumpcycle</code> option) to prevent overwriting a backup image that would be needed to do a full recovery.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt; </p>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
