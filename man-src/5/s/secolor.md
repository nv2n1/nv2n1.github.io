---
title: "secolor(5)"
name: "secolor"
section: "5"
letter: "s"
url: "/docs/linux/man/5-secolor/"
description: "secolor.conf – The SELinux color configuration file"
---

<p>secolor.conf &#8211; The SELinux color configuration file</p>
<h2>Description</h2>
<p>This optional file controls the color to be associated to the context components associated to the <i>raw</i> context passed by <code><a href="/docs/linux/man/3-selinux_raw_context_to_color/">selinux_raw_context_to_color</a></code>(3), when context related information is to be displayed in color by an SELinux-aware application. </p>
<p> <code><a href="/docs/linux/man/3-selinux_raw_context_to_color/">selinux_raw_context_to_color</a></code>(3) obtains this color information from the active policy <code>secolor.conf</code> file as returned by <code><a href="/docs/linux/man/3-selinux_colors_path/">selinux_colors_path</a></code>(3).</p>
<h2>File Format</h2>
<p>The file format is as follows:</p>
<dl>
<dd><code>color</code> <i>color_name</i> <code>= #color_mask</code><br />
 [&#8230;] </p>
<p> <i>context_component string</i> <code>=</code> <i>fg_color_name bg_color_name</i><br />
 [&#8230;] </p>
</dl>
<p> Where:<br />
 <code>color</code></p>
<dl>
<dd>The color keyword. Each color entry is on a new line.</dl>
<p> <i>color_name</i></p>
<dl>
<dd>A single word name for the color (e.g. red).</dl>
<p> <i>color_mask</i></p>
<dl>
<dd>A color mask starting with a hash (#) that describes the hexadecimal RGB colors with black being #000000 and white being #ffffff.</dl>
<p> <i>context_component</i></p>
<dl>
<dd>The context component name that must be one of the following: </p>
<dl>
<dd>user, role, type or range</dl>
<p> Each <i>context_component</i> <i>string</i> &#8230; entry is on a new line.</dl>
<p> <i>string</i></p>
<dl>
<dd>This is the <i>context_component</i> string that will be matched with the <i>raw</i> context component passed by <code><a href="/docs/linux/man/3-selinux_raw_context_to_color/">selinux_raw_context_to_color</a></code>(3).<br />
 A wildcard &#8216;*&#8217; may be used to match any undefined string for the user, role and type <i>context_component</i> entries only.</dl>
<p> <i>fg_color_name</i></p>
<dl>
<dd>The color_name string that will be used as the foreground color. A <i>color_mask</i> may also be used.</dl>
<p> <i>bg_color_name</i></p>
<dl>
<dd>The color_name string that will be used as the background color. A <i>color_mask</i> may also be used.</dl>
<h2>Examples</h2>
<p>Example 1 entries are:</p>
<dl>
<dd>color black = #000000<br />
 color green = #008000<br />
 color yellow = #ffff00<br />
 color blue = #0000ff<br />
 color white = #ffffff<br />
 color red = #ff0000<br />
 color orange = #ffa500<br />
 color tan = #D2B48C </p>
<p> user * = black white<br />
 role * = white black<br />
 type * = tan orange<br />
 range s0-s0:c0.c1023 = black green<br />
 range s1-s1:c0.c1023 = white green<br />
 range s3-s3:c0.c1023 = black tan<br />
 range s5-s5:c0.c1023 = white blue<br />
 range s7-s7:c0.c1023 = black red<br />
 range s9-s9:c0.c1023 = black orange<br />
 range s15:c0.c1023 = black yellow</dl>
<p> Example 2 entries are:</p>
<dl>
<dd>color black = #000000<br />
 color green = #008000<br />
 color yellow = #ffff00<br />
 color blue = #0000ff<br />
 color white = #ffffff<br />
 color red = #ff0000<br />
 color orange = #ffa500<br />
 color tan = #d2b48c </p>
<p> user unconfined_u = #ff0000 green<br />
 role unconfined_r = red #ffffff<br />
 type unconfined_t = red orange<br />
 user user_u = black green<br />
 role user_r = white black<br />
 type user_t = tan red<br />
 user xguest_u = black yellow<br />
 role xguest_r = black red<br />
 type xguest_t = black green<br />
 user sysadm_u = white black<br />
 range s0:c0.c1023 = black white<br />
 user * = black white<br />
 role * = black white<br />
 type * = black white</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_raw_context_to_color/">selinux_raw_context_to_color</a></code>(3), <code><a href="/docs/linux/man/3-selinux_colors_path/">selinux_colors_path</a></code>(3) </p>
