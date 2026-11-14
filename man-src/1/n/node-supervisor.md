---
title: "node-supervisor(1)"
name: "node-supervisor"
section: "1"
letter: "n"
url: "/docs/linux/man/1-node-supervisor/"
---

<dl>
<dt>
<dd> Node Supervisor is used to restart programs when they crash. </p>
<p> It can also be used to restart programs when a *.js file changes.</dl>
<dl>
<dt>
<dd> Usage: </p>
<pre><code>
supervisor[options]&lt;program&gt;
    supervisor[options]--&lt;program&gt;[args...]
</code></pre>
<p> Required: </p>
<pre>
  &lt;program&gt;
    The program to run.
</pre>
<p> Options: </p>
<pre>
  -w|--watch &lt;watchItems&gt;
    A comma-delimited list of folders or js files to watch for changes.
    When a change to a js file occurs, reload the program
    Default is '.'
</pre>
<dl>
<dt>
<dd> <code>-i</code>|<code>&#8211;ignore</code> &lt;ignoreItems&gt; </p>
<pre>
    A comma-delimited list of folders to ignore for changes.
    No default
</pre>
<p> <code>-p</code>|<code>&#8211;poll-interval</code> &lt;milliseconds&gt; </p>
<pre>
    How often to poll watched files for changes.
    Defaults to Node default.
</pre>
<p> <code>-e</code>|<code>&#8211;extensions</code> &lt;extensions&gt; </p>
<pre>
    Specific file extensions to watch in addition to defaults.
    Used when --watch option includes folders
    Default is 'node,js'
</pre>
<p> <code>-x</code>|<code>&#8211;exec</code> &lt;executable&gt; </p>
<pre>
    The executable that runs the specified program.
    Default is 'node'
</pre>
<p> <code>&#8211;debug</code> </p>
<pre>
    Start node with --debug flag.
</pre>
<p> <code>&#8211;debug-brk</code>[=port] </p>
<pre>
    Start node with --debug-brk[=port] flag.
</pre>
<p> <code>&#8211;harmony</code> </p>
<pre>
    Start node with --harmony flag.
</pre>
<p> <code>-n</code>|<code>&#8211;no-restart-on</code> error|exit </p>
<pre>
    Don't automatically restart the supervised program if it ends.
    Supervisor will wait for a change in the source files.
    If &quot;error&quot;, an exit code of 0 will still restart.
    If &quot;exit&quot;, no restart regardless of exit code.
</pre>
<p> <code>&#8211;force-watch</code> </p>
<pre>
    Use fs.watch instead of fs.watchFile.
    This may be useful if you see a high cpu load on a windows machine.
</pre>
<p> <code>-h</code>|<code>&#8211;help</code>|-? </p>
<pre>
    Display these usage instructions.
</pre>
<p> <code>-q</code>|<code>&#8211;quiet</code> </p>
<pre>
    Suppress DEBUG messages
</pre>
<p> <code>-V</code>|<code>&#8211;verbose</code> </p>
<pre>
    Show extra DEBUG messages
</pre>
</dl>
<p> Examples: </p>
<pre>
  supervisor myapp.js
  supervisor myapp.coffee
  supervisor -w scripts -e myext -x myrunner myapp
  supervisor -- server.js -h host -p port
</dl>
</pre>
