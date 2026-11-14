---
title: "strnstr(3)"
name: "strnstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strnstr/"
description: "strnstr – locate a substring in a string"
---

<p><code>strnstr</code> &#8211; locate a substring in a string</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/string.h Ft char * Fn strnstr const char *big const char *little size_t len</p>
<h2>Description</h2>
<p>The Fn strnstr function locates the first occurrence of the null-terminated string Fa little in the string Fa big , where not more than Fa len characters are searched. Characters that appear after a `
