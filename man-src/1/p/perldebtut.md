---
title: "perldebtut(1)"
name: "perldebtut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldebtut/"
description: "perldebtut – Perl debugging tutorial"
---

<h2 class="name">NAME</h2>
<p> perldebtut &#8211; Perl debugging tutorial </p>
<h2>DESCRIPTION</h2>
<p> A (very) lightweight introduction in the use of the perl debugger, and a pointer to existing, deeper sources of information on the subject of debugging perl programs. </p>
<p> There&#8217;s an extraordinary number of people out there who don&#8217;t appear to know anything about using the perl debugger, though they use the language every day. This is for them.</p>
<h2>use strict</h2>
<p> First of all, there&#8217;s a few things you can do to make your life a lot more straightforward when it comes to debugging perl programs, without using the debugger at all. To demonstrate, here&#8217;s a simple script, named &#8220;hello&#8221;, with a problem: </p>
<pre><code>
#!/ usr / bin / perl
$var1 = 'Hello World';
#always wanted to do that : -)
    $var2 = "$varl
";
print $var2;
exit;
</code></pre>
<p> While this compiles and runs happily, it probably won&#8217;t do what&#8217;s expected, namely it doesn&#8217;t print &#8220;Hello World
&#8221; at all; It will on the other hand do exactly what it was told to do, computers being a bit that way inclined. That is, it will print out a newline character, and you&#8217;ll get what looks like a blank line. It looks like there&#8217;s 2 variables when (because of the typo) there&#8217;s really 3: </p>
<pre>
        $var1 = 'Hello World';
        $varl = undef;
        $var2 = &quot;
&quot;;
</pre>
<p> To catch this kind of problem, we can force each variable to be declared before use by pulling in the strict module, by putting &#8216;use strict;&#8217; after the first line of the script. </p>
<p> Now when you run it, perl complains about the 3 undeclared variables and we get four error messages because one variable is referenced twice: </p>
<pre>
 Global symbol &quot;$var1&quot; requires explicit package name at ./t1 line 4.
 Global symbol &quot;$var2&quot; requires explicit package name at ./t1 line 5.
 Global symbol &quot;$varl&quot; requires explicit package name at ./t1 line 5.
 Global symbol &quot;$var2&quot; requires explicit package name at ./t1 line 7.
 Execution of ./hello aborted due to compilation errors.
</pre>
<p> Luvverly! and to fix this we declare all variables explicitly and now our script looks like this: </p>
<p>#!/ usr / bin / perl<br />
use strict;<br />
my $var1 = &#8216;Hello World&#8217;;<br />
my $varl = undef;<br />
my $var2 = &#8220;$varl
&#8221;;<br />
print $var2;<br />
exit;</p>
<p> We then do (always a good idea) a syntax check before we try to run it again: </p>
<pre>
        &gt; perl -c hello
        hello syntax OK
