---
title: "more(1)"
name: "more"
section: "1"
letter: "m"
url: "/docs/linux/man/1-more/"
description: "more – file perusal filter for crt viewing"
---

<h2 class="name">NAME</h2>
<p> more &#8211; file perusal filter for crt viewing </p>
<h2>SYNOPSIS</h2>
<p> <code>more</code> [options] <i>file</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>more</code> is a filter for paging through text one screenful at a time. This version is especially primitive. Users should realize that <code><a href="/docs/linux/man/1-less/">less</a></code>(1) provides <code><a href="/docs/linux/man/1-more/">more</a></code>(1) emulation plus extensive enhancements.</p>
<h2>OPTIONS</h2>
<p> Options are also taken from the environment variable <code>MORE</code> (make sure to precede them with a dash (<code>&#8211;</code>)) but command-line options will override those. </p>
<p> <code>-d</code>, <code>&#8211;silent</code></p>
<dl>
<dt>
<dd> Prompt with &quot;[Press space to continue, &#8216;q&#8217; to quit.]&quot;, and display &quot;[Press &#8216;h&#8217; for instructions.]&quot; instead of ringing the bell when an illegal key is pressed.</dl>
<p> <code>-l</code>, <code>&#8211;logical</code></p>
<dl>
<dt>
<dd> Do not pause after any line containing a <code>^L</code> (form feed).</dl>
<p> <code>-f</code>, <code>&#8211;no-pause</code></p>
<dl>
<dt>
<dd> Count logical lines, rather than screen lines (i.e., long lines are not folded).</dl>
<p> <code>-p</code>, <code>&#8211;print-over</code></p>
<dl>
<dt>
<dd> Do not scroll. Instead, clear the whole screen and then display the text. Notice that this option is switched on automatically if the executable is named <code>page</code>.</dl>
<p> <code>-c</code>, <code>&#8211;clean-print</code></p>
<dl>
<dt>
<dd> Do not scroll. Instead, paint each screen from the top, clearing the remainder of each line as it is displayed.</dl>
<p> <code>-s</code>, <code>&#8211;squeeze</code></p>
<dl>
<dt>
<dd> Squeeze multiple blank lines into one.</dl>
<p> <code>-u</code>, <code>&#8211;plain</code></p>
<dl>
<dt>
<dd> Suppress underlining. This option is silently ignored as backwards compatibility.</dl>
<p> <code>-n</code>, <code>&#8211;lines</code> <i>number</i></p>
<dl>
<dt>
<dd> Specify the <i>number</i> of lines per screenful. The <i>number</i> argument is a positive decimal integer. The <code>&#8211;lines</code> option shall override any values obtained from any other source, such as number of lines reported by terminal.</dl>
<p> <code>&#8211;</code><i>number</i></p>
<dl>
<dt>
<dd> A numeric option means the same as <code>&#8211;lines</code> option argument.</dl>
<p> <code>+</code><i>number</i></p>
<dl>
<dt>
<dd> Start displaying each file at line <i>number</i>.</dl>
<p> <code>+</code>/<i>string</i></p>
<dl>
<dt>
<dd> The <i>string</i> to be searched in each file before starting to display it.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h2>COMMANDS</h2>
<p> Interactive commands for <code>more</code> are based on <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1). Some commands may be preceded by a decimal number, called k in the descriptions below. In the following descriptions, <code>^X</code> means <code>control-X</code>. </p>
<p> <code>h</code> or <code>?</code></p>
<dl>
<dt>
<dd> Help; display a summary of these commands. If you forget all other commands, remember this one.</dl>
<p> <code>SPACE</code></p>
<dl>
<dt>
<dd> Display next k lines of text. Defaults to current screen size.</dl>
<p> <code>z</code></p>
<dl>
<dt>
<dd> Display next k lines of text. Defaults to current screen size. Argument becomes new default.</dl>
<p> <code>RETURN</code></p>
<dl>
<dt>
<dd> Display next k lines of text. Defaults to 1. Argument becomes new default.</dl>
<p> <code>d</code> or <code>^D</code></p>
<dl>
<dt>
<dd> Scroll k lines. Default is current scroll size, initially 11. Argument becomes new default.</dl>
<p> <code>q</code> or <code>Q</code> or <code>INTERRUPT</code></p>
<dl>
<dt>
<dd> Exit.</dl>
<p> <code>s</code></p>
<dl>
<dt>
<dd> Skip forward k lines of text. Defaults to 1.</dl>
<p> <code>f</code></p>
<dl>
<dt>
<dd> Skip forward k screenfuls of text. Defaults to 1.</dl>
<p> <code>b</code> or <code>^B</code></p>
<dl>
<dt>
<dd> Skip backwards k screenfuls of text. Defaults to 1. Only works with files, not pipes.</dl>
<p> <code>&#8216;</code></p>
<dl>
<dt>
<dd> Go to the place where the last search started.</dl>
<p> <code>=</code></p>
<dl>
<dt>
<dd> Display current line number.</dl>
<p> <code>/pattern</code></p>
<dl>
<dt>
<dd> Search for kth occurrence of regular expression. Defaults to 1.</dl>
<p> <code>n</code></p>
<dl>
<dt>
<dd> Search for kth occurrence of last regular expression. Defaults to 1.</dl>
<p> <code>!command</code> or <code>:!command</code></p>
<dl>
<dt>
<dd> Execute <i>command</i> in a subshell.</dl>
<p> <code>v</code></p>
<dl>
<dt>
<dd> Start up an editor at current line. The editor is taken from the environment variable <code>VISUAL</code> if defined, or <code>EDITOR</code> if <code>VISUAL</code> is not defined, or defaults to <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) if neither <code>VISUAL</code> nor <code>EDITOR</code> is defined.</dl>
<p> <code>^L</code></p>
<dl>
<dt>
<dd> Redraw screen.</dl>
<p> <code>:n</code></p>
<dl>
<dt>
<dd> Go to kth next file. Defaults to 1.</dl>
<p> <code>:p</code></p>
<dl>
<dt>
<dd> Go to kth previous file. Defaults to 1.</dl>
<p> <code>:f</code></p>
<dl>
<dt>
<dd> Display current file name and line number.</dl>
<p> <code>.</code></p>
<dl>
<dt>
<dd> Repeat previous command.</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>more</code> command respects the following environment variables, if they exist: </p>
<p> <code>MORE</code></p>
<dl>
<dt>
<dd> This variable may be set with favored options to <code>more</code>.</dl>
<p> <code>SHELL</code></p>
<dl>
<dt>
<dd> Current shell in use (normally set by the shell at login time).</dl>
<p> <code>TERM</code></p>
<dl>
<dt>
<dd> The terminal type used by <code>more</code> to get the terminal characteristics necessary to manipulate the screen.</dl>
<p> <code>VISUAL</code></p>
<dl>
<dt>
<dd> The editor the user prefers. Invoked when command key <i>v</i> is pressed.</dl>
<p> <code>EDITOR</code></p>
<dl>
<dt>
<dd> The editor of choice when <code>VISUAL</code> is not specified.</dl>
<h2>HISTORY</h2>
<p> The <code>more</code> command appeared in 3.0BSD. This man page documents <code>more</code> version 5.19 (Berkeley 6/29/88), which is currently in use in the Linux community. Documentation was produced using several other versions of the man page, and extensive inspection of the source code.</p>
<h2>AUTHORS</h2>
<p> Eric Shienbrood, UC Berkeley. </p>
<p> Modified by Geoff Peck, UCB to add underlining, single spacing. </p>
<p> Modified by John Foderaro, UCB to add -c and MORE environment variable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-less/">less</a></code>(1), <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>more</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
