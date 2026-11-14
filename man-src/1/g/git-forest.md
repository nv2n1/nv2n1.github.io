---
title: "git-forest(1)"
name: "git-forest"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-forest/"
---

<h2>Name</h2>
<dl>
<dt>git-forest &#8212; display the commit history forest</p>
<dd></dl>
<h2>Syntax</h2>
<p> <code>git-forest</code> [<code>-a</code>] [<code>&#8211;no-rebase</code>] [<code>&#8211;style=</code><i>number</i>] [<code>&#8211;sha</code>] [<code>&#8211;svdepth=</code><i>depth</i>] [<i>rev-list-options</i>] [<i>refspec</i>&#8230;]</p>
<h2>Description</h2>
<p> git-forest is a command-line zero-lookahead git repository history visualizer with Unicode output with a bit of gitk resemblance.</p>
<h3>Why another program?</h3>
<p> The tree visualization of gitk is very useful, but there were (git 1.5.4 timeframe) no decent visualizers that can run in a console window, without the need to have X around (which gitk depends on). tig has numerous limitations, it cannot display octopus merges or octopus branching. As of git 1.5.6, there are still no other Unicode-output programs known to me.</p>
<h3>A bit of internals</h3>
<p> git-forest originally was a zero-lookahead visualizer, i.e. branches were accomodated when they have first been seen. Since mid-June 2008, git-forest has a lookahead tunable that controls how long an inter-merge vine (a branch in the graphical sense) can be.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd> Display author for each commit.</p>
<dt><code>&#8211;no-rebase</code></p>
<dd> Do not show the rebase pseudo-refs.</p>
<dt><code>&#8211;style=1</code></p>
<dd> Use single-line visuals (default).</p>
<dt><code>&#8211;style=2</code></p>
<dd> Use double-line visuals.</p>
<dt><code>&#8211;style=10</code></p>
<dd> Use specific rounded Unicode visuals for edges; glyphs might only be available with X11 terminals and appropriate fonts.</p>
<dt><code>&#8211;style=15</code></p>
<dd> Use single bold-line visuals. Not readily usable with VGA console fonts without special unimaps.</p>
<dt><code>&#8211;sha</code></p>
<dd> Display (abbreviated) SHAs for each commit.</p>
<dt><code>&#8211;svdepth=</code><i>depth</i></p>
<dd> This option controls the maximum length of merge subvines. It defaults to 2.</dl>
<p> All other options and arguments are passed down to git-log. Commonly useful options are &#8211;all and &#8211;topo-order.</p>
<h2>Examples</h2>
<pre>
git-forest --all | less -RS
git-forest origin/master | less -RS
</pre>
<p> This tool does not try to minimize the empty space between branches like gitk does. Take it as a feature.</p>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/7-hxtools/">hxtools</a></code>(7) </p>
<h2>Index</h2>
