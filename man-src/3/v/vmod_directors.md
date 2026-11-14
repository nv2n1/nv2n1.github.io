---
title: "vmod_directors(3)"
name: "vmod_directors"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vmod_directors/"
description: "vmod_directors – Backend traffic directors"
---

<p>vmod_directors &#8211; Backend traffic directors</p>
<h2>Synopsis</h2>
<p>import directors [from &quot;path&quot;] ;</p>
<h2>Description</h2>
<p><i>vmod_directors</i> enables backend load balancing in Varnish. The module implements a set of basic load balancing techniques, and also serves as an example on how one could extend the load balancing capabilities of Varnish. To enable load balancing you must import this vmod (directors) in your VCL:: </p>
<pre>import directors;</pre>
<p>Then you define your backends. Once you have the backends declared you can add them to a director. This happens in executed VCL code. If you want to emulate the previous behavior of Varnish 3.0 you can just initialize the directors in vcl_init, like this:: </p>
<pre><code>sub vcl_init {
    new vdir = directors.round_robin();
    vdir.add_backend(backend1);
    vdir.add_backend(backend2);
}</code></pre>
<p> As you can see there is nothing keeping you from manipulating the directors elsewhere in VCL. So, you could have VCL code that would add more backends to a director when a certain URL is called. Note that directors can use other directors as backends.</p>
<h2>Contents</h2>
<dl>
<dt>&bull;</p>
<dd>Object fallback</p>
<dt>&bull;</p>
<dd>VOID fallback.add_backend(BACKEND)</p>
<dt>&bull;</p>
<dd>BACKEND fallback.backend()</p>
<dt>&bull;</p>
<dd>Object hash</p>
<dt>&bull;</p>
<dd>VOID hash.add_backend(BACKEND, REAL)</p>
<dt>&bull;</p>
<dd>BACKEND hash.backend(STRING_LIST)</p>
<dt>&bull;</p>
<dd>Object random</p>
<dt>&bull;</p>
<dd>VOID random.add_backend(BACKEND, REAL)</p>
<dt>&bull;</p>
<dd>BACKEND random.backend()</p>
<dt>&bull;</p>
<dd>Object round_robin</p>
<dt>&bull;</p>
<dd>VOID round_robin.add_backend(BACKEND)</p>
<dt>&bull;</p>
<dd>BACKEND round_robin.backend()</dl>
<h2>Object Round_Robin</h2>
<dl>
<dt><code>Description</code></p>
<dd>Create a round robin director. </p>
<p> This director will pick backends in a round robin fashion.</p>
<dt><code>Example</code></p>
<dd>new vdir = directors.round_robin();</dl>
<h3>VOID round_robin.add_backend(BACKEND)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID round_robin.add_backend(BACKEND)</p>
<dt><code>Description</code></p>
<dd>Add a backend to the round-robin director.</p>
<dt><code>Example</code></p>
<dd>vdir.add_backend(backend1); vdir.add_backend(backend2);</dl>
<h3>BACKEND round_robin.backend()</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>BACKEND round_robin.backend()</p>
<dt><code>Description</code></p>
<dd>Pick a backend from the director.</p>
<dt><code>Example</code></p>
<dd>set req.backend_hint = vdir.backend();</dl>
<h2>Object Fallback</h2>
<dl>
<dt><code>Description</code></p>
<dd>Create a fallback director. </p>
<p> A fallback director will try each of the added backends in turn, and return the first one that is healthy.</p>
<dt><code>Example</code></p>
<dd>new vdir = directors.fallback();</dl>
<h3>VOID fallback.add_backend(BACKEND)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID fallback.add_backend(BACKEND)</p>
<dt><code>Description</code></p>
<dd>Add a backend to the director. </p>
<p> Note that the order in which this is done matters for the fallback director.</p>
<dt><code>Example</code></p>
<dd>vdir.add_backend(backend1); vdir.add_backend(backend2);</dl>
<h3>BACKEND fallback.backend()</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>BACKEND fallback.backend()</p>
<dt><code>Description</code></p>
<dd>Pick a backend from the director.</p>
<dt><code>Example</code></p>
<dd>set req.backend_hint = vdir.backend();</dl>
<h2>Object Random</h2>
<dl>
<dt><code>Description</code></p>
<dd>Create a random backend director. </p>
<p> The random director distributes load over the backends using a weighted random probability distribution.</p>
<dt><code>Example</code></p>
<dd>new vdir = directors.random();</dl>
<h3>VOID random.add_backend(BACKEND, REAL)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID random.add_backend(BACKEND, REAL)</p>
<dt><code>Description</code></p>
<dd>Add a backend to the director with a given weight. </p>
<p> Each backend backend will receive approximately 100 * (weight / (sum(all_added_weights))) per cent of the traffic sent to this director.</p>
<dt><code>Example</code></p>
<dd>vdir.add_backend(backend1, 10); vdir.add_backend(backend2, 5); # 2/3 to backend1, 1/3 to backend2.</dl>
<h3>BACKEND random.backend()</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>BACKEND random.backend()</p>
<dt><code>Description</code></p>
<dd>Pick a backend from the director.</p>
<dt><code>Example</code></p>
<dd>set req.backend_hint = vdir.backend();</dl>
<h2>Object Hash</h2>
<dl>
<dt><code>Description</code></p>
<dd>Create a hashing backend director. </p>
<p> The director chooses the backend server by computing a hash/digest of the string given to .backend(). </p>
<p> Commonly used with <code>client.identity</code> or a session cookie to get sticky sessions.</p>
<dt><code>Example</code></p>
<dd>new vdir = directors.hash();</dl>
<h3>VOID hash.add_backend(BACKEND, REAL)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID hash.add_backend(BACKEND, REAL)</p>
<dt><code>Description</code></p>
<dd>Add a backend to the director with a certain weight. </p>
<p> Weight is used as in the random director. Recommended value is 1.0 unless you have special needs.</p>
<dt><code>Example</code></p>
<dd>vdir.add_backend(backend1, 1.0); vdir.add_backend(backend2, 1.0);</dl>
<h3>BACKEND hash.backend(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>BACKEND hash.backend(STRING_LIST)</p>
<dt><code>Description</code></p>
<dd>Pick a backend from the backend director. </p>
<p> Use the string or list of strings provided to pick the backend.</p>
<dt><code>Example</code></p>
<dd>set req.backend_hint = vdir.backend(req.http.cookie); # pick a backend based on the cookie header from the client </p>
</dl>
