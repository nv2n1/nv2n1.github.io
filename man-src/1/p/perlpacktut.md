---
title: "perlpacktut(1)"
name: "perlpacktut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlpacktut/"
---

<h2 class="name">NAME</h2>
 

 perlpacktut - tutorial on &quot;pack&quot; and &quot;unpack&quot; 

<h2>DESCRIPTION</h2>

 <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> are two functions for transforming data according to a user-defined template, between the guarded way Perl stores values and some well-defined representation as might be required in the environment of a Perl program. Unfortunately, they're also two of the most misunderstood and most often overlooked functions that Perl provides. This tutorial will demystify them for you.

<h2>The Basic Principle</h2>

 Most programming languages don't shelter the memory where variables are stored. In C, for instance, you can take the address of some variable, and the <tt>&quot;sizeof&quot;</tt> operator tells you how many bytes are allocated to the variable. Using the address and the size, you may access the storage to your heart's content. 

 In Perl, you just can't access memory at random, but the structural and representational conversion provided by <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> is an excellent alternative. The <tt>&quot;pack&quot;</tt> function converts values to a byte sequence containing representations according to a given specification, the so-called ``template'' argument. <tt>&quot;unpack&quot;</tt> is the reverse process, deriving some values from the contents of a string of bytes. (Be cautioned, however, that not all that has been packed together can be neatly unpacked - a very common experience as seasoned travellers are likely to confirm.) 

 Why, you may ask, would you need a chunk of memory containing some values in binary representation? One good reason is input and output accessing some file, a device, or a network connection, whereby this binary representation is either forced on you or will give you some benefit in processing. Another cause is passing data to some system call that is not available as a Perl function: <tt>&quot;syscall&quot;</tt> requires you to provide parameters stored in the way it happens in a C program. Even text processing (as shown in the next section) may be simplified with judicious usage of these two functions. 

 To see how (un)packing works, we'll start with a simple template code where the conversion is in low gear: between the contents of a byte sequence and a string of hexadecimal digits. Let's use <tt>&quot;unpack&quot;</tt>, since this is likely to remind you of a dump program, or some desperate last message unfortunate programs are wont to throw at you before they expire into the wild blue yonder. Assuming that the variable <tt>$mem</tt> holds a sequence of bytes that we'd like to inspect without assuming anything about its meaning, we can write 

 <pre><code>
my($hex) = unpack('H*', $mem);
print "$hex\n";
</code></pre> 

 whereupon we might see something like this, with each pair of hex digits corresponding to a byte: 

 <pre>
   41204d414e204120504c414e20412043414e414c2050414e414d41
</pre> 

 What was in this chunk of memory? Numbers, characters, or a mixture of both? Assuming that we're on a computer where <font SIZE="-1">ASCII</font> (or some similar) encoding is used: hexadecimal values in the range <tt>0x40</tt> - <tt>0x5A</tt> indicate an uppercase letter, and <tt>0x20</tt> encodes a space. So we might assume it is a piece of text, which some are able to read like a tabloid; but others will have to get hold of an <font SIZE="-1">ASCII</font> table and relive that firstgrader feeling. Not caring too much about which way to read this, we note that <tt>&quot;unpack&quot;</tt> with the template code <tt>&quot;H&quot;</tt> converts the contents of a sequence of bytes into the customary hexadecimal notation. Since ``a sequence of'' is a pretty vague indication of quantity, <tt>&quot;H&quot;</tt> has been defined to convert just a single hexadecimal digit unless it is followed by a repeat count. An asterisk for the repeat count means to use whatever remains. 

 The inverse operation - packing byte contents from a string of hexadecimal digits - is just as easily written. For instance: 

 
my $s = pack('H2' x 10, 30..39);
print "$s\n";
 

 Since we feed a list of ten 2-digit hexadecimal strings to <tt>&quot;pack&quot;</tt>, the pack template should contain ten pack codes. If this is run on a computer with <font SIZE="-1">ASCII</font> character coding, it will print <tt>0123456789</tt>.

<h2>Packing Text</h2>

 Let's suppose you've got to read in a data file like this: 

 <pre>
    Date      |Description                | Income|Expenditure
    01/24/2001 Zed's Camel Emporium                    1147.99
    01/28/2001 Flea spray                                24.99
    01/29/2001 Camel rides to tourists      235.00
</pre> 

 How do we do it? You might think first to use <tt>&quot;split&quot;</tt>; however, since <tt>&quot;split&quot;</tt> collapses blank fields, you'll never know whether a record was income or expenditure. Oops. Well, you could always use <tt>&quot;substr&quot;</tt>: 

 
while (&lt;&gt;) {
    my $date = substr($_, 0, 11);
    my $desc = substr($_, 12, 27);
    my $income = substr($_, 40, 7);
    my $expend = substr($_, 52, 7);
    ...
}
 

 It's not really a barrel of laughs, is it? In fact, it's worse than it may seem; the eagle-eyed may notice that the first field should only be 10 characters wide, and the error has propagated right through the other numbers - which we've had to count by hand. So it's error-prone as well as horribly unfriendly. 

 Or maybe we could use regular expressions: 

 
while (&lt;&gt;) {
    my($date, $desc, $income, $expend) =
        m | (\d\d /\d\d /\d{4})(.{27})(.{7})(.*) |
        ;
    ...
}
 

 Urgh. Well, it's a bit better, but - well, would you want to maintain that? 

 Hey, isn't Perl supposed to make this sort of thing easy? Well, it does, if you use the right tools. <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> are designed to help you out when dealing with fixed-width data like the above. Let's have a look at a solution with <tt>&quot;unpack&quot;</tt>: 

 
while (&lt;&gt;) {
    my($date, $desc, $income, $expend) = unpack("A10xA27xA7A*", $_);
    ...
}
 

 That looks a bit nicer; but we've got to take apart that weird template. Where did I pull that out of? 

 <font SIZE="-1">OK,</font> let's have a look at some of our data again; in fact, we'll include the headers, and a handy ruler so we can keep track of where we are. 

 <pre>
             1         2         3         4         5        
    1234567890123456789012345678901234567890123456789012345678
    Date      |Description                | Income|Expenditure
    01/28/2001 Flea spray                                24.99
    01/29/2001 Camel rides to tourists      235.00
</pre> 

 From this, we can see that the date column stretches from column 1 to column 10 - ten characters wide. The <tt>&quot;pack&quot;</tt>-ese for ``character'' is <tt>&quot;A&quot;</tt>, and ten of them are <tt>&quot;A10&quot;</tt>. So if we just wanted to extract the dates, we could say this: 

 <pre>
    my($date) = unpack(&quot;A10&quot;, $_);
</pre> 

 <font SIZE="-1">OK,</font> what's next? Between the date and the description is a blank column; we want to skip over that. The <tt>&quot;x&quot;</tt> template means ``skip forward'', so we want one of those. Next, we have another batch of characters, from 12 to 38. That's 27 more characters, hence <tt>&quot;A27&quot;</tt>. (Don't make the fencepost error - there are 27 characters between 12 and 38, not 26. Count 'em!) 

 Now we skip another character and pick up the next 7 characters: 

 <pre>
    my($date,$description,$income) = unpack(&quot;A10xA27xA7&quot;, $_);
