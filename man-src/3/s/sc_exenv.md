---
title: "sc_exenv(3)"
name: "sc_exenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_exenv/"
description: "sc::ExEnv –"
---

<p>sc::ExEnv &#8211; </p>
<p> The <code>ExEnv</code> class is used to find out about how the program is being run.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;exenv.h&gt;

Static Public Member Functions
static void init (int &amp;argcref, char **&amp;argvref)


Set the argument count and vector.


static int initialized ()


Return nonzero if ExEnv has been initialized.


static int &amp; argc ()


Return an reference to the argument count.


static char **&amp; argv ()


Return an reference to the argument vector.


static const char * program_name ()


Return argv[0] with the path removed.


static const char * hostname ()


Return the host name.


static const char * username ()


Return the user name.


static void set_out (std::ostream *o)



static std::ostream &amp; outn ()


Return an ostream that writes from all nodes.


static std::ostream &amp; errn ()


Return an ostream for error messages that writes from all nodes.


static std::ostream &amp; out0 ()


Return an ostream that writes from node 0.


static std::ostream &amp; err0 ()


Return an ostream for error messages that writes from node 0.


static size_t memory ()


The amount of memory on this node.


static int nproc ()


The number of processors on this node.



Static Protected Attributes
static int initialized_



static int * argc_



static char *** argv_



static char hostname_ [256]



static char username_ [9]



static size_t mem_



static int nproc_



static std::ostream * out_



static std::ostream * nullstream_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>ExEnv</code> class is used to find out about how the program is being run.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
