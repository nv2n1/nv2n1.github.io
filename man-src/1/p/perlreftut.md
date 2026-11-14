---
title: "perlreftut(1)"
name: "perlreftut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlreftut/"
description: "perlreftut – Mark’s very short tutorial about references"
---

<h2 class="name">NAME</h2>
<p> perlreftut &#8211; Mark&#8217;s very short tutorial about references </p>
<h2>DESCRIPTION</h2>
<p> One of the most important new features in Perl 5 was the capability to manage complicated data structures like multidimensional arrays and nested hashes. To enable these, Perl 5 introduced a feature called <i>references</i>, and using references is the key to managing complicated, structured data in Perl. Unfortunately, there&#8217;s a lot of funny syntax to learn, and the main manual page can be hard to follow. The manual is quite complete, and sometimes people find that a problem, because it can be hard to tell what is important and what isn&#8217;t. </p>
<p> Fortunately, you only need to know 10% of what&#8217;s in the main page to get 90% of the benefit. This page will show you that 10%.</p>
<h2>Who Needs Complicated Data Structures?</h2>
<p> One problem that comes up all the time is needing a hash whose values are lists. Perl has hashes, of course, but the values have to be scalars; they can&#8217;t be lists. </p>
<p> Why would you want a hash of lists? Let&#8217;s take a simple example: You have a file of city and country names, like this: </p>
<pre>
        Chicago, USA
        Frankfurt, Germany
        Berlin, Germany
        Washington, USA
        Helsinki, Finland
        New York, USA
</pre>
<p> and you want to produce an output like this, with each country mentioned once, and then an alphabetical list of the cities in that country: </p>
<pre>
        Finland: Helsinki.
        Germany: Berlin, Frankfurt.
        USA:  Chicago, New York, Washington.
</pre>
<p> The natural way to do this is to have a hash whose keys are country names. Associated with each country name key is a list of the cities in that country. Each time you read a line of input, split it into a country and a city, look up the list of cities already known to be in that country, and append the new city to the list. When you&#8217;re done reading the input, iterate over the hash as usual, sorting each list of cities before you print it out. </p>
<p> If hash values couldn&#8217;t be lists, you lose. You&#8217;d probably have to combine all the cities into a single string somehow, and then when time came to write the output, you&#8217;d have to break the string into a list, sort the list, and turn it back into a string. This is messy and error-prone. And it&#8217;s frustrating, because Perl already has perfectly good lists that would solve the problem if only you could use them.</p>
<h2>The Solution</h2>
<p> By the time Perl 5 rolled around, we were already stuck with this design: Hash values must be scalars. The solution to this is references. </p>
<p> A reference is a scalar value that <i>refers to</i> an entire array or an entire hash (or to just about anything else). Names are one kind of reference that you&#8217;re already familiar with. Each human being is a messy, inconvenient collection of cells. But to refer to a particular human, for instance the first computer programmer, it isn&#8217;t necessary to describe each of their cells; all you need is the easy, convenient scalar string &#8220;Ada Lovelace&#8221;. </p>
<p> References in Perl are like names for arrays and hashes. They&#8217;re Perl&#8217;s private, internal names, so you can be sure they&#8217;re unambiguous. Unlike a human name, a reference only refers to one thing, and you always know what it refers to. If you have a reference to an array, you can recover the entire array from it. If you have a reference to a hash, you can recover the entire hash. But the reference is still an easy, compact scalar value. </p>
<p> You can&#8217;t have a hash whose values are arrays; hash values can only be scalars. We&#8217;re stuck with that. But a single reference can refer to an entire array, and references are scalars, so you can have a hash of references to arrays, and it&#8217;ll act a lot like a hash of arrays, and it&#8217;ll be just as useful as a hash of arrays. </p>
<p> We&#8217;ll come back to this city-country problem later, after we&#8217;ve seen some syntax for managing references.</p>
<h2>Syntax</h2>
<p> There are just two ways to make a reference, and just two ways to use it once you have it.</p>
<h3>Making References</h3>
<p> <i></i>Make Rule 1<i></i> </p>
<p> If you put a <tt>&quot;\&quot;</tt> in front of a variable, you get a reference to that variable. </p>
<pre>
    $aref = \@array;         # $aref now holds a reference to @array
    $href = \%hash;          # $href now holds a reference to %hash
    $sref = \$scalar;        # $sref now holds a reference to $scalar
