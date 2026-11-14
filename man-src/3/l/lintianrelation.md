---
title: "lintianrelation(3)"
name: "lintianrelation"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianrelation/"
description: "Lintian::Relation – Lintian operations on dependencies and relationships"
---

<p>Lintian::Relation &#8211; Lintian operations on dependencies and relationships </p>
<h2>Synopsis</h2>
<pre> my $depends = Lintian::Relation-&gt;new('foo | bar, baz');
 print &quot;yes
&quot; if $depends-&gt;implies('baz');
 print &quot;no
&quot; if $depends-&gt;implies('foo');</pre>
<h2>Description</h2>
<p>This module provides functions for parsing and evaluating package relationship fields such as Depends and Recommends for binary packages and Build-Depends for source packages. It parses a relationship into an internal format and can then answer questions such as &#8220;does this dependency require that a given package be installed&#8221; or &#8220;is this relationship a superset of another relationship.&#8221; </p>
<p> A dependency line is viewed as a predicate formula. The comma separator means &#8220;and&#8221;, and the alternatives separator means &#8220;or&#8221;. A bare package name is the predicate &#8220;a package of this name is available&#8221;. A package name with a version clause is the predicate &#8220;a package of this name that satisfies this version clause is available.&#8221; Architecture restrictions, as specified in Policy for build dependencies, are supported and also checked in the implication logic unless the <code>new_noarch()</code> constructor is used. With that constructor, architecture restrictions are ignored.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new(<font SIZE="-1">RELATION</font>)</p>
<dd>Creates a new Lintian::Relation object corresponding to the parsed relationship <font SIZE="-1">RELATION.</font> This object can then be used to ask questions about that relationship. <font SIZE="-1">RELATION</font> may be <tt>&quot;undef&quot;</tt> or the empty string, in which case the returned Lintian::Relation object is empty (always satisfied).</p>
<dt>parse_element</p>
<dd>
<dt>new_norestriction(<font SIZE="-1">RELATION</font>)</p>
<dd>Creates a new Lintian::Relation object corresponding to the parsed relationship <font SIZE="-1">RELATION,</font> ignoring architecture restrictions and restriction lists. This should be used in cases where we only care if a dependency is present in some cases and we don&#8217;t want to require that the architectures match (such as when checking for proper build dependencies, since if there are architecture constraints the maintainer is doing something beyond Lintian&#8217;s ability to analyze) or that the restrictions list match (Lintian can&#8217;t handle dependency implications with build profiles yet). <font SIZE="-1">RELATION</font> may be <tt>&quot;undef&quot;</tt> or the empty string, in which case the returned Lintian::Relation object is empty (always satisfied).</p>
<dt>new_noarch(<font SIZE="-1">RELATION</font>)</p>
<dd>An alias for new_norestriction.</p>
<dt>and(<font SIZE="-1">RELATION, &#8230;</font>)</p>
<dd>Creates a new Lintian::Relation object produced by <font SIZE="-1">AND</font>&#8216;ing all the relations together. Semantically it is the similar to: </p>
<pre> Lintian::Relation-&gt;new (join (', ', @relations))</pre>
<p>Except it can avoid some overhead and it works if some of the elements are Lintian::Relation objects already.</dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt><code>duplicates()</code></p>
<dd>Returns a list of duplicated elements within the relation object. Each element of the returned list will be a reference to an anonymous array holding a set of relations considered duplicates of each other. Two relations are considered duplicates if one implies the other, meaning that if one relationship is satisfied, the other is necessarily satisfied. This relationship does not have to be commutative: the opposite implication may not hold.</p>
<dt><code>restriction_less()</code></p>
<dd>Returns a restriction-less variant of this relation (or this relation object if it has no restrictions).</p>
<dt>implies(<font SIZE="-1">RELATION</font>)</p>
<dd>Returns true if the relationship implies <font SIZE="-1">RELATION,</font> meaning that if the Lintian::Relation object is satisfied, <font SIZE="-1">RELATION</font> will always be satisfied. <font SIZE="-1">RELATION</font> may be either a string or another Lintian::Relation object. </p>
<p> By default, architecture restrictions are honored in <font SIZE="-1">RELATION</font> if it is a string. If architecture restrictions should be ignored in <font SIZE="-1">RELATION,</font> create a Lintian::Relation object with <code>new_noarch()</code> and pass that in as <font SIZE="-1">RELATION</font> instead of the string.</p>
<dt>implies_element</p>
<dd>
<dt>implies_array</p>
<dd>
<dt>implies_inverse(<font SIZE="-1">RELATION</font>)</p>
<dd>Returns true if the relationship implies that <font SIZE="-1">RELATION</font> is certainly false, meaning that if the Lintian::Relation object is satisfied, <font SIZE="-1">RELATION</font> cannot be satisfied. <font SIZE="-1">RELATION</font> may be either a string or another Lintian::Relation object. </p>
<p> As with <code>implies()</code>, by default, architecture restrictions are honored in <font SIZE="-1">RELATION</font> if it is a string. If architecture restrictions should be ignored in <font SIZE="-1">RELATION,</font> create a Lintian::Relation object with <code>new_noarch()</code> and pass that in as <font SIZE="-1">RELATION</font> instead of the string.</p>
<dt>implies_element_inverse</p>
<dd>
<dt>implies_array_inverse</p>
<dd>
<dt><code>unparse()</code></p>
<dd>Returns the textual form of a relationship. This converts the internal form back into the textual representation and returns that, not the original argument, so the spacing is standardized. Returns undef on internal failures (such as an object in an unexpected format).</p>
<dt>matches (REGEX[, <font SIZE="-1">WHAT</font>])</p>
<dd>Check if one of the predicates in this relation matches <font SIZE="-1">REGEX.</font> <font SIZE="-1">WHAT</font> determines what is tested against <font SIZE="-1">REGEX</font> and if not given, defaults to <font SIZE="-1">VISIT_PRED_NAME.</font> </p>
<p> This method will return a truth value if <font SIZE="-1">REGEX</font> matches at least one predicate or clause (as defined by the <font SIZE="-1">WHAT</font> parameter &#8211; see below). </p>
<p> <font SIZE="-1">NOTE:</font> Often &#8220;implies&#8221; (or &#8220;implies_inverse&#8221;) is a better choice than this method. This method should generally only be used when checking for a &#8220;pattern&#8221; package (e.g. phpapi-[\d\w+]+). </p>
<p> <font SIZE="-1">WHAT</font> can be one of:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">VISIT_PRED_NAME</font></p>
<dd>Match <font SIZE="-1">REGEX</font> against the package name in each predicate (i.e. version and architecture constrains are ignored). Each predicate is tested in isolation. As an example: </p>
<pre> my $rel = Lintian::Relation-&gt;new ('somepkg | pkg-0 (&gt;= 1)');
 # Will match (version is ignored)
 $rel-&gt;matches (qr/^pkg-\d$/, VISIT_PRED_NAME);</pre>
<dt><font SIZE="-1">VISIT_PRED_FULL</font></p>
<dd>Match <font SIZE="-1">REGEX</font> against the full (normalized) predicate (i.e. including version and architecture). Each predicate is tested in isolation. As an example: </p>
<pre> my $vrel = Lintian::Relation-&gt;new ('somepkg | pkg-0 (&gt;= 1)');
 my $uvrel = Lintian::Relation-&gt;new ('somepkg | pkg-0');
 # Will NOT match (does not match with version)
 $vrel-&gt;matches (qr/^pkg-\d$/, VISIT_PRED_FULL);
 # Will match (this relation does not have a version)
 $uvrel-&gt;matches (qr/^pkg-\d$/, VISIT_PRED_FULL);
 # Will match (but only because there is a version)
 $vrel-&gt;matches (qr/^pkg-\d \(.*\)$/, VISIT_PRED_FULL);
 # Will NOT match (there is no version in the relation)
 $uvrel-&gt;matches (qr/^pkg-\d \(.*\)$/, VISIT_PRED_FULL);</pre>
<dt><font SIZE="-1">VISIT_OR_CLAUSE_FULL</font></p>
<dd>Match <font SIZE="-1">REGEX</font> against the full (normalized) <font SIZE="-1">OR</font> clause. Each predicate will have both version and architecture constrains present. As an example: </p>
<pre> my $vpred = Lintian::Relation-&gt;new ('pkg-0 (&gt;= 1)');
 my $orrel = Lintian::Relation-&gt;new ('somepkg | pkg-0 (&gt;= 1)');
 my $rorrel = Lintian::Relation-&gt;new ('pkg-0 (&gt;= 1) | somepkg');
 # Will match
 $vrel-&gt;matches (qr/^pkg-\d(?: \([^\)]\))?$/, VISIT_OR_CLAUSE_FULL);
 # These Will NOT match (does not match the &quot;|&quot; and the &quot;somepkg&quot; part)
 $orrel-&gt;matches (qr/^pkg-\d(?: \([^\)]\))?$/, VISIT_OR_CLAUSE_FULL);
 $rorrel-&gt;matches (qr/^pkg-\d(?: \([^\)]\))?$/, VISIT_OR_CLAUSE_FULL);</pre>
