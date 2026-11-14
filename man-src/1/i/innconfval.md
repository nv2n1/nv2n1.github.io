---
title: "innconfval(1)"
name: "innconfval"
section: "1"
letter: "i"
url: "/docs/linux/man/1-innconfval/"
description: "innconfval – Get configuration parameters from inn.conf"
---

<h2 class="name">NAME</h2>
<p> innconfval &#8211; Get configuration parameters from inn.conf </p>
<h2>SYNOPSIS</h2>
<p> <code>innconfval</code> [<code>-pstv</code>] [<code>-i</code> <i>file</i>] [<i>parameter</i> &#8230;] </p>
<p> <code>innconfval</code> <code>-C</code> [<code>-i</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>innconfval</code> normally prints the values of the parameters specified on the command line. By default, it just prints the parameter values, but if <code>-p</code>, <code>-s</code>, or <code>-t</code> are given, it instead prints the parameter and value in the form of a variable assignment in Perl, Bourne shell, or Tcl respectively. If no parameters are specifically requested, <code>innconfval</code> prints out all parameter values (this isn&#8217;t particularly useful unless one of <code>-p</code>, <code>-s</code>, or <code>-t</code> were specified). </p>
<p> All parameters are taken from <i>inn.conf</i> except for <i>version</i>, which is always the version string of <font SIZE="-1">INN</font>. </p>
<p> If given the <code>-C</code> option, <code>innconfval</code> instead checks <i>inn.conf</i>, reporting any problems found to standard error. <code>innconfval</code> will exit with status 0 if no problems are found and with status 1 otherwise.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Check <i>inn.conf</i> rather than printing out the values of parameters.</p>
<dt><code>-i</code> <i>file</i></p>
<dd> Use <i>file</i> as the source configuration file rather than <i>inn.conf</i>. <i>file</i> must be a valid <i>inn.conf</i> file and will be parsed the same as <i>inn.conf</i> would be.</p>
<dt><code>-p</code></p>
<dd> Print out parameters as Perl assignment statements. The variable name will be the same as the <i>inn.conf</i> parameter, and string values will be enclosed in single quotes with appropriate escaping. Boolean values will be mapped to the strings <tt>&quot;true&quot;</tt> or <tt>&quot;false&quot;</tt>. List values will be mapped to an array of strings. <font SIZE="-1">NULL</font> values are printed out with the <tt>&quot;undef&quot;</tt> value. </p>
<p> Here is an example: </p>
<pre><code>
$enableoverview = 'true';
@extraoverviewadvertised = ('Newsgroups', 'Injection-Info');
@extraoverviewhidden = undef;
$organization = 'Let\'s try nasty "quotes"';
$maxforks = 10;
</code></pre>
<p> If <code>innconfval</code> is called via the Perl <tt>&quot;INN::Config&quot;</tt> module, all these variables are properly exported.</p>
<dt><code>-s</code></p>
<dd> Print out parameters as Bourne shell assignment statements. The variable name will be the <i>inn.conf</i> parameter name in all capitals, and all variables will be exported, if not <font SIZE="-1">NULL</font>. String values will be enclosed in single quotes with appropriate escaping, and boolean values will be mapped to <tt>&quot;true&quot;</tt> or <tt>&quot;false&quot;</tt>. List values will be mapped to a space-separated string representing an array of strings (as Bourne shell does not recognize arrays, contrary to several other shells, an array cannot be returned for interoperability reasons). </p>
<p> Here is an example: </p>
<pre><code>
ENABLEOVERVIEW = true;
export ENABLEOVERVIEW;
EXTRAOVERVIEWADVERTISED = '"Newsgroups" "Injection-Info"';
export EXTRAOVERVIEWADVERTISED;
ORGANIZATION = 'Let'\''s try nasty "quotes"'; export ORGANIZATION; MAXFORKS = 10;
export MAXFORKS;
</code></pre>
<dt><code>-t</code></p>
<dd> Print out parameters as Tcl assignment statements. The variable name will be the same as the <i>inn.conf</i> parameter name but with <tt>&quot;inn_&quot;</tt> prepended, and string variables will be escaped appropriately. Boolean values will be mapped to the strings <tt>&quot;true&quot;</tt> or <tt>&quot;false&quot;</tt>. List values will be mapped to an array of strings. <font SIZE="-1">NULL</font> values are not printed out. </p>
<p> Here is an example: </p>
<pre>
    set inn_enableoverview &quot;true&quot;
    set inn_extraoverviewadvertised { &quot;Newsgroups&quot; &quot;Injection-Info&quot; }
    set inn_organization &quot;Let's try nasty \&quot;quotes\&quot;&quot;
    set inn_maxforks 10
</pre>
<dt><code>-v</code></p>
<dd> Print <font SIZE="-1">INN</font>&#8216;s version. This is equivalent to <tt>&quot;innconfval version&quot;</tt>.</dl>
<h2>HISTORY</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> innconfval.pod 9311 2011-08-06 20:18:42Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="//www.systutorials.com/docs/linux/man/3pm-INN::Config/">INN::Config</a></i>(3pm). </p>
<h2>Index</h2>
