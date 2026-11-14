---
title: "rrdlua(1)"
name: "rrdlua"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdlua/"
description: "RRDLua – Lua binding for RRDTool"
---

<h2 class="name">NAME</h2>
<p> RRDLua &#8211; Lua binding for RRDTool </p>
<h2>SYNOPSIS</h2>
<pre>
  require 'rrd'
  rrd.create(...)
  rrd.dump(...)
  rrd.fetch(...)
  rrd.first(...)
  rrd.graph(...)
  rrd.graphv(...)
  rrd.info(...)
  rrd.last(...)
  rrd.resize(...)
  rrd.restore(...)
  rrd.tune(...)
  rrd.update(...)
  rrd.updatev(...)
</pre>
<h2>DESCRIPTION</h2>
<h3>Calling Sequence</h3>
<p> This module accesses RRDtool functionality directly from within Lua. The arguments to the functions listed in the <font SIZE="-1">SYNOPSIS</font> are explained in the regular RRDtool documentation. The command-line call </p>
<pre>
    rrdtool update mydemo.rrd --template in:out N:12:13
</pre>
<p> gets turned into </p>
<pre>
    rrd.update (&quot;mydemo.rrd&quot;, &quot;--template&quot;, &quot;in:out&quot;, &quot;N:12:13&quot;)
</pre>
<p> Note that &#8211;template=in:out is also valid.</p>
<h3>Using with Lua 5.1</h3>
<p> Start your programs with: </p>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -package.cpath = '/usr/local/rrdtool-1.3.2/lib/lua/5.1/?.so;'..package.cpath
                                                                                                                  require 'rrd' -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
</code></pre>
<p> <font SIZE="-1">OBS:</font> If you configured with &#8211;enable-lua-site-install, you don&#8217;t need to set package.cpath like above.</p>
<h3>Using with Lua 5.0</h3>
<p> The Lua binding for RRDtool needs the Lua module compat-5.1 to work with Lua 5.0. Some Linux distros, like Ubuntu gutsy and hardy, have it already integrated in Lua 5.0 -dev packages, so you just have to require it: </p>
<pre>
    require 'compat-5.1'
</pre>
<p> For other platforms, the compat-5.1 module that comes with this binding will be installed for you in the same dir where RRDtool was installed, under the subdir &#8230;/lib/lua/5.0. In this case, you must tell your Lua programs where to find it by changing the Lua var <font SIZE="-1">LUA_PATH:</font> </p>
<p>    &#8212; compat-5.1.lua is only necessary for Lua 5.0 &#8212;&#8212;&#8212;&#8212;&#8212;-<br />
    &#8212; try only compat-5.1 installed with RRDtool package<br />
    local original_LUA_PATH = LUA_PATH<br />
    LUA_PATH = &#8216;/usr/local/rrdtool-1.3.2/lib/lua/5.0/?.lua&#8217;<br />
    require &#8216;compat-5.1&#8217;<br />
    LUA_PATH = original_LUA_PATH<br />
    original_LUA_PATH = nil<br />
    &#8212; end of code to require compat-5.1 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p>    Now we can require the rrd module in the same way we did for 5.1 above:</p>
<p>    &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
    package.cpath = &#8216;/usr/local/rrdtool-1.3.2/lib/lua/5.0/?.so;&#8217; ..<br />
                    package.cpath<br />
    require &#8216;rrd&#8217;<br />
    &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<h3>Error Handling</h3>
<p> The Lua RRDTool module functions will abort your program with a stack traceback when they can not make sense out of the arguments you fed them. However, you can capture and handle the errors yourself, instead of just letting the program abort, by calling the module functions through Lua protected calls &#8211; &#8216;pcall&#8217; or &#8216;xpcall&#8217;. </p>
<p>     Ex: program t.lua</p>
<p>     &#8212; compat-5.1.lua is only necessary for Lua 5.0 &#8212;&#8212;&#8212;&#8212;&#8212;-<br />
     &#8212; uncomment below if your distro has not compat-5.1<br />
     &#8212; original_LUA_PATH = LUA_PATH<br />
     &#8212; try only compat-5.1.lua installed with RRDtool package<br />
     &#8212; LUA_PATH = &#8216;/usr/local/rrdtool-1.3.2/lib/lua/5.0/?.lua&#8217;</p>
