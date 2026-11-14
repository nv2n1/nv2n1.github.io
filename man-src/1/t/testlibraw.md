---
title: "testlibraw(1)"
name: "testlibraw"
section: "1"
letter: "t"
url: "/docs/linux/man/1-testlibraw/"
description: "testlibraw – run basic functionality tests on libraw1394"
---

<h2>NAME</h2>
<p> testlibraw &#8211; run basic functionality tests on libraw1394</p>
<h2>SYNOPSIS</h2>
<p> <code>testlibraw</code></p>
<h2>DESCRIPTION</h2>
<p> testlibraw attaches to the Linux IEEE 1394 subsystem through libraw1394 and tries to read data from all connected nodes. It therefore acts as a check that:</p>
<dl>
<dt>*</p>
<dd> libraw1394 is installed correctly</p>
<dt>*</p>
<dd> the IEEE 1394 subsystem is loaded in the kernel and of a supported version</p>
<dt>*</p>
<dd> libraw1394 and kernel side raw1394 can communicate</p>
<dt>*</p>
<dd> connected nodes can be reached and do respond.</dl>
<p> The read transactions are of a form that all powered up nodes conforming to the IEEE 1394 standard have to be able to respond to. </p>
<p> The source of this program also acts as a demonstration of libraw1394 programming, including initialization, transactions and the event loop.</p>
<h2>EXAMPLE RUN</h2>
<p> FIXME: insert example here</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://linux1394.sourceforge.net/">http://linux1394.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> Andreas Bombe &lt;aeb [at] debian.org&gt; </p>
<h2>Index</h2>
