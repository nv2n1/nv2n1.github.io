---
title: "gstream-operator(3)"
name: "gstream-operator"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-operator/"
description: "operator, operator"
---

<h2>NAME</h2>
<p> operator, operator</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>ostream&amp; operator&lt;&lt;(ostream&amp; o, fix const&amp; x);</code> </p>
<p> <code>istream&amp; operator&gt;&gt;(istream&amp; i, fix&amp; x);</code></p>
<h2>DESCRIPTION</h2>
<p> These two functions don&#8217;t actually belong to the gstreams, they are here simply because they sometimes make the life a bit easier (without costing anything in executable size if they are left unused). Their purpose is to make the class fix capable of extracting/inserting with the notation </p>
<pre>
   fix a_number = 0.3;
   cout &lt;&lt; a_number;
   cin &gt;&gt; a_number;
   
</pre>
<p> in conjuction with the standard stream system. And, by the way, consequently also in conjuction with a gstream: </p>
<pre>
   gstream gs;
   gs &lt;&lt; a_number;
   gs &gt;&gt; a_number;
   
</pre>
<p> You are probably not interested in calling them with their function names, only with the &lt;&lt;/&gt;&gt; operators, so this paragraph is written just to make you aware of the possibility of doing that. </p>
<h2>Index</h2>
