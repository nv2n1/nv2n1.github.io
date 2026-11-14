---
title: "osd_cat(1)"
name: "osd_cat"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osd_cat/"
description: "osd_cat – X on-screen file displayer"
---

<h2>NAME</h2>
<p> osd_cat &#8211; X on-screen file displayer</p>
<h2>SYNOPSIS</h2>
<p> <code>osd_cat</code> [<i>OPTION</i>] [<i>FILE</i>]&#8230;<br />
 <code>osd_cat</code> <code>-b percentage</code>|<code>slider</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> Display FILE, or standard input, on X screen.</p>
<dl>
<dt><code>-p</code>, <code>&#8211;pos</code>=<i>POS</i></p>
<dd> This option tells <code>osd_cat</code> where to display the text. <i>POS</i> can be <code>top</code>, <code>middle</code>, or <code>bottom</code>. The default is <code>top</code>.</p>
<dt><code>-o</code>, <code>&#8211;offset</code>=<i>OFFSET</i></p>
<dd> This option specifies the <i>offset</i> from the top or bottom of screen the text is displayed. The default is <code>0</code>.</p>
<dt><code>-A</code>, <code>&#8211;align</code>=<i>ALIGN</i></p>
<dd> This option tells <code>osd_cat</code> where to display the text. <i>ALIGN</i> can be <code>left</code>, <code>right</code> or <code>center</code>. The default is <code>left</code>.</p>
<dt><code>-i</code>, <code>&#8211;indent</code>=<i>OFFSET</i></p>
<dd> This option specifies the <i>INDENT</i> from the left of screen the text is displayed. The default is <code>0</code>.</p>
<dt><code>-f</code>, <code>&#8211;font</code>=<i>FONT</i></p>
<dd> This option specifies the <i>FONT</i> to be used for displaying the text. The default is <code>fixed</code>.</p>
<dt><code>-c</code>, <code>&#8211;color</code>=<i>COLOR</i></p>
<dd> This option specifies the <i>COLOR</i> to be used for displaying the text. The default is <code>red</code>.</p>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>TIME</i></p>
<dd> This option specifies the number of seconds the text is displayed. The default is <code>5</code> seconds.</p>
<dt><code>-l</code>, <code>&#8211;lines</code>=<i>LINES</i></p>
<dd> This option specifies the number of <i>LINES</i> to scroll the display over. The default is <code>5</code>.</p>
<dt><code>-s</code>, <code>&#8211;shadow</code>=<i>OFFSET</i></p>
<dd> This option specifies the <i>OFFSET</i> of the text shadow. The default is <code>0</code>, which means no text shadow is created.</p>
<dt><code>-a</code>, <code>&#8211;age</code>[=<i>SCROLL_AGE</i>]</p>
<dd> This option affects screen redrawing. If <i>SCROLL_AGE</i> seconds pass before a new line is ready (for example, you&#8217;re reading from a pipe), all lines are cleared at once instead of being scrolled off as new lines replace old lines. The default is <code>0</code>.<br />
 When no <i>SCROLL_AGE</i> is explicitly given, the current value from <i>DELAY</i> is used.</p>
<dt><code>-w</code>, <code>&#8211;wait</p>
<dd> This option also affects screen redrawing. When there is data ready to be put on screen, this option will cause osd_cat</code> to wait until the display is clear. An alternative to scrolling.</p>
<dt><code>-b</code>, <code>&#8211;barmode</code>=<i>TYPE</i></p>
<dd> Lets you display a percentage or slider bar instead of just text. <i>TYPE</i> may be <code>percentage</code> or <code>slider</code>. In this mode no text is read from any file, but the following options can be used:</p>
<dt><code>-P</code>, <code>&#8211;percentage</code>=<i>PERCENTAGE</i></p>
<dd> This option specified the position of the percentage / slider bar. <i>PERCENTAGE</i> may be in the range from <code>0</code> to <code>100</code>, the default is <code>50</code>.</p>
<dt><code>-T</code>, <code>&#8211;text</code>=<i>TEXT</i></p>
<dd> This option specifies an optional <i>TEXT</i> which gets displayed above the percentage bar. The default is empty, so no additional text is displayed.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display help (which is often more up to date) and exit</dl>
<p> With no <i>FILE</i>, or when <i>FILE</i> is <code>&#8211;</code>, read standard input.</p>
<h2>AUTHOR</h2>
<p> Martijn van de Streek &lt;martijn [at] foodfight.org&gt;, Some patching done by Malcolm Valentine &lt;farkit [at] iprimus.com.au&gt; and Tim Wright &lt;tim [at] ignavus.net&gt;.<br />
 xosd was written by Andre Renaud &lt;andre [at] ignavus.net&gt; and is maintained by Tim Wright &lt;tim [at] ignavus.net&gt;</p>
<h2>SEE ALSO</h2>
<p> More information on the X OSD Library and its author can be found on <a rel="nofollow" href="http://www.ignavus.net/software.html">http://www.ignavus.net/software.html</a></p>
<h2>COPYRIGHT</h2>
<p> It is distributed under the GNU General Public License. </p>
<h2>Index</h2>
