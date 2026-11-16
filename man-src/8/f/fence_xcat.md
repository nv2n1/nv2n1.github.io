---
title: "fence_xcat(8)"
name: "fence_xcat"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_xcat/"
description: "fence_xcat – I/O Fencing agent for xcat environments"
---

<p>fence_xcat &#8211; I/O Fencing agent for xcat environments</p>
<h2>Synopsis</h2>
<p><code>fence_xcat</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_xcat is a wrapper to the rpower(1) command that is distributed with the xCAT project available at <a rel="nofollow" href="http://www.xcat.org.">http://www.xcat.org.</a> Use of fence_xcat requires that xcat has already been properly configured for your environment. Refer to xCAT(1) for more information on configuring xCAT. fence_xcat accepts options on the command line as well as from stdin. fenced sends parameters through stdin when it execs the agent. fence_xcat can be run by itself with command line options which is useful for testing. NOTE: It is recommended that <a href="/docs/linux/man/8-fence_bladecenter/">fence_bladecenter</a>(8) is used instead of fence_xcat if the bladecenter firmware supports telnet. This interface is much cleaner and easier to setup. Vendor URL: <a rel="nofollow" href="http://www.xcat.org">http://www.xcat.org</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-n</code> <i>nodename</i></dt>
<dd>The nodename as defined in nodelist.tab of the xCAT setup.</dd>
<dt><code>-o</code> <i>action</i></dt>
<dd>The action required. on, off, reset (default) or stat.</dd>
<dt><code>-r</code> <i>rpower</i></dt>
<dd>The path to the rpower binary.</dd>
<dt><code>-q</code></dt>
<dd>Quiet mode: print only error messages.</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></dt>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_xcat.</dd>
<dt><i>nodename = &lt; param &gt;</i></dt>
<dd>The nodename as defined in nodelist.tab of the xCAT setup.</dd>
<dt><i>action = &lt; param &gt;</i></dt>
<dd>The action required. on, off, reset (default) or stat.</dd>
<dt><i>rpower = &lt; param &gt;</i></dt>
<dd>The path to the rpower binary. </dd>
</dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8), <a href="/docs/linux/man/8-fence_bladecenter/">fence_bladecenter</a>(8), nodelist.tab(8), rpower(1), xCAT(1) </p>
