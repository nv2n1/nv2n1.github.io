---
title: "urxvt-option-popup(1)"
name: "urxvt-option-popup"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-option-popup/"
---

<h2 class="name">NAME</h2>
 

 option-popup - option menu (enabled by default) 

<h2>DESCRIPTION</h2>

 Binds a popup menu to Ctrl-Button2 that lets you toggle (some) options at runtime. 

 Other extensions can extend this popup menu by pushing a code reference onto <tt>&quot;@{ $term-&gt;{option_popup_hook} }&quot;</tt>, which gets called whenever the popup is being displayed. 

 Its sole argument is the popup menu, which can be modified. It should either return nothing or a string, the initial boolean value and a code reference. The string will be used as button text and the code reference will be called when the toggle changes, with the new boolean value as first argument. 

 The following will add an entry <tt>&quot;myoption&quot;</tt> that changes <tt>&quot;$self-&gt;{myoption}&quot;</tt>: 

 <pre><code>
push @{$self-&gt;{term} {option_popup_hook}}, sub{
                                               ("my option" = &gt; $myoption, sub{$self-&gt;{myoption} = $_[0]})};
</code></pre> 

<h2>Index</h2>


