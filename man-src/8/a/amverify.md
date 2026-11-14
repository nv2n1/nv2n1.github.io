---
title: "amverify(8)"
name: "amverify"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amverify/"
description: "amverify – check an Amanda tape for errors"
---

<p>amverify &#8211; check an Amanda tape for errors</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amverify</code> <i>config</i> [<i>slot</i>&nbsp;<wbr>[<i>runtapes</i>]]</dl>
<h2>Description</h2>
<p><code>Amverify</code></p>
<dd>reads an Amanda format tape and makes sure each backup image can be processed by <code>amrestore</code> and, if possible, the appropriate restore program (e.g. <code>tar</code>). </p>
<p> <code>Amverify</code> runs <code>amrestore</code> on each file of the tape and pipes the output to a restore program (if available) with an option to create a catalogue of the backup. The catalogue itself is discarded. Only the success or failure of the operation itself is reported. </p>
<p> If the backup image cannot be processed by the restore program, e.g. if it was written on a different operating system, the image is sent through <code>dd</code> to /dev/null. This still determines if the tape is readable, but does not do any internal consistency check on the image. </p>
<p> If <i>config</i> is set up to use a tape changer, the <i>slot</i> argument may be used to choose the first tape to process. Otherwise, the <code>current</code> slot is used. </p>
<p> The <code>runtapes</code> configuration parameter determines how many tapes are processed unless it is specified on the command line. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Author</h2>
<p>Axel Zinser &lt;fifi [at] icem.de&gt; : Original text </p>
<p> Stefan G. Weichinger, &lt;sgw [at] amanda.org&gt;, maintainer of the <i>Amanda</i>-documentation: XML-conversion</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amverifyrun/">amverifyrun</a></code>(8), : <a rel="nofollow" href="http://wiki.zmanda.com">http://wiki.zmanda.com</a> </p>
