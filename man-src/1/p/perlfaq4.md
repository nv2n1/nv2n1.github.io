---
title: "perlfaq4(1)"
name: "perlfaq4"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq4/"
description: "perlfaq4 – Data Manipulation"
---

<h2 class="name">NAME</h2>
<p> perlfaq4 &#8211; Data Manipulation </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section of the <font SIZE="-1">FAQ</font> answers questions related to manipulating numbers, dates, strings, arrays, hashes, and miscellaneous data issues.</p>
<h2>Data: Numbers</h2>
<h3>Why am I getting long decimals (eg, 19.9499999999999) instead of the numbers I should be getting (eg, 19.95)?</h3>
<p> For the long explanation, see David Goldberg&#8217;s &#8220;What Every Computer Scientist Should Know About Floating-Point Arithmetic&#8221; (&lt;<a rel="nofollow" href="http://web.cse.msu.edu/~cse320/Documents/FloatingPoint.pdf">http://web.cse.msu.edu/~cse320/Documents/FloatingPoint.pdf</a>&gt;). </p>
<p> Internally, your computer represents floating-point numbers in binary. Digital (as in powers of two) computers cannot store all numbers exactly. Some real numbers lose precision in the process. This is a problem with how computers store numbers and affects all computer languages, not just Perl. </p>
<p> perlnumber shows the gory details of number representations and conversions. </p>
<p> To limit the number of decimal places in your numbers, you can use the <tt>&quot;printf&quot;</tt> or <tt>&quot;sprintf&quot;</tt> function. See &#8220;Floating-point Arithmetic&#8221; in perlop for more details. </p>
<pre>
    printf &quot;%.2f&quot;, 10/3;
    my $number = sprintf &quot;%.2f&quot;, 10/3;
</pre>
<h3>Why is <code>int()</code> broken?</h3>
<p> Your <tt>&quot;int()&quot;</tt> is most probably working just fine. It&#8217;s the numbers that aren&#8217;t quite what you think. </p>
<p> First, see the answer to &#8220;Why am I getting long decimals (eg, 19.9499999999999) instead of the numbers I should be getting (eg, 19.95)?&#8221;. </p>
<p> For example, this </p>
<pre>
    print int(0.6/0.2-2), &quot;
&quot;;
</pre>
<p> will in most computers print 0, not 1, because even such simple numbers as 0.6 and 0.2 cannot be presented exactly by floating-point numbers. What you think in the above as &#8216;three&#8217; is really more like 2.9999999999999995559.</p>
<h3>Why isn&#8217;t my octal data interpreted correctly?</h3>
<p> (contributed by brian d foy) </p>
<p> You&#8217;re probably trying to convert a string to a number, which Perl only converts as a decimal number. When Perl converts a string to a number, it ignores leading spaces and zeroes, then assumes the rest of the digits are in base 10: </p>
<pre>
    my $string = '0644';
    print $string + 0;  # prints 644
    print $string + 44; # prints 688, certainly not octal!
</pre>
<p> This problem usually involves one of the Perl built-ins that has the same name a Unix command that uses octal numbers as arguments on the command line. In this example, <tt>&quot;chmod&quot;</tt> on the command line knows that its first argument is octal because that&#8217;s what it does: </p>
<pre>
    %prompt&gt; chmod 644 file
</pre>
<p> If you want to use the same literal digits (644) in Perl, you have to tell Perl to treat them as octal numbers either by prefixing the digits with a <tt>0</tt> or using <tt>&quot;oct&quot;</tt>: </p>
<pre><code>
chmod(0644, $filename);
#right, has leading zero
            chmod(oct(644), $filename);
#also correct
</code></pre>
<p> The problem comes in when you take your numbers from something that Perl thinks is a string, such as a command line argument in <tt>@ARGV</tt>: </p>
<p>chmod($ARGV[0], $filename);<br />
#wrong, even if &#8220;0644&#8221; chmod(oct($ARGV[0]), $filename);<br />
#correct, treat string as octal</p>
<p> You can always check the value you&#8217;re using by printing it in octal notation to ensure it matches what you think it should be. Print it in octal and decimal format: </p>
<pre>
    printf &quot;0%o %d&quot;, $number, $number;
</pre>
<h3>Does Perl have a <code>round()</code> function? What about <code>ceil()</code> and <code>floor()</code>? Trig functions?</h3>
<p> Remember that <tt>&quot;int()&quot;</tt> merely truncates toward 0. For rounding to a certain number of digits, <tt>&quot;sprintf()&quot;</tt> or <tt>&quot;printf()&quot;</tt> is usually the easiest route. </p>
<pre>
    printf(&quot;%.3f&quot;, 3.1415926535);   # prints 3.142
