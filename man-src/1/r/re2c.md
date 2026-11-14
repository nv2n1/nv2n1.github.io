---
title: "re2c(1)"
name: "re2c"
section: "1"
letter: "r"
url: "/docs/linux/man/1-re2c/"
description: "re2c – convert regular expressions to C/C++"
---

<h2 class="name">NAME</h2>
<p> re2c &#8211; convert regular expressions to C/C++ </p>
<h2>SYNOPSIS</h2>
<p> <code>re2c</code> [<i>OPTIONS</i>] <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> <code>re2c</code> is a lexer generator for C/C++. It finds regular expression specifications inside of C/C++ comments and replaces them with a hard-coded DFA. The user must supply some interface code in order to control and customize the generated DFA.</p>
<h2>EXAMPLE</h2>
<p> Given the following code: </p>
<dl>
<dt>
<dd>
<pre><code>
unsigned int stou(const char *s)
{
#define YYCTYPE char
    const YYCTYPE *YYCURSOR = s;
    unsigned int result = 0;
    for (;;) {
        /*!re2c
            re2c:yyfill:enable = 0;
            "
