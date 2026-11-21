---

title: "jack_wait(1)"
name: "jack_wait"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_wait/"
description: "jack_wait – JACK toolkit client to check and wait for existence/exit of jackd."
---

<p> jack_wait &#8211; JACK toolkit client to check and wait for existence/exit of jackd.</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_wait</code> [ <i>-s</i> | <i>&#8211;server</i> servername ] [ <i>-t</i> | <i>&#8211;timeout</i> timeout_seconds [ <i>-cqwhv</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>jack_wait</code> When invoked with <i>-c</i> it only checks for the existence of a jack server. When invoked with <i>-w</i> the program will wait for a jackd to be available. The <i>-q</i> makes it wait for the jackd to exit. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code>, <code>&#8211;wait</code></dt>
<dd>
 Wait for jackd to be available.</dd>
<dt><code>-q</code>, <code>&#8211;quit</code></dt>
<dd>
 Wait for jackd quit.</dd>
<dt><code>-c</code>, <code>&#8211;check</code></dt>
<dd>
 Only check for existence of jackd, and exit.</dd>
<dt><code>-s</code>, <code>&#8211;server</code> <i>servername</i></dt>
<dd>
 Connect to the jack server named <i>servername</i></dd>
<dt><code>-t</code>, <code>&#8211;timeout</code> <i>timeout_seconds</i></dt>
<dd>
 Only wait <i>timeout_seconds</i>.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Display help/usage message</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>
 Output version information and exit </dd>
</dl>
