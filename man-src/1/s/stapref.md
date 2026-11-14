---
title: "stapref(1)"
name: "stapref"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stapref/"
description: "stapref – systemtap language reference"
---

<h2>NAME</h2>
<p> stapref &#8211; systemtap language reference </p>
<h2>SYNOPSIS</h2>
<p> <code>stapref</code> </p>
<h2>DESCRIPTION</h2>
<p> The reference for the systemtap scripting language. </p>
<h2>LANGUAGE</h2>
<p> Keywords </p>
<dl>
<dt>
<dd>
<pre><code>
&amp;bull;
break
    &amp;bull;
continue
    &amp;bull;
delete &amp;bull;
else
    &amp;bull;
exit
    &amp;bull;
foreach
    &amp;bull; for
    &amp;bull;
function
    &amp;bull;
global
    &amp;bull;
private
&amp;bull;
if
    &amp;bull;
in
    &amp;bull;
next
    &amp;bull;
probe
    &amp;bull;
return &amp;bull;
try / catch
          &amp;bull;
while
</code></pre>
</dl>
<p> Data Types and Operators </p>
<dl>
<dt>
<dd>
Integers<br />
    &amp;bull;<br />
var1 = 5 &amp; bull;<br />
global var2 = 10 Strings &amp; bull;<br />
var1 = &#8220;string1&#8221; &amp; bull;<br />
global var2 = &#8220;string2&#8221; Associative Arrays &amp; bull;<br />
global array1[] &amp; bull;<br />
global array2[SIZE] &amp; bull;<br />
array[index] = 5 Context Variables &amp; bull;<br />
$var<br />
    &amp;bull;<br />
$var$(pretty printed string form)<br />
    Binary numeric operators<br />
        &amp;bull;<br />
* / % +- &lt;&lt; &gt;&gt; &amp;^ | &amp;&amp; ||<br />
    Binary string operators<br />
        &amp;bull;<br />
.(string concatenation)<br />
    Numeric assignment operators<br />
        &amp;bull;<br />
= += -= *= /= %= &gt;&gt;= &lt;&lt;= &amp;= ^= |=<br />
    String assignment operators &amp; bull;<br />
=.=<br />
    Unary numeric operators &amp; bull;<br />
+ &#8211; !~++&#8211;Numeric &amp; string comparison operators &amp; bull;<br />
&lt;&gt; &lt;= &gt;= == !=<br />
    Regular expression matching operators<br />
        &amp;bull;<br />
= ~!~Ternary operator&amp; bull;<br />
cond ? exp1 : exp2 Grouping operator&amp; bull;<br />
(expression)<br />
    Array operators<br />
        &amp;bull;<br />
array[index](array read / write) &amp; bull;<br />
[index] in array<br />
    Aggregation<br />
    operator&amp; bull;<br />
var &lt; &lt; &lt; value
</dl>
<p> Statements </p>
<dl>
<dt>
<dd>
Jump Statements<br />
    &amp;bull;<br />
continue<br />
    &amp;bull;<br />
break<br />
    &amp;bull;<br />
next<br />
    &amp;bull;<br />
return expression &amp; bull;<br />
try statement catch (message)
</dl>
<dl>
<dt>
<dd>
Selection Statements<br />
    &amp;bull;<br />
if (expression)<br />
    statement<br />
        &amp;bull;<br />
else<br />
    statement
</dl>
<dl>
<dt>
<dd>
Iteration Statements<br />
    &amp;bull;<br />
foreach (variable in array)<br />
    statement<br />
        &amp;bull;<br />
