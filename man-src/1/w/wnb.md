---
title: "wnb(1)"
name: "wnb"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wnb/"
description: "wnb – WordNet window-based browser interface"
---

<h2>NAME</h2>
<p> wnb &#8211; WordNet window-based browser interface</p>
<h2>SYNOPSIS</h2>
<p> <code>wnb</code></p>
<h2>DESCRIPTION</h2>
<p> <code>wnb()</code> provides a window-based interface for browsing the WordNet database, allowing synsets and relations to be displayed as formatted text. For each search word, different searches are available based on syntactic category and information available in the database. </p>
<p> <code>wnb</code> is written in Tcl/Tk, which is available for Unix and Windows platforms. This allows the same code to work on all supported WordNet platforms without modification.</p>
<h2>WNB WINDOWS</h2>
<p> <code>wnb()</code> was developed with the philosophy that only those searches and buttons that are applicable at the current time are displayed. As a result, the appearance of the interface changes as it is used. Use the standard windowing system mouse functions to open and close the WordNet Browser Window, move the window, and change its size. </p>
<p> The WordNet Browser Window contains the following areas, from top to bottom:</p>
<dl>
<dt>Menubar</p>
<dd> A menubar runs along the top of the browser window with pulldown menus and button entitled <code>File</code>, <code>History</code>, <code>Options</code>, and <code>Help</code>.</p>
<dt>Search Word Entry</p>
<dd> Below the Menubar is a line for entering the search word. A search word can be a single word, hyphenated string, or a collocation. Case is ignored. Although only uninflected forms of words are usually stored in WordNet, users may search for inflected forms. WordNet&#8217;s morphological processor finds the base form automatically.</p>
<dt>Search Selection</p>
<dd> Below the Search Word Entry line is an area for selecting the search type and senses to search. Until a search word is entered this area is blank. After a search word is entered, buttons appear corresponding to each syntactic category (<code>Noun</code>, <code>Verb</code>, <code>Adjective</code>, <code>Adverb</code>) in which the search string is defined in WordNet. </p>
<p> At the right edge of the Search Selection line is a box for entering sense numbers. When this box is empty, search results for all senses of the search word that match the search type are displayed. The search may be restricted to one or more specific senses by entering a comma or space separated list of sense numbers in the <code>Senses</code> box. These sense numbers remain in effect until either the user changes or deletes them, or a new search word is entered.</p>
<dt>Results Window</p>
<dd> Most of the browser window consists of a large text buffer for displaying the results of WordNet searches. Horizontal and vertical scroll bars are present for scrolling through the output.</p>
<dt>Status Line</p>
<dd> A status line is at the bottom of the browser window. When search results are displayed in the Results Window, this status line reflects the type of search selected. When there is no search word entered, your are prompted to <code>&quot;Enter search word and press return.&quot;</code> If the search word entered is not in WordNet, the message <code>&quot;Sorry, no matches found.&quot;</code> is displayed.</dl>
<h2>SEARCHING THE DATABASE</h2>
<p> The WordNet browser navigates through WordNet in two steps. First a search word is entered and an overview of all the senses of the word in all syntactic categories is displayed in the Results Window. The senses are grouped by syntactic category, and each synset is annotated as described above with <i>synset_offset</i>, <i>lex_filename</i>, and <i>sense_number</i> as dictated by the advanced search options set. The overview search also indicates how many of the senses in each syntactic category are represented in the tagged texts. This is a way for the user to determine whether a sense&#8217;s sense number is based on semantic tagging data, or was arbitrarily assigned. For each sense that has appeared in such texts, the number of semantic tags to that sense are indicated in parentheses after the sense number. </p>
<p> Then, within a syntactic category, a specific search is selected. The desired search is performed and the search results are displayed in the Results Window. Additional searches on the same word can be performed, or a new search word can be entered. </p>
<p> To enter a search word, click the mouse in the horizontal box labeled <code>Search Word</code>, type a single word, hyphenated string, or collocation and press <font SIZE="-1"><code>RETURN.</code></font> </p>
<p> <code>wnb()</code> responds by making a set of Part of Speech buttons appear in the Search Selection line. Each button corresponds to a syntactic category in which the search string is defined in WordNet. At the same time, an Overview of the synsets for all senses of the search word is displayed in the Results Window. The Overview includes the gloss for each synset and also indicates which of the senses have appeared in the semantically tagged texts. For each sense that has appeared in such texts, the number of semantic tags to that sense are indicated in parentheses after the sense number. </p>
<p> The pulldown menus in the Search Selection line list all of the WordNet searches that can be performed for the search word in that part of speech. To select a search, highlight it by dragging the mouse to it, and release the mouse while it is highlighted. Drag the mouse outside of the pulldown list and release to hide the menu without making a selection. Dragging the mouse across the Part of Speech buttons displays the available searches for each syntactic category. </p>
<p> To restrict a search to one or more senses within a syntactic category, enter a comma or space separated list of sense numbers in the <code>Senses</code> box before selecting a search. </p>
<p> After a search is selected, <code>wnb()</code> performs the search on the WordNet database and displays the formatted results in the Results Window. Whenever search results are displayed, a button entitled <code>Redisplay Overview</code> is present at the right edge of the Search Word Entry line. Clicking on this button redisplays the Overview of all synsets for the search word in the Results Window.</p>
<h3>Changing the Search Word</h3>
<p> A new search word can be entered at any time by moving to the Search Word Entry box, if necessary highlighting it by clicking, erasing the old string, typing a new one and pressing <font SIZE="-1"><code>RETURN.</code></font> The <code>Senses</code> box is cleared if necessary, the Part of Speech buttons applicable to the new search word appear, and the Overview for the new search word is displayed. </p>
<p> The middle mouse button can also be used to select a new search word by placing the mouse over any word in the Results Window and clicking. The selected word will replace the text in the Search Word Entry box, and the overview for that word will automatically be displayed. </p>
<p> To select a new search string collocation from text in the Results Window, highlight the text with the mouse and press <font SIZE="-1"><code>CONTROL-S.</code></font> </p>
<h3>Interrupting a Search</h3>
<p> When a search is in progress the message <code>&quot;Searching&#8230;(press escape to abort)&quot;</code> is displayed in the Status Line. Note that most searches return very quickly, so this message isn&#8217;t noticeable. As indicated, pressing the <font SIZE="-1"><code>ESCAPE</code></font> key will interrupt the search. The results of the search obtained before the time the search was interrupted are displayed in the Results Window.</p>
<h2>MENUS</h2>
<h3>File Menu</h3>
<dl>
<dt>
<dd>
<dl>
<dt>Find keywords by substring</p>
<dd> Display a popup window for specifying a search of WordNet for words or collocations that contain a specific substring. If a search word is currently entered in the <code>Search Word</code> box, it is used as the substring to search for by default. The Substring Search Window contains a box for entering a substring, a pulldown menu to its right for specifying the part of speech to search, a large area for displaying the search results, and action buttons at the bottom entitled <code>Search</code>, <code>Save</code>, <code>Print</code> <code>Dismiss</code>. </p>
<p> Once a substring is entered and a part of speech selected, clicking on the <code>Search</code> button causes a search to be done for all words and collocations in WordNet, in that syntactic category, that contain the substring according to the following criteria: </p>
<p> 1. The substring can appear at the beginning or end of a word, hyphenated string o collocation. </p>
<p> 2. The substring can appear in the middle of a hyphenated string or collocation, but only delimited on both sides by spaces or hyphens. </p>
<p> The search results are displayed in the large buffer. Clicking on an item from the search results list causes <code>wnb()</code> to automatically enter that word in the <code>Search Word</code> box of the WordNet Browser Window and perform the Overview search. </p>
<p> Clicking the <code>Save</code> button generates a popup dialog for specifying a filename to save the substring search results to. Clicking the <code>Print</code> button generates a popup dialog in which a print command can be specified. </p>
<p> Selecting <code>Dismiss</code> closes the Substring Search Window.</p>
<dt>Save current display</p>
<dd> Display a popup dialog for specifying a filename to save the current Results Window contents to.</p>
<dt>Print current display</p>
<dd> Display a popup dialog in which to specify a print command to which the current Results Window contents can be piped. Note &#8211; this option does not exist in the Windows version.</p>
<dt>Clear current display</p>
<dd> Clear the <code>Search Word</code> and <code>Senses</code> boxes, and Results Window.</p>
<dt>Exit</p>
<dd> Does what you would expect.</dl>
</dl>
<h3>History</h3>
<p> This pulldown menu contains a list of the last searches performed. Selecting an item from this list performs that search again. The maximum number of searches stored in the list can be adjusted from the <code>Options</code> menu. The default is 10.</p>
<h3>Options</h3>
<dl>
<dt>
<dd>
<dl>
<dt>Show help with each search</p>
<dd> When this checkbox is selected search results are preceded by some explanatory text about the type of search selected. This is off by default.</p>
<dt>Show descriptive gloss</p>
<dd> When this checkbox is selected, synset glosses are displayed in all search results. This is set by default. Note that glosses are always displayed in the Overview.</p>
<dt>Wrap Lines</p>
<dd> When this checkbox is selected, lines in the Results Window that are wider than the window are automatically wrapped. This is set by default. If not selected, a horizontal scroll bar is present if any lines are longer than the width of the window.</p>
<dt>Set advanced search options&#8230;</p>
<dd> Selecting this item displays a popup window for setting the following search options: <code>Lexical file information; Synset location in database file; Sense number</code>. Choices for each are: </p>
<pre>
        <code>Don't show</code> (default)
        <code>Show with searches</code>
        <code>Show with searches and overview</code>
