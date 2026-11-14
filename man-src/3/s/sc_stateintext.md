---
title: "sc_stateintext(3)"
name: "sc_stateintext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateintext/"
description: "sc::StateInText –"
---

<p>sc::StateInText &#8211; </p>
<p> Reads state information written with <code>StateOutText</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state_text.h&gt;</code></pre>
<p> Inherits <code>sc::StateInFile</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>StateInText (std::istream &amp;s)



StateInText (const char *)



StateInText (const Ref&lt; KeyVal &gt; &amp;)



int getstring (char *&amp;)


This restores strings saved with StateOut::putstring.


int get_array_char (char *, int)


These restore data saved with StateOut's put.


int get_array_uint (unsigned int *, int)



int get_array_int (int *, int)



int get_array_float (float *, int)



int get_array_double (double *, int)



int get (const ClassDesc **)


This restores ClassDesc's.


int get (char &amp;r, const char *key=0)


These restore data saved with StateOut's put. members.


int get (unsigned int &amp;r, const char *key=0)



int get (int &amp;r, const char *key=0)



int get (float &amp;r, const char *key=0)



int get (double &amp;r, const char *key=0)



int get (char *&amp;)


These restore data saved with StateOut's put.


int get (unsigned int *&amp;)



int get (int *&amp;)



int get (float *&amp;)



int get (double *&amp;)



Protected Member Functions
void no_newline ()



void no_array ()



int read (char *)



int read (unsigned int &amp;)



int read (int &amp;)



int read (float &amp;)



int read (double &amp;)



void newline ()



void start_array ()



void end_array ()



int getobject (Ref&lt; SavableState &gt; &amp;)


This is used to restore an object.


void abort ()



Protected Attributes
int newlines_



int no_newline_



int no_array_</code></pre>
<h2>Detailed Description</h2>
<p>Reads state information written with <code>StateOutText</code>.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::StateInText::get (char *&amp;) [virtual]</h3>
<p>These restore data saved with StateOut&#8217;s put. members. The data is allocated by <code>StateIn</code>. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::StateInText::get (const <code>ClassDesc</code> **) [virtual]</h3>
<p>This restores ClassDesc&#8217;s. It will set the pointer to the address of the static <code>ClassDesc</code> for the class which has the same name as the class that had the <code>ClassDesc</code> that was saved by put(const ClassDesc*). </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::StateInText::get_array_char (char * p, int size) [virtual]</h3>
<p>These restore data saved with StateOut&#8217;s put. members. The data must be preallocated by the user. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::StateInText::getobject (<code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;) [protected, virtual]</h3>
<p>This is used to restore an object. It is called with the reference to the reference being restored. If the data being restored has previously been restored, then the pointer being restored is set to a reference to the previously restored object. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