foreach ([ var1, var2, &#8230; ] in array)<br />
    statement<br />
        &amp;bull;<br />
for (expression; expression; expression)<br />
    statement<br />
        &amp;bull;<br />
while (expression)<br />
statement
</dl>
<dl>
<dt>
<dd>
Declaration Statements<br />
    &amp;bull;<br />
function name(variable<br />
              : type, &#8230;){statement} &amp;<br />
    bull;<br />
function name : type(variable<br />
                     : type, &#8230;){statement} &amp;<br />
                bull;<br />
function name : type(variable<br />
                     : type, &#8230;) %<br />
                {c_statement % } &amp;<br />
    bull;<br />
probe probepoint{statement} &amp; bull;<br />
probe label = probepoint<br />
{<br />
    statement<br />
}
</dl>
<p> Lexical Structure </p>
<dl>
<dt>
<dd>
<pre>
Comments
&bull; <code>#</code> ... comment
&bull; <code>//</code> ... comment
&bull; <code>/*</code> ... comment ... <code>*/</code>
</pre>
</dl>
<dl>
<dt>
<dd>
Preprocessor<br />
    &amp;bull;<br />
% (expression % ? true_tokens % : false_tokens %) &amp; bull;<br />
@define label(variable, &#8230;) %<br />
{<br />
    statement %<br />
}
</dl>
<p> Builtin Functions </p>
<dl>
<dt>
<dd>
Aggregation Builtin Functions<br />
    &amp;bull;<br />
@avg(variable) &amp; bull;<br />
@count(variable) &amp; bull;<br />
@hist_linear(variable, N, N, N) &amp; bull;<br />
@hist_log(variable) &amp; bull;<br />
@max(variable) &amp; bull;<br />
@min(variable) &amp; bull;<br />
@sum(variable)
</dl>
<dl>
<dt>
<dd>
Output Builtin Functions<br />
    &amp;bull;<br />
print(variable) &amp; bull;<br />
printf(format<br />
       : string, variable, &#8230;) &amp;<br />
    nbsp;<br />
where format is of the form : % [flags][width][.precision][length] specifier<br />
                                    &amp;bull;<br />
printd(delimiter<br />
       : string, variable, &#8230;) &amp;<br />
    bull;<br />
printdln(delimiter<br />
         : string, variable, &#8230;) &amp;<br />
    bull;<br />
println() &amp; bull;<br />
sprint : string(variable) &amp; bull;<br />
sprintf : string(format<br />
                 : string, variable, &#8230;)
</dl>
<dl>
<dt>
<dd>
Variable Access Builtin Functions<br />
    &amp;bull;<br />
@cast(variable, &#8220;type_name&#8221;[, &#8220;module&#8221;]) &amp; bull;<br />
@defined(variable)
</dl>
<p> Probepoints </p>
<dl>
<dt>
<dd>
Some of the more commonly used probepoints<br />
    &amp;bull;<br />
kernel.function(PATTERN) kernel.function(PATTERN).call<br />
    &amp;bull;<br />
kernel.function(PATTERN).return &amp;bull;<br />
kernel.FUNCTION(PATTERN).return.maxactive(VALUE) &amp; bull;<br />
kernel.FUNCTION(PATTERN).inline<br />
    &amp;bull;<br />
kernel.FUNCTION(PATTERN).label(LPATTERN) &amp; bull;<br />
module(MPATTERN).FUNCTION(PATTERN) &amp; bull;<br />
module(MPATTERN).FUNCTION(PATTERN).call<br />
    &amp;bull;<br />
module(MPATTERN).FUNCTION(PATTERN).return.maxactive(VALUE) &amp; bull;<br />
module(MPATTERN).FUNCTION(PATTERN).inline<br />
    &amp;bull;<br />
kernel.statement(PATTERN) &amp; bull;<br />
kernel.statement(ADDRESS).absolute<br />
    &amp;bull;<br />
module(MPATTERN).statement(PATTERN) &amp; bull;<br />
kprobe.FUNCTION(FUNCTION) &amp; bull;<br />
kprobe.FUNCTION(FUNCTION).return &amp;bull;<br />
kprobe.module(NAME).FUNCTION(FUNCTION) &amp; bull;<br />
kprobe.module(NAME).FUNCTION(FUNCTION).return &amp;bull;<br />
kprobe.statement(ADDRESS).absolute<br />
    &amp;bull;<br />
process.begin process(&#8220;PATH&#8221;).begin<br />
    &amp;bull;<br />
process(PID).begin process.thread.begin<br />
    &amp;bull;<br />
process(&#8220;PATH&#8221;).thread.begin<br />
    &amp;bull;<br />
process(PID).thread.begin<br />
    &amp;bull;<br />
process.end<br />
    &amp;bull;<br />
process(&#8220;PATH&#8221;).end<br />
    &amp;bull;<br />
process(PID).end<br />
    &amp;bull;<br />
process.thread.end<br />
    &amp;bull;<br />
process(&#8220;PATH&#8221;).thread.end<br />
    &amp;bull;<br />
process(PID).thread.end<br />
    &amp;bull;<br />
process(&#8220;PATH&#8221;).syscall<br />
    &amp;bull;<br />
process(PID).syscall<br />
    &amp;bull;<br />
process.syscall.return &amp;bull;<br />
process(&#8220;PATH&#8221;).syscall.return &amp;bull;<br />
process(PID).syscall.return &amp;bull;<br />
process(&#8220;PATH&#8221;).FUNCTION(&#8220;NAME&#8221;) &amp; bull;<br />
process(&#8220;PATH&#8221;).statement(&#8220;*@FILE.c:123&#8221;) &amp; bull;<br />
process(&#8220;PATH&#8221;).FUNCTION(&#8220;*&#8221;).return &amp;bull;<br />
process(&#8220;PATH&#8221;).FUNCTION(&#8220;myfun&#8221;).label(&#8220;foo&#8221;) &amp; bull;<br />
process(&#8220;PATH&#8221;).mark(&#8220;LABEL&#8221;) &amp; bull;<br />
java(&#8220;PNAME&#8221;).class(&#8220;CLASSNAME&#8221;).method(&#8220;PATTERN&#8221;) &amp; bull;<br />
java(&#8220;PNAME&#8221;).class(&#8220;CLASSNAME&#8221;).method(&#8220;PATTERN&#8221;).return &amp;bull;<br />
java(PID).class(&#8220;CLASSNAME&#8221;).method(&#8220;PATTERN&#8221;) &amp; bull;<br />
java(PID).class(&#8220;CLASSNAME&#8221;).method(&#8220;PATTERN&#8221;).return &amp;bull;<br />
python2.module(&#8220;MODULENAME&#8221;).function(&#8220;PATTERN&#8221;) &amp; bull;<br />
python2.module(&#8220;MODULENAME&#8221;).function(&#8220;PATTERN&#8221;).return &amp;bull;<br />
python3.module(&#8220;MODULENAME&#8221;).function(&#8220;PATTERN&#8221;) &amp; bull;<br />
python3.module(&#8220;MODULENAME&#8221;).function(&#8220;PATTERN&#8221;).return
</dl>
<p> Tapset Functions </p>
<dl>
<dt>
<dd>
<pre><code>
Some of the more commonly used tapset functions
    &amp;bull;
addr : long() &amp; bull;
backtrace : string() &amp; bull;
caller : string() &amp; bull;
caller_addr : long() &amp; bull;
cmdline_arg : string(N
                     : long) &amp;
              bull;
cmdline_args : string(N
                      : long, m
                      : long, delim
                      : string) &amp;
               bull;
cmdline_str : string() &amp; bull;
env_var : string(name
                 : string) &amp;
          bull;
execname : string() &amp; bull;
int_arg : long(N
               : long) &amp;
          bull;
isinstr : long(s1
               : string, s2
               : string) &amp;
          bull;
long_arg : long(N
                : long) &amp;
           bull;
modname : string() &amp; bull;
module_name : string() &amp; bull;
pid : long() &amp; bull;
pn : string() &amp; bull;
pointer_arg : string(N
                     : long) &amp;
              bull;
pp : string() &amp; bull;
print_backtrace() &amp; bull;
probefunc : string() &amp; bull;
register : long(name
                : string) &amp;
           bull;
str_replace : string(prnt_str
                     : string, srch_str
                     : string, rplc_str
                     : string) &amp;
              bull;
stringat : long(str
                : string, pos
                : long) &amp;
           bull;
strlen : long(str
              : string) &amp;
         bull;
strtol : long(str
              : string, base
              : long) &amp;
         bull;
substr : string(str
                : string, start
                : long, length
                : long) &amp;
         bull;
user_long : long(addr
                 : long) &amp;
            bull;
user_string : string(addr
                     : long)
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i><a href="//www.systutorials.com/docs/linux/man/1-stap/">stap</a></i>(1)
</pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>,<code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<h2>Index</h2>