</pre>
<p> When lexical file information is shown, the name of the lexicographer file is printed before each synset, enclosed in angle brackets (<code>&lt;~~</code><i>&#8230;</i><code>~~&gt;</code>). When both lexical file information and synset location information are displayed, the synset location information appears first. If within one lexicographer file more than one sense of a word is entered, an integer <i>lex_id</i> is appended onto all but one of the word&#8217;s instances to uniquely identify it. In each synset, each word having a non-zero <i>lex_id</i> is printed with the <i>lex_id</i> value printed immediately following the word. If both lexicographer information and sense numbers are displayed, <i>lex_id</i>s, if present, precede sense numbers. </p>
<p> When synset location is shown, the byte offset of the synset in the database &quot;data&quot; file corresponding to the syntactic category of the synset is printed before each synset, enclosed in curly braces (<code>{~~</code><i>&#8230;</i><code>~~}</code>). When both lexical file information and synset location information are displayed, the synset location information appears first. </p>
<p> When sense numbers are shown, the sense number of each word in each synset is printed immediately after the word, and is preceded by a number sign (<code>#</code>).</p>
<dt>Set maximum history length&#8230;</p>
<dd> Display a popup dialog in which the maximum number of previous searches to be kept on the History list can be set.</p>
<dt>Set font&#8230;~~~~~~~~~~~</p>
<dd> Display a popup window for setting the font (typeface) and font size to use for the Results Window. Choices for typeface are: <code>Courier</code>, <code>Helvetica</code>, and <code>Times</code> (default). Font size can be <code>small</code>, <code>medium</code> (default), or <code>large</code>.</p>
<dt>Save current options as default</p>
<dd> Save the currently set options. Next time the browser is started, these options will be used as the user defaults.</dl>
</dl>
<h3>Help</h3>
<dl>
<dt>
<dd>
<dl>
<dt>Help on using the WordNet browser</p>
<dd> Display this manual page.</p>
<dt>Help on WordNet terminology</p>
<dd> Display the <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7) manual page.</p>
<dt>Display the WordNet license</p>
<dd> Display the WordNet copyright notice and license agreement.</p>
<dt>About the WordNet browser</p>
<dd> Information about this application.</dl>
</dl>
<h2>SHORCUTS</h2>
<p> Clicking on any word in the Results Window while holding down the <font SIZE="-1"><code>SHIFT</code></font> key on the keyboard causes the browser to replace <code>Search Word</code> with the word and display its Overview and available searches. Clicking on any word in the Results Window with the middle mouse button does the same thing. </p>
<p> Pressing the <font SIZE="-1"><code>CONTROL-S</code></font> keys causes the browser to do as above on the text that is currently highlighted. Under Unix, this will work even if the highlighted text is in another window. This works on hyphenated strings and collocations, as well as individual words. </p>
<p> Pressing the <font SIZE="-1"><code>CONTROL-G </code></font> keys displays the Substring Search Window. </p>
<h2>SEARCH RESULTS</h2>
<p> The results of a search of the WordNet database are displayed in the Results Window. Horizontal and vertical scroll bars are present for scrolling through the search results. </p>
<p> All searches other than the Overview list all senses matching the search results in the following general format. Items enclosed in italicized square brackets (<i>[~&#8230;~]</i>) may not be present. </p>
<p> If a search cannot be performed on some senses of <i>searchstr</i>, the search results are headed by a string of the form: </p>
<pre>
        X of Y senses of <i>searchstr</i>
</pre>
<dl>
<dt>
<dd> One line listing the number of senses matching the search selected. </p>
<p> Each sense matching the search selected displayed as follows: </p>
<pre><code>
Sense n
    [{synset_offset}][&lt;lex_filename&gt;] ~~word1[#sense_number][, ~~word2...]
</code></pre>
<p> Where <i>n</i> is the sense number of the search word, <i>synset_offset</i> is the byte offset of the synset in the <code>data.</code><i>pos</i> file corresponding to the syntactic category, <i>lex_filename</i> is the name of the lexicographer file that the synset comes from, <i>word1</i> is the first word in the synset (note that this is not necessarily the search word) and <i>sense_number</i> is the WordNet sense number assigned to the preceding word. <i>synset_offset</i>, <i>lex_filename</i>, and <i>sense_number</i> are generated if the appropriate Options are specified. </p>
<p> The synsets matching the search selected are printed below each sense&#8217;s synset output described above. Each line of output is preceded by a marker (usually <code>=&gt;</code>), then a synset, formatted as described above. If a search traverses more one level of the tree, then successive lines are indented by spaces corresponding to its level in the hierarchy. Glosses are displayed in parentheses at the end of each synset if the appropriate Option is set. Each synset is printed on one line. </p>
<p> Senses are ordered from most to least frequently used, with the most common sense numbered <code>1</code>. Frequency of use is determined by the number of times a sense is tagged in the various semantic concordance texts. Senses that are not semantically tagged follow the ordered senses. Note that this ordering is only an estimate based on usage in a small corpus. </p>
<p> Verb senses can be grouped by similarity of meaning, rather than ordered by frequency of use. When the <code>&quot;Synonyms, grouped by similarity&quot;</code> search is selected, senses that are close in meaning are printed together, with a line of dashes indicating the end of a group. See <code><a href="/docs/linux/man/7-wngroups/">wngroups</a></code>(7) for a discussion how senses are grouped. </p>
<p> The output of the <code>&quot;Derivationally Related Forms&quot;</code> search shows word forms that are morphologically related to <code>searchstr</code>. Each word form pointed to from <i>searchstr</i> is displayed, preceded by <code>RELATED TO-&gt;</code> and the syntactic category of the link, followed, on the next line, by its synset. Printed after the word form is <code>#</code><i>n</i> where <i>n</i> indicates the WordNet sense number of the term pointed to. </p>
<p> The <code>&quot;Domain&quot;</code> and <code>&quot;Domain Terms&quot;</code> searches show the domain that a synset has been classified in and, conversely, all of the terms that have been assigned to a specific domain. A domain is either a <code>TOPIC,</code> <code>REGION</code> or <code>USAGE,</code> as reflected in the specific pointer character stored in the database, and displayed in the output. A <code>Domain</code> search on a term shows the domain, if any, that each synset containing <i>searchstr</i> has been classified in. The output display shows the domain type (<code>TOPIC,</code> <code>REGION</code> or <code>USAGE</code>), followed by the syntactic category of the domain synset and the terms in the synset. Each term is followed by <code>#</code><i>n</i> where <i>n</i> indicates the WordNet sense number of the term. The converse search, <code>Domain Terms</code>, shows all of the synsets that have been placed into the domain <i>searchstr</i>, with analogous markers. </p>
<p> When the <code>&quot;Sentence Frames&quot;</code> search is specified, sample illustrative sentences and generic sentence frames are displayed. If a sample sentence is found, the base form of the search word is substituted into the sentence, and it is printed below the synset, preceded with the <code>EX:</code> marker. When no sample sentences are found, the generic sentence frames are displayed. Sentence frames that are acceptable for all words in a synset are preceded by the marker <code>*&gt;</code>. If a frame is acceptable for the search word only, it is preceded by the marker <code>=&gt;</code>. </p>
<p> Search results for adjectives are slightly different from those for other parts of speech. When an adjective is printed, its direct antonym, if it has one, is also printed in parentheses. When the search word is in a head synset, all of the head synset&#8217;s satellites are also displayed. The position of an adjective in relation to the noun may be restricted to the <i>prenominal</i>, <i>postnominal</i> or <i>predicative</i> position. Where present, these restrictions are noted in parentheses. </p>
<p> When an adjective is a participle of a verb, the output indicates the verb and displays its synset. </p>
<p> When an adverb is derived from an adjective, the specific adjectival sense on which it is based is indicated. </p>
<p> The morphological transformations performed by the search code may result in more than one word to search for. <code>wnb()</code> automatically performs the requested search on all of the strings and returns the results grouped by word. For example, the verb <code>saw</code> is both the present tense of <code>saw</code> and the past tense of <code>see</code>. When there is more than one word to search for, search results are grouped by word.</dl>
<h2>DIAGNOSTICS</h2>
<p> If the WordNet database files cannot be opened, error messages are displayed. This is usually corrected by setting the environment variables described below to the proper location of the WordNet database for your installation.</p>
<h2>ENVIRONMENT VARIABLES (UNIX)</h2>
<dl>
<dt><code>WNHOME</code></p>
<dd> Base directory for WordNet. Default is <code>/usr/local/WordNet-3.0</code>.</p>
<dt><code>WNSEARCHDIR</code></p>
<dd> Directory in which the WordNet database has been installed. Default is <code>WNHOME/dict</code>.</dl>
<h2>REGISTRY (WINDOWS)</h2>
<dl>
<dt><code>HKEY_LOCAL_MACHINE\SOFTWARE\WordNet\3.0\WNHome</code></p>
<dd> Base directory for WordNet. Default is <code>C:\Program~Files\WordNet\3.0</code>.</p>
<dt><code>HKEY_CURRENT_USER\SOFTWARE\WordNet\3.0\wnres</code></p>
<dd> User&#8217;s default browser options.</dl>
<h2>FILES</h2>
<dl>
<dt><code>index.</code><i>pos</i></p>
<dd> database index files</p>
<dt><code>data.</code><i>pos</i></p>
<dd> database data files</p>
<dt><code>*.vrb</code></p>
<dd> files of sentences illustrating the use of verbs</p>
<dt><i>pos</i>.exc</p>
<dd> morphology exception lists</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wnintro/">wnintro</a></code>(1), <code><a href="/docs/linux/man/1-wn/">wn</a></code>(1), <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5), <code><a href="/docs/linux/man/7-morphy/">morphy</a></code>(7), <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7), <code><a href="/docs/linux/man/7-wngroups/">wngroups</a></code>(7).</p>
<h2>BUGS</h2>
<p> Please reports bugs to wordnet [at] princeton.edu. </p>
<h2>Index</h2>
