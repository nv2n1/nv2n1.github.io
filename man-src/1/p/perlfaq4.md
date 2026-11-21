---
title: "perlfaq4(1)"
name: "perlfaq4"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq4/"
description: "perlfaq4 – Data Manipulation"
---
<h2>VERSION</h2>
<p> version 5.20190126  </p>
<h2>DESCRIPTION</h2>
<p> This section of the <font SIZE="-1">FAQ</font> answers questions related to manipulating numbers, dates, strings, arrays, hashes, and miscellaneous data issues.  </p>
<h2>Data: Numbers</h2>
<h3>Why am I getting long decimals (eg, 19.9499999999999) instead of the numbers I should be getting (eg, 19.95)?</h3>
<p> For the long explanation, see David Goldberg&#8217;s ``What Every Computer Scientist Should Know About Floating-Point Arithmetic&#8217;&#8216; (&lt;<a rel="nofollow" href="http://web.cse.msu.edu/~cse320/Documents/FloatingPoint.pdf">http://web.cse.msu.edu/~cse320/Documents/FloatingPoint.pdf</a>&gt;). </p>
<p> Internally, your computer represents floating-point numbers in binary. Digital (as in powers of two) computers cannot store all numbers exactly. Some real numbers lose precision in the process. This is a problem with how computers store numbers and affects all computer languages, not just Perl. </p>
<p> perlnumber shows the gory details of number representations and conversions. </p>
<p> To limit the number of decimal places in your numbers, you can use the <code>&quot;printf&quot;</code> or <code>&quot;sprintf&quot;</code> function. See ``Floating-point Arithmetic&#8217;&#8216; in perlop for more details. </p>
<pre><code>    printf &quot;%.2f&quot;, 10/3;
    my $number = sprintf &quot;%.2f&quot;, 10/3;
</code></pre>
<code></code><h3>Why is int() broken?</h3>
<p> Your <code>&quot;int()&quot;</code> is most probably working just fine. It&#8217;s the numbers that aren&#8217;t quite what you think. </p>
<p> First, see the answer to ``Why am I getting long decimals (eg, 19.9499999999999) instead of the numbers I should be getting (eg, 19.95)?&#8216;&#8216;. </p>
<p> For example, this </p>
<pre><code>    print int(0.6/0.2-2), &quot;\n&quot;;
</code></pre>
<p> will in most computers print 0, not 1, because even such simple numbers as 0.6 and 0.2 cannot be presented exactly by floating-point numbers. What you think in the above as &#8216;three&#8217; is really more like 2.9999999999999995559.  </p>
<h3>Why isn't my octal data interpreted correctly?</h3>
<p> (contributed by brian d foy) </p>
<p> You&#8217;re probably trying to convert a string to a number, which Perl only converts as a decimal number. When Perl converts a string to a number, it ignores leading spaces and zeroes, then assumes the rest of the digits are in base 10: </p>
<pre><code>    my $string = '0644';
    print $string + 0; # prints 644
    print $string + 44; # prints 688, certainly not octal!
</code></pre>
<p> This problem usually involves one of the Perl built-ins that has the same name a Unix command that uses octal numbers as arguments on the command line. In this example, <code>&quot;chmod&quot;</code> on the command line knows that its first argument is octal because that&#8217;s what it does: </p>
<pre><code>    %prompt&gt; chmod 644 file
</code></pre>
<p> If you want to use the same literal digits (644) in Perl, you have to tell Perl to treat them as octal numbers either by prefixing the digits with a <code>0</code> or using <code>&quot;oct&quot;</code>: </p>
<pre><code>    chmod( 0644, $filename ); # right, has leading zero
    chmod( oct(644), $filename ); # also correct
</code></pre>
<p> The problem comes in when you take your numbers from something that Perl thinks is a string, such as a command line argument in <code>@ARGV</code>: </p>
<pre><code>    chmod( $ARGV[0], $filename ); # wrong, even if &quot;0644&quot;
    chmod( oct($ARGV[0]), $filename ); # correct, treat string as octal
</code></pre>
<p> You can always check the value you&#8217;re using by printing it in octal notation to ensure it matches what you think it should be. Print it in octal and decimal format: </p>
<pre><code>    printf &quot;0%o %d&quot;, $number, $number;
</code></pre>
<code></code><code></code><code></code><h3>Does Perl have a round() function? What about ceil() and floor() ? Trig functions?</h3>
<p> Remember that <code>&quot;int()&quot;</code> merely truncates toward 0. For rounding to a certain number of digits, <code>&quot;sprintf()&quot;</code> or <code>&quot;printf()&quot;</code> is usually the easiest route. </p>
<pre><code>    printf(&quot;%.3f&quot;, 3.1415926535); # prints 3.142
</code></pre>
<p> The <font SIZE="-1">POSIX</font> module (part of the standard Perl distribution) implements <code>&quot;ceil()&quot;</code>, <code>&quot;floor()&quot;</code>, and a number of other mathematical and trigonometric functions. </p>
<pre><code>    use POSIX;
    my $ceil = ceil(3.5); # 4
    my $floor = floor(3.5); # 3
</code></pre>
<p> In 5.000 to 5.003 perls, trigonometry was done in the Math::Complex module. With 5.004, the Math::Trig module (part of the standard Perl distribution) implements the trigonometric functions. Internally it uses the Math::Complex module and some functions can break out from the real axis into the complex plane, for example the inverse sine of 2. </p>
<p> Rounding in financial applications can have serious implications, and the rounding method used should be specified precisely. In these cases, it probably pays not to trust whichever system of rounding is being used by Perl, but instead to implement the rounding function you need yourself. </p>
<p> To see why, notice how you&#8217;ll still have an issue on half-way-point alternation: </p>
<pre><code>    for (my $i = -5; $i &lt;= 5; $i += 0.5) { printf &quot;%.0f &quot;,$i }
    -5 -4 -4 -4 -3 -2 -2 -2 -1 -0 0 0 1 2 2 2 3 4 4 4 5
</code></pre>
<p> Don&#8217;t blame Perl. It&#8217;s the same as in C. <font SIZE="-1">IEEE</font> says we have to do this. Perl numbers whose absolute values are integers under 2**31 (on 32-bit machines) will work pretty much like mathematical integers. Other numbers are not guaranteed.  </p>
<h3>How do I convert between numeric representations/bases/radixes?</h3>
<p> As always with Perl there is more than one way to do it. Below are a few examples of approaches to making common conversions between number representations. This is intended to be representational rather than exhaustive. </p>
<p> Some of the examples later in perlfaq4 use the Bit::Vector module from <font SIZE="-1">CPAN.</font> The reason you might choose Bit::Vector over the perl built-in functions is that it works with numbers of <font SIZE="-1">ANY</font> size, that it is optimized for speed on some operations, and for at least some programmers the notation might be familiar. </p>
<dl>
<dt>How do I convert hexadecimal into decimal</dt>
<dd> <p> Using perl&#8217;s built in conversion of <code>&quot;0x&quot;</code> notation: </p>
<pre><code>    my $dec = 0xDEADBEEF;
</code></pre>
<p> Using the <code>&quot;hex&quot;</code> function: </p>
<pre><code>    my $dec = hex(&quot;DEADBEEF&quot;);
</code></pre>
<p> Using <code>&quot;pack&quot;</code>: </p>
<pre><code>    my $dec = unpack(&quot;N&quot;, pack(&quot;H8&quot;, substr(&quot;0&quot; x 8 . &quot;DEADBEEF&quot;, -8)));
</code></pre>
<p> Using the <font SIZE="-1">CPAN</font> module <code>&quot;Bit::Vector&quot;</code>: </p>
<pre><code>    use Bit::Vector;
    my $vec = Bit::Vector-&gt;new_Hex(32, &quot;DEADBEEF&quot;);
    my $dec = $vec-&gt;to_Dec();
</code></pre>
 </dd>
<dt>How do I convert from decimal to hexadecimal</dt>
<dd> <p> Using <code>&quot;sprintf&quot;</code>: </p>
<pre><code>    my $hex = sprintf(&quot;%X&quot;, 3735928559); # upper case A-F
    my $hex = sprintf(&quot;%x&quot;, 3735928559); # lower case a-f
</code></pre>
<p> Using <code>&quot;unpack&quot;</code>: </p>
<pre><code>    my $hex = unpack(&quot;H*&quot;, pack(&quot;N&quot;, 3735928559));
</code></pre>
<p> Using Bit::Vector: </p>
<pre><code>    use Bit::Vector;
    my $vec = Bit::Vector-&gt;new_Dec(32, -559038737);
    my $hex = $vec-&gt;to_Hex();
</code></pre>
<p> And Bit::Vector supports odd bit counts: </p>
<pre><code>    use Bit::Vector;
    my $vec = Bit::Vector-&gt;new_Dec(33, 3735928559);
    $vec-&gt;Resize(32); # suppress leading 0 if unwanted
    my $hex = $vec-&gt;to_Hex();
</code></pre>
 </dd>
