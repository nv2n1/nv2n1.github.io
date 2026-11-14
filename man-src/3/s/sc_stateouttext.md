---
title: "sc_stateouttext(3)"
name: "sc_stateouttext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateouttext/"
description: "sc::StateOutText –"
---

<p>sc::StateOutText &#8211; </p>
<p> Writes out state information in an almost human readable format.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state_text.h&gt;</code></pre>
<p> Inherits <code>sc::StateOutFile</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateOutText</code> (std::ostream &amp;s) </p>
<p> <code>StateOutText</code> (const char *) </p>
<p> int <code>putstring</code> (const char *)<br />
 <i>This is like put except the length of the char array is determined by interpreting the character array as a character string. </i><br />
 int <code>put_array_char</code> (const char *, int)<br />
 <i>Put arrays of data. </i><br />
 int <code>put_array_uint</code> (const unsigned int *, int) </p>
<p> int <code>put_array_int</code> (const int *, int) </p>
<p> int <code>put_array_float</code> (const float *, int) </p>
<p> int <code>put_array_double</code> (const double *, int) </p>
<p> int <code>put</code> (const <code>ClassDesc</code> *)<br />
 <i>Write out information about the given </i><code>ClassDesc</code>.<br />
 int <code>put</code> (char r)<br />
 <i>Write the given datum. </i><br />
 int <code>put</code> (unsigned int r) </p>
<p> int <code>put</code> (int r) </p>
<p> int <code>put</code> (float r) </p>
<p> int <code>put</code> (double r) </p>
<p> int <code>put</code> (const char *, int)<br />
 <i>Write the given array data. </i><br />
 int <code>put</code> (const unsigned int *, int) </p>
<p> int <code>put</code> (const int *, int) </p>
<p> int <code>put</code> (const float *, int) </p>
<p> int <code>put</code> (const double *, int)</p>
<h3>Protected Member Functions</h3>
<pre><code>void no_newline ()



void no_array ()



void newline ()



void start_array ()



void end_array ()



int putobject (const Ref&lt; SavableState &gt; &amp;)


This will prepare StateOut to output a pointer to data.


int putparents (const ClassDesc *)



Protected Attributes
int no_newline_



int no_array_</code></pre>
<h2>Detailed Description</h2>
<p>Writes out state information in an almost human readable format. </p>
<p> <code>StateOutText</code> is intended for debugging only. The state information can read in again with <code>StateInText</code>.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::StateOutText::put (const char *, int) [virtual]</h3>
<p>Write the given array data. Size information is also saved. The data is allocated and read by the get(T*&amp;) routines. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>int sc::StateOutText::put_array_char (const char * p, int size) [virtual]</h3>
<p>Put arrays of data. No size information is stored. This data is read by the get_array_T routines. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>int sc::StateOutText::putobject (const <code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;) [protected, virtual]</h3>
<p>This will prepare <code>StateOut</code> to output a pointer to data. It first checks to see if the data has already been saved. If it has, then a reference to this data is saved. Otherwise the object is written out. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>int sc::StateOutText::putstring (const char *) [virtual]</h3>
<p>This is like put except the length of the char array is determined by interpreting the character array as a character string. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
