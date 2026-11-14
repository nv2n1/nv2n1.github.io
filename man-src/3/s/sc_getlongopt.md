---
title: "sc_getlongopt(3)"
name: "sc_getlongopt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_getlongopt/"
description: "sc::GetLongOpt –"
---

<p>sc::GetLongOpt &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<pre><code>struct Cell



Public Types</code></pre>
<p> enum <code>OptType</code> { <code>NoValue</code>, <code>OptionalValue</code>, <code>MandatoryValue</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>GetLongOpt (const char optmark= '-')



int parse (int argc, char *const *argv)



int parse (char *const str, char *const p)



int enroll (const char *const opt, const OptType t, const char *const desc, const char *const val)



const char * retrieve (const char *const opt) const



void usage (std::ostream &amp;outfile=std::cout) const



void usage (const char *str)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
