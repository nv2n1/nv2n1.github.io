---
title: "perlunitut(1)"
name: "perlunitut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunitut/"
description: "perlunitut – Perl Unicode Tutorial"
---

<h2 class="name">NAME</h2>
<p> perlunitut &#8211; Perl Unicode Tutorial </p>
<h2>DESCRIPTION</h2>
<p> The days of just flinging strings around are over. It&#8217;s well established that modern programs need to be capable of communicating funny accented letters, and things like euro symbols. This means that programmers need new habits. It&#8217;s easy to program Unicode capable software, but it does require discipline to do it right. </p>
<p> There&#8217;s a lot to know about character sets, and text encodings. It&#8217;s probably best to spend a full day learning all this, but the basics can be learned in minutes. </p>
<p> These are not the very basics, though. It is assumed that you already know the difference between bytes and characters, and realise (and accept!) that there are many different character sets and encodings, and that your program has to be explicit about them. Recommended reading is &#8220;The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)&#8221; by Joel Spolsky, at &lt;<a rel="nofollow" href="http://joelonsoftware.com/articles/Unicode.html">http://joelonsoftware.com/articles/Unicode.html</a>&gt;. </p>
<p> This tutorial speaks in rather absolute terms, and provides only a limited view of the wealth of character string related features that Perl has to offer. For most projects, this information will probably suffice.</p>
<h3>Definitions</h3>
<p> It&#8217;s important to set a few things straight first. This is the most important part of this tutorial. This view may conflict with other information that you may have found on the web, but that&#8217;s mostly because many sources are wrong. </p>
<p> You may have to re-read this entire section a few times&#8230; </p>
<p> <i>Unicode</i> </p>
<p> <code>Unicode</code> is a character set with room for lots of characters. The ordinal value of a character is called a <code>code point</code>. (But in practice, the distinction between code point and character is blurred, so the terms often are used interchangeably.) </p>
<p> There are many, many code points, but computers work with bytes, and a byte has room for only 256 values. Unicode has many more characters than that, so you need a method to make these accessible. </p>
<p> Unicode is encoded using several competing encodings, of which <font SIZE="-1">UTF-8</font> is the most used. In a Unicode encoding, multiple subsequent bytes can be used to store a single code point, or simply: character. </p>
<p> <i></i><font SIZE="-1"><i>UTF-8</i></font><i></i> </p>
<p> <font SIZE="-1"><code>UTF-8</code></font> is a Unicode encoding. Many people think that Unicode and <font SIZE="-1">UTF-8</font> are the same thing, but they&#8217;re not. There are more Unicode encodings, but much of the world has standardized on <font SIZE="-1">UTF-8.</font> </p>
<p> <font SIZE="-1">UTF-8</font> treats the first 128 codepoints, 0..127, the same as <font SIZE="-1">ASCII.</font> They take only one byte per character. All other characters are encoded as two to four bytes using a complex scheme. Fortunately, Perl handles this for us, so we don&#8217;t have to worry about this. </p>
<p> <i>Text strings (character strings)</i> </p>
<p> <code>Text strings</code>, or <code>character strings</code> are made of characters. Bytes are irrelevant here, and so are encodings. Each character is just that: the character. </p>
<p> On a text string, you would do things like: </p>
<pre><code>
$text = ~s / foo / bar / ;
if ($string = ~ / ^\d + $ /) {
    ...
}
$text = ucfirst $text;
my $character_count = length $text;
</code></pre>
<p> The value of a character (<tt>&quot;ord&quot;</tt>, <tt>&quot;chr&quot;</tt>) is the corresponding Unicode code point. </p>
<p> <i>Binary strings (byte strings)</i> </p>
<p> <code>Binary strings</code>, or <code>byte strings</code> are made of bytes. Here, you don&#8217;t have characters, just bytes. All communication with the outside world (anything outside of your current Perl process) is done in binary. </p>
<p> On a binary string, you would do things like: </p>
<p>my(@length_content) = unpack &#8220;(V/a)*&#8221;, $binary;<br />
$binary = ~s /
