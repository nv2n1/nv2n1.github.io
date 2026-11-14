---
title: "readpass(3)"
name: "readpass"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readpass/"
description: "readpass – read password"
---

<p>readpass &#8211; read password</p>
<h2>Library</h2>
<p>Readpass library (librpass, -lrpass)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;readpass.h&gt;
char *readpass(const char *prompt, char display, size_t len);</code></pre>
<h2>Description</h2>
<p>The readpass() function reads in password from standard input. readpass displays the <code>prompt</code>, turns off character echo, and reads the password string of up to <code>len</code> number of characters or till a newline character, whichever occurs first. While reading password, readpass shows <code>display</code> character instead of actual input entered by user, and then turns on the character echo.</p>
<h2>Return Value</h2>
<p>readpass returns pointer to a dynamically allocated buffer holding the password, or NULL otherwise.</p>
<h2>Note</h2>
<p>The pointer returned, points to the password in its clear text form, thus user should take care of its confidentiality. </p>
<p> Secondly, don&#8217;t forget to release memory (<a href="/docs/linux/man/3-free/">free</a>(3)) allocated by readpass to store password.</p>
<h2>Bugs</h2>
<p>If you encounter any problems/bugs in working of readpass(), please send an email to &lt;pj.pandit AT yahoo.co.in&gt; mentioning about problem/bug; while doing so, do include &#8216;readpass()&#8217; string in the subject line.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-tlock/">tlock</a>(1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a href="/docs/linux/man/3-free/">free</a>(3) <a href="/docs/linux/man/3-crypt/">crypt</a>(3)</p>
<h2>Author</h2>
<p>Prasad J Pandit &lt;<i>pj.pandit AT yahoo.co.in</i>&gt;</p>
