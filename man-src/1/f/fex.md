---
title: "fex(1)"
name: "fex"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fex/"
description: "fex – simple and powerful field extraction"
---

<h2 class="name">NAME</h2>
<p> fex &#8211; simple and powerful field extraction </p>
<h2>SYNOPSIS</h2>
<p> <code>fex</code> <i>selector &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> fex helps you split things by field. Common tasks you might do with awk or cut are much simpler in fex, and there are things in fex you can&#8217;t do nearly as easily in awk or cut.</p>
<h2>SELECTOR SYNTAX</h2>
<p> The selector syntax looks like this: </p>
<pre>
  &lt;delimiter&gt;&lt;selection&gt;...
</pre>
<p> The delimiter is a single character that is used to split the input string. </p>
<p> The first delimiter is implied as space &#8216; &#8216;. You can specify multiple fields with curly braces and numbers split by commas. Also valid in curly braces {} are number ranges. Number ranges are similar to python array slices, split by colon. </p>
<p> The selection is one of the following and is used to choose fields split by the delimiter.</p>
<dl>
<dt>a single number</p>
<dd> A single number will select that numbered field. Like awk, field start at 1. </p>
<p> Example selecting third field: </p>
<pre>
  % echo &quot;a b c d e&quot; | fex '3'
  a b c d
</pre>
<p> Example selecting the second field delimited by slash: </p>
<pre>
  % echo &quot;/home/hello/world&quot; | fex '/2'
  hello
</pre>
<dt>{N:M}</p>
<dd> This is a range selection. The syntax for ranges is, in curly braces, N:M, which chooses the fields in range N to M, inclusive. </p>
<p> Example selecting first through fourth fields: </p>
<pre>
  % echo &quot;a b c d e&quot; | fex '{1:4}'
  a b c d
</pre>
<dt>{N,M,&#8230;}</p>
<dd> The syntax for multiple selections is numbers within curly braces. </p>
<p> Example selecting first and fifth fields: </p>
<pre>
  % echo &quot;a b c d e&quot; | fex '{1,5}'
  a e
</pre>
<dt>{range,field,field,range,field}</p>
<dd> Combining the above, you can actually select ranges and individual fields using the {&#8230;} syntax by delimiting each selection by comma. </p>
<p> Example selecting fields 1 to 3, and 5: {1:3,5} </p>
<pre>
  % echo &quot;a b c d e&quot; | fex '{1:3,5}'
  a b c e
</pre>
<dt>{?range,field,&#8230;}</p>
<dd> The {?&#8230;} notation turns on &#8216;non greedy&#8217; field separation. The differences here can be shown best by example, first: </p>
<pre><code>
% echo "1...2.3.4" | fex '.{1:3}' 1.2.3 % echo "1...2.3.4" | fex '.{?1:3}' 1..
</code></pre>
<p> In the first example, fex uses &#8216;.&#8217; as delimiter and ignores empty fields. In the second example (non greedy), it does not ignore those empty fields.</p>
<dt>/regexp/</p>
<dd> The /regexp/ selection will choose only fields that match the given pattern. </p>
<p> Example, pulling out words with &#8216;addr:&#8217; in it from &#8216;ifconfig&#8217; output: </p>
<pre>
  % ifconfig | fex ' /addr:[0-9]/'    
  addr:127.0.0.1
  addr:192.168.0.28
</pre>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Show the <font SIZE="-1">MTU</font> for a given interface</p>
<dd> The &#8216;mtu&#8217; in ifconfig output looks like &#8216;mtu:1500&#8217;. So have fex split by space, then grab fields matching /mtu:/, split by colon, and choose the last field. </p>
<pre>
  % ifconfig wlan0 | fex ' /mtu:/:-1'
  1500
</pre>
<dt>Parse apache logs</p>
<dd> Pull the <font SIZE="-1">IP</font> address (first field by space) and the path requested (2nd field in &#8220;<font SIZE="-1">GET</font> &lt;path&gt; &#8230;&#8221;) </p>
<pre>
    % fex 1 '&quot;2 2' &lt; /b/logs/access
    65.57.245.11 /
    65.57.245.11 /icons/blank.gif
    65.57.245.11 /icons/folder.gif
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-awk/">awk</a></i>(1), <i><a href="/docs/linux/man/1-cut/">cut</a></i>(1), </p>
<p> Project site: &lt;<a rel="nofollow" href="http://www.semicomplete.com/projects/fex">http://www.semicomplete.com/projects/fex</a>&gt; </p>
<p> Source Code: &lt;<a rel="nofollow" href="https://github.com/jordansissel/fex">https://github.com/jordansissel/fex</a>&gt;</p>
<h2>CONTACT</h2>
<p> Please send questions to jls [at] semicomplete.com </p>
<p> File bugs and feature requests at the following <font SIZE="-1">URL:</font> </p>
<p> &lt;<a rel="nofollow" href="https://github.com/jordansissel/fex/issues">https://github.com/jordansissel/fex/issues</a>&gt; </p>
<p> Alternately, if you prefer email, feel free to file bugs by email. Whatever works for you :) </p>
<p> Patches, ideas, and other contributions by many, nice folks. See the <font SIZE="-1">CHANGELIST</font> file for who provided what.</p>
<h2>AUTHOR</h2>
<p> fex was written by Jordan Sissel. </p>
<h2>Index</h2>
