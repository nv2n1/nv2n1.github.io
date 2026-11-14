---
title: "urxvt-selection-popup(1)"
name: "urxvt-selection-popup"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-selection-popup/"
---

<h2 class="name">NAME</h2>
 

 selection-popup (enabled by default) 

<h2>DESCRIPTION</h2>

 Binds a popup menu to Ctrl-Button3 that lets you paste the X selections and either modify or use the internal selection text in various ways (such as uri unescaping, perl evaluation, web-browser starting etc.), depending on content. 

 Other extensions can extend this popup menu by pushing a code reference onto <tt>&quot;@{ $term-&gt;{selection_popup_hook} }&quot;</tt>, which gets called whenever the popup is being displayed. 

 Its sole argument is the popup menu, which can be modified. The selection is in <tt>$_</tt>, which can be used to decide whether to add something or not. It should either return nothing or a string and a code reference. The string will be used as button text and the code reference will be called when the button gets activated and should transform <tt>$_</tt>. 

 The following will add an entry <tt>&quot;a to b&quot;</tt> that transforms all <tt>&quot;a&quot;</tt>s in the selection to <tt>&quot;b&quot;</tt>s, but only if the selection currently contains any <tt>&quot;a&quot;</tt>s: 

 <pre><code>
push @{$self-&gt;{term} {selection_popup_hook}}, sub{
                                                  / a / ? ("a to b" = &gt; sub{s / a / b / g}
                                                           : ()};
</code></pre> 

<h2>Index</h2>