</pre>
<p> And now when we run it, we get &#8220;
&#8221; still, but at least we know why. Just getting this script to compile has exposed the &#8216;$varl&#8217; (with the letter &#8216;l&#8217;) variable, and simply changing <tt>$varl</tt> to <tt>$var1</tt> solves the problem.</p>
<h2>Looking at data and -w and v</h2>
<p> Ok, but how about when you want to really see your data, what&#8217;s in that dynamic variable, just before using it? </p>
<p>#!/ usr / bin / perl<br />
use strict;<br />
my $key = &#8216;welcome&#8217;;<br />
my % data = (&#8216;this&#8217; = &gt; qw(that),<br />
             &#8216;tom&#8217; = &gt; qw(and jerry),<br />
             &#8216;welcome&#8217; = &gt; q(Hello World),<br />
             &#8216;zip&#8217; = &gt; q(welcome), );<br />
my @data = keys % data;<br />
print &#8220;$data{$key}
&#8221;;<br />
exit;</p>
<p> Looks <font SIZE="-1">OK,</font> after it&#8217;s been through the syntax check (perl -c scriptname), we run it and all we get is a blank line again! Hmmmm. </p>
<p> One common debugging approach here, would be to liberally sprinkle a few print statements, to add a check just before we print out our data, and another just after: </p>
<p>print &#8220;All OK
&#8221; if grep ($key, keys % data);<br />
print &#8220;$data{$key}
&#8221;;<br />
print &#8220;done: &#8216;$data{$key}&#8217;
&#8221;;</p>
<p> And try again: </p>
<pre>
        &gt; perl data
        All OK     
        done: ''
</pre>
<p> After much staring at the same piece of code and not seeing the wood for the trees for some time, we get a cup of coffee and try another approach. That is, we bring in the cavalry by giving perl the &#8216;<code>-d</code>&#8216; switch on the command line: </p>
<p>        &gt; perl -d data<br />
        Default die handler restored.<br />
        Loading DB routines from perl5db.pl version 1.07<br />
        Editor support available.<br />
        Enter h or `h h&#8217; for help, or `man perldebug&#8217; for more help.<br />
        main::(./data:4):     my $key = &#8216;welcome&#8217;;</p>
<p> Now, what we&#8217;ve done here is to launch the built-in perl debugger on our script. It&#8217;s stopped at the first line of executable code and is waiting for input. </p>
<p> Before we go any further, you&#8217;ll want to know how to quit the debugger: use just the letter &#8216;<code>q</code>&#8216;, not the words &#8216;quit&#8217; or &#8216;exit&#8217;: </p>
<pre>
        DB&lt;1&gt; q
        &gt;
</pre>
<p> That&#8217;s it, you&#8217;re back on home turf again.</p>
<h2>help</h2>
<p> Fire the debugger up again on your script and we&#8217;ll look at the help menu. There&#8217;s a couple of ways of calling help: a simple &#8216;<code>h</code>&#8216; will get the summary help list, &#8216;<code>|h</code>&#8216; (pipe-h) will pipe the help through your pager (which is (probably &#8216;more&#8217; or &#8216;less&#8217;), and finally, &#8216;<code>h h</code>&#8216; (h-space-h) will give you the entire help screen. Here is the summary page: </p>
<p> D<code>1</code>h </p>
<p>List / search source lines : Control script execution : l[ln | sub] List source code T Stack trace &#8211; or.List previous / current line s[expr] Single step<br />
                                                                                                                            [in expr] v[line] View around line n[expr] Next,<br />
    steps over<br />
            subs<br />
                f filename View source in file&lt;CR / Enter&gt;<br />
                    Repeat last n or s / pattern /<br />
    ? patt ? Search forw / backw r Return from<br />
                               subroutine<br />
                                   M Show module versions c[ln | sub] Continue until<br />
                                       position<br />
                                           Debugger controls<br />
           : L List break / watch /<br />
                         actions<br />
                             o[&#8230;] Set debugger options t[expr] Toggle trace<br />
                                 [trace expr] &lt;<br />
                     [ &lt; ] |<br />
{[{]|&gt;[&gt;] [cmd] Do pre/post-prompt b [ln|event|sub] [cnd] Set<br />
                                                              breakpoint<br />
  ! [N|pat]   Redo a previous command     B ln|*      Delete a/all<br />
                                                             breakpoints<br />
  H [-num]    Display last num commands   a [ln] cmd  Do cmd before line<br />
  = [a val]   Define/list an alias        A ln|*      Delete a/all<br />
                                                                 actions<br />
  h [db_cmd]  Get help on command         w expr      Add a watch<br />
                                                              expression<br />
  h h         Complete help page          W expr|*    Delete a/all watch<br />
                                                                   exprs<br />
  |[|]db_cmd  Send output to pager        ![!] syscmd Run cmd in a<br />
                                                              subprocess<br />
  q or ^D     Quit                        R           Attempt a restart<br />
 Data Examination:     expr     Execute perl code, also see: s,n,t expr<br />
  x|m expr       Evals expr in list context, dumps the result or lists<br />
                                                                methods.<br />
  p expr         Print expression (uses script&#8217;s current package).<br />
  S [[!]pat]     List subroutine names [not] matching pattern<br />
  V [Pk [Vars]]  List Variables in Package.  Vars can be ~pattern or<br />
                                                               !pattern.<br />
  X [Vars]       Same as &#8220;V current_package [Vars]&#8221;.<br />
  y [n [Vars]]   List lexicals in higher scope &lt;n&gt;.  Vars same as V.<br />
 For more help, type h cmd_letter, or run man perldebug for all docs.</p>
<p> More confusing options than you can shake a big stick at! It&#8217;s not as bad as it looks and it&#8217;s very useful to know more about all of it, and fun too! </p>
<p> There&#8217;s a couple of useful ones to know about straight away. You wouldn&#8217;t think we&#8217;re using any libraries at all at the moment, but &#8216;<code>M</code>&#8216; will show which modules are currently loaded, and their version number, while &#8216;<code>m</code>&#8216; will show the methods, and &#8216;<code>S</code>&#8216; shows all subroutines (by pattern) as shown below. &#8216;<code>V</code>&#8216; and &#8216;<code>X</code>&#8216; show variables in the program by package scope and can be constrained by pattern. </p>
<pre>
        DB&lt;2&gt;S str 
        dumpvar::stringify
        strict::bits
        strict::import
        strict::unimport
</pre>
<p> Using &#8216;X&#8217; and cousins requires you not to use the type identifiers ($@%), just the &#8216;name&#8217;: </p>
<pre>
        DM&lt;3&gt;X ~err
        FileHandle(stderr) =&gt; <a href="//www.systutorials.com/docs/linux/man/2-fileno/">fileno</a>(2)
</pre>
<p> Remember we&#8217;re in our tiny program with a problem, we should have a look at where we are, and what our data looks like. First of all let&#8217;s view some code at our present position (the first line of code in this case), via &#8216;<code>v</code>&#8216;: </p>
<p>DB&lt;4&gt; v 1 #! / usr / bin / perl 2 : use strict;<br />
3 4 == &gt; my $key = &#8216;welcome&#8217;;<br />
5 : my % data = (6 &#8216;this&#8217; = &gt; qw(that),<br />
                 7 &#8216;tom&#8217; = &gt; qw(and jerry),<br />
                 8 &#8216;welcome&#8217; = &gt; q(Hello World),<br />
                 9 &#8216;zip&#8217; = &gt; q(welcome),<br />
                 10);</p>
<p> At line number 4 is a helpful pointer, that tells you where you are now. To see more code, type &#8216;v&#8217; again: </p>
<p>        DB&lt;4&gt; v<br />
        8               &#8216;welcome&#8217; =&gt; q(Hello World),<br />
        9               &#8216;zip&#8217; =&gt; q(welcome),<br />
        10      );<br />
        11 : my @data = keys % data;<br />
        12 : print &#8220;All OK
&#8221; if grep ($key, keys % data);<br />
        13 : print &#8220;$data{$key}
&#8221;;<br />
        14 : print &#8220;done: &#8216;$data{$key}&#8217;
&#8221;;<br />
        15 : exit;</p>
<p> And if you wanted to list line 5 again, type &#8216;l 5&#8217;, (note the space): </p>
<pre>
        DB&lt;4&gt; l 5
        5:      my %data = (
</pre>
<p> In this case, there&#8217;s not much to see, but of course normally there&#8217;s pages of stuff to wade through, and &#8216;l&#8217; can be very useful. To reset your view to the line we&#8217;re about to execute, type a lone period &#8216;.&#8217;: </p>
<pre>
        DB&lt;5&gt; .
        main::(./data_a:4):     my $key = 'welcome';
</pre>
<p> The line shown is the one that is about to be executed <code>next</code>, it hasn&#8217;t happened yet. So while we can print a variable with the letter &#8216;<code>p</code>&#8216;, at this point all we&#8217;d get is an empty (undefined) value back. What we need to do is to step through the next executable statement with an &#8216;<code>s</code>&#8216;: </p>
<pre>
        DB&lt;6&gt; s
        main::(./data_a:5):     my %data = (
        main::(./data_a:6):             'this' =&gt; qw(that),
        main::(./data_a:7):             'tom' =&gt; qw(and jerry),
        main::(./data_a:8):             'welcome' =&gt; q(Hello World),
        main::(./data_a:9):             'zip' =&gt; q(welcome),
        main::(./data_a:10):    );
</pre>
<p> Now we can have a look at that first ($key) variable: </p>
<pre>
        DB&lt;7&gt; p $key 
        welcome
</pre>
<p> line 13 is where the action is, so let&#8217;s continue down to there via the letter &#8216;<code>c</code>&#8216;, which by the way, inserts a &#8216;one-time-only&#8217; breakpoint at the given line or sub routine: </p>
<pre>
        DB&lt;8&gt; c 13
        All OK
        main::(./data_a:13):    print &quot;$data{$key}
&quot;;
</pre>
<p> We&#8217;ve gone past our check (where &#8216;All <font SIZE="-1">OK</font>&#8216; was printed) and have stopped just before the meat of our task. We could try to print out a couple of variables to see what is happening: </p>
<pre>
        DB&lt;9&gt; p $data{$key}
</pre>
<p> Not much in there, lets have a look at our hash: </p>
<pre>
        DB&lt;10&gt; p %data
        Hello Worldziptomandwelcomejerrywelcomethisthat 
        DB&lt;11&gt; p keys %data
        Hello Worldtomwelcomejerrythis
</pre>
<p> Well, this isn&#8217;t very easy to read, and using the helpful manual (<code>h h</code>), the &#8216;<code>x</code>&#8216; command looks promising: </p>
<pre>
        DB&lt;12&gt; x %data
        0  'Hello World'
        1  'zip'
        2  'tom'
        3  'and'
        4  'welcome'
        5  undef
        6  'jerry'
        7  'welcome'
        8  'this'
        9  'that'
</pre>
<p> That&#8217;s not much help, a couple of welcomes in there, but no indication of which are keys, and which are values, it&#8217;s just a listed array dump and, in this case, not particularly helpful. The trick here, is to use a <code>reference</code> to the data structure: </p>
<pre>
        DB&lt;13&gt; x \%data
        0  HASH(0x8194bc4)
           'Hello World' =&gt; 'zip'
           'jerry' =&gt; 'welcome'
           'this' =&gt; 'that'
           'tom' =&gt; 'and'
           'welcome' =&gt; undef
</pre>
<p> The reference is truly dumped and we can finally see what we&#8217;re dealing with. Our quoting was perfectly valid but wrong for our purposes, with &#8216;and jerry&#8217; being treated as 2 separate words rather than a phrase, thus throwing the evenly paired hash structure out of alignment. </p>
<p> The &#8216;<code>-w</code>&#8216; switch would have told us about this, had we used it at the start, and saved us a lot of trouble: </p>
<pre>
        &gt; perl -w data
        Odd number of elements in hash assignment at ./data line 5.
</pre>
<p> We fix our quoting: &#8216;tom&#8217; =&gt; q(and jerry), and run it again, this time we get our expected output: </p>
<pre>
        &gt; perl -w data
        Hello World
</pre>
<p> While we&#8217;re here, take a closer look at the &#8216;<code>x</code>&#8216; command, it&#8217;s really useful and will merrily dump out nested references, complete objects, partial objects &#8211; just about whatever you throw at it: </p>
<p> Let&#8217;s make a quick object and x-plode it, first we&#8217;ll start the debugger: it wants some form of input from <font SIZE="-1">STDIN,</font> so we give it something non-committal, a zero: </p>
<pre>
 &gt; perl -de 0
 Default die handler restored.
 Loading DB routines from perl5db.pl version 1.07
 Editor support available.
 Enter h or `h h' for help, or `man perldebug' for more help.
 main::(-e:1):   0
</pre>
<p> Now build an on-the-fly object over a couple of lines (note the backslash): </p>
<p>DB&lt;1&gt; $obj = bless({&#8216;unique_id&#8217; = &gt; &#8216;123&#8217;, &#8216;attr&#8217; = &gt; cont : {&#8216;col&#8217; = &gt; &#8216;black&#8217;, &#8216;things&#8217; = &gt; [qw(this that etc)]}}, &#8216;MY_class&#8217;)</p>
<p> And let&#8217;s have a look at it: </p>
<pre>
        DB&lt;2&gt; x $obj
 0  MY_class=HASH(0x828ad98)
                'attr' =&gt; HASH(0x828ad68)
        'col' =&gt; 'black'
        'things' =&gt; ARRAY(0x828abb8)
                0  'this'
                1  'that'
                2  'etc'
                'unique_id' =&gt; 123       
        DB&lt;3&gt;
</pre>
<p> Useful, huh? You can eval nearly anything in there, and experiment with bits of code or regexes until the cows come home: </p>
<p>DB&lt;3&gt; @data = qw(this that the other atheism leather theory scythe)<br />
                  DB&lt;4&gt;<br />
                      p &#8216;saw -&gt; &#8216;.($cnt += map{print &#8220;	:	$_
&#8221;} grep(/ the /, sort @data))<br />
                          atheism<br />
                              leather<br />
                                  other<br />
                                      scythe<br />
                                          the<br />
                                              theory<br />
                                                  saw-&gt;6</p>
<p> If you want to see the command History, type an &#8216;<code>H</code>&#8216;: </p>
<p>DB&lt;5&gt; H 4 : p &#8216;saw -&gt; &#8216;.($cnt += map{print &#8220;	:	$_
&#8221;} grep(/ the /, sort @data))3 : @data = qw(this that the other atheism leather theory scythe) 2 : x $obj<br />
                                                                                                                                                        1 : $obj = bless({&#8216;unique_id&#8217; = &gt; &#8216;123&#8217;, &#8216;attr&#8217; = &gt;<br />
                                                                                                                                                                                                          {&#8216;col&#8217; = &gt; &#8216;black&#8217;, &#8216;things&#8217; = &gt; [qw(this that etc)]}},<br />
                                                                                                                                                                         &#8216;MY_class&#8217;)<br />
                                                                                                                                                                DB&lt;5&gt;</p>
<p> And if you want to repeat any previous command, use the exclamation: &#8216;<code>!</code>&#8216;: </p>
<p>DB&lt;5&gt; !4 p &#8216;saw -&gt; &#8216;.($cnt += map{print &#8220;$_
&#8221;} grep(/ the /, sort @data))<br />
    atheism<br />
        leather<br />
            other<br />
                scythe<br />
                    the<br />
                        theory<br />
                            saw-&gt;12</p>
<p> For more on references see perlref and perlreftut</p>
<h2>Stepping through code</h2>
<p> Here&#8217;s a simple program which converts between Celsius and Fahrenheit, it too has a problem: </p>
<p>#!/ usr / bin / perl &#8211; w<br />
use strict;<br />
my $arg = $ARGV[0] || &#8216;-c20&#8217;;<br />
if ($arg = ~ / ^\- (c | f)((\- |\+) *\d + (\.\d +) *)$ /) {<br />
    my($deg, $num) = ($1, $2);<br />
    my($in, $out) = ($num, $num);<br />
    if ($deg eq &#8216;c&#8217;) {<br />
        $deg = &#8216;f&#8217;;<br />
        $out = &amp;c2f($num);<br />
    } else {<br />
        $deg = &#8216;c&#8217;;<br />
        $out = &amp;f2c($num);<br />
    }<br />
    $out = sprintf(&#8216;%0.2f&#8217;, $out);<br />
    $out = ~s / ^((\- |\+) *\d +)\.0 + $ / $1 / ;<br />
    print &#8220;$out $deg
&#8221;;<br />
} else {<br />
    print &#8220;Usage: $0 -[c|f] num
&#8221;;<br />
}<br />
exit;<br />
sub f2c<br />
{<br />
    my $f = shift;<br />
    my $c = 5 * $f &#8211; 32 / 9;<br />
    return $c;<br />
}<br />
sub c2f<br />
{<br />
    my $c = shift;<br />
    my $f = 9 * $c / 5 + 32;<br />
    return $f;<br />
}</p>
<p> For some reason, the Fahrenheit to Celsius conversion fails to return the expected output. This is what it does: </p>
<pre>
 &gt; temp -c0.72
 33.30 f
 &gt; temp -f33.3
 162.94 c
</pre>
<p> Not very consistent! We&#8217;ll set a breakpoint in the code manually and run it under the debugger to see what&#8217;s going on. A breakpoint is a flag, to which the debugger will run without interruption, when it reaches the breakpoint, it will stop execution and offer a prompt for further interaction. In normal use, these debugger commands are completely ignored, and they are safe &#8211; if a little messy, to leave in production code. </p>
<p>my($in, $out) = ($num, $num);<br />
$DB::single = 2;<br />
#insert at line 9 !if ($deg eq &#8216;c&#8217;)&#8230;&gt; perl &#8211; d temp &#8211; f33 .3 Default die handler restored.Loading DB routines from perl5db.pl version 1.07 Editor support available.Enter h or `h h &#8216; for help, or `man perldebug&#8217; for more help.main::(temp : 4) : my $arg = $ARGV[0] || &#8216;-c100&#8217;;</p>
<p> We&#8217;ll simply continue down to our pre-set breakpoint with a &#8216;<code>c</code>&#8216;: </p>
<pre>
        DB&lt;1&gt; c
        main::(temp:10):                if ($deg eq 'c') {
</pre>
<p> Followed by a view command to see where we are: </p>
<p>DB&lt;1&gt; v 7 : my($deg, $num) = ($1, $2);<br />
8 : my($in, $out) = ($num, $num);<br />
9 : $DB::single = 2;<br />
10 == &gt; if ($deg eq &#8216;c&#8217;)<br />
{<br />
    11 : $deg = &#8216;f&#8217;;<br />
    12 : $out = &amp;c2f($num);<br />
    13<br />
}<br />
else<br />
{<br />
    14 : $deg = &#8216;c&#8217;;<br />
    15 : $out = &amp;f2c($num);<br />
    16<br />
}</p>
<p> And a print to show what values we&#8217;re currently using: </p>
<pre>
        DB&lt;1&gt; p $deg, $num
        f33.3
</pre>
<p> We can put another break point on any line beginning with a colon, we&#8217;ll use line 17 as that&#8217;s just as we come out of the subroutine, and we&#8217;d like to pause there later on: </p>
<pre>
        DB&lt;2&gt; b 17
</pre>
<p> There&#8217;s no feedback from this, but you can see what breakpoints are set by using the list &#8216;L&#8217; command: </p>
<pre>
        DB&lt;3&gt; L
        temp:
                17:            print &quot;$out $deg
&quot;;
                break if (1)
</pre>
<p> Note that to delete a breakpoint you use &#8216;B&#8217;. </p>
<p> Now we&#8217;ll continue down into our subroutine, this time rather than by line number, we&#8217;ll use the subroutine name, followed by the now familiar &#8216;v&#8217;: </p>
<p>DB&lt;3&gt; c f2c<br />
    main::f2c(temp : 30)<br />
    : my $f = shift;<br />
DB&lt;4&gt; v 24 : exit;<br />
25 26 sub f2c<br />
{<br />
    27 == &gt; my $f = shift;<br />
    28 : my $c = 5 * $f &#8211; 32 / 9;<br />
    29 : return $c;<br />
    30<br />
}<br />
31 32 sub c2f<br />
{<br />
    33 : my $c = shift;</p>
<p> Note that if there was a subroutine call between us and line 29, and we wanted to <code>single-step</code> through it, we could use the &#8216;<code>s</code>&#8216; command, and to step over it we would use &#8216;<code>n</code>&#8216; which would execute the sub, but not descend into it for inspection. In this case though, we simply continue down to line 29: </p>
<pre>
        DB&lt;4&gt; c 29  
        main::f2c(temp:29):             return $c;
</pre>
<p> And have a look at the return value: </p>
<pre>
        DB&lt;5&gt; p $c
        162.944444444444
</pre>
<p> This is not the right answer at all, but the sum looks correct. I wonder if it&#8217;s anything to do with operator precedence? We&#8217;ll try a couple of other possibilities with our sum: </p>
<pre>
        DB&lt;6&gt; p (5 * $f - 32 / 9)
        162.944444444444
        DB&lt;7&gt; p 5 * $f - (32 / 9) 
        162.944444444444
        DB&lt;8&gt; p (5 * $f) - 32 / 9
        162.944444444444
        DB&lt;9&gt; p 5 * ($f - 32) / 9
        0.722222222222221
</pre>
<p> :-) that&#8217;s more like it! Ok, now we can set our return variable and we&#8217;ll return out of the sub with an &#8216;r&#8217;: </p>
<pre>
        DB&lt;10&gt; $c = 5 * ($f - 32) / 9
        DB&lt;11&gt; r
        scalar context return from main::f2c: 0.722222222222221
</pre>
<p> Looks good, let&#8217;s just continue off the end of the script: </p>
<pre>
        DB&lt;12&gt; c
        0.72 c 
        Debugged program terminated.  Use q to quit or R to restart,
        use O inhibit_exit to avoid stopping after program termination,
        h q, h R or h O to get additional info.
</pre>
<p> A quick fix to the offending line (insert the missing parentheses) in the actual program and we&#8217;re finished.</p>
<h2>Placeholder for a, w, t, T</h2>
<p> Actions, watch variables, stack traces etc.: on the <font SIZE="-1">TODO</font> list. </p>
<pre>
        a 
        w 
        t 
        T
</pre>
<h2>REGULAR EXPRESSIONS</h2>
<p> Ever wanted to know what a regex looked like? You&#8217;ll need perl compiled with the <font SIZE="-1">DEBUGGING</font> flag for this one: </p>
<p>&gt; perl &#8211; Dr &#8211; e &#8216;/^pe(a)*rl$/i&#8217; Compiling REx `^ pe(a) * rl$&#8217; size 17 first at 2 rarest char at 0 1 : BOL(2) 2 : EXACTF&lt;pe&gt;(4) 4 : CURLYN[1]{0, 32767}(14)6 : NOTHING(8) 8 : EXACTF&lt;a&gt;(0) 12 : WHILEM(0) 13 : NOTHING(14) 14 : EXACTF&lt;rl&gt;(16) 16 : EOL(17) 17 : END(0) floating `&#8217;$ at 4..2147483647 (checking floating) stclass<br />
    `EXACTF&lt;pe&gt;&#8217; anchored(BOL) minlen 4 Omitting $` $ &amp;$&#8217; support. EXECUTING&#8230; Freeing REx : `^ pe(a) * rl$&#8217;</p>
<p> Did you really want to know? :-) For more gory details on getting regular expressions to work, have a look at perlre, perlretut, and to decode the mysterious labels (<font SIZE="-1">BOL</font> and <font SIZE="-1">CURLYN,</font> etc. above), see perldebguts.</p>
<h2>OUTPUT TIPS</h2>
<p> To get all the output from your error log, and not miss any messages via helpful operating system buffering, insert a line like this, at the start of your script: </p>
<pre>
        $|=1;
</pre>
<p> To watch the tail of a dynamically growing logfile, (from the command line): </p>
<pre>
        tail -f $error_log
</pre>
<p> Wrapping all die calls in a handler routine can be useful to see how, and from where, they&#8217;re being called, perlvar has more information: </p>
<pre><code>
BEGIN
{
    $SIG{__DIE__} = sub
    {
        require Carp;
        Carp::confess(@_)
    }
}
</code></pre>
<p> Various useful techniques for the redirection of <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR</font> filehandles are explained in perlopentut and perlfaq8.</p>
<h2>CGI</h2>
<p> Just a quick hint here for all those <font SIZE="-1">CGI</font> programmers who can&#8217;t figure out how on earth to get past that &#8216;waiting for input&#8217; prompt, when running their <font SIZE="-1">CGI</font> script from the command-line, try something like this: </p>
<pre>
        &gt; perl -d my_cgi.pl -nodebug
</pre>
<p> Of course <font SIZE="-1">CGI</font> and perlfaq9 will tell you more.</p>
<h2>GUIs</h2>
<p> The command line interface is tightly integrated with an <code>emacs</code> extension and there&#8217;s a <code>vi</code> interface too. </p>
<p> You don&#8217;t have to do this all on the command line, though, there are a few <font SIZE="-1">GUI</font> options out there. The nice thing about these is you can wave a mouse over a variable and a dump of its data will appear in an appropriate window, or in a popup balloon, no more tiresome typing of &#8216;x <tt>$varname</tt>&#8216; :-) </p>
<p> In particular have a hunt around for the following: </p>
<p> <code>ptkdb</code> perlTK based wrapper for the built-in debugger </p>
<p> <code>ddd</code> data display debugger </p>
<p> <code>PerlDevKit</code> and <code>PerlBuilder</code> are <font SIZE="-1">NT</font> specific </p>
<p> <font SIZE="-1">NB.</font> (more info on these and others would be appreciated).</p>
<h2>SUMMARY</h2>
<p> We&#8217;ve seen how to encourage good coding practices with <code>use strict</code> and <code>-w</code>. We can run the perl debugger <code>perl -d scriptname</code> to inspect your data from within the perl debugger with the <code>p</code> and <code>x</code> commands. You can walk through your code, set breakpoints with <code>b</code> and step through that code with <code>s</code> or <code>n</code>, continue with <code>c</code> and return from a sub with <code>r</code>. Fairly intuitive stuff when you get down to it. </p>
<p> There is of course lots more to find out about, this has just scratched the surface. The best way to learn more is to use perldoc to find out more about the language, to read the on-line help (perldebug is probably the next place to go), and of course, experiment.</p>
<h2>SEE ALSO</h2>
<p> perldebug, perldebguts, perldiag, perlrun</p>
<h2>AUTHOR</h2>
<p> Richard Foley &lt;richard.foley [at] rfi.net&gt; Copyright (c) 2000</p>
<h2>CONTRIBUTORS</h2>
<p> Various people have made helpful suggestions and contributions, in particular: </p>
<p> Ronald J Kimball &lt;rjk [at] linguist.dartmouth.edu&gt; </p>
<p> Hugo van der Sanden &lt;hv [at] crypt0.demon.co.uk&gt; </p>
<p> Peter Scott &lt;Peter [at] PSDT.com&gt; </p>
<h2>Index</h2>
