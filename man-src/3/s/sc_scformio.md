---
title: "sc_scformio(3)"
name: "sc_scformio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scformio/"
---

sc::SCFormIO - 

 This utility class is used to print only on node 0 and to provide attractive indentation of output.

<h2>Synopsis</h2>

<pre><code>

#include &lt;formio.h&gt;

Static Public Member Functions
static std::ios &amp; indent (std::ios &amp;o)



static std::ios &amp; decindent (std::ios &amp;o)



static std::ios &amp; incindent (std::ios &amp;o)



static std::ios &amp; skipnextindent (std::ios &amp;o)



static void setverbose (std::ios &amp;o, long v)



static long getverbose (std::ios &amp;o)



static void setindent (std::ios &amp;o, long column)



static long getindent (std::ios &amp;o)



static int set_printnode (int)



static int get_printnode ()



static void set_debug (int)



static int get_debug ()



static void init_mp (int me)



static int get_node ()



static void set_default_basename (const char *)



static const char * default_basename ()



static char * fileext_to_filename (const char *extension)



static void init_ostream (std::ostream &amp;)



static std::ostream &amp; license (std::ostream &amp;)



static std::ostream &amp; warranty (std::ostream &amp;)



static std::ostream &amp; copyright (std::ostream &amp;)</code></pre>

<h2>Detailed Description</h2>

This utility class is used to print only on node 0 and to provide attractive indentation of output.

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
