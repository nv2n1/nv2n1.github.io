---
title: "perlcall(1)"
name: "perlcall"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlcall/"
description: "perlcall – Perl calling conventions from C"
---

<h2 class="name">NAME</h2>
<p> perlcall &#8211; Perl calling conventions from C </p>
<h2>DESCRIPTION</h2>
<p> The purpose of this document is to show you how to call Perl subroutines directly from C, i.e., how to write <i>callbacks</i>. </p>
<p> Apart from discussing the C interface provided by Perl for writing callbacks the document uses a series of examples to show how the interface actually works in practice. In addition some techniques for coding callbacks are covered. </p>
<p> Examples where callbacks are necessary include</p>
<dl>
<dt>&bull;</p>
<dd> An Error Handler </p>
<p> You have created an <font SIZE="-1">XSUB</font> interface to an application&#8217;s C <font SIZE="-1">API.</font> </p>
<p> A fairly common feature in applications is to allow you to define a C function that will be called whenever something nasty occurs. What we would like is to be able to specify a Perl subroutine that will be called instead.</p>
<dt>&bull;</p>
<dd> An Event-Driven Program </p>
<p> The classic example of where callbacks are used is when writing an event driven program, such as for an X11 application. In this case you register functions to be called whenever specific events occur, e.g., a mouse button is pressed, the cursor moves into a window or a menu item is selected.</dl>
<p> Although the techniques described here are applicable when embedding Perl in a C program, this is not the primary goal of this document. There are other details that must be considered and are specific to embedding Perl. For details on embedding Perl in C refer to perlembed. </p>
<p> Before you launch yourself head first into the rest of this document, it would be a good idea to have read the following two documents&#8212;perlxs and perlguts.</p>
<h2>THE CALL_ FUNCTIONS</h2>
<p> Although this stuff is easier to explain using examples, you first need be aware of a few important definitions. </p>
<p> Perl has a number of C functions that allow you to call Perl subroutines. They are </p>
<pre><code>
I32 call_sv(SV *sv, I32 flags);
I32 call_pv(char *subname, I32 flags);
I32 call_method(char *methname, I32 flags);
I32 call_argv(char *subname, I32 flags, char **argv);
</code></pre>
<p> The key function is <i>call_sv</i>. All the other functions are fairly simple wrappers which make it easier to call Perl subroutines in special cases. At the end of the day they will all call <i>call_sv</i> to invoke the Perl subroutine. </p>
<p> All the <i>call_*</i> functions have a <tt>&quot;flags&quot;</tt> parameter which is used to pass a bit mask of options to Perl. This bit mask operates identically for each of the functions. The settings available in the bit mask are discussed in &#8220;<font SIZE="-1">FLAG VALUES&#8221;</font>. </p>
<p> Each of the functions will now be discussed in turn.</p>
<dl>
<dt>call_sv</p>
<dd> <i>call_sv</i> takes two parameters. The first, <tt>&quot;sv&quot;</tt>, is an SV*. This allows you to specify the Perl subroutine to be called either as a C string (which has first been converted to an <font SIZE="-1">SV</font>) or a reference to a subroutine. The section, &#8220;Using call_sv&#8221;, shows how you can make use of <i>call_sv</i>.</p>
<dt>call_pv</p>
<dd> The function, <i>call_pv</i>, is similar to <i>call_sv</i> except it expects its first parameter to be a C char* which identifies the Perl subroutine you want to call, e.g., <tt>&quot;call_pv(&quot;fred&quot;, 0)&quot;</tt>. If the subroutine you want to call is in another package, just include the package name in the string, e.g., <tt>&quot;pkg::fred&quot;</tt>.</p>
<dt>call_method</p>
<dd> The function <i>call_method</i> is used to call a method from a Perl class. The parameter <tt>&quot;methname&quot;</tt> corresponds to the name of the method to be called. Note that the class that the method belongs to is passed on the Perl stack rather than in the parameter list. This class can be either the name of the class (for a static method) or a reference to an object (for a virtual method). See perlobj for more information on static and virtual methods and &#8220;Using call_method&#8221; for an example of using <i>call_method</i>.</p>
<dt>call_argv</p>
<dd> <i>call_argv</i> calls the Perl subroutine specified by the C string stored in the <tt>&quot;subname&quot;</tt> parameter. It also takes the usual <tt>&quot;flags&quot;</tt> parameter. The final parameter, <tt>&quot;argv&quot;</tt>, consists of a NULL-terminated list of C strings to be passed as parameters to the Perl subroutine. See &#8220;Using call_argv&#8221;.</dl>
<p> All the functions return an integer. This is a count of the number of items returned by the Perl subroutine. The actual items returned by the subroutine are stored on the Perl stack. </p>
<p> As a general rule you should <i>always</i> check the return value from these functions. Even if you are expecting only a particular number of values to be returned from the Perl subroutine, there is nothing to stop someone from doing something unexpected&#8212;don&#8217;t say you haven&#8217;t been warned.</p>
<h2>FLAG VALUES</h2>
<p> The <tt>&quot;flags&quot;</tt> parameter in all the <i>call_*</i> functions is one of G_VOID, G_SCALAR, or G_ARRAY, which indicate the call context, <font SIZE="-1">OR</font>&#8216;ed together with a bit mask of any combination of the other G_* symbols defined below.</p>
<h3>G_VOID</h3>
<p> Calls the Perl subroutine in a void context. </p>
<p> This flag has 2 effects:</p>
<dl>
<dt>1.</p>
<dd> It indicates to the subroutine being called that it is executing in a void context (if it executes <i>wantarray</i> the result will be the undefined value).</p>
<dt>2.</p>
<dd> It ensures that nothing is actually returned from the subroutine.</dl>
<p> The value returned by the <i>call_*</i> function indicates how many items have been returned by the Perl subroutine&#8212;in this case it will be 0.</p>
<h3>G_SCALAR</h3>
<p> Calls the Perl subroutine in a scalar context. This is the default context flag setting for all the <i>call_*</i> functions. </p>
<p> This flag has 2 effects:</p>
<dl>
<dt>1.</p>
<dd> It indicates to the subroutine being called that it is executing in a scalar context (if it executes <i>wantarray</i> the result will be false).</p>
<dt>2.</p>
<dd> It ensures that only a scalar is actually returned from the subroutine. The subroutine can, of course, ignore the <i>wantarray</i> and return a list anyway. If so, then only the last element of the list will be returned.</dl>
<p> The value returned by the <i>call_*</i> function indicates how many items have been returned by the Perl subroutine &#8211; in this case it will be either 0 or 1. </p>
<p> If 0, then you have specified the G_DISCARD flag. </p>
<p> If 1, then the item actually returned by the Perl subroutine will be stored on the Perl stack &#8211; the section &#8220;Returning a Scalar&#8221; shows how to access this value on the stack. Remember that regardless of how many items the Perl subroutine returns, only the last one will be accessible from the stack &#8211; think of the case where only one value is returned as being a list with only one element. Any other items that were returned will not exist by the time control returns from the <i>call_*</i> function. The section &#8220;Returning a List in Scalar Context&#8221; shows an example of this behavior.</p>
<h3>G_ARRAY</h3>
<p> Calls the Perl subroutine in a list context. </p>
<p> As with G_SCALAR, this flag has 2 effects:</p>
<dl>
<dt>1.</p>
<dd> It indicates to the subroutine being called that it is executing in a list context (if it executes <i>wantarray</i> the result will be true).</p>
<dt>2.</p>
<dd> It ensures that all items returned from the subroutine will be accessible when control returns from the <i>call_*</i> function.</dl>
<p> The value returned by the <i>call_*</i> function indicates how many items have been returned by the Perl subroutine. </p>
<p> If 0, then you have specified the G_DISCARD flag. </p>
<p> If not 0, then it will be a count of the number of items returned by the subroutine. These items will be stored on the Perl stack. The section &#8220;Returning a List of Values&#8221; gives an example of using the G_ARRAY flag and the mechanics of accessing the returned items from the Perl stack.</p>
<h3>G_DISCARD</h3>
<p> By default, the <i>call_*</i> functions place the items returned from by the Perl subroutine on the stack. If you are not interested in these items, then setting this flag will make Perl get rid of them automatically for you. Note that it is still possible to indicate a context to the Perl subroutine by using either G_SCALAR or G_ARRAY. </p>
<p> If you do not set this flag then it is <i>very</i> important that you make sure that any temporaries (i.e., parameters passed to the Perl subroutine and values returned from the subroutine) are disposed of yourself. The section &#8220;Returning a Scalar&#8221; gives details of how to dispose of these temporaries explicitly and the section &#8220;Using Perl to Dispose of Temporaries&#8221; discusses the specific circumstances where you can ignore the problem and let Perl deal with it for you.</p>
<h3>G_NOARGS</h3>
<p> Whenever a Perl subroutine is called using one of the <i>call_*</i> functions, it is assumed by default that parameters are to be passed to the subroutine. If you are not passing any parameters to the Perl subroutine, you can save a bit of time by setting this flag. It has the effect of not creating the <tt>@_</tt> array for the Perl subroutine. </p>
<p> Although the functionality provided by this flag may seem straightforward, it should be used only if there is a good reason to do so. The reason for being cautious is that, even if you have specified the G_NOARGS flag, it is still possible for the Perl subroutine that has been called to think that you have passed it parameters. </p>
<p> In fact, what can happen is that the Perl subroutine you have called can access the <tt>@_</tt> array from a previous Perl subroutine. This will occur when the code that is executing the <i>call_*</i> function has itself been called from another Perl subroutine. The code below illustrates this </p>
<p>sub fred{print &#8220;@_
&#8221;} sub joe{&amp;fred} &amp; joe(1, 2, 3);</p>
<p> This will print </p>
<pre>
    1 2 3
</pre>
<p> What has happened is that <tt>&quot;fred&quot;</tt> accesses the <tt>@_</tt> array which belongs to <tt>&quot;joe&quot;</tt>.</p>
<h3>G_EVAL</h3>
<p> It is possible for the Perl subroutine you are calling to terminate abnormally, e.g., by calling <i>die</i> explicitly or by not actually existing. By default, when either of these events occurs, the process will terminate immediately. If you want to trap this type of event, specify the G_EVAL flag. It will put an <i>eval { }</i> around the subroutine call. </p>
<p> Whenever control returns from the <i>call_*</i> function you need to check the <tt>$@</tt> variable as you would in a normal Perl script. </p>
<p> The value returned from the <i>call_*</i> function is dependent on what other flags have been specified and whether an error has occurred. Here are all the different cases that can occur:</p>
<dl>
<dt>&bull;</p>
<dd> If the <i>call_*</i> function returns normally, then the value returned is as specified in the previous sections.</p>
<dt>&bull;</p>
<dd> If G_DISCARD is specified, the return value will always be 0.</p>
<dt>&bull;</p>
<dd> If G_ARRAY is specified <i>and</i> an error has occurred, the return value will always be 0.</p>
<dt>&bull;</p>
<dd> If G_SCALAR is specified <i>and</i> an error has occurred, the return value will be 1 and the value on the top of the stack will be <i>undef</i>. This means that if you have already detected the error by checking <tt>$@</tt> and you want the program to continue, you must remember to pop the <i>undef</i> from the stack.</dl>
<p> See &#8220;Using G_EVAL&#8221; for details on using G_EVAL.</p>
<h3>G_KEEPERR</h3>
<p> Using the G_EVAL flag described above will always set <tt>$@</tt>: clearing it if there was no error, and setting it to describe the error if there was an error in the called code. This is what you want if your intention is to handle possible errors, but sometimes you just want to trap errors and stop them interfering with the rest of the program. </p>
<p> This scenario will mostly be applicable to code that is meant to be called from within destructors, asynchronous callbacks, and signal handlers. In such situations, where the code being called has little relation to the surrounding dynamic context, the main program needs to be insulated from errors in the called code, even if they can&#8217;t be handled intelligently. It may also be useful to do this with code for <tt>&quot;__DIE__&quot;</tt> or <tt>&quot;__WARN__&quot;</tt> hooks, and <tt>&quot;tie&quot;</tt> functions. </p>
<p> The G_KEEPERR flag is meant to be used in conjunction with G_EVAL in <i>call_*</i> functions that are used to implement such code, or with <tt>&quot;eval_sv&quot;</tt>. This flag has no effect on the <tt>&quot;call_*&quot;</tt> functions when G_EVAL is not used. </p>
<p> When G_KEEPERR is used, any error in the called code will terminate the call as usual, and the error will not propagate beyond the call (as usual for G_EVAL), but it will not go into <tt>$@</tt>. Instead the error will be converted into a warning, prefixed with the string &#8220;	(in cleanup)&#8221;. This can be disabled using <tt>&quot;no warnings 'misc'&quot;</tt>. If there is no error, <tt>$@</tt> will not be cleared. </p>
<p> Note that the G_KEEPERR flag does not propagate into inner evals; these may still set <tt>$@</tt>. </p>
<p> The G_KEEPERR flag was introduced in Perl version 5.002. </p>
<p> See &#8220;Using G_KEEPERR&#8221; for an example of a situation that warrants the use of this flag.</p>
<h3>Determining the Context</h3>
<p> As mentioned above, you can determine the context of the currently executing subroutine in Perl with <i>wantarray</i>. The equivalent test can be made in C by using the <tt>&quot;GIMME_V&quot;</tt> macro, which returns <tt>&quot;G_ARRAY&quot;</tt> if you have been called in a list context, <tt>&quot;G_SCALAR&quot;</tt> if in a scalar context, or <tt>&quot;G_VOID&quot;</tt> if in a void context (i.e., the return value will not be used). An older version of this macro is called <tt>&quot;GIMME&quot;</tt>; in a void context it returns <tt>&quot;G_SCALAR&quot;</tt> instead of <tt>&quot;G_VOID&quot;</tt>. An example of using the <tt>&quot;GIMME_V&quot;</tt> macro is shown in section &#8220;Using <font SIZE="-1">GIMME_V&#8221;</font>.</p>
<h2>EXAMPLES</h2>
<p> Enough of the definition talk! Let&#8217;s have a few examples. </p>
<p> Perl provides many macros to assist in accessing the Perl stack. Wherever possible, these macros should always be used when interfacing to Perl internals. We hope this should make the code less vulnerable to any changes made to Perl in the future. </p>
<p> Another point worth noting is that in the first series of examples I have made use of only the <i>call_pv</i> function. This has been done to keep the code simpler and ease you into the topic. Wherever possible, if the choice is between using <i>call_pv</i> and <i>call_sv</i>, you should always try to use <i>call_sv</i>. See &#8220;Using call_sv&#8221; for details.</p>
<h3>No Parameters, Nothing Returned</h3>
<p> This first trivial example will call a Perl subroutine, <i>PrintUID</i>, to print out the <font SIZE="-1">UID</font> of the process. </p>
<pre>
    sub PrintUID
    {
        print &quot;UID is $&lt;
&quot;;
    }
</pre>
<p> and here is a C function to call it </p>
<p>static void<br />
call_PrintUID()<br />
{<br />
    dSP;<br />
    PUSHMARK(SP);<br />
    call_pv(&#8220;PrintUID&#8221;, G_DISCARD | G_NOARGS);<br />
}</p>
<p> Simple, eh? </p>
<p> A few points to note about this example:</p>
<dl>
<dt>1.</p>
<dd> Ignore <tt>&quot;dSP&quot;</tt> and <tt>&quot;PUSHMARK(SP)&quot;</tt> for now. They will be discussed in the next example.</p>
<dt>2.</p>
<dd> We aren&#8217;t passing any parameters to <i>PrintUID</i> so G_NOARGS can be specified.</p>
<dt>3.</p>
<dd> We aren&#8217;t interested in anything returned from <i>PrintUID</i>, so G_DISCARD is specified. Even if <i>PrintUID</i> was changed to return some value(s), having specified G_DISCARD will mean that they will be wiped by the time control returns from <i>call_pv</i>.</p>
<dt>4.</p>
<dd> As <i>call_pv</i> is being used, the Perl subroutine is specified as a C string. In this case the subroutine name has been &#8216;hard-wired&#8217; into the code.</p>
<dt>5.</p>
<dd> Because we specified G_DISCARD, it is not necessary to check the value returned from <i>call_pv</i>. It will always be 0.</dl>
<h3>Passing Parameters</h3>
<p> Now let&#8217;s make a slightly more complex example. This time we want to call a Perl subroutine, <tt>&quot;LeftString&quot;</tt>, which will take 2 parameters&#8212;a string ($s) and an integer ($n). The subroutine will simply print the first <tt>$n</tt> characters of the string. </p>
<p> So the Perl subroutine would look like this: </p>
<p>sub LeftString<br />
{<br />
    my($s, $n) = @_;<br />
    print substr($s, 0, $n), &#8220;
&#8221;;<br />
}</p>
<p> The C function required to call <i>LeftString</i> would look like this: </p>
<p>static void<br />
    call_LeftString(a, b) char *a;<br />
int b;<br />
{<br />
    dSP;<br />
    ENTER;<br />
    SAVETMPS;<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSVpv(a, 0)));<br />
    PUSHs(sv_2mortal(newSViv(b)));<br />
    PUTBACK;<br />
    call_pv(&#8220;LeftString&#8221;, G_DISCARD);<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> Here are a few notes on the C function <i>call_LeftString</i>.</p>
<dl>
<dt>1.</p>
<dd> Parameters are passed to the Perl subroutine using the Perl stack. This is the purpose of the code beginning with the line <tt>&quot;dSP&quot;</tt> and ending with the line <tt>&quot;PUTBACK&quot;</tt>. The <tt>&quot;dSP&quot;</tt> declares a local copy of the stack pointer. This local copy should <code>always</code> be accessed as <tt>&quot;SP&quot;</tt>.</p>
<dt>2.</p>
<dd> If you are going to put something onto the Perl stack, you need to know where to put it. This is the purpose of the macro <tt>&quot;dSP&quot;</tt>&#8211;it declares and initializes a <i>local</i> copy of the Perl stack pointer. </p>
<p> All the other macros which will be used in this example require you to have used this macro. </p>
<p> The exception to this rule is if you are calling a Perl subroutine directly from an <font SIZE="-1">XSUB</font> function. In this case it is not necessary to use the <tt>&quot;dSP&quot;</tt> macro explicitly&#8212;it will be declared for you automatically.</p>
<dt>3.</p>
<dd> Any parameters to be pushed onto the stack should be bracketed by the <tt>&quot;PUSHMARK&quot;</tt> and <tt>&quot;PUTBACK&quot;</tt> macros. The purpose of these two macros, in this context, is to count the number of parameters you are pushing automatically. Then whenever Perl is creating the <tt>@_</tt> array for the subroutine, it knows how big to make it. </p>
<p> The <tt>&quot;PUSHMARK&quot;</tt> macro tells Perl to make a mental note of the current stack pointer. Even if you aren&#8217;t passing any parameters (like the example shown in the section &#8220;No Parameters, Nothing Returned&#8221;) you must still call the <tt>&quot;PUSHMARK&quot;</tt> macro before you can call any of the <i>call_*</i> functions&#8212;Perl still needs to know that there are no parameters. </p>
<p> The <tt>&quot;PUTBACK&quot;</tt> macro sets the global copy of the stack pointer to be the same as our local copy. If we didn&#8217;t do this, <i>call_pv</i> wouldn&#8217;t know where the two parameters we pushed were&#8212;remember that up to now all the stack pointer manipulation we have done is with our local copy, <i>not</i> the global copy.</p>
<dt>4.</p>
<dd> Next, we come to <font SIZE="-1">EXTEND</font> and PUSHs. This is where the parameters actually get pushed onto the stack. In this case we are pushing a string and an integer. </p>
<p> Alternatively you can use the <code>XPUSHs()</code> macro, which combines a <tt>&quot;EXTEND(SP, 1)&quot;</tt> and <tt>&quot;PUSHs()&quot;</tt>. This is less efficient if you&#8217;re pushing multiple values. </p>
<p> See &#8220;XSUBs and the Argument Stack&#8221; in perlguts for details on how the <font SIZE="-1">PUSH</font> macros work.</p>
<dt>5.</p>
<dd> Because we created temporary values (by means of <code>sv_2mortal()</code> calls) we will have to tidy up the Perl stack and dispose of mortal SVs. </p>
<p> This is the purpose of </p>
<pre>
    ENTER;
    SAVETMPS;
</pre>
<p> at the start of the function, and </p>
<pre>
    FREETMPS;
    LEAVE;
</pre>
<p> at the end. The <tt>&quot;ENTER&quot;</tt>/<tt>&quot;SAVETMPS&quot;</tt> pair creates a boundary for any temporaries we create. This means that the temporaries we get rid of will be limited to those which were created after these calls. </p>
<p> The <tt>&quot;FREETMPS&quot;</tt>/<tt>&quot;LEAVE&quot;</tt> pair will get rid of any values returned by the Perl subroutine (see next example), plus it will also dump the mortal SVs we have created. Having <tt>&quot;ENTER&quot;</tt>/<tt>&quot;SAVETMPS&quot;</tt> at the beginning of the code makes sure that no other mortals are destroyed. </p>
<p> Think of these macros as working a bit like <tt>&quot;{&quot;</tt> and <tt>&quot;}&quot;</tt> in Perl to limit the scope of local variables. </p>
<p> See the section &#8220;Using Perl to Dispose of Temporaries&#8221; for details of an alternative to using these macros.</p>
<dt>6.</p>
<dd> Finally, <i>LeftString</i> can now be called via the <i>call_pv</i> function. The only flag specified this time is G_DISCARD. Because we are passing 2 parameters to the Perl subroutine this time, we have not specified G_NOARGS.</dl>
<h3>Returning a Scalar</h3>
<p> Now for an example of dealing with the items returned from a Perl subroutine. </p>
<p> Here is a Perl subroutine, <i>Adder</i>, that takes 2 integer parameters and simply returns their sum. </p>
<p>sub Adder<br />
{<br />
    my($a, $b) = @_;<br />
    $a + $b;<br />
}</p>
<p> Because we are now concerned with the return value from <i>Adder</i>, the C function required to call it is now a bit more complex. </p>
<p>static void<br />
    call_Adder(a, b) int a;<br />
int b;<br />
{<br />
    dSP;<br />
    int count;<br />
    ENTER;<br />
    SAVETMPS;<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSViv(a)));<br />
    PUSHs(sv_2mortal(newSViv(b)));<br />
    PUTBACK;<br />
    count = call_pv(&#8220;Adder&#8221;, G_SCALAR);<br />
    SPAGAIN;<br />
    if (count != 1)<br />
        croak(&#8220;Big trouble
&#8221;);<br />
    printf(&#8220;The sum of %d and %d is %d
&#8221;, a, b, POPi);<br />
    PUTBACK;<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> Points to note this time are</p>
<dl>
<dt>1.</p>
<dd> The only flag specified this time was G_SCALAR. That means that the <tt>@_</tt> array will be created and that the value returned by <i>Adder</i> will still exist after the call to <i>call_pv</i>.</p>
<dt>2.</p>
<dd> The purpose of the macro <tt>&quot;SPAGAIN&quot;</tt> is to refresh the local copy of the stack pointer. This is necessary because it is possible that the memory allocated to the Perl stack has been reallocated during the <i>call_pv</i> call. </p>
<p> If you are making use of the Perl stack pointer in your code you must always refresh the local copy using <font SIZE="-1">SPAGAIN</font> whenever you make use of the <i>call_*</i> functions or any other Perl internal function.</p>
<dt>3.</p>
<dd> Although only a single value was expected to be returned from <i>Adder</i>, it is still good practice to check the return code from <i>call_pv</i> anyway. </p>
<p> Expecting a single value is not quite the same as knowing that there will be one. If someone modified <i>Adder</i> to return a list and we didn&#8217;t check for that possibility and take appropriate action the Perl stack would end up in an inconsistent state. That is something you <i>really</i> don&#8217;t want to happen ever.</p>
<dt>4.</p>
<dd> The <tt>&quot;POPi&quot;</tt> macro is used here to pop the return value from the stack. In this case we wanted an integer, so <tt>&quot;POPi&quot;</tt> was used. </p>
<p> Here is the complete list of <font SIZE="-1">POP</font> macros available, along with the types they return. </p>
<p>POPs SV<br />
    POPp<br />
    pointer(PV)<br />
POPpbytex pointer to bytes(PV)<br />
POPn double(NV)<br />
    POPi integer(IV)<br />
POPu unsigned integer(UV)<br />
POPl long<br />
    POPul unsigned long</p>
<p> Since these macros have side-effects don&#8217;t use them as arguments to macros that may evaluate their argument several times, for example: </p>
<p>/* Bad idea, don&#8217;t do this */<br />
STRLEN len;<br />
const char *s = SvPV(POPs, len);</p>
<p> Instead, use a temporary: </p>
<p>STRLEN len;<br />
SV *sv = POPs;<br />
const char *s = SvPV(sv, len);</p>
<p> or a macro that guarantees it will evaluate its arguments only once: </p>
<p>STRLEN len;<br />
const char *s = SvPVx(POPs, len);</p>
<dt>5.</p>
<dd> The final <tt>&quot;PUTBACK&quot;</tt> is used to leave the Perl stack in a consistent state before exiting the function. This is necessary because when we popped the return value from the stack with <tt>&quot;POPi&quot;</tt> it updated only our local copy of the stack pointer. Remember, <tt>&quot;PUTBACK&quot;</tt> sets the global stack pointer to be the same as our local copy.</dl>
<h3>Returning a List of Values</h3>
<p> Now, let&#8217;s extend the previous example to return both the sum of the parameters and the difference. </p>
<p> Here is the Perl subroutine </p>
<p>sub AddSubtract<br />
{<br />
    my($a, $b) = @_;<br />
    ($a + $b, $a &#8211; $b);<br />
}</p>
<p> and this is the C function </p>
<p>static void<br />
    call_AddSubtract(a, b) int a;<br />
int b;<br />
{<br />
    dSP;<br />
    int count;<br />
    ENTER;<br />
    SAVETMPS;<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSViv(a)));<br />
    PUSHs(sv_2mortal(newSViv(b)));<br />
    PUTBACK;<br />
    count = call_pv(&#8220;AddSubtract&#8221;, G_ARRAY);<br />
    SPAGAIN;<br />
    if (count != 2)<br />
        croak(&#8220;Big trouble
&#8221;);<br />
    printf(&#8220;%d &#8211; %d = %d
&#8221;, a, b, POPi);<br />
    printf(&#8220;%d + %d = %d
&#8221;, a, b, POPi);<br />
    PUTBACK;<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> If <i>call_AddSubtract</i> is called like this </p>
<pre>
    call_AddSubtract(7, 4);
</pre>
<p> then here is the output </p>
<pre>
    7 - 4 = 3
    7 + 4 = 11
</pre>
<p> Notes</p>
<dl>
<dt>1.</p>
<dd> We wanted list context, so G_ARRAY was used.</p>
<dt>2.</p>
<dd> Not surprisingly <tt>&quot;POPi&quot;</tt> is used twice this time because we were retrieving 2 values from the stack. The important thing to note is that when using the <tt>&quot;POP*&quot;</tt> macros they come off the stack in <i>reverse</i> order.</dl>
<h3>Returning a List in Scalar Context</h3>
<p> Say the Perl subroutine in the previous section was called in a scalar context, like this </p>
<p>static void<br />
    call_AddSubScalar(a, b) int a;<br />
int b;<br />
{<br />
    dSP;<br />
    int count;<br />
    int i;<br />
    ENTER;<br />
    SAVETMPS;<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSViv(a)));<br />
    PUSHs(sv_2mortal(newSViv(b)));<br />
    PUTBACK;<br />
    count = call_pv(&#8220;AddSubtract&#8221;, G_SCALAR);<br />
    SPAGAIN;<br />
    printf(&#8220;Items Returned = %d
&#8221;, count);<br />
    for (i = 1; i &lt;= count; ++i)<br />
        printf(&#8220;Value %d = %d
&#8221;, i, POPi);<br />
    PUTBACK;<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> The other modification made is that <i>call_AddSubScalar</i> will print the number of items returned from the Perl subroutine and their value (for simplicity it assumes that they are integer). So if <i>call_AddSubScalar</i> is called </p>
<pre>
    call_AddSubScalar(7, 4);
</pre>
<p> then the output will be </p>
<pre>
    Items Returned = 1
    Value 1 = 3
</pre>
<p> In this case the main point to note is that only the last item in the list is returned from the subroutine. <i>AddSubtract</i> actually made it back to <i>call_AddSubScalar</i>.</p>
<h3>Returning Data from Perl via the Parameter List</h3>
<p> It is also possible to return values directly via the parameter list&#8212;whether it is actually desirable to do it is another matter entirely. </p>
<p> The Perl subroutine, <i>Inc</i>, below takes 2 parameters and increments each directly. </p>
<p>sub Inc<br />
{<br />
    ++$_[0];<br />
    ++$_[1];<br />
}</p>
<p> and here is a C function to call it. </p>
<p>static void<br />
    call_Inc(a, b) int a;<br />
int b;<br />
{<br />
    dSP;<br />
    int count;<br />
    SV *sva;<br />
    SV *svb;<br />
    ENTER;<br />
    SAVETMPS;<br />
    sva = sv_2mortal(newSViv(a));<br />
    svb = sv_2mortal(newSViv(b));<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sva);<br />
    PUSHs(svb);<br />
    PUTBACK;<br />
    count = call_pv(&#8220;Inc&#8221;, G_DISCARD);<br />
    if (count != 0)<br />
        croak(&#8220;call_Inc: expected 0 values from &#8216;Inc&#8217;, got %d
&#8221;,<br />
              count);<br />
    printf(&#8220;%d + 1 = %d
&#8221;, a, SvIV(sva));<br />
    printf(&#8220;%d + 1 = %d
&#8221;, b, SvIV(svb));<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> To be able to access the two parameters that were pushed onto the stack after they return from <i>call_pv</i> it is necessary to make a note of their addresses&#8212;thus the two variables <tt>&quot;sva&quot;</tt> and <tt>&quot;svb&quot;</tt>. </p>
<p> The reason this is necessary is that the area of the Perl stack which held them will very likely have been overwritten by something else by the time control returns from <i>call_pv</i>.</p>
<h3>Using G_EVAL</h3>
<p> Now an example using G_EVAL. Below is a Perl subroutine which computes the difference of its 2 parameters. If this would result in a negative result, the subroutine calls <i>die</i>. </p>
<p>sub Subtract<br />
{<br />
    my($a, $b) = @_;<br />
    die &#8220;death can be fatal
&#8221; if $a &lt; $b;<br />
    $a &#8211; $b;<br />
}</p>
<p> and some C to call it </p>
<p>static void<br />
    call_Subtract(a, b) int a;<br />
int b;<br />
{<br />
    dSP;<br />
    int count;<br />
    SV *err_tmp;<br />
    ENTER;<br />
    SAVETMPS;<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSViv(a)));<br />
    PUSHs(sv_2mortal(newSViv(b)));<br />
    PUTBACK;<br />
    count = call_pv(&#8220;Subtract&#8221;, G_EVAL | G_SCALAR);<br />
    SPAGAIN;<br />
    /* Check the eval first */<br />
    err_tmp = ERRSV;<br />
    if (SvTRUE(err_tmp)) {<br />
        printf(&#8220;Uh oh &#8211; %s
&#8221;, SvPV_nolen(err_tmp));<br />
        POPs;<br />
    } else {<br />
        if (count != 1)<br />
            croak(&#8220;call_Subtract: wanted 1 value from &#8216;Subtract&#8217;, got %d
&#8221;,<br />
                  count);<br />
        printf(&#8220;%d &#8211; %d = %d
&#8221;, a, b, POPi);<br />
    }<br />
    PUTBACK;<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> If <i>call_Subtract</i> is called thus </p>
<pre>
    call_Subtract(4, 5)
</pre>
<p> the following will be printed </p>
<pre>
    Uh oh - death can be fatal
</pre>
<p> Notes</p>
<dl>
<dt>1.</p>
<dd> We want to be able to catch the <i>die</i> so we have used the G_EVAL flag. Not specifying this flag would mean that the program would terminate immediately at the <i>die</i> statement in the subroutine <i>Subtract</i>.</p>
<dt>2.</p>
<dd> The code </p>
<p>err_tmp = ERRSV;<br />
if (SvTRUE(err_tmp)) {<br />
    printf(&#8220;Uh oh &#8211; %s
&#8221;, SvPV_nolen(err_tmp));<br />
    POPs;<br />
}</p>
<p> is the direct equivalent of this bit of Perl </p>
<pre>
    print &quot;Uh oh - $@
&quot; if $@;
</pre>
<p> <tt>&quot;PL_errgv&quot;</tt> is a perl global of type <tt>&quot;GV *&quot;</tt> that points to the symbol table entry containing the error. <tt>&quot;ERRSV&quot;</tt> therefore refers to the C equivalent of <tt>$@</tt>. We use a local temporary, <tt>&quot;err_tmp&quot;</tt>, since <tt>&quot;ERRSV&quot;</tt> is a macro that calls a function, and <tt>&quot;SvTRUE(ERRSV)&quot;</tt> would end up calling that function multiple times.</p>
<dt>3.</p>
<dd> Note that the stack is popped using <tt>&quot;POPs&quot;</tt> in the block where <tt>&quot;SvTRUE(err_tmp)&quot;</tt> is true. This is necessary because whenever a <i>call_*</i> function invoked with G_EVAL|G_SCALAR returns an error, the top of the stack holds the value <i>undef</i>. Because we want the program to continue after detecting this error, it is essential that the stack be tidied up by removing the <i>undef</i>.</dl>
<h3>Using G_KEEPERR</h3>
<p> Consider this rather facetious example, where we have used an <font SIZE="-1">XS</font> version of the call_Subtract example above inside a destructor: </p>
<p>package Foo;<br />
sub new {bless{}, $_[0]} sub Subtract<br />
{<br />
    my($a, $b) = @_;<br />
    die &#8220;death can be fatal&#8221; if $a &lt; $b;<br />
    $a &#8211; $b;<br />
}<br />
sub DESTROY<br />
{<br />
    call_Subtract(5, 4);<br />
}<br />
sub foo<br />
{<br />
    die &#8220;foo dies&#8221;;<br />
}<br />
package main;<br />
{<br />
    my $foo = Foo-&gt;new;<br />
    eval{$foo-&gt;foo};<br />
}<br />
print &#8220;Saw: $@&#8221; if $ @;<br />
#should be, but isn&#8217;t</p>
<p> This example will fail to recognize that an error occurred inside the <tt>&quot;eval {}&quot;</tt>. Here&#8217;s why: the call_Subtract code got executed while perl was cleaning up temporaries when exiting the outer braced block, and because call_Subtract is implemented with <i>call_pv</i> using the G_EVAL flag, it promptly reset <tt>$@</tt>. This results in the failure of the outermost test for <tt>$@</tt>, and thereby the failure of the error trap. </p>
<p> Appending the G_KEEPERR flag, so that the <i>call_pv</i> call in call_Subtract reads: </p>
<pre>
        count = call_pv(&quot;Subtract&quot;, G_EVAL|G_SCALAR|G_KEEPERR);
</pre>
<p> will preserve the error and restore reliable error handling.</p>
<h3>Using call_sv</h3>
<p> In all the previous examples I have &#8216;hard-wired&#8217; the name of the Perl subroutine to be called from C. Most of the time though, it is more convenient to be able to specify the name of the Perl subroutine from within the Perl script, and you&#8217;ll want to use call_sv. </p>
<p> Consider the Perl code below </p>
<p>sub fred<br />
{<br />
    print &#8220;Hello there
&#8221;;<br />
}<br />
CallSubPV(&#8220;fred&#8221;);</p>
<p> Here is a snippet of <font SIZE="-1">XSUB</font> which defines <i>CallSubPV</i>. </p>
<p>void<br />
    CallSubPV(name) char *name<br />
    CODE : PUSHMARK(SP);<br />
call_pv(name, G_DISCARD | G_NOARGS);</p>
<p> That is fine as far as it goes. The thing is, the Perl subroutine can be specified as only a string, however, Perl allows references to subroutines and anonymous subroutines. This is where <i>call_sv</i> is useful. </p>
<p> The code below for <i>CallSubSV</i> is identical to <i>CallSubPV</i> except that the <tt>&quot;name&quot;</tt> parameter is now defined as an SV* and we use <i>call_sv</i> instead of <i>call_pv</i>. </p>
<p>void<br />
    CallSubSV(name)<br />
        SV *name<br />
    CODE : PUSHMARK(SP);<br />
call_sv(name, G_DISCARD | G_NOARGS);</p>
<p> Because we are using an <font SIZE="-1">SV</font> to call <i>fred</i> the following can all be used: </p>
<p>CallSubSV(&#8220;fred&#8221;);<br />
CallSubSV(\&amp;fred);<br />
$ref = \&amp; fred;<br />
CallSubSV($ref);<br />
CallSubSV(sub{print &#8220;Hello there
&#8221;});</p>
<p> As you can see, <i>call_sv</i> gives you much greater flexibility in how you can specify the Perl subroutine. </p>
<p> You should note that, if it is necessary to store the <font SIZE="-1">SV</font> (<tt>&quot;name&quot;</tt> in the example above) which corresponds to the Perl subroutine so that it can be used later in the program, it not enough just to store a copy of the pointer to the <font SIZE="-1">SV.</font> Say the code above had been like this: </p>
<p>static SV *rememberSub;<br />
void<br />
    SaveSub1(name)<br />
        SV *name<br />
    CODE : rememberSub = name;<br />
void CallSavedSub1()<br />
    CODE : PUSHMARK(SP);<br />
call_sv(rememberSub, G_DISCARD | G_NOARGS);</p>
<p> The reason this is wrong is that, by the time you come to use the pointer <tt>&quot;rememberSub&quot;</tt> in <tt>&quot;CallSavedSub1&quot;</tt>, it may or may not still refer to the Perl subroutine that was recorded in <tt>&quot;SaveSub1&quot;</tt>. This is particularly true for these cases: </p>
<p>SaveSub1(\&amp;fred);<br />
CallSavedSub1();<br />
SaveSub1(sub{print &#8220;Hello there
&#8221;});<br />
CallSavedSub1();</p>
<p> By the time each of the <tt>&quot;SaveSub1&quot;</tt> statements above has been executed, the SV*s which corresponded to the parameters will no longer exist. Expect an error message from Perl of the form </p>
<pre>
    Can't use an undefined value as a subroutine reference at ...
</pre>
<p> for each of the <tt>&quot;CallSavedSub1&quot;</tt> lines. </p>
<p> Similarly, with this code </p>
<p>$ref = \&amp; fred;<br />
SaveSub1($ref);<br />
$ref = 47;<br />
CallSavedSub1();</p>
<p> you can expect one of these messages (which you actually get is dependent on the version of Perl you are using) </p>
<pre>
    Not a CODE reference at ...
    Undefined subroutine &amp;main::47 called ...
</pre>
<p> The variable <tt>$ref</tt> may have referred to the subroutine <tt>&quot;fred&quot;</tt> whenever the call to <tt>&quot;SaveSub1&quot;</tt> was made but by the time <tt>&quot;CallSavedSub1&quot;</tt> gets called it now holds the number <tt>47</tt>. Because we saved only a pointer to the original <font SIZE="-1">SV</font> in <tt>&quot;SaveSub1&quot;</tt>, any changes to <tt>$ref</tt> will be tracked by the pointer <tt>&quot;rememberSub&quot;</tt>. This means that whenever <tt>&quot;CallSavedSub1&quot;</tt> gets called, it will attempt to execute the code which is referenced by the SV* <tt>&quot;rememberSub&quot;</tt>. In this case though, it now refers to the integer <tt>47</tt>, so expect Perl to complain loudly. </p>
<p> A similar but more subtle problem is illustrated with this code: </p>
<p>$ref = \&amp; fred;<br />
SaveSub1($ref);<br />
$ref = \&amp; joe;<br />
CallSavedSub1();</p>
<p> This time whenever <tt>&quot;CallSavedSub1&quot;</tt> gets called it will execute the Perl subroutine <tt>&quot;joe&quot;</tt> (assuming it exists) rather than <tt>&quot;fred&quot;</tt> as was originally requested in the call to <tt>&quot;SaveSub1&quot;</tt>. </p>
<p> To get around these problems it is necessary to take a full copy of the <font SIZE="-1">SV.</font> The code below shows <tt>&quot;SaveSub2&quot;</tt> modified to do that. </p>
<p>/* this isn&#8217;t thread-safe */<br />
static SV *keepSub = (SV *)NULL;<br />
void<br />
    SaveSub2(name)<br />
        SV *name<br />
    CODE :<br />
    /* Take a copy of the callback */<br />
    if (keepSub == (SV *)NULL)<br />
    /* First time, so create a new SV */<br />
    keepSub = newSVsv(name);<br />
else<br />
    /* Been here before, so overwrite */<br />
    SvSetSV(keepSub, name);<br />
void CallSavedSub2()<br />
    CODE : PUSHMARK(SP);<br />
call_sv(keepSub, G_DISCARD | G_NOARGS);</p>
<p> To avoid creating a new <font SIZE="-1">SV</font> every time <tt>&quot;SaveSub2&quot;</tt> is called, the function first checks to see if it has been called before. If not, then space for a new <font SIZE="-1">SV</font> is allocated and the reference to the Perl subroutine <tt>&quot;name&quot;</tt> is copied to the variable <tt>&quot;keepSub&quot;</tt> in one operation using <tt>&quot;newSVsv&quot;</tt>. Thereafter, whenever <tt>&quot;SaveSub2&quot;</tt> is called, the existing <font SIZE="-1">SV,</font> <tt>&quot;keepSub&quot;</tt>, is overwritten with the new value using <tt>&quot;SvSetSV&quot;</tt>. </p>
<p> Note: using a static or global variable to store the <font SIZE="-1">SV</font> isn&#8217;t thread-safe. You can either use the <tt>&quot;MY_CXT&quot;</tt> mechanism documented in &#8220;Safely Storing Static Data in <font SIZE="-1">XS&#8221;</font> in perlxs which is fast, or store the values in perl global variables, using <code>get_sv()</code>, which is much slower.</p>
<h3>Using call_argv</h3>
<p> Here is a Perl subroutine which prints whatever parameters are passed to it. </p>
<p>sub PrintList<br />
{<br />
    my(@list) = @_;<br />
    foreach (@list) {<br />
        print &#8220;$_
&#8221;<br />
    }<br />
}</p>
<p> And here is an example of <i>call_argv</i> which will call <i>PrintList</i>. </p>
<p>static char *words[] = {&#8220;alpha&#8221;, &#8220;beta&#8221;, &#8220;gamma&#8221;, &#8220;delta&#8221;, NULL};<br />
static void<br />
call_PrintList()<br />
{<br />
    call_argv(&#8220;PrintList&#8221;, G_DISCARD, words);<br />
}</p>
<p> Note that it is not necessary to call <tt>&quot;PUSHMARK&quot;</tt> in this instance. This is because <i>call_argv</i> will do it for you.</p>
<h3>Using call_method</h3>
<p> Consider the following Perl code: </p>
<p>{<br />
    package Mine;<br />
    sub new<br />
    {<br />
        my($type) = shift;<br />
        bless[@_]<br />
    }<br />
    sub Display<br />
    {<br />
        my($self, $index) = @_;<br />
        print &#8220;$index: $$self[$index]
&#8221;;<br />
    }<br />
    sub PrintID<br />
    {<br />
        my($class) = @_;<br />
        print &#8220;This is Class $class version 1.0
&#8221;;<br />
    }<br />
}</p>
<p> It implements just a very simple class to manage an array. Apart from the constructor, <tt>&quot;new&quot;</tt>, it declares methods, one static and one virtual. The static method, <tt>&quot;PrintID&quot;</tt>, prints out simply the class name and a version number. The virtual method, <tt>&quot;Display&quot;</tt>, prints out a single element of the array. Here is an all-Perl example of using it. </p>
<p>$a = Mine-&gt;new (&#8216;red&#8217;, &#8216;green&#8217;, &#8216;blue&#8217;);<br />
$a-&gt;Display(1);<br />
Mine-&gt;PrintID;</p>
<p> will print </p>
<pre>
    1: green
    This is Class Mine version 1.0
</pre>
<p> Calling a Perl method from C is fairly straightforward. The following things are required:</p>
<dl>
<dt>&bull;</p>
<dd> A reference to the object for a virtual method or the name of the class for a static method</p>
<dt>&bull;</p>
<dd> The name of the method</p>
<dt>&bull;</p>
<dd> Any other parameters specific to the method</dl>
<p> Here is a simple <font SIZE="-1">XSUB</font> which illustrates the mechanics of calling both the <tt>&quot;PrintID&quot;</tt> and <tt>&quot;Display&quot;</tt> methods from C. </p>
<p>void<br />
    call_Method(ref, method, index)<br />
        SV *ref<br />
    char *method<br />
    int index<br />
    CODE : PUSHMARK(SP);<br />
EXTEND(SP, 2);<br />
PUSHs(ref);<br />
PUSHs(sv_2mortal(newSViv(index)));<br />
PUTBACK;<br />
call_method(method, G_DISCARD);<br />
void<br />
    call_PrintID(class, method) char *class<br />
    char *method<br />
    CODE : PUSHMARK(SP);<br />
XPUSHs(sv_2mortal(newSVpv(class, 0)));<br />
PUTBACK;<br />
call_method(method, G_DISCARD);</p>
<p> So the methods <tt>&quot;PrintID&quot;</tt> and <tt>&quot;Display&quot;</tt> can be invoked like this: </p>
<p>$a = Mine-&gt;new (&#8216;red&#8217;, &#8216;green&#8217;, &#8216;blue&#8217;);<br />
call_Method($a, &#8216;Display&#8217;, 1);<br />
call_PrintID(&#8216;Mine&#8217;, &#8216;PrintID&#8217;);</p>
<p> The only thing to note is that, in both the static and virtual methods, the method name is not passed via the stack&#8212;it is used as the first parameter to <i>call_method</i>.</p>
<h3>Using <font SIZE="-1">GIMME_V</font></h3>
<p> Here is a trivial <font SIZE="-1">XSUB</font> which prints the context in which it is currently executing. </p>
<p>void PrintContext()<br />
    CODE : U8 gimme = GIMME_V;<br />
if (gimme == G_VOID)<br />
    printf(&#8220;Context is Void
&#8221;);<br />
else if (gimme == G_SCALAR)<br />
    printf(&#8220;Context is Scalar
&#8221;);<br />
else<br />
    printf(&#8220;Context is Array
&#8221;);</p>
<p> And here is some Perl to test it. </p>
<pre>
    PrintContext;
    $a = PrintContext;
    @a = PrintContext;
</pre>
<p> The output from that will be </p>
<pre>
    Context is Void
    Context is Scalar
    Context is Array
</pre>
<h3>Using Perl to Dispose of Temporaries</h3>
<p> In the examples given to date, any temporaries created in the callback (i.e., parameters passed on the stack to the <i>call_*</i> function or values returned via the stack) have been freed by one of these methods:</p>
<dl>
<dt>&bull;</p>
<dd> Specifying the G_DISCARD flag with <i>call_*</i></p>
<dt>&bull;</p>
<dd> Explicitly using the <tt>&quot;ENTER&quot;</tt>/<tt>&quot;SAVETMPS&quot;</tt>&#8212;<tt>&quot;FREETMPS&quot;</tt>/<tt>&quot;LEAVE&quot;</tt> pairing</dl>
<p> There is another method which can be used, namely letting Perl do it for you automatically whenever it regains control after the callback has terminated. This is done by simply not using the </p>
<p>ENTER;<br />
SAVETMPS;<br />
&#8230; FREETMPS;<br />
LEAVE;</p>
<p> sequence in the callback (and not, of course, specifying the G_DISCARD flag). </p>
<p> If you are going to use this method you have to be aware of a possible memory leak which can arise under very specific circumstances. To explain these circumstances you need to know a bit about the flow of control between Perl and the callback routine. </p>
<p> The examples given at the start of the document (an error handler and an event driven program) are typical of the two main sorts of flow control that you are likely to encounter with callbacks. There is a very important distinction between them, so pay attention. </p>
<p> In the first example, an error handler, the flow of control could be as follows. You have created an interface to an external library. Control can reach the external library like this </p>
<pre>
    perl --&gt; XSUB --&gt; external library
</pre>
<p> Whilst control is in the library, an error condition occurs. You have previously set up a Perl callback to handle this situation, so it will get executed. Once the callback has finished, control will drop back to Perl again. Here is what the flow of control will be like in that situation </p>
<p>perl&#8211; &gt; XSUB&#8211; &gt; external library&#8230; error occurs&#8230; external library&#8211; &gt; call_ * &#8212; &gt; perl |<br />
    perl &lt; &#8211;XSUB &lt; &#8211;external library &lt; &#8211;call_ * &lt; &#8212; &#8211;+</p>
<p> After processing of the error using <i>call_*</i> is completed, control reverts back to Perl more or less immediately. </p>
<p> In the diagram, the further right you go the more deeply nested the scope is. It is only when control is back with perl on the extreme left of the diagram that you will have dropped back to the enclosing scope and any temporaries you have left hanging around will be freed. </p>
<p> In the second example, an event driven program, the flow of control will be more like this </p>
<p>perl&#8211; &gt; XSUB&#8211; &gt; event handler&#8230; event handler&#8211; &gt; call_ * &#8212; &gt; perl |<br />
    event handler&lt;&#8211;call_ *&lt;&#8211; &#8211;+&#8230; event handler&#8211;&gt; call_ * &#8211;&gt; perl |<br />
    event handler&lt;&#8211;call_ *&lt;&#8211; &#8211;+&#8230; event handler&#8211;&gt; call_ * &#8211;&gt; perl |<br />
    event handler &lt; &#8211;call_ * &lt; &#8212; &#8211;+</p>
<p> In this case the flow of control can consist of only the repeated sequence </p>
<pre>
    event handler --&gt; call_* --&gt; perl
</pre>
<p> for practically the complete duration of the program. This means that control may <i>never</i> drop back to the surrounding scope in Perl at the extreme left. </p>
<p> So what is the big problem? Well, if you are expecting Perl to tidy up those temporaries for you, you might be in for a long wait. For Perl to dispose of your temporaries, control must drop back to the enclosing scope at some stage. In the event driven scenario that may never happen. This means that, as time goes on, your program will create more and more temporaries, none of which will ever be freed. As each of these temporaries consumes some memory your program will eventually consume all the available memory in your system&#8212;kapow! </p>
<p> So here is the bottom line&#8212;if you are sure that control will revert back to the enclosing Perl scope fairly quickly after the end of your callback, then it isn&#8217;t absolutely necessary to dispose explicitly of any temporaries you may have created. Mind you, if you are at all uncertain about what to do, it doesn&#8217;t do any harm to tidy up anyway.</p>
<h3>Strategies for Storing Callback Context Information</h3>
<p> Potentially one of the trickiest problems to overcome when designing a callback interface can be figuring out how to store the mapping between the C callback function and the Perl equivalent. </p>
<p> To help understand why this can be a real problem first consider how a callback is set up in an all C environment. Typically a C <font SIZE="-1">API</font> will provide a function to register a callback. This will expect a pointer to a function as one of its parameters. Below is a call to a hypothetical function <tt>&quot;register_fatal&quot;</tt> which registers the C function to get called when a fatal error occurs. </p>
<pre>
    register_fatal(cb1);
</pre>
<p> The single parameter <tt>&quot;cb1&quot;</tt> is a pointer to a function, so you must have defined <tt>&quot;cb1&quot;</tt> in your code, say something like this </p>
<p>static void<br />
cb1()<br />
{<br />
    printf(&#8220;Fatal Error
&#8221;);<br />
    exit(1);<br />
}</p>
<p> Now change that to call a Perl subroutine instead </p>
<p>static SV *callback = (SV *)NULL;<br />
static void<br />
cb1()<br />
{<br />
    dSP;<br />
    PUSHMARK(SP);<br />
    /* Call the Perl sub to process the callback */<br />
    call_sv(callback, G_DISCARD);<br />
}<br />
void<br />
    register_fatal(fn)<br />
        SV *fn<br />
    CODE :<br />
    /* Remember the Perl sub */<br />
    if (callback == (SV *)NULL)<br />
        callback = newSVsv(fn);<br />
else SvSetSV(callback, fn);<br />
/* register the callback with the external library */<br />
register_fatal(cb1);</p>
<p> where the Perl equivalent of <tt>&quot;register_fatal&quot;</tt> and the callback it registers, <tt>&quot;pcb1&quot;</tt>, might look like this </p>
<p>#Register the sub pcb1<br />
register_fatal(\&amp;pcb1);<br />
sub pcb1<br />
{<br />
    die &#8220;I&#8217;m dying&#8230;
&#8221;;<br />
}</p>
<p> The mapping between the C callback and the Perl equivalent is stored in the global variable <tt>&quot;callback&quot;</tt>. </p>
<p> This will be adequate if you ever need to have only one callback registered at any time. An example could be an error handler like the code sketched out above. Remember though, repeated calls to <tt>&quot;register_fatal&quot;</tt> will replace the previously registered callback function with the new one. </p>
<p> Say for example you want to interface to a library which allows asynchronous file i/o. In this case you may be able to register a callback whenever a read operation has completed. To be of any use we want to be able to call separate Perl subroutines for each file that is opened. As it stands, the error handler example above would not be adequate as it allows only a single callback to be defined at any time. What we require is a means of storing the mapping between the opened file and the Perl subroutine we want to be called for that file. </p>
<p> Say the i/o library has a function <tt>&quot;asynch_read&quot;</tt> which associates a C function <tt>&quot;ProcessRead&quot;</tt> with a file handle <tt>&quot;fh&quot;</tt>&#8211;this assumes that it has also provided some routine to open the file and so obtain the file handle. </p>
<pre>
    asynch_read(fh, ProcessRead)
</pre>
<p> This may expect the C <i>ProcessRead</i> function of this form </p>
<p>void<br />
    ProcessRead(fh, buffer) int fh;<br />
char *buffer;<br />
{<br />
    &#8230;<br />
}</p>
<p> To provide a Perl interface to this library we need to be able to map between the <tt>&quot;fh&quot;</tt> parameter and the Perl subroutine we want called. A hash is a convenient mechanism for storing this mapping. The code below shows a possible implementation </p>
<p>static HV *Mapping = (HV *)NULL;<br />
void<br />
    asynch_read(fh, callback) int fh<br />
    SV *callback<br />
    CODE :<br />
    /* If the hash doesn&#8217;t already exist, create it */<br />
    if (Mapping == (HV *)NULL)<br />
        Mapping = newHV();<br />
/* Save the fh -&gt; callback mapping */<br />
hv_store(Mapping, (char *)&amp;fh, sizeof(fh), newSVsv(callback), 0);<br />
/* Register with the C Library */<br />
asynch_read(fh, asynch_read_if);</p>
<p> and <tt>&quot;asynch_read_if&quot;</tt> could look like this </p>
<p>static void<br />
    asynch_read_if(fh, buffer) int fh;<br />
char *buffer;<br />
{<br />
    dSP;<br />
    SV **sv;<br />
    /* Get the callback associated with fh */<br />
    sv = hv_fetch(Mapping, (char *)&amp;fh, sizeof(fh), FALSE);<br />
    if (sv == (SV **)NULL)<br />
        croak(&#8220;Internal error&#8230;
&#8221;);<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSViv(fh)));<br />
    PUSHs(sv_2mortal(newSVpv(buffer, 0)));<br />
    PUTBACK;<br />
    /* Call the Perl sub */<br />
    call_sv(*sv, G_DISCARD);<br />
}</p>
<p> For completeness, here is <tt>&quot;asynch_close&quot;</tt>. This shows how to remove the entry from the hash <tt>&quot;Mapping&quot;</tt>. </p>
<p>void<br />
    asynch_close(fh) int fh<br />
    CODE :<br />
    /* Remove the entry from the hash */<br />
    (void)hv_delete(Mapping, (char *)&amp;fh, sizeof(fh), G_DISCARD);<br />
/* Now call the real asynch_close */<br />
asynch_close(fh);</p>
<p> So the Perl interface would look like this </p>
<p>sub callback1<br />
{<br />
    my($handle, $buffer) = @_;<br />
}<br />
#Register the Perl callback<br />
asynch_read($fh, \&amp;callback1);<br />
asynch_close($fh);</p>
<p> The mapping between the C callback and Perl is stored in the global hash <tt>&quot;Mapping&quot;</tt> this time. Using a hash has the distinct advantage that it allows an unlimited number of callbacks to be registered. </p>
<p> What if the interface provided by the C callback doesn&#8217;t contain a parameter which allows the file handle to Perl subroutine mapping? Say in the asynchronous i/o package, the callback function gets passed only the <tt>&quot;buffer&quot;</tt> parameter like this </p>
<p>void<br />
    ProcessRead(buffer) char *buffer;<br />
{<br />
    &#8230;<br />
}</p>
<p> Without the file handle there is no straightforward way to map from the C callback to the Perl subroutine. </p>
<p> In this case a possible way around this problem is to predefine a series of C functions to act as the interface to Perl, thus </p>
<p>#define MAX_CB 3<br />
#define NULL_HANDLE -1<br />
typedef void (*FnMap)();<br />
struct MapStruct {<br />
    FnMap Function;<br />
    SV *PerlSub;<br />
    int Handle;<br />
};<br />
static void fn1();<br />
static void fn2();<br />
static void fn3();<br />
static struct MapStruct Map[MAX_CB] =<br />
    {<br />
        {fn1, NULL, NULL_HANDLE},<br />
        {fn2, NULL, NULL_HANDLE},<br />
        {fn3, NULL, NULL_HANDLE}};<br />
static void<br />
    Pcb(index, buffer) int index;<br />
char *buffer;<br />
{<br />
    dSP;<br />
    PUSHMARK(SP);<br />
    XPUSHs(sv_2mortal(newSVpv(buffer, 0)));<br />
    PUTBACK;<br />
    /* Call the Perl sub */<br />
    call_sv(Map[index].PerlSub, G_DISCARD);<br />
}<br />
static void<br />
    fn1(buffer) char *buffer;<br />
{<br />
    Pcb(0, buffer);<br />
}<br />
static void<br />
    fn2(buffer) char *buffer;<br />
{<br />
    Pcb(1, buffer);<br />
}<br />
static void<br />
    fn3(buffer) char *buffer;<br />
{<br />
    Pcb(2, buffer);<br />
}<br />
void<br />
    array_asynch_read(fh, callback) int fh<br />
    SV *callback<br />
    CODE : int index;<br />
int null_index = MAX_CB;<br />
/* Find the same handle or an empty entry */<br />
for (index = 0; index &lt; MAX_CB; ++index) {<br />
    if (Map[index].Handle == fh)<br />
        break;<br />
    if (Map[index].Handle == NULL_HANDLE)<br />
        null_index = index;<br />
}<br />
if (index == MAX_CB &amp;&amp; null_index == MAX_CB)<br />
    croak(&#8220;Too many callback functions registered
&#8221;);<br />
if (index == MAX_CB)<br />
    index = null_index;<br />
/* Save the file handle */<br />
Map[index].Handle = fh;<br />
/* Remember the Perl sub */<br />
if (Map[index].PerlSub == (SV *)NULL)<br />
    Map[index].PerlSub = newSVsv(callback);<br />
else<br />
    SvSetSV(Map[index].PerlSub, callback);<br />
asynch_read(fh, Map[index].Function);<br />
void<br />
    array_asynch_close(fh) int fh<br />
    CODE : int index;<br />
/* Find the file handle */<br />
for (index = 0; index &lt; MAX_CB; ++index)<br />
    if (Map[index].Handle == fh)<br />
        break;<br />
if (index == MAX_CB)<br />
    croak(&#8220;could not close fh %d
&#8221;, fh);<br />
Map[index].Handle = NULL_HANDLE;<br />
SvREFCNT_dec(Map[index].PerlSub);<br />
Map[index].PerlSub = (SV *)NULL;<br />
asynch_close(fh);</p>
<p> In this case the functions <tt>&quot;fn1&quot;</tt>, <tt>&quot;fn2&quot;</tt>, and <tt>&quot;fn3&quot;</tt> are used to remember the Perl subroutine to be called. Each of the functions holds a separate hard-wired index which is used in the function <tt>&quot;Pcb&quot;</tt> to access the <tt>&quot;Map&quot;</tt> array and actually call the Perl subroutine. </p>
<p> There are some obvious disadvantages with this technique. </p>
<p> Firstly, the code is considerably more complex than with the previous example. </p>
<p> Secondly, there is a hard-wired limit (in this case 3) to the number of callbacks that can exist simultaneously. The only way to increase the limit is by modifying the code to add more functions and then recompiling. None the less, as long as the number of functions is chosen with some care, it is still a workable solution and in some cases is the only one available. </p>
<p> To summarize, here are a number of possible methods for you to consider for storing the mapping between C and the Perl callback</p>
<dl>
<dt>1. Ignore the problem &#8211; Allow only 1 callback</p>
<dd> For a lot of situations, like interfacing to an error handler, this may be a perfectly adequate solution.</p>
<dt>2. Create a sequence of callbacks &#8211; hard wired limit</p>
<dd> If it is impossible to tell from the parameters passed back from the C callback what the context is, then you may need to create a sequence of C callback interface functions, and store pointers to each in an array.</p>
<dt>3. Use a parameter to map to the Perl callback</p>
<dd> A hash is an ideal mechanism to store the mapping between C and Perl.</dl>
<h3>Alternate Stack Manipulation</h3>
<p> Although I have made use of only the <tt>&quot;POP*&quot;</tt> macros to access values returned from Perl subroutines, it is also possible to bypass these macros and read the stack using the <tt>&quot;ST&quot;</tt> macro (See perlxs for a full description of the <tt>&quot;ST&quot;</tt> macro). </p>
<p> Most of the time the <tt>&quot;POP*&quot;</tt> macros should be adequate; the main problem with them is that they force you to process the returned values in sequence. This may not be the most suitable way to process the values in some cases. What we want is to be able to access the stack in a random order. The <tt>&quot;ST&quot;</tt> macro as used when coding an <font SIZE="-1">XSUB</font> is ideal for this purpose. </p>
<p> The code below is the example given in the section &#8220;Returning a List of Values&#8221; recoded to use <tt>&quot;ST&quot;</tt> instead of <tt>&quot;POP*&quot;</tt>. </p>
<p>static void<br />
    call_AddSubtract2(a, b) int a;<br />
int b;<br />
{<br />
    dSP;<br />
    I32 ax;<br />
    int count;<br />
    ENTER;<br />
    SAVETMPS;<br />
    PUSHMARK(SP);<br />
    EXTEND(SP, 2);<br />
    PUSHs(sv_2mortal(newSViv(a)));<br />
    PUSHs(sv_2mortal(newSViv(b)));<br />
    PUTBACK;<br />
    count = call_pv(&#8220;AddSubtract&#8221;, G_ARRAY);<br />
    SPAGAIN;<br />
    SP -= count;<br />
    ax = (SP &#8211; PL_stack_base) + 1;<br />
    if (count != 2)<br />
        croak(&#8220;Big trouble
&#8221;);<br />
    printf(&#8220;%d + %d = %d
&#8221;, a, b, SvIV(ST(0)));<br />
    printf(&#8220;%d &#8211; %d = %d
&#8221;, a, b, SvIV(ST(1)));<br />
    PUTBACK;<br />
    FREETMPS;<br />
    LEAVE;<br />
}</p>
<p> Notes</p>
<dl>
<dt>1.</p>
<dd> Notice that it was necessary to define the variable <tt>&quot;ax&quot;</tt>. This is because the <tt>&quot;ST&quot;</tt> macro expects it to exist. If we were in an <font SIZE="-1">XSUB</font> it would not be necessary to define <tt>&quot;ax&quot;</tt> as it is already defined for us.</p>
<dt>2.</p>
<dd> The code </p>
<p>SPAGAIN;<br />
SP -= count;<br />
ax = (SP &#8211; PL_stack_base) + 1;</p>
<p> sets the stack up so that we can use the <tt>&quot;ST&quot;</tt> macro.</p>
<dt>3.</p>
<dd> Unlike the original coding of this example, the returned values are not accessed in reverse order. So <tt>ST(0)</tt> refers to the first value returned by the Perl subroutine and <tt>&quot;ST(count-1)&quot;</tt> refers to the last.</dl>
<h3>Creating and Calling an Anonymous Subroutine in C</h3>
<p> As we&#8217;ve already shown, <tt>&quot;call_sv&quot;</tt> can be used to invoke an anonymous subroutine. However, our example showed a Perl script invoking an <font SIZE="-1">XSUB</font> to perform this operation. Let&#8217;s see how it can be done inside our C code: </p>
<p> &#8230;<br />
 SV *cvrv<br />
    = eval_pv(&#8220;sub {<br />
                print &#8216;You will not find me cluttering any namespace!&#8217;<br />
 }<br />
 &#8220;, TRUE);<br />
     &#8230; call_sv(cvrv, G_VOID | G_NOARGS);</p>
<p> <tt>&quot;eval_pv&quot;</tt> is used to compile the anonymous subroutine, which will be the return value as well (read more about <tt>&quot;eval_pv&quot;</tt> in &#8220;eval_pv&#8221; in perlapi). Once this code reference is in hand, it can be mixed in with all the previous examples we&#8217;ve shown.</p>
<h2>LIGHTWEIGHT CALLBACKS</h2>
<p> Sometimes you need to invoke the same subroutine repeatedly. This usually happens with a function that acts on a list of values, such as Perl&#8217;s built-in <code>sort()</code>. You can pass a comparison function to <code>sort()</code>, which will then be invoked for every pair of values that needs to be compared. The <code>first()</code> and <code>reduce()</code> functions from List::Util follow a similar pattern. </p>
<p> In this case it is possible to speed up the routine (often quite substantially) by using the lightweight callback <font SIZE="-1">API.</font> The idea is that the calling context only needs to be created and destroyed once, and the sub can be called arbitrarily many times in between. </p>
<p> It is usual to pass parameters using global variables (typically <tt>$_</tt> for one parameter, or <tt>$a</tt> and <tt>$b</tt> for two parameters) rather than via <tt>@_</tt>. (It is possible to use the <tt>@_</tt> mechanism if you know what you&#8217;re doing, though there is as yet no supported <font SIZE="-1">API</font> for it. It&#8217;s also inherently slower.) </p>
<p> The pattern of macro calls is like this: </p>
<pre><code>
dMULTICALL;          /* Declare local variables */
U8 gimme = G_SCALAR; /* context of the call: G_SCALAR,
                      * G_ARRAY, or G_VOID */
PUSH_MULTICALL(cv);  /* Set up the context for calling cv,
                        and set local vars appropriately */
/* loop */ {
    /* set the value(s) af your parameter variables */
    MULTICALL; /* Make the actual call */
} /* end of loop */
POP_MULTICALL; /* Tear down the calling context */
</code></pre>
<p> For some concrete examples, see the implementation of the <code>first()</code> and <code>reduce()</code> functions of List::Util 1.18. There you will also find a header file that emulates the multicall <font SIZE="-1">API</font> on older versions of perl.</p>
<h2>SEE ALSO</h2>
<p> perlxs, perlguts, perlembed</p>
<h2>AUTHOR</h2>
<p> Paul Marquess </p>
<p> Special thanks to the following people who assisted in the creation of the document. </p>
<p> Jeff Okamoto, Tim Bunce, Nick Gianniotis, Steve Kelem, Gurusamy Sarathy and Larry Wall.</p>
<h2>DATE</h2>
<p> Last updated for perl 5.23.1. </p>
<h2>Index</h2>
<dt><a href="#lbBE">LIGHTWEIGHT CALLBACKS</a></p>
<dd>
<dt><a href="#lbBF">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBG">AUTHOR</a></p>
<dd>
<dt><a href="#lbBH">DATE</a></p>
<dd></dl>
