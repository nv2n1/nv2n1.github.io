---
title: "luajit(1)"
name: "luajit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luajit/"
description: "luajit – Just-In-Time Compiler for the Lua Language"
---

<h2>NAME</h2>
<p> luajit &#8211; Just-In-Time Compiler for the Lua Language</p>
<h2>SYNOPSIS</h2>
<p> <code>luajit</code> [<i>options</i>]&#8230; [<i>script</i> [<i>args</i>]&#8230;]</p>
<h2>WEB SITE</h2>
<p> <i><a rel="nofollow" href="http://luajit.org">http://luajit.org</a></i></p>
<h2>DESCRIPTION</h2>
<p> This is the command-line program to run Lua programs with <code>LuaJIT</code>. </p>
<p> <code>LuaJIT</code> is a just-in-time (JIT) compiler for the Lua language. The virtual machine (VM) is based on a fast interpreter combined with a trace compiler. It can significantly improve the performance of Lua programs. </p>
<p> <code>LuaJIT</code> is API- and ABI-compatible with the VM of the standard Lua 5.1 interpreter. When embedding the VM into an application, the built library can be used as a drop-in replacement.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e </code><i>chunk</i></p>
<dd> Run the given chunk of Lua code.</p>
<dt><code>-l </code><i>library</i></p>
<dd> Load the named library, just like <code>require(&quot;</code><i>library</i><code>&quot;)</code>.</p>
<dt><code>-b </code><i>&#8230;</i></p>
<dd> Save or list bytecode. Run without arguments to get help on options.</p>
<dt><code>-j </code><i>command</i></p>
<dd> Perform LuaJIT control command (optional space after <code>-j</code>).</p>
<dt><code>-O</code><i>[opt]</i></p>
<dd> Control LuaJIT optimizations.</p>
<dt><code>-i</code></p>
<dd> Run in interactive mode.</p>
<dt><code>-v</code></p>
<dd> Show <code>LuaJIT</code> version.</p>
<dt><code>-E</code></p>
<dd> Ignore environment variables.</p>
<dt><code>&#8212;</code></p>
<dd> Stop processing options.</p>
<dt><code>&#8211;</code></p>
<dd> Read script from stdin instead.</dl>
<p> After all options are processed, the given <i>script</i> is run. The arguments are passed in the global <i>arg</i> table. </p>
<p> Interactive mode is only entered, if no <i>script</i> and no <code>-e</code> option is given. Interactive mode can be left with EOF (<i>Ctrl-Z</i><code>). </code></p>
<h2>EXAMPLES</h2>
<dl>
<dt>luajit hello.lua world</p>
<dd>
<p> Prints &quot;Hello world&quot;, assuming <i>hello.lua</i> contains: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>print(&quot;Hello&quot;, arg[1])</p>
<dt>luajit -e &quot;local x=0; for i=1,1e9 do x=x+i end; print(x)&quot;</p>
<dd>
<p> Calculates the sum of the numbers from 1 to 1000000000.<br />
 And finishes in a reasonable amount of time, too.</p>
<dt>luajit -jv -e &quot;for i=1,10 do for j=1,10 do for k=1,100 do end end end&quot;</p>
<dd>
<p> Runs some nested loops and shows the resulting traces.</dl>
<h2>COPYRIGHT</h2>
<p> <code>LuaJIT</code> is Copyright &#169; 2005-2015 Mike Pall.<br />
 <code>LuaJIT</code> is open source software, released under the MIT license.</p>
<h2>SEE ALSO</h2>
<p> More details in the provided HTML docs or at: <i><a rel="nofollow" href="http://luajit.org">http://luajit.org</a></i><br />
 More about the Lua language can be found at: <i><a rel="nofollow" href="http://lua.org/docs.html">http://lua.org/docs.html</a></i> </p>
<p> <a href="/docs/linux/man/1-lua/">lua</a>(1) </p>
<h2>Index</h2>
