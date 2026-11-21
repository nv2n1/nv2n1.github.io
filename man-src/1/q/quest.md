---

title: "quest(1)"
name: "quest"
section: "1"
letter: "q"
url: "/docs/linux/man/1-quest/"
description: "quest – Xapian command line search tool"
---

<p> quest &#8211; Xapian command line search tool</p>
<h2>SYNOPSIS</h2>
<p> <code>quest</code> [<i>OPTIONS</i>] <i>&#8216;QUERY&#8217;</i></p>
<h2>DESCRIPTION</h2>
<p> quest &#8211; Xapian command line search tool </p>
<p> NB: QUERY should be quoted to protect it from the shell.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;db</code>=<i>DIRECTORY</i></dt>
<dd> database to search (multiple databases may be specified)</dd>
<dt><code>-m</code>, <code>&#8211;msize</code>=<i>MSIZE</i></dt>
<dd> maximum number of matches to return</dd>
<dt><code>-c</code>, <code>&#8211;check-at-least</code>=<i>HOWMANY</i></dt>
<dd> minimum number of matches to check</dd>
<dt><code>-s</code>, <code>&#8211;stemmer</code>=<i>LANG</i></dt>
<dd> set the stemming language, the default is &#8216;english&#8217; (pass &#8216;none&#8217; to disable stemming)</dd>
<dt><code>-p</code>, <code>&#8211;prefix</code>=<i>PFX</i>:TERMPFX</dt>
<dd> add a prefix</dd>
<dt><code>-b</code>, <code>&#8211;boolean-prefix</code>=<i>PFX</i>:TERMPFX</dt>
<dd> add a boolean prefix</dd>
<dt><code>-f</code>, <code>&#8211;flags</code>=<i>FLAG1[</i>,FLAG2]&#8230;</dt>
<dd> specify QueryParser flags. Valid flags: auto_multiword_synonyms, auto_synonyms, boolean, boolean_any_case, cjk_ngram, default, lovehate, partial, phrase, pure_not, spelling_correction, synonym, wildcard</dd>
<dt><code>-o</code>, <code>&#8211;default-op</code>=<i>OP</i></dt>
<dd> specify QueryParser default operator (default: or). Valid operators: and, elite_set, near, or, phrase, synonym</dd>
<dt><code>-w</code>, <code>&#8211;weight</code>=<i>SCHEME</i></dt>
<dd> specify weighting scheme to use (default: bm25). Valid schemes: bm25, bool, trad</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