</pre>
<p> Once the reference is stored in a variable like <tt>$aref</tt> or <tt>$href</tt>, you can copy it or store it just the same as any other scalar value: </p>
<pre><code>
$xy = $aref;
#$xy now holds a reference to @array
    $p[3] = $href;
#$p[3] now holds a reference to % hash
                                      $z = $p[3];
#$z now holds a reference to % hash
</code></pre>
<p> These examples show how to make references to variables with names. Sometimes you want to make an array or a hash that doesn&#8217;t have a name. This is analogous to the way you like to be able to use the string <tt>&quot;
&quot;</tt> or the number 80 without having to store it in a named variable first. </p>
<p> <i></i>Make Rule 2<i></i> </p>
<p> <tt>&quot;[ ITEMS ]&quot;</tt> makes a new, anonymous array, and returns a reference to that array. <tt>&quot;{ ITEMS }&quot;</tt> makes a new, anonymous hash, and returns a reference to that hash. </p>
<p>$aref = [ 1, &#8220;foo&#8221;, undef, 13 ];<br />
#$aref now holds a reference to an array<br />
$href = {APR = &gt; 4, AUG = &gt; 8};<br />
#$href now holds a reference to a hash</p>
<p> The references you get from rule 2 are the same kind of references that you get from rule 1: </p>
<p>#This:<br />
$aref = [ 1, 2, 3 ];<br />
#Does the same as this:<br />
@array = (1, 2, 3);<br />
$aref = \@array;</p>
<p> The first line is an abbreviation for the following two lines, except that it doesn&#8217;t create the superfluous array variable <tt>@array</tt>. </p>
<p> If you write just <tt>&quot;[]&quot;</tt>, you get a new, empty anonymous array. If you write just <tt>&quot;{}&quot;</tt>, you get a new, empty anonymous hash.</p>
<h3>Using References</h3>
<p> What can you do with a reference once you have it? It&#8217;s a scalar value, and we&#8217;ve seen that you can store it as a scalar and get it back again just like any scalar. There are just two more ways to use it: </p>
<p> <i></i>Use Rule 1<i></i> </p>
<p> You can always use an array reference, in curly braces, in place of the name of an array. For example, <tt>&quot;@{$aref}&quot;</tt> instead of <tt>@array</tt>. </p>
<p> Here are some examples of that: </p>
<p> Arrays: </p>
<p>@a @{$aref} An array<br />
    reverse @a reverse @{$aref} Reverse the array<br />
        $a[3] ${$aref}[3] An element of the array<br />
            $a[3] = 17;<br />
${$aref}[3] = 17 Assigning an element</p>
<p> On each line are two expressions that do the same thing. The left-hand versions operate on the array <tt>@a</tt>. The right-hand versions operate on the array that is referred to by <tt>$aref</tt>. Once they find the array they&#8217;re operating on, both versions do the same things to the arrays. </p>
<p> Using a hash reference is <i>exactly</i> the same: </p>
<p>% h % {$href} A hash keys % h keys % {$href} Get the keys from the hash $h{&#8216;red&#8217;} ${$href} {&#8216;red&#8217;} An element of the hash $h{&#8216;red&#8217;} = 17 ${$href} {&#8216;red&#8217;} = 17 Assigning an element</p>
<p> Whatever you want to do with a reference, <code>Use Rule 1</code> tells you how to do it. You just write the Perl code that you would have written for doing the same thing to a regular array or hash, and then replace the array or hash name with <tt>&quot;{$reference}&quot;</tt>. &#8220;How do I loop over an array when all I have is a reference?&#8221; Well, to loop over an array, you would write </p>
<pre>
        for my $element (@array) {
          ...
        }
</pre>
<p> so replace the array name, <tt>@array</tt>, with the reference: </p>
<p>        for<br />
            my $element(@{$aref})<br />
            {<br />
                &#8230;<br />
            }</p>
<p> &#8220;How do I print out the contents of a hash when all I have is a reference?&#8221; First write the code for printing out a hash: </p>
<p>        for<br />
            my $key(keys % hash)<br />
            {<br />
                print &#8220;$key =&gt; $hash{$key}
&#8221;;<br />
            }</p>
<p> And then replace the hash name with the reference: </p>
<p>        for<br />
            my $key(keys % {$href})<br />
            {<br />
                print &#8220;$key =&gt; ${$href}{$key}
&#8221;;<br />
            }</p>
<p> <i></i>Use Rule 2<i></i> </p>
<p> <code>Use Rule 1</code> is all you really need, because it tells you how to do absolutely everything you ever need to do with references. But the most common thing to do with an array or a hash is to extract a single element, and the <code>Use Rule 1</code> notation is cumbersome. So there is an abbreviation. </p>
<p> <tt>&quot;${$aref}[3]&quot;</tt> is too hard to read, so you can write <tt>&quot;$aref-&gt;[3]&quot;</tt> instead. </p>
<p> <tt>&quot;${$href}{red}&quot;</tt> is too hard to read, so you can write <tt>&quot;$href-&gt;{red}&quot;</tt> instead. </p>
<p> If <tt>$aref</tt> holds a reference to an array, then <tt>&quot;$aref-&gt;[3]&quot;</tt> is the fourth element of the array. Don&#8217;t confuse this with <tt>$aref[3]</tt>, which is the fourth element of a totally different array, one deceptively named <tt>@aref</tt>. <tt>$aref</tt> and <tt>@aref</tt> are unrelated the same way that <tt>$item</tt> and <tt>@item</tt> are. </p>
<p> Similarly, <tt>&quot;$href-&gt;{'red'}&quot;</tt> is part of the hash referred to by the scalar variable <tt>$href</tt>, perhaps even one with no name. <tt>$href{'red'}</tt> is part of the deceptively named <tt>%href</tt> hash. It&#8217;s easy to forget to leave out the <tt>&quot;-&gt;&quot;</tt>, and if you do, you&#8217;ll get bizarre results when your program gets array and hash elements out of totally unexpected hashes and arrays that weren&#8217;t the ones you wanted to use.</p>
<h3>An Example</h3>
<p> Let&#8217;s see a quick example of how all this is useful. </p>
<p> First, remember that <tt>&quot;[1, 2, 3]&quot;</tt> makes an anonymous array containing <tt>&quot;(1, 2, 3)&quot;</tt>, and gives you a reference to that array. </p>
<p> Now think about </p>
<p>@a = ([ 1, 2, 3 ],<br />
      [ 4, 5, 6 ],<br />
      [ 7, 8, 9 ]);</p>
<p> <tt>@a</tt> is an array with three elements, and each one is a reference to another array. </p>
<p> <tt>$a[1]</tt> is one of these references. It refers to an array, the array containing <tt>&quot;(4, 5, 6)&quot;</tt>, and because it is a reference to an array, <code>Use Rule 2</code> says that we can write <tt>$a[1]-&gt;[2]</tt> to get the third element from that array. <tt>$a[1]-&gt;[2]</tt> is the 6. Similarly, <tt>$a[0]-&gt;[1]</tt> is the 2. What we have here is like a two-dimensional array; you can write <tt>$a[ROW]-&gt;[COLUMN]</tt> to get or set the element in any row and any column of the array. </p>
<p> The notation still looks a little cumbersome, so there&#8217;s one more abbreviation:</p>
<h3>Arrow Rule</h3>
<p> In between two <code>subscripts</code>, the arrow is optional. </p>
<p> Instead of <tt>$a[1]-&gt;[2]</tt>, we can write <tt>$a[1][2]</tt>; it means the same thing. Instead of <tt>&quot;$a[0]-&gt;[1] = 23&quot;</tt>, we can write <tt>&quot;$a[0][1] = 23&quot;</tt>; it means the same thing. </p>
<p> Now it really looks like two-dimensional arrays! </p>
<p> You can see why the arrows are important. Without them, we would have had to write <tt>&quot;${$a[1]}[2]&quot;</tt> instead of <tt>$a[1][2]</tt>. For three-dimensional arrays, they let us write <tt>$x[2][3][5]</tt> instead of the unreadable <tt>&quot;${${$x[2]}[3]}[5]&quot;</tt>.</p>
<h2>Solution</h2>
<p> Here&#8217;s the answer to the problem I posed earlier, of reformatting a file of city and country names. </p>
<p>1 my % table;<br />
2 while (&lt;&gt;)<br />
{<br />
    3 chomp;<br />
    4 my($city, $country) = split /, / ;<br />
    5 $table{$country} = [] unless exists $table { $country };<br />
    6 push @{$table{$country}}, $city;<br />
    7<br />
}<br />
    8   for my $country (sort keys %table)<br />
    {<br />
        9 print &#8220;$country: &#8220;;<br />
        10 my @cities = @{$table{$country}};<br />
        11 print join &#8216;, &#8216;, sort @cities;<br />
        12 print &#8220;.
&#8221;;<br />
        13<br />
    }</p>
<p> The program has two pieces: Lines 2-7 read the input and build a data structure, and lines 8-13 analyze the data and print out the report. We&#8217;re going to have a hash, <tt>%table</tt>, whose keys are country names, and whose values are references to arrays of city names. The data structure will look like this: </p>
<p>% table + &#8212; &#8212; &#8212; -+&#8211; -+ | | | +&#8211; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+ | Germany | *&#8211; &#8212; &gt; | Frankfurt | Berlin |<br />
    | | | +&#8211; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; -+&#8211; -+ | | | +&#8211; &#8212; &#8212; &#8212; &#8211;+ | Finland | *&#8211; &#8212; &gt; | Helsinki |<br />
    | | | +&#8211; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; -+&#8211; -+ | | | +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+ | USA | *&#8211; &#8212; &gt; | Chicago | Washington | New York |<br />
    | | | +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; -+&#8211; -+</p>
<p> We&#8217;ll look at output first. Supposing we already have this structure, how do we print it out? </p>
<p>    8   for my $country (sort keys %table)<br />
    {<br />
        9 print &#8220;$country: &#8220;;<br />
        10 my @cities = @{$table{$country}};<br />
        11 print join &#8216;, &#8216;, sort @cities;<br />
        12 print &#8220;.
&#8221;;<br />
        13<br />
    }</p>
<p> <tt>%table</tt> is an ordinary hash, and we get a list of keys from it, sort the keys, and loop over the keys as usual. The only use of references is in line 10. <tt>$table{$country}</tt> looks up the key <tt>$country</tt> in the hash and gets the value, which is a reference to an array of cities in that country. <code>Use Rule 1</code> says that we can recover the array by saying <tt>&quot;@{$table{$country}}&quot;</tt>. Line 10 is just like </p>
<pre>
        @cities = @array;
</pre>
<p> except that the name <tt>&quot;array&quot;</tt> has been replaced by the reference <tt>&quot;{$table{$country}}&quot;</tt>. The <tt>&quot;@&quot;</tt> tells Perl to get the entire array. Having gotten the list of cities, we sort it, join it, and print it out as usual. </p>
<p> Lines 2-7 are responsible for building the structure in the first place. Here they are again: </p>
<p>2 while (&lt;&gt;)<br />
{<br />
    3 chomp;<br />
    4 my($city, $country) = split /, / ;<br />
    5 $table{$country} = [] unless exists $table { $country };<br />
    6 push @{$table{$country}}, $city;<br />
    7<br />
}</p>
<p> Lines 2-4 acquire a city and country name. Line 5 looks to see if the country is already present as a key in the hash. If it&#8217;s not, the program uses the <tt>&quot;[]&quot;</tt> notation (<code>Make Rule 2</code>) to manufacture a new, empty anonymous array of cities, and installs a reference to it into the hash under the appropriate key. </p>
<p> Line 6 installs the city name into the appropriate array. <tt>$table{$country}</tt> now holds a reference to the array of cities seen in that country so far. Line 6 is exactly like </p>
<pre>
        push @array, $city;
</pre>
<p> except that the name <tt>&quot;array&quot;</tt> has been replaced by the reference <tt>&quot;{$table{$country}}&quot;</tt>. The <tt>&quot;push&quot;</tt> adds a city name to the end of the referred-to array. </p>
<p> There&#8217;s one fine point I skipped. Line 5 is unnecessary, and we can get rid of it. </p>
<p>2 while (&lt;&gt;)<br />
{<br />
    3 chomp;<br />
    4 my($city, $country) = split /, / ;<br />
    5####$table{$country} = [] unless exists $table { $country };<br />
    6 push @{$table{$country}}, $city;<br />
    7<br />
}</p>
<p> If there&#8217;s already an entry in <tt>%table</tt> for the current <tt>$country</tt>, then nothing is different. Line 6 will locate the value in <tt>$table{$country}</tt>, which is a reference to an array, and push <tt>$city</tt> into the array. But what does it do when <tt>$country</tt> holds a key, say <tt>&quot;Greece&quot;</tt>, that is not yet in <tt>%table</tt>? </p>
<p> This is Perl, so it does the exact right thing. It sees that you want to push <tt>&quot;Athens&quot;</tt> onto an array that doesn&#8217;t exist, so it helpfully makes a new, empty, anonymous array for you, installs it into <tt>%table</tt>, and then pushes <tt>&quot;Athens&quot;</tt> onto it. This is called <i>autovivification</i>&#8211;bringing things to life automatically. Perl saw that the key wasn&#8217;t in the hash, so it created a new hash entry automatically. Perl saw that you wanted to use the hash value as an array, so it created a new empty array and installed a reference to it in the hash automatically. And as usual, Perl made the array one element longer to hold the new city name.</p>
<h2>The Rest</h2>
<p> I promised to give you 90% of the benefit with 10% of the details, and that means I left out 90% of the details. Now that you have an overview of the important parts, it should be easier to read the perlref manual page, which discusses 100% of the details. </p>
<p> Some of the highlights of perlref:</p>
<dl>
<dt>&bull;</p>
<dd> You can make references to anything, including scalars, functions, and other references.</p>
<dt>&bull;</p>
<dd> In <code>Use Rule 1</code>, you can omit the curly brackets whenever the thing inside them is an atomic scalar variable like <tt>$aref</tt>. For example, <tt>@$aref</tt> is the same as <tt>&quot;@{$aref}&quot;</tt>, and <tt>$$aref[1]</tt> is the same as <tt>&quot;${$aref}[1]&quot;</tt>. If you&#8217;re just starting out, you may want to adopt the habit of always including the curly brackets.</p>
<dt>&bull;</p>
<dd> This doesn&#8217;t copy the underlying array: </p>
<pre>
        $aref2 = $aref1;
</pre>
<p> You get two references to the same array. If you modify <tt>&quot;$aref1-&gt;[23]&quot;</tt> and then look at <tt>&quot;$aref2-&gt;[23]&quot;</tt> you&#8217;ll see the change. </p>
<p> To copy the array, use </p>
<p>$aref2 = [@{$aref1}];</p>
<p> This uses <tt>&quot;[...]&quot;</tt> notation to create a new anonymous array, and <tt>$aref2</tt> is assigned a reference to the new array. The new array is initialized with the contents of the array referred to by <tt>$aref1</tt>. </p>
<p> Similarly, to copy an anonymous hash, you can use </p>
<pre><code>
$href2 = { % {$href1}};
</code></pre>
<dt>&bull;</p>
<dd> To see if a variable contains a reference, use the <tt>&quot;ref&quot;</tt> function. It returns true if its argument is a reference. Actually it&#8217;s a little better than that: It returns <tt>&quot;HASH&quot;</tt> for hash references and <tt>&quot;ARRAY&quot;</tt> for array references.</p>
<dt>&bull;</p>
<dd> If you try to use a reference like a string, you get strings like </p>
<pre>
        ARRAY(0x80f5dec)   or    HASH(0x826afc0)
</pre>
<p> If you ever see a string that looks like this, you&#8217;ll know you printed out a reference by mistake. </p>
<p> A side effect of this representation is that you can use <tt>&quot;eq&quot;</tt> to see if two references refer to the same thing. (But you should usually use <tt>&quot;==&quot;</tt> instead because it&#8217;s much faster.)</p>
<dt>&bull;</p>
<dd> You can use a string as if it were a reference. If you use the string <tt>&quot;foo&quot;</tt> as an array reference, it&#8217;s taken to be a reference to the array <tt>@foo</tt>. This is called a <i>symbolic reference</i>. The declaration <tt>&quot;use strict 'refs'&quot;</tt> disables this feature, which can cause all sorts of trouble if you use it by accident.</dl>
<p> You might prefer to go on to perllol instead of perlref; it discusses lists of lists and multidimensional arrays in detail. After that, you should move on to perldsc; it&#8217;s a Data Structure Cookbook that shows recipes for using and printing out arrays of hashes, hashes of arrays, and other kinds of data.</p>
<h2>Summary</h2>
<p> Everyone needs compound data structures, and in Perl the way you get them is with references. There are four important rules for managing references: Two for making references and two for using them. Once you know these rules you can do most of the important things you need to do with references.</p>
<h2>Credits</h2>
<p> Author: Mark Jason Dominus, Plover Systems (<tt>&quot;mjd-perl-ref+ [at] plover.com&quot;</tt>) </p>
<p> This article originally appeared in <i>The Perl Journal</i> ( &lt;<a rel="nofollow" href="http://www.tpj.com/">http://www.tpj.com/</a>&gt; ) volume 3, #2. Reprinted with permission. </p>
<p> The original title was <i>Understand References Today</i>.</p>
<h3>Distribution Conditions</h3>
<p> Copyright 1998 The Perl Journal. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples in these files are hereby placed into the public domain. You are permitted and encouraged to use this code in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit would be courteous but is not required. </p>
<h2>Index</h2>
