---
title: "lexnames(5)"
name: "lexnames"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lexnames/"
description: "lexnames – List of WordNet lexicographer file names and numbers"
---

<p>lexnames &#8211; List of WordNet lexicographer file names and numbers</p>
<h2>Description</h2>
<p>During WordNet development synsets are organized into forty-five lexicographer files based on syntactic category and logical groupings. <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) processes these files and produces a database suitable for use with the WordNet library, interface code, and other applications. The format of the lexicographer files is described in <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5). </p>
<p> A file number corresponds to each lexicographer file. File numbers are encoded in several parts of the WordNet system as an efficient way to indicate a lexicographer file name. The file <code>lexnames</code> lists the mapping between file names and numbers, and can be used by programs or end users to correlate the two.</p>
<h3>File Format</h3>
<p>Each line in <code>lexnames</code> contains 3 tab separated fields, and is terminated with a newline character. The first field is the two digit decimal integer file number. (The first file in the list is numbered <code>00</code>.) The second field is the name of the lexicographer file that is represented by that number, and the third field is an integer that indicates the syntactic category of the synsets contained in the file. This is simply a shortcut for programs and scripts, since the syntactic category is also part of the lexicographer file&#8217;s name.</p>
<h3>Syntactic Category</h3>
<p>The syntactic category field is encoded as follows: </p>
<dl>
<dd>
<pre><code>1</code> NOUN
<code>2</code> VERB
<code>3</code> ADJECTIVE
<code>4</code> ADVERB</pre>
</dl>
<h3>Lexicographer Files</h3>
<p>The names of the lexicographer files and their corresponding file numbers are listed below along with a brief description each file&#8217;s contents. </p>
<dl>
<dd><center></p>
<table>
<tr VALIGN=top>
<td><code>File Number</code></td>
<td><code>Name</code></td>
<td><code>Contents</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>00</td>
<td>adj.all</td>
<td>all adjective clusters
</td>
</tr>
<tr VALIGN=top>
<td>01</td>
<td>adj.pert</td>
<td>relational adjectives (pertainyms)
</td>
</tr>
<tr VALIGN=top>
<td>02</td>
<td>adv.all</td>
<td>all adverbs
</td>
</tr>
<tr VALIGN=top>
<td>03</td>
<td>noun.Tops</td>
<td>unique beginner for nouns
</td>
</tr>
<tr VALIGN=top>
<td>04</td>
<td>noun.act</td>
<td>nouns denoting acts or actions
</td>
</tr>
<tr VALIGN=top>
<td>05</td>
<td>noun.animal</td>
<td>nouns denoting animals
</td>
</tr>
<tr VALIGN=top>
<td>06</td>
<td>noun.artifact</td>
<td>nouns denoting man-made objects
</td>
</tr>
<tr VALIGN=top>
<td>07</td>
<td>noun.attribute</td>
<td>nouns denoting attributes of people and objects
</td>
</tr>
<tr VALIGN=top>
<td>08</td>
<td>noun.body</td>
<td>nouns denoting body parts
</td>
</tr>
<tr VALIGN=top>
<td>09</td>
<td>noun.cognition</td>
<td>nouns denoting cognitive processes and contents
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>noun.communication</td>
<td>nouns denoting communicative processes and contents
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>noun.event</td>
<td>nouns denoting natural events
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td>noun.feeling</td>
<td>nouns denoting feelings and emotions
</td>
</tr>
<tr VALIGN=top>
<td>13</td>
<td>noun.food</td>
<td>nouns denoting foods and drinks
</td>
</tr>
<tr VALIGN=top>
<td>14</td>
<td>noun.group</td>
<td>nouns denoting groupings of people or objects
</td>
</tr>
<tr VALIGN=top>
<td>15</td>
<td>noun.location</td>
<td>nouns denoting spatial position
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td>noun.motive</td>
<td>nouns denoting goals
</td>
</tr>
<tr VALIGN=top>
<td>17</td>
<td>noun.object</td>
<td>nouns denoting natural objects (not man-made)
</td>
</tr>
<tr VALIGN=top>
<td>18</td>
<td>noun.person </td>
<td>nouns denoting people
</td>
</tr>
<tr VALIGN=top>
<td>19</td>
<td>noun.phenomenon</td>
<td>nouns denoting natural phenomena
</td>
</tr>
<tr VALIGN=top>
<td>20</td>
<td>noun.plant</td>
<td>nouns denoting plants
</td>
</tr>
<tr VALIGN=top>
<td>21</td>
<td>noun.possession</td>
<td>nouns denoting possession and transfer of possession
</td>
</tr>
<tr VALIGN=top>
<td>22</td>
<td>noun.process</td>
<td>nouns denoting natural processes
</td>
</tr>
<tr VALIGN=top>
<td>23</td>
<td>noun.quantity</td>
<td>nouns denoting quantities and units of measure
</td>
</tr>
<tr VALIGN=top>
<td>24</td>
<td>noun.relation</td>
<td>nouns denoting relations between people or things or ideas
</td>
</tr>
<tr VALIGN=top>
<td>25</td>
<td>noun.shape</td>
<td>nouns denoting two and three dimensional shapes
</td>
</tr>
<tr VALIGN=top>
<td>26</td>
<td>noun.state</td>
<td>nouns denoting stable states of affairs
</td>
</tr>
<tr VALIGN=top>
<td>27</td>
<td>noun.substance</td>
<td>nouns denoting substances
</td>
</tr>
<tr VALIGN=top>
<td>28</td>
<td>noun.time</td>
<td>nouns denoting time and temporal relations
</td>
</tr>
<tr VALIGN=top>
<td>29</td>
<td>verb.body</td>
<td>verbs of grooming, dressing and bodily care
</td>
</tr>
<tr VALIGN=top>
<td>30</td>
<td>verb.change</td>
<td>verbs of size, temperature change, intensifying, etc.
</td>
</tr>
<tr VALIGN=top>
<td>31</td>
<td>verb.cognition</td>
<td>verbs of thinking, judging, analyzing, doubting
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td>verb.communication</td>
<td>verbs of telling, asking, ordering, singing
</td>
</tr>
<tr VALIGN=top>
<td>33</td>
<td>verb.competition</td>
<td>verbs of fighting, athletic activities
</td>
</tr>
<tr VALIGN=top>
<td>34</td>
<td>verb.consumption</td>
<td>verbs of eating and drinking
</td>
</tr>
<tr VALIGN=top>
<td>35</td>
<td>verb.contact</td>
<td>verbs of touching, hitting, tying, digging
</td>
</tr>
<tr VALIGN=top>
<td>36</td>
<td>verb.creation</td>
<td>verbs of sewing, baking, painting, performing
</td>
</tr>
<tr VALIGN=top>
<td>37</td>
<td>verb.emotion</td>
<td>verbs of feeling
</td>
</tr>
<tr VALIGN=top>
<td>38</td>
<td>verb.motion</td>
<td>verbs of walking, flying, swimming
</td>
</tr>
<tr VALIGN=top>
<td>39</td>
<td>verb.perception</td>
<td>verbs of seeing, hearing, feeling
</td>
</tr>
<tr VALIGN=top>
<td>40</td>
<td>verb.possession</td>
<td>verbs of buying, selling, owning
</td>
</tr>
<tr VALIGN=top>
<td>41</td>
<td>verb.social</td>
<td>verbs of political and social activities and events
</td>
</tr>
<tr VALIGN=top>
<td>42</td>
<td>verb.stative</td>
<td>verbs of being, having, spatial relations
</td>
</tr>
<tr VALIGN=top>
<td>43</td>
<td>verb.weather</td>
<td>verbs of raining, snowing, thawing, thundering
</td>
</tr>
<tr VALIGN=top>
<td>44</td>
<td>adj.ppl</td>
<td>participial adjectives
</td>
</tr>
</table>
<p></center></dl>
<h2>Notes</h2>
<p>The lexicographer files are not included in the WordNet database package.</p>
<h2>Environment Variables (Unix)</h2>
<dl>
<dt><code>WNHOME</code></p>
<dd>Base directory for WordNet. Default is <code>/usr/local/WordNet-3.0</code>.</p>
<dt><code>WNSEARCHDIR</code></p>
<dd>Directory in which the WordNet database has been installed. Default is <code>WNHOME/dict</code>.</dl>
<h2>Registry (Windows)</h2>
<dl>
<dt><code>HKEY_LOCAL_MACHINE\SOFTWARE\WordNet\3.0\WNHome</code></p>
<dd>Base directory for WordNet. Default is <code>C:\Program~Files\WordNet\3.0</code>.</dl>
<h2>Files</h2>
<dl>
<dt><code>lexnames</code></p>
<dd>list of lexicographer file names and numbers</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grind/">grind</a></code>(1), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5). </p>
