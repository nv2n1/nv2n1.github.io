---
title: "adime_evaluate(3)"
name: "adime_evaluate"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_evaluate/"
description: "adime_evaluate"
---

<h2>NAME</h2>
<p> adime_evaluate</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>double adime_evaluate(const char *equation, int *error,</code> <code>double (*var)(const char *name));</code></p>
<h2>DESCRIPTION</h2>
<p> Helper function for evaluating arithmetic expressions, which may be useful in your programs even though it isn&#8217;t really logically connected to the other functions (i.e. it&#8217;s not a gui function). It evaluates the provided equation, returning the result, and storing a nonzero value in `error&#8217; if anything goes wrong. If the `var&#8217; function is not NULL, this will be called whenever a variable is encountered in the expression, allowing you to look up and return a suitable value for it. For more information on the expressions, see expressi.txt </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_uevaluate/">adime_uevaluate</a></code>(3) </p>
<h2>Index</h2>
