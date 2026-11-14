---
title: "set_allegro_resource_path(3)"
name: "set_allegro_resource_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_allegro_resource_path/"
description: "set_allegro_resource_path – Sets a specific resource search path. Allegro game programming library."
---

<p>set_allegro_resource_path &#8211; Sets a specific resource search path. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int set_allegro_resource_path(int priority, const char *path);</code></pre>
<h2>Description</h2>
<p>Sometimes Allegro doesn&#8217;t look in enough places to find a resource. For those special cases, you can call this function before loading your resource with additional paths to search for. You set up the priorities, higher numbers are searched for first. To modify an already setup path, call this function with the same priority and the new path. To remove an already setup path, call this function with the priority of the path and NULL as the path parameter. Example: </p>
<pre> set_allegro_resource_path(10, &quot;my_game/configs&quot;);
 set_allegro_resource_path(0, &quot;users/configs/&quot;);
 set_allegro_resource_path(-45, &quot;temp&quot;);</pre>
<p>These custom paths will be valid until you call allegro_exit(). You can call this function before install_allegro(), but after set_uformat() if you want to use a text encoding format other than the default.</p>
<h2>Return Value</h2>
<p>Returns non-zero on success, zero if the path could not be added or you wanted to remove a path and the priority used didn&#8217;t have any associated path. Modification of existing paths always succeeds. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-find_allegro_resource/">find_allegro_resource</a></code>(3) </p>
