---
title: "rand_get_rand_method(3)"
name: "rand_get_rand_method"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rand_get_rand_method/"
description: "RAND crypto functions –"
---

<p>RAND crypto functions &#8211; </p>
<h3>Functions</h3>
<p>void <code>RAND_seed</code> (const void *indata, size_t size) </p>
<p> int <code>RAND_bytes</code> (void *outdata, size_t size) </p>
<p> void <code>RAND_cleanup</code> (void) </p>
<p> void <code>RAND_add</code> (const void *indata, size_t size, double entropi) </p>
<p> int <code>RAND_pseudo_bytes</code> (void *outdata, size_t size) </p>
<p> int <code>RAND_status</code> (void) </p>
<p> int <code>RAND_set_rand_method</code> (const RAND_METHOD *meth) </p>
<p> const RAND_METHOD * <code>RAND_get_rand_method</code> (void) </p>
<p> int <code>RAND_set_rand_engine</code> (ENGINE *engine) </p>
<p> int <code>RAND_load_file</code> (const char *filename, size_t size) </p>
<p> int <code>RAND_write_file</code> (const char *filename) </p>
<p> const char * <code>RAND_file_name</code> (char *filename, size_t size) </p>
<h2>Detailed Description</h2>
<p>See the <code>RAND &#8211; random number</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>void RAND_add (const void *indata, size_tsize, doubleentropi)</h3>
<p>Seed that random number generator. Secret material can securely be feed into the function, they will never be returned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>indata</i> the input data.<br />
 <i>size</i> size of in data.<br />
 <i>entropi</i> entropi in data.</dl>
<h3>int RAND_bytes (void *outdata, size_tsize)</h3>
<p>Get a random block from the random generator, can be used for key material. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>outdata</i> random data<br />
 <i>size</i> length random data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure.</dl>
<h3>void RAND_cleanup (void)</h3>
<p>Reset and free memory used by the random generator.</p>
<h3>const char* RAND_file_name (char *filename, size_tsize)</h3>
<p>Return the default random state filename for a user to use for <code>RAND_load_file()</code>, and <code>RAND_write_file()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filename</i> buffer to hold file name.<br />
 <i>size</i> size of buffer filename.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the buffer filename or NULL on failure.</dl>
<h3>const RAND_METHOD* RAND_get_rand_method (void)</h3>
<p>Get the default random method.</p>
<h3>int RAND_load_file (const char *filename, size_tsize)</h3>
<p>Load a a file and feed it into <code>RAND_seed()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filename</i> name of file to read.<br />
 <i>size</i> minimum size to read.</dl>
<h3>int RAND_pseudo_bytes (void *outdata, size_tsize)</h3>
<p>Get a random block from the random generator, should NOT be used for key material. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>outdata</i> random data<br />
 <i>size</i> length random data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure.</dl>
<h3>void RAND_seed (const void *indata, size_tsize)</h3>
<p>Seed that random number generator. Secret material can securely be feed into the function, they will never be returned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>indata</i> seed data<br />
 <i>size</i> length seed data</dl>
<h3>int RAND_set_rand_engine (ENGINE *engine)</h3>
<p>Set the default random method from engine. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>engine</i> use engine, if NULL is passed it, old method and engine is cleared.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure.</dl>
<h3>int RAND_set_rand_method (const RAND_METHOD *meth)</h3>
<p>Set the default random method. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>meth</i> set the new default method.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int RAND_status (void)</h3>
<p>Return status of the random generator </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the random generator can deliver random data.</dl>
<h3>int RAND_write_file (const char *filename)</h3>
<p>Write of random numbers to a file to store for later initiation with <code>RAND_load_file()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filename</i> name of file to write.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success and non-one on failure.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
