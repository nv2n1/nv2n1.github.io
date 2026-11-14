---
title: "admblackboxmethods(3)"
name: "admblackboxmethods"
section: "3"
letter: "a"
url: "/docs/linux/man/3-admblackboxmethods/"
description: "AdmBlackBoxMethods –"
---

<p>AdmBlackBoxMethods &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/blackbox.h">blackbox.h</a>&gt; </p>
<h3>Public Attributes</h3>
<p>void(* <code>free</code> )(void *data) </p>
<p> <code>AdmContext</code> *(* <code>read</code> )(void *data, <code>AdmError</code> **error) </p>
<p> unsigned int(* <code>listSerial</code> )(void *data, unsigned int *array, unsigned int array_len, unsigned int top_serial, <code>AdmError</code> **error) </p>
<p> <code>AdmContext</code> *(* <code>readSerial</code> )(void *data, unsigned int serial, <code>AdmError</code> **error) </p>
<p> int(* <code>write</code> )(void *data, <code>AdmContext</code> *context, <code>AdmError</code> **error) </p>
<h2>Member Data Documentation</h2>
<h3>void(* <code>AdmBlackBoxMethods::free</code>)(void *data)</h3>
<h3><code>AdmContext</code>*(* <code>AdmBlackBoxMethods::read</code>)(void *data, <code>AdmError</code> **error)</h3>
<h3>unsigned int(* <code>AdmBlackBoxMethods::listSerial</code>)(void *data, unsigned int *array, unsigned int array_len, unsigned int top_serial, <code>AdmError</code> **error)</h3>
<h3><code>AdmContext</code>*(* <code>AdmBlackBoxMethods::readSerial</code>)(void *data, unsigned int serial, <code>AdmError</code> **error)</h3>
<h3>int(* <code>AdmBlackBoxMethods::write</code>)(void *data, <code>AdmContext</code> *context, <code>AdmError</code> **error)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Alchemist from the source code.</p>
