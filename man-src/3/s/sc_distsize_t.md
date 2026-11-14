---
title: "sc_distsize_t(3)"
name: "sc_distsize_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distsize_t/"
---

sc::distsize_t -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>distsize_t (int a)



distsize_t (unsigned int a)



distsize_t (unsigned long long a)



distsize_t &amp; operator= (const distsize_t &amp;a)



distsize_t &amp; operator+= (const distsize_t &amp;a)



distsize_t operator* (const distsize_t &amp;a) const



distsize_t operator+ (const distsize_t &amp;a) const



distsize_t operator- (const distsize_t &amp;a) const



distsize_t operator/ (const distsize_t &amp;a) const



distsize_t operator% (const distsize_t &amp;a) const



bool operator&lt; (const distsize_t &amp;a) const



bool operator&lt;= (const distsize_t &amp;a) const



bool operator&gt; (const distsize_t &amp;a) const



bool operator&gt;= (const distsize_t &amp;a) const



bool operator== (const distsize_t &amp;a) const



distsize_t operator* (const int &amp;a) const



distsize_t operator+ (const int &amp;a) const



distsize_t operator- (const int &amp;a) const



distsize_t operator/ (const int &amp;a) const



distsize_t operator% (const int &amp;a) const



Friends
size_t distsize_to_size (const distsize_t &amp;a)



distsize_t operator* (const int &amp;a, const distsize_t &amp;b)



distsize_t operator+ (const int &amp;a, const distsize_t &amp;b)



distsize_t operator- (const int &amp;a, const distsize_t &amp;b)



distsize_t operator/ (const int &amp;a, const distsize_t &amp;b)



distsize_t operator% (const int &amp;a, const distsize_t &amp;b)



ostream &amp; operator&lt;&lt; (ostream &amp;o, const distsize_t &amp;s)
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