</pre> 

 Now comes the clever bit. Lines in our ledger which are just income and not expenditure might end at column 46. Hence, we don't want to tell our <tt>&quot;unpack&quot;</tt> pattern that we <b>need</b> to find another 12 characters; we'll just say ``if there's anything left, take it''. As you might guess from regular expressions, that's what the <tt>&quot;*&quot;</tt> means: ``use everything remaining''.
<dl>
<dt>&bull;
<dd> Be warned, though, that unlike regular expressions, if the <tt>&quot;unpack&quot;</tt> template doesn't match the incoming data, Perl will scream and die.</dl>
 

 Hence, putting it all together: 

 <pre>
    my ($date, $description, $income, $expend) =
        unpack(&quot;A10xA27xA7xA*&quot;, $_);
</pre> 

 Now, that's our data parsed. I suppose what we might want to do now is total up our income and expenditure, and add another line to the end of our ledger - in the same format - saying how much we've brought in and how much we've spent: 

 
while (&lt;&gt;) {
    my($date, $desc, $income, $expend) =
        unpack("A10xA27xA7xA*", $_);
    $tot_income += $income;
    $tot_expend += $expend;
}
$tot_income = sprintf("%.2f", $tot_income);
#Get them into
    $tot_expend = sprintf("%.2f", $tot_expend);
#"financial" format $date = POSIX::strftime("%m/%d/%Y", localtime);
#OK, let's go:
print pack("A10xA27xA7xA*", $date, "Totals",
           $tot_income, $tot_expend);
 

 Oh, hmm. That didn't quite work. Let's see what happened: 

 <pre>
    01/24/2001 Zed's Camel Emporium                     1147.99
    01/28/2001 Flea spray                                 24.99
    01/29/2001 Camel rides to tourists     1235.00
    03/23/2001Totals                     1235.001172.98
</pre> 

 <font SIZE="-1">OK,</font> it's a start, but what happened to the spaces? We put <tt>&quot;x&quot;</tt>, didn't we? Shouldn't it skip forward? Let's look at what ``pack'' in perlfunc says: 

 <pre>
    x   A null byte.
</pre> 

 Urgh. No wonder. There's a big difference between ``a null byte'', character zero, and ``a space'', character 32. Perl's put something between the date and the description - but unfortunately, we can't see it! 

 What we actually need to do is expand the width of the fields. The <tt>&quot;A&quot;</tt> format pads any non-existent characters with spaces, so we can use the additional spaces to line up our fields, like this: 

 <pre>
    print pack(&quot;A11 A28 A8 A*&quot;, $date, &quot;Totals&quot;,
        $tot_income, $tot_expend);
