---
title: "sc_assignedkeyval(3)"
name: "sc_assignedkeyval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_assignedkeyval/"
description: "sc::AssignedKeyVal –"
---

<p>sc::AssignedKeyVal &#8211; </p>
<p> This class allows keyval associations to be set up by the program, rather than determined by an external file.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;keyval.h&gt;</code></pre>
<p> Inherits <code>sc::KeyVal</code>.</p>
<h3>Public Member Functions</h3>
<p>void <code>clear</code> ()<br />
 <i>Erase all of the stored assignments. </i> <code>Assignments.</code><br />
 Each of this routines assigns key to val. </p>
<pre><code>void assign (const char *key, const Ref&lt; KeyValValue &gt; &amp;val)



void assign (const char *key, double val)



void assignboolean (const char *key, int val)



void assign (const char *key, float val)



void assign (const char *key, char val)



void assign (const char *key, int val)



void assign (const char *key, const char *val)



void assign (const char *key, const Ref&lt; DescribedClass &gt; &amp;val)



Protected Member Functions</code></pre>
<p> int <code>key_exists</code> (const char *)<br />
 <i>Ultimately called by exists. </i><br />
 <code>Ref</code>&lt; <code>KeyValValue</code> &gt; <code>key_value</code> (const char *, const <code>KeyValValue</code> &amp;def)<br />
 <i>Ultimately called by value. </i></p>
<h2>Detailed Description</h2>
<p>This class allows keyval associations to be set up by the program, rather than determined by an external file.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
