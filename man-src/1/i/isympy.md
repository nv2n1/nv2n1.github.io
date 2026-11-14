---
title: "isympy(1)"
name: "isympy"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isympy/"
description: "isympy – interactive shell for SymPy"
---

<h2>NAME</h2>
<p> isympy &#8211; interactive shell for SymPy</p>
<h2>SYNOPSIS</h2>
<p> <code>isympy</code> [<code>-c</code> | <code>&#8211;console</code>] [<code>-p</code> ENCODING | <code>&#8211;pretty</code> ENCODING] [<code>-t</code> TYPE | <code>&#8211;types</code> TYPE] [<code>-o</code> ORDER | <code>&#8211;order</code> ORDER] [<code>-q</code> | <code>&#8211;quiet</code>] [<code>-d</code> | <code>&#8211;doctest</code>] [<code>-C</code> | <code>&#8211;no-cache</code>] [<code>-a</code> | <code>&#8211;auto</code>] [<code>-D</code> | <code>&#8211;debug</code>] [ &#8212; | PYTHONOPTIONS] <code>isympy</code> [ {<code>-h</code> | <code>&#8211;help</code>} | {<code>-v</code> | <code>&#8211;version</code>} ]</p>
<h2>DESCRIPTION</h2>
<p> isympy is a Python shell for SymPy. It is just a normal python shell (ipython shell if you have the ipython package installed) that executes the following commands so that you don&#8217;t have to: </p>
<pre>
&gt;&gt;&gt; from __future__ import division
&gt;&gt;&gt; from sympy import *
&gt;&gt;&gt; x, y, z = symbols(&quot;x,y,z&quot;)
&gt;&gt;&gt; k, m, n = symbols(&quot;k,m,n&quot;, integer=True)
    
</pre>
<p> So starting isympy is equivalent to starting python (or ipython) and executing the above commands by hand. It is intended for easy and quick experimentation with SymPy. For more complicated programs, it is recommended to write a script and import things explicitly (using the &quot;from sympy import sin, log, Symbol, &#8230;&quot; idiom).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>SHELL</i>, <code>&#8211;console=</code><i>SHELL</i></p>
<dd> Use the specified shell (python or ipython) as console backend instead of the default one (ipython if present or python otherwise). </p>
<p> Example: isympy -c python </p>
<p> <i>SHELL</i> could be either &#8216;ipython&#8217; or &#8216;python&#8217;</p>
<dt><code>-p </code><i>ENCODING</i>, <code>&#8211;pretty=</code><i>ENCODING</i></p>
<dd> Setup pretty printing in SymPy. By default, the most pretty, unicode printing is enabled (if the terminal supports it). You can use less pretty ASCII printing instead or no pretty printing at all. </p>
<p> Example: isympy -p no </p>
<p> <i>ENCODING</i> must be one of &#8216;unicode&#8217;, &#8216;ascii&#8217; or &#8216;no&#8217;.</p>
<dt><code>-t </code><i>TYPE</i>, <code>&#8211;types=</code><i>TYPE</i></p>
<dd> Setup the ground types for the polys. By default, gmpy ground types are used if gmpy2 or gmpy is installed, otherwise it falls back to python ground types, which are a little bit slower. You can manually choose python ground types even if gmpy is installed (e.g., for testing purposes). </p>
<p> Note that sympy ground types are not supported, and should be used only for experimental purposes. </p>
<p> Note that the gmpy1 ground type is primarily intended for testing; it the use of gmpy even if gmpy2 is available. </p>
<p> This is the same as setting the environment variable SYMPY_GROUND_TYPES to the given ground type (e.g., SYMPY_GROUND_TYPES=&#8217;gmpy&#8217;) </p>
<p> The ground types can be determined interactively from the variable sympy.polys.domains.GROUND_TYPES inside the isympy shell itself. </p>
<p> Example: isympy -t python </p>
<p> <i>TYPE</i> must be one of &#8216;gmpy&#8217;, &#8216;gmpy1&#8217; or &#8216;python&#8217;.</p>
<dt><code>-o </code><i>ORDER</i>, <code>&#8211;order=</code><i>ORDER</i></p>
<dd> Setup the ordering of terms for printing. The default is lex, which orders terms lexicographically (e.g., x**2 + x + 1). You can choose other orderings, such as rev-lex, which will use reverse lexicographic ordering (e.g., 1 + x + x**2). </p>
<p> Note that for very large expressions, ORDER=&#8217;none&#8217; may speed up printing considerably, with the tradeoff that the order of the terms in the printed expression will have no canonical order </p>
<p> Example: isympy -o rev-lax </p>
<p> <i>ORDER</i> must be one of &#8216;lex&#8217;, &#8216;rev-lex&#8217;, &#8216;grlex&#8217;, &#8216;rev-grlex&#8217;, &#8216;grevlex&#8217;, &#8216;rev-grevlex&#8217;, &#8216;old&#8217;, or &#8216;none&#8217;.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Print only Python&#8217;s and SymPy&#8217;s versions to stdout at startup, and nothing else.</p>
<dt><code>-d</code>, <code>&#8211;doctest</code></p>
<dd> Use the same format that should be used for doctests. This is equivalent to &#8216;<i>isympy -c python -p no</i>&#8216;.</p>
<dt><code>-C</code>, <code>&#8211;no-cache</code></p>
<dd> Disable the caching mechanism. Disabling the cache may slow certain operations down considerably. This is useful for testing the cache, or for benchmarking, as the cache can result in deceptive benchmark timings. </p>
<p> This is the same as setting the environment variable SYMPY_USE_CACHE to &#8216;no&#8217;.</p>
<dt><code>-a</code>, <code>&#8211;auto</code></p>
<dd> Automatically create missing symbols. Normally, typing a name of a Symbol that has not been instantiated first would raise NameError, but with this option enabled, any undefined name will be automatically created as a Symbol. This only works in IPython 0.11. </p>
<p> Note that this is intended only for interactive, calculator style usage. In a script that uses SymPy, Symbols should be instantiated at the top, so that it&#8217;s clear what they are. </p>
<p> This will not override any names that are already defined, which includes the single character letters represented by the mnemonic QCOSINE (see the &quot;Gotchas and Pitfalls&quot; document in the documentation). You can delete existing names by executing &quot;del name&quot; in the shell itself. You can see if a name is defined by typing &quot;&#8217;name&#8217; in globals()&quot;. </p>
<p> The Symbols that are created using this have default assumptions. If you want to place assumptions on symbols, you should create them using symbols() or var(). </p>
<p> Finally, this only works in the top level namespace. So, for example, if you define a function in isympy with an undefined Symbol, it will not work.</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Enable debugging output. This is the same as setting the environment variable SYMPY_DEBUG to &#8216;True&#8217;. The debug status is set in the variable SYMPY_DEBUG within isympy.</p>
<dt>&#8212; <i>PYTHONOPTIONS</i></p>
<dd> These options will be passed on to <i>ipython (1)</i> shell. Only supported when ipython is being used (standard python shell not supported). </p>
<p> Two dashes (&#8211;) are required to separate <i>PYTHONOPTIONS</i> from the other isympy options. </p>
<p> For example, to run iSymPy without startup banner and colors: </p>
<p> isympy -q -c ipython &#8212; &#8211;colors=NoColor</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help output and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print isympy version information and exit.</dl>
<h2>FILES</h2>
<dl>
<dt><i>${HOME}/.sympy-history</i></p>
<dd> Saves the history of commands when using the python shell as backend.</dl>
<h2>BUGS</h2>
<p> The upstreams BTS can be found at &lt;<a rel="nofollow" href="https://github.com/sympy/sympy/issues">https://github.com/sympy/sympy/issues</a>&gt; Please report all bugs that you find in there, this will help improve the overall quality of SymPy.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipython/">ipython</a></code>(1), <code><a href="/docs/linux/man/1-python/">python</a></code>(1) </p>
<h2>Index</h2>
