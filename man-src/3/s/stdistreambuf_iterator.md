---
title: "stdistreambuf_iterator(3)"
name: "stdistreambuf_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdistreambuf_iterator/"
description: "std::istreambuf_iterator<CharT,Traits>::operator++,operator++(int) – std::istreambuf_iterator<CharT,Traits>::operator++,operator++(int)"
---

<p>std::istreambuf_iterator&lt;CharT,Traits&gt;::operator++,operator++(int) &#8211; std::istreambuf_iterator&lt;CharT,Traits&gt;::operator++,operator++(int)</p>
<h2>Synopsis</h2>
<p>istreambuf_iterator&amp; operator++(); <code>(1)</code><br />
/* proxy */ operator++(int); <code>(2)</code><br />
Advances the iterator by calling sbuf_-&gt;sbumpc() where sbuf_ is the stored pointer to the stream buffer.<br />
The behavior is undefined if the iterator is end-of-stream iterator. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) *this.<br />
2) A proxy object holding the current character obtained via operator*() and the sbuf_ pointer. Dereferencing a proxy object with operator* yields the stored character.<br />
The name proxy is for exposition only. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