</pre>
<p> The <font SIZE="-1">POSIX</font> module (part of the standard Perl distribution) implements <tt>&quot;ceil()&quot;</tt>, <tt>&quot;floor()&quot;</tt>, and a number of other mathematical and trigonometric functions. </p>
<p>use POSIX;<br />
my $ceil = ceil(3.5);<br />
# 4 my $floor = floor(3.5);<br />
# 3</p>
<p> In 5.000 to 5.003 perls, trigonometry was done in the Math::Complex module. With 5.004, the Math::Trig module (part of the standard Perl distribution) implements the trigonometric functions. Internally it uses the Math::Complex module and some functions can break out from the real axis into the complex plane, for example the inverse sine of 2. </p>
<p> Rounding in financial applications can have serious implications, and the rounding method used should be specified precisely. In these cases, it probably pays not to trust whichever system of rounding is being used by Perl, but instead to implement the rounding function you need yourself. </p>
<p> To see why, notice how you&#8217;ll still have an issue on half-way-point alternation: </p>
<p>for (my $i = -5; $i &lt;= 5; $i += 0.5) {<br />
    printf &#8220;%.0f &#8220;, $i<br />
}<br />
&#8211; 5 &#8211; 4 &#8211; 4 &#8211; 4 &#8211; 3 &#8211; 2 &#8211; 2 &#8211; 2 &#8211; 1 &#8211; 0 0 0 1 2 2 2 3 4 4 4 5</p>
<p> Don&#8217;t blame Perl. It&#8217;s the same as in C. <font SIZE="-1">IEEE</font> says we have to do this. Perl numbers whose absolute values are integers under 2**31 (on 32-bit machines) will work pretty much like mathematical integers. Other numbers are not guaranteed.</p>
<h3>How do I convert between numeric representations/bases/radixes?</h3>
<p> As always with Perl there is more than one way to do it. Below are a few examples of approaches to making common conversions between number representations. This is intended to be representational rather than exhaustive. </p>
<p> Some of the examples later in perlfaq4 use the Bit::Vector module from <font SIZE="-1">CPAN.</font> The reason you might choose Bit::Vector over the perl built-in functions is that it works with numbers of <font SIZE="-1">ANY</font> size, that it is optimized for speed on some operations, and for at least some programmers the notation might be familiar.</p>
<dl>
<dt>How do I convert hexadecimal into decimal</p>
<dd> Using perl&#8217;s built in conversion of <tt>&quot;0x&quot;</tt> notation: </p>
<pre>
    my $dec = 0xDEADBEEF;
</pre>
<p> Using the <tt>&quot;hex&quot;</tt> function: </p>
<pre>
    my $dec = hex(&quot;DEADBEEF&quot;);
</pre>
<p> Using <tt>&quot;pack&quot;</tt>: </p>
<pre>
    my $dec = unpack(&quot;N&quot;, pack(&quot;H8&quot;, substr(&quot;0&quot; x 8 . &quot;DEADBEEF&quot;, -8)));
