---
title: "gstream-set_input_string(3)"
name: "gstream-set_input_string"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_input_string/"
description: "set_input_string"
---

<h2>NAME</h2>
<p> set_input_string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_input_string(char const *s);</code></p>
<h2>DESCRIPTION</h2>
<p> This function provides a way to specify an editable default string when inputting. Consider the following example: </p>
<pre><code>
char buf[100];
gs &lt;&lt; "What's your opinion about gstream?
";

gs.set_input_string("I think it is incredible wonderful!");
gs.getline(buf, 100);
</code></pre>
<p> The user will see the following </p>
<pre>
   What's your opinion about gstream?
   I think it is incredible wonderful!|
   
</pre>
<p> where the &#8216;|&#8217; represents the cursor, and (s)he can edit the string, for example </p>
<pre>
   What's your opinion about gstream?
   I think it is superior, fantastic and| wonderful!
   
</pre>
<p> resulting in &#8216;buf&#8217; containing the string &quot;I think it is superior, fantastic and wonderful!&quot; </p>
<h2>Index</h2>