<p>     &#8212; here we use a protected call to require compat-5.1<br />
     local r = pcall(require, &#8216;compat-5.1&#8217;)<br />
     if not r then<br />
       print(&#8216;** could not load compat-5.1.lua&#8217;)<br />
       os.exit(1)<br />
     end</p>
<p>     &#8212; uncomment below if your distro has not compat-5.1<br />
     &#8212; LUA_PATH = original_LUA_PATH<br />
     &#8212; original_LUA_PATH = nil<br />
     &#8212; end of code to require compat-5.1 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p>     &#8212; If the Lua RRDTool module was installed together with RRDTool,<br />
     &#8212; in /usr/local/rrdtool-1.3.2/lib/lua/5.0, package.cpath must be<br />
     &#8212; set accordingly so that &#8216;require&#8217; can find the module:</p>
<p>     package.cpath = &#8216;/usr/local/rrdtool-1.3.2/lib/lua/5.0/?.so;&#8217; ..<br />
                     package.cpath</p>
<p>     local rrd = require &#8216;rrd&#8217;<br />
     rrd.update (&#8220;mydemo.rrd&#8221;,&#8221;N:12:13&#8243;)</p>
<p> If we execute the program above we&#8217;ll get: </p>
<p>$ lua t.lua</p>
<p>        lua : t.lua : 27 : opening &#8216;mydemo.rrd&#8217; : No such file or<br />
    directory<br />
        stack traceback : [C] : in function `update&#8217; t.lua : 27 : in main chunk<br />
                                                                      [C] :<br />
    ?</p>
<h3>Return Values</h3>
<p> The functions rrd.first, rrd.last, rrd.graph, rrd.info and rrd.fetch return their findings. </p>
<p> <code>rrd.first</code> returns a single <font SIZE="-1">INTEGER</font> representing the timestamp of the first data sample in an <font SIZE="-1">RRA</font> within an <font SIZE="-1">RRD</font> file. Example returning the first timestamp of the third <font SIZE="-1">RRA </font>(index 2): </p>
<pre>
     local firstdate = rrd.first('example.rrd', '--rraindex', 2)
</pre>
<p> <code>rrd.last</code> returns a single <font SIZE="-1">INTEGER</font> representing the last update time. </p>
<pre>
     local lastupdate = rrd.last('example.rrd')
</pre>
<p> <code>rrd.graph</code> returns the x-size and y-size of the created image and a table with the results of the <font SIZE="-1">PRINT</font> arguments. </p>
<pre>
     local xsize, ysize, averages = rrd.graph ...
     print(string.format(&quot;Image size: %dx%d&quot;, xsize, ysize)
     print(&quot;Averages: &quot;, table.concat(averages, ', '))
</pre>
<p> <code>rrd.info</code> returns a table where the keys and the values represent property names and property values of the <font SIZE="-1">RRD.</font> </p>
<pre>
     local info = rrd.info(&quot;test.rrd&quot;)
     for key, value in pairs(info) do
       print(key, ' = ', value)
     end
</pre>
<p> <code>rrd.graphv</code> takes the same parameters as rrd.graph but it returns a table only. The table returned contains meta information about the graph, like its size as well as the position of the graph area on the image. When called with and empty filename, the contents of the graph will be returned in the table as well (key &#8216;image&#8217;). </p>
<p> <code>rrd.updatev</code> also returns a table. The keys of the table are strings formed by the concatenation of timestamp, <font SIZE="-1">RRA</font> index and data source name for each consolidated data point (<font SIZE="-1">CDP</font>) written to disk as a result of the current update call. The key values are <font SIZE="-1">CDP</font> values. </p>
<p> <code>rrd.fetch</code> is the most complex of the pack regarding return values. It returns 5 values: the initial timestamp, the step, two parallel arrays containing the data source names and their data points respectively, and the final timestamp. </p>
<pre><code>
     --require compat-5.1 if necessary
    
     package.cpath = '/usr/local/rrdtool-1.3.2/lib/lua/5.0/?.so;' ..
                     package.cpath
    
     local rrd = require "rrd"
     local first, last = rrd.first("test.rrd"), rrd.last("test.rrd")
     local start, step, names, data =
       rrd.fetch("test.rrd", "--start", first, "--end", last, "AVERAGE")
     io.write(string.format("Start:       %s (%d)
",
                            os.date("%c", start),start))
     io.write("Step size:   ", step, " seconds
")
     io.write("DS names:    ", table.concat(names, ', '), "
")
     io.write("Data points: ", #data[1], "
")
     io.write("Data:
")
     for i,dp in ipairs(data) do
       io.write(os.date("%t", start), " (", start, "): ")
       start = start + step
       for j,v in ipairs(dp) do
         io.write(v, " ")
       end
     io.write("
")
     end
</code></pre>
<h2>AUTHOR</h2>
<p> Fidelis Assis &lt;fidelis [at] pobox.com&gt; </p>
<h2>Index</h2>