</pre> 

 (Note that you can put spaces in the template to make it more readable, but they don't translate to spaces in the output.) Here's what we got this time: 

 <pre>
    01/24/2001 Zed's Camel Emporium                     1147.99
    01/28/2001 Flea spray                                 24.99
    01/29/2001 Camel rides to tourists     1235.00
    03/23/2001 Totals                      1235.00 1172.98
</pre> 

 That's a bit better, but we still have that last column which needs to be moved further over. There's an easy way to fix this up: unfortunately, we can't get <tt>&quot;pack&quot;</tt> to right-justify our fields, but we can get <tt>&quot;sprintf&quot;</tt> to do it: 

 
$tot_income = sprintf("%.2f", $tot_income);
$tot_expend = sprintf("%12.2f", $tot_expend);
$date = POSIX::strftime("%m/%d/%Y", localtime);
print pack("A11 A28 A8 A*", $date, "Totals",
           $tot_income, $tot_expend);
 

 This time we get the right answer: 

 <pre>
    01/28/2001 Flea spray                                 24.99
    01/29/2001 Camel rides to tourists     1235.00
    03/23/2001 Totals                      1235.00      1172.98
</pre> 

 So that's how we consume and produce fixed-width data. Let's recap what we've seen of <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> so far:
<dl>
<dt>&bull;
<dd> Use <tt>&quot;pack&quot;</tt> to go from several pieces of data to one fixed-width version; use <tt>&quot;unpack&quot;</tt> to turn a fixed-width-format string into several pieces of data.
<dt>&bull;
<dd> The pack format <tt>&quot;A&quot;</tt> means ``any character''; if you're <tt>&quot;pack&quot;</tt>ing and you've run out of things to pack, <tt>&quot;pack&quot;</tt> will fill the rest up with spaces.
<dt>&bull;
<dd> <tt>&quot;x&quot;</tt> means ``skip a byte'' when <tt>&quot;unpack&quot;</tt>ing; when <tt>&quot;pack&quot;</tt>ing, it means ``introduce a null byte'' - that's probably not what you mean if you're dealing with plain text.
<dt>&bull;
<dd> You can follow the formats with numbers to say how many characters should be affected by that format: <tt>&quot;A12&quot;</tt> means ``take 12 characters''; <tt>&quot;x6&quot;</tt> means ``skip 6 bytes'' or ``character 0, 6 times''.
<dt>&bull;
<dd> Instead of a number, you can use <tt>&quot;*&quot;</tt> to mean ``consume everything else left''. 

 <b>Warning</b>: when packing multiple pieces of data, <tt>&quot;*&quot;</tt> only means ``consume all of the current piece of data''. That's to say 

 <pre>
    pack(&quot;A*A*&quot;, $one, $two)
</pre> 

 packs all of <tt>$one</tt> into the first <tt>&quot;A*&quot;</tt> and then all of <tt>$two</tt> into the second. This is a general principle: each format character corresponds to one piece of data to be <tt>&quot;pack&quot;</tt>ed.</dl>

<h2>Packing Numbers</h2>

 So much for textual data. Let's get onto the meaty stuff that <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> are best at: handling binary formats for numbers. There is, of course, not just one binary format - life would be too simple - but Perl will do all the finicky labor for you.

<h3>Integers</h3>

 Packing and unpacking numbers implies conversion to and from some <i>specific</i> binary representation. Leaving floating point numbers aside for the moment, the salient properties of any such representation are:
<dl>
<dt>&bull;
<dd> the number of bytes used for storing the integer,
<dt>&bull;
<dd> whether the contents are interpreted as a signed or unsigned number,
<dt>&bull;
<dd> the byte ordering: whether the first byte is the least or most significant byte (or: little-endian or big-endian, respectively).</dl>
 

 So, for instance, to pack 20302 to a signed 16 bit integer in your computer's representation you write 

 <pre>
   my $ps = pack( 's', 20302 );
</pre> 

 Again, the result is a string, now containing 2 bytes. If you print this string (which is, generally, not recommended) you might see <tt>&quot;ON&quot;</tt> or <tt>&quot;NO&quot;</tt> (depending on your system's byte ordering) - or something entirely different if your computer doesn't use <font SIZE="-1">ASCII</font> character encoding. Unpacking <tt>$ps</tt> with the same template returns the original integer value: 

 <pre>
   my( $s ) = unpack( 's', $ps );
</pre> 

 This is true for all numeric template codes. But don't expect miracles: if the packed value exceeds the allotted byte capacity, high order bits are silently discarded, and unpack certainly won't be able to pull them back out of some magic hat. And, when you pack using a signed template code such as <tt>&quot;s&quot;</tt>, an excess value may result in the sign bit getting set, and unpacking this will smartly return a negative value. 

 16 bits won't get you too far with integers, but there is <tt>&quot;l&quot;</tt> and <tt>&quot;L&quot;</tt> for signed and unsigned 32-bit integers. And if this is not enough and your system supports 64 bit integers you can push the limits much closer to infinity with pack codes <tt>&quot;q&quot;</tt> and <tt>&quot;Q&quot;</tt>. A notable exception is provided by pack codes <tt>&quot;i&quot;</tt> and <tt>&quot;I&quot;</tt> for signed and unsigned integers of the ``local custom'' variety: Such an integer will take up as many bytes as a local C compiler returns for <tt>&quot;sizeof(int)&quot;</tt>, but it'll use <i>at least</i> 32 bits. 

 Each of the integer pack codes <tt>&quot;sSlLqQ&quot;</tt> results in a fixed number of bytes, no matter where you execute your program. This may be useful for some applications, but it does not provide for a portable way to pass data structures between Perl and C programs (bound to happen when you call <font SIZE="-1">XS</font> extensions or the Perl function <tt>&quot;syscall&quot;</tt>), or when you read or write binary files. What you'll need in this case are template codes that depend on what your local C compiler compiles when you code <tt>&quot;short&quot;</tt> or <tt>&quot;unsigned long&quot;</tt>, for instance. These codes and their corresponding byte lengths are shown in the table below. Since the C standard leaves much leeway with respect to the relative sizes of these data types, actual values may vary, and that's why the values are given as expressions in C and Perl. (If you'd like to use values from <tt>%Config</tt> in your program you have to import it with <tt>&quot;use Config&quot;</tt>.) 

 
signed unsigned byte length in C byte length in Perl
    s !S !sizeof(short) $Config{shortsize} i !I !sizeof(int) $Config{intsize} l !L !sizeof(long) $Config{longsize} q !Q !sizeof(long long) $Config
{
    longlongsize
}
 

 The <tt>&quot;i!&quot;</tt> and <tt>&quot;I!&quot;</tt> codes aren't different from <tt>&quot;i&quot;</tt> and <tt>&quot;I&quot;</tt>; they are tolerated for completeness' sake.

<h3>Unpacking a Stack Frame</h3>

 Requesting a particular byte ordering may be necessary when you work with binary data coming from some specific architecture whereas your program could run on a totally different system. As an example, assume you have 24 bytes containing a stack frame as it happens on an Intel 8086: 

 
+ -- -- -- -- -+ +-- --+-- --+ +-- -- -- -- -+
    TOS: | IP | TOS +
      4: | FL | FH | FLAGS TOS + 14: | SI |
                                     +-- -- -- -- -+ +-- --+-- --+ +-- -- -- -- -+ | CS | | AL | AH | AX | DI |
                                     +-- -- -- -- -+ +-- --+-- --+ +-- -- -- -- -+ | BL | BH | BX | BP |
                                     +-- --+-- --+ +-- -- -- -- -+ | CL | CH | CX | DS |
                                     +-- --+-- --+ +-- -- -- -- -+ | DL | DH | DX | ES |
                                     +-- --+-- --+ +-- -- -- -- -+
 

 First, we note that this time-honored 16-bit <font SIZE="-1">CPU</font> uses little-endian order, and that's why the low order byte is stored at the lower address. To unpack such a (unsigned) short we'll have to use code <tt>&quot;v&quot;</tt>. A repeat count unpacks all 12 shorts: 

 <pre>
   my( $ip, $cs, $flags, $ax, $bx, $cd, $dx, $si, $di, $bp, $ds, $es ) =
     unpack( 'v12', $frame );
</pre> 

 Alternatively, we could have used <tt>&quot;C&quot;</tt> to unpack the individually accessible byte registers <font SIZE="-1">FL, FH, AL, AH,</font> etc.: 

 <pre>
   my( $fl, $fh, $al, $ah, $bl, $bh, $cl, $ch, $dl, $dh ) =
     unpack( 'C10', substr( $frame, 4, 10 ) );
</pre> 

 It would be nice if we could do this in one fell swoop: unpack a short, back up a little, and then unpack 2 bytes. Since Perl <i>is</i> nice, it proffers the template code <tt>&quot;X&quot;</tt> to back up one byte. Putting this all together, we may now write: 

 <pre>
   my( $ip, $cs,
       $flags,$fl,$fh,
       $ax,$al,$ah, $bx,$bl,$bh, $cx,$cl,$ch, $dx,$dl,$dh, 
       $si, $di, $bp, $ds, $es ) =
   unpack( 'v2' . ('vXXCC' x 5) . 'v5', $frame );
</pre> 

 (The clumsy construction of the template can be avoided - just read on!) 

 We've taken some pains to construct the template so that it matches the contents of our frame buffer. Otherwise we'd either get undefined values, or <tt>&quot;unpack&quot;</tt> could not unpack all. If <tt>&quot;pack&quot;</tt> runs out of items, it will supply null strings (which are coerced into zeroes whenever the pack code says so).

<h3>How to Eat an Egg on a Net</h3>

 The pack code for big-endian (high order byte at the lowest address) is <tt>&quot;n&quot;</tt> for 16 bit and <tt>&quot;N&quot;</tt> for 32 bit integers. You use these codes if you know that your data comes from a compliant architecture, but, surprisingly enough, you should also use these pack codes if you exchange binary data, across the network, with some system that you know next to nothing about. The simple reason is that this order has been chosen as the <i>network order</i>, and all standard-fearing programs ought to follow this convention. (This is, of course, a stern backing for one of the Lilliputian parties and may well influence the political development there.) So, if the protocol expects you to send a message by sending the length first, followed by just so many bytes, you could write: 

 <pre>
   my $buf = pack( 'N', length( $msg ) ) . $msg;
</pre> 

 or even: 

 <pre>
   my $buf = pack( 'NA*', length( $msg ), $msg );
</pre> 

 and pass <tt>$buf</tt> to your send routine. Some protocols demand that the count should include the length of the count itself: then just add 4 to the data length. (But make sure to read ``Lengths and Widths'' before you really code this!)

<h3>Byte-order modifiers</h3>

 In the previous sections we've learned how to use <tt>&quot;n&quot;</tt>, <tt>&quot;N&quot;</tt>, <tt>&quot;v&quot;</tt> and <tt>&quot;V&quot;</tt> to pack and unpack integers with big- or little-endian byte-order. While this is nice, it's still rather limited because it leaves out all kinds of signed integers as well as 64-bit integers. For example, if you wanted to unpack a sequence of signed big-endian 16-bit integers in a platform-independent way, you would have to write: 

 <pre>
   my @data = unpack 's*', pack 'S*', unpack 'n*', $buf;
</pre> 

 This is ugly. As of Perl 5.9.2, there's a much nicer way to express your desire for a certain byte-order: the <tt>&quot;&gt;&quot;</tt> and <tt>&quot;&lt;&quot;</tt> modifiers. <tt>&quot;&gt;&quot;</tt> is the big-endian modifier, while <tt>&quot;&lt;&quot;</tt> is the little-endian modifier. Using them, we could rewrite the above code as: 

 <pre>
   my @data = unpack 's&gt;*', $buf;
</pre> 

 As you can see, the ``big end'' of the arrow touches the <tt>&quot;s&quot;</tt>, which is a nice way to remember that <tt>&quot;&gt;&quot;</tt> is the big-endian modifier. The same obviously works for <tt>&quot;&lt;&quot;</tt>, where the ``little end'' touches the code. 

 You will probably find these modifiers even more useful if you have to deal with big- or little-endian C structures. Be sure to read ``Packing and Unpacking C Structures'' for more on that.

<h3>Floating point Numbers</h3>

 For packing floating point numbers you have the choice between the pack codes <tt>&quot;f&quot;</tt>, <tt>&quot;d&quot;</tt>, <tt>&quot;F&quot;</tt> and <tt>&quot;D&quot;</tt>. <tt>&quot;f&quot;</tt> and <tt>&quot;d&quot;</tt> pack into (or unpack from) single-precision or double-precision representation as it is provided by your system. If your systems supports it, <tt>&quot;D&quot;</tt> can be used to pack and unpack (<tt>&quot;long double&quot;</tt>) values, which can offer even more resolution than <tt>&quot;f&quot;</tt> or <tt>&quot;d&quot;</tt>. <b>Note that there are different long double formats.</b> 

 <tt>&quot;F&quot;</tt> packs an <tt>&quot;NV&quot;</tt>, which is the floating point type used by Perl internally. 

 There is no such thing as a network representation for reals, so if you want to send your real numbers across computer boundaries, you'd better stick to text representation, possibly using the hexadecimal float format (avoiding the decimal conversion loss), unless you're absolutely sure what's on the other end of the line. For the even more adventuresome, you can use the byte-order modifiers from the previous section also on floating point codes.

<h2>Exotic Templates</h2>

<h3>Bit Strings</h3>

 Bits are the atoms in the memory world. Access to individual bits may have to be used either as a last resort or because it is the most convenient way to handle your data. Bit string (un)packing converts between strings containing a series of <tt>0</tt> and <tt>1</tt> characters and a sequence of bytes each containing a group of 8 bits. This is almost as simple as it sounds, except that there are two ways the contents of a byte may be written as a bit string. Let's have a look at an annotated byte: 

 
7 6 5 4 3 2 1 0 + -- -- -- -- -- -- -- -- -+ | 1 0 0 0 1 1 0 0 |
    +-- -- -- -- -- -- -- -- -+MSB LSB
 

 It's egg-eating all over again: Some think that as a bit string this should be written ``10001100'' i.e. beginning with the most significant bit, others insist on ``00110001''. Well, Perl isn't biased, so that's why we have two bit string codes: 

 
$byte = pack('B8', '10001100');
#start with MSB
    $byte = pack('b8', '00110001');
#start with LSB
 

 It is not possible to pack or unpack bit fields - just integral bytes. <tt>&quot;pack&quot;</tt> always starts at the next byte boundary and ``rounds up'' to the next multiple of 8 by adding zero bits as required. (If you do want bit fields, there is ``vec'' in perlfunc. Or you could implement bit field handling at the character string level, using split, substr, and concatenation on unpacked bit strings.) 

 To illustrate unpacking for bit strings, we'll decompose a simple status register (a ``-'' stands for a ``reserved'' bit): 

 
+ -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -+ | S Z - A - P - C | - - - -O D I T |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -+MSB LSB MSB LSB
 

 Converting these two bytes to a string can be done with the unpack template <tt>'b16'</tt>. To obtain the individual bit values from the bit string we use <tt>&quot;split&quot;</tt> with the ``empty'' separator pattern which dissects into individual characters. Bit values from the ``reserved'' positions are simply assigned to <tt>&quot;undef&quot;</tt>, a convenient notation for ``I don't care where this goes''. 

 <pre>
   ($carry, undef, $parity, undef, $auxcarry, undef, $zero, $sign,
    $trace, $interrupt, $direction, $overflow) =
      split( //, unpack( 'b16', $status ) );
</pre> 

 We could have used an unpack template <tt>'b12'</tt> just as well, since the last 4 bits can be ignored anyway.

<h3>Uuencoding</h3>

 Another odd-man-out in the template alphabet is <tt>&quot;u&quot;</tt>, which packs a ``uuencoded string''. (``uu'' is short for Unix-to-Unix.) Chances are that you won't ever need this encoding technique which was invented to overcome the shortcomings of old-fashioned transmission mediums that do not support other than simple <font SIZE="-1">ASCII</font> data. The essential recipe is simple: Take three bytes, or 24 bits. Split them into 4 six-packs, adding a space (0x20) to each. Repeat until all of the data is blended. Fold groups of 4 bytes into lines no longer than 60 and garnish them in front with the original byte count (incremented by 0x20) and a <tt>&quot;\n&quot;</tt> at the end. - The <tt>&quot;pack&quot;</tt> chef will prepare this for you, a la minute, when you select pack code <tt>&quot;u&quot;</tt> on the menu: 

 <pre>
   my $uubuf = pack( 'u', $bindat );
</pre> 

 A repeat count after <tt>&quot;u&quot;</tt> sets the number of bytes to put into an uuencoded line, which is the maximum of 45 by default, but could be set to some (smaller) integer multiple of three. <tt>&quot;unpack&quot;</tt> simply ignores the repeat count.

<h3>Doing Sums</h3>

 An even stranger template code is <tt>&quot;%&quot;</tt>&lt;<i>number</i>&gt;. First, because it's used as a prefix to some other template code. Second, because it cannot be used in <tt>&quot;pack&quot;</tt> at all, and third, in <tt>&quot;unpack&quot;</tt>, doesn't return the data as defined by the template code it precedes. Instead it'll give you an integer of <i>number</i> bits that is computed from the data value by doing sums. For numeric unpack codes, no big feat is achieved: 

 
my $buf = pack('iii', 100, 20, 3);
print unpack('%32i3', $buf), "\n";
#prints 123
 

 For string values, <tt>&quot;%&quot;</tt> returns the sum of the byte values saving you the trouble of a sum loop with <tt>&quot;substr&quot;</tt> and <tt>&quot;ord&quot;</tt>: 

 <pre>
    print unpack( '%32A*', &quot;\x01\x10&quot; ), &quot;\n&quot;;  # prints 17
</pre> 

 Although the <tt>&quot;%&quot;</tt> code is documented as returning a ``checksum'': don't put your trust in such values! Even when applied to a small number of bytes, they won't guarantee a noticeable Hamming distance. 

 In connection with <tt>&quot;b&quot;</tt> or <tt>&quot;B&quot;</tt>, <tt>&quot;%&quot;</tt> simply adds bits, and this can be put to good use to count set bits efficiently: 

 <pre>
    my $bitcount = unpack( '%32b*', $mask );
</pre> 

 And an even parity bit can be determined like this: 

 <pre>
    my $evenparity = unpack( '%1b*', $mask );
</pre>

<h3>Unicode</h3>

 Unicode is a character set that can represent most characters in most of the world's languages, providing room for over one million different characters. Unicode 3.1 specifies 94,140 characters: The Basic Latin characters are assigned to the numbers 0 - 127. The Latin-1 Supplement with characters that are used in several European languages is in the next range, up to 255. After some more Latin extensions we find the character sets from languages using non-Roman alphabets, interspersed with a variety of symbol sets such as currency symbols, Zapf Dingbats or Braille. (You might want to visit &lt;<a rel="nofollow" HREF="http://www.unicode.org/">http://www.unicode.org/</a>&gt; for a look at some of them - my personal favourites are Telugu and Kannada.) 

 The Unicode character sets associates characters with integers. Encoding these numbers in an equal number of bytes would more than double the requirements for storing texts written in Latin alphabets. The <font SIZE="-1">UTF-8</font> encoding avoids this by storing the most common (from a western point of view) characters in a single byte while encoding the rarer ones in three or more bytes. 

 Perl uses <font SIZE="-1">UTF-8,</font> internally, for most Unicode strings. 

 So what has this got to do with <tt>&quot;pack&quot;</tt>? Well, if you want to compose a Unicode string (that is internally encoded as <font SIZE="-1">UTF-8</font>), you can do so by using template code <tt>&quot;U&quot;</tt>. As an example, let's produce the Euro currency symbol (code number 0x20AC): 

 
$UTF8{Euro} = pack('U', 0x20AC);
#Equivalent to : $UTF8{Euro } = "\x{20ac}";
 

 Inspecting <tt>$UTF8{Euro}</tt> shows that it contains 3 bytes: ``\xe2\x82\xac''. However, it contains only 1 character, number 0x20AC. The round trip can be completed with <tt>&quot;unpack&quot;</tt>: 

 
$Unicode{Euro} = unpack('U', $UTF8{Euro});
 

 Unpacking using the <tt>&quot;U&quot;</tt> template code also works on <font SIZE="-1">UTF-8</font> encoded byte strings. 

 Usually you'll want to pack or unpack <font SIZE="-1">UTF-8</font> strings: 

 
#pack and unpack the Hebrew alphabet
my $alefbet = pack('U*', 0x05d0..0x05ea);
my @hebrew = unpack('U*', $utf);
 

 Please note: in the general case, you're better off using <tt>&quot;Encode::decode('UTF-8', $utf)&quot;</tt> to decode a <font SIZE="-1">UTF-8</font> encoded byte string to a Perl Unicode string, and <tt>&quot;Encode::encode('UTF-8', $str)&quot;</tt> to encode a Perl Unicode string to <font SIZE="-1">UTF-8</font> bytes. These functions provide means of handling invalid byte sequences and generally have a friendlier interface.

<h3>Another Portable Binary Encoding</h3>

 The pack code <tt>&quot;w&quot;</tt> has been added to support a portable binary data encoding scheme that goes way beyond simple integers. (Details can be found at &lt;<a rel="nofollow" HREF="http://Casbah.org/">http://Casbah.org/</a>&gt;, the Scarab project.) A <font SIZE="-1">BER</font> (Binary Encoded Representation) compressed unsigned integer stores base 128 digits, most significant digit first, with as few digits as possible. Bit eight (the high bit) is set on each byte except the last. There is no size limit to <font SIZE="-1">BER</font> encoding, but Perl won't go to extremes. 

 <pre>
   my $berbuf = pack( 'w*', 1, 128, 128+1, 128*128+127 );
</pre> 

 A hex dump of <tt>$berbuf</tt>, with spaces inserted at the right places, shows 01 8100 8101 81807F. Since the last byte is always less than 128, <tt>&quot;unpack&quot;</tt> knows where to stop.

<h2>Template Grouping</h2>

 Prior to Perl 5.8, repetitions of templates had to be made by <tt>&quot;x&quot;</tt>-multiplication of template strings. Now there is a better way as we may use the pack codes <tt>&quot;(&quot;</tt> and <tt>&quot;)&quot;</tt> combined with a repeat count. The <tt>&quot;unpack&quot;</tt> template from the Stack Frame example can simply be written like this: 

 <pre>
   unpack( 'v2 (vXXCC)5 v5', $frame )
</pre> 

 Let's explore this feature a little more. We'll begin with the equivalent of 

 <pre>
   join( '', map( substr( $_, 0, 1 ), @str ) )
</pre> 

 which returns a string consisting of the first character from each string. Using pack, we can write 

 <pre>
   pack( '(A)'.@str, @str )
</pre> 

 or, because a repeat count <tt>&quot;*&quot;</tt> means ``repeat as often as required'', simply 

 <pre>
   pack( '(A)*', @str )
</pre> 

 (Note that the template <tt>&quot;A*&quot;</tt> would only have packed <tt>$str[0]</tt> in full length.) 

 To pack dates stored as triplets ( day, month, year ) in an array <tt>@dates</tt> into a sequence of byte, byte, short integer we can write 

 <pre>
   $pd = pack( '(CCS)*', map( @$_, @dates ) );
</pre> 

 To swap pairs of characters in a string (with even length) one could use several techniques. First, let's use <tt>&quot;x&quot;</tt> and <tt>&quot;X&quot;</tt> to skip forward and back: 

 <pre>
   $s = pack( '(A)*', unpack( '(xAXXAx)*', $s ) );
</pre> 

 We can also use <tt>&quot;@&quot;</tt> to jump to an offset, with 0 being the position where we were when the last <tt>&quot;(&quot;</tt> was encountered: 

 <pre>
   $s = pack( '(A)*', unpack( '(@1A @0A @2)*', $s ) );
</pre> 

 Finally, there is also an entirely different approach by unpacking big endian shorts and packing them in the reverse byte order: 

 <pre>
   $s = pack( '(v)*', unpack( '(n)*', $s );
</pre>

<h2>Lengths and Widths</h2>

<h3>String Lengths</h3>

 In the previous section we've seen a network message that was constructed by prefixing the binary message length to the actual message. You'll find that packing a length followed by so many bytes of data is a frequently used recipe since appending a null byte won't work if a null byte may be part of the data. Here is an example where both techniques are used: after two null terminated strings with source and destination address, a Short Message (to a mobile phone) is sent after a length byte: 

 <pre>
   my $msg = pack( 'Z*Z*CA*', $src, $dst, length( $sm ), $sm );
</pre> 

 Unpacking this message can be done with the same template: 

 <pre>
   ( $src, $dst, $len, $sm ) = unpack( 'Z*Z*CA*', $msg );
</pre> 

 There's a subtle trap lurking in the offing: Adding another field after the Short Message (in variable <tt>$sm</tt>) is all right when packing, but this cannot be unpacked naively: 

 
#pack a message
my $msg = pack('Z*Z*CA*C', $src, $dst, length($sm), $sm, $prio);
#unpack fails - $prio remains undefined !
($src, $dst, $len, $sm, $prio) = unpack('Z*Z*CA*C', $msg);
 

 The pack code <tt>&quot;A*&quot;</tt> gobbles up all remaining bytes, and <tt>$prio</tt> remains undefined! Before we let disappointment dampen the morale: Perl's got the trump card to make this trick too, just a little further up the sleeve. Watch this: 

 
#pack a message : ASCIIZ, ASCIIZ, length / string, byte
my $msg = pack('Z* Z* C/A* C', $src, $dst, $sm, $prio);
#unpack
($src, $dst, $sm, $prio) = unpack('Z* Z* C/A* C', $msg);
 

 Combining two pack codes with a slash (<tt>&quot;/&quot;</tt>) associates them with a single value from the argument list. In <tt>&quot;pack&quot;</tt>, the length of the argument is taken and packed according to the first code while the argument itself is added after being converted with the template code after the slash. This saves us the trouble of inserting the <tt>&quot;length&quot;</tt> call, but it is in <tt>&quot;unpack&quot;</tt> where we really score: The value of the length byte marks the end of the string to be taken from the buffer. Since this combination doesn't make sense except when the second pack code isn't <tt>&quot;a*&quot;</tt>, <tt>&quot;A*&quot;</tt> or <tt>&quot;Z*&quot;</tt>, Perl won't let you. 

 The pack code preceding <tt>&quot;/&quot;</tt> may be anything that's fit to represent a number: All the numeric binary pack codes, and even text codes such as <tt>&quot;A4&quot;</tt> or <tt>&quot;Z*&quot;</tt>: 

 
#pack / unpack a string preceded by its length in ASCII
my $buf = pack('A4/A*', "Humpty-Dumpty");
#unpack $buf : '13  Humpty-Dumpty'
my $txt = unpack('A4/A*', $buf);
 

 <tt>&quot;/&quot;</tt> is not implemented in Perls before 5.6, so if your code is required to work on ancient Perls you'll need to <tt>&quot;unpack( 'Z* Z* C')&quot;</tt> to get the length, then use it to make a new unpack string. For example 

 
#pack a message : ASCIIZ, ASCIIZ, length, string, byte
#(5.005 compatible)
my $msg = pack('Z* Z* C A* C', $src, $dst, length $sm, $sm, $prio);
#unpack
(undef, undef, $len) = unpack('Z* Z* C', $msg);
($src, $dst, $sm, $prio) = unpack("Z* Z* x A$len C", $msg);
 

 But that second <tt>&quot;unpack&quot;</tt> is rushing ahead. It isn't using a simple literal string for the template. So maybe we should introduce...

<h3>Dynamic Templates</h3>

 So far, we've seen literals used as templates. If the list of pack items doesn't have fixed length, an expression constructing the template is required (whenever, for some reason, <tt>&quot;()*&quot;</tt> cannot be used). Here's an example: To store named string values in a way that can be conveniently parsed by a C program, we create a sequence of names and null terminated <font SIZE="-1">ASCII</font> strings, with <tt>&quot;=&quot;</tt> between the name and the value, followed by an additional delimiting null byte. Here's how: 

 <pre>
   my $env = pack( '(A*A*Z*)' . keys( %Env ) . 'C',
                   map( { ( $_, '=', $Env{$_} ) } keys( %Env ) ), 0 );
</pre> 

 Let's examine the cogs of this byte mill, one by one. There's the <tt>&quot;map&quot;</tt> call, creating the items we intend to stuff into the <tt>$env</tt> buffer: to each key (in <tt>$_</tt>) it adds the <tt>&quot;=&quot;</tt> separator and the hash entry value. Each triplet is packed with the template code sequence <tt>&quot;A*A*Z*&quot;</tt> that is repeated according to the number of keys. (Yes, that's what the <tt>&quot;keys&quot;</tt> function returns in scalar context.) To get the very last null byte, we add a <tt>0</tt> at the end of the <tt>&quot;pack&quot;</tt> list, to be packed with <tt>&quot;C&quot;</tt>. (Attentive readers may have noticed that we could have omitted the 0.) 

 For the reverse operation, we'll have to determine the number of items in the buffer before we can let <tt>&quot;unpack&quot;</tt> rip it apart: 

 <pre>
   my $n = $env =~ tr/\0// - 1;
   my %env = map( split( /=/, $_ ), unpack( &quot;(Z*)$n&quot;, $env ) );
</pre> 

 The <tt>&quot;tr&quot;</tt> counts the null bytes. The <tt>&quot;unpack&quot;</tt> call returns a list of name-value pairs each of which is taken apart in the <tt>&quot;map&quot;</tt> block.

<h3>Counting Repetitions</h3>

 Rather than storing a sentinel at the end of a data item (or a list of items), we could precede the data with a count. Again, we pack keys and values of a hash, preceding each with an unsigned short length count, and up front we store the number of pairs: 

 <pre>
   my $env = pack( 'S(S/A* S/A*)*', scalar keys( %Env ), %Env );
</pre> 

 This simplifies the reverse operation as the number of repetitions can be unpacked with the <tt>&quot;/&quot;</tt> code: 

 <pre>
   my %env = unpack( 'S/(S/A* S/A*)', $env );
</pre> 

 Note that this is one of the rare cases where you cannot use the same template for <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> because <tt>&quot;pack&quot;</tt> can't determine a repeat count for a <tt>&quot;()&quot;</tt>-group.

<h3>Intel <font SIZE="-1">HEX</font></h3>

 Intel <font SIZE="-1">HEX</font> is a file format for representing binary data, mostly for programming various chips, as a text file. (See &lt;<a rel="nofollow" HREF="http://en.wikipedia.org/wiki/.hex">http://en.wikipedia.org/wiki/.hex</a>&gt; for a detailed description, and &lt;<a rel="nofollow" HREF="http://en.wikipedia.org/wiki/SREC_(file_format)">http://en.wikipedia.org/wiki/SREC_(file_format)</a>&gt; for the Motorola S-record format, which can be unravelled using the same technique.) Each line begins with a colon (':') and is followed by a sequence of hexadecimal characters, specifying a byte count <i>n</i> (8 bit), an address (16 bit, big endian), a record type (8 bit), <i>n</i> data bytes and a checksum (8 bit) computed as the least significant byte of the two's complement sum of the preceding bytes. Example: <tt>&quot;:0300300002337A1E&quot;</tt>. 

 The first step of processing such a line is the conversion, to binary, of the hexadecimal data, to obtain the four fields, while checking the checksum. No surprise here: we'll start with a simple <tt>&quot;pack&quot;</tt> call to convert everything to binary: 

 <pre>
   my $binrec = pack( 'H*', substr( $hexrec, 1 ) );
</pre> 

 The resulting byte sequence is most convenient for checking the checksum. Don't slow your program down with a for loop adding the <tt>&quot;ord&quot;</tt> values of this string's bytes - the <tt>&quot;unpack&quot;</tt> code <tt>&quot;%&quot;</tt> is the thing to use for computing the 8-bit sum of all bytes, which must be equal to zero: 

 <pre>
   die unless unpack( &quot;%8C*&quot;, $binrec ) == 0;
</pre> 

 Finally, let's get those four fields. By now, you shouldn't have any problems with the first three fields - but how can we use the byte count of the data in the first field as a length for the data field? Here the codes <tt>&quot;x&quot;</tt> and <tt>&quot;X&quot;</tt> come to the rescue, as they permit jumping back and forth in the string to unpack. 

 <pre>
   my( $addr, $type, $data ) = unpack( &quot;x n C X4 C x3 /a&quot;, $bin );
</pre> 

 Code <tt>&quot;x&quot;</tt> skips a byte, since we don't need the count yet. Code <tt>&quot;n&quot;</tt> takes care of the 16-bit big-endian integer address, and <tt>&quot;C&quot;</tt> unpacks the record type. Being at offset 4, where the data begins, we need the count. <tt>&quot;X4&quot;</tt> brings us back to square one, which is the byte at offset 0. Now we pick up the count, and zoom forth to offset 4, where we are now fully furnished to extract the exact number of data bytes, leaving the trailing checksum byte alone.

<h2>Packing and Unpacking C Structures</h2>

 In previous sections we have seen how to pack numbers and character strings. If it were not for a couple of snags we could conclude this section right away with the terse remark that C structures don't contain anything else, and therefore you already know all there is to it. Sorry, no: read on, please. 

 If you have to deal with a lot of C structures, and don't want to hack all your template strings manually, you'll probably want to have a look at the <font SIZE="-1">CPAN</font> module <tt>&quot;Convert::Binary::C&quot;</tt>. Not only can it parse your C source directly, but it also has built-in support for all the odds and ends described further on in this section.

<h3>The Alignment Pit</h3>

 In the consideration of speed against memory requirements the balance has been tilted in favor of faster execution. This has influenced the way C compilers allocate memory for structures: On architectures where a 16-bit or 32-bit operand can be moved faster between places in memory, or to or from a <font SIZE="-1">CPU</font> register, if it is aligned at an even or multiple-of-four or even at a multiple-of eight address, a C compiler will give you this speed benefit by stuffing extra bytes into structures. If you don't cross the C shoreline this is not likely to cause you any grief (although you should care when you design large data structures, or you want your code to be portable between architectures (you do want that, don't you?)). 

 To see how this affects <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt>, we'll compare these two C structures: 

 
typedef struct {
    char c1;
    short s;
    char c2;
    long l;
} gappy_t;
typedef struct {
    long l;
    short s;
    char c1;
    char c2;
} dense_t;
 

 Typically, a C compiler allocates 12 bytes to a <tt>&quot;gappy_t&quot;</tt> variable, but requires only 8 bytes for a <tt>&quot;dense_t&quot;</tt>. After investigating this further, we can draw memory maps, showing where the extra 4 bytes are hidden: 

 
0 + 4 + 8 + 12 + --+--+--+--+--+--+--+--+--+--+--+--+ | c1 | xx | s | c2 | xx | xx | xx | l | xx = fill byte + --+--+--+--+--+--+--+--+--+--+--+--+gappy_t 0 + 4 + 8 + --+--+--+--+--+--+--+--+ | l | h | c1 | c2 |
                                                                                                   +--+--+--+--+--+--+--+--+dense_t
 

 And that's where the first quirk strikes: <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> templates have to be stuffed with <tt>&quot;x&quot;</tt> codes to get those extra fill bytes. 

 The natural question: ``Why can't Perl compensate for the gaps?'' warrants an answer. One good reason is that C compilers might provide (non-ANSI) extensions permitting all sorts of fancy control over the way structures are aligned, even at the level of an individual structure field. And, if this were not enough, there is an insidious thing called <tt>&quot;union&quot;</tt> where the amount of fill bytes cannot be derived from the alignment of the next item alone. 

 <font SIZE="-1">OK,</font> so let's bite the bullet. Here's one way to get the alignment right by inserting template codes <tt>&quot;x&quot;</tt>, which don't take a corresponding item from the list: 

 <pre>
  my $gappy = pack( 'cxs cxxx l!', $c1, $s, $c2, $l );
</pre> 

 Note the <tt>&quot;!&quot;</tt> after <tt>&quot;l&quot;</tt>: We want to make sure that we pack a long integer as it is compiled by our C compiler. And even now, it will only work for the platforms where the compiler aligns things as above. And somebody somewhere has a platform where it doesn't. [Probably a Cray, where <tt>&quot;short&quot;</tt>s, <tt>&quot;int&quot;</tt>s and <tt>&quot;long&quot;</tt>s are all 8 bytes. :-)] 

 Counting bytes and watching alignments in lengthy structures is bound to be a drag. Isn't there a way we can create the template with a simple program? Here's a C program that does the trick: 

 
#include &lt;stddef.h&gt;
#include &lt;stdio.h&gt;
typedef struct {
    char fc1;
    short fs;
    char fc2;
    long fl;
} gappy_t;
#define Pt(struct, field, tchar) \
    printf("@%d%s ", offsetof(struct, field), #tchar);
int main()
{
    Pt(gappy_t, fc1, c);
    Pt(gappy_t, fs, s !);
    Pt(gappy_t, fc2, c);
    Pt(gappy_t, fl, l !);
    printf("\n");
}
 

 The output line can be used as a template in a <tt>&quot;pack&quot;</tt> or <tt>&quot;unpack&quot;</tt> call: 

 <pre>
  my $gappy = pack( '@0c @2s! @4c @8l!', $c1, $s, $c2, $l );
</pre> 

 Gee, yet another template code - as if we hadn't plenty. But <tt>&quot;@&quot;</tt> saves our day by enabling us to specify the offset from the beginning of the pack buffer to the next item: This is just the value the <tt>&quot;offsetof&quot;</tt> macro (defined in <tt>&quot;&lt;stddef.h&gt;&quot;</tt>) returns when given a <tt>&quot;struct&quot;</tt> type and one of its field names (``member-designator'' in C standardese). 

 Neither using offsets nor adding <tt>&quot;x&quot;</tt>'s to bridge the gaps is satisfactory. (Just imagine what happens if the structure changes.) What we really need is a way of saying ``skip as many bytes as required to the next multiple of N''. In fluent Templatese, you say this with <tt>&quot;x!N&quot;</tt> where N is replaced by the appropriate value. Here's the next version of our struct packaging: 

 <pre>
  my $gappy = pack( 'c x!2 s c x!4 l!', $c1, $s, $c2, $l );
</pre> 

 That's certainly better, but we still have to know how long all the integers are, and portability is far away. Rather than <tt>2</tt>, for instance, we want to say ``however long a short is''. But this can be done by enclosing the appropriate pack code in brackets: <tt>&quot;[s]&quot;</tt>. So, here's the very best we can do: 

 <pre>
  my $gappy = pack( 'c x![s] s c x![l!] l!', $c1, $s, $c2, $l );
</pre>

<h3>Dealing with Endian-ness</h3>

 Now, imagine that we want to pack the data for a machine with a different byte-order. First, we'll have to figure out how big the data types on the target machine really are. Let's assume that the longs are 32 bits wide and the shorts are 16 bits wide. You can then rewrite the template as: 

 <pre>
  my $gappy = pack( 'c x![s] s c x![l] l', $c1, $s, $c2, $l );
</pre> 

 If the target machine is little-endian, we could write: 

 <pre>
  my $gappy = pack( 'c x![s] s&lt; c x![l] l&lt;', $c1, $s, $c2, $l );
</pre> 

 This forces the short and the long members to be little-endian, and is just fine if you don't have too many struct members. But we could also use the byte-order modifier on a group and write the following: 

 <pre>
  my $gappy = pack( '( c x![s] s c x![l] l )&lt;', $c1, $s, $c2, $l );
</pre> 

 This is not as short as before, but it makes it more obvious that we intend to have little-endian byte-order for a whole group, not only for individual template codes. It can also be more readable and easier to maintain.

<h3>Alignment, Take 2</h3>

 I'm afraid that we're not quite through with the alignment catch yet. The hydra raises another ugly head when you pack arrays of structures: 

 
typedef struct {
    short count;
    char glyph;
} cell_t;
typedef cell_t buffer_t[BUFLEN];
 

 Where's the catch? Padding is neither required before the first field <tt>&quot;count&quot;</tt>, nor between this and the next field <tt>&quot;glyph&quot;</tt>, so why can't we simply pack like this: 

 <pre>
   # something goes wrong here:
   pack( 's!a' x @buffer,
         map{ ( $_-&gt;{count}, $_-&gt;{glyph} ) } @buffer );
</pre> 

 This packs <tt>&quot;3*@buffer&quot;</tt> bytes, but it turns out that the size of <tt>&quot;buffer_t&quot;</tt> is four times <tt>&quot;BUFLEN&quot;</tt>! The moral of the story is that the required alignment of a structure or array is propagated to the next higher level where we have to consider padding <i>at the end</i> of each component as well. Thus the correct template is: 

 <pre>
   pack( 's!ax' x @buffer,
         map{ ( $_-&gt;{count}, $_-&gt;{glyph} ) } @buffer );
</pre>

<h3>Alignment, Take 3</h3>

 And even if you take all the above into account, <font SIZE="-1">ANSI</font> still lets this: 

 
typedef struct {
    char foo[2];
} foo_t;
 

 vary in size. The alignment constraint of the structure can be greater than any of its elements. [And if you think that this doesn't affect anything common, dismember the next cellphone that you see. Many have <font SIZE="-1">ARM</font> cores, and the <font SIZE="-1">ARM</font> structure rules make <tt>&quot;sizeof (foo_t)&quot;</tt> == 4]

<h3>Pointers for How to Use Them</h3>

 The title of this section indicates the second problem you may run into sooner or later when you pack C structures. If the function you intend to call expects a, say, <tt>&quot;void *&quot;</tt> value, you <i>cannot</i> simply take a reference to a Perl variable. (Although that value certainly is a memory address, it's not the address where the variable's contents are stored.) 

 Template code <tt>&quot;P&quot;</tt> promises to pack a ``pointer to a fixed length string''. Isn't this what we want? Let's try: 

 
#allocate some storage and pack a pointer to it
my $memory = "\x00" x $size;
my $memptr = pack('P', $memory);
 

 But wait: doesn't <tt>&quot;pack&quot;</tt> just return a sequence of bytes? How can we pass this string of bytes to some C code expecting a pointer which is, after all, nothing but a number? The answer is simple: We have to obtain the numeric address from the bytes returned by <tt>&quot;pack&quot;</tt>. 

 <pre>
    my $ptr = unpack( 'L!', $memptr );
</pre> 

 Obviously this assumes that it is possible to typecast a pointer to an unsigned long and vice versa, which frequently works but should not be taken as a universal law. - Now that we have this pointer the next question is: How can we put it to good use? We need a call to some C function where a pointer is expected. The <b><a HREF="/docs/linux/man/2-read/">read</a></b>(2) system call comes to mind: 

 
ssize_t read(int fd, void *buf, size_t count);
 

 After reading perlfunc explaining how to use <tt>&quot;syscall&quot;</tt> we can write this Perl function copying a file to standard output: 

 
require 'syscall.ph';
#run h2ph to generate this file
    sub
    cat($)
{
    my $path = shift();
    my $size = -s $path;
    my $memory = "\x00" x $size;
#allocate some memory
        my $ptr = unpack('L', pack('P', $memory));
    open(F, $path) || die("$path: cannot open ($!)\n");
    my $fd = fileno(F);
    my $res = syscall(&amp;SYS_read, fileno(F), $ptr, $size);
    print $memory;
    close(F);
}
 

 This is neither a specimen of simplicity nor a paragon of portability but it illustrates the point: We are able to sneak behind the scenes and access Perl's otherwise well-guarded memory! (Important note: Perl's <tt>&quot;syscall&quot;</tt> does <i>not</i> require you to construct pointers in this roundabout way. You simply pass a string variable, and Perl forwards the address.) 

 How does <tt>&quot;unpack&quot;</tt> with <tt>&quot;P&quot;</tt> work? Imagine some pointer in the buffer about to be unpacked: If it isn't the null pointer (which will smartly produce the <tt>&quot;undef&quot;</tt> value) we have a start address - but then what? Perl has no way of knowing how long this ``fixed length string'' is, so it's up to you to specify the actual size as an explicit length after <tt>&quot;P&quot;</tt>. 

 <pre>
   my $mem = &quot;abcdefghijklmn&quot;;
   print unpack( 'P5', pack( 'P', $mem ) ); # prints &quot;abcde&quot;
</pre> 

 As a consequence, <tt>&quot;pack&quot;</tt> ignores any number or <tt>&quot;*&quot;</tt> after <tt>&quot;P&quot;</tt>. 

 Now that we have seen <tt>&quot;P&quot;</tt> at work, we might as well give <tt>&quot;p&quot;</tt> a whirl. Why do we need a second template code for packing pointers at all? The answer lies behind the simple fact that an <tt>&quot;unpack&quot;</tt> with <tt>&quot;p&quot;</tt> promises a null-terminated string starting at the address taken from the buffer, and that implies a length for the data item to be returned: 

 
my $buf = pack('p', "abc\x00efhijklmn");
print unpack('p', $buf);
#prints "abc"
 

 Albeit this is apt to be confusing: As a consequence of the length being implied by the string's length, a number after pack code <tt>&quot;p&quot;</tt> is a repeat count, not a length as after <tt>&quot;P&quot;</tt>. 

 Using <tt>&quot;pack(..., $x)&quot;</tt> with <tt>&quot;P&quot;</tt> or <tt>&quot;p&quot;</tt> to get the address where <tt>$x</tt> is actually stored must be used with circumspection. Perl's internal machinery considers the relation between a variable and that address as its very own private matter and doesn't really care that we have obtained a copy. Therefore:
<dl>
<dt>&bull;
<dd> Do not use <tt>&quot;pack&quot;</tt> with <tt>&quot;p&quot;</tt> or <tt>&quot;P&quot;</tt> to obtain the address of variable that's bound to go out of scope (and thereby freeing its memory) before you are done with using the memory at that address.
<dt>&bull;
<dd> Be very careful with Perl operations that change the value of the variable. Appending something to the variable, for instance, might require reallocation of its storage, leaving you with a pointer into no-man's land.
<dt>&bull;
<dd> Don't think that you can get the address of a Perl variable when it is stored as an integer or double number! <tt>&quot;pack('P', $x)&quot;</tt> will force the variable's internal representation to string, just as if you had written something like <tt>&quot;$x .= ''&quot;</tt>.</dl>
 

 It's safe, however, to P- or p-pack a string literal, because Perl simply allocates an anonymous variable.

<h2>Pack Recipes</h2>

 Here are a collection of (possibly) useful canned recipes for <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt>: 

 
#Convert IP address for socket functions
pack("C4", split /\./, "123.4.5.6");
#Count the bits in a chunk of memory(e.g.a select vector)
unpack('%32b*', $mask);
#Determine the endianness of your system
$is_little_endian = unpack('c', pack('s', 1));
$is_big_endian = unpack('xc', pack('s', 1));
#Determine the number of bits in a native integer
$bits = unpack('%32I!', ~0);
#Prepare argument for the nanosleep system call
my $timespec = pack('L!L!', $secs, $nanosecs);
 

 For a simple memory dump we unpack some bytes into just as many pairs of hex digits, and use <tt>&quot;map&quot;</tt> to handle the traditional spacing - 16 bytes to a line: 

 
my $i;
print map(++$i % 16 ? "$_ " : "$_\n",
          unpack('H2' x length($mem), $mem)),
    length($mem) % 16 ? "\n" : '';


<h2>Funnies Section</h2>

 <pre><code>
#Pulling digits out of nowhere...
print unpack('C', pack('x')),
    unpack('%B*', pack('A')),
    unpack('H', pack('A')),
    unpack('A', unpack('C', pack('A'))), "\n";
#One for the road; -)
my $advice = pack('all u can in a van');
</code></pre>

<h2>Authors</h2>

 Simon Cozens and Wolfgang Laun. 

<h2>Index</h2>



<dt><a HREF="#lbAX">Packing and Unpacking C Structures</a>
<dd>


<dt><a HREF="#lbBD">Pack Recipes</a>
<dd>
<dt><a HREF="#lbBE">Funnies Section</a>
<dd>
<dt><a HREF="#lbBF">Authors</a>
<dd></dl>
