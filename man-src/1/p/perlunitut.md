---

title: "perlunitut(1)"
name: "perlunitut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunitut/"
description: "perlunitut – Perl Unicode Tutorial"
---

<p> The days of just flinging strings around are over. It&#8217;s well established that modern programs need to be capable of communicating funny accented letters, and things like euro symbols. This means that programmers need new habits. It&#8217;s easy to program Unicode capable software, but it does require discipline to do it right. </p>
<p> There&#8217;s a lot to know about character sets, and text encodings. It&#8217;s probably best to spend a full day learning all this, but the basics can be learned in minutes. </p>
<p> These are not the very basics, though. It is assumed that you already know the difference between bytes and characters, and realise (and accept!) that there are many different character sets and encodings, and that your program has to be explicit about them. Recommended reading is ``The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)&#8216;&#8216; by Joel Spolsky, at &lt;<a rel="nofollow" href="http://joelonsoftware.com/articles/Unicode.html">http://joelonsoftware.com/articles/Unicode.html</a>&gt;. </p>
<p> This tutorial speaks in rather absolute terms, and provides only a limited view of the wealth of character string related features that Perl has to offer. For most projects, this information will probably suffice.  </p>
<h3>Definitions</h3>
<p> It&#8217;s important to set a few things straight first. This is the most important part of this tutorial. This view may conflict with other information that you may have found on the web, but that&#8217;s mostly because many sources are wrong. </p>
<p> You may have to re-read this entire section a few times... </p>
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
<pre><code>    $text =~ s/foo/bar/;
    if ($string =~ /^\d+$/) { ... }
    $text = ucfirst $text;
    my $character_count = length $text;
</code></pre>
<p> The value of a character (<code>&quot;ord&quot;</code>, <code>&quot;chr&quot;</code>) is the corresponding Unicode code point. </p>
<p> <i>Binary strings (byte strings)</i> </p>
<p> <code>Binary strings</code>, or <code>byte strings</code> are made of bytes. Here, you don&#8217;t have characters, just bytes. All communication with the outside world (anything outside of your current Perl process) is done in binary. </p>
<p> On a binary string, you would do things like: </p>
<pre><code>    my (@length_content) = unpack &quot;(V/a)*&quot;, $binary;
    $binary =~ s/\x00\x0F/\xFF\xF0/; # for the brave :)
    print {$fh} $binary;
    my $byte_count = length $binary;
