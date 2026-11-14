---
title: "sc_resultinfo(3)"
name: "sc_resultinfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_resultinfo/"
description: "sc::ResultInfo –"
---

<p>sc::ResultInfo &#8211; </p>
<p> This is a base class for all of Compute&#8217;s result types.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;compute.h&gt;</code></pre>
<p> Inherited by <code>sc::AccResultInfo</code>, <code>sc::NCResult&lt; T &gt;</code>, and <code>sc::Result&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ResultInfo</code> (<code>Compute</code> *c) </p>
<p> int &amp; <code>compute</code> () </p>
<p> const int &amp; <code>compute</code> () const </p>
<p> int <code>compute</code> (int c) </p>
<p> int &amp; <code>computed</code> () </p>
<p> const int &amp; <code>computed</code> () const </p>
<p> virtual int <code>needed</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>virtual void update ()



ResultInfo (StateIn &amp;, Compute *)



ResultInfo (const ResultInfo &amp;, Compute *)



virtual void save_data_state (StateOut &amp;)



virtual void restore_state (StateIn &amp;)



ResultInfo &amp; operator= (const ResultInfo &amp;)



Protected Attributes
int _compute



int _computed



Compute * _c</code></pre>
<h2>Detailed Description</h2>
<p>This is a base class for all of Compute&#8217;s result types. </p>
<p> Usually Result&lt;Type&gt; will be used to create a result that has a particular datum associated with it, however a <code>ResultInfo</code> can also be declared to keep track of datum&#8217;s for which it is awkward to use Result_dec.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
