---
title: "null(4)"
name: "null"
section: "4"
letter: "n"
url: "/docs/linux/man/4-null/"
description: "null, zero – data sink"
---

<p>null, zero &#8211; data sink</p>
<h2>Description</h2>
<p>Data written to the <i>/dev/null</i> and <i>/dev/zero</i> special files is discarded. </p>
<p> Reads from <i>/dev/null</i> always return end of file (i.e., <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 0), whereas reads from <i>/dev/zero</i> always return bytes containing zero (&#8216;
