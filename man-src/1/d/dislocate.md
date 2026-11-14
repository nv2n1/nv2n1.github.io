---
title: "dislocate(1)"
name: "dislocate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dislocate/"
description: "Dislocate – disconnect and reconnect processes"
---

<h2 class="name">NAME</h2>
<p> Dislocate &#8211; disconnect and reconnect processes </p>
<h2>SYNOPSIS</h2>
<p> <code>dislocate</code> [ <i>program args&#8230;</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>Dislocate</code> allows processes to be disconnected and reconnected to the terminal. Possible uses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> You can disconnect a process from a terminal at work and reconnect from home, to continue working.</p>
<dt>&bull;</p>
<dd> After having your line be dropped due to noise, you can get back to your process without having to restart it from scratch.</p>
<dt>&bull;</p>
<dd> If you have a problem that you would like to show someone, you can set up the scenario at your own terminal, disconnect, walk down the hall, and reconnect on another terminal.</p>
<dt>&bull;</p>
<dd> If you are in the middle of a great game (or whatever) that does not allow you to save, and someone else kicks you off the terminal, you can disconnect, and reconnect later.</dl>
</dl>
<h2>USAGE</h2>
<p> When run with no arguments, <code>Dislocate</code> tells you about your disconnected processes and lets you reconnect to one. Otherwise, <code>Dislocate</code> runs the named program along with any arguments. </p>
<p> By default, ^] is an escape that lets you talk to <code>Dislocate</code> itself. At that point, you can disconnect (by pressing ^D) or suspend <code>Dislocate</code> (by pressing ^Z). </p>
<p> Any Tcl or Expect command is also acceptable at this point. For example, to insert the contents of a the file /etc/motd as if you had typed it, say: </p>
<pre>
     send -i $out [exec cat /etc/motd]
</pre>
<p> To send the numbers 1 to 100 in response to the prompt &quot;next #&quot;, say: </p>
<pre><code>
     for {
         set i 0
     }
     {$i &lt; 100} {incr i} {
         expect - i $in "next #" send - i $out "$i"
     }
</code></pre>
<p> Scripts can also be prepared and sourced in so that you don&#8217;t have to type them on the spot. </p>
<p> <code>Dislocate</code> is actually just a simple <code>Expect</code> script. Feel free to make it do what you want it to do or just use <code>Expect</code> directly, without going through <code>Dislocate</code>. <code>Dislocate</code> understands a few special arguments. These should appear before any program name. Each should be separated by whitespace. If the arguments themselves takes arguments, these should also be separated by whitespace. </p>
<p> The <code>-escape</code> flag sets the escape to whatever follows. The default escape is ^]. </p>
<h2>CAVEATS</h2>
<p> This program was written by the author as an exercise to show that communicating with disconnected processes is easy. There are many features that could be added, but that is not the intent of this program. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3), <code><a href="/docs/linux/man/3-libexpect/">libexpect</a></code>(3)<br />
 <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<h2>Index</h2>
