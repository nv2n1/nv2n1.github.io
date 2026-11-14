---
title: "perlembed(1)"
name: "perlembed"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlembed/"
description: "perlembed – how to embed perl in your C program"
---

<h2 class="name">NAME</h2>
<p> perlembed &#8211; how to embed perl in your C program </p>
<h2>DESCRIPTION</h2>
<h3><font SIZE="-1">PREAMBLE</font></h3>
<p> Do you want to:</p>
<dl>
<dt><code>Use C from Perl?</code></p>
<dd> Read perlxstut, perlxs, h2xs, perlguts, and perlapi.</p>
<dt><code>Use a Unix program from Perl?</code></p>
<dd> Read about back-quotes and about <tt>&quot;system&quot;</tt> and <tt>&quot;exec&quot;</tt> in perlfunc.</p>
<dt><code>Use Perl from Perl?</code></p>
<dd> Read about &#8220;do&#8221; in perlfunc and &#8220;eval&#8221; in perlfunc and &#8220;require&#8221; in perlfunc and &#8220;use&#8221; in perlfunc.</p>
<dt><code>Use C from C?</code></p>
<dd> Rethink your design.</p>
<dt><code>Use Perl from C?</code></p>
<dd> Read on&#8230;</dl>
<h3><font SIZE="-1">ROADMAP</font></h3>
<dl>
<dt>&bull;</p>
<dd> Compiling your C program</p>
<dt>&bull;</p>
<dd> Adding a Perl interpreter to your C program</p>
<dt>&bull;</p>
<dd> Calling a Perl subroutine from your C program</p>
<dt>&bull;</p>
<dd> Evaluating a Perl statement from your C program</p>
<dt>&bull;</p>
<dd> Performing Perl pattern matches and substitutions from your C program</p>
<dt>&bull;</p>
<dd> Fiddling with the Perl stack from your C program</p>
<dt>&bull;</p>
<dd> Maintaining a persistent interpreter</p>
<dt>&bull;</p>
<dd> Maintaining multiple interpreter instances</p>
<dt>&bull;</p>
<dd> Using Perl modules, which themselves use C libraries, from your C program</p>
<dt>&bull;</p>
<dd> Embedding Perl under Win32</dl>
<h3>Compiling your C program</h3>
<p> If you have trouble compiling the scripts in this documentation, you&#8217;re not alone. The cardinal rule: <font SIZE="-1">COMPILE THE PROGRAMS IN EXACTLY THE SAME WAY THAT YOUR PERL WAS COMPILED.</font> (Sorry for yelling.) </p>
<p> Also, every C program that uses Perl must link in the <i>perl library</i>. What&#8217;s that, you ask? Perl is itself written in C; the perl library is the collection of compiled C programs that were used to create your perl executable (<i>/usr/bin/perl</i> or equivalent). (Corollary: you can&#8217;t use Perl from your C program unless Perl has been compiled on your machine, or installed properly&#8212;that&#8217;s why you shouldn&#8217;t blithely copy Perl executables from machine to machine without also copying the <i>lib</i> directory.) </p>
<p> When you use Perl from C, your C program will&#8212;usually&#8211;allocate, &#8220;run&#8221;, and deallocate a <i>PerlInterpreter</i> object, which is defined by the perl library. </p>
<p> If your copy of Perl is recent enough to contain this documentation (version 5.002 or later), then the perl library (and <i></i><font SIZE="-1"><i>EXTERN</i></font><i>.h</i> and <i>perl.h</i>, which you&#8217;ll also need) will reside in a directory that looks like this: </p>
<pre>
    /usr/local/lib/perl5/your_architecture_here/CORE
</pre>
<p> or perhaps just </p>
<pre>
    /usr/local/lib/perl5/CORE
</pre>
<p> or maybe something like </p>
<pre>
    /usr/opt/perl5/CORE
</pre>
<p> Execute this statement for a hint about where to find <font SIZE="-1">CORE:</font> </p>
<pre>
    perl -MConfig -e 'print $Config{archlib}'
</pre>
<p> Here&#8217;s how you&#8217;d compile the example in the next section, &#8220;Adding a Perl interpreter to your C program&#8221;, on my Linux box: </p>
<pre>
    % gcc -O2 -Dbool=char -DHAS_BOOL -I/usr/local/include
    -I/usr/local/lib/perl5/i586-linux/5.003/CORE
    -L/usr/local/lib/perl5/i586-linux/5.003/CORE
    -o interp interp.c -lperl -lm
</pre>
<p> (That&#8217;s all one line.) On my <font SIZE="-1">DEC</font> Alpha running old 5.003_05, the incantation is a bit different: </p>
<pre>
    % cc -O2 -Olimit 2900 -I/usr/local/include
    -I/usr/local/lib/perl5/alpha-dec_osf/5.00305/CORE
    -L/usr/local/lib/perl5/alpha-dec_osf/5.00305/CORE -L/usr/local/lib
    -D__LANGUAGE_C__ -D_NO_PROTO -o interp interp.c -lperl -lm
</pre>
<p> How can you figure out what to add? Assuming your Perl is post-5.001, execute a <tt>&quot;perl -V&quot;</tt> command and pay special attention to the &#8220;cc&#8221; and &#8220;ccflags&#8221; information. </p>
<p> You&#8217;ll have to choose the appropriate compiler (<i>cc</i>, <i>gcc</i>, et al.) for your machine: <tt>&quot;perl -MConfig -e 'print $Config{cc}'&quot;</tt> will tell you what to use. </p>
<p> You&#8217;ll also have to choose the appropriate library directory (<i>/usr/local/lib/&#8230;</i>) for your machine. If your compiler complains that certain functions are undefined, or that it can&#8217;t locate <i>-lperl</i>, then you need to change the path following the <tt>&quot;-L&quot;</tt>. If it complains that it can&#8217;t find <i></i><font SIZE="-1"><i>EXTERN</i></font><i>.h</i> and <i>perl.h</i>, you need to change the path following the <tt>&quot;-I&quot;</tt>. </p>
<p> You may have to add extra libraries as well. Which ones? Perhaps those printed by </p>
<pre>
   perl -MConfig -e 'print $Config{libs}'
</pre>
<p> Provided your perl binary was properly configured and installed the <code>ExtUtils::Embed</code> module will determine all of this information for you: </p>
<pre>
   % cc -o interp interp.c `perl -MExtUtils::Embed -e ccopts -e ldopts`
</pre>
<p> If the <code>ExtUtils::Embed</code> module isn&#8217;t part of your Perl distribution, you can retrieve it from &lt;<a rel="nofollow" href="http://www.perl.com/perl/CPAN/modules/by-module/ExtUtils/">http://www.perl.com/perl/CPAN/modules/by-module/ExtUtils/</a>&gt; (If this documentation came from your Perl distribution, then you&#8217;re running 5.004 or better and you already have it.) </p>
<p> The <code>ExtUtils::Embed</code> kit on <font SIZE="-1">CPAN</font> also contains all source code for the examples in this document, tests, additional examples and other information you may find useful.</p>
<h3>Adding a Perl interpreter to your C program</h3>
<p> In a sense, perl (the C program) is a good example of embedding Perl (the language), so I&#8217;ll demonstrate embedding with <i>miniperlmain.c</i>, included in the source distribution. Here&#8217;s a bastardized, non-portable version of <i>miniperlmain.c</i> containing the essentials of embedding: </p>
<pre><code>
#include &lt;EXTERN.h&gt;              /* from the Perl distribution     */
#include &lt;perl.h&gt;                /* from the Perl distribution     */
static PerlInterpreter *my_perl; /***    The Perl interpreter    ***/
int main(int argc, char **argv, char **env)
{
    PERL_SYS_INIT3(&amp;argc, &amp;argv, &amp;env);
    my_perl = perl_alloc();
    perl_construct(my_perl);
    PL_exit_flags |= PERL_EXIT_DESTRUCT_END;
    perl_parse(my_perl, NULL, argc, argv, (char **)NULL);
    perl_run(my_perl);
    perl_destruct(my_perl);
    perl_free(my_perl);
    PERL_SYS_TERM();
    exit(EXIT_SUCCESS);
}
</code></pre>
<p> Notice that we don&#8217;t use the <tt>&quot;env&quot;</tt> pointer. Normally handed to <tt>&quot;perl_parse&quot;</tt> as its final argument, <tt>&quot;env&quot;</tt> here is replaced by <tt>&quot;NULL&quot;</tt>, which means that the current environment will be used. </p>
<p> The macros <font SIZE="-1"><code>PERL_SYS_INIT3</code></font><code>()</code> and <font SIZE="-1"><code>PERL_SYS_TERM</code></font><code>()</code> provide system-specific tune up of the C runtime environment necessary to run Perl interpreters; they should only be called once regardless of how many interpreters you create or destroy. Call <font SIZE="-1"><code>PERL_SYS_INIT3</code></font><code>()</code> before you create your first interpreter, and <font SIZE="-1"><code>PERL_SYS_TERM</code></font><code>()</code> after you free your last interpreter. </p>
<p> Since <font SIZE="-1"><code>PERL_SYS_INIT3</code></font><code>()</code> may change <tt>&quot;env&quot;</tt>, it may be more appropriate to provide <tt>&quot;env&quot;</tt> as an argument to <code>perl_parse()</code>. </p>
<p> Also notice that no matter what arguments you pass to <code>perl_parse()</code>, <font SIZE="-1"><code>PERL_SYS_INIT3</code></font><code>()</code> must be invoked on the C <code>main()</code> argc, argv and env and only once. </p>
<p> Mind that argv[argc] must be <font SIZE="-1">NULL,</font> same as those passed to a main function in C. </p>
<p> Now compile this program (I&#8217;ll call it <i>interp.c</i>) into an executable: </p>
<pre>
    % cc -o interp interp.c `perl -MExtUtils::Embed -e ccopts -e ldopts`
</pre>
<p> After a successful compilation, you&#8217;ll be able to use <i>interp</i> just like perl itself: </p>
<pre>
    % interp
    print &quot;Pretty Good Perl 
&quot;;
    print &quot;10890 - 9801 is &quot;, 10890 - 9801;
    &lt;CTRL-D&gt;
    Pretty Good Perl
    10890 - 9801 is 1089
</pre>
<p> or </p>
<pre>
    % interp -e 'printf(&quot;%x&quot;, 3735928559)'
    deadbeef
</pre>
<p> You can also read and execute Perl statements from a file while in the midst of your C program, by placing the filename in <i>argv[1]</i> before calling <i>perl_run</i>.</p>
<h3>Calling a Perl subroutine from your C program</h3>
<p> To call individual Perl subroutines, you can use any of the <code>call_*</code> functions documented in perlcall. In this example we&#8217;ll use <tt>&quot;call_argv&quot;</tt>. </p>
<p> That&#8217;s shown below, in a program I&#8217;ll call <i>showtime.c</i>. </p>
<p>#include &lt;EXTERN.h&gt;<br />
#include &lt;perl.h&gt;<br />
static PerlInterpreter *my_perl;<br />
int main(int argc, char **argv, char **env)<br />
{<br />
    char *args[] = {NULL};<br />
    PERL_SYS_INIT3(&amp;argc, &amp;argv, &amp;env);<br />
    my_perl = perl_alloc();<br />
    perl_construct(my_perl);<br />
    perl_parse(my_perl, NULL, argc, argv, NULL);<br />
    PL_exit_flags |= PERL_EXIT_DESTRUCT_END;<br />
    /*** skipping perl_run() ***/<br />
    call_argv(&#8220;showtime&#8221;, G_DISCARD | G_NOARGS, args);<br />
    perl_destruct(my_perl);<br />
    perl_free(my_perl);<br />
    PERL_SYS_TERM();<br />
    exit(EXIT_SUCCESS);<br />
}</p>
<p> where <i>showtime</i> is a Perl subroutine that takes no arguments (that&#8217;s the <i>G_NOARGS</i>) and for which I&#8217;ll ignore the return value (that&#8217;s the <i>G_DISCARD</i>). Those flags, and others, are discussed in perlcall. </p>
<p> I&#8217;ll define the <i>showtime</i> subroutine in a file called <i>showtime.pl</i>: </p>
<p>print &#8220;I shan&#8217;t be printed.&#8221;;<br />
sub showtime<br />
{<br />
    print time;<br />
}</p>
<p> Simple enough. Now compile and run: </p>
<pre>
 % cc -o showtime showtime.c \
     `perl -MExtUtils::Embed -e ccopts -e ldopts`
 % showtime showtime.pl
 818284590
</pre>
<p> yielding the number of seconds that elapsed between January 1, 1970 (the beginning of the Unix epoch), and the moment I began writing this sentence. </p>
<p> In this particular case we don&#8217;t have to call <i>perl_run</i>, as we set the PL_exit_flag <font SIZE="-1">PERL_EXIT_DESTRUCT_END</font> which executes <font SIZE="-1">END</font> blocks in perl_destruct. </p>
<p> If you want to pass arguments to the Perl subroutine, you can add strings to the <tt>&quot;NULL&quot;</tt>-terminated <tt>&quot;args&quot;</tt> list passed to <i>call_argv</i>. For other data types, or to examine return values, you&#8217;ll need to manipulate the Perl stack. That&#8217;s demonstrated in &#8220;Fiddling with the Perl stack from your C program&#8221;.</p>
<h3>Evaluating a Perl statement from your C program</h3>
<p> Perl provides two <font SIZE="-1">API</font> functions to evaluate pieces of Perl code. These are &#8220;eval_sv&#8221; in perlapi and &#8220;eval_pv&#8221; in perlapi. </p>
<p> Arguably, these are the only routines you&#8217;ll ever need to execute snippets of Perl code from within your C program. Your code can be as long as you wish; it can contain multiple statements; it can employ &#8220;use&#8221; in perlfunc, &#8220;require&#8221; in perlfunc, and &#8220;do&#8221; in perlfunc to include external Perl files. </p>
<p> <i>eval_pv</i> lets us evaluate individual Perl strings, and then extract variables for coercion into C types. The following program, <i>string.c</i>, executes three Perl strings, extracting an <tt>&quot;int&quot;</tt> from the first, a <tt>&quot;float&quot;</tt> from the second, and a <tt>&quot;char *&quot;</tt> from the third. </p>
<p>#include &lt;EXTERN.h&gt;<br />
#include &lt;perl.h&gt;<br />
static PerlInterpreter *my_perl;<br />
main(int argc, char **argv, char **env)<br />
{<br />
    char *embedding[] = {&#8220;&#8221;, &#8220;-e&#8221;, &#8220;0&#8221;, NULL};<br />
    PERL_SYS_INIT3(&amp;argc, &amp;argv, &amp;env);<br />
    my_perl = perl_alloc();<br />
    perl_construct(my_perl);<br />
    perl_parse(my_perl, NULL, 3, embedding, NULL);<br />
    PL_exit_flags |= PERL_EXIT_DESTRUCT_END;<br />
    perl_run(my_perl);<br />
    /** Treat $a as an integer **/<br />
    eval_pv(&#8220;$a = 3; $a **= 2&#8221;, TRUE);<br />
    printf(&#8220;a = %d
&#8221;, SvIV(get_sv(&#8220;a&#8221;, 0)));<br />
    /** Treat $a as a float **/<br />
    eval_pv(&#8220;$a = 3.14; $a **= 2&#8221;, TRUE);<br />
    printf(&#8220;a = %f
&#8221;, SvNV(get_sv(&#8220;a&#8221;, 0)));<br />
    /** Treat $a as a string **/<br />
    eval_pv(<br />
        &#8220;$a = &#8216;rekcaH lreP rehtonA tsuJ&#8217;; $a = reverse($a);&#8221;, TRUE);<br />
    printf(&#8220;a = %s
&#8221;, SvPV_nolen(get_sv(&#8220;a&#8221;, 0)));<br />
    perl_destruct(my_perl);<br />
    perl_free(my_perl);<br />
    PERL_SYS_TERM();<br />
}</p>
<p> All of those strange functions with <i>sv</i> in their names help convert Perl scalars to C types. They&#8217;re described in perlguts and perlapi. </p>
<p> If you compile and run <i>string.c</i>, you&#8217;ll see the results of using <i></i>SvIV()<i></i> to create an <tt>&quot;int&quot;</tt>, <i></i>SvNV()<i></i> to create a <tt>&quot;float&quot;</tt>, and <i></i>SvPV()<i></i> to create a string: </p>
<pre>
   a = 9
   a = 9.859600
   a = Just Another Perl Hacker
</pre>
<p> In the example above, we&#8217;ve created a global variable to temporarily store the computed value of our eval&#8217;ed expression. It is also possible and in most cases a better strategy to fetch the return value from <i></i>eval_pv()<i></i> instead. Example: </p>
<p>&#8230; SV *val = eval_pv(&#8220;reverse &#8216;rekcaH lreP rehtonA tsuJ'&#8221;, TRUE);<br />
printf(&#8220;%s
&#8221;, SvPV_nolen(val));<br />
&#8230;</p>
<p> This way, we avoid namespace pollution by not creating global variables and we&#8217;ve simplified our code as well.</p>
<h3>Performing Perl pattern matches and substitutions from your C program</h3>
<p> The <i></i>eval_sv()<i></i> function lets us evaluate strings of Perl code, so we can define some functions that use it to &#8220;specialize&#8221; in matches and substitutions: <i></i>match()<i></i>, <i></i>substitute()<i></i>, and <i></i>matches()<i></i>. </p>
<p>I32 match(SV *string, char *pattern);</p>
<p> Given a string and a pattern (e.g., <tt>&quot;m/clasp/&quot;</tt> or <tt>&quot;/\w*/&quot;</tt>, which in your C program might appear as &#8220;/\b\w*\b/&#8221;), <code>match()</code> returns 1 if the string matches the pattern and 0 otherwise. </p>
<p>int substitute(SV **string, char *pattern);</p>
<p> Given a pointer to an <tt>&quot;SV&quot;</tt> and an <tt>&quot;=~&quot;</tt> operation (e.g., <tt>&quot;s/bob/robert/g&quot;</tt> or <tt>&quot;tr[A-Z][a-z]&quot;</tt>), <code>substitute()</code> modifies the string within the <tt>&quot;SV&quot;</tt> as according to the operation, returning the number of substitutions made. </p>
<p>SSize_t matches(SV *string, char *pattern, AV **matches);</p>
<p> Given an <tt>&quot;SV&quot;</tt>, a pattern, and a pointer to an empty <tt>&quot;AV&quot;</tt>, <code>matches()</code> evaluates <tt>&quot;$string =~ $pattern&quot;</tt> in a list context, and fills in <i>matches</i> with the array elements, returning the number of matches found. </p>
<p> Here&#8217;s a sample program, <i>match.c</i>, that uses all three (long lines have been wrapped here): </p>
<p>#include &lt;EXTERN.h&gt;<br />
#include &lt;perl.h&gt;<br />
static PerlInterpreter *my_perl;<br />
/** my_eval_sv(code, error_check)<br />
** kinda like eval_sv(),<br />
** but we pop the return value off the stack<br />
**/<br />
SV *my_eval_sv(SV *sv, I32 croak_on_error)<br />
{<br />
    dSP;<br />
    SV *retval;<br />
    PUSHMARK(SP);<br />
    eval_sv(sv, G_SCALAR);<br />
    SPAGAIN;<br />
    retval = POPs;<br />
    PUTBACK;<br />
    if (croak_on_error &amp;&amp; SvTRUE(ERRSV))<br />
        croak_sv(ERRSV);<br />
    return retval;<br />
}<br />
/** match(string, pattern)<br />
**<br />
** Used for matches in a scalar context.<br />
**<br />
** Returns 1 if the match was successful; 0 otherwise.<br />
**/<br />
I32 match(SV *string, char *pattern)<br />
{<br />
    SV *command = newSV(0), *retval;<br />
    sv_setpvf(command, &#8220;my $string = &#8216;%s&#8217;; $string =~ %s&#8221;,<br />
              SvPV_nolen(string), pattern);<br />
    retval = my_eval_sv(command, TRUE);<br />
    SvREFCNT_dec(command);<br />
    return SvIV(retval);<br />
}<br />
/** substitute(string, pattern)<br />
**<br />
** Used for =~ operations that<br />
** modify their left-hand side (s/// and tr///)<br />
**<br />
** Returns the number of successful matches, and<br />
** modifies the input string if there were any.<br />
**/<br />
I32 substitute(SV **string, char *pattern)<br />
{<br />
    SV *command = newSV(0), *retval;<br />
    sv_setpvf(command, &#8220;$string = &#8216;%s&#8217;; ($string =~ %s)&#8221;,<br />
              SvPV_nolen(*string), pattern);<br />
    retval = my_eval_sv(command, TRUE);<br />
    SvREFCNT_dec(command);<br />
    *string = get_sv(&#8220;string&#8221;, 0);<br />
    return SvIV(retval);<br />
}<br />
/** matches(string, pattern, matches)<br />
**<br />
** Used for matches in a list context.<br />
**<br />
** Returns the number of matches,<br />
** and fills in **matches with the matching substrings<br />
**/<br />
SSize_t matches(SV *string, char *pattern, AV **match_list)<br />
{<br />
    SV *command = newSV(0);<br />
    SSize_t num_matches;<br />
    sv_setpvf(command, &#8220;my $string = &#8216;%s&#8217;; @array = ($string =~ %s)&#8221;,<br />
              SvPV_nolen(string), pattern);<br />
    my_eval_sv(command, TRUE);<br />
    SvREFCNT_dec(command);<br />
    *match_list = get_av(&#8220;array&#8221;, 0);<br />
    num_matches = av_top_index(*match_list) + 1;<br />
    return num_matches;<br />
}<br />
main(int argc, char **argv, char **env)<br />
{<br />
    char *embedding[] = {&#8220;&#8221;, &#8220;-e&#8221;, &#8220;0&#8221;, NULL};<br />
    AV *match_list;<br />
    I32 num_matches, i;<br />
    SV *text;<br />
    PERL_SYS_INIT3(&amp;argc, &amp;argv, &amp;env);<br />
    my_perl = perl_alloc();<br />
    perl_construct(my_perl);<br />
    perl_parse(my_perl, NULL, 3, embedding, NULL);<br />
    PL_exit_flags |= PERL_EXIT_DESTRUCT_END;<br />
    text = newSV(0);<br />
    sv_setpv(text, &#8220;When he is at a convenience store and the &#8221;<br />
                   &#8220;bill comes to some amount like 76 cents, Maynard is &#8221;<br />
                   &#8220;aware that there is something he *should* do, something &#8221;<br />
                   &#8220;that will enable him to get back a quarter, but he has &#8221;<br />
                   &#8220;no idea *what*.  He fumbles through his red squeezey &#8221;<br />
                   &#8220;changepurse and gives the boy three extra pennies with &#8221;<br />
                   &#8220;his dollar, hoping that he might luck into the correct &#8221;<br />
                   &#8220;amount.  The boy gives him back two of his own pennies &#8221;<br />
                   &#8220;and then the big shiny quarter that is his prize. &#8221;<br />
                   &#8220;-RICHH&#8221;);<br />
    if (match(text, &#8220;m/quarter/&#8221;)) /** Does text contain &#8216;quarter&#8217;? **/<br />
        printf(&#8220;match: Text contains the word &#8216;quarter&#8217;.

&#8221;);<br />
    else<br />
        printf(&#8220;match: Text doesn&#8217;t contain the word &#8216;quarter&#8217;.

&#8221;);<br />
    if (match(text, &#8220;m/eighth/&#8221;)) /** Does text contain &#8216;eighth&#8217;? **/<br />
        printf(&#8220;match: Text contains the word &#8216;eighth&#8217;.

&#8221;);<br />
    else<br />
        printf(&#8220;match: Text doesn&#8217;t contain the word &#8216;eighth&#8217;.

&#8221;);<br />
    /** Match all occurrences of /wi../ **/<br />
    num_matches = matches(text, &#8220;m/(wi..)/g&#8221;, &amp;match_list);<br />
    printf(&#8220;matches: m/(wi..)/g found %d matches&#8230;
&#8221;, num_matches);<br />
    for (i = 0; i &lt; num_matches; i++)<br />
        printf(&#8220;match: %s
&#8221;,<br />
               SvPV_nolen(*av_fetch(match_list, i, FALSE)));<br />
    printf(&#8220;
&#8221;);<br />
    /** Remove all vowels from text **/<br />
    num_matches = substitute(&amp;text, &#8220;s/[aeiou]//gi&#8221;);<br />
    if (num_matches) {<br />
        printf(&#8220;substitute: s/[aeiou]//gi&#8230;%lu substitutions made.
&#8221;,<br />
               (unsigned long)num_matches);<br />
        printf(&#8220;Now text is: %s

&#8221;, SvPV_nolen(text));<br />
    }<br />
    /** Attempt a substitution **/<br />
    if (!substitute(&amp;text, &#8220;s/Perl/C/&#8221;)) {<br />
        printf(&#8220;substitute: s/Perl/C&#8230;No substitution made.

&#8221;);<br />
    }<br />
    SvREFCNT_dec(text);<br />
    PL_perl_destruct_level = 1;<br />
    perl_destruct(my_perl);<br />
    perl_free(my_perl);<br />
    PERL_SYS_TERM();<br />
}</p>
<p> which produces the output (again, long lines have been wrapped here) </p>
<pre>
  match: Text contains the word 'quarter'.
  match: Text doesn't contain the word 'eighth'.
  matches: m/(wi..)/g found 2 matches...
  match: will
  match: with
  substitute: s/[aeiou]//gi...139 substitutions made.
  Now text is: Whn h s t  cnvnnc str nd th bll cms t sm mnt lk 76 cnts,
  Mynrd s wr tht thr s smthng h *shld* d, smthng tht wll nbl hm t gt
  bck qrtr, bt h hs n d *wht*.  H fmbls thrgh hs rd sqzy chngprs nd
  gvs th by thr xtr pnns wth hs dllr, hpng tht h mght lck nt th crrct
  mnt.  Th by gvs hm bck tw f hs wn pnns nd thn th bg shny qrtr tht s
  hs prz. -RCHH
  substitute: s/Perl/C...No substitution made.
</pre>
<h3>Fiddling with the Perl stack from your C program</h3>
<p> When trying to explain stacks, most computer science textbooks mumble something about spring-loaded columns of cafeteria plates: the last thing you pushed on the stack is the first thing you pop off. That&#8217;ll do for our purposes: your C program will push some arguments onto &#8220;the Perl stack&#8221;, shut its eyes while some magic happens, and then pop the results&#8212;the return value of your Perl subroutine&#8212;off the stack. </p>
<p> First you&#8217;ll need to know how to convert between C types and Perl types, with <code>newSViv()</code> and <code>sv_setnv()</code> and <code>newAV()</code> and all their friends. They&#8217;re described in perlguts and perlapi. </p>
<p> Then you&#8217;ll need to know how to manipulate the Perl stack. That&#8217;s described in perlcall. </p>
<p> Once you&#8217;ve understood those, embedding Perl in C is easy. </p>
<p> Because C has no builtin function for integer exponentiation, let&#8217;s make Perl&#8217;s ** operator available to it (this is less useful than it sounds, because Perl implements ** with C&#8217;s <i></i>pow()<i></i> function). First I&#8217;ll create a stub exponentiation function in <i>power.pl</i>: </p>
<p>sub expo<br />
{<br />
    my($a, $b) = @_;<br />
    return $a * *$b;<br />
}</p>
<p> Now I&#8217;ll create a C program, <i>power.c</i>, with a function <i></i>PerlPower()<i></i> that contains all the perlguts necessary to push the two arguments into <i></i>expo()<i></i> and to pop the return value out. Take a deep breath&#8230; </p>
<p>#include &lt;EXTERN.h&gt;<br />
#include &lt;perl.h&gt;<br />
static PerlInterpreter *my_perl;<br />
static void<br />
PerlPower(int a, int b)<br />
{<br />
    dSP;                            /* initialize stack pointer      */<br />
    ENTER;                          /* everything created after here */<br />
    SAVETMPS;                       /* &#8230;is a temporary variable.   */<br />
    PUSHMARK(SP);                   /* remember the stack pointer    */<br />
    XPUSHs(sv_2mortal(newSViv(a))); /* push the base onto the stack  */<br />
    XPUSHs(sv_2mortal(newSViv(b))); /* push the exponent onto stack  */<br />
    PUTBACK;                        /* make local stack pointer global */<br />
    call_pv(&#8220;expo&#8221;, G_SCALAR);      /* call the function             */<br />
    SPAGAIN;                        /* refresh stack pointer         */<br />
                                    /* pop the return value from stack */<br />
    printf(&#8220;%d to the %dth power is %d.
&#8221;, a, b, POPi);<br />
    PUTBACK;<br />
    FREETMPS; /* free that return value        */<br />
    LEAVE;    /* &#8230;and the XPUSHed &#8220;mortal&#8221; args.*/<br />
}<br />
int main(int argc, char **argv, char **env)<br />
{<br />
    char *my_argv[] = {&#8220;&#8221;, &#8220;power.pl&#8221;, NULL};<br />
    PERL_SYS_INIT3(&amp;argc, &amp;argv, &amp;env);<br />
    my_perl = perl_alloc();<br />
    perl_construct(my_perl);<br />
    perl_parse(my_perl, NULL, 2, my_argv, (char **)NULL);<br />
    PL_exit_flags |= PERL_EXIT_DESTRUCT_END;<br />
    perl_run(my_perl);<br />
    PerlPower(3, 4); /*** Compute 3 ** 4 ***/<br />
    perl_destruct(my_perl);<br />
    perl_free(my_perl);<br />
    PERL_SYS_TERM();<br />
    exit(EXIT_SUCCESS);<br />
}</p>
<p> Compile and run: </p>
<pre>
    % cc -o power power.c `perl -MExtUtils::Embed -e ccopts -e ldopts`
    % power
    3 to the 4th power is 81.
</pre>
<h3>Maintaining a persistent interpreter</h3>
<p> When developing interactive and/or potentially long-running applications, it&#8217;s a good idea to maintain a persistent interpreter rather than allocating and constructing a new interpreter multiple times. The major reason is speed: since Perl will only be loaded into memory once. </p>
<p> However, you have to be more cautious with namespace and variable scoping when using a persistent interpreter. In previous examples we&#8217;ve been using global variables in the default package <tt>&quot;main&quot;</tt>. We knew exactly what code would be run, and assumed we could avoid variable collisions and outrageous symbol table growth. </p>
<p> Let&#8217;s say your application is a server that will occasionally run Perl code from some arbitrary file. Your server has no way of knowing what code it&#8217;s going to run. Very dangerous. </p>
<p> If the file is pulled in by <tt>&quot;perl_parse()&quot;</tt>, compiled into a newly constructed interpreter, and subsequently cleaned out with <tt>&quot;perl_destruct()&quot;</tt> afterwards, you&#8217;re shielded from most namespace troubles. </p>
<p> One way to avoid namespace collisions in this scenario is to translate the filename into a guaranteed-unique package name, and then compile the code into that package using &#8220;eval&#8221; in perlfunc. In the example below, each file will only be compiled once. Or, the application might choose to clean out the symbol table associated with the file after it&#8217;s no longer needed. Using &#8220;call_argv&#8221; in perlapi, We&#8217;ll call the subroutine <tt>&quot;Embed::Persistent::eval_file&quot;</tt> which lives in the file <tt>&quot;persistent.pl&quot;</tt> and pass the filename and boolean cleanup/cache flag as arguments. </p>
<p> Note that the process will continue to grow for each file that it uses. In addition, there might be <tt>&quot;AUTOLOAD&quot;</tt>ed subroutines and other conditions that cause Perl&#8217;s symbol table to grow. You might want to add some logic that keeps track of the process size, or restarts itself after a certain number of requests, to ensure that memory consumption is minimized. You&#8217;ll also want to scope your variables with &#8220;my&#8221; in perlfunc whenever possible. </p>
<p>package Embed::Persistent;<br />
#persistent.pl<br />
use strict;<br />
our % Cache;<br />
use Symbol qw(delete_package);<br />
sub valid_package_name<br />
{<br />
    my($string) = @_;<br />
    $string = ~s / ([^A &#8211; Za &#8211; z0 &#8211; 9\/ ]) / sprintf(&#8220;_%2x&#8221;, unpack(&#8220;C&#8221;, $1)) / eg;<br />
#second pass only for words starting with a digit<br />
    $string = ~s | / (\d) | sprintf(&#8220;/_%2x&#8221;, unpack(&#8220;C&#8221;, $1)) | eg;<br />
#Dress it up as a real package name<br />
    $string = ~s | / | :: | g;<br />
    return &#8220;Embed&#8221;.$string;<br />
}<br />
sub eval_file<br />
{<br />
    my($filename, $delete) = @_;<br />
    my $package = valid_package_name($filename);<br />
    my $mtime = -M $filename;<br />
    if (defined $Cache{$package} {mtime} &amp;&amp;<br />
        $Cache{$package} {mtime} &lt;= $mtime) {<br />
#we have compiled this subroutine already,<br />
#it has not been updated on disk, nothing left to do<br />
        print STDERR &#8220;already compiled $package-&gt;handler
&#8221;;<br />
    } else {<br />
        local *FH;<br />
        open FH, $filename or die &#8220;open &#8216;$filename&#8217; $!&#8221;;<br />
        local($ /) = undef;<br />
        my $sub = &lt;FH&gt;;<br />
        close FH;<br />
#wrap the code into a subroutine inside our unique package<br />
        my $eval = qq<br />
        {<br />
            package $package;<br />
            sub handler<br />
            {<br />
                $sub;<br />
            }<br />
        };<br />
        {<br />
#hide our variables within this block<br />
            my($filename, $mtime, $package, $sub);<br />
            eval $eval;<br />
        }<br />
        die $ @ if $ @;<br />
#cache it unless we&#8217;re cleaning out each time<br />
        $Cache{$package} {mtime} = $mtime unless $delete;<br />
    }<br />
    eval<br />
    {<br />
        $package-&gt;handler;<br />
    };<br />
    die $ @ if $ @;<br />
    delete_package($package) if $delete;<br />
#take a look if you want<br />
#print Devel::Symdump-&gt;rnew($package)-&gt;as_string, $ / ;<br />
}<br />
1;<br />
__END__<br />
/* persistent.c */<br />
#include &lt;EXTERN.h&gt;<br />
#include &lt;perl.h&gt;<br />
/* 1 = clean out filename&#8217;s symbol table after each request,<br />
   0 = don&#8217;t<br />
*/<br />
#ifndef DO_CLEAN<br />
#define DO_CLEAN 0<br />
#endif<br />
#define BUFFER_SIZE 1024<br />
static PerlInterpreter *my_perl = NULL;<br />
int main(int argc, char **argv, char **env)<br />
{<br />
    char *embedding[] = {&#8220;&#8221;, &#8220;persistent.pl&#8221;, NULL};<br />
    char *args[] = {&#8220;&#8221;, DO_CLEAN, NULL};<br />
    char filename[BUFFER_SIZE];<br />
    int failing, exitstatus;<br />
    PERL_SYS_INIT3(&amp;argc, &amp;argv, &amp;env);<br />
    if ((my_perl = perl_alloc()) == NULL) {<br />
        fprintf(stderr, &#8220;no memory!&#8221;);<br />
        exit(EXIT_FAILURE);<br />
    }<br />
    perl_construct(my_perl);<br />
    PL_origalen = 1; /* don&#8217;t let $0 assignment update the<br />
                        proctitle or embedding[0] */<br />
    failing = perl_parse(my_perl, NULL, 2, embedding, NULL);<br />
    PL_exit_flags |= PERL_EXIT_DESTRUCT_END;<br />
    if (!failing)<br />
        failing = perl_run(my_perl);<br />
    if (!failing) {<br />
        while (printf(&#8220;Enter file name: &#8220;) &amp;&amp;<br />
               fgets(filename, BUFFER_SIZE, stdin)) {<br />
            filename[strlen(filename) &#8211; 1] = &#8216;
