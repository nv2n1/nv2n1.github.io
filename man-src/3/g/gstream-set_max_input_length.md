---
title: "gstream-set_max_input_length(3)"
name: "gstream-set_max_input_length"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_max_input_length/"
description: "set_max_input_length"
---

<h2>NAME</h2>
<p> set_max_input_length</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_max_input_length(int)</code></p>
<h2>DESCRIPTION</h2>
<p> This sets the maximum number of characters that the inputter will accept from the user at the next, and only the next, input, i.e. if you call this function with 5 </p>
<pre>
   <a href="//www.systutorials.com/docs/linux/man/5-set_max_input_length/">set_max_input_length</a>(5);
   
</pre>
<p> and the user has made the following input </p>
<pre>
   abcde|
   
</pre>
<p> he won&#8217;t be able to enter anymore characters before at least one of them has been deleted. If the three middle characters are deleted </p>
<pre>
   a|e
   
</pre>
<p> then it is possible to enter three new characters wherever the user want. For example </p>
<pre>
   1a2e3|
   
</pre>
<p> Note that it is possible to set a default string which is longer than this supplied value; in that case the user will have to delete some characters if he wants to enter any himself. </p>
<p> Also note that this function only affects the next input, not the inputs after that. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-set_input_string/">gstream-set_input_string</a></code>(3) </p>
<h2>Index</h2>