</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>visit (CODE[, <font SIZE="-1">FLAGS</font>])</p>
<dd>Visit clauses or predicates of this relation. Each clause or predicate is passed to <font SIZE="-1">CODE</font> as first argument and will be available as <tt>$_</tt>. </p>
<p> The optional bitmask parameter, <font SIZE="-1">FLAGS,</font> can be used to control what is visited and such. If <font SIZE="-1">FLAGS</font> is not given, it defaults to <font SIZE="-1">VISIT_PRED_NAME.</font> The possible values of <font SIZE="-1">FLAGS</font> are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">VISIT_PRED_NAME</font></p>
<dd>The package name in each predicate is visited, but the version and architecture part(s) are left out (if any).</p>
<dt><font SIZE="-1">VISIT_PRED_FULL</font></p>
<dd>The full predicates are visited in turn. The predicate will be normalized (by &#8220;unparse&#8221;).</p>
<dt><font SIZE="-1">VISIT_OR_CLAUSE_FULL</font></p>
<dd><font SIZE="-1">CODE</font> will be passed the full <font SIZE="-1">OR</font> clauses of this relation. The clauses will be normalized (by &#8220;unparse&#8221;) </p>
<p> Note: It will not visit the underlying predicates in the clause.</p>
<dt><font SIZE="-1">VISIT_STOP_FIRST_MATCH</font></p>
<dd>Stop the visits the first time <font SIZE="-1">CODE</font> returns a truth value. This is similar to first, except visit will return the value returned by <font SIZE="-1">CODE.</font></dl>
</dl>
<dl COMPACT>
<dd>Except where a given flag specifies otherwise, the return value of visit is last value returned by <font SIZE="-1">CODE</font> (or <tt>&quot;undef&quot;</tt> for the empty relation).</dl>
<dt>empty</p>
<dd>Returns a truth value if this relation is empty (i.e. it contains no predicates).</p>
<dt>unparsable_predicates</p>
<dd>Returns a list of predicates that were unparsable. </p>
<p> They are returned in the original textual representation and are also sorted by said representation.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
