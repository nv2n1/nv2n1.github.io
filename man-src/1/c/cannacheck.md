---

title: "cannacheck(1)"
name: "cannacheck"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cannacheck/"
description: "cannacheck – Display information about Japanese input system Canna"
---

<h2>NAME</h2>
<p> cannacheck &#8211; Display information about Japanese input system Canna</p>
<p> <code>cannacheck [-v]</code></p>
<p> cannacheck displays the problems concerning use of Canna and the related information. It examines the following items:</p>
<dl>
<dt>&#8211;</dt>
<dd> Customize file to be used</dd>
<dt>&#8211;</dt>
<dd> Romaji-to-Kana conversion dictionary to be used</dd>
<dt>&#8211;</dt>
<dd> Destination to which the server is to be connected. Is it connectable?</dd>
<dt>&#8211;</dt>
<dd> Dictionaries to be mounted. Are they mountable?</dd>
<dt>&#8211;</dt>
<dd> Errors in the customize file</dd></dl>
<p> The problem(s) are displayed on the standard output if found.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-v</dt>
<dd> Displays all the above information including items that contain no problem.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/etc/canna/cannahost</dt>
<dd> Name of the host under which <i>cannaserver(1M)</i> is in operation.</dd></dl>
<h2>SEE ALSO</h2>
<p> cannaserver(1M), cannakill(1M), <a href="/docs/linux/man/1-cannastat/">cannastat</a>(1)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>CANNAHOST</dt>
<dd> Specifies the name of the host under which <i>cannaserver(1M)</i> is in operation.</dd>
<dt>CANNAFILE</dt>
<dd> Specifies the initialize file (.canna). </dd>
</dl>
