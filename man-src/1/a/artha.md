---
title: "artha(1)"
name: "artha"
section: "1"
letter: "a"
url: "/docs/linux/man/1-artha/"
description: "Artha – An cross-platform thesaurus based on WordNet"
---

<h2>NAME</h2>
<p> Artha &#8211; An cross-platform thesaurus based on WordNet</p>
<h2>DESCRIPTION</h2>
<p> <code>Artha</code> is an open thesaurus based on the WordNet database, created with simplicity in mind. Once executed, Artha monitors for a user preset global hotkey combination. When the user selects some text in any window, and presses this hotkey combo, Artha looks up WordNet thesaurus for the selected text and pops-up with the results. </p>
<p> When executed for the first time Artha tries to register a hotkey automatically, in the order, Ctrl + Alt + [W or A or T or Q]. You can view/change it via the &#8216;Hotkey&#8217; button in the toolbar. It can also be disabled.</p>
<h2>DEFINITIONS</h2>
<p> Definitions are categorized based on the PoS (Part of Speech &#8211; Noun, Verb, Adjective and Adverb). Apart from showing the definitions/senses of a searched string with usage examples, Artha also shows a word&#8217;s relatives like Synonyms, Antonyms, Derivatives, Pertainyms (Related noun/verb), Attributes, Similar Terms, Domain/Domain Terms, Causes, Entails, Hypernyms (is a kind of), Hyponyms (Kinds), Holonyms (is a part of), Meronyms (Parts).</p>
<h3>SENSES AND RELATIVES</h3>
<p> A word can have more then one sense i.e. it can convey more than a single meaning/definition. Relative words are words that are related to one or more senses of the searched word, by a relationship like Synonym, Derivative, etc. To know which all sense a relative is related to, just select the it, the corresponding senses it maps to are highlighted. As per WordNet, depending on the number of senses a word has (polysemy count), it&#8217;s familiarity is determined. It gets displayed next to the PoS in the definition area. There are 7 types: extremely rare, very rare, rare, uncommon, common, familiar, very familiar and extremely familiar.</p>
<h2>MODES</h2>
<p> Artha has 2 modes. Simple and Detailed. Artha enters Detailed mode when the &#8216;Detailed&#8217; button in the toolbar is pressed. When toggled again, it returns back to simple mode. For relatives like Antonyms, Pertainyms, Hypernyms, Hyponyms, Holonyms and Meronyms, where more than one level of relatives may be present, is showed in a tree fashion, in detailed mode. If in simple mode, only one level of relatives are shown even when more levels are present. E.g. &#8216;rich&#8217; has &#8216;poor&#8217; and &#8216;lean&#8217; alone as antonyms in simple mode. While in detailed mode, &#8216;poor&#8217; further infers broke, skint, etc. which are shown as children of &#8216;poor&#8217;.</p>
<h2>REGULAR EXPRESSIONS BASED SEARCH</h2>
<p> Regular expressions can be used to search for a term when you vaguely know it and want to locate it in the thesaurus. Artha&#8217;s regular expression pattern closely follows Wildmat syntax by Rich Salz owing to its simplicity.</p>
<dl>
<dt>
<dd> * (wildcard) matches any number of (including 0) unknown characters</p>
<dt>
<dd> ? (joker) matches one unknown character</p>
<dt>
<dd> [&#8230;] (range) matches one unknown character within the range specified</p>
<dt>
<dd> {m, n} (limits) upper &amp; lower limits of the number of characters in a range</p>
<dt>
<dd> [^&#8230;] (not in the range) matches one unknown character NOT within the range specified</p>
<dt>
<dd> EXAMPLES:</p>
<dt>
<dd> Expr. `cro*p` means the term you want to corner starts with `cro` and ends with `p` while the number of characters in between are unknown. It fetches crop, crop up, croup, crock up and crow step.</p>
<dt>
<dd> Expr. `*chester` means the searched word ends with a `chester` while the beginning and its number characters are unknown. It fetches chester, manchester, rochester, winchester and toy manchester.</p>
<dt>
<dd> Expr. `can????r` means the term sought starts with `can` and ends with `r` while you are sure that there are 5 unknown characters in between. It fetches canister and cannular.</p>
<dt>
<dd> Expr. `andre*[x|y|z]` means the word searched for starts with andre and ends with either an x or y or z, and there could be any number of terms in betweem these. It fetches andre malraux, andrei tarkovsky, andres martinez, etc.</p>
<dt>
<dd> Expr. `a[c|d|e]{2,}` means the word looked for starts with a and then there are minimum 2 or more occurances of c, d or e. It fetches acc, accede, ace, add, ade and aec.</p>
<dt>
<dd></dl>
<h2>NOTIFICATIONS</h2>
<p> Should the user prefer passive desktop notifications (balloon tips), rather than the application popping up with the definitions, it can be done by enabling Notifications. This is done via the Notify tool button or by right-clicking on Artha&#8217;s system tray icon, and tick off the &#8216;Notifications&#8217; check box in the menu. When notifications are enabled, and the user selects text in a window and presses the hotkey combo, Artha takes the prime definition of that term from WordNet and shows that definition as a system tray notification. </p>
<p> Note: For the notifications feature to be present, notify library&#8217;s binary (libnotify.so.1) should be available on your system. If not, Artha will not expose the feature at all. Also the notification-daemon should installed for the notifications to show up.</p>
<h2>SUGGESTIONS</h2>
<p> Suggestions is a feature that gives out possible near matches when a misspelled word is searched for. To have this feature, your system should have libenchant binary (libenchant.so.1) installed and an English dict file for the spell engine to refer (locale doesn&#8217;t matter).</p>
<h2>AVAILABILITY</h2>
<p> Artha has a World Wide Web site at <code><a rel="nofollow" href="http://artha.sourceforge.net">http://artha.sourceforge.net</a></code>. From this web site users can know more about the Artha project and also download its source and binary distributions for various distros.</p>
<h2>AUTHOR</h2>
<p> Sundaram Ramaswamy &lt;legends2k [at] yahoo.com&gt; </p>
<h2>Index</h2>
