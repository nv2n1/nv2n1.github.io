---
title: "revpath(1)"
name: "revpath"
section: "1"
letter: "r"
url: "/docs/linux/man/1-revpath/"
description: "revpath – generate a relative path that can be used to undo a change-directory"
---

<h2>NAME</h2>
<p> revpath &#8211; generate a relative path that can be used to undo a change-directory</p>
<h2>SYNOPSIS</h2>
<p> <code>revpath</code> <i>path</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>revpath</i> program prints out a relative path that is the &#8220;reverse&#8221; or &#8220;inverse&#8221; of <i>path</i>. Start with two directories <i>top</i> and <i>bottom</i>, with the latter below the former, and <i>path</i> is the location of <i>bottom</i> relative to <i>top</i>. The output of <i>revpath</i> is the location of <i>top</i> relative to <i>bottom</i>. The resulting path contains a trailing `/&#8217; character when the result is non-trivial. If <i>path</i> is equivalent to `.&#8217;, the resulting output is empty. If <i>path</i> is invalid in some way (e.g., doesn&#8217;t represent the path to a subdirectory) the output is also empty and no error messages are ever generated.</p>
<h2>DIAGNOSTICS</h2>
<p> There are no diagnostics. Error conditions are silently ignored, and the exit status is always 0.</p>
<h2>BUGS</h2>
<p> It isn&#8217;t possible to reverse arbitrary relative paths. If any path element between the two end points of <i>path</i> is a symbolic link, the results will probably be incorrect. </p>
<h2>Index</h2>
