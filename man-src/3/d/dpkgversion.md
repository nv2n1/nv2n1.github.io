---
title: "dpkgversion(3)"
name: "dpkgversion"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgversion/"
---

Dpkg::Version - handling and comparing dpkg-style version numbers 

<h2>Description</h2>The Dpkg::Version module provides pure-Perl routines to compare dpkg-style version numbers (as used in Debian packages) and also an object oriented interface overriding perl operators to do the right thing when you compare Dpkg::Version object between them.
<h2>Object Interface</h2><dl COMPACT><dt>my $v = Dpkg::Version-&gt;new($version, %opts)
<dd>Create a new Dpkg::Version object corresponding to the version indicated in the string (scalar) <tt>$version</tt>. By default it will accepts any string and consider it as a valid version. If you pass the option ``check =&gt; 1'', it will return undef if the version is invalid (see version_check for details). 

 You can always call <tt>$v</tt>-&gt;<i>is_valid()</i> later on to verify that the version is valid.
<dt>boolean evaluation
<dd>When the Dpkg::Version object is used in a boolean evaluation (for example in ``if ($v)'' or ``$v || 'default''') it returns its string representation if the version stored is valid ($v-&gt;<i>is_valid()</i>) and undef otherwise.
<dt>$v-&gt;<i>is_valid()</i>
<dd>Returns true if the version is valid, false otherwise.
<dt>$v-&gt;<i>epoch()</i>, $v-&gt;<i>version()</i>, $v-&gt;<i>revision()</i>
<dd>Returns the corresponding part of the full version string.
<dt>$v-&gt;<i>is_native()</i>
<dd>Returns true if the version is native, false if it has a revision.
<dt>$v1 &lt;=&gt; $v2, $v1 &lt; $v2, $v1 &lt;= $v2, $v1 &gt; $v2, $v1 &gt;= $v2
<dd>Numerical comparison of various versions numbers. One of the two operands needs to be a Dpkg::Version, the other one can be anything provided that its string representation is a version number.
<dt>&quot;$v&quot;, $v-&gt;<i>as_string()</i>, $v-&gt;as_string(%options)
<dd>Accepts an optional option hash reference, affecting the string conversion. 

 Options:
<dl COMPACT><dd><dl COMPACT><dt>omit_epoch (defaults to 0)
<dd>Omit the epoch, if present, in the output string.
<dt>omit_revision (defaults to 0)
<dd>Omit the revision, if present, in the output string.</dl></dl><dl COMPACT><dd>Returns the string representation of the version number.</dl></dl><h2>Functions</h2>All the functions are exported by default.
<dl COMPACT><dt>version_compare($a, $b)
<dd>Returns -1 if <tt>$a</tt> is earlier than <tt>$b</tt>, 0 if they are equal and 1 if <tt>$a</tt> is later than <tt>$b</tt>. 

 If <tt>$a</tt> or <tt>$b</tt> are not valid version numbers, it dies with an error.
<dt>version_compare_relation($a, $rel, $b)
<dd>Returns the result (0 or 1) of the given comparison operation. This function is implemented on top of <i>version_compare()</i>. 

 Allowed values for <tt>$rel</tt> are the exported constants <font SIZE="-1">REL_GT, REL_GE, REL_EQ, REL_LE, REL_LT.</font> Use <i>version_normalize_relation()</i> if you have an input string containing the operator.
<dt>my $rel = version_normalize_relation($rel_string)
<dd>Returns the normalized constant of the relation <tt>$rel</tt> (a value among <font SIZE="-1">REL_GT, REL_GE, REL_EQ, REL_LE</font> and <font SIZE="-1">REL_LT</font>). Supported relations names in input are: ``gt'', ``ge'', ``eq'', ``le'', ``lt'', ``&gt;&gt;'', ``&gt;='', ``='', ``&lt;='', ``&lt;&lt;''. ``&gt;'' and ``&lt;'' are also supported but should not be used as they are obsolete aliases of ``&gt;='' and ``&lt;=''.
<dt>version_compare_string($a, $b)
<dd>String comparison function used for comparing non-numerical parts of version numbers. Returns -1 if <tt>$a</tt> is earlier than <tt>$b</tt>, 0 if they are equal and 1 if <tt>$a</tt> is later than <tt>$b</tt>. 

 The ``~'' character always sort lower than anything else. Digits sort lower than non-digits. Among remaining characters alphabetic characters (A-Za-z) sort lower than the other ones. Within each range, the <font SIZE="-1">ASCII</font> decimal value of the character is used to sort between characters.
<dt>version_compare_part($a, $b)
<dd>Compare two corresponding sub-parts of a version number (either upstream version or debian revision). 

 Each parameter is split by <i>version_split_digits()</i> and resulting items are compared together. As soon as a difference happens, it returns -1 if <tt>$a</tt> is earlier than <tt>$b</tt>, 0 if they are equal and 1 if <tt>$a</tt> is later than <tt>$b</tt>.
<dt>my @items = version_split_digits($version)
<dd>Splits a string in items that are each entirely composed either of digits or of non-digits. For instance for ``1.024~beta1+svn234'' it would return (``1'', ``.'', ``024'', ``~beta'', ``1'', ``+svn'', ``234'').
<dt>my ($ok, $msg) = version_check($version)
<dd><dt>my $ok = version_check($version)
<dd>Checks the validity of <tt>$version</tt> as a version number. Returns 1 in <tt>$ok</tt> if the version is valid, 0 otherwise. In the latter case, <tt>$msg</tt> contains a description of the problem with the <tt>$version</tt> scalar.</dl><h2>Changes</h2><h3>Version 1.01</h3>New argument: Accept an options argument in <tt>$v</tt>-&gt;<i>as_string()</i>. 

 New method: <tt>$v</tt>-&gt;<i>is_native()</i>.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Don Armstrong &lt;don [at] donarmstrong.com&gt;, Colin Watson &lt;cjwatson [at] debian.org&gt; and Raphaël Hertzog &lt;hertzog [at] debian.org&gt;, based on the implementation in <i>dpkg/lib/version.c</i> by Ian Jackson and others.