</pre>
<p> Using the <font SIZE="-1">CPAN</font> module <tt>&quot;Bit::Vector&quot;</tt>: </p>
<p>use Bit::Vector;<br />
my $vec = Bit::Vector-&gt;new_Hex(32, &#8220;DEADBEEF&#8221;);<br />
my $dec = $vec-&gt;to_Dec();</p>
<dt>How do I convert from decimal to hexadecimal</p>
<dd> Using <tt>&quot;sprintf&quot;</tt>: </p>
<p>my $hex = sprintf(&#8220;%X&#8221;, 3735928559);<br />
#upper case A &#8211; F<br />
                    my $hex = sprintf(&#8220;%x&#8221;, 3735928559);<br />
#lower case a &#8211; f</p>
<p> Using <tt>&quot;unpack&quot;</tt>: </p>
<pre>
    my $hex = unpack(&quot;H*&quot;, pack(&quot;N&quot;, 3735928559));
</pre>
<p> Using Bit::Vector: </p>
<p>use Bit::Vector;<br />
my $vec = Bit::Vector-&gt;new_Dec(32, -559038737);<br />
my $hex = $vec-&gt;to_Hex();</p>
<p> And Bit::Vector supports odd bit counts: </p>
<p>use Bit::Vector;<br />
my $vec = Bit::Vector-&gt;new_Dec(33, 3735928559);<br />
$vec-&gt;Resize(32);<br />
#suppress leading 0 if unwanted<br />
    my $hex = $vec-&gt;to_Hex();</p>
<dt>How do I convert from octal to decimal</p>
<dd> Using Perl&#8217;s built in conversion of numbers with leading zeros: </p>
<pre>
    my $dec = 033653337357; # note the leading 0!
</pre>
<p> Using the <tt>&quot;oct&quot;</tt> function: </p>
<pre>
    my $dec = oct(&quot;33653337357&quot;);
</pre>
<p> Using Bit::Vector: </p>
<p>use Bit::Vector;<br />
my $vec = Bit::Vector-&gt;new (32);<br />
    $vec-&gt;Chunk_List_Store(3, split(//, reverse &#8220;33653337357&#8221;));<br />
    my $dec = $vec-&gt;to_Dec();</p>
<dt>How do I convert from decimal to octal</p>
<dd> Using <tt>&quot;sprintf&quot;</tt>: </p>
<pre>
    my $oct = sprintf(&quot;%o&quot;, 3735928559);
</pre>
<p> Using Bit::Vector: </p>
<p>use Bit::Vector;<br />
my $vec = Bit::Vector-&gt;new_Dec(32, -559038737);<br />
my $oct = reverse join(&#8221;, $vec-&gt;Chunk_List_Read(3));</p>
<dt>How do I convert from binary to decimal</p>
<dd> Perl 5.6 lets you write binary numbers directly with the <tt>&quot;0b&quot;</tt> notation: </p>
<pre>
    my $number = 0b10110110;
</pre>
<p> Using <tt>&quot;oct&quot;</tt>: </p>
<p>my $input = &#8220;10110110&#8221;;<br />
my $decimal = oct(&#8220;0b$input&#8221;);</p>
<p> Using <tt>&quot;pack&quot;</tt> and <tt>&quot;ord&quot;</tt>: </p>
<pre>
    my $decimal = ord(pack('B8', '10110110'));
</pre>
<p> Using <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> for larger strings: </p>
<p>my $int = unpack(&#8220;N&#8221;, pack(&#8220;B32&#8221;,<br />
                           substr(&#8220;0&#8243; x 32.&#8221;11110101011011011111011101111&#8221;, -32)));<br />
my $dec = sprintf(&#8220;%d&#8221;, $int);<br />
#substr() is used to left &#8211; pad a 32 &#8211; character string with zeros.</p>
<p> Using Bit::Vector: </p>
<p>my $vec = Bit::Vector-&gt;new_Bin(32, &#8220;11011110101011011011111011101111&#8221;);<br />
my $dec = $vec-&gt;to_Dec();</p>
<dt>How do I convert from decimal to binary</p>
<dd> Using <tt>&quot;sprintf&quot;</tt> (perl 5.6+): </p>
<pre>
    my $bin = sprintf(&quot;%b&quot;, 3735928559);
</pre>
<p> Using <tt>&quot;unpack&quot;</tt>: </p>
<pre>
    my $bin = unpack(&quot;B*&quot;, pack(&quot;N&quot;, 3735928559));
</pre>
<p> Using Bit::Vector: </p>
<p>use Bit::Vector;<br />
my $vec = Bit::Vector-&gt;new_Dec(32, -559038737);<br />
my $bin = $vec-&gt;to_Bin();</p>
<p> The remaining transformations (e.g. hex -&gt; oct, bin -&gt; hex, etc.) are left as an exercise to the inclined reader.</dl>
<h3>Why doesn&#8217;t &amp; work the way I want it to?</h3>
<p> The behavior of binary arithmetic operators depends on whether they&#8217;re used on numbers or strings. The operators treat a string as a series of bits and work with that (the string <tt>&quot;3&quot;</tt> is the bit pattern <tt>00110011</tt>). The operators work with the binary form of a number (the number <tt>3</tt> is treated as the bit pattern <tt>00000011</tt>). </p>
<p> So, saying <tt>&quot;11 &amp; 3&quot;</tt> performs the &#8220;and&#8221; operation on numbers (yielding <tt>3</tt>). Saying <tt>&quot;11&quot; &amp; &quot;3&quot;</tt> performs the &#8220;and&#8221; operation on strings (yielding <tt>&quot;1&quot;</tt>). </p>
<p> Most problems with <tt>&quot;&amp;&quot;</tt> and <tt>&quot;|&quot;</tt> arise because the programmer thinks they have a number but really it&#8217;s a string or vice versa. To avoid this, stringify the arguments explicitly (using <tt>&quot;&quot;</tt> or <tt>&quot;qq()&quot;</tt>) or convert them to numbers explicitly (using <tt>&quot;0+$arg&quot;</tt>). The rest arise because the programmer says: </p>
<pre>
    if (&quot;&quot; &amp; &quot;\101\101&quot;) {
        # ...
    }
</pre>
<p> but a string consisting of two null bytes (the result of <tt>&quot;&quot; &amp; &quot;\101\101&quot;</tt>) is not a false value in Perl. You need: </p>
<p>if ((&#8220;&#8221; &amp; &#8220;\101\101&#8221;) !~ / [^