</code></pre>
<p> <i>Encoding</i> </p>
<p> <code>Encoding</code> (as a verb) is the conversion from <i>text</i> to <i>binary</i>. To encode, you have to supply the target encoding, for example <code>&quot;iso-8859-1&quot;</code> or <code>&quot;UTF-8&quot;</code>. Some encodings, like the <code>&quot;iso-8859&quot;</code> (``latin&#8217;&#8216;) range, do not support the full Unicode standard; characters that can&#8217;t be represented are lost in the conversion. </p>
<p> <i>Decoding</i> </p>
<p> <code>Decoding</code> is the conversion from <i>binary</i> to <i>text</i>. To decode, you have to know what encoding was used during the encoding phase. And most of all, it must be something decodable. It doesn&#8217;t make much sense to decode a <font SIZE="-1">PNG</font> image into a text string. </p>
<p> <i>Internal format</i> </p>
<p> Perl has an <code>internal format</code>, an encoding that it uses to encode text strings so it can store them in memory. All text strings are in this internal format. In fact, text strings are never in any other format! </p>
<p> You shouldn&#8217;t worry about what this format is, because conversion is automatically done when you decode or encode.  </p>
<h3>Your new toolkit</h3>
<p> Add to your standard heading the following line: </p>
<pre><code>    use Encode qw(encode decode);
</code></pre>
<p> Or, if you&#8217;re lazy, just: </p>
<pre><code>    use Encode;
</code></pre>
<h3>I/O flow (the actual 5 minute tutorial)</h3>
<p> The typical input/output flow of a program is: </p>
<pre><code>    1. Receive and decode
    2. Process
    3. Encode and output
</code></pre>
<p> If your input is binary, and is supposed to remain binary, you shouldn&#8217;t decode it to a text string, of course. But in all other cases, you should decode it. </p>
<p> Decoding can&#8217;t happen reliably if you don&#8217;t know how the data was encoded. If you get to choose, it&#8217;s a good idea to standardize on <font SIZE="-1">UTF-8.</font> </p>
<pre><code>    my $foo = decode('UTF-8', get 'http://example.com/');
    my $bar = decode('ISO-8859-1', readline STDIN);
    my $xyzzy = decode('Windows-1251', $cgi-&gt;param('foo'));
</code></pre>
<p> Processing happens as you knew before. The only difference is that you&#8217;re now using characters instead of bytes. That&#8217;s very useful if you use things like <code>&quot;substr&quot;</code>, or <code>&quot;length&quot;</code>. </p>
<p> It&#8217;s important to realize that there are no bytes in a text string. Of course, Perl has its internal encoding to store the string in memory, but ignore that. If you have to do anything with the number of bytes, it&#8217;s probably best to move that part to step 3, just after you&#8217;ve encoded the string. Then you know exactly how many bytes it will be in the destination string. </p>
<p> The syntax for encoding text strings to binary strings is as simple as decoding: </p>
<pre><code>    $body = encode('UTF-8', $body);
</code></pre>
<p> If you needed to know the length of the string in bytes, now&#8217;s the perfect time for that. Because <code>$body</code> is now a byte string, <code>&quot;length&quot;</code> will report the number of bytes, instead of the number of characters. The number of characters is no longer known, because characters only exist in text strings. </p>
<pre><code>    my $byte_count = length $body;
</code></pre>
<p> And if the protocol you&#8217;re using supports a way of letting the recipient know which character encoding you used, please help the receiving end by using that feature! For example, E-mail and <font SIZE="-1">HTTP</font> support <font SIZE="-1">MIME</font> headers, so you can use the <code>&quot;Content-Type&quot;</code> header. They can also have <code>&quot;Content-Length&quot;</code> to indicate the number of <i>bytes</i>, which is always a good idea to supply if the number is known. </p>
<pre><code>    &quot;Content-Type: text/plain; charset=UTF-8&quot;,
    &quot;Content-Length: $byte_count&quot;
</code></pre>
<h2>SUMMARY</h2>
<p> Decode everything you receive, encode everything you send out. (If it&#8217;s text data.)  </p>
<h2>Q and A (or FAQ)</h2>
<p> After reading this document, you ought to read perlunifaq too, then perluniintro.  </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Thanks to Johan Vromans from Squirrel Consultancy. His <font SIZE="-1">UTF-8</font> rants during the Amsterdam Perl Mongers meetings got me interested and determined to find out how to use character encodings in Perl in ways that don&#8217;t break easily. </p>
<p> Thanks to Gerard Goossen from <font SIZE="-1">TTY.</font> His presentation ``<font SIZE="-1">UTF-8</font> in the wild&#8217;&#8216; (Dutch Perl Workshop 2006) inspired me to publish my thoughts and write this tutorial. </p>
<p> Thanks to the people who asked about this kind of stuff in several Perl <font SIZE="-1">IRC</font> channels, and have constantly reminded me that a simpler explanation was needed. </p>
<p> Thanks to the people who reviewed this document for me, before it went public. They are: Benjamin Smith, Jan-Pieter Cornet, Johan Vromans, Lukas Mai, Nathan Gray.  </p>
<h2>AUTHOR</h2>
<p> Juerd Waalboer &lt;#####@juerd.nl&gt;  </p>
<h2>SEE ALSO</h2>
<p> perlunifaq, perlunicode, perluniintro, Encode </p>
