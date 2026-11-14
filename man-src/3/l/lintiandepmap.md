---
title: "lintiandepmap(3)"
name: "lintiandepmap"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiandepmap/"
description: "Lintian::DepMap – Dependencies map/tree creator"
---

<p>Lintian::DepMap &#8211; Dependencies map/tree creator </p>
<h2>Synopsis</h2>
<pre> use Lintian::DepMap;
 my $map = Lintian::DepMap-&gt;new;
 # know about A:
 $map-&gt;add('A');
 # B depends on A:
 $map-&gt;add('B', 'A');
 # prints 'A':
 print $map-&gt;selectable;
 # indicate we are working on 'A' (optional):
 $map-&gt;select('A');
 # do 'A' ... work work work
 # we are done with A:
 $map-&gt;satisfy('A');
 # prints 'B':
 print $map-&gt;selectable;</pre>
<h2>Description</h2>
<p>Lintian::DepMap is a simple dependencies map/tree creator and &#8220;resolver&#8221;. It works by creating a tree based on the indicated dependencies and destroying it to resolve it. </p>
<p> Note: in the below documentation a <tt>&quot;node&quot;</tt> means a node name; no internal reference is ever returned and therefore never accepted as a parameter.</p>
<dl COMPACT>
<dt><i>new()</i></p>
<dd>Creates a new Lintian::DepMap object and returns a reference to it.</p>
<dt><i>initialise()</i></p>
<dd>Ensure, by reconstructing if necessary, the map&#8217;s status is the initial. That is, partially or fully resolved maps can be restored to its original state by calling this method. </p>
<p> This can be useful when the same map will be used multiple times. </p>
<p> E.g. </p>
<pre> $map-&gt;add('A');
 $map-&gt;satisfy('A');
 # prints nothing
 print $map-&gt;selectable;
 $map-&gt;initialise;
 print $map-&gt;selectable;</pre>
