---
title: "stdbasic_iostream(3)"
name: "stdbasic_iostream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_iostream/"
---

std::basic_iostream&lt;CharT,Traits&gt;::~basic_iostream - std::basic_iostream&lt;CharT,Traits&gt;::~basic_iostream

<h2>Synopsis</h2>

<pre><code>virtual ~basic_iostream();</code></pre> 
Destructs the input/output stream. 

<h2>Notes</h2>

This destructor does not perform any operation on the underlying stream buffer (rdbuf()): the destructors of the derived streams such as std::basic_fstream and std::basic_stringstream are responsible for calling the destructors of the stream buffers. 