<dt>How do I convert from octal to decimal</dt>
<dd> <p> Using Perl&#8217;s built in conversion of numbers with leading zeros: </p>
<pre><code>    my $dec = 033653337357; # note the leading 0!
</code></pre>
<p> Using the <code>&quot;oct&quot;</code> function: </p>
<pre><code>    my $dec = oct(&quot;33653337357&quot;);
</code></pre>
<p> Using Bit::Vector: </p>
<pre><code>    use Bit::Vector;
    my $vec = Bit::Vector-&gt;new(32);
    $vec-&gt;Chunk_List_Store(3, split(//, reverse &quot;33653337357&quot;));
    my $dec = $vec-&gt;to_Dec();
</code></pre>
 </dd>
<dt>How do I convert from decimal to octal</dt>
<dd> <p> Using <code>&quot;sprintf&quot;</code>: </p>
<pre><code>    my $oct = sprintf(&quot;%o&quot;, 3735928559);
</code></pre>
<p> Using Bit::Vector: </p>
<pre><code>    use Bit::Vector;
    my $vec = Bit::Vector-&gt;new_Dec(32, -559038737);
    my $oct = reverse join('', $vec-&gt;Chunk_List_Read(3));
</code></pre>
 </dd>
<dt>How do I convert from binary to decimal</dt>
<dd> <p> Perl 5.6 lets you write binary numbers directly with the <code>&quot;0b&quot;</code> notation: </p>
<pre><code>    my $number = 0b10110110;
</code></pre>
<p> Using <code>&quot;oct&quot;</code>: </p>
<pre><code>    my $input = &quot;10110110&quot;;
    my $decimal = oct( &quot;0b$input&quot; );
</code></pre>
<p> Using <code>&quot;pack&quot;</code> and <code>&quot;ord&quot;</code>: </p>
<pre><code>    my $decimal = ord(pack('B8', '10110110'));
</code></pre>
<p> Using <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> for larger strings: </p>
<pre><code>    my $int = unpack(&quot;N&quot;, pack(&quot;B32&quot;,
    substr(&quot;0&quot; x 32 . &quot;11110101011011011111011101111&quot;, -32)));
    my $dec = sprintf(&quot;%d&quot;, $int);
    # substr() is used to left-pad a 32-character string with zeros.
</code></pre>
<p> Using Bit::Vector: </p>
<pre><code>    my $vec = Bit::Vector-&gt;new_Bin(32, &quot;11011110101011011011111011101111&quot;);
    my $dec = $vec-&gt;to_Dec();
</code></pre>
 </dd>
<dt>How do I convert from decimal to binary</dt>
<dd> <p> Using <code>&quot;sprintf&quot;</code> (perl 5.6+): </p>
<pre><code>    my $bin = sprintf(&quot;%b&quot;, 3735928559);
</code></pre>
<p> Using <code>&quot;unpack&quot;</code>: </p>
<pre><code>    my $bin = unpack(&quot;B*&quot;, pack(&quot;N&quot;, 3735928559));
</code></pre>
<p> Using Bit::Vector: </p>
<pre><code>    use Bit::Vector;
    my $vec = Bit::Vector-&gt;new_Dec(32, -559038737);
    my $bin = $vec-&gt;to_Bin();
</code></pre>
<p> The remaining transformations (e.g. hex -&gt; oct, bin -&gt; hex, etc.) are left as an exercise to the inclined reader. </p>
 </dd></dl>
<h3>Why doesn't &amp; work the way I want it to?</h3>
<p> The behavior of binary arithmetic operators depends on whether they&#8217;re used on numbers or strings. The operators treat a string as a series of bits and work with that (the string <code>&quot;3&quot;</code> is the bit pattern <code>00110011</code>). The operators work with the binary form of a number (the number <code>3</code> is treated as the bit pattern <code>00000011</code>). </p>
<p> So, saying <code>&quot;11 &amp; 3&quot;</code> performs the ``and&#8217;&#8216; operation on numbers (yielding <code>3</code>). Saying <code>&quot;11&quot; &amp; &quot;3&quot;</code> performs the ``and&#8217;&#8216; operation on strings (yielding <code>&quot;1&quot;</code>). </p>
<p> Most problems with <code>&quot;&amp;&quot;</code> and <code>&quot;|&quot;</code> arise because the programmer thinks they have a number but really it&#8217;s a string or vice versa. To avoid this, stringify the arguments explicitly (using <code>&quot;&quot;</code> or <code>&quot;qq()&quot;</code>) or convert them to numbers explicitly (using <code>&quot;0+$arg&quot;</code>). The rest arise because the programmer says: </p>
<pre><code>    if (&quot;\020\020&quot; &amp; &quot;\101\101&quot;) {
        # ...
    }
</code></pre>
<p> but a string consisting of two null bytes (the result of <code>&quot;\020\020&quot; &amp; &quot;\101\101&quot;</code>) is not a false value in Perl. You need: </p>
<pre><code>    if ( (&quot;\020\020&quot; &amp; &quot;\101\101&quot;) !~ /[^\000]/) {
        # ...
    }
</code></pre>
<h3>How do I multiply matrices?</h3>
<p> Use the Math::Matrix or Math::MatrixReal modules (available from <font SIZE="-1">CPAN</font>) or the <font SIZE="-1">PDL</font> extension (also available from <font SIZE="-1">CPAN</font>).  </p>
<h3>How do I perform an operation on a series of integers?</h3>
<p> To call a function on each element in an array, and collect the results, use: </p>
<pre><code>    my @results = map { my_func($_) } @array;
</code></pre>
<p> For example: </p>
<pre><code>    my @triple = map { 3 * $_ } @single;
</code></pre>
<p> To call a function on each element of an array, but ignore the results: </p>
<pre><code>    foreach my $iterator (@array) {
        some_func($iterator);
    }
</code></pre>
<p> To call a function on each integer in a (small) range, you <code>can</code> use: </p>
<pre><code>    my @results = map { some_func($_) } (5 .. 25);
</code></pre>
<p> but you should be aware that in this form, the <code>&quot;..&quot;</code> operator creates a list of all integers in the range, which can take a lot of memory for large ranges. However, the problem does not occur when using <code>&quot;..&quot;</code> within a <code>&quot;for&quot;</code> loop, because in that case the range operator is optimized to <i>iterate</i> over the range, without creating the entire list. So </p>
<pre><code>    my @results = ();
    for my $i (5 .. 500_005) {
        push(@results, some_func($i));
    }
</code></pre>
<p> or even </p>
<pre><code>   push(@results, some_func($_)) for 5 .. 500_005;
</code></pre>
<p> will not create an intermediate list of 500,000 integers.  </p>
<h3>How can I output Roman numerals?</h3>
<p> Get the &lt;<a rel="nofollow" href="http://www.cpan.org/modules/by-module/Roman">http://www.cpan.org/modules/by-module/Roman</a>&gt; module.  </p>
<h3>Why aren't my random numbers random?</h3>
<p> If you&#8217;re using a version of Perl before 5.004, you must call <code>&quot;srand&quot;</code> once at the start of your program to seed the random number generator. </p>
<pre><code>     BEGIN { srand() if $] &lt; 5.004 }
</code></pre>
<p> 5.004 and later automatically call <code>&quot;srand&quot;</code> at the beginning. Don&#8217;t call <code>&quot;srand&quot;</code> more than once---you make your numbers less random, rather than more. </p>
<p> Computers are good at being predictable and bad at being random (despite appearances caused by bugs in your programs :-). The <i>random</i> article in the ``Far More Than You Ever Wanted To Know&#8217;&#8216; collection in &lt;<a rel="nofollow" href="http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz">http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz</a>&gt;, courtesy of Tom Phoenix, talks more about this. John von Neumann said, ``Anyone who attempts to generate random numbers by deterministic means is, of course, living in a state of sin.&#8216;&#8216; </p>
<p> Perl relies on the underlying system for the implementation of <code>&quot;rand&quot;</code> and <code>&quot;srand&quot;</code>; on some systems, the generated numbers are not random enough (especially on Windows : see &lt;<a rel="nofollow" href="http://www.perlmonks.org/?node_id=803632">http://www.perlmonks.org/?node_id=803632</a>&gt;). Several <font SIZE="-1">CPAN</font> modules in the <code>&quot;Math&quot;</code> namespace implement better pseudorandom generators; see for example Math::Random::MT (``Mersenne Twister&#8217;&#8216;, fast), or Math::TrulyRandom (uses the imperfections in the system&#8217;s timer to generate random numbers, which is rather slow). More algorithms for random numbers are described in ``Numerical Recipes in C&#8217;&#8216; at &lt;<a rel="nofollow" href="http://www.nr.com/">http://www.nr.com/</a>&gt;  </p>
<h3>How do I get a random number between X and Y?</h3>
<p> To get a random number between two values, you can use the <code>&quot;rand()&quot;</code> built-in to get a random number between 0 and 1. From there, you shift that into the range that you want. </p>
<p> <code>&quot;rand($x)&quot;</code> returns a number such that <code>&quot;0 &lt;= rand($x) &lt; $x&quot;</code>. Thus what you want to have perl figure out is a random number in the range from 0 to the difference between your <i>X</i> and <i>Y</i>. </p>
<p> That is, to get a number between 10 and 15, inclusive, you want a random number between 0 and 5 that you can then add to 10. </p>
<pre><code>    my $number = 10 + int rand( 15-10+1 ); # ( 10,11,12,13,14, or 15 )
</code></pre>
<p> Hence you derive the following simple function to abstract that. It selects a random integer between the two given integers (inclusive). For example: <code>&quot;random_int_between(50,120)&quot;</code>. </p>
<pre><code>    sub random_int_between {
        my($min, $max) = @_;
        # Assumes that the two arguments are integers themselves!
        return $min if $min == $max;
        ($min, $max) = ($max, $min) if $min &gt; $max;
        return $min + int rand(1 + $max - $min);
    }
</code></pre>
<h2>Data: Dates</h2>
<h3>How do I find the day or week of the year?</h3>
<p> The day of the year is in the list returned by the <code>&quot;localtime&quot;</code> function. Without an argument <code>&quot;localtime&quot;</code> uses the current time. </p>
<pre><code>    my $day_of_year = (localtime)[7];
</code></pre>
<p> The <font SIZE="-1">POSIX</font> module can also format a date as the day of the year or week of the year. </p>
<pre><code>    use POSIX qw/strftime/;
    my $day_of_year = strftime &quot;%j&quot;, localtime;
    my $week_of_year = strftime &quot;%W&quot;, localtime;
</code></pre>
<p> To get the day of year for any date, use <font SIZE="-1">POSIX</font>&#8216;s <code>&quot;mktime&quot;</code> to get a time in epoch seconds for the argument to <code>&quot;localtime&quot;</code>. </p>
<pre><code>    use POSIX qw/mktime strftime/;
    my $week_of_year = strftime &quot;%W&quot;,
        localtime( mktime( 0, 0, 0, 18, 11, 87 ) );
</code></pre>
<p> You can also use Time::Piece, which comes with Perl and provides a <code>&quot;localtime&quot;</code> that returns an object: </p>
<pre><code>    use Time::Piece;
    my $day_of_year = localtime-&gt;yday;
    my $week_of_year = localtime-&gt;week;
</code></pre>
<p> The Date::Calc module provides two functions to calculate these, too: </p>
<pre><code>    use Date::Calc;
    my $day_of_year = Day_of_Year( 1987, 12, 18 );
    my $week_of_year = Week_of_Year( 1987, 12, 18 );
</code></pre>
<h3>How do I find the current century or millennium?</h3>
<p> Use the following simple functions: </p>
<pre><code>    sub get_century {
        return int((((localtime(shift || time))[5] + 1999))/100);
    }
    sub get_millennium {
        return 1+int((((localtime(shift || time))[5] + 1899))/1000);
    }
</code></pre>
<p> On some systems, the <font SIZE="-1">POSIX</font> module&#8217;s <code>&quot;strftime()&quot;</code> function has been extended in a non-standard way to use a <code>%C</code> format, which they sometimes claim is the ``century&#8217;&#8216;. It isn&#8217;t, because on most such systems, this is only the first two digits of the four-digit year, and thus cannot be used to determine reliably the current century or millennium.  </p>
<h3>How can I compare two dates and find the difference?</h3>
<p> (contributed by brian d foy) </p>
<p> You could just store all your dates as a number and then subtract. Life isn&#8217;t always that simple though. </p>
<p> The Time::Piece module, which comes with Perl, replaces localtime with a version that returns an object. It also overloads the comparison operators so you can compare them directly: </p>
<pre><code>    use Time::Piece;
    my $date1 = localtime( $some_time );
    my $date2 = localtime( $some_other_time );
    if( $date1 &lt; $date2 ) {
        print &quot;The date was in the past\n&quot;;
    }
</code></pre>
<p> You can also get differences with a subtraction, which returns a Time::Seconds object: </p>
<pre><code>    my $date_diff = $date1 - $date2;
    print &quot;The difference is &quot;, $date_diff-&gt;days, &quot; days\n&quot;;
</code></pre>
<p> If you want to work with formatted dates, the Date::Manip, Date::Calc, or DateTime modules can help you.  </p>
<h3>How can I take a string and turn it into epoch seconds?</h3>
<p> If it&#8217;s a regular enough string that it always has the same format, you can split it up and pass the parts to <code>&quot;timelocal&quot;</code> in the standard Time::Local module. Otherwise, you should look into the Date::Calc, Date::Parse, and Date::Manip modules from <font SIZE="-1">CPAN.</font>  </p>
<h3>How can I find the Julian Day?</h3>
<p> (contributed by brian d foy and Dave Cross) </p>
<p> You can use the Time::Piece module, part of the Standard Library, which can convert a date/time to a Julian Day: </p>
<pre><code>    $ perl -MTime::Piece -le 'print localtime-&gt;julian_day'
    2455607.7959375
</code></pre>
<p> Or the modified Julian Day: </p>
<pre><code>    $ perl -MTime::Piece -le 'print localtime-&gt;mjd'
    55607.2961226851
</code></pre>
<p> Or even the day of the year (which is what some people think of as a Julian day): </p>
<pre><code>    $ perl -MTime::Piece -le 'print localtime-&gt;yday'
    45
</code></pre>
<p> You can also do the same things with the DateTime module: </p>
<pre><code>    $ perl -MDateTime -le'print DateTime-&gt;today-&gt;jd'
    2453401.5
    $ perl -MDateTime -le'print DateTime-&gt;today-&gt;mjd'
    53401
    $ perl -MDateTime -le'print DateTime-&gt;today-&gt;doy'
    31
</code></pre>
<p> You can use the Time::JulianDay module available on <font SIZE="-1">CPAN.</font> Ensure that you really want to find a Julian day, though, as many people have different ideas about Julian days (see &lt;<a rel="nofollow" href="http://www.hermetic.ch/cal_stud/jdn.htm">http://www.hermetic.ch/cal_stud/jdn.htm</a>&gt; for instance): </p>
<pre><code>    $ perl -MTime::JulianDay -le 'print local_julian_day( time )'
    55608
</code></pre>
<h3>How do I find yesterday's date?</h3>
<p> (contributed by brian d foy) </p>
<p> To do it correctly, you can use one of the <code>&quot;Date&quot;</code> modules since they work with calendars instead of times. The DateTime module makes it simple, and give you the same time of day, only the day before, despite daylight saving time changes: </p>
<pre><code>    use DateTime;
    my $yesterday = DateTime-&gt;now-&gt;subtract( days =&gt; 1 );
    print &quot;Yesterday was $yesterday\n&quot;;
</code></pre>
<p> You can also use the Date::Calc module using its <code>&quot;Today_and_Now&quot;</code> function. </p>
<pre><code>    use Date::Calc qw( Today_and_Now Add_Delta_DHMS );
    my @date_time = Add_Delta_DHMS( Today_and_Now(), -1, 0, 0, 0 );
    print &quot;@date_time\n&quot;;
</code></pre>
<p> Most people try to use the time rather than the calendar to figure out dates, but that assumes that days are twenty-four hours each. For most people, there are two days a year when they aren&#8217;t: the switch to and from summer time throws this off. For example, the rest of the suggestions will be wrong sometimes: </p>
<p> Starting with Perl 5.10, Time::Piece and Time::Seconds are part of the standard distribution, so you might think that you could do something like this: </p>
<pre><code>    use Time::Piece;
    use Time::Seconds;
    my $yesterday = localtime() - ONE_DAY; # WRONG
    print &quot;Yesterday was $yesterday\n&quot;;
</code></pre>
<p> The Time::Piece module exports a new <code>&quot;localtime&quot;</code> that returns an object, and Time::Seconds exports the <code>&quot;ONE_DAY&quot;</code> constant that is a set number of seconds. This means that it always gives the time 24 hours ago, which is not always yesterday. This can cause problems around the end of daylight saving time when there&#8217;s one day that is 25 hours long. </p>
<p> You have the same problem with Time::Local, which will give the wrong answer for those same special cases: </p>
<pre><code>    # contributed by Gunnar Hjalmarsson
     use Time::Local;
     my $today = timelocal 0, 0, 12, ( localtime )[3..5];
     my ($d, $m, $y) = ( localtime $today-86400 )[3..5]; # WRONG
     printf &quot;Yesterday: %d-%02d-%02d\n&quot;, $y+1900, $m+1, $d;
</code></pre>
<h3>Does Perl have a Year 2000 or 2038 problem? Is Perl Y2K compliant?</h3>
<p> (contributed by brian d foy) </p>
<p> Perl itself never had a Y2K problem, although that never stopped people from creating Y2K problems on their own. See the documentation for <code>&quot;localtime&quot;</code> for its proper use. </p>
<p> Starting with Perl 5.12, <code>&quot;localtime&quot;</code> and <code>&quot;gmtime&quot;</code> can handle dates past 03:14:08 January 19, 2038, when a 32-bit based time would overflow. You still might get a warning on a 32-bit <code>&quot;perl&quot;</code>: </p>
<pre><code>    % perl5.12 -E 'say scalar localtime( 0x9FFF_FFFFFFFF )'
    Integer overflow in hexadecimal number at -e line 1.
    Wed Nov 1 19:42:39 5576711
</code></pre>
<p> On a 64-bit <code>&quot;perl&quot;</code>, you can get even larger dates for those really long running projects: </p>
<pre><code>    % perl5.12 -E 'say scalar gmtime( 0x9FFF_FFFFFFFF )'
    Thu Nov 2 00:42:39 5576711
</code></pre>
<p> You&#8217;re still out of luck if you need to keep track of decaying protons though.  </p>
<h2>Data: Strings</h2>
<h3>How do I validate input?</h3>
<p> (contributed by brian d foy) </p>
<p> There are many ways to ensure that values are what you expect or want to accept. Besides the specific examples that we cover in the perlfaq, you can also look at the modules with ``Assert&#8217;&#8216; and ``Validate&#8217;&#8216; in their names, along with other modules such as Regexp::Common. </p>
<p> Some modules have validation for particular types of input, such as Business::ISBN, Business::CreditCard, Email::Valid, and Data::Validate::IP.  </p>
<h3>How do I unescape a string?</h3>
<p> It depends just what you mean by ``escape&#8217;&#8216;. <font SIZE="-1">URL</font> escapes are dealt with in perlfaq9. Shell escapes with the backslash (<code>&quot;\&quot;</code>) character are removed with </p>
<pre><code>    s/\\(.)/$1/g;
</code></pre>
<p> This won&#8217;t expand <code>&quot;\n&quot;</code> or <code>&quot;\t&quot;</code> or any other special escapes.  </p>
<h3>How do I remove consecutive pairs of characters?</h3>
<p> (contributed by brian d foy) </p>
<p> You can use the substitution operator to find pairs of characters (or runs of characters) and replace them with a single instance. In this substitution, we find a character in <code>&quot;(.)&quot;</code>. The memory parentheses store the matched character in the back-reference <code>&quot;\g1&quot;</code> and we use that to require that the same thing immediately follow it. We replace that part of the string with the character in <code>$1</code>. </p>
<pre><code>    s/(.)\g1/$1/g;
</code></pre>
<p> We can also use the transliteration operator, <code>&quot;tr///&quot;</code>. In this example, the search list side of our <code>&quot;tr///&quot;</code> contains nothing, but the <code>&quot;c&quot;</code> option complements that so it contains everything. The replacement list also contains nothing, so the transliteration is almost a no-op since it won&#8217;t do any replacements (or more exactly, replace the character with itself). However, the <code>&quot;s&quot;</code> option squashes duplicated and consecutive characters in the string so a character does not show up next to itself </p>
<pre><code>    my $str = 'Haarlem'; # in the Netherlands
    $str =~ tr///cs; # Now Harlem, like in New York
</code></pre>
<h3>How do I expand function calls in a string?</h3>
<p> (contributed by brian d foy) </p>
<p> This is documented in perlref, and although it&#8217;s not the easiest thing to read, it does work. In each of these examples, we call the function inside the braces used to dereference a reference. If we have more than one return value, we can construct and dereference an anonymous array. In this case, we call the function in list context. </p>
<pre><code>    print &quot;The time values are @{ [localtime] }.\n&quot;;
</code></pre>
<p> If we want to call the function in scalar context, we have to do a bit more work. We can really have any code we like inside the braces, so we simply have to end with the scalar reference, although how you do that is up to you, and you can use code inside the braces. Note that the use of parens creates a list context, so we need <code>&quot;scalar&quot;</code> to force the scalar context on the function: </p>
<pre><code>    print &quot;The time is ${\(scalar localtime)}.\n&quot;
    print &quot;The time is ${ my $x = localtime; \$x }.\n&quot;;
</code></pre>
<p> If your function already returns a reference, you don&#8217;t need to create the reference yourself. </p>
<pre><code>    sub timestamp { my $t = localtime; \$t }
    print &quot;The time is ${ timestamp() }.\n&quot;;
</code></pre>
<p> The <code>&quot;Interpolation&quot;</code> module can also do a lot of magic for you. You can specify a variable name, in this case <code>&quot;E&quot;</code>, to set up a tied hash that does the interpolation for you. It has several other methods to do this as well. </p>
<pre><code>    use Interpolation E =&gt; 'eval';
    print &quot;The time values are $E{localtime()}.\n&quot;;
</code></pre>
<p> In most cases, it is probably easier to simply use string concatenation, which also forces scalar context. </p>
<pre><code>    print &quot;The time is &quot; . localtime() . &quot;.\n&quot;;
</code></pre>
<h3>How do I find matching/nesting anything?</h3>
<p> To find something between two single characters, a pattern like <code>&quot;/x([^x]*)x/&quot;</code> will get the intervening bits in <code>$1</code>. For multiple ones, then something more like <code>&quot;/alpha(.*?)omega/&quot;</code> would be needed. For nested patterns and/or balanced expressions, see the so-called (?PARNO) construct (available since perl 5.10). The <font SIZE="-1">CPAN</font> module Regexp::Common can help to build such regular expressions (see in particular Regexp::Common::balanced and Regexp::Common::delimited). </p>
<p> More complex cases will require to write a parser, probably using a parsing module from <font SIZE="-1">CPAN,</font> like Regexp::Grammars, Parse::RecDescent, Parse::Yapp, Text::Balanced, or Marpa::R2.  </p>
<h3>How do I reverse a string?</h3>
<p> Use <code>&quot;reverse()&quot;</code> in scalar context, as documented in ``reverse&#8217;&#8216; in perlfunc. </p>
<pre><code>    my $reversed = reverse $string;
</code></pre>
<h3>How do I expand tabs in a string?</h3>
<p> You can do it yourself: </p>
<pre><code>    1 while $string =~ s/\t+/' ' x (length($&amp;) * 8 - length($`) % 8)/e;
</code></pre>
<p> Or you can just use the Text::Tabs module (part of the standard Perl distribution). </p>
<pre><code>    use Text::Tabs;
    my @expanded_lines = expand(@lines_with_tabs);
</code></pre>
<h3>How do I reformat a paragraph?</h3>
<p> Use Text::Wrap (part of the standard Perl distribution): </p>
<pre><code>    use Text::Wrap;
    print wrap(&quot;\t&quot;, ' ', @paragraphs);
</code></pre>
<p> The paragraphs you give to Text::Wrap should not contain embedded newlines. Text::Wrap doesn&#8217;t justify the lines (flush-right). </p>
<p> Or use the <font SIZE="-1">CPAN</font> module Text::Autoformat. Formatting files can be easily done by making a shell alias, like so: </p>
<pre><code>    alias fmt=&quot;perl -i -MText::Autoformat -n0777 \
        -e 'print autoformat $_, {all=&gt;1}' $*&quot;
</code></pre>
<p> See the documentation for Text::Autoformat to appreciate its many capabilities.  </p>
<h3>How can I access or change N characters of a string?</h3>
<p> You can access the first characters of a string with <code>substr()</code>. To get the first character, for example, start at position 0 and grab the string of length 1. </p>
<pre><code>    my $string = &quot;Just another Perl Hacker&quot;;
    my $first_char = substr( $string, 0, 1 ); # 'J'
</code></pre>
<p> To change part of a string, you can use the optional fourth argument which is the replacement string. </p>
<pre><code>    substr( $string, 13, 4, &quot;Perl 5.8.0&quot; );
</code></pre>
<p> You can also use <code>substr()</code> as an lvalue. </p>
<pre><code>    substr( $string, 13, 4 ) = &quot;Perl 5.8.0&quot;;
</code></pre>
<h3>How do I change the Nth occurrence of something?</h3>
<p> You have to keep track of N yourself. For example, let&#8217;s say you want to change the fifth occurrence of <code>&quot;whoever&quot;</code> or <code>&quot;whomever&quot;</code> into <code>&quot;whosoever&quot;</code> or <code>&quot;whomsoever&quot;</code>, case insensitively. These all assume that <code>$_</code> contains the string to be altered. </p>
<pre><code>    $count = 0;
    s{((whom?)ever)}{
    ++$count == 5 # is it the 5th?
        ? &quot;${2}soever&quot; # yes, swap
        : $1 # renege and leave it there
        }ige;
</code></pre>
<p> In the more general case, you can use the <code>&quot;/g&quot;</code> modifier in a <code>&quot;while&quot;</code> loop, keeping count of matches. </p>
<pre><code>    $WANT = 3;
    $count = 0;
    $_ = &quot;One fish two fish red fish blue fish&quot;;
    while (/(\w+)\s+fish\b/gi) {
        if (++$count == $WANT) {
            print &quot;The third fish is a $1 one.\n&quot;;
        }
    }
</code></pre>
<p> That prints out: <code>&quot;The third fish is a red one.&quot;</code> You can also use a repetition count and repeated pattern like this: </p>
<pre><code>    /(?:\w+\s+fish\s+){2}(\w+)\s+fish/i;
</code></pre>
<h3>How can I count the number of occurrences of a substring within a string?</h3>
<p> There are a number of ways, with varying efficiency. If you want a count of a certain single character (X) within a string, you can use the <code>&quot;tr///&quot;</code> function like so: </p>
<pre><code>    my $string = &quot;ThisXlineXhasXsomeXx'sXinXit&quot;;
    my $count = ($string =~ tr/X//);
    print &quot;There are $count X characters in the string&quot;;
</code></pre>
<p> This is fine if you are just looking for a single character. However, if you are trying to count multiple character substrings within a larger string, <code>&quot;tr///&quot;</code> won&#8217;t work. What you can do is wrap a <code>while()</code> loop around a global pattern match. For example, let&#8217;s count negative integers: </p>
<pre><code>    my $string = &quot;-9 55 48 -2 23 -76 4 14 -44&quot;;
    my $count = 0;
    while ($string =~ /-\d+/g) { $count++ }
    print &quot;There are $count negative numbers in the string&quot;;
</code></pre>
<p> Another version uses a global match in list context, then assigns the result to a scalar, producing a count of the number of matches. </p>
<pre><code>    my $count = () = $string =~ /-\d+/g;
</code></pre>
<h3>How do I capitalize all the words on one line?</h3>
<p> (contributed by brian d foy) </p>
<p> Damian Conway&#8217;s Text::Autoformat handles all of the thinking for you. </p>
<pre><code>    use Text::Autoformat;
    my $x = &quot;Dr. Strangelove or: How I Learned to Stop &quot;.
      &quot;Worrying and Love the Bomb&quot;;
    print $x, &quot;\n&quot;;
    for my $style (qw( sentence title highlight )) {
        print autoformat($x, { case =&gt; $style }), &quot;\n&quot;;
    }
</code></pre>
<p> How do you want to capitalize those words? </p>
<pre><code>    FRED AND BARNEY'S LODGE # all uppercase
    Fred And Barney's Lodge # title case
    Fred and Barney's Lodge # highlight case
</code></pre>
<p> It&#8217;s not as easy a problem as it looks. How many words do you think are in there? Wait for it... wait for it.... If you answered 5 you&#8217;re right. Perl words are groups of <code>&quot;\w+&quot;</code>, but that&#8217;s not what you want to capitalize. How is Perl supposed to know not to capitalize that <code>&quot;s&quot;</code> after the apostrophe? You could try a regular expression: </p>
<pre><code>    $string =~ s/ (
                 (^\w) #at the beginning of the line
                   | # or
                 (\s\w) #preceded by whitespace
                   )
                /\U$1/xg;
    $string =~ s/([\w']+)/\u\L$1/g;
</code></pre>
<p> Now, what if you don&#8217;t want to capitalize that ``and&#8217;&#8216;? Just use Text::Autoformat and get on with the next problem. :)  </p>
<h3>How can I split a [character]-delimited string except when inside [character]?</h3>
<p> Several modules can handle this sort of parsing---Text::Balanced, Text::CSV, Text::CSV_XS, and Text::ParseWords, among others. </p>
<p> Take the example case of trying to split a string that is comma-separated into its different fields. You can&#8217;t use <code>&quot;split(/,/)&quot;</code> because you shouldn&#8217;t split if the comma is inside quotes. For example, take a data line like this: </p>
<pre><code>    SAR001,&quot;&quot;,&quot;Cimetrix, Inc&quot;,&quot;Bob Smith&quot;,&quot;CAM&quot;,N,8,1,0,7,&quot;Error, Core Dumped&quot;
</code></pre>
<p> Due to the restriction of the quotes, this is a fairly complex problem. Thankfully, we have Jeffrey Friedl, author of <i>Mastering Regular Expressions</i>, to handle these for us. He suggests (assuming your string is contained in <code>$text</code>): </p>
<pre><code>     my @new = ();
     push(@new, $+) while $text =~ m{
         &quot;([^\&quot;\\]*(?:\\.[^\&quot;\\]*)*)&quot;,? # groups the phrase inside the quotes
        | ([^,]+),?
        | ,
     }gx;
     push(@new, undef) if substr($text,-1,1) eq ',';
</code></pre>
<p> If you want to represent quotation marks inside a quotation-mark-delimited field, escape them with backslashes (eg, <code>&quot;like \&quot;this\&quot;&quot;</code>. </p>
<p> Alternatively, the Text::ParseWords module (part of the standard Perl distribution) lets you say: </p>
<pre><code>    use Text::ParseWords;
    @new = quotewords(&quot;,&quot;, 0, $text);
</code></pre>
<p> For parsing or generating <font SIZE="-1">CSV,</font> though, using Text::CSV rather than implementing it yourself is highly recommended; you&#8217;ll save yourself odd bugs popping up later by just using code which has already been tried and tested in production for years.  </p>
<h3>How do I strip blank space from the beginning/end of a string?</h3>
<p> (contributed by brian d foy) </p>
<p> A substitution can do this for you. For a single line, you want to replace all the leading or trailing whitespace with nothing. You can do that with a pair of substitutions: </p>
<pre><code>    s/^\s+//;
    s/\s+$//;
</code></pre>
<p> You can also write that as a single substitution, although it turns out the combined statement is slower than the separate ones. That might not matter to you, though: </p>
<pre><code>    s/^\s+|\s+$//g;
</code></pre>
<p> In this regular expression, the alternation matches either at the beginning or the end of the string since the anchors have a lower precedence than the alternation. With the <code>&quot;/g&quot;</code> flag, the substitution makes all possible matches, so it gets both. Remember, the trailing newline matches the <code>&quot;\s+&quot;</code>, and the <code>&quot;$&quot;</code> anchor can match to the absolute end of the string, so the newline disappears too. Just add the newline to the output, which has the added benefit of preserving ``blank&#8217;&#8216; (consisting entirely of whitespace) lines which the <code>&quot;^\s+&quot;</code> would remove all by itself: </p>
<pre><code>    while( &lt;&gt; ) {
        s/^\s+|\s+$//g;
        print &quot;$_\n&quot;;
    }
</code></pre>
<p> For a multi-line string, you can apply the regular expression to each logical line in the string by adding the <code>&quot;/m&quot;</code> flag (for ``multi-line&#8217;&#8216;). With the <code>&quot;/m&quot;</code> flag, the <code>&quot;$&quot;</code> matches <i>before</i> an embedded newline, so it doesn&#8217;t remove it. This pattern still removes the newline at the end of the string: </p>
<pre><code>    $string =~ s/^\s+|\s+$//gm;
</code></pre>
<p> Remember that lines consisting entirely of whitespace will disappear, since the first part of the alternation can match the entire string and replace it with nothing. If you need to keep embedded blank lines, you have to do a little more work. Instead of matching any whitespace (since that includes a newline), just match the other whitespace: </p>
<pre><code>    $string =~ s/^[\t\f ]+|[\t\f ]+$//mg;
</code></pre>
<h3>How do I pad a string with blanks or pad a number with zeroes?</h3>
<p> In the following examples, <code>$pad_len</code> is the length to which you wish to pad the string, <code>$text</code> or <code>$num</code> contains the string to be padded, and <code>$pad_char</code> contains the padding character. You can use a single character string constant instead of the <code>$pad_char</code> variable if you know what it is in advance. And in the same way you can use an integer in place of <code>$pad_len</code> if you know the pad length in advance. </p>
<p> The simplest method uses the <code>&quot;sprintf&quot;</code> function. It can pad on the left or right with blanks and on the left with zeroes and it will not truncate the result. The <code>&quot;pack&quot;</code> function can only pad strings on the right with blanks and it will truncate the result to a maximum length of <code>$pad_len</code>. </p>
<pre><code>    # Left padding a string with blanks (no truncation):
    my $padded = sprintf(&quot;%${pad_len}s&quot;, $text);
    my $padded = sprintf(&quot;%*s&quot;, $pad_len, $text); # same thing
    # Right padding a string with blanks (no truncation):
    my $padded = sprintf(&quot;%-${pad_len}s&quot;, $text);
    my $padded = sprintf(&quot;%-*s&quot;, $pad_len, $text); # same thing
    # Left padding a number with 0 (no truncation):
    my $padded = sprintf(&quot;%0${pad_len}d&quot;, $num);
    my $padded = sprintf(&quot;%0*d&quot;, $pad_len, $num); # same thing
    # Right padding a string with blanks using pack (will truncate):
    my $padded = pack(&quot;A$pad_len&quot;,$text);
</code></pre>
<p> If you need to pad with a character other than blank or zero you can use one of the following methods. They all generate a pad string with the <code>&quot;x&quot;</code> operator and combine that with <code>$text</code>. These methods do not truncate <code>$text</code>. </p>
<p> Left and right padding with any character, creating a new string: </p>
<pre><code>    my $padded = $pad_char x ( $pad_len - length( $text ) ) . $text;
    my $padded = $text . $pad_char x ( $pad_len - length( $text ) );
</code></pre>
<p> Left and right padding with any character, modifying <code>$text</code> directly: </p>
<pre><code>    substr( $text, 0, 0 ) = $pad_char x ( $pad_len - length( $text ) );
    $text .= $pad_char x ( $pad_len - length( $text ) );
</code></pre>
<h3>How do I extract selected columns from a string?</h3>
<p> (contributed by brian d foy) </p>
<p> If you know the columns that contain the data, you can use <code>&quot;substr&quot;</code> to extract a single column. </p>
<pre><code>    my $column = substr( $line, $start_column, $length );
</code></pre>
<p> You can use <code>&quot;split&quot;</code> if the columns are separated by whitespace or some other delimiter, as long as whitespace or the delimiter cannot appear as part of the data. </p>
<pre><code>    my $line = ' fred barney betty ';
    my @columns = split /\s+/, $line;
        # ( '', 'fred', 'barney', 'betty' );
    my $line = 'fred||barney||betty';
    my @columns = split /\|/, $line;
        # ( 'fred', '', 'barney', '', 'betty' );
</code></pre>
<p> If you want to work with comma-separated values, don&#8217;t do this since that format is a bit more complicated. Use one of the modules that handle that format, such as Text::CSV, Text::CSV_XS, or Text::CSV_PP. </p>
<p> If you want to break apart an entire line of fixed columns, you can use <code>&quot;unpack&quot;</code> with the A (<font SIZE="-1">ASCII</font>) format. By using a number after the format specifier, you can denote the column width. See the <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> entries in perlfunc for more details. </p>
<pre><code>    my @fields = unpack( $line, &quot;A8 A8 A8 A16 A4&quot; );
</code></pre>
<p> Note that spaces in the format argument to <code>&quot;unpack&quot;</code> do not denote literal spaces. If you have space separated data, you may want <code>&quot;split&quot;</code> instead.  </p>
<h3>How do I find the soundex value of a string?</h3>
<p> (contributed by brian d foy) </p>
<p> You can use the <code>&quot;Text::Soundex&quot;</code> module. If you want to do fuzzy or close matching, you might also try the String::Approx, and Text::Metaphone, and Text::DoubleMetaphone modules.  </p>
<h3>How can I expand variables in text strings?</h3>
<p> (contributed by brian d foy) </p>
<p> If you can avoid it, don&#8217;t, or if you can use a templating system, such as Text::Template or Template Toolkit, do that instead. You might even be able to get the job done with <code>&quot;sprintf&quot;</code> or <code>&quot;printf&quot;</code>: </p>
<pre><code>    my $string = sprintf 'Say hello to %s and %s', $foo, $bar;
</code></pre>
<p> However, for the one-off simple case where I don&#8217;t want to pull out a full templating system, I&#8217;ll use a string that has two Perl scalar variables in it. In this example, I want to expand <code>$foo</code> and <code>$bar</code> to their variable&#8217;s values: </p>
<pre><code>    my $foo = 'Fred';
    my $bar = 'Barney';
    $string = 'Say hello to $foo and $bar';
</code></pre>
<p> One way I can do this involves the substitution operator and a double <code>&quot;/e&quot;</code> flag. The first <code>&quot;/e&quot;</code> evaluates <code>$1</code> on the replacement side and turns it into <code>$foo</code>. The second /e starts with <code>$foo</code> and replaces it with its value. <code>$foo</code>, then, turns into &#8216;Fred&#8217;, and that&#8217;s finally what&#8217;s left in the string: </p>
<pre><code>    $string =~ s/(\$\w+)/$1/eeg; # 'Say hello to Fred and Barney'
</code></pre>
<p> The <code>&quot;/e&quot;</code> will also silently ignore violations of strict, replacing undefined variable names with the empty string. Since I&#8217;m using the <code>&quot;/e&quot;</code> flag (twice even!), I have all of the same security problems I have with <code>&quot;eval&quot;</code> in its string form. If there&#8217;s something odd in <code>$foo</code>, perhaps something like <code>&quot;@{[ system &quot;rm -rf /&quot; ]}&quot;</code>, then I could get myself in trouble. </p>
<p> To get around the security problem, I could also pull the values from a hash instead of evaluating variable names. Using a single <code>&quot;/e&quot;</code>, I can check the hash to ensure the value exists, and if it doesn&#8217;t, I can replace the missing value with a marker, in this case <code>&quot;???&quot;</code> to signal that I missed something: </p>
<pre><code>    my $string = 'This has $foo and $bar';
    my %Replacements = (
        foo =&gt; 'Fred',
        );
    # $string =~ s/\$(\w+)/$Replacements{$1}/g;
    $string =~ s/\$(\w+)/
        exists $Replacements{$1} ? $Replacements{$1} : '???'
        /eg;
    print $string;
</code></pre>
<h3>What's wrong with always quoting $vars?</h3>
<p> The problem is that those double-quotes force stringification---coercing numbers and references into strings---even when you don&#8217;t want them to be strings. Think of it this way: double-quote expansion is used to produce new strings. If you already have a string, why do you need more? </p>
<p> If you get used to writing odd things like these: </p>
<pre><code>    print &quot;$var&quot;; # BAD
    my $new = &quot;$old&quot;; # BAD
    somefunc(&quot;$var&quot;); # BAD
</code></pre>
<p> You&#8217;ll be in trouble. Those should (in 99.8% of the cases) be the simpler and more direct: </p>
<pre><code>    print $var;
    my $new = $old;
    somefunc($var);
</code></pre>
<p> Otherwise, besides slowing you down, you&#8217;re going to break code when the thing in the scalar is actually neither a string nor a number, but a reference: </p>
<pre><code>    func(\@array);
    sub func {
        my $aref = shift;
        my $oref = &quot;$aref&quot;; # WRONG
    }
</code></pre>
<p> You can also get into subtle problems on those few operations in Perl that actually do care about the difference between a string and a number, such as the magical <code>&quot;++&quot;</code> autoincrement operator or the <code>syscall()</code> function. </p>
<p> Stringification also destroys arrays. </p>
<pre><code>    my @lines = `command`;
    print &quot;@lines&quot;; # WRONG - extra blanks
    print @lines; # right
</code></pre>
<font SIZE="-1"></font><h3>Why don't my &lt;&lt; HERE documents work?</h3>
<p> Here documents are found in perlop. Check for these three things: </p>
<dl>
<dt>There must be no space after the &lt;&lt; part.</dt>
<dd>  </dd>
<dt>There (probably) should be a semicolon at the end of the opening token</dt>
<dd>  </dd>
<dt>You can&#8217;t (easily) have any space in front of the tag.</dt>
<dd>  </dd>
<dt>There needs to be at least a line separator after the end token.</dt>
<dd>  </dd></dl>
<p> If you want to indent the text in the here document, you can do this: </p>
<pre><code>    # all in one
    (my $VAR = &lt;&lt;HERE_TARGET) =~ s/^\s+//gm;
        your text
        goes here
    HERE_TARGET
</code></pre>
<p> But the <font SIZE="-1">HERE_TARGET</font> must still be flush against the margin. If you want that indented also, you&#8217;ll have to quote in the indentation. </p>
<pre><code>    (my $quote = &lt;&lt;' FINIS') =~ s/^\s+//gm;
            ...we will have peace, when you and all your works have
            perished--and the works of your dark master to whom you
            would deliver us. You are a liar, Saruman, and a corrupter
            of men's hearts. --Theoden in /usr/src/perl/taint.c
        FINIS
    $quote =~ s/\s+--/\n--/;
</code></pre>
<p> A nice general-purpose fixer-upper function for indented here documents follows. It expects to be called with a here document as its argument. It looks to see whether each line begins with a common substring, and if so, strips that substring off. Otherwise, it takes the amount of leading whitespace found on the first line and removes that much off each subsequent line. </p>
<pre><code>    sub fix {
        local $_ = shift;
        my ($white, $leader); # common whitespace and common leading string
        if (/^\s*(?:([^\w\s]+)(\s*).*\n)(?:\s*\g1\g2?.*\n)+$/) {
            ($white, $leader) = ($2, quotemeta($1));
        } else {
            ($white, $leader) = (/^(\s+)/, '');
        }
        s/^\s*?$leader(?:$white)?//gm;
        return $_;
    }
</code></pre>
<p> This works with leading special strings, dynamically determined: </p>
<pre><code>    my $remember_the_main = fix&lt;&lt;' MAIN_INTERPRETER_LOOP';
    @@@ int
    @@@ runops() {
    @@@ SAVEI32(runlevel);
    @@@ runlevel++;
    @@@ while ( op = (*op-&gt;op_ppaddr)() );
    @@@ TAINT_NOT;
    @@@ return 0;
    @@@ }
    MAIN_INTERPRETER_LOOP
</code></pre>
<p> Or with a fixed amount of leading whitespace, with remaining indentation correctly preserved: </p>
<pre><code>    my $poem = fix&lt;&lt;EVER_ON_AND_ON;
       Now far ahead the Road has gone,
      And I must follow, if I can,
       Pursuing it with eager feet,
      Until it joins some larger way
       Where many paths and errands meet.
      And whither then? I cannot say.
        --Bilbo in /usr/src/perl/pp_ctl.c
    EVER_ON_AND_ON
</code></pre>
<p> Beginning with Perl version 5.26, a much simpler and cleaner way to write indented here documents has been added to the language: the tilde (~) modifier. See ``Indented Here-docs&#8217;&#8216; in perlop for details.  </p>
<h2>Data: Arrays</h2>
<h3>What is the difference between a list and an array?</h3>
<p> (contributed by brian d foy) </p>
<p> A list is a fixed collection of scalars. An array is a variable that holds a variable collection of scalars. An array can supply its collection for list operations, so list operations also work on arrays: </p>
<pre><code>    # slices
    ( 'dog', 'cat', 'bird' )[2,3];
    @animals[2,3];
    # iteration
    foreach ( qw( dog cat bird ) ) { ... }
    foreach ( @animals ) { ... }
    my @three = grep { length == 3 } qw( dog cat bird );
    my @three = grep { length == 3 } @animals;
    # supply an argument list
    wash_animals( qw( dog cat bird ) );
    wash_animals( @animals );
</code></pre>
<p> Array operations, which change the scalars, rearrange them, or add or subtract some scalars, only work on arrays. These can&#8217;t work on a list, which is fixed. Array operations include <code>&quot;shift&quot;</code>, <code>&quot;unshift&quot;</code>, <code>&quot;push&quot;</code>, <code>&quot;pop&quot;</code>, and <code>&quot;splice&quot;</code>. </p>
<p> An array can also change its length: </p>
<pre><code>    $#animals = 1; # truncate to two elements
    $#animals = 10000; # pre-extend to 10,001 elements
</code></pre>
<p> You can change an array element, but you can&#8217;t change a list element: </p>
<pre><code>    $animals[0] = 'Rottweiler';
    qw( dog cat bird )[0] = 'Rottweiler'; # syntax error!
    foreach ( @animals ) {
        s/^d/fr/; # works fine
    }
    foreach ( qw( dog cat bird ) ) {
        s/^d/fr/; # Error! Modification of read only value!
    }
</code></pre>
<p> However, if the list element is itself a variable, it appears that you can change a list element. However, the list element is the variable, not the data. You&#8217;re not changing the list element, but something the list element refers to. The list element itself doesn&#8217;t change: it&#8217;s still the same variable. </p>
<p> You also have to be careful about context. You can assign an array to a scalar to get the number of elements in the array. This only works for arrays, though: </p>
<pre><code>    my $count = @animals; # only works with arrays
</code></pre>
<p> If you try to do the same thing with what you think is a list, you get a quite different result. Although it looks like you have a list on the righthand side, Perl actually sees a bunch of scalars separated by a comma: </p>
<pre><code>    my $scalar = ( 'dog', 'cat', 'bird' ); # $scalar gets bird
</code></pre>
<p> Since you&#8217;re assigning to a scalar, the righthand side is in scalar context. The comma operator (yes, it&#8217;s an operator!) in scalar context evaluates its lefthand side, throws away the result, and evaluates it&#8217;s righthand side and returns the result. In effect, that list-lookalike assigns to <code>$scalar</code> it&#8217;s rightmost value. Many people mess this up because they choose a list-lookalike whose last element is also the count they expect: </p>
<pre><code>    my $scalar = ( 1, 2, 3 ); # $scalar gets 3, accidentally
</code></pre>
<h3>What is the difference between $array[1] and @array[1]?</h3>
<p> (contributed by brian d foy) </p>
<p> The difference is the sigil, that special character in front of the array name. The <code>&quot;$&quot;</code> sigil means ``exactly one item&#8217;&#8216;, while the <code>&quot;@&quot;</code> sigil means ``zero or more items&#8217;&#8216;. The <code>&quot;$&quot;</code> gets you a single scalar, while the <code>&quot;@&quot;</code> gets you a list. </p>
<p> The confusion arises because people incorrectly assume that the sigil denotes the variable type. </p>
<p> The <code>$array[1]</code> is a single-element access to the array. It&#8217;s going to return the item in index 1 (or undef if there is no item there). If you intend to get exactly one element from the array, this is the form you should use. </p>
<p> The <code>@array[1]</code> is an array slice, although it has only one index. You can pull out multiple elements simultaneously by specifying additional indices as a list, like <code>@array[1,4,3,0]</code>. </p>
<p> Using a slice on the lefthand side of the assignment supplies list context to the righthand side. This can lead to unexpected results. For instance, if you want to read a single line from a filehandle, assigning to a scalar value is fine: </p>
<pre><code>    $array[1] = &lt;STDIN&gt;;
</code></pre>
<p> However, in list context, the line input operator returns all of the lines as a list. The first line goes into <code>@array[1]</code> and the rest of the lines mysteriously disappear: </p>
<pre><code>    @array[1] = &lt;STDIN&gt;; # most likely not what you want
</code></pre>
<p> Either the <code>&quot;use warnings&quot;</code> pragma or the <code>-w</code> flag will warn you when you use an array slice with a single index.  </p>
<h3>How can I remove duplicate elements from a list or array?</h3>
<p> (contributed by brian d foy) </p>
<p> Use a hash. When you think the words ``unique&#8217;&#8216; or ``duplicated&#8217;&#8216;, think ``hash keys&#8217;&#8216;. </p>
<p> If you don&#8217;t care about the order of the elements, you could just create the hash then extract the keys. It&#8217;s not important how you create that hash: just that you use <code>&quot;keys&quot;</code> to get the unique elements. </p>
<pre><code>    my %hash = map { $_, 1 } @array;
    # or a hash slice: @hash{ @array } = ();
    # or a foreach: $hash{$_} = 1 foreach ( @array );
    my @unique = keys %hash;
</code></pre>
<p> If you want to use a module, try the <code>&quot;uniq&quot;</code> function from List::MoreUtils. In list context it returns the unique elements, preserving their order in the list. In scalar context, it returns the number of unique elements. </p>
<pre><code>    use List::MoreUtils qw(uniq);
    my @unique = uniq( 1, 2, 3, 4, 4, 5, 6, 5, 7 ); # 1,2,3,4,5,6,7
    my $unique = uniq( 1, 2, 3, 4, 4, 5, 6, 5, 7 ); # 7
</code></pre>
<p> You can also go through each element and skip the ones you&#8217;ve seen before. Use a hash to keep track. The first time the loop sees an element, that element has no key in <code>%Seen</code>. The <code>&quot;next&quot;</code> statement creates the key and immediately uses its value, which is <code>&quot;undef&quot;</code>, so the loop continues to the <code>&quot;push&quot;</code> and increments the value for that key. The next time the loop sees that same element, its key exists in the hash <i>and</i> the value for that key is true (since it&#8217;s not 0 or <code>&quot;undef&quot;</code>), so the next skips that iteration and the loop goes to the next element. </p>
<pre><code>    my @unique = ();
    my %seen = ();
    foreach my $elem ( @array ) {
        next if $seen{ $elem }++;
        push @unique, $elem;
    }
</code></pre>
<p> You can write this more briefly using a grep, which does the same thing. </p>
<pre><code>    my %seen = ();
    my @unique = grep { ! $seen{ $_ }++ } @array;
</code></pre>
<h3>How can I tell whether a certain element is contained in a list or array?</h3>
<p> (portions of this answer contributed by Anno Siegel and brian d foy) </p>
<p> Hearing the word ``in&#8217;&#8216; is an <i>in</i>dication that you probably should have used a hash, not a list or array, to store your data. Hashes are designed to answer this question quickly and efficiently. Arrays aren&#8217;t. </p>
<p> That being said, there are several ways to approach this. In Perl 5.10 and later, you can use the smart match operator to check that an item is contained in an array or a hash: </p>
<pre><code>    use 5.010;
    if( $item ~~ @array ) {
        say &quot;The array contains $item&quot;
    }
    if( $item ~~ %hash ) {
        say &quot;The hash contains $item&quot;
    }
</code></pre>
<p> With earlier versions of Perl, you have to do a bit more work. If you are going to make this query many times over arbitrary string values, the fastest way is probably to invert the original array and maintain a hash whose keys are the first array&#8217;s values: </p>
<pre><code>    my @blues = qw/azure cerulean teal turquoise lapis-lazuli/;
    my %is_blue = ();
    for (@blues) { $is_blue{$_} = 1 }
</code></pre>
<p> Now you can check whether <code>$is_blue{$some_color}</code>. It might have been a good idea to keep the blues all in a hash in the first place. </p>
<p> If the values are all small integers, you could use a simple indexed array. This kind of an array will take up less space: </p>
<pre><code>    my @primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31);
    my @is_tiny_prime = ();
    for (@primes) { $is_tiny_prime[$_] = 1 }
    # or simply @istiny_prime[@primes] = (1) x @primes;
</code></pre>
<p> Now you check whether <code>$is_tiny_prime</code>[$some_number]. </p>
<p> If the values in question are integers instead of strings, you can save quite a lot of space by using bit strings instead: </p>
<pre><code>    my @articles = ( 1..10, 150..2000, 2017 );
    undef $read;
    for (@articles) { vec($read,$_,1) = 1 }
</code></pre>
<p> Now check whether <code>&quot;vec($read,$n,1)&quot;</code> is true for some <code>$n</code>. </p>
<p> These methods guarantee fast individual tests but require a re-organization of the original list or array. They only pay off if you have to test multiple values against the same array. </p>
<p> If you are testing only once, the standard module List::Util exports the function <code>&quot;first&quot;</code> for this purpose. It works by stopping once it finds the element. It&#8217;s written in C for speed, and its Perl equivalent looks like this subroutine: </p>
<pre><code>    sub first (&amp;@) {
        my $code = shift;
        foreach (@_) {
            return $_ if &amp;{$code}();
        }
        undef;
    }
</code></pre>
<p> If speed is of little concern, the common idiom uses grep in scalar context (which returns the number of items that passed its condition) to traverse the entire list. This does have the benefit of telling you how many matches it found, though. </p>
<pre><code>    my $is_there = grep $_ eq $whatever, @array;
</code></pre>
<p> If you want to actually extract the matching elements, simply use grep in list context. </p>
<pre><code>    my @matches = grep $_ eq $whatever, @array;
</code></pre>
<h3>How do I compute the difference of two arrays? How do I compute the intersection of two arrays?</h3>
<p> Use a hash. Here&#8217;s code to do both and more. It assumes that each element is unique in a given array: </p>
<pre><code>    my (@union, @intersection, @difference);
    my %count = ();
    foreach my $element (@array1, @array2) { $count{$element}++ }
    foreach my $element (keys %count) {
        push @union, $element;
        push @{ $count{$element} &gt; 1 ? \@intersection : \@difference }, $element;
    }
</code></pre>
<p> Note that this is the <i>symmetric difference</i>, that is, all elements in either A or in B but not in both. Think of it as an xor operation.  </p>
<h3>How do I test whether two arrays or hashes are equal?</h3>
<p> With Perl 5.10 and later, the smart match operator can give you the answer with the least amount of work: </p>
<pre><code>    use 5.010;
    if( @array1 ~~ @array2 ) {
        say &quot;The arrays are the same&quot;;
    }
    if( %hash1 ~~ %hash2 ) # doesn't check values! {
        say &quot;The hash keys are the same&quot;;
    }
</code></pre>
<p> The following code works for single-level arrays. It uses a stringwise comparison, and does not distinguish defined versus undefined empty strings. Modify if you have other needs. </p>
<pre><code>    $are_equal = compare_arrays(\@frogs, \@toads);
    sub compare_arrays {
        my ($first, $second) = @_;
        no warnings; # silence spurious -w undef complaints
        return 0 unless @$first == @$second;
        for (my $i = 0; $i &lt; @$first; $i++) {
            return 0 if $first-&gt;[$i] ne $second-&gt;[$i];
        }
        return 1;
    }
</code></pre>
<p> For multilevel structures, you may wish to use an approach more like this one. It uses the <font SIZE="-1">CPAN</font> module FreezeThaw: </p>
<pre><code>    use FreezeThaw qw(cmpStr);
    my @a = my @b = ( &quot;this&quot;, &quot;that&quot;, [ &quot;more&quot;, &quot;stuff&quot; ] );
    printf &quot;a and b contain %s arrays\n&quot;,
        cmpStr(\@a, \@b) == 0
        ? &quot;the same&quot;
        : &quot;different&quot;;
</code></pre>
<p> This approach also works for comparing hashes. Here we&#8217;ll demonstrate two different answers: </p>
<pre><code>    use FreezeThaw qw(cmpStr cmpStrHard);
    my %a = my %b = ( &quot;this&quot; =&gt; &quot;that&quot;, &quot;extra&quot; =&gt; [ &quot;more&quot;, &quot;stuff&quot; ] );
    $a{EXTRA} = \%b;
    $b{EXTRA} = \%a;
    printf &quot;a and b contain %s hashes\n&quot;,
    cmpStr(\%a, \%b) == 0 ? &quot;the same&quot; : &quot;different&quot;;
    printf &quot;a and b contain %s hashes\n&quot;,
    cmpStrHard(\%a, \%b) == 0 ? &quot;the same&quot; : &quot;different&quot;;
</code></pre>
<p> The first reports that both those the hashes contain the same data, while the second reports that they do not. Which you prefer is left as an exercise to the reader.  </p>
<h3>How do I find the first array element for which a condition is true?</h3>
<p> To find the first array element which satisfies a condition, you can use the <code>&quot;first()&quot;</code> function in the List::Util module, which comes with Perl 5.8. This example finds the first element that contains ``Perl&#8217;&#8216;. </p>
<pre><code>    use List::Util qw(first);
    my $element = first { /Perl/ } @array;
</code></pre>
<p> If you cannot use List::Util, you can make your own loop to do the same thing. Once you find the element, you stop the loop with last. </p>
<pre><code>    my $found;
    foreach ( @array ) {
        if( /Perl/ ) { $found = $_; last }
    }
</code></pre>
<p> If you want the array index, use the <code>&quot;firstidx()&quot;</code> function from <code>&quot;List::MoreUtils&quot;</code>: </p>
<pre><code>    use List::MoreUtils qw(firstidx);
    my $index = firstidx { /Perl/ } @array;
</code></pre>
<p> Or write it yourself, iterating through the indices and checking the array element at each index until you find one that satisfies the condition: </p>
<pre><code>    my( $found, $index ) = ( undef, -1 );
    for( $i = 0; $i &lt; @array; $i++ ) {
        if( $array[$i] =~ /Perl/ ) {
            $found = $array[$i];
            $index = $i;
            last;
        }
    }
</code></pre>
<h3>How do I handle linked lists?</h3>
<p> (contributed by brian d foy) </p>
<p> Perl&#8217;s arrays do not have a fixed size, so you don&#8217;t need linked lists if you just want to add or remove items. You can use array operations such as <code>&quot;push&quot;</code>, <code>&quot;pop&quot;</code>, <code>&quot;shift&quot;</code>, <code>&quot;unshift&quot;</code>, or <code>&quot;splice&quot;</code> to do that. </p>
<p> Sometimes, however, linked lists can be useful in situations where you want to ``shard&#8217;&#8216; an array so you have many small arrays instead of a single big array. You can keep arrays longer than Perl&#8217;s largest array index, lock smaller arrays separately in threaded programs, reallocate less memory, or quickly insert elements in the middle of the chain. </p>
<p> Steve Lembark goes through the details in his <font SIZE="-1">YAPC::NA 2009</font> talk ``Perly Linked Lists&#8217;&#8216; ( &lt;<a rel="nofollow" href="http://www.slideshare.net/lembark/perly-linked-lists">http://www.slideshare.net/lembark/perly-linked-lists</a>&gt; ), although you can just use his LinkedList::Single module.  </p>
<h3>How do I handle circular lists?</h3>
<p> (contributed by brian d foy) </p>
<p> If you want to cycle through an array endlessly, you can increment the index modulo the number of elements in the array: </p>
<pre><code>    my @array = qw( a b c );
    my $i = 0;
    while( 1 ) {
        print $array[ $i++ % @array ], &quot;\n&quot;;
        last if $i &gt; 20;
    }
</code></pre>
<p> You can also use Tie::Cycle to use a scalar that always has the next element of the circular array: </p>
<pre><code>    use Tie::Cycle;
    tie my $cycle, 'Tie::Cycle', [ qw( FFFFFF 000000 FFFF00 ) ];
    print $cycle; # FFFFFF
    print $cycle; # 000000
    print $cycle; # FFFF00
</code></pre>
<p> The Array::Iterator::Circular creates an iterator object for circular arrays: </p>
<pre><code>    use Array::Iterator::Circular;
    my $color_iterator = Array::Iterator::Circular-&gt;new(
        qw(red green blue orange)
        );
    foreach ( 1 .. 20 ) {
        print $color_iterator-&gt;next, &quot;\n&quot;;
    }
</code></pre>
<h3>How do I shuffle an array randomly?</h3>
<p> If you either have Perl 5.8.0 or later installed, or if you have Scalar-List-Utils 1.03 or later installed, you can say: </p>
<pre><code>    use List::Util 'shuffle';
    @shuffled = shuffle(@list);
</code></pre>
<p> If not, you can use a Fisher-Yates shuffle. </p>
<pre><code>    sub fisher_yates_shuffle {
        my $deck = shift; # $deck is a reference to an array
        return unless @$deck; # must not be empty!
        my $i = @$deck;
        while (--$i) {
            my $j = int rand ($i+1);
            @$deck[$i,$j] = @$deck[$j,$i];
        }
    }
    # shuffle my mpeg collection
    #
    my @mpeg = &lt;audio/*/*.mp3&gt;;
    fisher_yates_shuffle( \@mpeg ); # randomize @mpeg in place
    print @mpeg;
</code></pre>
<p> Note that the above implementation shuffles an array in place, unlike the <code>&quot;List::Util::shuffle()&quot;</code> which takes a list and returns a new shuffled list. </p>
<p> You&#8217;ve probably seen shuffling algorithms that work using splice, randomly picking another element to swap the current element with </p>
<pre><code>    srand;
    @new = ();
    @old = 1 .. 10; # just a demo
    while (@old) {
        push(@new, splice(@old, rand @old, 1));
    }
</code></pre>
<p> This is bad because splice is already O(N), and since you do it N times, you just invented a quadratic algorithm; that is, O(N**2). This does not scale, although Perl is so efficient that you probably won&#8217;t notice this until you have rather largish arrays.  </p>
<h3>How do I process/modify each element of an array?</h3>
<p> Use <code>&quot;for&quot;</code>/<code>&quot;foreach&quot;</code>: </p>
<pre><code>    for (@lines) {
        s/foo/bar/; # change that word
        tr/XZ/ZX/; # swap those letters
    }
</code></pre>
<p> Here&#8217;s another; let&#8217;s compute spherical volumes: </p>
<pre><code>    my @volumes = @radii;
    for (@volumes) { # @volumes has changed parts
        $_ **= 3;
        $_ *= (4/3) * 3.14159; # this will be constant folded
    }
</code></pre>
<p> which can also be done with <code>&quot;map()&quot;</code> which is made to transform one list into another: </p>
<pre><code>    my @volumes = map {$_ ** 3 * (4/3) * 3.14159} @radii;
</code></pre>
<p> If you want to do the same thing to modify the values of the hash, you can use the <code>&quot;values&quot;</code> function. As of Perl 5.6 the values are not copied, so if you modify <code>$orbit</code> (in this case), you modify the value. </p>
<pre><code>    for my $orbit ( values %orbits ) {
        ($orbit **= 3) *= (4/3) * 3.14159;
    }
</code></pre>
<p> Prior to perl 5.6 <code>&quot;values&quot;</code> returned copies of the values, so older perl code often contains constructions such as <code>@orbits{keys %orbits}</code> instead of <code>&quot;values %orbits&quot;</code> where the hash is to be modified.  </p>
<h3>How do I select a random element from an array?</h3>
<p> Use the <code>&quot;rand()&quot;</code> function (see ``rand&#8217;&#8216; in perlfunc): </p>
<pre><code>    my $index = rand @array;
    my $element = $array[$index];
</code></pre>
<p> Or, simply: </p>
<pre><code>    my $element = $array[ rand @array ];
</code></pre>
<h3>How do I permute N elements of a list?</h3>
<p> Use the List::Permutor module on <font SIZE="-1">CPAN.</font> If the list is actually an array, try the Algorithm::Permute module (also on <font SIZE="-1">CPAN</font>). It&#8217;s written in <font SIZE="-1">XS</font> code and is very efficient: </p>
<pre><code>    use Algorithm::Permute;
    my @array = 'a'..'d';
    my $p_iterator = Algorithm::Permute-&gt;new ( \@array );
    while (my @perm = $p_iterator-&gt;next) {
       print &quot;next permutation: (@perm)\n&quot;;
    }
</code></pre>
<p> For even faster execution, you could do: </p>
<pre><code>    use Algorithm::Permute;
    my @array = 'a'..'d';
    Algorithm::Permute::permute {
        print &quot;next permutation: (@array)\n&quot;;
    } @array;
</code></pre>
<p> Here&#8217;s a little program that generates all permutations of all the words on each line of input. The algorithm embodied in the <code>&quot;permute()&quot;</code> function is discussed in Volume 4 (still unpublished) of Knuth&#8217;s <i>The Art of Computer Programming</i> and will work on any list: </p>
<pre><code>    #!/usr/bin/perl -n
    # Fischer-Krause ordered permutation generator
    sub permute (&amp;@) {
        my $code = shift;
        my @idx = 0..$#_;
        while ( $code-&gt;(@_[@idx]) ) {
            my $p = $#idx;
            --$p while $idx[$p-1] &gt; $idx[$p];
            my $q = $p or return;
            push @idx, reverse splice @idx, $p;
            ++$q while $idx[$p-1] &gt; $idx[$q];
            @idx[$p-1,$q]=@idx[$q,$p-1];
        }
    }
    permute { print &quot;@_\n&quot; } split;
</code></pre>
<p> The Algorithm::Loops module also provides the <code>&quot;NextPermute&quot;</code> and <code>&quot;NextPermuteNum&quot;</code> functions which efficiently find all unique permutations of an array, even if it contains duplicate values, modifying it in-place: if its elements are in reverse-sorted order then the array is reversed, making it sorted, and it returns false; otherwise the next permutation is returned. </p>
<p> <code>&quot;NextPermute&quot;</code> uses string order and <code>&quot;NextPermuteNum&quot;</code> numeric order, so you can enumerate all the permutations of <code>0..9</code> like this: </p>
<pre><code>    use Algorithm::Loops qw(NextPermuteNum);
    my @list= 0..9;
    do { print &quot;@list\n&quot; } while NextPermuteNum @list;
</code></pre>
<h3>How do I sort an array by (anything)?</h3>
<p> Supply a comparison function to <code>sort()</code> (described in ``sort&#8217;&#8216; in perlfunc): </p>
<pre><code>    @list = sort { $a &lt;=&gt; $b } @list;
</code></pre>
<p> The default sort function is cmp, string comparison, which would sort <code>&quot;(1, 2, 10)&quot;</code> into <code>&quot;(1, 10, 2)&quot;</code>. <code>&quot;&lt;=&gt;&quot;</code>, used above, is the numerical comparison operator. </p>
<p> If you have a complicated function needed to pull out the part you want to sort on, then don&#8217;t do it inside the sort function. Pull it out first, because the sort <font SIZE="-1">BLOCK</font> can be called many times for the same element. Here&#8217;s an example of how to pull out the first word after the first number on each item, and then sort those words case-insensitively. </p>
<pre><code>    my @idx;
    for (@data) {
        my $item;
        ($item) = /\d+\s*(\S+)/;
        push @idx, uc($item);
    }
    my @sorted = @data[ sort { $idx[$a] cmp $idx[$b] } 0 .. $#idx ];
</code></pre>
<p> which could also be written this way, using a trick that&#8217;s come to be known as the Schwartzian Transform: </p>
<pre><code>    my @sorted = map { $_-&gt;[0] }
        sort { $a-&gt;[1] cmp $b-&gt;[1] }
        map { [ $_, uc( (/\d+\s*(\S+)/)[0]) ] } @data;
</code></pre>
<p> If you need to sort on several fields, the following paradigm is useful. </p>
<pre><code>    my @sorted = sort {
        field1($a) &lt;=&gt; field1($b) ||
        field2($a) cmp field2($b) ||
        field3($a) cmp field3($b)
    } @data;
</code></pre>
<p> This can be conveniently combined with precalculation of keys as given above. </p>
<p> See the <i>sort</i> article in the ``Far More Than You Ever Wanted To Know&#8217;&#8216; collection in &lt;<a rel="nofollow" href="http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz">http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz</a>&gt; for more about this approach. </p>
<p> See also the question later in perlfaq4 on sorting hashes.  </p>
<h3>How do I manipulate arrays of bits?</h3>
<p> Use <code>&quot;pack()&quot;</code> and <code>&quot;unpack()&quot;</code>, or else <code>&quot;vec()&quot;</code> and the bitwise operations. </p>
<p> For example, you don&#8217;t have to store individual bits in an array (which would mean that you&#8217;re wasting a lot of space). To convert an array of bits to a string, use <code>&quot;vec()&quot;</code> to set the right bits. This sets <code>$vec</code> to have bit N set only if <code>$ints[N]</code> was set: </p>
<pre><code>    my @ints = (...); # array of bits, e.g. ( 1, 0, 0, 1, 1, 0 ... )
    my $vec = '';
    foreach( 0 .. $#ints ) {
        vec($vec,$_,1) = 1 if $ints[$_];
    }
</code></pre>
<p> The string <code>$vec</code> only takes up as many bits as it needs. For instance, if you had 16 entries in <code>@ints</code>, <code>$vec</code> only needs two bytes to store them (not counting the scalar variable overhead). </p>
<p> Here&#8217;s how, given a vector in <code>$vec</code>, you can get those bits into your <code>@ints</code> array: </p>
<pre><code>    sub bitvec_to_list {
        my $vec = shift;
        my @ints;
        # Find null-byte density then select best algorithm
        if ($vec =~ tr/\0// / length $vec &gt; 0.95) {
            use integer;
            my $i;
            # This method is faster with mostly null-bytes
            while($vec =~ /[^\0]/g ) {
                $i = -9 + 8 * pos $vec;
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
                push @ints, $i if vec($vec, ++$i, 1);
            }
        }
        else {
            # This method is a fast general algorithm
            use integer;
            my $bits = unpack &quot;b*&quot;, $vec;
            push @ints, 0 if $bits =~ s/^(\d)// &amp;&amp; $1;
            push @ints, pos $bits while($bits =~ /1/g);
        }
        return \@ints;
    }
</code></pre>
<p> This method gets faster the more sparse the bit vector is. (Courtesy of Tim Bunce and Winfried Koenig.) </p>
<p> You can make the while loop a lot shorter with this suggestion from Benjamin Goldberg: </p>
<pre><code>    while($vec =~ /[^\0]+/g ) {
        push @ints, grep vec($vec, $_, 1), $-[0] * 8 .. $+[0] * 8;
    }
</code></pre>
<p> Or use the <font SIZE="-1">CPAN</font> module Bit::Vector: </p>
<pre><code>    my $vector = Bit::Vector-&gt;new($num_of_bits);
    $vector-&gt;Index_List_Store(@ints);
    my @ints = $vector-&gt;Index_List_Read();
</code></pre>
<p> Bit::Vector provides efficient methods for bit vector, sets of small integers and ``big int&#8217;&#8216; math. </p>
<p> Here&#8217;s a more extensive illustration using <code>vec()</code>: </p>
<pre><code>    # vec demo
    my $vector = &quot;\xff\x0f\xef\xfe&quot;;
    print &quot;Ilya's string \\xff\\x0f\\xef\\xfe represents the number &quot;,
    unpack(&quot;N&quot;, $vector), &quot;\n&quot;;
    my $is_set = vec($vector, 23, 1);
    print &quot;Its 23rd bit is &quot;, $is_set ? &quot;set&quot; : &quot;clear&quot;, &quot;.\n&quot;;
    pvec($vector);
    set_vec(1,1,1);
    set_vec(3,1,1);
    set_vec(23,1,1);
    set_vec(3,1,3);
    set_vec(3,2,3);
    set_vec(3,4,3);
    set_vec(3,4,7);
    set_vec(3,8,3);
    set_vec(3,8,7);
    set_vec(0,32,17);
    set_vec(1,32,17);
    sub set_vec {
        my ($offset, $width, $value) = @_;
        my $vector = '';
        vec($vector, $offset, $width) = $value;
        print &quot;offset=$offset width=$width value=$value\n&quot;;
        pvec($vector);
    }
    sub pvec {
        my $vector = shift;
        my $bits = unpack(&quot;b*&quot;, $vector);
        my $i = 0;
        my $BASE = 8;
        print &quot;vector length in bytes: &quot;, length($vector), &quot;\n&quot;;
        @bytes = unpack(&quot;A8&quot; x length($vector), $bits);
        print &quot;bits are: @bytes\n\n&quot;;
    }
</code></pre>
<code></code><h3>Why does defined() return true on empty arrays and hashes?</h3>
<p> The short story is that you should probably only use defined on scalars or functions, not on aggregates (arrays and hashes). See ``defined&#8217;&#8216; in perlfunc in the 5.004 release or later of Perl for more detail.  </p>
<h2>Data: Hashes (Associative Arrays)</h2>
<h3>How do I process an entire hash?</h3>
<p> (contributed by brian d foy) </p>
<p> There are a couple of ways that you can process an entire hash. You can get a list of keys, then go through each key, or grab a one key-value pair at a time. </p>
<p> To go through all of the keys, use the <code>&quot;keys&quot;</code> function. This extracts all of the keys of the hash and gives them back to you as a list. You can then get the value through the particular key you&#8217;re processing: </p>
<pre><code>    foreach my $key ( keys %hash ) {
        my $value = $hash{$key}
        ...
    }
</code></pre>
<p> Once you have the list of keys, you can process that list before you process the hash elements. For instance, you can sort the keys so you can process them in lexical order: </p>
<pre><code>    foreach my $key ( sort keys %hash ) {
        my $value = $hash{$key}
        ...
    }
</code></pre>
<p> Or, you might want to only process some of the items. If you only want to deal with the keys that start with <code>&quot;text:&quot;</code>, you can select just those using <code>&quot;grep&quot;</code>: </p>
<pre><code>    foreach my $key ( grep /^text:/, keys %hash ) {
        my $value = $hash{$key}
        ...
    }
</code></pre>
<p> If the hash is very large, you might not want to create a long list of keys. To save some memory, you can grab one key-value pair at a time using <code>&quot;each()&quot;</code>, which returns a pair you haven&#8217;t seen yet: </p>
<pre><code>    while( my( $key, $value ) = each( %hash ) ) {
        ...
    }
</code></pre>
<p> The <code>&quot;each&quot;</code> operator returns the pairs in apparently random order, so if ordering matters to you, you&#8217;ll have to stick with the <code>&quot;keys&quot;</code> method. </p>
<p> The <code>&quot;each()&quot;</code> operator can be a bit tricky though. You can&#8217;t add or delete keys of the hash while you&#8217;re using it without possibly skipping or re-processing some pairs after Perl internally rehashes all of the elements. Additionally, a hash has only one iterator, so if you mix <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code>, or <code>&quot;each&quot;</code> on the same hash, you risk resetting the iterator and messing up your processing. See the <code>&quot;each&quot;</code> entry in perlfunc for more details.  </p>
<h3>How do I merge two hashes?</h3>
<p> (contributed by brian d foy) </p>
<p> Before you decide to merge two hashes, you have to decide what to do if both hashes contain keys that are the same and if you want to leave the original hashes as they were. </p>
<p> If you want to preserve the original hashes, copy one hash (<code>%hash1</code>) to a new hash (<code>%new_hash</code>), then add the keys from the other hash (<code>%hash2</code> to the new hash. Checking that the key already exists in <code>%new_hash</code> gives you a chance to decide what to do with the duplicates: </p>
<pre><code>    my %new_hash = %hash1; # make a copy; leave %hash1 alone
    foreach my $key2 ( keys %hash2 ) {
        if( exists $new_hash{$key2} ) {
            warn &quot;Key [$key2] is in both hashes!&quot;;
            # handle the duplicate (perhaps only warning)
            ...
            next;
        }
        else {
            $new_hash{$key2} = $hash2{$key2};
        }
    }
</code></pre>
<p> If you don&#8217;t want to create a new hash, you can still use this looping technique; just change the <code>%new_hash</code> to <code>%hash1</code>. </p>
<pre><code>    foreach my $key2 ( keys %hash2 ) {
        if( exists $hash1{$key2} ) {
            warn &quot;Key [$key2] is in both hashes!&quot;;
            # handle the duplicate (perhaps only warning)
            ...
            next;
        }
        else {
            $hash1{$key2} = $hash2{$key2};
        }
      }
</code></pre>
<p> If you don&#8217;t care that one hash overwrites keys and values from the other, you could just use a hash slice to add one hash to another. In this case, values from <code>%hash2</code> replace values from <code>%hash1</code> when they have keys in common: </p>
<pre><code>    @hash1{ keys %hash2 } = values %hash2;
</code></pre>
<h3>What happens if I add or remove keys from a hash while iterating over it?</h3>
<p> (contributed by brian d foy) </p>
<p> The easy answer is ``Don&#8217;t do that!&#8216;&#8216; </p>
<p> If you iterate through the hash with <code>each()</code>, you can delete the key most recently returned without worrying about it. If you delete or add other keys, the iterator may skip or double up on them since perl may rearrange the hash table. See the entry for <code>&quot;each()&quot;</code> in perlfunc.  </p>
<h3>How do I look up a hash element by value?</h3>
<p> Create a reverse hash: </p>
<pre><code>    my %by_value = reverse %by_key;
    my $key = $by_value{$value};
</code></pre>
<p> That&#8217;s not particularly efficient. It would be more space-efficient to use: </p>
<pre><code>    while (my ($key, $value) = each %by_key) {
        $by_value{$value} = $key;
    }
</code></pre>
<p> If your hash could have repeated values, the methods above will only find one of the associated keys. This may or may not worry you. If it does worry you, you can always reverse the hash into a hash of arrays instead: </p>
<pre><code>    while (my ($key, $value) = each %by_key) {
         push @{$key_list_by_value{$value}}, $key;
    }
</code></pre>
<h3>How can I know how many entries are in a hash?</h3>
<p> (contributed by brian d foy) </p>
<p> This is very similar to ``How do I process an entire hash?&#8216;&#8216;, also in perlfaq4, but a bit simpler in the common cases. </p>
<p> You can use the <code>&quot;keys()&quot;</code> built-in function in scalar context to find out have many entries you have in a hash: </p>
<pre><code>    my $key_count = keys %hash; # must be scalar context!
</code></pre>
<p> If you want to find out how many entries have a defined value, that&#8217;s a bit different. You have to check each value. A <code>&quot;grep&quot;</code> is handy: </p>
<pre><code>    my $defined_value_count = grep { defined } values %hash;
</code></pre>
<p> You can use that same structure to count the entries any way that you like. If you want the count of the keys with vowels in them, you just test for that instead: </p>
<pre><code>    my $vowel_count = grep { /[aeiou]/ } keys %hash;
</code></pre>
<p> The <code>&quot;grep&quot;</code> in scalar context returns the count. If you want the list of matching items, just use it in list context instead: </p>
<pre><code>    my @defined_values = grep { defined } values %hash;
</code></pre>
<p> The <code>&quot;keys()&quot;</code> function also resets the iterator, which means that you may see strange results if you use this between uses of other hash operators such as <code>&quot;each()&quot;</code>.  </p>
<h3>How do I sort a hash (optionally by value instead of key)?</h3>
<p> (contributed by brian d foy) </p>
<p> To sort a hash, start with the keys. In this example, we give the list of keys to the sort function which then compares them ASCIIbetically (which might be affected by your locale settings). The output list has the keys in ASCIIbetical order. Once we have the keys, we can go through them to create a report which lists the keys in ASCIIbetical order. </p>
<pre><code>    my @keys = sort { $a cmp $b } keys %hash;
    foreach my $key ( @keys ) {
        printf &quot;%-20s %6d\n&quot;, $key, $hash{$key};
    }
</code></pre>
<p> We could get more fancy in the <code>&quot;sort()&quot;</code> block though. Instead of comparing the keys, we can compute a value with them and use that value as the comparison. </p>
<p> For instance, to make our report order case-insensitive, we use <code>&quot;lc&quot;</code> to lowercase the keys before comparing them: </p>
<pre><code>    my @keys = sort { lc $a cmp lc $b } keys %hash;
</code></pre>
<p> Note: if the computation is expensive or the hash has many elements, you may want to look at the Schwartzian Transform to cache the computation results. </p>
<p> If we want to sort by the hash value instead, we use the hash key to look it up. We still get out a list of keys, but this time they are ordered by their value. </p>
<pre><code>    my @keys = sort { $hash{$a} &lt;=&gt; $hash{$b} } keys %hash;
</code></pre>
<p> From there we can get more complex. If the hash values are the same, we can provide a secondary sort on the hash key. </p>
<pre><code>    my @keys = sort {
        $hash{$a} &lt;=&gt; $hash{$b}
            or
        &quot;\L$a&quot; cmp &quot;\L$b&quot;
    } keys %hash;
</code></pre>
<h3>How can I always keep my hash sorted?</h3>
<p> You can look into using the <code>&quot;DB_File&quot;</code> module and <code>&quot;tie()&quot;</code> using the <code>$DB_BTREE</code> hash bindings as documented in ``In Memory Databases&#8217;&#8216; in DB_File. The Tie::IxHash module from <font SIZE="-1">CPAN</font> might also be instructive. Although this does keep your hash sorted, you might not like the slowdown you suffer from the tie interface. Are you sure you need to do this? :)  </p>
<h3>What's the difference between delete and undef with hashes?</h3>
<p> Hashes contain pairs of scalars: the first is the key, the second is the value. The key will be coerced to a string, although the value can be any kind of scalar: string, number, or reference. If a key <code>$key</code> is present in <code>%hash</code>, <code>&quot;exists($hash{$key})&quot;</code> will return true. The value for a given key can be <code>&quot;undef&quot;</code>, in which case <code>$hash{$key}</code> will be <code>&quot;undef&quot;</code> while <code>&quot;exists $hash{$key}&quot;</code> will return true. This corresponds to (<code>$key</code>, <code>&quot;undef&quot;</code>) being in the hash. </p>
<p> Pictures help... Here&#8217;s the <code>%hash</code> table: </p>
<pre><code>      keys values
    +------+------+
    | a | 3 |
    | x | 7 |
    | d | 0 |
    | e | 2 |
    +------+------+
</code></pre>
<p> And these conditions hold </p>
<pre><code>    $hash{'a'} is true
    $hash{'d'} is false
    defined $hash{'d'} is true
    defined $hash{'a'} is true
    exists $hash{'a'} is true (Perl 5 only)
    grep ($_ eq 'a', keys %hash) is true
</code></pre>
<p> If you now say </p>
<pre><code>    undef $hash{'a'}
</code></pre>
<p> your table now reads: </p>
<pre><code>      keys values
    +------+------+
    | a | undef|
    | x | 7 |
    | d | 0 |
    | e | 2 |
    +------+------+
</code></pre>
<p> and these conditions now hold; changes in caps: </p>
<pre><code>    $hash{'a'} is FALSE
    $hash{'d'} is false
    defined $hash{'d'} is true
    defined $hash{'a'} is FALSE
    exists $hash{'a'} is true (Perl 5 only)
    grep ($_ eq 'a', keys %hash) is true
</code></pre>
<p> Notice the last two: you have an undef value, but a defined key! </p>
<p> Now, consider this: </p>
<pre><code>    delete $hash{'a'}
</code></pre>
<p> your table now reads: </p>
<pre><code>      keys values
    +------+------+
    | x | 7 |
    | d | 0 |
    | e | 2 |
    +------+------+
</code></pre>
<p> and these conditions now hold; changes in caps: </p>
<pre><code>    $hash{'a'} is false
    $hash{'d'} is false
    defined $hash{'d'} is true
    defined $hash{'a'} is false
    exists $hash{'a'} is FALSE (Perl 5 only)
    grep ($_ eq 'a', keys %hash) is FALSE
</code></pre>
<p> See, the whole entry is gone!  </p>
<h3>Why don't my tied hashes make the defined/exists distinction?</h3>
<p> This depends on the tied hash&#8217;s implementation of <font SIZE="-1"><code>EXISTS</code></font><code>()</code>. For example, there isn&#8217;t the concept of undef with hashes that are tied to DBM* files. It also means that <code>exists()</code> and <code>defined()</code> do the same thing with a DBM* file, and what they end up doing is not what they do with ordinary hashes.  </p>
<code></code><h3>How do I reset an each() operation part-way through?</h3>
<p> (contributed by brian d foy) </p>
<p> You can use the <code>&quot;keys&quot;</code> or <code>&quot;values&quot;</code> functions to reset <code>&quot;each&quot;</code>. To simply reset the iterator used by <code>&quot;each&quot;</code> without doing anything else, use one of them in void context: </p>
<pre><code>    keys %hash; # resets iterator, nothing else.
    values %hash; # resets iterator, nothing else.
</code></pre>
<p> See the documentation for <code>&quot;each&quot;</code> in perlfunc.  </p>
<h3>How can I get the unique keys from two hashes?</h3>
<p> First you extract the keys from the hashes into lists, then solve the ``removing duplicates&#8217;&#8216; problem described above. For example: </p>
<pre><code>    my %seen = ();
    for my $element (keys(%foo), keys(%bar)) {
        $seen{$element}++;
    }
    my @uniq = keys %seen;
</code></pre>
<p> Or more succinctly: </p>
<pre><code>    my @uniq = keys %&#123;&#123;%foo,%bar&#125;&#125;;
</code></pre>
<p> Or if you really want to save space: </p>
<pre><code>    my %seen = ();
    while (defined ($key = each %foo)) {
        $seen{$key}++;
    }
    while (defined ($key = each %bar)) {
        $seen{$key}++;
    }
    my @uniq = keys %seen;
</code></pre>
<font SIZE="-1"></font><h3>How can I store a multidimensional array in a DBM file?</h3>
<p> Either stringify the structure yourself (no fun), or else get the <font SIZE="-1">MLDBM</font> (which uses Data::Dumper) module from <font SIZE="-1">CPAN</font> and layer it on top of either DB_File or GDBM_File. You might also try DBM::Deep, but it can be a bit slow.  </p>
<h3>How can I make my hash remember the order I put elements into it?</h3>
<p> Use the Tie::IxHash from <font SIZE="-1">CPAN.</font> </p>
<pre><code>    use Tie::IxHash;
    tie my %myhash, 'Tie::IxHash';
    for (my $i=0; $i&lt;20; $i++) {
        $myhash{$i} = 2*$i;
    }
    my @keys = keys %myhash;
    # @keys = (0,1,2,3,...)
</code></pre>
<h3>Why does passing a subroutine an undefined element in a hash create it?</h3>
<p> (contributed by brian d foy) </p>
<p> Are you using a really old version of Perl? </p>
<p> Normally, accessing a hash key&#8217;s value for a nonexistent key will <i>not</i> create the key. </p>
<pre><code>    my %hash = ();
    my $value = $hash{ 'foo' };
    print &quot;This won't print\n&quot; if exists $hash{ 'foo' };
</code></pre>
<p> Passing <code>$hash{ &#8216;foo&#8217; }</code> to a subroutine used to be a special case, though. Since you could assign directly to <code>$_[0]</code>, Perl had to be ready to make that assignment so it created the hash key ahead of time: </p>
<pre><code>    my_sub( $hash{ 'foo' } );
    print &quot;This will print before 5.004\n&quot; if exists $hash{ 'foo' };
    sub my_sub {
        # $_[0] = 'bar'; # create hash key in case you do this
        1;
    }
</code></pre>
<p> Since Perl 5.004, however, this situation is a special case and Perl creates the hash key only when you make the assignment: </p>
<pre><code>    my_sub( $hash{ 'foo' } );
    print &quot;This will print, even after 5.004\n&quot; if exists $hash{ 'foo' };
    sub my_sub {
        $_[0] = 'bar';
    }
</code></pre>
<p> However, if you want the old behavior (and think carefully about that because it&#8217;s a weird side effect), you can pass a hash slice instead. Perl 5.004 didn&#8217;t make this a special case: </p>
<pre><code>    my_sub( @hash{ qw/foo/ } );
</code></pre>
<font SIZE="-2"></font><h3>How can I make the Perl equivalent of a C structure/C ++ class/hash or array of hashes or arrays?</h3>
<p> Usually a hash ref, perhaps like this: </p>
<pre><code>    $record = {
        NAME =&gt; &quot;Jason&quot;,
        EMPNO =&gt; 132,
        TITLE =&gt; &quot;deputy peon&quot;,
        AGE =&gt; 23,
        SALARY =&gt; 37_000,
        PALS =&gt; [ &quot;Norbert&quot;, &quot;Rhys&quot;, &quot;Phineas&quot;],
    };
</code></pre>
<p> References are documented in perlref and perlreftut. Examples of complex data structures are given in perldsc and perllol. Examples of structures and object-oriented classes are in perlootut.  </p>
<h3>How can I use a reference as a hash key?</h3>
<p> (contributed by brian d foy and Ben Morrow) </p>
<p> Hash keys are strings, so you can&#8217;t really use a reference as the key. When you try to do that, perl turns the reference into its stringified form (for instance, <code>&quot;HASH(0xDEADBEEF)&quot;</code>). From there you can&#8217;t get back the reference from the stringified form, at least without doing some extra work on your own. </p>
<p> Remember that the entry in the hash will still be there even if the referenced variable goes out of scope, and that it is entirely possible for Perl to subsequently allocate a different variable at the same address. This will mean a new variable might accidentally be associated with the value for an old. </p>
<p> If you have Perl 5.10 or later, and you just want to store a value against the reference for lookup later, you can use the core Hash::Util::Fieldhash module. This will also handle renaming the keys if you use multiple threads (which causes all variables to be reallocated at new addresses, changing their stringification), and garbage-collecting the entries when the referenced variable goes out of scope. </p>
<p> If you actually need to be able to get a real reference back from each hash entry, you can use the Tie::RefHash module, which does the required work for you.  </p>
<h3>How can I check if a key exists in a multilevel hash?</h3>
<p> (contributed by brian d foy) </p>
<p> The trick to this problem is avoiding accidental autovivification. If you want to check three keys deep, you might naïvely try this: </p>
<pre><code>    my %hash;
    if( exists $hash{key1}{key2}{key3} ) {
        ...;
    }
</code></pre>
<p> Even though you started with a completely empty hash, after that call to <code>&quot;exists&quot;</code> you&#8217;ve created the structure you needed to check for <code>&quot;key3&quot;</code>: </p>
<pre><code>    %hash = (
              'key1' =&gt; {
                          'key2' =&gt; {}
                        }
            );
</code></pre>
<p> That&#8217;s autovivification. You can get around this in a few ways. The easiest way is to just turn it off. The lexical <code>&quot;autovivification&quot;</code> pragma is available on <font SIZE="-1">CPAN.</font> Now you don&#8217;t add to the hash: </p>
<pre><code>    {
        no autovivification;
        my %hash;
        if( exists $hash{key1}{key2}{key3} ) {
            ...;
        }
    }
</code></pre>
<p> The Data::Diver module on <font SIZE="-1">CPAN</font> can do it for you too. Its <code>&quot;Dive&quot;</code> subroutine can tell you not only if the keys exist but also get the value: </p>
<pre><code>    use Data::Diver qw(Dive);
    my @exists = Dive( \%hash, qw(key1 key2 key3) );
    if( ! @exists ) {
        ...; # keys do not exist
    }
    elsif( ! defined $exists[0] ) {
        ...; # keys exist but value is undef
    }
</code></pre>
<p> You can easily do this yourself too by checking each level of the hash before you move onto the next level. This is essentially what Data::Diver does for you: </p>
<pre><code>    if( check_hash( \%hash, qw(key1 key2 key3) ) ) {
        ...;
    }
    sub check_hash {
       my( $hash, @keys ) = @_;
       return unless @keys;
       foreach my $key ( @keys ) {
           return unless eval { exists $hash-&gt;{$key} };
           $hash = $hash-&gt;{$key};
        }
       return 1;
    }
</code></pre>
<h3>How can I prevent addition of unwanted keys into a hash?</h3>
<p> Since version 5.8.0, hashes can be <i>restricted</i> to a fixed number of given keys. Methods for creating and dealing with restricted hashes are exported by the Hash::Util module.  </p>
<h2>Data: Misc</h2>
<h3>How do I handle binary data correctly?</h3>
<p> Perl is binary-clean, so it can handle binary data just fine. On Windows or <font SIZE="-1">DOS,</font> however, you have to use <code>&quot;binmode&quot;</code> for binary files to avoid conversions for line endings. In general, you should use <code>&quot;binmode&quot;</code> any time you want to work with binary data. </p>
<p> Also see ``binmode&#8217;&#8216; in perlfunc or perlopentut. </p>
<p> If you&#8217;re concerned about 8-bit textual data then see perllocale. If you want to deal with multibyte characters, however, there are some gotchas. See the section on Regular Expressions.  </p>
<h3>How do I determine whether a scalar is a number/whole/integer/float?</h3>
<p> Assuming that you don&#8217;t care about <font SIZE="-1">IEEE</font> notations like ``NaN&#8217;&#8216; or ``Infinity&#8217;&#8216;, you probably just want to use a regular expression (see also perlretut and perlre): </p>
<pre><code>    use 5.010;
    if ( /\D/ )
        { say &quot;\thas nondigits&quot;; }
    if ( /^\d+\z/ )
        { say &quot;\tis a whole number&quot;; }
    if ( /^-?\d+\z/ )
        { say &quot;\tis an integer&quot;; }
    if ( /^[+-]?\d+\z/ )
        { say &quot;\tis a +/- integer&quot;; }
    if ( /^-?(?:\d+\.?|\.\d)\d*\z/ )
        { say &quot;\tis a real number&quot;; }
    if ( /^[+-]?(?=\.?\d)\d*\.?\d*(?:e[+-]?\d+)?\z/i )
        { say &quot;\tis a C float&quot; }
</code></pre>
<p> There are also some commonly used modules for the task. Scalar::Util (distributed with 5.8) provides access to perl&#8217;s internal function <code>&quot;looks_like_number&quot;</code> for determining whether a variable looks like a number. Data::Types exports functions that validate data types using both the above and other regular expressions. Thirdly, there is Regexp::Common which has regular expressions to match various types of numbers. Those three modules are available from the <font SIZE="-1">CPAN.</font> </p>
<p> If you&#8217;re on a <font SIZE="-1">POSIX</font> system, Perl supports the <code>&quot;POSIX::strtod&quot;</code> function for converting strings to doubles (and also <code>&quot;POSIX::strtol&quot;</code> for longs). Its semantics are somewhat cumbersome, so here&#8217;s a <code>&quot;getnum&quot;</code> wrapper function for more convenient access. This function takes a string and returns the number it found, or <code>&quot;undef&quot;</code> for input that isn&#8217;t a C float. The <code>&quot;is_numeric&quot;</code> function is a front end to <code>&quot;getnum&quot;</code> if you just want to say, ``Is this a float?&#8216;&#8216; </p>
<pre><code>    sub getnum {
        use POSIX qw(strtod);
        my $str = shift;
        $str =~ s/^\s+//;
        $str =~ s/\s+$//;
        $! = 0;
        my($num, $unparsed) = strtod($str);
        if (($str eq '') || ($unparsed != 0) || $!) {
                return undef;
        }
        else {
            return $num;
        }
    }
    sub is_numeric { defined getnum($_[0]) }
</code></pre>
<p> Or you could check out the String::Scanf module on the <font SIZE="-1">CPAN</font> instead.  </p>
<h3>How do I keep persistent data across program calls?</h3>
<p> For some specific applications, you can use one of the <font SIZE="-1">DBM</font> modules. See AnyDBM_File. More generically, you should consult the FreezeThaw or Storable modules from <font SIZE="-1">CPAN.</font> Starting from Perl 5.8, Storable is part of the standard distribution. Here&#8217;s one example using Storable&#8217;s <code>&quot;store&quot;</code> and <code>&quot;retrieve&quot;</code> functions: </p>
<pre><code>    use Storable;
    store(\%hash, &quot;filename&quot;);
    # later on...
    $href = retrieve(&quot;filename&quot;); # by ref
    %hash = %{ retrieve(&quot;filename&quot;) }; # direct to hash
</code></pre>
<h3>How do I print out or copy a recursive data structure?</h3>
<p> The Data::Dumper module on <font SIZE="-1">CPAN</font> (or the 5.005 release of Perl) is great for printing out data structures. The Storable module on <font SIZE="-1">CPAN</font> (or the 5.8 release of Perl), provides a function called <code>&quot;dclone&quot;</code> that recursively copies its argument. </p>
<pre><code>    use Storable qw(dclone);
    $r2 = dclone($r1);
</code></pre>
<p> Where <code>$r1</code> can be a reference to any kind of data structure you&#8217;d like. It will be deeply copied. Because <code>&quot;dclone&quot;</code> takes and returns references, you&#8217;d have to add extra punctuation if you had a hash of arrays that you wanted to copy. </p>
<pre><code>    %newhash = %{ dclone(\%oldhash) };
</code></pre>
<h3>How do I define methods for every class/object?</h3>
<p> (contributed by Ben Morrow) </p>
<p> You can use the <code>&quot;UNIVERSAL&quot;</code> class (see <font SIZE="-1">UNIVERSAL</font>). However, please be very careful to consider the consequences of doing this: adding methods to every object is very likely to have unintended consequences. If possible, it would be better to have all your object inherit from some common base class, or to use an object system like Moose that supports roles.  </p>
<h3>How do I verify a credit card checksum?</h3>
<p> Get the Business::CreditCard module from <font SIZE="-1">CPAN.</font>  </p>
<font SIZE="-1"></font><h3>How do I pack arrays of doubles or floats for XS code?</h3>
<p> The arrays.h/arrays.c code in the <font SIZE="-1">PGPLOT</font> module on <font SIZE="-1">CPAN</font> does just this. If you&#8217;re doing a lot of float or double processing, consider using the <font SIZE="-1">PDL</font> module from <font SIZE="-1">CPAN</font> instead---it makes number-crunching easy. </p>
<p> See &lt;<a rel="nofollow" href="https://metacpan.org/release/PGPLOT">https://metacpan.org/release/PGPLOT</a>&gt; for the code.  </p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples in this file are hereby placed into the public domain. You are permitted and encouraged to use this code in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit would be courteous but is not required. </p>
