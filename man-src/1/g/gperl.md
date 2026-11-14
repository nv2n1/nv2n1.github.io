---
title: "gperl(1)"
name: "gperl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gperl/"
description: "gperl – groff preprocessor for Perl parts in roff files"
---

<h2 class="name">NAME</h2>
<p> gperl &#8211; groff preprocessor for Perl parts in roff files </p>
<h2>SYNOPSIS</h2>
<p> [<i>filespec</i> &#8230; ] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> This is a preprocessor for <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). It allows the use of <code><a href="/docs/linux/man/7-perl/">perl</a></code>(7) code in <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) files. The result of a <i>Perl part</i> can be stored in groff <i>strings</i> or <i>numerical registers</i> based on the arguments at a final line of a <i>Perl part</i>.</p>
<h2>OPTIONS</h2>
<p> So far, there are only <i>filespec</i> or <i>breaking</i> options. </p>
<p> <i>filespec</i> are file names or the minus character <code>&#8211;</code> character for standard input. As usual, the argument <code>&#8212;</code> can be used in order to let all following arguments mean file names, even if the names begin with a minus character <code>&#8211;</code>. </p>
<p> An option is <i>breaking</i>, when the program just writes the information that was asked for and then stops. All other arguments will be ignored by that. These <i>breaking</i> options are here</p>
<dl>
<dt><code>-h~</code>|<code>~&#8211;help</code></p>
<dd> Print help information with a short explanation of options to standard output.</p>
<dt><code>-v~</code>|<code>~&#8211;version</code></p>
<dd> Print version information to standard output.</dl>
<h2>PERL PARTS</h2>
<p> <i>Perl</i> parts in <i>groff files</i> are enclosed by two <code>.Perl</code> requests with different arguments, a <i>starting</i> and an <i>ending</i> command.</p>
<h3>Starting Perl Mode</h3>
<p> The starting <i>Perl request</i> can either be without arguments, or by a request that has the term <code>start</code> as its only argument.</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code>.Perl</code></p>
<dt>*</p>
<dd> <code>.Perl start</code></dl>
</dl>
<h3>Ending Perl Mode without Storage</h3>
<p> A <code>.Perl</code> command line with an argument different from <code>start</code> finishes a running <i>Perl part</i>. Of course, it would be reasonable to add the argument <code>stop</code>; that&#8217;s possible, but not necessary.</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code>.Perl stop</code></p>
<dt>*</p>
<dd> <code>.Perl</code><i> other_than_start</i></dl>
</dl>
<p> The argument <i>other_than_start</i> can additionally be used as a <i>groff</i> string variable name for storage &#8212; see next section.</p>
<h3>Ending Perl Mode with Storage</h3>
<p> A useful feature of <code>gperl</code> is to store one or more results from the <i>Perl mode</i>. </p>
<p> The output of a <i>Perl part</i> can be got with backticks <code>`&#8230;`</code>. </p>
<p> This program collects all printing to STDOUT (normal standard output) by the Perl <code>print</code> program. This pseudo-printing output can have several lines, due to printed line breaks with <code>
</code>. By that, the output of a Perl run should be stored into a Perl array, with a single line for each array member. </p>
<p> This Perl array output can be stored by <code>gperl</code> in either</p>
<dl>
<dt><i>groff strings</i></p>
<dd> by creating a groff command <code>.ds</code></p>
<dt><i>groff number register</i></p>
<dd> by creating a groff command <code>.rn</code></dl>
<p> The storage modes can be determined by arguments of a final stopping <code>.Perl</code> command. Each argument <code>.ds</code> changes the mode into <i>groff string</i> and <code>.nr</code> changes the mode into <i>groff number register</i> for all following output parts. </p>
<p> By default, all output is saved as strings, so <code>.ds</code> is not really needed before the first <code>.nr</code> command. That suits to <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7), because every output can be saved as <i>groff</i> string, but the number registers can be very restrictive. </p>
<p> In <i>string mode</i>, <code>gperl</code> generates a <i>groff string</i> storage line</p>
<dl>
<dt>
<dd> <code>.ds</code><i> var_name content</i></dl>
<p> In <i>number register mode</i> the following groff command is generated</p>
<dl>
<dt>
<dd> <code>.nr</code><i> var_name content</i></dl>
<p> We present argument collections in the following. You can add as first argument for all <code>stop</code>. We omit this additional element. </p>
<dl>
<dt><code>.Perl .ds </code><i>var_name</i></p>
<dd> This will store 1 output line into the groff string named <i>var_name</i> by the automatically created command</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>.ds</code><i> var_name output</i></dl>
</dl>
<dt><code>.Perl</code><i> var_name</i></p>
<dd> If <i>var_name</i> is different from <code>start</code> this is equivalent to the former command, because the string mode is string with <code>.ds</code> command. default.</p>
<dt><code>.Perl</code><i> var_name1 var_name2</i></p>
<dd> This will store 2 output lines into groff string names <i>var_name1</i> and <i>var_name2</i>, because the default mode <code>.ds</code> is active, such that no <code>.ds</code> argument is needed. Of course, this is equivalent to</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>.Perl .ds </code><i>var_name1 var_name2</i></dl>
<p> and</p>
<dl>
<dt>
<dd> <code>.Perl .ds </code><i>var_name1 </i><code>.ds</code><i> var_name2</i></dl>
</dl>
<dt><code>.Perl .nr</code><i> var_name1 varname2</i></p>
<dd> stores both variables as number register variables. <code>gperl</code> generates</p>
<dl>
<dt>
<dd> <code>.nr</code><i> var_name1 output_line1</i> <code>.nr</code><i> var_name2 output_line2</i></dl>
<dt><code>.Perl .nr </code><i>var_name1</i><code> .ds </code><i>var_name2</i></p>
<dd> stores the 1st argument as <i>number register</i> and the second as <i>string</i> by</p>
<dl>
<dt>
<dd> <code>.nr</code><i> var_name1 output_line1</i> <code>.ds</code><i> var_name2 output_line2</i></dl>
</dl>
<h3>Printing towards STDERR is without Storage</h3>
<p> The printing towards <i>STDERR</i>, (standard error) works as usual. All error information goes to the real normal <i>standard error</i>, without other automatic storage.</p>
<h2>EXAMPLES</h2>
<p> A possible <i>Perl part</i> in a <i>roff file</i> could look like that:</p>
<dl>
<dt>
<dd> before .Perl start my $result = &#8216;some data&#8217;; print $result; .Perl stop .ds string_var after</dl>
<p> This stores the result <code>&#8220;some data&#8221;</code> into the <i>roff string</i> called <code>string_var</code>, such that the following line is printed:</p>
<dl>
<dt>
<dd> .ds string_var some data</dl>
<p> by <code>gperl</code> as food for the coming <code>groff</code> run. </p>
<p> A <i>Perl part</i> with several outputs is:</p>
<dl>
<dt>
<dd> .Perl start print &#8220;first
&#8221;; print &#8220;second line
&#8221;; print &#8220;3
&#8221;; .Perl var1 var2 .nr var3</dl>
<p> This stores 3 printed lines into 3 <i>groff</i> strings. <code>var1</code>,<code>var2</code>,<code>var3</code>. So the following <i>groff</i> command lines are created:</p>
<dl>
<dt>
<dd> .ds var1 first .ds var2 second line .nr var3 3</dl>
<h2>AUTHORS</h2>
<p> <code>gperl</code> was written by Bernd Warken</p>
<h2>SEE ALSO</h2>
<p> Man pages related to <i>groff</i> are <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7), <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1), and <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1). </p>
<p> Documents related to <i>Perl</i> are <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/7-perl/">perl</a></code>(7). </p>
<h2>Index</h2>
