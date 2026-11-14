---
title: "lintiandepmapproperties(3)"
name: "lintiandepmapproperties"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiandepmapproperties/"
---

Lintian::DepMap::Properties - Dependencies with properties map/tree creator 

<h2>Synopsis</h2><pre> use Lintian::DepMap::Properties;
 my $map = Lintian::DepMap::Properties-&gt;new;</pre><h2>Description</h2>Lintian::DepMap::Properties is a simple layer between Lintian::DepMap and the application allowing nodes to have application-defined properties.
<dl COMPACT><dt>add(node, [dependencies], [ref to property])
<dd>Adds a node with possibly one or more dependencies and sets the <tt>&quot;node&quot;</tt>'s property to the ref, if defined. The property must be a reference (it can be to a hash, an array, a function, an object, etc) and must be the last argument given to the method. 

 E.g. 

 <pre> $map-&gt;add('foo', {name =&gt; 'John Doe', age =&gt; 20});</pre><dt>addp(node[, prefix, dependency[, dependency...]], [ref to property])
<dd>Adds the given <tt>&quot;node&quot;</tt> to the map marking any third or more parameters, after prefixing them with <tt>&quot;prefix&quot;</tt>, as its dependencies and sets the <tt>&quot;node&quot;</tt>'s property to the ref, if defined. See <i>add()</i>'s description for more information about properties. E.g. 

 <pre> # pA and pB have no dependency:
 $map-&gt;addp('pA', {name =&gt; 'John Doe'});
 $map-&gt;addp('pB', {name =&gt; 'Jane Doe'});
 # Df depends on pA and pB:
 $map-&gt;addp('Df', 'p', 'A', 'B', {name =&gt; 'Doe Family'});</pre><dt>getp(node)
<dd>Returns the reference to the given <tt>&quot;node&quot;</tt>'s properties. 

 E.g. 

 <pre> # prints John Doe
 print $map-&gt;getp('foo')-&gt;{'name'};
 # changes the value of 'name'
 $map-&gt;getp('foo')-&gt;{'name'} = 'Jane Doe';
 # prints Jane Doe
 print $map-&gt;getp('foo')-&gt;{'name'};</pre></dl><h2>Author</h2>Originally written by Raphael Geissert &lt;atomo64 [at] gmail.com&gt; for Lintian.
