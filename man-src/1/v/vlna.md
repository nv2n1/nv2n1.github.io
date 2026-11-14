---
title: "vlna(1)"
name: "vlna"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vlna/"
description: "vlna – adds tilde after each non-syllabic preposition"
---

<h2 class="name">NAME</h2>
<p> vlna &#8211; adds tilde after each non-syllabic preposition </p>
<h2>USAGE</h2>
<p> <code>vlna</code> [<i>options</i>] [<i>filenames</i>]</p>
<h2>PREFACE</h2>
<p> There exists a special Czech and Slovak typographical rule: you cannot leave the non-syllabic preposition on the end of one line and continue writting text on next line. For example, you cannot write down the text &quot;v lese&quot; (in a forest) like &quot;v&lt;new-line&gt;lese&quot;. The program vlna adds the asciitilde between such preposition and the next word and removes the space(s) in this place. It means, the program converts &quot;v lese&quot; to &quot;v~lese&quot;. You can use this program as a preporcessor before TeXing. Moreower, you can set another sequence to store instead asciitilte (see the <code>-x</code> option).</p>
<h2>DESCRIPTION</h2>
<p> The program <code>vlna</code> processes one or more files, searches the non-syllabic prepositions followed by space(s) in these files and converts this/these space(s) to asciitilde for each such occurrence. </p>
<p> In the processed file, the activity of the program can be blocked by <code>%~-</code> sequence and the activity can be restored again by the <code>%~+</code> sequence. These sequences can include spaces, it means that <code>% ~-</code> is a correct sequence too. </p>
<p> The rule to recognize a preposition follows: The arbitrary number of opening parentheses can be written before the preposition and before these (optional) parentheses must be the space, tabelator or new-line. The preposition itself is one-letter word, the letters have to be from this set: {KkSsVvZzOoUuAI}. See the <code>-v</code> option if you want to change this set of letters. From version 1.2, the TeX sequence can be written before preposition and before the brace. Example: &quot;&lt;new-line&gt;([V lese&quot; is converted to &quot;&lt;new-line&gt;([V~lese&quot;. Another example: &quot;
