---
title: "sc_filerender(3)"
name: "sc_filerender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_filerender/"
description: "sc::FileRender –"
---

<p>sc::FileRender &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Render</code>. Inherited by <code>sc::OOGLRender</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>FileRender (const char *filename)



FileRender (std::ostream &amp;o=ExEnv::out0())



FileRender (const Ref&lt; KeyVal &gt; &amp;)



void clear ()



virtual void set_filename (const char *name)



virtual void set_basename (const char *name)



virtual const char * file_extension ()



Protected Member Functions
char * get_filename (const char *objectname)



void open_sbuf (const char *objectname)



void close_sbuf ()



Protected Attributes
char * filename_



char * basename_



std::streambuf * sbuf_



int delete_sbuf_



int depth_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
