---
title: "urxvt256c-ml-searchable-scrollback(1)"
name: "urxvt256c-ml-searchable-scrollback"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml-searchable-scrollback/"
---

<h2 class="name">NAME</h2>
 

 searchable-scrollback - incremental scrollback search (enabled by default) 

<h2>DESCRIPTION</h2>

 Adds regex search functionality to the scrollback buffer, triggered by the <tt>&quot;searchable-scrollback:start&quot;</tt> action (bound to <tt>&quot;M-s&quot;</tt> by default). While in search mode, normal terminal input/output is suspended and a regex is displayed at the bottom of the screen. 

 Inputting characters appends them to the regex and continues incremental search. <tt>&quot;BackSpace&quot;</tt> removes a character from the regex, <tt>&quot;Up&quot;</tt> and <tt>&quot;Down&quot;</tt> search upwards/downwards in the scrollback buffer, <tt>&quot;End&quot;</tt> jumps to the bottom. <tt>&quot;Escape&quot;</tt> leaves search mode and returns to the point where search was started, while <tt>&quot;Enter&quot;</tt> or <tt>&quot;Return&quot;</tt> stay at the current position and additionally stores the first match in the current line into the primary selection if the <tt>&quot;Shift&quot;</tt> modifier is active. 

 The regex defaults to ``(?i)'', resulting in a case-insensitive search. To get a case-sensitive search you can delete this prefix using <tt>&quot;BackSpace&quot;</tt> or simply use an uppercase character which removes the ``(?i)'' prefix. 

 See perlre for more info about perl regular expression syntax. 

<h2>Index</h2>