<dt>add(node[, dependency[, dependency[, &#8230;]]])</p>
<dd>Adds the given <tt>&quot;node&quot;</tt> to the map marking any second or more parameter as its dependencies. E.g. </p>
<pre> # A has no dependency:
 $map-&gt;add('A');
 # B depends on A:
 $map-&gt;add('B', 'A');</pre>
<dt>addp(node[, prefix, dependency[, dependency[, &#8230;]]])</p>
<dd>Adds the given <tt>&quot;node&quot;</tt> to the map marking any third or more parameters, after prefixing them with <tt>&quot;prefix&quot;</tt>, as its dependencies. E.g. </p>
<pre> # pA and pB have no dependency:
 $map-&gt;add('pA');
 $map-&gt;add('pA');
 # C depends on pA and pB:
 $map-&gt;addp('C', 'p', 'A', 'B');</pre>
<dt>satisfy(node)</p>
<dd>Indicates that the given <tt>&quot;node&quot;</tt> has been satisfied/done. </p>
<p> The given <tt>&quot;node&quot;</tt> is no longer marked as being selected, if it was; all of its branches that have no other parent are now <i>selectable()</i> and all the references to <tt>&quot;node&quot;</tt> are deleted except the one from the <i>known()</i> list. </p>
<p> E.g. </p>
<pre> # A has no dependencies:
 $map-&gt;add('A');
 # B depends on A:
 $map-&gt;add('B', 'A');
 # we work on A, and we are done:
 $map-&gt;satisfy('A');
 # B is now available:
 $map-&gt;selectable('B');</pre>
<p><code>Note</code>: shall the requested node not exist this method <i>die()</i>s.</p>
<dt>done(node)</p>
<dd>Returns whether the given <tt>&quot;node&quot;</tt> has been satisfied/done. </p>
<p> E.g. </p>
<pre> # A has no dependencies:
 $map-&gt;add('A');
 # we work on A, and we are done:
 $map-&gt;satisfy('A');
 print &quot;A is done!&quot;
 if ($map-&gt;done('A'));</pre>
<dt>unlink(node)</p>
<dd>Removes all references to the given <tt>&quot;node&quot;</tt> except for the entry in the <i>known()</i> table. </p>
<p> <font SIZE="-1"><code>IMPORTANT</code></font>: since all references are deleted it is possible that a node that depended on <tt>&quot;node&quot;</tt> may become available even when it was not expected to. </p>
<p> <font SIZE="-1"><code>IMPORTANT</code></font>: this operation can <code>not</code> be reversed by the means of <i>initialise()</i>. </p>
<p> E.g. </p>
<pre> $map-&gt;add('A');
 # Prints A
 print $map-&gt;selectable;
 # we later notice we don't want A
 $map-&gt;unlink('A');
 # Prints nothing
 print $map-&gt;selectable;</pre>
<p><code>Note</code>: shall the requested node not exist this method <i>die()</i>s.</p>
<dt>select(node)</p>
<dd>Marks the given <tt>&quot;node&quot;</tt> as selected to indicate that whatever it represents is being worked on. Note: this operation is not atomic. </p>
<p> E.g. </p>
<pre> $map-&gt;add('A');
 $map-&gt;add('B', 'A');
 while($map-&gt;pending) {
 for my $node ($map-&gt;selectable) {
 $map-&gt;select($node);
 # work work work
 $map-&gt;satisfy($node);
 }
 }</pre>
<dt>selectable([node])</p>
<dd>If a <tt>&quot;node&quot;</tt> is specified returns <font SIZE="-1">TRUE</font> if it can be <i>select()</i>ed. </p>
<p> <code>Note</code>: already <i>select()</i>ed nodes cannot be re-selected, i.e. if the given <tt>&quot;node&quot;</tt> has already been selected this function will return <font SIZE="-1">FALSE</font>; or any selected item will be omitted from the returned array, in case no <tt>&quot;node&quot;</tt> is specified.</p>
<dt>selected([node])</p>
<dd>If a <tt>&quot;node&quot;</tt> is specified returns <font SIZE="-1">TRUE</font> if it is has been selected, <font SIZE="-1">FALSE</font> otherwise. </p>
<p> If no <tt>&quot;node&quot;</tt> is specified it returns an array with the name of all the nodes that have been <i>select()</i>ed but not yet satisfied. </p>
<p> E.g. </p>
<pre> # We are going to work on A
 $map-&gt;select('A');
 # Returns true
 $map-&gt;selected('A');
 # Prints A
 print $map-&gt;selected;</pre>
<dt><i>selectAll()</i></p>
<dd><i>select()</i>s all the <i>selectable()</i> nodes.</p>
<dt>parents(node)</p>
<dd>Return an array with the name of the parent nodes for the given <tt>&quot;node&quot;</tt>. </p>
<p> E.g. </p>
<pre> $map-&gt;add('A');
 $map-&gt;add('B', 'A');
 # Prints 'A'
 print $map-&gt;parents('B');</pre>
<p><code>Note</code>: shall the requested node not exist this method <i>die()</i>s.</p>
<dt><i>pending()</i></p>
<dd>Return the number of nodes that can or have already been selected. E.g. </p>
<pre> $map-&gt;add('B', 'A');
 # prints 1:
 print $map-&gt;pending;
 $map-&gt;select('A');
 # prints 1:
 print $map-&gt;pending;
 $map-&gt;satisfy('A');
 # prints 1 ('B' is now available):
 print $map-&gt;pending;</pre>
<dt><i>known()</i></p>
<dd>Return an array containing the names of nodes that were added. E.g. </p>
<pre> $map-&gt;add('B', 'A');
 # prints 'B':
 print $map-&gt;known;
 $map-&gt;add('A');
 # prints 'A' and 'B':
 print $map-&gt;known;</pre>
<dt>known(<font SIZE="-1">NODE</font>)</p>
<dd>Returns a truth value if <font SIZE="-1">NODE</font> is known or <tt>&quot;undef&quot;</tt> otherwise.</p>
<dt><i>missing()</i></p>
<dd>Return an array containing the names of nodes that were not added but that another node depended on it. E.g. </p>
<pre> $map-&gt;add('B', 'A');
 # prints 'A':
 print $map-&gt;missing;
 $map-&gt;add('A');
 # prints nothing:
 print $map-&gt;missing;
 # this also works; A depends on 'Z':
 $map-&gt;add('A', 'Z');
 # but now this prints 'Z':
 print $map-&gt;missing;</pre>
<dt>circular([&#8216;deep&#8217;])</p>
<dd>Returns an array of nodes that have a circular dependency. </p>
<p> E.g. </p>
<pre> $map-&gt;add('A', 'B');
 $map-&gt;add('B', 'A');
 # Prints A and B
 print $map-&gt;circular;</pre>
<p><code>Note</code>: since recursive/deep circular dependencies detection is a bit more resource expensive it is not the default. </p>
<pre> $map-&gt;add('A', 'B');
 $map-&gt;add('B', 'C');
 $map-&gt;add('C', 'A');
 # No deep/recursive scanning is performed, prints nothing
 print $map-&gt;circular;
 # deep scan, prints 'A, B, C'
 print $map-&gt;circular('deep');</pre>
</dl>
<h2>Author</h2>
<p>Originally written by Raphael Geissert &lt;atomo64 [at] gmail.com&gt; for Lintian.</p>
