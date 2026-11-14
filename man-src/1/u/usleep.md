---
title: "usleep(1)"
name: "usleep"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usleep/"
description: "usleep – sleep some number of microseconds"
---

<h2>NAME</h2>
<p> usleep &#8211; sleep some number of microseconds</p>
<h2>SYNOPSIS</h2>
<p> <code>usleep</code> [<i>number</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>usleep</code> sleeps some number of microseconds. The default is 1.</p>
<h2>OPTIONS</h2>
<p> <i>&#8211;usage</i> Show short usage message.</p>
<dl>
<dt><i>&#8211;help, -?</i></p>
<dd> Print help information.</p>
<dt><i>-v, &#8211;version</i></p>
<dd> Print version information.</dl>
<h2>BUGS</h2>
<p> Probably not accurate on many machines down to the microsecond. Count on precision only to -4 or maybe -5.</p>
<h2>AUTHOR</h2>
<p> Donald Barnes &lt;djb [at] redhat.com&gt;<br />
 Erik Troan &lt;ewt [at] redhat.com&gt; </p>
<h2>Index</h2>
